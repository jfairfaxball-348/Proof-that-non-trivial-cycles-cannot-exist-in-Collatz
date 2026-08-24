# RL43 one-excursion `e<=40` exact phase computation ledger

Date: 2026-08-22

## Status

**EXACT COMPUTATION, AUDIT PENDING.** This is not promoted to an analytic theorem in the handover.

The calculation combines:

1. a cutoff-free quotient-state automaton with the neutral `(d,T)=(1,-2)` `11` pump represented parametrically;
2. near-resonance, gcd, inherited `rho>=50`, endpoint ownership, and exact effective-mass feasibility filters;
3. an exact forward/backward pruned dynamic program carrying all possible `V mod M` residues, where `M=2^65-3^41`;
4. the full-denominator requirement `V == -4*3^41 (mod M)`.

## 1. Normalized admissible geometry families through `e=40`

After normalizing away the pump-length bookkeeping, every coarse survivor has

`(a,ell,q)=(65,41,24)`.

The geometry families are:

- `(z,t,g_out)=(24,0,4)` for `e=26..40`;
- `(22,2,16)` for `e=30..40`;
- `(20,4,64)` for `e=34..40`;
- `(18,6,256)` for `e=35..40`.

Note the `t=6` family begins at `e=35`, correcting an earlier conversational statement that said `e=37`.

## 2. Exact residue counts; all required-residue hits are false

### `z=24, t=0`

`e: count`

- 26: 16
- 27: 172
- 28: 977
- 29: 3941
- 30: 12036
- 31: 28855
- 32: 58119
- 33: 102696
- 34: 163204
- 35: 242413
- 36: 343965
- 37: 472073
- 38: 643706
- 39: 871236
- 40: 1176006

### `z=22, t=2`

- 30: 23
- 31: 159
- 32: 678
- 33: 2081
- 34: 5021
- 35: 10571
- 36: 20529
- 37: 36933
- 38: 63215
- 39: 103329
- 40: 163066

### `z=20, t=4`

- 34: 9
- 35: 3
- 36: 27
- 37: 39
- 38: 93
- 39: 130
- 40: 237

### `z=18, t=6`

- 35: 3
- 36: 3
- 37: 6
- 38: 15
- 39: 22
- 40: 34

For every listed case, the Boolean test

`(-4*3^41 mod M) in residue_set`

is `False`.

## 3. Conservative consequence

If RL44 independently confirms both the geometry exhaustion and the residue DP, then the one-excursion sector has no solution with `e<=40`, so its computational frontier is

> **`e>=41`.**

Do not use this as a uniform theorem; it is a finite exact certificate over defect, not a proof for all `e`.

## 4. Reproduction

Core scripts are under `rl43_exploratory/`:

- `search_one_excursion_survivors.py`
- `explore_one_excursion_quotient.py`
- `exact_phase_geometry.py`
- `batch_phase_geometry.py`

The phase DP can be run by geometry family rather than all at once to reduce peak runtime/memory. See `verification/PHASE_E40_RUN.txt` for the recorded commands/output.
