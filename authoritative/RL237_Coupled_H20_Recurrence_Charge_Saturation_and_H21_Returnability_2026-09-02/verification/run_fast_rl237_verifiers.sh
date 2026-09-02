#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl237_fast_charge.py
python3 verification/verify_rl237_proof_state.py
