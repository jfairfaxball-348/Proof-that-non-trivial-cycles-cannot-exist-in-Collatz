#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
BIN="${TMPDIR:-/tmp}/verify_rl91_scale_scan"
gcc -O3 "$HERE/verify_rl91_scale_scan.c" -lgmp -o "$BIN"
# Wide tier: exact complete scan, chunked.
N=5000056; STEP=125000; START=0; END=7000000
while [ "$START" -le "$END" ]; do
  STOP=$((START+STEP-1)); [ "$STOP" -gt "$END" ] && STOP="$END"
  "$BIN" "$N" "$START" "$STOP"
  START=$((STOP+1))
done
# Deep tier: exact complete scan, chunked.
N=10000056; STEP=100000; START=0; END=300000
while [ "$START" -le "$END" ]; do
  STOP=$((START+STEP-1)); [ "$STOP" -gt "$END" ] && STOP="$END"
  "$BIN" "$N" "$START" "$STOP"
  START=$((STOP+1))
done
