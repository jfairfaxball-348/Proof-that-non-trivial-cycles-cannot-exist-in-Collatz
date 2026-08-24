#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo '== RL56 aggregate Xi/Psi + 10.7 terminal-compatible prefix certificate =='
out="$(python3 verification/verify_rl56_aggregate_potential_and_legal26.py)"
echo "$out"
grep -q 'RL56 aggregate potential / legal-prefix theorem: PASS' <<<"$out"
grep -q 'terminal-compatible legal first-26 mass <= 107/10' <<<"$out"

echo '== K>=25 tightened 10.3 decision =='
out="$(python3 verification/verify_tight_prefix_fast.py 25 103/10)"
echo "$out"
grep -q 'TARGET 103 10 10.3 hit False' <<<"$out"

echo '== coupled-K nonvacuity witness above 8 =='
out="$(python3 verification/verify_viable_kselector_fast.py 8)"
echo "$out"
grep -q 'TARGET 8 1 8.0 hit True' <<<"$out"
grep -q '^hit ' <<<"$out"

echo 'RL56 EXTENDED PREFIX CHECKS: PASS'
