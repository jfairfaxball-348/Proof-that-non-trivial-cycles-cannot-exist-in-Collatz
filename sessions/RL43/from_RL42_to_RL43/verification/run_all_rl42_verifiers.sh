#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

run() {
  local f="$1"
  echo "===== $f ====="
  python3 "$f"
  echo
}

run rl41_checkpoint/verify_rl41_arithmetic_checkpoint.py
run rl42_additions/verify_rl42_moved_rank_sparse_bridge.py
run rl42_additions/verify_rl42_prefix_cap_gap_vs_moved_mass.py
run rl42_additions/verify_rl42_lightweight_rho28.py
run rl42_additions/verify_rl42_rho28_excess_dp.py
run rl42_additions/verify_rl42_transport_efficiency_bridge.py
run rl42_additions/verify_rl42_crossing_excess_transport_floor.py
run rl42_additions/verify_rl42_rho48_elimination.py

echo "ALL RETAINED RL41/RL42 VERIFIERS: PASS"
