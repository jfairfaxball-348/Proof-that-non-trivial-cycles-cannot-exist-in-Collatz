# RL27 proof status and next attack

Date: 2026-08-21

## Executive state

**RL is open.** This handover preserves the fully verified RL26 base and adds a repaired cubic full-spread theorem, exact adjacent-block prefix/valuation ownership, and exploratory evidence identifying which local/nonlocal ideas do and do not currently scale.

The release state is divided into: analytic results, exact finite certificates, external inputs, exploratory/method evidence, and open targets.

---

## A. Inherited analytic frontier (RL26)

The inherited proof state is documented in `inherited_rl26/RL26_PROOF_STATUS_AND_NEXT_ATTACK.md`. The most important retained facts are:

1. Global packing supporting line:
   `lim R*C_H(R) = 457841/1843200 ~= 0.248394639756944`.
2. Near-resonant order-3 numerator upper:
   `Delta < Y[(4/5)e - 3 + 3(2/3)^e]`.
3. Five-bit least-state sieve:
   near-minimum roots lie in `{7,15,27,31} mod32`, and the weak cubic geometry survives only at `R==27 mod32`.
4. Under the inherited weak-close package the unique exceptional root class is
   `R==91 mod288`, with coordinate-minimal gaps
   `G=12, H=4`.
5. Exact radius 3 remains closed under its inherited audited hypotheses/dependencies. Do not reopen it unless a bundled verifier or dependency audit fails.

---

## B. New RL27 analytic repair: full pairwise cubic spread

Retain

`B=2^b`, `Y=3^e`,

and balanced block numerators

`U=(B-Y)R+BG`,
`V=(B-Y)R+BH-YG`,
`W=(B-Y)R-YH`.

After factoring a common `2^r` from `G=2^r N`, `H=2^r K`, the third pairwise difference omitted by the old lattice verifier is

`(U-V)/2^r = B(N-K)+YN`.

Using the inherited mod-3 ownership, the true orientation-independent spread satisfies

`Delta >= 2^r(2B+3Y)`.

At the universal shared-`11` level `r=2`,

> `Delta >= 4(2B+3Y)`.

At the exceptional `(N,K)=(3,1)`, equivalently `(G,H)=(12,4)`,

`U-W = 4(3B+Y)`,
`V-W = 4(B-2Y)`,
`U-V = 4(2B+3Y)`,

and because `Y < B < 2Y`,

> `Delta = 4(2B+3Y)`.

This repairs RL25/RL26 sharpness wording. It does **not** invalidate their weaker lower bounds.

Combining with the inherited global numerator upper gives the modest analytic consequence

> `e >= 29`.

---

## C. New RL27 analytic adjacent-block ownership

In the exact weak-close geometry

`R==91 mod288`, `G=12`, `H=4`,

the three balanced macroblock prefixes are forced:

- `U` block from `R` to `R+12`: `11011...`;
- `V` block from `R+12` to `R+4`: `11101...`;
- `W` block from `R+4` to `R`: `11111...`.

For the middle `V` block, fixed weight plus prefix `11101` gives

`V >= (35/27)Y - 2^(e+1)`.

Together with the exact block equation and inherited near-resonant bounds this forces

> `e >= 37`.

The incoming odd-map valuations at the three balanced cuts satisfy

- into `x=R+12`: `nu_x == 0 or 2 (mod 6)`, hence `nu_x>=2`;
- into `y=R+4`: `nu_y == 3 or 5 (mod 6)`, hence `nu_y>=3`;
- into `R` under the inherited exceptional final return: `nu_R=2` exactly.

The last identity gives the exact predecessor

`z_close=(4R-1)/3`.

The cheapest predecessors into the other cuts align with fixed offsets from the same threshold:

- if `nu_x=2`, predecessor of `R+12` is `z_close+16`;
- if `nu_y=3`, predecessor of `R+4` is `2*z_close+11`.

This is a concrete interface between the cubic extremizer and the RL23/RL24 high-threshold packing geometry.

---

## D. New RL27 three-trajectory braid

Define

`u_j=T^j(R)`,
`v_j=T^j(R+12)`,
`w_j=T^j(R+4)`.

The forced prefixes yield after five steps

`w_5 > v_5 > u_5`,

whereas at the common macroblock endpoint

