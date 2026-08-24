#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
./run_fast_rl63_verifiers.sh
CXX="${CXX:-g++}"
"$CXX" -O2 -std=c++17 verify_rl62_rl45_H24_extension_struct.cpp -o /tmp/rl63_h24_struct
/tmp/rl63_h24_struct > /tmp/rl63_h24_struct.out
diff -u RL62_RL45_H24_EXTENSION_STRUCT.out /tmp/rl63_h24_struct.out
"$CXX" -O2 -std=c++17 verify_rl62_rl45_H24_extension_packed.cpp -o /tmp/rl63_h24_packed
/tmp/rl63_h24_packed > /tmp/rl63_h24_packed.out
diff -u RL62_RL45_H24_EXTENSION_PACKED.out /tmp/rl63_h24_packed.out
echo 'FULL_RL63_VERIFIERS PASS'
