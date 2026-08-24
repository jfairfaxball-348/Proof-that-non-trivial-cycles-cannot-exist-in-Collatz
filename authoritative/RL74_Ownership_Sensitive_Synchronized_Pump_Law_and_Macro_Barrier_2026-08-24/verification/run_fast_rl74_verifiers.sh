#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/inherited"
sha256sum -c RL73_Ownership_Forced_Zero_Area_Macro_and_Low_K_Localization_2026-08-24.zip.sha256
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
unzip -q RL73_Ownership_Forced_Zero_Area_Macro_and_Low_K_Localization_2026-08-24.zip -d "$TMP"
R73="$(find "$TMP" -mindepth 1 -maxdepth 1 -type d | head -n1)"
(cd "$R73" && sha256sum -c SHA256SUMS.txt >/dev/null && bash verification/run_fast_rl73_verifiers.sh >/dev/null)
cd "$ROOT"
python3 verification/verify_rl74_synchronized_pump_law.py
echo 'FAST_RL74_VERIFIERS PASS'
