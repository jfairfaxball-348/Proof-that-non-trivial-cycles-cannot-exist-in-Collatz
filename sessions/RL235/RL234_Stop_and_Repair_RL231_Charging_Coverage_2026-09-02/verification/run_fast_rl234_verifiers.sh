#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl234_charging_gap.py
python3 verification/verify_rl234_proof_state.py
