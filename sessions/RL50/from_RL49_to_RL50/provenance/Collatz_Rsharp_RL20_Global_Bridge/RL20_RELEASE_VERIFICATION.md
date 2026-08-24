# RL20 release verification

Date: 2026-08-20

All eight RL20 verifiers were rerun freshly immediately before packaging this handover and passed.

| Verifier | Result |
|---|---|
| `verify_rl20_bounded_bridge_countermodel.py` | PASS |
| `verify_rl20_global_cf_gate.py` | PASS |
| `verify_rl20_block_coboundary.py` | PASS |
| `verify_rl20_final_return_cf_decoupling.py` | PASS |
| `verify_rl20_hard_root_second_low.py` | PASS |
| `verify_rl20_final_return_phase_compatibility.py` | PASS |
| `verify_rl20_hard_universal_global_numerator.py` | PASS |
| `verify_rl20_near_gcd_block_geometry.py` | PASS |

Key exact outputs include:

- length-184 local countermodel: all-rotation minimum distance `4` at shifts `(0,19)`;
- reduced CF denominator floor: `q>=49,547,666,544` conditional on `R#>=2^71`;
- block coboundary: `2,645` exact rational word/block checks;
- repaired weak-close class: unique `t_close=1` hard class `R#==91 mod144`;
- fixed-endpoint numerator verifier: `511` exhaustive small-word checks;
- first narrow undercritical rescue reaching `2^71`: `(m,p)=(195,123)`;
- reduced canonical block length: `a>=78,450,472,029` conditional on the same external floor.

Raw outputs are in `logs/`.

The inherited RL19 bundle, including its own radius-3 release verification and dependency audit, is preserved unchanged under `inherited/`.
