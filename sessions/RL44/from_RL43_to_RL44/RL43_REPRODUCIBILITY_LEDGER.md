# RL43 reproducibility ledger

Date: 2026-08-22

## Fast theorem/certificate suite

Run:

`bash verification/run_all_rl43_verifiers.sh`

Expected: all four RL43 verifiers print `PASS`.

### `verify_rl43_rho49_elimination.py`

Expected key lines:

- targeted 2-adic prefix nodes = 7670
- `(45,4)` near survivors `(130,82,1)`, `(149,94,1)`
- `(44,5)` near survivor `(130,82)`
- `(43,6)` near survivor `(130,82)`
- certified consequence `rho>=50`

### `verify_rl43_defect_support_radius3_bridge.py`

Expected key lines:

- equal-weight pairs exhausted through `n=9`
- pairs checked = 66196
- support sanity `support <= 4(E+N)`

### `verify_rl43_gap9_cutofffree.py`

Expected key lines:

- state counts `[3,9,18,31,49,72,100,134,180]`
- first crossing `e=8`, outgoing gap 4, terminal `T=7`

### `verify_rl43_full_denominator_phase_bridge.py`

Expected key lines:

- explicit countermodel `(a,ell)=(65,41)`, `e=26`
- proper factor passes while full `D` divisibility fails as intended
- small factor identities checked = 575

## Heavy exact phase scan

This is not part of the fast master verifier because it carries large exact residue sets.

Recorded outputs are in `verification/PHASE_E40_RUN.txt`. Re-run during audit, preferably independently or after code review.

## Environment

Python 3 standard library only for included RL43 scripts. No network access is required.
