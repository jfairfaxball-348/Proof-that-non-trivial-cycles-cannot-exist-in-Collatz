#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$HERE/verify_rl108_word_arithmetic.py"
python3 "$HERE/verify_rl108_first_surplus_census.py"
