#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
(
  cd inherited
  sha256sum -c RL79_Post_Tournament_Common_Barrier_Synthesis_and_Unit_Increment_Reset_2026-08-24.zip.sha256
)
python3 verification/verify_rl80_blue_basin.py
