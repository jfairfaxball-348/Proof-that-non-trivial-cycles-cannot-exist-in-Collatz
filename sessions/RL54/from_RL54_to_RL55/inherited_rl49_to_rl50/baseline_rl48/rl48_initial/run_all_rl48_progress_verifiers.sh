#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
python3 verify_rl48_same_root_selector.py
python3 verify_rl48_rank_relaxation_barrier.py
python3 verify_rl48_phase_rank_defect.py
echo 'RL48 progress verifiers: PASS'
