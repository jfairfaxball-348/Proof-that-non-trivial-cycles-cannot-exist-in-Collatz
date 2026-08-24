#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python verify_rl48_four_swap_factorization.py
python verify_rl48_two_trajectory_semantics.py
