#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
BIN="${TMPDIR:-/tmp}/verify_rl92_scale_scan"
gcc -O3 "$HERE/verify_rl92_scale_scan.c" -lgmp -o "$BIN"
# Reproduce only the new RL92 deep frontier beyond the inherited r<=300000 certificate.
START=300001
END=1100000
STEP=25000
while [ "$START" -le "$END" ]; do
  STOP=$((START+STEP-1)); [ "$STOP" -gt "$END" ] && STOP="$END"
  "$BIN" 10000056 "$START" "$STOP"
  START=$((STOP+1))
done
# Reproduce the non-load-bearing ultra-deep probe.
"$BIN" 15000056 0 1000
