#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl178_inherited_early_window.py
python3 verification/verify_rl193_physical_debt.py
python3 verification/verify_rl194_rank_order.py
python3 verification/verify_rl194_weight_order.py
python3 verification/verify_rl194_owned_prefix.py
python3 verification/verify_rl194_chronological_speed.py
