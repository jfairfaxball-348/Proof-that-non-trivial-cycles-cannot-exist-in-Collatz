#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
sha256sum -c SHA256SUMS_RL60_FREEZE_TO_RL61.txt
python3 verification/verify_rl60_frozen_arithmetic.py
cd inherited_current
sha256sum -c Collatz_Rsharp_RL59_to_RL60_Terminal_Tail_Bootstrap_Handover_2026-08-23.zip.sha256
echo 'RL60 freeze handover integrity: PASS'
