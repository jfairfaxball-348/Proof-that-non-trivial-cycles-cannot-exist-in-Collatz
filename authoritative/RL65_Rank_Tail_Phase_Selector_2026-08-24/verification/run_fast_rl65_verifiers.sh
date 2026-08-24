#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 verification/verify_rl65_rank_tail_phase_selector.py
(
  cd inherited
  sha256sum -c RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip.sha256
)
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
unzip -q inherited/RL64_Full_Phase_Recovery_and_All_Word_Cylinder_Selector_2026-08-24.zip -d "$tmp"
rl64="$(find "$tmp" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
(
  cd "$rl64"
  sha256sum -c SHA256SUMS.txt
  bash verification/run_fast_rl64_verifiers.sh
)
echo 'FAST_RL65_VERIFIERS PASS'
