#!/usr/bin/env python3
"""Flat-branded User-Agent that tracks the package version (FR-013 traceability).

The generator emits `OpenAPI-Generator/<version>/python`, which identifies neither Flat nor this
client: in the API logs it is indistinguishable from any other generated client. Worse, the version
is baked in from generator config, so it drifts from the real package version.

This derives it from `__version__`, so it cannot go stale. The previous generation hard-coded
`flat_api/1.1.0` in generator config and was still claiming 1.1.0 years later.

Idempotent: rewrites to a fixed expression.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TARGET = ROOT / "flat_api" / "api_client.py"

text = TARGET.read_text()

# The generated literal, or our own expression from a previous run.
pattern = re.compile(r"self\.user_agent = (?:'[^']*'|f'[^']*'|_flat_user_agent\(\))")
replacement = "self.user_agent = _flat_user_agent()"

if not pattern.search(text):
    sys.exit("80_user_agent: could not find the user_agent assignment (FR-025)")

text = pattern.sub(replacement, text, count=1)

helper = '''

def _flat_user_agent() -> str:
    """`Flat-SDK-Python/<version> (python/<runtime>)`.

    Derived from the package version so it can never drift from what is published.
    """
    import platform

    from flat_api import __version__

    return (
        f"Flat-SDK-Python/{__version__} (python/{platform.python_version()})"
    )
'''

# Append the helper only if it is not already present anywhere. Checking only the text before the
# assignment would always be true (the helper lives after it) and append a fresh copy every run.
if "def _flat_user_agent" not in text:
    text = text.rstrip() + "\n" + helper

TARGET.write_text(text)
print("    user-agent: Flat-SDK-Python/<version>")
