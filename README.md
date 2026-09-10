# Flat API client for Python

Official client for the [Flat REST API](https://flat.io/developers/docs/api/), generated from Flat's
public OpenAPI specification and kept current automatically.

```sh
pip install flat-api
```

```python
from flat_api import FlatClient

client = FlatClient(access_token="YOUR_TOKEN")
me = client.api_client  # generated APIs hang off here
```

Get a token in seconds with a [Personal Access Token](https://flat.io/developers/apps); it works
exactly like an OAuth access token for your own account.

## What this client does for you

- **Typed errors.** Branch on the error, not the status code. Flat returns HTTP 403 for both rate
  limiting and authorization failures, so status alone cannot tell them apart.
- **Automatic retries.** Rate limits and server errors are retried with backoff. Flat sends no
  `Retry-After`, so the client reads `X-RateLimit-Reset` instead.
- **Automatic pagination.** Eight collection endpoints are cursor-paginated with the cursor in a
  `Link` header. You get an iterator; you never touch a cursor.
- **OAuth2 built in.** Authorization URLs, code exchange and transparent token refresh.
- **Full type information**, so your editor and your coding assistant both know the API.

### Pagination

```python
from flat_api import paginate

for score in paginate(api.get_user_scores_with_http_info, user="me"):
    print(score.title)
```

### Errors

```python
from flat_api import FlatRateLimitError, FlatNotFoundError

try:
    ...
except FlatRateLimitError as exc:
    print("retry after", exc.reset)
except FlatNotFoundError:
    print("no such score")
```

### Asynchronous use

```python\nfrom flat_api import AsyncFlatClient

client = AsyncFlatClient(access_token="YOUR_TOKEN")
# every operation is awaitable\n```

## Supported versions

Python 3.11, 3.12 and 3.13. Versions past their upstream end of life are not supported; see
[MIGRATION.md](MIGRATION.md) if you are on an older runtime.

## Documentation

- [Quickstart](QUICKSTART.md), install to first call
- [Per-operation reference](docs/reference/), generated
- [API documentation](https://flat.io/developers/docs/api/)
- [Migrating from 1.1.x](MIGRATION.md)

## Verifying this package

Every release carries a signed provenance attestation linking the package back to the commit, the
workflow run that built it, and the API specification version it was generated from.

```sh
pip download --no-deps flat-api
gh attestation verify flat_api-*.whl --repo FlatIO/api-client-python
```

Published through PyPI trusted publishing: no long-lived token exists that could publish under this
name.

## How this client is maintained

Generated from the public specification published at
[FlatIO/api-reference](https://github.com/FlatIO/api-reference). A new specification release
regenerates, validates and publishes this package automatically, so it never drifts from the API.

Files under `docs/reference/` and the client sources are generated: edit the generator configuration
in `tools/`, not the output.

## License

Apache 2.0. See [LICENSE](LICENSE).
