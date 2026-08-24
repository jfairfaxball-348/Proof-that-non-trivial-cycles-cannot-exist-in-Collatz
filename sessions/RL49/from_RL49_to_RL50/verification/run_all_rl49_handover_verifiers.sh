#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo '[1/7] repaired RL48->RL49 baseline'
(cd "$ROOT/baseline_rl48" && bash verification/run_rl48_handover_verifiers.sh)

echo '[2/7] RL49 half-rotation metric'
(cd "$ROOT/rl49_research" && python verify_rl49_half_rotation_metric.py)

echo '[3/7] RL49 phase resonance squeeze'
(cd "$ROOT/rl49_research" && python phase_squeeze/verify_rl49_phase_resonance_squeeze.py)

echo '[4/7] RL49 height-one telescoping'
(cd "$ROOT/rl49_research" && python phase_squeeze/verify_rl49_height1_mass_telescoping.py)

echo '[5/7] RL49 strengthened external-floor/Farey arithmetic'
(cd "$ROOT/rl49_research" && python phase_squeeze/verify_rl49_ansari_floor_and_farey_extension.py)

echo '[6/7] RL49 zero-position telescoping'
(cd "$ROOT/rl49_research" && python phase_squeeze/verify_rl49_zero_position_telescoping.py)

echo '[7/7] recovered bundle integrity against release manifest'
# Full per-file release hashes are checked separately by SHA256SUMS.txt; here ensure ZIPs are readable.
python - "$ROOT" <<'PY'
import sys, zipfile, pathlib
root=pathlib.Path(sys.argv[1])
for p in sorted((root/'recovered_bundles').glob('*.zip')):
    with zipfile.ZipFile(p) as z:
        bad=z.testzip()
        assert bad is None, (p,bad)
        assert z.namelist(), p
        print(p.name, 'ZIP OK')
PY

echo 'RL49->RL50 handover verifiers: PASS'
