#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
ADD="$HERE/rl46_additions"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT
python "$ADD/verify_fixed_pair_boundary_layerdp.py" 149 94 > "$TMP"
tail -n 1 "$TMP"
grep -Fq 'violations []' "$TMP"
grep -Fq 'equalities []' "$TMP"
echo 'RL46 Q55 BOUNDARY VERIFIER PASSED'
