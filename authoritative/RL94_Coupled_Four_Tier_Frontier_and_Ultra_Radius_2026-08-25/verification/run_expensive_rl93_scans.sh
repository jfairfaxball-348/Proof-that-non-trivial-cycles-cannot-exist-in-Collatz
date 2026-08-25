#!/usr/bin/env bash
set -euo pipefail
# EXPENSIVE: exact replay of RL93 new scans. Not part of normal verification economy.
cd "$(dirname "$0")"
gcc -O3 verify_rl93_scale_scan.c -lgmp -o rl93_scale_scan
mkdir -p replay_rl93
idx=0
for a in $(seq 1100001 25000 1750001); do b=$((a+24999)); printf -v f 'deep_rl93_%03d_%d_%d.txt' "$idx" "$a" "$b"; ./rl93_scale_scan 10000056 "$a" "$b" > "replay_rl93/$f"; idx=$((idx+1)); done
idx=0
for a in $(seq 1250001 25000 3500001); do b=$((a+24999)); printf -v f 'mid_rl93_%03d_%d_%d.txt' "$idx" "$a" "$b"; ./rl93_scale_scan 7500056 "$a" "$b" > "replay_rl93/$f"; idx=$((idx+1)); done
# Ultra chunks used in RL93:
./rl93_scale_scan 15000056 1001 5000 > replay_rl93/ultra_rl93_000_1001_5000.txt
idx=1
for a in 5001 10001 15001 20001 25001 30001; do b=$((a+4999)); printf -v f 'ultra_rl93_%03d_%d_%d.txt' "$idx" "$a" "$b"; ./rl93_scale_scan 15000056 "$a" "$b" > "replay_rl93/$f"; idx=$((idx+1)); done
echo "Expensive RL93 scan replay complete."
