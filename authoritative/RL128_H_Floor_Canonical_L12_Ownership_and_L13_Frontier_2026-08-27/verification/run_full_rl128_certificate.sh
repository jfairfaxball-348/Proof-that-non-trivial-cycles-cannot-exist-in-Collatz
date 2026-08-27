#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
WORK="$(mktemp -d /tmp/rl128-full.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
"${CXX:-c++}" -O3 -std=c++17 "$HERE/verify_rl128_l12_canonical_ownership.cpp" -o "$WORK/scan"
JOBS="${RL128_JOBS:-5}"
seq 8 40 | xargs -P "$JOBS" -I{} bash -c '"$0" "$1" "$1" | head -n1 > "$2/z$1.txt"' "$WORK/scan" {} "$WORK"
{
  echo '# RL128 L=12 canonical constrained ownership certificate'
  for z in $(seq 8 40); do cat "$WORK/z${z}.txt"; done
  python3 - "$WORK" <<'PY'
import re,sys,pathlib
w=pathlib.Path(sys.argv[1]); keys=['capacity_profiles','periodic','canonical_primitive_profiles','orbit_weight','canonical_roots_tested','divisibility_hits']; t={k:0 for k in keys}
for z in range(8,41):
    line=(w/f'z{z}.txt').read_text()
    for k in keys:t[k]+=int(re.search(k+r'=(\d+)',line).group(1))
print('TOTAL '+' '.join(f'{k}={t[k]}' for k in keys))
PY
} > "$WORK/certificate.txt"
diff -u "$ROOT/audit/RL128_L12_CANONICAL_OWNERSHIP_CERTIFICATE.txt" "$WORK/certificate.txt"
echo 'RL128 full exact certificate reproduction: PASS'
