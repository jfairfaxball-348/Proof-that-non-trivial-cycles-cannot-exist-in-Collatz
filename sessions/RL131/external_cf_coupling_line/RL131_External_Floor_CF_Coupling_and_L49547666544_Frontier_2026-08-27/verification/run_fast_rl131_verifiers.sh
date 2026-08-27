#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify_inherited_minimum_coupling.py"
python3 "$HERE/verify_external_cf.py"
echo "RL131 external-floor verifier suite: PASS"
