#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
(
  cd inherited
  sha256sum -c RL80_Blue_Dyadic_Funnel_Certified_Basin_NoGo_and_Auxiliary_Capture_2026-08-24.zip.sha256
)
/usr/bin/python3 verification/verify_rl81_auxiliary_transfer.py
/usr/bin/python3 verification/verify_rl82_rlflat_seed.py
