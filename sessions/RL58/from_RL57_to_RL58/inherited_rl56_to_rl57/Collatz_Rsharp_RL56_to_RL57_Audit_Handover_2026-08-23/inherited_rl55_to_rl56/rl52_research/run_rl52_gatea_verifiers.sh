#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
CXX=${CXX:-g++}
BIN=rl52_research/.verify_rl52_terminal_event_automaton
$CXX -O3 -std=c++20 rl52_research/verify_rl52_terminal_event_automaton.cpp -o "$BIN"
python3 rl52_research/verify_rl52_z35_bootstrap.py
"$BIN" 33 6 16 100 54
"$BIN" 35 1 34 110 85
"$BIN" 35 3 18 100 52
"$BIN" 35 5 16 100 54
"$BIN" 35 7 14 100 51
"$BIN" 35 8 12 100 48
rm -f "$BIN"
echo 'RL52 Gate-A z=33/z=35 verifier suite: PASS'
