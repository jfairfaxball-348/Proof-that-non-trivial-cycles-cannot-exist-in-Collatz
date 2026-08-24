#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
(
  cd "$ROOT/inherited"
  sha256sum -c RL76_Owned_Pump_Physical_Scale_Trade_and_Packing_Barrier_2026-08-24.zip.sha256
)
python3 "$ROOT/verification/verify_rl77_product_cf_scale.py"
echo 'FAST_RL77_VERIFIERS PASS'
