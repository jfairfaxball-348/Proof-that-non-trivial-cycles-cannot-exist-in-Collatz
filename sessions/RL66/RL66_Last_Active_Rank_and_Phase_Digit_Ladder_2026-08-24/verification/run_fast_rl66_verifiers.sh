#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# Verification-economy boundary: verify that the frozen incoming RL65 binary still
# matches its sidecar, but do not recursively rerun RL65/RL64 historical suites.
(
  cd inherited
  sha256sum -c RL65_Rank_Tail_Phase_Selector_2026-08-24.zip.sha256
)
python3 verification/verify_rl66_last_active_rank.py
printf '%s\n' 'FAST_RL66_VERIFIERS PASS'
