#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo '== RL55 independent legal-26 certificate =='
python3 rl55_audit/verify_rl55_legal26_independent.py

echo '== inherited RL54->RL55 lightweight audit suite =='
bash verification/run_all_rl54_audit_verifiers.sh

echo 'ALL RL55->RL56 HANDOVER VERIFIERS: PASS'
