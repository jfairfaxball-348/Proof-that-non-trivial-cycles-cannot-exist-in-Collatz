#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
( cd inherited && sha256sum -c RL72_Global_Audit_Lemma_Synthesis_and_Roadmap_2026-08-24.zip.sha256 )
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
unzip -q inherited/RL72_Global_Audit_Lemma_Synthesis_and_Roadmap_2026-08-24.zip -d "$tmp"
cd "$tmp/RL72_Global_Audit_Lemma_Synthesis_and_Roadmap_2026-08-24"
sha256sum -c SHA256SUMS.txt >/dev/null
bash verification/run_fast_rl72_verifiers.sh
cd "$ROOT"
python3 verification/verify_rl73_owned_zero_area_macro.py
echo "FAST_RL73_VERIFIERS PASS"
