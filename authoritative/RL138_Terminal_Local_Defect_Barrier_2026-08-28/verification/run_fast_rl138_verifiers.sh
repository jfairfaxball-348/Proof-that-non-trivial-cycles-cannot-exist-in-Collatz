#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_rl138_terminal_barrier.py"
echo "RL138 fast verifier suite: PASS"
