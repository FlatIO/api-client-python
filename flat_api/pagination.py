"""Cursor pagination for the Flat API.

Eight operations at v2.25.0 are cursor-paginated, identified by a ``next`` query parameter. Note the
parameter is a shared component (``#/components/parameters/next``): any tool that reads an
operation\'s parameters without resolving ``$ref`` under-counts them and ships collections that
silently truncate.

The cursor itself is **not in the response body**. It arrives in the ``Link`` header, which the
specification does not declare, so it is parsed at runtime from the generated ``ApiResponse``.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Iterator
from typing import Any, TypeVar

__all__ = ["parse_link_header", "paginate"]

T = TypeVar("T")

_LINK = re.compile(r'<(?P<url>[^>]+)>\s*;\s*rel="(?P<rel>[^"]+)"')
_NEXT_PARAM = re.compile(r"[?&]next=(?P<cursor>[^&]+)")


def parse_link_header(value: str | None) -> dict[str, str]:
    """Parse an RFC 5988 Link header into {rel: url}."""
    if not value:
        return {}
    return {m.group("rel"): m.group("url") for m in _LINK.finditer(value)}


def next_cursor(headers: dict[str, str] | None) -> str | None:
    """Extract the opaque ``next`` cursor from a response\'s Link header, if any."""
    if not headers:
        return None
    link = next((v for k, v in headers.items() if k.lower() == "link"), None)
    url = parse_link_header(link).get("next")
    if not url:
        return None
    match = _NEXT_PARAM.search(url)
    return match.group("cursor") if match else None


def paginate(
    fetch_page: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> Iterator[T]:
    """Yield every item across all pages of a cursor-paginated operation.

    ``fetch_page`` must be the generated ``*_with_http_info`` variant, which returns an
    ``ApiResponse`` carrying the headers the cursor lives in.

    A token expiring mid-traversal is refreshed by the client and the traversal resumes from the
    same cursor, so no page is skipped or repeated.
    """
    cursor: str | None = kwargs.pop("next", None)
    seen: set[str] = set()

    while True:
        response = fetch_page(*args, **({**kwargs, "next": cursor} if cursor else kwargs))
        page = getattr(response, "data", response)
        if page:
            yield from page

        cursor = next_cursor(getattr(response, "headers", None))
        if not cursor:
            return
        # A server that returns a cursor it already gave us would loop forever.
        if cursor in seen:
            return
        seen.add(cursor)
