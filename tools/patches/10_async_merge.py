#!/usr/bin/env python3
"""Merge the async generation pass into the package as `flat_api.aio` (FR-005).

The generator emits sync or async but never both (T001 spike), so the async pass is generated as a
separate package and copied to `flat_api/aio`. Its internal absolute imports still reference the
standalone package name and must be rewritten to the subpackage path.

Idempotent: rewriting an already-rewritten import is a no-op.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
AIO = ROOT / "flat_api" / "aio"

if not AIO.is_dir():
    sys.exit("10_async_merge: flat_api/aio missing; the async generation pass did not run")

PATTERNS = (
    (re.compile(r"\bfrom flat_api_async\b"), "from flat_api.aio"),
    (re.compile(r"\bimport flat_api_async\b"), "import flat_api.aio"),
    (re.compile(r"\bflat_api_async\."), "flat_api.aio."),
)

changed = 0
for path in AIO.rglob("*.py"):
    original = path.read_text()
    text = original
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    if text != original:
        path.write_text(text)
        changed += 1

if list(AIO.rglob("*.py")) and "flat_api_async" in (AIO / "__init__.py").read_text():
    sys.exit("10_async_merge: rewrite incomplete, flat_api_async still referenced (FR-025)")

print(f"    async merge: rewrote imports in {changed} file(s)")
