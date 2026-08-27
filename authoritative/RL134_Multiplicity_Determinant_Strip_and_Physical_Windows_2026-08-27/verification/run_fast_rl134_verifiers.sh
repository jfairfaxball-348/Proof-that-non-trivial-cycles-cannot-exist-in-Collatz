#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 verification/verify_rl134_multiplicity_windows.py
echo "RL134 fast verifier suite: PASS"
