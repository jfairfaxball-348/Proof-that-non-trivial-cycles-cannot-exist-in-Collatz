#!/bin/sh
set -eu
python3 verification/verify_rl110_sparse_diameter.py
python3 verification/scan_rl110_pairwise_divisibility.py
