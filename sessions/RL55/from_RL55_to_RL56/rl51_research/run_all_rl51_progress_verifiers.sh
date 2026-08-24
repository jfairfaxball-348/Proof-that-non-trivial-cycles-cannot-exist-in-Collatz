#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
echo '=== inherited RL50 handover ==='
bash verification/run_all_rl50_handover_verifiers.sh
echo '=== RL51 z=27 terminal-tail certificate ==='
python3 rl51_research/verify_rl51_z27_terminal_tail.py
echo '=== RL51 z=29 terminal proximity/barrier ==='
python3 rl51_research/verify_rl51_z29_terminal_proximity_barrier.py
echo 'RL51 progress verifiers: PASS'
