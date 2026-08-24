#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NEW="$ROOT/verification/new_rl57"
BUILD="${TMPDIR:-/tmp}/rl57_to_rl58_build_$$"
mkdir -p "$BUILD"
trap 'rm -rf "$BUILD"' EXIT

echo '[1/6] verify inherited RL56->RL57 outer checksum'
(
  cd "$ROOT/inherited_rl56_to_rl57"
  sha256sum -c Collatz_Rsharp_RL56_to_RL57_Audit_Handover_2026-08-23.zip.sha256
)

echo '[2/6] compile independent 33/4 audit'
g++ -O3 -std=c++17 "$NEW/independent_viable_33_4.cpp" -o "$BUILD/independent_viable_33_4"
"$BUILD/independent_viable_33_4" | tee "$BUILD/independent_viable_33_4.out"
grep -F 'TARGET 33/4 hit False' "$BUILD/independent_viable_33_4.out" >/dev/null
grep -F 'nodes 3676571 states 542063' "$BUILD/independent_viable_33_4.out" >/dev/null

echo '[3/6] compile/run defect-aware 77/10 discovery certificate'
g++ -O3 -std=c++17 "$NEW/defect_viable_search_pareto.cpp" -o "$BUILD/defect_viable_search_pareto"
"$BUILD/defect_viable_search_pareto" 77/10 | tee "$BUILD/defect_viable_77_10.out"
grep -F 'target=77/10 hit=0' "$BUILD/defect_viable_77_10.out" >/dev/null

echo '[4/6] compile/run aligned 17/3 discovery certificate'
g++ -O3 -std=c++17 "$NEW/aligned_prefix_search.cpp" -o "$BUILD/aligned_prefix_search"
"$BUILD/aligned_prefix_search" 17/3 | tee "$BUILD/aligned_prefix_17_3.out"
grep -F 'target=17/3 hit=0' "$BUILD/aligned_prefix_17_3.out" >/dev/null

echo '[5/6] rerun target-8 witness generator (exit 2 is expected because a target-8 hit exists)'
g++ -O3 -std=c++17 "$NEW/independent_viable_8_path.cpp" -o "$BUILD/independent_viable_8_path"
set +e
"$BUILD/independent_viable_8_path" > "$BUILD/target8.out" 2>&1
st=$?
set -e
cat "$BUILD/target8.out"
if [[ "$st" -ne 2 ]]; then
  echo "unexpected target-8 verifier exit status: $st" >&2
  exit 1
fi
grep -F 'TARGET 8 hit True' "$BUILD/target8.out" >/dev/null

echo '[6/6] exact defect replay of target-8 witness'
python3 "$NEW/verify_target8_witness_defect.py"

echo 'PASS: RL57->RL58 current verifier suite'
echo 'NOTE: 77/10 and 17/3 are reproducible discovery certificates, not independently audited certificates.'
