#!/usr/bin/env bash
set -euo pipefail
python3 verification/verify_rl262_selector_and_phase.py
echo 'FAST_RL262_VERIFIERS PASS'
