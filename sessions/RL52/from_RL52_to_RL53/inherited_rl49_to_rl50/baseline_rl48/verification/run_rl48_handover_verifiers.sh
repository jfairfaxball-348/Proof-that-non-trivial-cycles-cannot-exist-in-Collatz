#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo '[1/5] RL48 initial internal checksums'
(cd "$ROOT/rl48_initial" && sha256sum -c SHA256SUMS.txt)

echo '[2/5] RL48 initial verifiers'
(cd "$ROOT/rl48_initial" && bash run_all_rl48_progress_verifiers.sh)

echo '[3/5] RL48 continued internal checksums'
(cd "$ROOT/rl48_continued" && sha256sum -c SHA256SUMS.txt)

echo '[4/5] RL48 continued verifiers'
(cd "$ROOT/rl48_continued" && bash run_all_rl48_continued_verifiers.sh)

echo '[5/5] inherited ZIP sidecars'
for sidecar in "$ROOT"/inherited/*.zip.sha256; do
  (cd "$(dirname "$sidecar")" && sha256sum -c "$(basename "$sidecar")")
done

echo 'RL48->RL49 handover verifiers: PASS'
