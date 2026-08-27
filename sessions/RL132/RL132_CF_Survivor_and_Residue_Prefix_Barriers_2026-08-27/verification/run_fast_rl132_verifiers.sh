#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_external_cf_gate.py"
python3 "$HERE/verify_rl132_cf_survivor.py"
python3 "$HERE/verify_residue_prefix_barrier.py"
echo "RL132 barrier verifier suite: PASS"
