#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE/rl43_additions"
for f in \
  verify_rl43_rho49_elimination.py \
  verify_rl43_defect_support_radius3_bridge.py \
  verify_rl43_gap9_cutofffree.py \
  verify_rl43_full_denominator_phase_bridge.py
do
  echo "===== $f ====="
  python3 "$f"
done
