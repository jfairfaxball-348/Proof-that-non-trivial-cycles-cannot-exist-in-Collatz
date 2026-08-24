#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE"
(
  cd inherited
  sha256sum -c RL66_Last_Active_Rank_and_Phase_Digit_Ladder_2026-08-24.zip.sha256
)
python3 verification/verify_rl67_previous_active_interface.py
echo "FAST_RL67_VERIFIERS PASS"
