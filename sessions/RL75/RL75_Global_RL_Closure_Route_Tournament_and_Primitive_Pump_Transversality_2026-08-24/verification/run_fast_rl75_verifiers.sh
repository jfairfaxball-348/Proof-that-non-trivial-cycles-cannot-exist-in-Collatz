#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL74_Ownership_Sensitive_Synchronized_Pump_Law_and_Macro_Barrier_2026-08-24.zip.sha256
cd "$ROOT"
python3 verification/verify_rl75_pump_transversality.py
echo 'FAST_RL75_VERIFIERS PASS'
