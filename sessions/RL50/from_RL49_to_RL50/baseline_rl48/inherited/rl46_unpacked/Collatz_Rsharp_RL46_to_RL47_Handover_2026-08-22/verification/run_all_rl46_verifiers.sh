#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
bash "$HERE/run_rl46_structural_verifiers.sh"
bash "$HERE/run_rl46_q55_verifier.sh"
echo 'ALL RL46 CORE VERIFIERS PASSED'
