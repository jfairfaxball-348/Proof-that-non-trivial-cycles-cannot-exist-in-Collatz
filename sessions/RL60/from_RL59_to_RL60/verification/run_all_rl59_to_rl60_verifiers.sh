#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

echo '[1/7] Type-B normalized-P obstruction'
python3 verify_rl59_typeB_normalizedP_obstruction.py

echo '[2/7] defect-compatible four-pump entry witness'
python3 verify_rl59_defect_compatible_fourpump_entry.py

echo '[3/7] final-tail rational forcing'
python3 verify_rl59_final_tail_forcing.py

echo '[4/7] strengthened tail/bootstrap arithmetic'
python3 verify_rl59_strengthened_tail_bootstrap_arithmetic.py

echo '[5/7] compile exact terminal-ancestor searches'
g++ -O3 -std=c++17 search_small_terminal_ancestors.cpp -o search_small_terminal_ancestors.bin
g++ -O3 -std=c++17 search_terminal_ancestors_kmin.cpp -o search_terminal_ancestors_kmin.bin

echo '[6/7] K>=25 boundary'
./search_small_terminal_ancestors.bin 11184809 | tee _k25_below.tmp
./search_small_terminal_ancestors.bin 11184810 | tee _k25_at.tmp
diff -u search_small_terminal_ancestors_below_K25.out _k25_below.tmp
diff -u search_small_terminal_ancestors_at_K25.out _k25_at.tmp

echo '[7/7] K>=27 and K>=29 boundaries'
./search_terminal_ancestors_kmin.bin 13256070 27 | tee _k27_below.tmp
./search_terminal_ancestors_kmin.bin 13256071 27 | tee _k27_at.tmp
./search_terminal_ancestors_kmin.bin 125687198 29 | tee _k29_below.tmp
./search_terminal_ancestors_kmin.bin 125687199 29 | tee _k29_at.tmp
diff -u kmin27_below.out _k27_below.tmp
diff -u kmin27_at.out _k27_at.tmp
diff -u kmin29_below.out _k29_below.tmp
diff -u kmin29_at.out _k29_at.tmp

rm -f search_small_terminal_ancestors.bin search_terminal_ancestors_kmin.bin \
  _k25_below.tmp _k25_at.tmp _k27_below.tmp _k27_at.tmp _k29_below.tmp _k29_at.tmp

echo 'RL59 -> RL60 targeted verifier suite: PASS'
