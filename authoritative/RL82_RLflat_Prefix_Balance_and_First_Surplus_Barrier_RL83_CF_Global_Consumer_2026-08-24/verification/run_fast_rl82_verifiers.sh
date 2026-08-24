#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

(
  cd inherited
  sha256sum -c RL81_Auxiliary_Basin_Transfer_Physical_Lift_Barrier_RL82_RLflat_Maximum_Pivot_2026-08-24.zip.sha256
)

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
unzip -q inherited/RL81_Auxiliary_Basin_Transfer_Physical_Lift_Barrier_RL82_RLflat_Maximum_Pivot_2026-08-24.zip -d "$tmp"
incoming_root="$tmp/RL81_Auxiliary_Basin_Transfer_Physical_Lift_Barrier_RL82_RLflat_Maximum_Pivot_2026-08-24"
(
  cd "$incoming_root"
  sha256sum -c SHA256SUMS.txt >/dev/null
  bash verification/run_fast_rl81_verifiers.sh
)

python3 verification/verify_rl82_rlflat_prefix_balance.py
