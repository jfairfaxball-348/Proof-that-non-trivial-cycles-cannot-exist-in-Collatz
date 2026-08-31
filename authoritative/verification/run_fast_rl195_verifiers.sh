#!/bin/sh
set -eu
export PYTHONDONTWRITEBYTECODE=1
VERIFIER_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 "$VERIFIER_DIR/verify_rl178_inherited_early_window.py"
python3 "$VERIFIER_DIR/verify_rl193_physical_debt.py"
python3 "$VERIFIER_DIR/verify_rl194_rank_order.py"
python3 "$VERIFIER_DIR/verify_rl194_weight_order.py"
python3 "$VERIFIER_DIR/verify_rl194_owned_prefix.py"
python3 "$VERIFIER_DIR/verify_rl194_chronological_speed.py"
python3 "$VERIFIER_DIR/verify_rl195_moment_adjacency.py"
python3 "$VERIFIER_DIR/verify_rl195_zero_geometry.py"
python3 "$VERIFIER_DIR/verify_rl195_window_reconstruction.py"
python3 "$VERIFIER_DIR/verify_rl195_owned_local_realizability.py"
