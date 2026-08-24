#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL71_Finite_Window_Backward_Operator_Q5_Phase_and_Mod162_Lift_2026-08-24.zip.sha256
cd "$ROOT"
python3 verification/verify_rl72_audit_corollaries.py
echo 'FAST_RL72_VERIFIERS PASS'
