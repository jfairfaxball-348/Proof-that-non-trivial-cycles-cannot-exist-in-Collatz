#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl94_scan_certificate.py
python3 verification/verify_rl94_four_tier_geometry.py
python3 verification/verify_rl94_coupled_interval.py
TMP=$(mktemp)
gcc -O2 verification/verify_rl94_scale_scan.c -lgmp -o "$TMP"
rm -f "$TMP"
echo 'RL94 GMP scanner compile check: PASS'
echo 'RL94 fast verifier suite: PASS'
