#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl92_scan_certificate.py"
python3 "$HERE/verify_rl92_multiscale_interval.py"
python3 "$HERE/verify_rl92_geometric_tier_audit.py"
echo "RL92 fast verifier suite: PASS"
