# RL20 handover — start here

Date: 2026-08-20

## Exact current status

- **RL remains OPEN.** No proof of the global RL statement is claimed.
- **Exact radius 3 remains CLOSED for the inherited proof chain.** Do not redo its branch analysis unless a verifier fails.
- The old bridge “least-root/final-return local grammar alone forces a radius-3 rotation pair” is **formally false**. The exact length-184 local model has all-rotation minimum adjacent-transposition distance exactly `4` and satisfies the inherited local slope/endpoint grammar, but it is not an RL object because `D does not divide Q`.
- Therefore radius 3 is not wasted; it is a sharp local obstruction awaiting a genuinely global entry theorem. Any viable bridge must use `D|Q`, cycle-state ownership, a weighted rotation difference, or equivalent global arithmetic.

## Fresh RL20 release gate

Run these eight verifiers before extending anything:

1. `python verify_rl20_bounded_bridge_countermodel.py`
2. `python verify_rl20_global_cf_gate.py`
3. `python verify_rl20_block_coboundary.py`
4. `python verify_rl20_final_return_cf_decoupling.py`
5. `python verify_rl20_hard_root_second_low.py`
6. `python verify_rl20_final_return_phase_compatibility.py`
7. `python verify_rl20_hard_universal_global_numerator.py`
8. `python verify_rl20_near_gcd_block_geometry.py`

All eight passed freshly when this bundle was released. Treat any failure as a stop-and-repair event.

## Main new global geometry

Write

`g=gcd(A,L)`, `A=ga`, `L=g ell`, and at the canonical `a`-step block cuts define

`E_j=K_j-j ell`.

In the near-resonant branch `lambda=2^A/3^L<16/15`, least-state suffix domination gives

`E_j>=0`

for every proper canonical block cut. The block imbalance path is therefore a nonnegative excursion from `0` back to `0`.

At a proper block cut with state `x_j`:

- if `E_j=0`, then
  `R# < x_j < (16/15)R#`,
  and `x_j` is necessarily **odd**;
- if `E_j>=1`, then
  `x_j > (45/16)R#`.

Thus there are two sharply separated cases.

### Case B — balanced return

Some proper `E_j=0`. Then there is a second genuine odd cycle rotation with exact reduced-slope balance and physical height below `16R#/15`.

This is the **primary next target**: use the arbitrary-rotation weighted-difference identity, `D|Q`, or a transportation/radius estimate to prove that such a second exact-balanced near-minimum rotation either

1. lies within the already-closed radius-3 regime, or
2. creates a direct contradiction without radius language.

Do not assume either conclusion. Prove or falsify the sharpest candidate statement.

### Case S — strict excursion

If there is no proper balanced cut, then every proper canonical block boundary lies above `45R#/16`. Use the monotone normalized coboundary lift

`H_j=z^j 3^{-E_j}x_j`

inside the narrow strip `(R#,lambda R#]` together with the large physical height jumps to seek a global packing/weighted-difference contradiction.

This is the secondary parallel track.

## Other frozen RL20 results

- Every actual phase state is nonzero mod `3`; in the k=0 branch this sharpens odd-state packing.
- Conditional on the inherited external input `R#>=2^71`, the reduced denominator obeys
  `L/gcd(A,L) >= 49,547,666,544`, without LMN.
- Consequently the canonical reduced block length satisfies
  `a>=78,450,472,029`.
- The raw canonical block polynomial is an exact state coboundary and telescopes back to `Q=R#D`; bare proper-factor divisibility is therefore tautological and should not be retried without extra one-sided state information.
- The direct final-return-address/continued-fraction sieve is a proved no-go at endpoint-only level.
- Phase compatibility repairs the hard weak-close branch: `t_close=1` survives only for
  `R# == 91 (mod144), n_close=t_close=1`.
- In that unique weak-close branch, fixed endpoint bits plus `D|Q` give
  `(R#-1/4)(lambda-1) >= 61/36 - 3(2/3)^L`,
  hence using inherited `L>=92`,
  `lambda-1 > 5/[3(R#-1/4)]`.
- In the same hard weak-close branch, either another low-excess plateau exists or the cycle falls into the huge-length branch `L>1+6R#/5` (conditional on `R#>=2^71`).

## Read next

1. `RL20_PROOF_STATUS_AND_NEXT_ATTACK.md`
2. `RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md`
3. `RL20_HARD_UNIVERSAL_GLOBAL_NUMERATOR_LOWER_BOUND.md`
4. `RL20_FINAL_RETURN_PHASE_COMPATIBILITY.md`
5. `RL20_BOUNDED_RADIUS_BRIDGE_COUNTERMODEL.md`
6. `RL20_CANONICAL_BLOCK_COBOUNDARY.md`

The complete inherited RL19 handover is nested under `inherited/`.
