#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl261_full_phase.py
printf '%s\n' 'FAST_RL261_VERIFIERS PASS'
