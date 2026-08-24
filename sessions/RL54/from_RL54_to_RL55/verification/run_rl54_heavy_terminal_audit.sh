#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
CXX="${CXX:-g++}"
BIN="/tmp/verify_rl54_terminal_exactx_split.$$"
trap 'rm -f "$BIN"' EXIT
"$CXX" -O3 -std=c++17 -fopenmp rl54_research/verify_rl54_terminal_exactx_split.cpp -o "$BIN"
# Reproduce the recorded z=41 X=8 Y=17 split-10 certificate.
"$BIN" 41 8 17 10
