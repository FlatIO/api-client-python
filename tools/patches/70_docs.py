#!/usr/bin/env python3
"""Verify the generated code actually carries the specification's documentation (FR-004).

emit_inventory.py records what the *specification* documents. That is necessary but not sufficient:
the generator can drop a description on the way through. This checks the generated Python itself and
fails loudly if operation docstrings are missing, so a silent regression in generator configuration
cannot ship an undocumented SDK.

Idempotent: it inspects and reports, it does not rewrite.
"""

from __future__ import annotations

import ast
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
API_DIR = ROOT / "flat_api" / "api"

#: Below this, the generator has stopped propagating descriptions and the config is wrong.
THRESHOLD = 0.95


def main() -> int:
    if not API_DIR.is_dir():
        print("    docs: no generated api/ directory", file=sys.stderr)
        return 1

    total = documented = 0
    undocumented: list[str] = []

    for path in sorted(API_DIR.glob("*.py")):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
                continue
            # The generator emits three variants per operation; check the plain one.
            if node.name.endswith(("_with_http_info", "_without_preload_content")):
                continue
            total += 1
            doc = ast.get_docstring(node)
            if doc and len(doc.strip()) > 20:
                documented += 1
            else:
                undocumented.append(f"{path.stem}.{node.name}")

    if total == 0:
        print("    docs: no operations found to check", file=sys.stderr)
        return 1

    ratio = documented / total
    print(f"    docs: {documented}/{total} operations documented ({ratio:.1%})")

    if ratio < THRESHOLD:
        print(f"    docs: FAIL below {THRESHOLD:.0%} (FR-004)", file=sys.stderr)
        for name in undocumented[:10]:
            print(f"      undocumented: {name}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
