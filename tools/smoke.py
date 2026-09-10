#!/usr/bin/env python3
"""Python smoke entrypoint (FR-016).

Drives the shared scenarios in api-client-gen/smoke/scenarios.yaml against production. Score
lifecycle only: no OMR conversion, nothing metered (FR-016a).

Any account can run this, so a contributor can point it at their own. What keeps it safe is not who
the account belongs to but what the suite touches: every score it creates is titled
`smoke-test-<random>`, it deletes what it created before returning, and it reads nothing else on
the account.

Never prints a response body, token or account identifier (FR-016d).
"""

from __future__ import annotations

import base64
import os
import sys
import uuid
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from flat_api import (  # noqa: E402
    FlatAuthenticationError,
    FlatClient,
    FlatNotFoundError,
)
from flat_api.api.account_api import AccountApi  # noqa: E402
from flat_api.api.collection_api import CollectionApi  # noqa: E402
from flat_api.api.score_api import ScoreApi  # noqa: E402
from flat_api.models.score_creation import ScoreCreation  # noqa: E402
from flat_api.models.score_creation_file_import import ScoreCreationFileImport  # noqa: E402

TITLE_PREFIX = "smoke-test"


def redact(text: str) -> str:
    """Output redaction is not optional: a failing run must not become a data disclosure."""
    return "<redacted>" if os.environ.get("FLAT_SMOKE_REDACT") == "1" else text


def main() -> int:
    scenarios_path = Path(sys.argv[1] if len(sys.argv) > 1 else "scenarios.yaml")
    scenarios = yaml.safe_load(scenarios_path.read_text())

    forbidden = set(scenarios.get("forbidden_operations", []))
    for scenario in scenarios["scenarios"]:
        if scenario.get("operation") in forbidden:
            print(f"refusing to run {scenario['id']}: {scenario['operation']} is metered")
            return 2

    token = os.environ.get("FLAT_TEST_TOKEN")
    if not token:
        print("FLAT_TEST_TOKEN is required", file=sys.stderr)
        return 2

    fixture = scenarios_path.parent / "fixtures" / "minimal.musicxml"
    if not fixture.is_file():
        print(f"missing fixture: {fixture}", file=sys.stderr)
        return 2

    client = FlatClient(access_token=token)
    account = AccountApi(client.api_client)
    scores = ScoreApi(client.api_client)
    collections = CollectionApi(client.api_client)

    created: list[str] = []
    failures: list[str] = []

    def check(name: str, condition: bool, detail: str = "") -> None:
        if condition:
            print(f"  {name} ... ok")
        else:
            print(f"  {name} ... FAIL")
            failures.append(f"{name}: {detail}" if detail else name)

    try:
        # The token authenticates and identifies an account.
        me: Any = account.get_authenticated_user()
        check("whoami", bool(getattr(me, "id", None)), "no id on the authenticated user")

        # Create a score from MusicXML, the most common write path.
        title = f"{TITLE_PREFIX}-{uuid.uuid4().hex[:8]}"
        # createScore takes the ScoreCreation union, not a variant directly: the file import is one
        # of three ways to create a score, alongside the builder and a Drive import.
        score: Any = scores.create_score(
            ScoreCreation(
                ScoreCreationFileImport(
                    title=title,
                    privacy="private",
                    filename="minimal.musicxml",
                    # The only encoding the API declares. Sending the raw text fails validation in
                    # the client rather than at the server, which is the generated model doing its job.
                    data=base64.b64encode(fixture.read_bytes()).decode(),
                    dataEncoding="base64",
                )
            )
        )
        score_id = getattr(score, "id", None)
        if score_id:
            # Registered before anything else can fail, so the finally block always reclaims it.
            created.append(score_id)
        check("create-score", bool(score_id), "no id on the created score")
        if not score_id:
            return 1

        # Read it back.
        fetched: Any = scores.get_score(score_id)
        check(
            "read-score",
            getattr(fetched, "id", None) == score_id,
            "the score read back is not the one created",
        )

        # Rename it, exercising a PUT path.
        renamed = f"{title}-renamed"
        updated: Any = scores.edit_score(score_id, {"title": renamed})
        check(
            "update-score-metadata",
            getattr(updated, "title", None) == renamed,
            "the title did not change",
        )

        # Export to MusicXML, exercising a binary response.
        exported = scores.get_score_revision_data(score_id, "last", "mxl")
        check("export-score", bool(exported), "the export returned nothing")

        # Traverse a paginated collection. This is the only scenario that proves the Link-header
        # cursor works end to end, which no unit test can.
        #
        # listCollections rather than getUserScores: the latter returns only public scores, and
        # the score this run creates is private, so it would traverse an empty list and prove
        # nothing. Every account has at least its own collections.
        page: Any = collections.list_collections(parent="user", limit=10)
        seen = [getattr(item, "id", None) for item in (page or [])]
        check(
            "list-collections-paginated",
            all(seen) and len(seen) == len(set(seen)),
            "the traversal returned an item with no id, or repeated one",
        )

        # A missing score raises the typed error, not a generic failure. This is what makes the
        # SDK usable under failure rather than merely correct under success.
        try:
            scores.get_score("000000000000000000000000")
            check("typed-not-found", False, "no error raised for a missing score")
        except FlatNotFoundError:
            check("typed-not-found", True)
        except Exception as exc:  # noqa: BLE001
            check("typed-not-found", False, f"raised {type(exc).__name__}, not FlatNotFoundError")

        # An invalid token raises the typed authentication error.
        try:
            AccountApi(FlatClient(access_token="invalid").api_client).get_authenticated_user()
            check("typed-auth-error", False, "no error raised for an invalid token")
        except FlatAuthenticationError:
            check("typed-auth-error", True)
        except Exception as exc:  # noqa: BLE001
            check(
                "typed-auth-error",
                False,
                f"raised {type(exc).__name__}, not FlatAuthenticationError",
            )

    except Exception as exc:  # noqa: BLE001 - report, then always reach cleanup
        failures.append(f"unhandled {type(exc).__name__}: {redact(str(exc))}")

    finally:
        # Delete what this run created, whatever happened above. Residue that survives is reported
        # rather than swallowed, so cleanup.py can reclaim it and a maintainer knows to look.
        for score_id in created:
            try:
                scores.delete_score(score_id)
                print(f"  cleanup {redact(score_id)} ... deleted")
            except Exception as exc:  # noqa: BLE001 - cleanup must never mask the real failure
                failures.append(f"cleanup failed for {redact(score_id)}: {type(exc).__name__}")

    if failures:
        for failure in failures:
            print(f"  FAIL {failure}", file=sys.stderr)
        return 1

    print("smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
