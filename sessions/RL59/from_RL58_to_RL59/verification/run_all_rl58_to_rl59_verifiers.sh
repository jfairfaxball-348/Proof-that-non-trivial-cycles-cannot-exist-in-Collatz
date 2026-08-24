#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo '[1/7] inherited RL57->RL58 outer checksum'
(
  cd inherited_rl57_to_rl58
  sha256sum -c Collatz_Rsharp_RL57_to_RL58_Audit_Handover_2026-08-23.zip.sha256
)

echo '[2/7] independent aligned-prefix 17/3 audit'
g++ -O3 -std=c++17 verification/rl58_audit/independent_aligned_gap_search.cpp -o /tmp/rl58_aligned_gap_audit
/tmp/rl58_aligned_gap_audit | tee /tmp/rl58_aligned_gap_audit.out
grep -q 'RL58_GAP_AUDIT target=17/3 hit=0' /tmp/rl58_aligned_gap_audit.out
rm -f /tmp/rl58_aligned_gap_audit /tmp/rl58_aligned_gap_audit.out

echo '[3/7] independent total-prefix 77/10 audit'
g++ -O3 -std=c++17 verification/rl58_audit/independent_total_gap_search.cpp -o /tmp/rl58_total_gap_audit
/tmp/rl58_total_gap_audit | tee /tmp/rl58_total_gap_audit.out
grep -q 'RL58_GAP_TOTAL_AUDIT target=77/10 hit=0' /tmp/rl58_total_gap_audit.out
rm -f /tmp/rl58_total_gap_audit /tmp/rl58_total_gap_audit.out

echo '[4/7] local r=0/r=1 grammar and terminal LTE regression'
python3 verification/rl58_audit/verify_rl58_local_grammar.py

echo '[5/7] exact positive synchronized-cycle obstruction'
python3 verification/rl58_audit/verify_rl58_positive_cycle_obstruction.py

echo '[6/7] exact arbitrary m-pump formula'
python3 verification/rl58_audit/verify_rl58_cycle_block_formula.py

echo '[7/7] sharpened Psi cut from audited 77/10 + inherited phase squeeze'
python3 verification/rl58_audit/verify_rl58_sharp_psi_cut.py

echo 'RL58->RL59 verification suite: PASS'
