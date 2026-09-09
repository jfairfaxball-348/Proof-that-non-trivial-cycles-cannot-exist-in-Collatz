# RL288 — fixed-seed 2-adic lift selection / global Gate-A sign target

Date prepared: 2026-09-09
Status: PREPARED, NOT STARTED

## Incoming classification

RL287 closed as

`STATE_RESERVE_PHASE_TRANSPORT_AND_GLOBAL_REACHABILITY_BARRIERS_PROVED`.

Gate A remains open with exact residual

`k>=25`, `k` odd, `H_can<k`.

## Frozen RL287 conclusions

RL287 established that:

1. the natural scalar reserve candidates are exhausted:
   - the boundary one-zero quotient is exact but resets between components;
   - the unique affine reserve `Q(2J+3)/5` is a dependent ledger;
   - the boundary-invariant normalized Ferrers reserve is exactly the inherited coupon defect `D`;
   - a hybrid sign-definite reserve exists but absolute reserve/F/mass costs can vanish while local 2-adic hazard diverges;

2. every fixed legal canonical segment of length `L` is a 2-adic cylinder isometry:
   once its `L` legality bits are fixed, arbitrary higher input-lift bits pass to the output by an odd affine map;

3. a height-`H` canonical path has at most `H` first-return excursions and at most `2H` non-boundary columns, but low-height local terminal predecessors exist for every odd terminal exponent;

4. residual violators require a linear surplus of zero-height boundary `x=1` columns, but arbitrary such surplus can occur in cycle-free positive boundary transients with full future hazard `Beta=3`.

Therefore no further local reserve, local component-height, scalar-cost, boundary-density, neutral-cycle, or fixed finite shifted-valuation argument is the preferred route.

## Mission

Attack the remaining **fixed-seed global 2-adic lift-selection theorem** directly.

Preferred sufficient theorem:

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

Preferred all-depth form:

`J>0, K=J+2^d-1, A=H+d-1
 => nu_2(K-1)<=A`.

Equivalent fixed-seed shifted-shadow/sign form from RL285:

for a canonical paired prefix `(x,y)` of length `n`, depth `d`, and post-column area `A`, with

`Z=3^d W_x-W_y-2^n = 2^n(K-1)`,

prove

`2^(n+A+1) | Z => Z<=0`.

Any theorem implying that a positive high-divisibility lift cannot be selected from the fixed seed is acceptable.

## Required starting point

1. **Fixed seed, not variable local input.**
   The local cylinder-isometry theorem proves that a fixed suffix cannot restrict its own higher lift. The proof must use how the complete canonical prefix from the initial seed selects that lift.

2. **Use RL285's global representation.**
   Work with:
   - `W_empty=-6`;
   - `W_(w0)=W_w+2^|w|`;
   - `W_(w1)=3W_w`;
   - `Z=3^d W_x-W_y-2^n`;
   - `A=sum(d_i-1)` / prefix-dominance area;
   - high divisibility reconstructs canonical prefix legality.

3. **Adversarially test against RL287 local families.**
   Any proposed invariant must survive:
   - height-2/4 direct-terminal predecessor shells for arbitrary odd `k`;
   - arbitrary fixed-segment 2-adic lift isometry;
   - `(110)^N` zero-height boundary surplus with `Beta=3`;
   - vanishing scalar costs at arbitrarily deep local phase.

4. **Exact finite certificate is only a falsification oracle.**
   The inherited `H<=22` raw-state/checkpoint certificates may be used to reject candidates, not as the principal proof route and not to enlarge the residual by raw enumeration.

## Promising forms to test

- a fixed-seed restriction on the quotient after the mandatory `2^n` integrality has been removed, i.e. on `K-1`;
- a nonlocal congruence/cocycle carried by the common seed `-7` that is not algebraically equivalent to the `B`, `S`, `D`, or endpoint-potential telescopes;
- a minimal positive bad-prefix argument that genuinely uses the full ancestor chain, rather than only the four local parent congruences;
- a theorem that couples prefix-dominance area to which higher 2-adic lift of a legality cylinder is selected by the fixed seed.

## Forbidden repeats

Do not make the principal route:

- another scalar reserve in `(S,D,Q,F,B)`;
- another local first-return carry bound;
- local hazard versus component height;
- fixed finite shifted-valuation tables;
- boundary-one density, boundary run count, or neutral-cycle deletion alone;
- larger raw height-cap enumeration;
- an algebraic relaxation whose dangerous high-divisibility region merely reconstructs the original canonical problem without a new invariant;
- Gate B;
- the fifth selector;
- Radius 6+.

## Scope

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen.

No global non-trivial-cycle exclusion is claimed.

The successor should stop at the next theorem-sized fixed-seed advance, decisive barrier, or material contraction.
