#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d /tmp/rl126-verify.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
"${CXX:-c++}" -O3 -std=c++17 "$HERE/verify_rl126_corrected_l10.cpp" -o "$WORK/verify"
"$WORK/verify" > "$WORK/output.txt"
if grep -q '^HIT ' "$WORK/output.txt"; then
  echo 'unexpected divisibility hit' >&2
  exit 1
fi
diff -u "$HERE/../audit/RL126_CORRECTED_L10_CERTIFICATE.txt" "$WORK/output.txt"
echo 'RL126 corrected L10 verifier: PASS'
