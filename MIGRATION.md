# Migrating to 2.0.0

Version 2.0.0 is a full regeneration of this client against the current Flat API. The previous
release line (1.1.x) was generated in 2024 or earlier and is missing everything the API has
shipped since.

The previous major stays installable and is deprecated on PyPI, not withdrawn. Nothing breaks
until you choose to upgrade.

## Why upgrade

- **Complete API coverage.** All 119 public operations, verified automatically on every release.
  The old client predates a great deal of the API, including OMR.
- **It stays current.** Releases are now automatic, tied to specification releases.
- **Typed errors, retries, pagination and OAuth refresh**, none of which the old client had.
- **Modern runtimes and full type information.**

## What breaks

1. **Package layout changed.** Import from the package root rather than reaching into internals.
2. **Errors are typed.** Code that inspected status codes or parsed message strings should branch on
   the error class instead. Note that rate limiting is HTTP 403, not 429.
3. **Supported runtimes moved up** to Python 3.11, 3.12 and 3.13. End-of-life runtimes are no longer supported.
4. **Manual pagination is unnecessary.** Hand-rolled cursor loops still work, but the built-in
   iterator is correct in cases hand-rolled loops usually miss.
5. **Model names follow the specification.** A few renames follow schema names upstream.

## How to upgrade

1. Raise your runtime to a supported version.
2. Bump the dependency: `pip install flat-api`.
3. Replace status-code checks with typed error handling.
4. Replace manual paging loops with the built-in iterator.
5. Run your tests. Anything unresolved is likely a model rename; check
   [the reference](docs/reference/).

## Staying on 1.1.x

It keeps working and stays installable. It will not receive new API capability, and it is not
regenerated when the API changes. If you need something added to the API after early 2024, you need
2.0.0.

## Problems

Open an issue on this repository, or email developers@flat.io.
