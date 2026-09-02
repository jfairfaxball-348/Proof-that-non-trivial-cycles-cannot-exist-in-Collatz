#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl231_chronological_renewal.py
python3 verification/verify_rl231_proof_state.py