`u_b=R+12 > v_b=R+4 > w_b=R`.

Thus the ordering is completely reversed across the three adjacent balanced blocks. Same-parity steps cannot change the sign of a pairwise difference, so at least two later opposite-parity crossings are forced.

This is nonlocal, but currently only `O(1)`. The missing theorem must make the reconvergence cost scale with `e`, valuation excess, transport area, or another global quantity.

---

## E. Exact sparse adjacent-block identity

At `G=12,H=4`,

> `U-V = 8B+12Y = 4(2B+3Y)`.

This is the most promising algebraic bridge back toward the already-developed sparse/resultant machinery. A successful RL28 argument should test whether the sparse identity, endpoint valuation ownership, and synchronized trajectory crossings together force a proper-factor/resultant obstruction or a positive-density valuation penalty.

---

## F. Synchronized sign-reversal formulation — primary RL28 target

At times `j` where the three trajectories have accumulated the same number `p` of odd steps, their affine numerator differences simplify. In particular,

`2^j(v_j-u_j) = 3^p*12 + (Q_v(j)-Q_u(j))`,

`2^j(w_j-u_j) = 3^p*4  + (Q_w(j)-Q_u(j))`.

Initially synchronized gaps have positive coordinates relative to `u`; at the macroblock endpoint the synchronized target is

`(v_b-u_b, w_b-u_b)=(-8,-12)`.

Therefore a genuine survivor must contain a first equal-odd-count synchronization where a coordinate changes sign. Such a sign reversal is exactly a **nonlocal numerator-difference event**.

### Primary theorem sought

Prove a first-synchronized-sign-reversal lemma using both:

1. forward constraints from `11011/11101/11111`, leastness, and the sparse numerator identities;
2. backward constraints from `nu_x mod6 in {0,2}`, `nu_y mod6 in {3,5}`, `nu_R=2`, and the endpoint gaps `12,8,4`.

Desired outcomes, in descending order of strength:

1. the forward and backward cones cannot meet — eliminating `G=12,H=4`;
2. every meeting has a proper-factor/resultant obstruction covered by existing sparse machinery;
3. every meeting pays a valuation/high-state cost repeated `Omega(e)` times;
4. derive an `o(eY)` or otherwise substantially improved numerator upper bound in the unique weak sector.

---

## G. Certified finite results

These are exact within their stated ranges and are not global substitutions:

- inherited RL24 CF denominator floor conditional on the external `R>=2^71` input;
- inherited RL25 near-resonant terminal-pair scan;
- inherited RL26 five-bit small-pair localization;
- RL27 exact threshold checks supporting `e>=29` and `e>=37`.

See verifier outputs.

---

## H. External dependency retained

The lower bound

`R>=2^71`

remains **EXTERNAL COMPUTATIONAL INPUT**. RL27 does not prove it. Any theorem using it remains conditional on that external input.

The older radius-3 closure retains its previously audited dependency chain; see the inherited ledgers.

---

## I. Do not overclaim

The following are **not proved**:

- RL itself;
- exclusion of the `R==91 mod288`, `G=12,H=4` sector;
- positive-density valuation gain from the endpoint congruence classes;
- impossibility of arbitrarily deep simultaneous least-state lifts;
- a global contradiction from the raw 3-adic tail congruence;
- a theorem that synchronized gap coordinates stay positive before the endpoint.

---

## J. Low-priority / avoid

1. Do not reopen radius 3 absent verifier/dependency failure.
2. Do not spend the session merely extending the mod-32/root sieve to larger fixed modulus.
3. Do not treat deeper finite least-state lifting as a likely closure; the exploratory tree grows substantially.
4. Do not treat the raw 3-adic tail congruence as sufficient for a density contradiction; low-average admissible tails exist in the exploratory DP.
5. Do not confuse finite prefix evidence with an invariant.
6. Keep `g=2` or independent local packing improvements secondary unless they directly couple to the exceptional three-block geometry.

---

## K. Release verification

The handover release ran 20 verifiers: all 19 inherited RL21--RL26 verifiers plus `verify_rl27_full_spread_adjacent_ownership.py`.

`TOTAL_VERIFIERS=20`

`STATUS=PASS`

See `RL27_RELEASE_VERIFIER_RUN.txt`.
