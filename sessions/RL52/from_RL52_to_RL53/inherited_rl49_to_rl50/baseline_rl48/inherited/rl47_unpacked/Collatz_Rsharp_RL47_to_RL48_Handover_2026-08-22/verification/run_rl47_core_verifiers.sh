#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p verification/current_runs
python3 rl47_additions/verify_rl47_phase_coordinate.py | tee verification/current_runs/RL47_PHASE_COORDINATE_RERUN.txt
python3 rl47_additions/verify_rl47_rank_transport_bound.py | tee verification/current_runs/RL47_RANK_TRANSPORT_BOUND_RERUN.txt
g++ -O3 -std=c++17 rl47_additions/verify_fixed_pair_violation_by_t_hull.cpp -o verification/current_runs/verify_fixed_pair_violation_by_t_hull
for pair in "46 29" "65 41" "149 94" "214 135"; do
  set -- $pair
  A=$1; L=$2; Q=$((A-L))
  OUT="verification/current_runs/RL47_HULL_${A}_${L}.txt"
  verification/current_runs/verify_fixed_pair_violation_by_t_hull "$A" "$L" | tee "$OUT"
  grep -F "PAIR ($A,$L,$Q) any_violation 0" "$OUT" >/dev/null
done
echo "RL47 core verifiers: PASS"
