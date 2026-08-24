#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
ADD="$HERE/rl46_additions"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
python "$ADD/verify_fixed_pair_prefixcap_cutofffree.py" 46 29 > "$TMP/46.txt"
cat "$TMP/46.txt"
grep -Fq 'hits 0' "$TMP/46.txt"
python "$ADD/verify_fixed_pair_prefixcap_cutofffree.py" 65 41 > "$TMP/65.txt"
cat "$TMP/65.txt"
grep -Fq 'hits 1' "$TMP/65.txt"
grep -Fq '(22, 2, 16, 38, 39, 0, 0, False, 60, 31)' "$TMP/65.txt"
python "$ADD/verify_min_excess_65_41_fast.py" > "$TMP/min.txt"
cat "$TMP/min.txt"
grep -Fq 'target present True min_e 125' "$TMP/min.txt"
echo 'RL46 STRUCTURAL VERIFIERS PASSED'
