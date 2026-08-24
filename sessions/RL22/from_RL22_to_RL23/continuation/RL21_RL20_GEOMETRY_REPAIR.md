# RL21 — repair of the RL20 normalized block-lift increment

Date: 2026-08-20

## Status

**ANALYTIC REPAIR + EXACT FINITE WITNESS.**

This note repairs one displayed identity in `RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md`. The eight RL20 release scripts all pass, but the near-geometry verifier did not test this displayed coboundary increment.

The repair does **not** reopen the radius-3 closure. It does materially weaken the proposed strict-excursion packing route.

## 1. Setup

Use the RL20 canonical block notation

- `A=g a`, `L=g ell`,
- `X=2^a`, `Y=3^ell`, `z=X/Y`,
- `E_j=K_j-j ell`,
- `x_j` the phase state at block cut `j a`,
- `y_j=3^(-E_j)x_j`,
- `H_j=z^j y_j`.

RL20-B.3 is correct:

`3^(-E_(j+1)) Q(B_j) = X y_(j+1)-Y y_j`.

## 2. Correct normalized-lift increment

Since `X=zY`, multiply RL20-B.3 by `z^j/Y`:

`H_(j+1)-H_j`

`= z^j [z y_(j+1)-y_j]`

`= z^j 3^(-E_(j+1)) Q(B_j)/Y`.                         (R21R.1)

Thus the correct formula is

> **`H_(j+1)-H_j = z^j 3^(-E_(j+1)) Q(B_j)/Y`.**

The displayed RL20 equation R20G.12 omitted the factor `3^(-E_(j+1))`.

Monotonicity survives because the omitted factor is positive:

`H_(j+1)>=H_j`, with strict inequality for every nonempty block numerator.

The strip statement also survives unchanged:

`H_0=R#`, `H_g=lambda R#`, and every proper `H_j` lies in `(R#,lambda R#]`.

## 3. Why this matters for the strict-excursion track

The omitted factor is exactly the normalization that cancels the large physical height multiplier attached to a positive imbalance.

If `E_j` is large, the physical block state is of size roughly `3^(E_j)R#`, but the block contribution to the narrow lift is suppressed by `3^(-E_(j+1))`.

Therefore the heuristic

> repeated physical factor-3 excursions must consume correspondingly large width in the normalized strip

is false at the coboundary level.

Any strict-excursion contradiction must add information not already present in the normalized coboundary, for example integer/residue ownership inside blocks, a proper-factor condition, or a separate population inequality.

## 4. Exact witness from the frozen RL20 184-bit word

The already-frozen RL20 local countermodel has

`A=184`, `L=116`, `g=4`, `a=46`, `ell=29`,

and at canonical cuts

`E=(0,1,1,1,0)`.

Its exact rational fixed orbit `R=Q/D` is positive and has its unique least rational phase at the root. The three proper block-cut states satisfy approximately

`x_1/R = 3.005979...`,

`x_2/R = 3.006359...`,

`x_3/R = 3.004953...`,

so all three sit well above the RL20 strict-excursion threshold `45R/16`.

Nevertheless the corrected normalized increments are only approximately

`7.31236`, `6.98721`, `6.99366`, `6.81837`,

summing to the exact strip width `(lambda-1)R = 28.11160...`.

The incorrect R20G.12 expression would multiply the first three increments by `3`.

This witness is not an RL object because `D does not divide Q`; its role here is only to show exactly why physical block height does not by itself force strip-width growth.

## 5. Proof-state effect

Unaffected RL20 claims:

- one-sided block imbalance `E_j>=0` in the near-resonant least rotation;
- physical height bands for `E_j=0` and `E_j>=1`;
- balanced cuts are near-minimum and odd in an actual integer cycle;
- the corrected lift is monotone and remains in the same narrow strip;
- the continued-fraction and block-length consequences.

Revised strategic claim:

- the strict-excursion branch remains open, but **the bare physical-height-vs-strip-width argument is not available** from the RL20 coboundary alone.

Verifier: `verify_rl21_geometry_repair.py`.
