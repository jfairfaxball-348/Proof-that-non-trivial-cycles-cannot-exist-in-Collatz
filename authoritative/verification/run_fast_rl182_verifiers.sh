#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl182_numerator_ownership.py"
echo "PASS: RL182 fast verifier suite"
