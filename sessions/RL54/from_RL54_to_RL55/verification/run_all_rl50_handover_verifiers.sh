#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INH="$ROOT/inherited_rl49_to_rl50"
R50="$ROOT/rl50_research"

echo '=== [1/4] inherited RL48 baseline ==='
(cd "$INH/baseline_rl48" && bash verification/run_rl48_handover_verifiers.sh)

echo '=== [2/4] inherited RL49 mathematics with portable path repair ==='
python "$ROOT/verification/verify_rl49_half_rotation_metric_portable.py"
(cd "$INH/rl49_research" && python phase_squeeze/verify_rl49_phase_resonance_squeeze.py)
(cd "$INH/rl49_research" && python phase_squeeze/verify_rl49_height1_mass_telescoping.py)
# Historical arithmetic verifier retained for reproducibility only. RL50 demotes
# the Ansari external-floor premise; do not promote its stronger floor.
(cd "$INH/rl49_research" && python phase_squeeze/verify_rl49_ansari_floor_and_farey_extension.py)
(cd "$INH/rl49_research" && python phase_squeeze/verify_rl49_zero_position_telescoping.py)

echo '=== [3/4] recovered/source ZIP integrity ==='
python - "$INH/recovered_bundles" "$ROOT/source_bundle" <<'PY'
import sys, zipfile, pathlib
for d in map(pathlib.Path, sys.argv[1:]):
    for p in sorted(d.glob('*.zip')):
        with zipfile.ZipFile(p) as z:
            bad=z.testzip()
            assert bad is None,(p,bad)
            assert z.namelist(),p
            print(p.name,'ZIP OK')
PY

echo '=== [4/4] RL50 new verifiers ==='
for f in \
  verify_rl50_external_floor_audit.py \
  verify_rl50_lift_zero_budget.py \
  verify_rl50_monotone_J_lift_defect_energy.py \
  verify_rl50_defect_energy_localization.py \
  verify_rl50_zero_displacement_excursion_macros.py
 do
   echo "--- $f"
   python "$R50/$f"
 done

echo 'RL50->RL51 handover verifiers: PASS'
