#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl95_scan_certificate.py"
python3 "$HERE/verify_rl95_four_tier_geometry.py"
python3 "$HERE/verify_rl95_coupled_interval.py"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
gcc -O2 "$HERE/verify_rl95_scale_scan.c" -lgmp -o "$tmp/verify_rl95_scale_scan"
"$tmp/verify_rl95_scale_scan" 1024 1 2 >/dev/null
echo "RL95 GMP scanner compile check: PASS"
echo "RL95 fast verifier suite: PASS"
