#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
./verification/run_fast_rl64_verifiers.sh
./verification/inherited_rl63/run_full_rl63_verifiers.sh
echo 'FULL_RL64_VERIFIERS PASS'
