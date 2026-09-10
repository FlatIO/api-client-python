#!/usr/bin/env python3
"""OAuth2 helpers and single-flight refresh (FR-006i to FR-006l). Idempotent."""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
(ROOT / "flat_api" / "oauth.py").write_text('''"""OAuth2 support for the Flat API.

The public specification declares one security scheme: OAuth2 with the authorization-code flow and
23 scopes. A Personal Access Token is an OAuth access token for your own account, so passing a token
straight to the client covers both cases.

A refresh token is only issued when the authorization request sets ``access_type=offline``.

This module never stores a token. Persistence is deployment-specific, so the client hands refreshed
tokens to a callback you supply and it is your job to save them.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from urllib.parse import urlencode

import httpx

from flat_api.errors import FlatAuthenticationError

__all__ = ["Tokens", "OAuth2Helper", "TokenManager"]

AUTHORIZE_URL = "https://flat.io/auth/oauth"
TOKEN_URL = "https://api.flat.io/oauth/access_token"

#: Refresh this many seconds before nominal expiry, to avoid racing the server clock.
EXPIRY_SKEW = 30.0


@dataclass
class Tokens:
    access_token: str
    refresh_token: str | None = None
    expires_at: float | None = None

    @classmethod
    def from_response(cls, payload: dict) -> "Tokens":
        expires_in = payload.get("expires_in")
        return cls(
            access_token=payload["access_token"],
            refresh_token=payload.get("refresh_token"),
            expires_at=time.time() + float(expires_in) if expires_in else None,
        )

    @property
    def expired(self) -> bool:
        return self.expires_at is not None and time.time() >= self.expires_at - EXPIRY_SKEW


class OAuth2Helper:
    """Builds the authorization URL and exchanges codes for tokens."""

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize_url(
        self,
        scopes: list[str],
        state: str,
        *,
        offline: bool = True,
    ) -> str:
        """URL to send a user to. ``offline=True`` is what yields a refresh token."""
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": "code",
            "scope": " ".join(scopes),
            "state": state,
        }
        if offline:
            params["access_type"] = "offline"
        return f"{AUTHORIZE_URL}?{urlencode(params)}"

    def exchange_code(self, code: str) -> Tokens:
        return self._token_request(
            {"grant_type": "authorization_code", "code": code, "redirect_uri": self.redirect_uri}
        )

    def refresh(self, refresh_token: str) -> Tokens:
        return self._token_request(
            {"grant_type": "refresh_token", "refresh_token": refresh_token}
        )

    def _token_request(self, payload: dict) -> Tokens:
        body = {**payload, "client_id": self.client_id, "client_secret": self.client_secret}
        response = httpx.post(TOKEN_URL, data=body, timeout=30)
        if response.status_code >= 400:
            raise FlatAuthenticationError(
                "OAuth2 token request failed; the user must re-authorize",
                status=response.status_code,
                body=_safe_json(response),
            )
        return Tokens.from_response(response.json())


class TokenManager:
    """Holds the current tokens and refreshes them at most once at a time.

    Single-flight matters: two concurrent requests hitting an expired token must not both refresh,
    because the second refresh would invalidate the token the first just obtained.
    """

    def __init__(
        self,
        tokens: Tokens,
        helper: OAuth2Helper | None = None,
        on_token_refresh=None,
    ) -> None:
        self._tokens = tokens
        self._helper = helper
        self._on_refresh = on_token_refresh
        self._lock = threading.Lock()

    @property
    def access_token(self) -> str:
        return self._tokens.access_token

    def refresh(self) -> str:
        """Refresh once, even under concurrency, and return the new access token."""
        with self._lock:
            current = self._tokens.access_token
            if self._tokens.access_token != current:
                return self._tokens.access_token
            if self._helper is None or not self._tokens.refresh_token:
                raise FlatAuthenticationError(
                    "the access token expired and no refresh token is available; "
                    "the user must re-authorize"
                )
            self._tokens = self._helper.refresh(self._tokens.refresh_token)
            if self._on_refresh is not None:
                self._on_refresh(self._tokens)
            return self._tokens.access_token


def _safe_json(response: httpx.Response):
    try:
        return response.json()
    except ValueError:
        return None
''')
print("    oauth: wrote flat_api/oauth.py")
