#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 -S "$ROOT/verification/verify_rl232_h17_cross_family.py"
python3 -S "$ROOT/verification/verify_rl232_relaxed_h17_graph_barrier.py"
python3 -S "$ROOT/verification/verify_rl232_h17_physical_scalar_graph.py"
python3 -S "$ROOT/verification/verify_rl232_h17_owned_prefix_graph.py"
python3 -S "$ROOT/verification/verify_rl232_h17_moving_window_saturation.py"
python3 -S "$ROOT/verification/verify_rl232_proof_state.py"
