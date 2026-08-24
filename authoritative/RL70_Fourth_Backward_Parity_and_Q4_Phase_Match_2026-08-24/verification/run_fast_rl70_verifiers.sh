#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE/inherited"
sha256sum -c RL69_Third_Backward_Digit_and_Phase_Match_2026-08-24.zip.sha256
cd "$HERE"
python3 verification/verify_rl70_fourth_backward_parity.py
echo 'FAST_RL70_VERIFIERS PASS'
