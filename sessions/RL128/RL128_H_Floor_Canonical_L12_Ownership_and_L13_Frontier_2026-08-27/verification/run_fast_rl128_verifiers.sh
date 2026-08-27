#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
python3 "$HERE/verify_rl128_h_floor.py"
python3 "$HERE/verify_rl128_certificate_audit.py"
WORK="$(mktemp -d /tmp/rl128-fast.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
"${CXX:-c++}" -O3 -std=c++17 "$HERE/verify_rl128_l12_canonical_ownership.cpp" -o "$WORK/scan"
for z in 8 16 23 27 34 36 40; do
  ("$WORK/scan" "$z" "$z" | head -n1 > "$WORK/z${z}.txt") &
done
wait
for z in 8 16 23 27 34 36 40; do
  expected="$(grep "^Z=${z} " "$ROOT/audit/RL128_L12_CANONICAL_OWNERSHIP_CERTIFICATE.txt")"
  actual="$(cat "$WORK/z${z}.txt")"
  test "$actual" = "$expected"
done
echo 'RL128 exact spot-reproduction: PASS (Z=8,16,23,27,34,36,40)'
echo 'RL128 fast verifier suite: PASS'
