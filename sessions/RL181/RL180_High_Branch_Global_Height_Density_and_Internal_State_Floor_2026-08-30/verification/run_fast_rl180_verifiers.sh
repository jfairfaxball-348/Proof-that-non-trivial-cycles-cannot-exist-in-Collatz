#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl180_phase_support.py"
python3 "$HERE/verify_rl180_global_height.py"
echo "PASS: RL180 fast verifier suite"
