#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 "$HERE/verify_rl269_analytic.py" > "$TMP/analytic.txt"
diff -u "$HERE/analytic_output.txt" "$TMP/analytic.txt"

python3 "$HERE/redteam_rl269_small.py" > "$TMP/redteam.txt"
diff -u "$HERE/redteam_output.txt" "$TMP/redteam.txt"

echo "RL269_FAST_SUITE_PASS"
