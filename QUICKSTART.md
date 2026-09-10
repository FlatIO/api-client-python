# Quickstart

From nothing to your first authenticated call.

## 1. Get a token

Create a [Personal Access Token](https://flat.io/developers/apps). It behaves like an OAuth access
token scoped to your own account, which is all you need to start.

## 2. Install

```sh
pip install flat-api
```

Requires Python 3.11, 3.12 and 3.13.

## 3. Call the API

```python
from flat_api import FlatClient

client = FlatClient(access_token="YOUR_TOKEN")
me = client.api_client  # generated APIs hang off here
```

If that prints your account, you are done.

## 4. Do something useful

List your scores. The client handles paging for you:

```python
from flat_api import paginate

for score in paginate(api.get_user_scores_with_http_info, user="me"):
    print(score.title)
```

## 5. Handle failure properly

```python
from flat_api import FlatRateLimitError, FlatNotFoundError

try:
    ...
except FlatRateLimitError as exc:
    print("retry after", exc.reset)
except FlatNotFoundError:
    print("no such score")
```

Two things worth knowing about the Flat API specifically:

- Rate limiting returns **403**, not 429, and carries no `Retry-After`. The reset time is in
  `X-RateLimit-Reset`. The client already handles this; the note matters if you disable retries.
- The error `id` is only present on internal and backend errors. When you have one, quote it to
  support: it makes diagnosis much faster.

## Where next

- [README](README.md) for the full feature tour
- [Per-operation reference](docs/reference/)
- [API documentation](https://flat.io/developers/docs/api/)
