#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl93_scan_certificate.py
python3 verify_rl93_four_tier_geometry.py
python3 verify_rl93_coupled_interval.py
if command -v gcc >/dev/null 2>&1 && pkg-config --exists gmp 2>/dev/null; then
  gcc -O2 verify_rl93_scale_scan.c -lgmp -o /tmp/verify_rl93_scale_scan_compile_test
  rm -f /tmp/verify_rl93_scale_scan_compile_test
  echo "RL93 GMP scanner compile check: PASS"
else
  echo "RL93 GMP scanner compile check: SKIP (toolchain unavailable)"
fi
echo "RL93 fast verifier suite: PASS"
