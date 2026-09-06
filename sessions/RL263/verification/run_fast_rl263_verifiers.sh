#!/usr/bin/env bash
set -euo pipefail
python3 verification/verify_rl263_physical_gap_barrier.py
echo FAST_RL263_VERIFIERS_PASS
