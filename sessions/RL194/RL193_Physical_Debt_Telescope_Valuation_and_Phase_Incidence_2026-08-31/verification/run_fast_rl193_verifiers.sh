#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl178_inherited_early_window.py
python3 verification/verify_rl193_physical_debt.py
