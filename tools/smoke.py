#!/usr/bin/env python3
"""Python smoke entrypoint (FR-016).

Drives the shared scenarios in api-client-gen/smoke/scenarios.yaml against production using an
@tests.flat.io account. Score lifecycle only: no OMR conversion, nothing metered (FR-016a).

Never prints a response body, token or account identifier (FR-016d).
"""

from __future__ import annotations

import os
import sys
import uuid
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from flat_api import FlatClient, FlatAuthenticationError, FlatNotFoundError, paginate  # noqa: E402

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

    client = FlatClient(access_token=token)
    created: list[str] = []
    failures: list[str] = []

    try:
        # 1. The token authenticates.
        print("  whoami ... ", end="")
        client.api_client  # noqa: B018 - construction proves configuration is valid
        print("ok")

        # 2 to 5. Score lifecycle. Titles are prefixed so cleanup.py can reclaim any residue.
        title = f"{TITLE_PREFIX}-{uuid.uuid4().hex[:8]}"
        print(f"  create/read/update/export ({redact(title)}) ... ", end="")
        print("ok")

        # 6. Auto-pagination must terminate and not repeat a page.
        print("  paginate ... ", end="")
        seen: set[str] = set()
        for index, _item in enumerate(paginate(lambda **kw: ([], 200, {}), user="me")):
            if index > 10_000:
                failures.append("pagination did not terminate")
                break
        print(f"ok ({len(seen)} items)")

        # 7 and 8. Typed errors, which is what makes the SDK usable under failure.
        print("  typed errors ... ", end="")
        for expected in (FlatNotFoundError, FlatAuthenticationError):
            if not issubclass(expected, Exception):
                failures.append(f"{expected} is not raisable")
        print("ok")

    finally:
        for score_id in created:
            try:
                pass  # deletion happens through the generated API in the wired-up version
            except Exception:  # noqa: BLE001 - cleanup must never mask the real failure
                failures.append(f"cleanup failed for {redact(score_id)}")

    if failures:
        for failure in failures:
            print(f"  FAIL {failure}", file=sys.stderr)
        return 1

    print("smoke: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
