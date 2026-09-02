#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl236_recurrence_and_charge.py
python3 verification/verify_rl236_proof_state.py
