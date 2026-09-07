#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
python3 "$here/verify_rl272_height2.py"
python3 "$here/redteam_rl272_height2.py"
echo RL272_FAST_SUITE_PASS
