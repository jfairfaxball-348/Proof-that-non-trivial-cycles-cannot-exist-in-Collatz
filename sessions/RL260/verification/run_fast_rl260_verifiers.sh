#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl260_core.py
g++ -O3 -std=c++17 verify_rl260_closure.cpp -o .verify_rl260_closure
./.verify_rl260_closure 1 10
./.verify_rl260_closure 11 28
rm -f .verify_rl260_closure .rl260_low_cases.tsv
echo "FAST_RL260_VERIFIERS PASS"
