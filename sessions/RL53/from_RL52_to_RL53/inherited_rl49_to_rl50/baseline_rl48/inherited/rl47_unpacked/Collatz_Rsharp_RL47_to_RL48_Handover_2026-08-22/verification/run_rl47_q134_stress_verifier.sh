#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p verification/current_runs
g++ -O3 -std=c++17 rl47_additions/verify_fixed_t_hull_budgetres64.cpp -o verification/current_runs/verify_fixed_t_hull_budgetres64
OUT=verification/current_runs/RL47_Q134_STRESS_RERUN.txt
: > "$OUT"
for t in 2 4 6 8 10 12 14 16; do
  line="$(verification/current_runs/verify_fixed_t_hull_budgetres64 363 229 "$t")"
  echo "$line" | tee -a "$OUT"
  echo "$line" | grep -F "hit 0" >/dev/null
done
echo "RL47 q134 low-t stress verifier: PASS" | tee -a "$OUT"
