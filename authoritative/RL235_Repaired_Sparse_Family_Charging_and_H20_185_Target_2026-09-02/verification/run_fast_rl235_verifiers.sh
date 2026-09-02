#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl235_repaired_charging.py
python3 verification/verify_rl235_proof_state.py
