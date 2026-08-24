#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL67_Previous_Active_Interface_and_HeightOne_Reachability_2026-08-24.zip.sha256
cd "$ROOT"
python3 verification/verify_rl68_nested_descent.py
printf '%s\n' 'FAST_RL68_VERIFIERS PASS'
