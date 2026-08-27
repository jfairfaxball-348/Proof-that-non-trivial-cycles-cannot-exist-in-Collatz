#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rotation_redteam.py"
python3 "$HERE/verify_rl131_bounds.py"
BIN="$(mktemp)"
trap 'rm -f "$BIN"' EXIT
${CXX:-c++} -O3 -std=c++17 "$HERE/verify_rl131_chunk.cpp" -o "$BIN"
"$BIN" 1 6496657853
"$BIN" 6496657855 9496657853
"$BIN" 9496657855 12496657853
"$BIN" 12496657855 15496657853
"$BIN" 15496657855 18496657853
"$BIN" 18496657855 21496657853
"$BIN" 21496657855 23506639475
echo "RL131 fast verifier suite: PASS"
