#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl130_rotation_redteam.py"
python3 "$HERE/verify_rl130_quotient_bounds.py"
BIN="$(mktemp)"
trap 'rm -f "$BIN"' EXIT
${CXX:-c++} -O3 -std=c++17 "$HERE/verify_rl130_descent.cpp" -o "$BIN"
"$BIN"
echo "RL130 fast verifier suite: PASS"
