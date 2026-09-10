#!/usr/bin/env python3
"""Ergonomic client with timeouts, base URL, retry and auth (FR-006g, FR-006i). Idempotent."""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
(ROOT / "flat_api" / "client.py").write_text('''"""The entry points a developer actually uses.

``FlatClient`` is synchronous, ``AsyncFlatClient`` is its asynchronous twin. Both take the same
arguments and raise the same typed errors; only the call convention differs.
"""

from __future__ import annotations

from typing import Any

from flat_api.api_client import ApiClient
from flat_api.configuration import Configuration
from flat_api.oauth import OAuth2Helper, TokenManager, Tokens
from flat_api._retry import RetryPolicy

__all__ = ["FlatClient", "AsyncFlatClient"]

DEFAULT_BASE_URL = "https://api.flat.io/v2"
#: A finite default. Waiting forever is not an acceptable default for an SDK.
DEFAULT_TIMEOUT = 30.0


class _BaseClient:
    def __init__(
        self,
        access_token: str | None = None,
        *,
        tokens: Tokens | None = None,
        oauth: OAuth2Helper | None = None,
        on_token_refresh: Any = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT,
        retry: RetryPolicy | None = None,
    ) -> None:
        if access_token is None and tokens is None:
            raise ValueError("pass either access_token= or tokens=")
        if tokens is None:
            tokens = Tokens(access_token=access_token or "")

        self.tokens = TokenManager(tokens, helper=oauth, on_token_refresh=on_token_refresh)
        self.retry = retry if retry is not None else RetryPolicy()
        self.base_url = base_url
        self.timeout = timeout

        configuration = Configuration(host=base_url)
        configuration.access_token = self.tokens.access_token
        self._configuration = configuration
        self._api_client = self._build_api_client(configuration)

    def _build_api_client(self, configuration: Configuration) -> Any:
        return ApiClient(configuration)

    @property
    def api_client(self) -> Any:
        """The generated client, for operations not yet surfaced ergonomically."""
        return self._api_client

    def _reauthenticate(self) -> None:
        """Refresh the access token and push it into the generated configuration."""
        token = self.tokens.refresh()
        self._configuration.access_token = token


class FlatClient(_BaseClient):
    """Synchronous Flat API client.

        client = FlatClient(access_token="...")
        me = client.api_client  # generated APIs hang off here
    """


class AsyncFlatClient(_BaseClient):
    """Asynchronous Flat API client, backed by the ``flat_api.aio`` generation pass."""

    def _build_api_client(self, configuration: Configuration) -> Any:
        from flat_api.aio.api_client import ApiClient as AsyncApiClient

        return AsyncApiClient(configuration)
''')
print("    client: wrote flat_api/client.py")
