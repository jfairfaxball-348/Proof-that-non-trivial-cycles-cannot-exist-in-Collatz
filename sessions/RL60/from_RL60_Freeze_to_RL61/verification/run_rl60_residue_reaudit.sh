#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
BIN="$HERE/residue_interval_cert"
SRC="$HERE/residue_interval_cert.cpp"
OUT="$HERE/replay_outputs"
mkdir -p "$OUT"
g++ -O3 -std=c++17 "$SRC" -o "$BIN"
run_interval(){ local L="$1" U="$2" K="$3" tag="$4"; echo "[$tag] [$L,$U] KMIN=$K"; "$BIN" "$L" "$U" "$K" | tee "$OUT/${tag}_${L}_${U}.out"; }
K35=10180663219; K37=45812984490; step=4000000000; L=$((K35+1)); i=0
while [ "$L" -lt "$K37" ]; do U=$((L+step-1)); if [ "$U" -ge "$K37" ]; then U=$((K37-1)); fi; run_interval "$L" "$U" 37 "k37_chunk$(printf '%02d' "$i")"; L=$((U+1)); i=$((i+1)); done
set +e; "$BIN" "$K37" "$K37" 37 | tee "$OUT/k37_boundary.out"; rc=$?; set -e
if [ "$rc" -eq 0 ]; then echo 'ERROR: K37 boundary unexpectedly certified hit-free' >&2; exit 10; fi
while read -r L U; do [ -n "${L:-}" ] || continue; run_interval "$L" "$U" 39 "k39"; done < "$HERE/k39_replay_intervals_original_session.txt"
K39=122167958641
set +e; "$BIN" "$K39" "$K39" 39 | tee "$OUT/k39_boundary.out"; rc=$?; set -e
if [ "$rc" -eq 0 ]; then echo 'ERROR: K39 boundary unexpectedly certified hit-free' >&2; exit 11; fi
echo "Residue replay completed. Inspect logs in $OUT and audit source independently."
