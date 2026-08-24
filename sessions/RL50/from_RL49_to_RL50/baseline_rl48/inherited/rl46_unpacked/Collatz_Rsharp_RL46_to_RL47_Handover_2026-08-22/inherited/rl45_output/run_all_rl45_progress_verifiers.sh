#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python "$HERE/verify_rl45_terminal_H23.py"
python "$HERE/verify_rl45_resultant_obstruction.py"
