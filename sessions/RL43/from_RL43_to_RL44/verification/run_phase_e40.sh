#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$HERE/rl43_exploratory"
run_case() {
  local z="$1" t="$2" T="$3" lo="$4" hi="$5"
  python3 - "$z" "$t" "$T" "$lo" "$hi" <<'PY'
from batch_phase_geometry import batch
import sys
z,t,T,lo,hi=map(int,sys.argv[1:])
Es=list(range(lo,hi+1))
out,fs,gs=batch(65,41,z,t,T,Es)
assert all(hit is False for _,hit in out.values())
print('z,t=',z,t,'results=',out,'forward/backward=',fs,gs,flush=True)
PY
}
run_case 24 0 7 26 40
run_case 22 2 31 30 40
run_case 20 4 127 34 40
run_case 18 6 511 35 40
echo 'PHASE E<=40 REQUIRED-RESIDUE TESTS: PASS'
