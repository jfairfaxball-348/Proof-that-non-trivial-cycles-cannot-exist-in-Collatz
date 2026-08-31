#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 verification/verify_rl200_h21_k_rank_and_prehistory.py
