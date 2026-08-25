#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TMPBIN="${TMPDIR:-/tmp}/verify_rl90_band550k.$$"
TMPOUT="${TMPDIR:-/tmp}/verify_rl90_band550k.$$.txt"
trap 'rm -f "$TMPBIN" "$TMPOUT"' EXIT

gcc -O3 "$HERE/verify_rl90_band550k.c" -lgmp -o "$TMPBIN"
"$TMPBIN" > "$TMPOUT"
diff -u "$HERE/RL90_DLOG_BAND550K_SCAN.txt" "$TMPOUT"
python3 "$HERE/verify_rl90_interval.py" "$TMPOUT"
echo "RL90 fast verifier suite: PASS"
