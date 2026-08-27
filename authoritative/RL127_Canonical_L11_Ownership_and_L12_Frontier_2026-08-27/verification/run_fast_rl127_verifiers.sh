#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d /tmp/rl127-verify.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
"${CXX:-c++}" -O3 -std=c++17 "$HERE/verify_rl127_l11_canonical_ownership.cpp" -o "$WORK/verify"
"$WORK/verify" > "$WORK/output.txt"
if grep -q '^HIT ' "$WORK/output.txt"; then
  echo 'unexpected divisibility hit' >&2
  exit 1
fi
diff -u "$HERE/../audit/RL127_L11_CANONICAL_OWNERSHIP_CERTIFICATE.txt" "$WORK/output.txt"
echo 'RL127 L11 canonical ownership verifier: PASS'
