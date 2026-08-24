#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
(
  cd inherited
  sha256sum -c RL75_Global_RL_Closure_Route_Tournament_and_Primitive_Pump_Transversality_2026-08-24.zip.sha256
)
python3 verification/verify_rl76_owned_pump_scale.py
echo "FAST_RL76_VERIFIERS PASS"
