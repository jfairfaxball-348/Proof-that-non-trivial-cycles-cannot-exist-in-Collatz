#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 -S "$ROOT/verification/verify_rl233_finite_modulus_decomposition.py"
python3 -S "$ROOT/verification/verify_rl233_proof_state.py"
