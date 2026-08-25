#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl91_scan_certificate.py"
python3 "$HERE/verify_rl91_multiscale_interval.py"
echo "RL91 fast verifier suite: PASS"
