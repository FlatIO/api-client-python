#!/usr/bin/env python3
"""Retry policy (FR-006e). Idempotent: writes a fixed file."""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
(ROOT / "flat_api" / "_retry.py").write_text('''"""Retry policy for the Flat API.

Flat does not follow the usual conventions, and getting this wrong is silent:

  * rate limiting returns **403**, not 429
  * there is **no Retry-After header**; the reset time is ``X-RateLimit-Reset``, UTC epoch seconds
  * a plain 403 is a genuine authorization failure and must never be retried

So the policy keys on the response body's ``code``, not on the status alone.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass

from flat_api.errors import FlatError, FlatRateLimitError, FlatServerError

#: Methods safe to replay. A non-idempotent request that may already have been applied is not.
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})

MAX_RATE_LIMIT_WAIT = 300.0


@dataclass(frozen=True)
class RetryPolicy:
    """How the client retries. Pass ``RetryPolicy.disabled()`` to opt out entirely."""

    attempts: int = 3
    backoff_base: float = 0.5
    backoff_max: float = 30.0
    jitter: float = 0.25
    respect_rate_limit_reset: bool = True

    @classmethod
    def disabled(cls) -> "RetryPolicy":
        """No retries. Errors still arrive typed, and a rate-limit error still carries its reset."""
        return cls(attempts=1)

    @property
    def enabled(self) -> bool:
        return self.attempts > 1

    def should_retry(self, error: BaseException, method: str, attempt: int) -> bool:
        if attempt >= self.attempts:
            return False
        if method.upper() not in IDEMPOTENT_METHODS:
            return False
        if isinstance(error, FlatRateLimitError):
            return True
        if isinstance(error, FlatServerError):
            return True
        # A transport failure before the request was sent is safe to replay.
        return isinstance(error, OSError) and not isinstance(error, FlatError)

    def delay_for(self, error: BaseException, attempt: int) -> float:
        if (
            self.respect_rate_limit_reset
            and isinstance(error, FlatRateLimitError)
            and error.reset is not None
        ):
            wait = error.reset - time.time()
            if wait > 0:
                return min(wait + random.uniform(0, self.jitter), MAX_RATE_LIMIT_WAIT)
        exponential = min(self.backoff_base * (2 ** (attempt - 1)), self.backoff_max)
        return exponential + random.uniform(0, self.jitter * exponential)
''')
print("    retry: wrote flat_api/_retry.py")
