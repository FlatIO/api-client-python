#!/usr/bin/env python3
"""Typed error hierarchy keyed on the API's `code` field (FR-006d, FR-006h).

Flat returns {"code", "message", "id"}. Two things make a naive mapping wrong:

  * rate limiting returns 403, not 429, so it shares a status with genuine authorization failures.
    Only the body's `code` separates them.
  * `id` is documented as present only for internal and backend errors, so it cannot be promised
    on every error.

Idempotent: writes a fixed file.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TARGET = ROOT / "flat_api" / "errors.py"

TARGET.write_text('''"""Typed errors for the Flat API.

Branch on the error class, not on the status code: rate limiting and authorization failures both
return HTTP 403 and are separated only by the response body's ``code``.
"""

from __future__ import annotations

from typing import Any, Mapping

__all__ = [
    "FlatError",
    "FlatAuthenticationError",
    "FlatAuthorizationError",
    "FlatRateLimitError",
    "FlatValidationError",
    "FlatNotFoundError",
    "FlatQuotaError",
    "FlatServerError",
    "from_response",
]

RATE_LIMIT_CODE = "API_RATE_LIMIT_EXCEEDED"
QUOTA_CODES = frozenset({"QUOTA_EXCEEDED", "CREDITS_EXHAUSTED", "OMR_CREDITS_EXHAUSTED"})


class FlatError(Exception):
    """Base class for every error raised by this SDK."""

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        code: str | None = None,
        request_id: str | None = None,
        headers: Mapping[str, str] | None = None,
        body: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.code = code
        #: The server-provided error identifier. Present only for internal and backend errors,
        #: so treat it as optional and quote it to support when you have it.
        self.request_id = request_id
        self.headers = dict(headers or {})
        self.body = body

    def __str__(self) -> str:
        parts = [self.message]
        if self.code:
            parts.append(f"code={self.code}")
        if self.status is not None:
            parts.append(f"status={self.status}")
        if self.request_id:
            parts.append(f"id={self.request_id}")
        return " ".join(parts)


class FlatAuthenticationError(FlatError):
    """The token is missing, invalid or expired, or a refresh failed. Re-authorize."""


class FlatAuthorizationError(FlatError):
    """Authenticated but not permitted: a missing scope or insufficient permission."""


class FlatRateLimitError(FlatError):
    """The account or IP exceeded its request quota. Returned as HTTP 403, not 429."""

    def __init__(self, message: str, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.limit = _int_header(self.headers, "X-RateLimit-Limit")
        self.remaining = _int_header(self.headers, "X-RateLimit-Remaining")
        #: UTC epoch seconds at which the window resets. Flat sends no Retry-After header.
        self.reset = _int_header(self.headers, "X-RateLimit-Reset")


class FlatValidationError(FlatError):
    """The request body or parameters failed validation."""


class FlatNotFoundError(FlatError):
    """The resource does not exist, or is not visible to this token."""


class FlatQuotaError(FlatError):
    """A metered resource, such as OMR credits, is exhausted."""


class FlatServerError(FlatError):
    """An internal or backend error. ``request_id`` is normally set here."""


def _int_header(headers: Mapping[str, str], name: str) -> int | None:
    for key, value in headers.items():
        if key.lower() == name.lower():
            try:
                return int(value)
            except (TypeError, ValueError):
                return None
    return None


def from_response(
    status: int,
    body: Any,
    headers: Mapping[str, str] | None = None,
) -> FlatError:
    """Build the right error for a non-2xx response."""
    payload = body if isinstance(body, dict) else {}
    code = payload.get("code")
    message = payload.get("message") or f"HTTP {status}"
    common = {
        "status": status,
        "code": code,
        "request_id": payload.get("id"),
        "headers": headers,
        "body": body,
    }

    if status == 403 and code == RATE_LIMIT_CODE:
        return FlatRateLimitError(message, **common)
    if code in QUOTA_CODES:
        return FlatQuotaError(message, **common)
    if status == 401:
        return FlatAuthenticationError(message, **common)
    if status == 403:
        return FlatAuthorizationError(message, **common)
    if status == 404:
        return FlatNotFoundError(message, **common)
    if status in (400, 422):
        return FlatValidationError(message, **common)
    if status >= 500:
        return FlatServerError(message, **common)
    return FlatError(message, **common)
''')

# Writing errors.py is not enough: nothing raises those classes unless the request path is taught
# to. The generated client raises its own ApiException subclasses, so a caller who follows the
# README and catches FlatNotFoundError catches nothing. Rewire the one raise site.
CLIENT = ROOT / "flat_api" / "api_client.py"
client_text = CLIENT.read_text()

raise_site = """                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )"""
flat_raise = """                raise _flat_error_from_response(
                    status=response_data.status,
                    body=return_data if isinstance(return_data, dict) else response_text,
                    headers=dict(response_data.getheaders() or {}),
                )"""

if raise_site not in client_text and "_flat_error_from_response" not in client_text:
    sys.exit("20_errors: could not find the raise site in api_client.py (FR-025)")

if raise_site in client_text:
    client_text = client_text.replace(raise_site, flat_raise, 1)

# Place the import with the other first-party ones, after the module docstring. Prepending it
# would displace the docstring and leave a stray string expression at the top of the file.
import_line = "from flat_api.errors import from_response as _flat_error_from_response\n"
if import_line not in client_text:
    anchor = "from flat_api.configuration import Configuration\n"
    if anchor not in client_text:
        sys.exit("20_errors: could not place the import in api_client.py (FR-025)")
    client_text = client_text.replace(anchor, import_line + anchor, 1)

CLIENT.write_text(client_text)

print("    errors: wrote flat_api/errors.py and raised them from api_client.py")
