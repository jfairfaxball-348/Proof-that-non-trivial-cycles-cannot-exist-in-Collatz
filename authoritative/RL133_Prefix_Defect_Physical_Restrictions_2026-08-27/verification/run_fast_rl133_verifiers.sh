#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d /tmp/rl133-verify.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
python3 "$HERE/verify_rl133_prefix_defect.py" > "$WORK/output.txt"
diff -u "$HERE/../audit/RL133_EXACT_CONSTANTS.txt" "$WORK/output.txt"
echo "RL133 fast verifier suite: PASS"
