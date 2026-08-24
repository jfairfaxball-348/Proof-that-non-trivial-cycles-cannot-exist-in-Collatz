#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo '== RL54 uniform defect recurrence =='
python3 rl54_research/verify_rl54_uniform_defect_recurrence.py

echo '== RL54 z=41 self-seeding recurrence =='
python3 rl54_research/verify_rl54_z41_self_seeding_recurrence.py

echo '== RL54 legal-prefix / uniform obstruction =='
python3 rl54_research/verify_rl54_legal_prefix_mass_and_uniform_obstruction.py

echo '== RL53 z=37 bootstrap =='
python3 rl53_research/verify_rl53_z37_bootstrap.py

echo '== RL53 z=39 bootstrap =='
python3 rl53_research/verify_rl53_z39_bootstrap.py

echo '== RL53 heavy chunk certificate audit =='
python3 rl53_research/verify_rl53_chunk_certificates.py

echo 'ALL LIGHTWEIGHT RL54->RL55 AUDIT VERIFIERS: PASS'
