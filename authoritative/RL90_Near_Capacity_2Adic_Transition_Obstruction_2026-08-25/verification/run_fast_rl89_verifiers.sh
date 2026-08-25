#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
# New-work verifier only. Historical expensive suites are intentionally not replayed.
gcc -O3 -fopenmp "$HERE/verify_rl89_dlog64.c" -o "$HERE/.verify_rl89_dlog64"
OMP_NUM_THREADS="${OMP_NUM_THREADS:-5}" "$HERE/.verify_rl89_dlog64" > "$HERE/RL89_DLOG64_SCAN.txt"
python3 "$HERE/verify_rl89_near_capacity.py" "$HERE/RL89_DLOG64_SCAN.txt"
rm -f "$HERE/.verify_rl89_dlog64"
