#!/usr/bin/env bash
# Shared generation helpers. Vendored per SDK on purpose: each repository must be able to
# regenerate itself with no orchestrator and no sibling checkout (FR-023).

SPEC_FILE="${SPEC_FILE:-$REPO_ROOT/.openapi-spec.yaml}"
BUMP="${BUMP:-patch}"
API_REFERENCE_RAW="https://raw.githubusercontent.com/FlatIO/api-reference"

log() { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
die() { printf '\033[1;31merror:\033[0m %s\n' "$*" >&2; exit 1; }

cleanup_spec() { rm -f "$SPEC_FILE"; }
trap cleanup_spec EXIT

manifest_get() {
  python3 - "$1" <<'PY'
import sys, yaml, functools, operator
key = sys.argv[1].split(".")
doc = yaml.safe_load(open(".sdkgen.yaml"))
print(functools.reduce(operator.getitem, key, doc))
PY
}

latest_release_tag() {
  python3 - <<'PY'
import json, urllib.request
url = "https://api.github.com/repos/FlatIO/api-reference/releases/latest"
with urllib.request.urlopen(url, timeout=30) as r:
    print(json.load(r)["tag_name"])
PY
}

resolve_spec() {
  if [ -n "${SPEC_LOCAL_FILE:-}" ]; then
    log "Using local spec: $SPEC_LOCAL_FILE"
    cp "$SPEC_LOCAL_FILE" "$SPEC_FILE"
  else
    local ref="${SPEC_REF:-$(latest_release_tag)}"
    log "Fetching FlatIO/api-reference@$ref"
    curl -fsSL "$API_REFERENCE_RAW/$ref/spec/openapi.yaml" -o "$SPEC_FILE" \
      || die "could not fetch the specification at $ref"
    local declared expected
    declared="$(python3 -c "import yaml,sys;print(yaml.safe_load(open('$SPEC_FILE'))['info']['version'])")"
    expected="${ref#v}"
    [ "$declared" = "$expected" ] \
      || die "tag/version mismatch: tag $ref implies $expected, spec declares $declared"
  fi
  log "Specification version $(python3 -c "import yaml;print(yaml.safe_load(open('$SPEC_FILE'))['info']['version'])")"
}

# Remove everything .sdkgen.yaml declares generated, so a removed operation leaves no orphan.
zone_wipe() {
  python3 - <<'PY'
import pathlib, shutil, yaml
doc = yaml.safe_load(open(".sdkgen.yaml"))
root = pathlib.Path(".")
n = 0
for glob in doc["generated_paths"]:
    for path in sorted(root.glob(glob), reverse=True):
        if path.is_file():
            path.unlink(); n += 1
        elif path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
print(f"    removed {n} file(s)")
PY
}

have_java() { command -v java >/dev/null 2>&1 && java -version >/dev/null 2>&1; }

# run_generator <generator-name> <config> <output-dir>
# <output-dir> MUST be relative to the repository root: the docker backend mounts the repo at
# /local, so an absolute path outside it lands inside the repository instead.
run_generator() {
  local gen="$1" config="$2" out="$3"
  case "$out" in
    /*) die "run_generator: output must be repo-relative, got $out" ;;
  esac
  local version; version="$(manifest_get 'generator.version')"
  if have_java; then
    local cache="${OPENAPI_GENERATOR_CACHE:-$HOME/.cache/openapi-generator}"
    local jar="$cache/openapi-generator-cli-$version.jar"
    if [ ! -f "$jar" ]; then
      mkdir -p "$cache"
      curl -fsSL -o "$jar" \
        "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/$version/openapi-generator-cli-$version.jar"
    fi
    java -jar "$jar" generate -i "$SPEC_FILE" -g "$gen" -o "$out" -c "$config" --skip-validate-spec
  elif command -v docker >/dev/null 2>&1; then
    docker run --rm -v "$REPO_ROOT":/local -w /local \
      "openapitools/openapi-generator-cli:v$version" \
      generate -i "/local/$(basename "$SPEC_FILE")" -g "$gen" -o "/local/$out" \
               -c "/local/$config" --skip-validate-spec
  else
    die "need a working java (JDK) or docker to run openapi-generator"
  fi
}

# Reads the current version through the manifest pattern. Non-zero exit when unavailable.
read_version() {
  python3 - <<'RV'
import re, yaml, pathlib
doc = yaml.safe_load(open(".sdkgen.yaml"))
vf = doc["version_file"]
path = pathlib.Path(vf["path"])
if not path.is_file():
    raise SystemExit(1)
m = re.search(vf["pattern"], path.read_text())
if not m or m.group("version") == "0.0.0":
    raise SystemExit(1)
print(m.group("version"))
RV
}

# apply_bump <current-version> -> the next version per $BUMP
apply_bump() {
  python3 - "$1" "$BUMP" <<'AB'
import sys
current, bump = sys.argv[1], sys.argv[2]
major, minor, patch = (int(x) for x in current.split("."))
match bump:
    case "major": major, minor, patch = major + 1, 0, 0
    case "minor": minor, patch = minor + 1, 0
    case "patch": patch += 1
    case "none": pass
    case _: raise SystemExit(f"error: invalid BUMP={bump}")
print(f"{major}.{minor}.{patch}")
AB
}
