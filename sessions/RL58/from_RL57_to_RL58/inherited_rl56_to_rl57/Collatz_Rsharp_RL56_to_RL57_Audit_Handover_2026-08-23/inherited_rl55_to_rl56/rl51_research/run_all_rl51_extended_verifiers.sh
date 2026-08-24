#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
echo '=== inherited RL50 handover ==='
bash verification/run_all_rl50_handover_verifiers.sh
echo '=== RL51 z=27 terminal-tail certificate ==='
python3 rl51_research/verify_rl51_z27_terminal_tail.py
echo '=== RL51 z=29 preliminary terminal proximity/barrier ==='
python3 rl51_research/verify_rl51_z29_terminal_proximity_barrier.py
echo '=== RL51 z=29 coupled elimination ==='
python3 rl51_research/verify_rl51_z29_coupled_twozero_elimination.py
echo '=== RL51 z=31 coupled elimination ==='
python3 rl51_research/verify_rl51_z31_coupled_elimination.py
echo '=== RL51 z=33 reduced frontier ==='
python3 rl51_research/verify_rl51_z33_reduced_frontier.py
echo 'RL51 extended verifiers: PASS'
