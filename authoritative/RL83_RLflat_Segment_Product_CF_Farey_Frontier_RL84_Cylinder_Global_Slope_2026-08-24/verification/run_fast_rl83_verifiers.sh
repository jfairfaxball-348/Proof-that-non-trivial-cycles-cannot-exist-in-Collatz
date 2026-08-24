#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$HERE/verification/verify_rl83_segment_product_farey_frontier.py"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
cd "$HERE/inherited"
sha256sum -c RL82_RLflat_Prefix_Balance_and_First_Surplus_Barrier_RL83_CF_Global_Consumer_2026-08-24.zip.sha256
unzip -q RL82_RLflat_Prefix_Balance_and_First_Surplus_Barrier_RL83_CF_Global_Consumer_2026-08-24.zip -d "$TMP"
INROOT="$(find "$TMP" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
cd "$INROOT"
sha256sum -c SHA256SUMS.txt
bash verification/run_fast_rl82_verifiers.sh
