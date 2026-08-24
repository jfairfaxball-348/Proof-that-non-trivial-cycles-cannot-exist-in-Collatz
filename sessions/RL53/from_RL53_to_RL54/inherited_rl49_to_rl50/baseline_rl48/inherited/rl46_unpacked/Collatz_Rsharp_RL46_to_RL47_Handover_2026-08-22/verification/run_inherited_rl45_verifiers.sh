#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
bash "$HERE/inherited/rl45_output/run_all_rl45_progress_verifiers.sh"
