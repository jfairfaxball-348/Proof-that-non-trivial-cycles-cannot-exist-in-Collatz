#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
(
  cd "$ROOT/inherited"
  sha256sum -c RL70_Fourth_Backward_Parity_and_Q4_Phase_Match_2026-08-24.zip.sha256
)
python3 "$ROOT/verification/verify_rl71_fifth_backward_digit.py"
echo "FAST_RL71_VERIFIERS PASS"
