#!/bin/sh
set -eu
export PYTHONDONTWRITEBYTECODE=1
VERIFIER_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
sh "$VERIFIER_DIR/run_fast_rl195_verifiers.sh"
python3 "$VERIFIER_DIR/verify_rl196_p_shift_compatibility.py"
