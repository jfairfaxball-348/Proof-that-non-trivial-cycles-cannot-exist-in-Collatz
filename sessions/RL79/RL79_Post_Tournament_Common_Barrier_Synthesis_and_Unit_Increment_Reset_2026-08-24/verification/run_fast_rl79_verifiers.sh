#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL78_DQ_Sensitive_Rotation_Defect_and_Block_Scale_Barrier_2026-08-24.zip.sha256
cd "$ROOT"
python3 verification/verify_rl79_common_barrier_reset.py
