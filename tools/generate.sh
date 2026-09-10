#!/usr/bin/env bash
# Regenerate the Flat Python SDK from the public OpenAPI specification.
#
# Self-contained (FR-023): fetches the spec, runs the pinned generator into a scratch tree, copies
# only the paths .sdkgen.yaml declares generated into the repository, applies post-generation
# patches, emits the inventory and bumps the version.
#
# Generating into a scratch tree and copying selectively makes FR-025d structural: the generator
# physically cannot write outside the declared zone, so a protected README or pyproject can never be
# clobbered by a generator that changes its output layout.
#
#   SPEC_REF         api-reference release tag to read       (default: latest release)
#   SPEC_LOCAL_FILE  use this local spec instead of fetching
#   BUMP             patch | minor | major | none            (default: patch)
#
# The generator emits sync OR async, never both (T001 spike), so this runs it twice and merges.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
# shellcheck source=tools/lib/generate-common.sh
source tools/lib/generate-common.sh

# Read the current version before anything is wiped. The exports patch rewrites __init__.py with a
# placeholder, so reading it afterwards would reset the version on every run.
# VERSION is the durable source of truth: it is hand-maintained, outside the generated zone, and
# unambiguous. __init__.py is derived from it, so reading that instead would be circular.
CUR_VERSION="$(cat VERSION 2>/dev/null || true)"
[ -n "$CUR_VERSION" ] || CUR_VERSION="$(read_version || echo '2.0.0')"
log "Current version $CUR_VERSION"

resolve_spec

# Scratch must live inside the repository: the docker backend mounts the repo root at /local,
# so a path outside it would be written into the repo as ./var/folders/...
SCRATCH=".sdkgen-scratch"
rm -rf "$SCRATCH"
trap 'rm -rf "$SCRATCH"; cleanup_spec' EXIT

log "Pass 1/2: synchronous client (urllib3)"
run_generator "python" "tools/openapi-config.json" "$SCRATCH/sync"

log "Pass 2/2: asynchronous client (asyncio)"
run_generator "python" "tools/openapi-config-async.json" "$SCRATCH/async"

log "Wiping the generated zone"
zone_wipe

log "Installing the generated zone"
mkdir -p flat_api docs/reference .openapi-generator
cp -R "$SCRATCH/sync/flat_api/." flat_api/
rm -rf flat_api/docs flat_api/test
# source-only mode emits per-operation docs under the package; they belong in the generated
# reference directory, not beside the hand-written README (FR-025c).
if [ -d "$SCRATCH/sync/flat_api/docs" ]; then cp -R "$SCRATCH/sync/flat_api/docs/." docs/reference/; fi
[ -d "$SCRATCH/sync/.openapi-generator" ] && cp -R "$SCRATCH/sync/.openapi-generator/." .openapi-generator/
# The async pass contributes its api/ and api_client under flat_api/aio (merged by patches).
mkdir -p flat_api/aio
cp -R "$SCRATCH/async/flat_api_async/." flat_api/aio/
rm -rf flat_api/aio/docs flat_api/aio/test

log "Applying post-generation patches"
for patch in tools/patches/*.py; do
  [ -f "$patch" ] || continue
  log "  $(basename "$patch")"
  python3 "$patch" || die "patch $(basename "$patch") failed (FR-025)"
done

log "Emitting operation inventory"
python3 tools/emit_inventory.py

NEW_VERSION="$(apply_bump "$CUR_VERSION")"
log "Version -> $NEW_VERSION"
python3 - "$NEW_VERSION" <<'PY'
import pathlib, re, sys
v = sys.argv[1]
p = pathlib.Path("flat_api/__init__.py")
t = p.read_text()
if re.search(r'__version__ = "[0-9]+\.[0-9]+\.[0-9]+"', t):
    t = re.sub(r'__version__ = "[0-9]+\.[0-9]+\.[0-9]+"', f'__version__ = "{v}"', t)
else:
    t += f'\n__version__ = "{v}"\n'
p.write_text(t)
PY

echo "$NEW_VERSION" > VERSION
log "Done. Version $NEW_VERSION"
