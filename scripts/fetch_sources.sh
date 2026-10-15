#!/usr/bin/env bash
# Clone the clEsperanto sources documented by this site.
#
# - On a tag build (e.g. "0.25.0", and "stable" which points to the latest tag),
#   CLIc is the reference and is cloned at the exact same version as the doc tag,
#   while pyclesperanto and clesperantoj are cloned at their latest patch release
#   of the same X.Y series (e.g. doc 0.25.0 -> CLIc 0.25.0, pyclesperanto 0.25.2,
#   clesperantoj-0.25.1).
# - Otherwise ("latest", branches, PR previews, local builds), the development
#   branches are cloned.
#
# The version can be forced locally with: CLESPERANTO_VERSION=0.25.0 bash scripts/fetch_sources.sh
# The cloned refs are written to _submodules/refs.txt (read by conf.py).
set -euo pipefail

version="${CLESPERANTO_VERSION:-}"
if [[ -z "$version" && "${READTHEDOCS_VERSION_TYPE:-}" == "tag" ]]; then
    version="${READTHEDOCS_GIT_IDENTIFIER#v}"
fi

# latest tag "<prefix>X.Y.<patch>" of a repository, ignoring pre-releases
latest_patch() {
    local url="$1" prefix="$2" series="$3"
    local ref
    ref=$(git ls-remote --tags --refs "$url" \
        | sed 's|.*refs/tags/||' \
        | grep -E "^${prefix}${series//./\\.}\.[0-9]+$" \
        | sort -V | tail -n 1 || true)
    if [[ -z "$ref" ]]; then
        echo "error: no tag ${prefix}${series}.* found in $url" >&2
        exit 1
    fi
    echo "$ref"
}

PYCLE_URL=https://github.com/clEsperanto/pyclesperanto.git
CLIC_URL=https://github.com/clEsperanto/CLIc.git
CLIJ_URL=https://github.com/clEsperanto/clesperantoj.git

if [[ -n "$version" ]]; then
    series=$(echo "$version" | cut -d. -f1,2)
    pycle_ref=$(latest_patch "$PYCLE_URL" "" "$series")
    clic_ref="$version"
    clij_ref=$(latest_patch "$CLIJ_URL" "clesperantoj-" "$series")
else
    pycle_ref="main"
    clic_ref="master"
    clij_ref="main"
fi

echo "Fetching sources: pyclesperanto@$pycle_ref, CLIc@$clic_ref, clesperantoj@$clij_ref"

rm -rf _submodules/pyclesperanto _submodules/clic _submodules/clesperantoj
git clone --depth 1 -b "$pycle_ref" "$PYCLE_URL" _submodules/pyclesperanto
git clone --depth 1 -b "$clic_ref" "$CLIC_URL" _submodules/clic
git clone --depth 1 -b "$clij_ref" "$CLIJ_URL" _submodules/clesperantoj

cat > _submodules/refs.txt <<EOF
pyclesperanto=$pycle_ref
clic=$clic_ref
clesperantoj=$clij_ref
EOF
