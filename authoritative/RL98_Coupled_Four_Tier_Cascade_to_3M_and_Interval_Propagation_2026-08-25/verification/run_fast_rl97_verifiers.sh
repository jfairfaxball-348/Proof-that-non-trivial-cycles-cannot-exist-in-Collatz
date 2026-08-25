#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl97_scan_certificate.py
python3 verify_rl97_four_tier_geometry.py
python3 verify_rl97_coupled_interval.py
cc -O2 verify_rl97_scale_scan.c -lgmp -o /tmp/verify_rl97_scale_scan_compile_check
rm -f /tmp/verify_rl97_scale_scan_compile_check
echo 'RL97 GMP scanner compile check: PASS'
echo 'RL97 fast verifier suite: PASS'
