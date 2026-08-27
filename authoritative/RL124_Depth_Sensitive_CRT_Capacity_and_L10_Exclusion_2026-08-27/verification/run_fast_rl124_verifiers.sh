#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
WORK="$(mktemp -d /tmp/rl124-verify.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
"${CXX:-c++}" -O3 -std=c++17 "$HERE/verify_rl124_depth_sensitive_capacity.cpp" -o "$WORK/verify"
"$WORK/verify" > "$WORK/output.txt"
if grep -q '^HIT ' "$WORK/output.txt"; then
  echo 'unexpected divisibility hit' >&2
  exit 1
fi
diff -u "$HERE/../audit/RL124_L10_PROFILE_OWNERSHIP_CERTIFICATE.txt" "$WORK/output.txt"
echo 'RL124 depth-sensitive capacity verifier: PASS'
