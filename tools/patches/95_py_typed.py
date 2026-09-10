#!/usr/bin/env python3
"""PEP 561 marker, so consumers actually get the type information (FR-025).

Every model in this client is a fully annotated pydantic class, but without `py.typed` a type
checker in a consumer project treats the whole package as untyped and silently ignores all of it.
The marker has to be recreated here because `flat_api/` is the generated zone: the wipe at the top
of every run removes it, and the generator does not emit one in source-only mode.

Idempotent: writes a zero-byte file that is identical on every run.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PACKAGE = ROOT / "flat_api"

if not PACKAGE.is_dir():
    sys.exit("95_py_typed: flat_api/ is missing, the generated zone was not installed (FR-025)")

(PACKAGE / "py.typed").write_bytes(b"")
print("    py.typed: PEP 561 marker written")
