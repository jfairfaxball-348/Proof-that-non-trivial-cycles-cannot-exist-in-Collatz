#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 rl51_research/verify_rl51_z27_terminal_tail.py
python3 rl51_research/verify_rl51_z29_terminal_proximity_barrier.py
python3 rl51_research/verify_rl51_z29_coupled_twozero_elimination.py
python3 rl51_research/verify_rl51_z31_coupled_elimination.py
python3 rl51_research/verify_rl51_z33_reduced_frontier.py
echo 'RL51 new verifiers: PASS'
