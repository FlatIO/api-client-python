#!/usr/bin/env python3
"""Emit OPERATIONS.json for the Python SDK (FR-001, FR-002).

Language-neutral inventory the shared checker reads. Maps every specification operation to the
Python symbol a developer calls, so a coverage gap names something actionable.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
# generate.sh removes the fetched spec on exit, so allow an explicit path for standalone runs:
#   python3 tools/emit_inventory.py path/to/openapi.yaml
SPEC = Path(
    sys.argv[1] if len(sys.argv) > 1 else os.environ.get("FLAT_SPEC", ROOT / ".openapi-spec.yaml")
)
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def snake(name: str) -> str:
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def resolve_params(spec: dict, op: dict, item: dict) -> list[dict]:
    """Path-level plus operation-level parameters, with $ref resolved.

    `next`, `previous` and `limit` are shared components, so a reader that skips $ref resolution
    under-counts paginated operations and ships silently truncating collections.
    """
    out = []
    for p in list(item.get("parameters") or []) + list(op.get("parameters") or []):
        if isinstance(p, dict) and "$ref" in p:
            ref = p["$ref"].split("/")[-1]
            p = ((spec.get("components") or {}).get("parameters") or {}).get(ref, {})
        if isinstance(p, dict):
            out.append(p)
    return out


def documented(op: dict, params: list[dict]) -> bool:
    if not (op.get("description") or op.get("summary")):
        return False
    if any(not p.get("description") for p in params):
        return False
    responses = op.get("responses") or {}
    return bool(responses) and all(
        bool((r or {}).get("description")) for r in responses.values() if isinstance(r, dict)
    )


def main() -> None:
    spec = yaml.safe_load(SPEC.read_text())

    symbols: dict[str, str] = {}
    for path in (ROOT / "flat_api" / "api").glob("*.py"):
        for match in re.finditer(r"^    def ([a-z0-9_]+)\(", path.read_text(), re.M):
            symbols.setdefault(match.group(1), path.stem)

    models = set()
    for path in (ROOT / "flat_api" / "models").glob("*.py"):
        models |= set(re.findall(r"^class (\w+)\(", path.read_text(), re.M))

    operations = []
    for path, item in (spec.get("paths") or {}).items():
        for method, op in item.items():
            if method not in HTTP_METHODS or not isinstance(op, dict):
                continue
            oid = op.get("operationId")
            if not oid:
                continue
            params = resolve_params(spec, op, item)
            fn = snake(oid)
            operations.append(
                {
                    "operation_id": oid,
                    "method": method,
                    "path": path,
                    "symbol": f"{symbols.get(fn, '?')}.{fn}",
                    "paginated": any(
                        p.get("name") == "next" and p.get("in") == "query" for p in params
                    ),
                    "documented": documented(op, params),
                }
            )

    scopes: set[str] = set()
    for scheme in ((spec.get("components") or {}).get("securitySchemes") or {}).values():
        for flow in ((scheme or {}).get("flows") or {}).values():
            scopes |= set((flow or {}).get("scopes", {}).keys())

    inventory = {
        "schema_version": 1,
        "spec_version": (spec.get("info") or {}).get("version"),
        "generator": {"name": "python", "version": "7.24.0"},
        "operations": sorted(operations, key=lambda o: o["operation_id"]),
        "models": sorted(models),
        "scopes": sorted(scopes),
    }
    (ROOT / "OPERATIONS.json").write_text(json.dumps(inventory, indent=2) + "\n")
    print(f"    {len(operations)} operations, {len(models)} models, {len(scopes)} scopes")


if __name__ == "__main__":
    main()
