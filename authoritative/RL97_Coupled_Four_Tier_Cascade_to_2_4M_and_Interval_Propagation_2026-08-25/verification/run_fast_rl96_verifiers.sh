#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl96_scan_certificate.py
python3 verify_rl96_four_tier_geometry.py
python3 verify_rl96_coupled_interval.py
gcc -O2 verify_rl96_scale_scan.c -lgmp -o /tmp/verify_rl96_scale_scan
rm -f /tmp/verify_rl96_scale_scan
echo 'RL96 GMP scanner compile check: PASS'
echo 'RL96 fast verifier suite: PASS'
