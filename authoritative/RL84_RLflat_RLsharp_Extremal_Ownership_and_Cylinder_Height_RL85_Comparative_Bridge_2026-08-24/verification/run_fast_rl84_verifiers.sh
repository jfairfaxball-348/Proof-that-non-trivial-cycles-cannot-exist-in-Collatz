#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
(
  cd "$ROOT/inherited"
  sha256sum -c RL83_RLflat_Segment_Product_CF_Farey_Frontier_RL84_Cylinder_Global_Slope_2026-08-24.zip.sha256
)
cd "$ROOT"
python3 verification/verify_rl84_extremal_comparison.py
