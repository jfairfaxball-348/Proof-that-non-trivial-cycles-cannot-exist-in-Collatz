#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_rl53_z37_bootstrap.py
python3 verify_rl53_z39_bootstrap.py
python3 verify_rl53_chunk_certificates.py

echo 'RL53 preserved frontier checks: PASS'
echo 'For independent terminal recomputation, compile the C++ sources and rerun the classes listed in RL53_EXACT_TERMINAL_RESULTS.txt.'
