#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo '== inherited RL55->RL56 verifier suite =='
bash inherited_rl55_to_rl56/verification/run_all_rl55_handover_verifiers.sh

echo '== inherited RL45 H<=23 quotient certificate (fresh direct copy) =='
python3 verification/verify_rl45_terminal_H23.py

echo '== RL56 coupled-K viable-prefix 33/4 decision =='
out="$(python3 verification/verify_viable_kselector_fast.py 33/4)"
echo "$out"
grep -q 'TARGET 33 4 8.25 hit False' <<<"$out"

echo '== RL56 arithmetic consequences =='
python3 verification/verify_rl56_session_consequences.py

echo 'ALL RL56->RL57 CORE AUDIT HANDOVER VERIFIERS: PASS'
echo 'Run bash verification/run_rl56_extended_prefix_checks.sh for the slower Xi/Psi 10.7, K>=25 10.3, and witness reruns.'
