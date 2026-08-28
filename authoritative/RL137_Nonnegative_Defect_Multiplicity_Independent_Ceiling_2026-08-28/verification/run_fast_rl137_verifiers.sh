#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl137_nonnegative_ceiling.py"
echo "RL137 fast verifier suite: PASS"
