#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE/inherited"
sha256sum -c RL68_Nested_Descent_and_Backward_Digit_Ladder_2026-08-24.zip.sha256
cd "$HERE"
python3 verification/verify_rl69_third_backward_digit.py
echo 'FAST_RL69_VERIFIERS PASS'
