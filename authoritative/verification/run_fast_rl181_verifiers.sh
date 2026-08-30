#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl181_pair_gap_occupancy.py"
echo "PASS: RL181 fast verifier suite"
