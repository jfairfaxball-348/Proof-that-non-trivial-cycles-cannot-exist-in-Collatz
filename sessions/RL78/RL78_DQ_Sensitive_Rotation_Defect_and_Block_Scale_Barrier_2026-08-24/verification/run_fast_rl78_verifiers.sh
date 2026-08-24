#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL77_Product_Growth_CF_Full_Phase_Scale_Coupling_and_Lattice_Barrier_2026-08-24.zip.sha256
cd "$ROOT"
python3 verification/verify_rl78_dq_rotation_and_block_scale.py
