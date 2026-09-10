#!/usr/bin/env python3
"""Public package surface (FR-004, FR-006b). Idempotent: writes a fixed file.

Runs last so it can re-export everything the earlier patches added. ``__version__`` is read from the
durable VERSION file rather than written as a placeholder: a placeholder would make this patch
non-idempotent, because re-applying it would reset a version generate.sh had already written.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
INIT = ROOT / "flat_api" / "__init__.py"
VERSION_FILE = ROOT / "VERSION"
version = VERSION_FILE.read_text().strip() if VERSION_FILE.is_file() else "0.0.0"

# Keep the generator's model and API re-exports; prepend the ergonomic surface.
generated = INIT.read_text() if INIT.is_file() else ""
marker = "# --- flat_api ergonomic surface (tools/patches/90_exports.py) ---"
if marker in generated:
    generated = generated.split(marker, 1)[1].split("# --- end ---", 1)[-1]
# The preserved tail already starts with a newline; the template supplies its own, so without this
# a blank line accumulates on every run and the patch is not idempotent (FR-025).
generated = generated.lstrip("\n")

INIT.write_text(
    f'''"""Flat API client.

    from flat_api import FlatClient
    client = FlatClient(access_token="...")

Async:

    from flat_api import AsyncFlatClient
    client = AsyncFlatClient(access_token="...")
"""

{marker}
__version__ = "{version}"

from flat_api.client import AsyncFlatClient, FlatClient
from flat_api.errors import (
    FlatAuthenticationError,
    FlatAuthorizationError,
    FlatError,
    FlatNotFoundError,
    FlatQuotaError,
    FlatRateLimitError,
    FlatServerError,
    FlatValidationError,
)
from flat_api.oauth import OAuth2Helper, Tokens
from flat_api.pagination import paginate
from flat_api._retry import RetryPolicy

__all__ = [
    "AsyncFlatClient",
    "FlatClient",
    "FlatAuthenticationError",
    "FlatAuthorizationError",
    "FlatError",
    "FlatNotFoundError",
    "FlatQuotaError",
    "FlatRateLimitError",
    "FlatServerError",
    "FlatValidationError",
    "OAuth2Helper",
    "RetryPolicy",
    "Tokens",
    "paginate",
    "__version__",
]
# --- end ---
{generated}'''
)
print("    exports: rewrote flat_api/__init__.py")
