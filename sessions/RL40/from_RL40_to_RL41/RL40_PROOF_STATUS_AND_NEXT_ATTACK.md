# RL40 proof status and next attack

Date: 2026-08-21

## Executive status

RL is **not proved**.  The active near-resonant order-2 / `g=2` balanced-return branch is also **not closed**.

RL40 nevertheless adds two rigorous pieces of progress on the exact frontier inherited from RL39:

1. **Crossing-aware low-transport reachability:** the inherited floor `rho>=16` is strengthened to

   > **`rho>=18`.**

   The proof uses the RL37 sign-reversal budget, RL38 integer crossing congruence, the forced `G=4` / common-prefix `11` geometry in the low-area range, exact propagation of the physical gap between excursions, the zero-odd terminal suffix, and the exact distortion product `prod J_E=z>1`.

2. **Exact RL39 single-state extremizer:** for fixed assigned valuation multiplicity `l`, the normalized correction contribution is exactly

   `C_l(q) = -R log(1-(z/R) 2^(-(l-1)/2) 3^(-q/l))`,

   where `q=lH-log_3(2)l(l-1)/2` is the RL39 charge.  This function is strictly decreasing and strictly convex in `q`.  Consequently, at fixed multiplicities and total charge, the correction product is maximized by concentrating all excess charge into one state.

The second point is strategically important: **RL39 alone cannot yield a product saving linear in raw total transport `rho`**.  A spread/cap theorem, direct RL38 distortion theorem, or low-transport sparse/reachability exclusion is required to defeat the concentration extremizer.

## Verification status

The uploaded RL39->RL40 handover hash verified successfully.

Fresh inherited verifier rerun:

- PASS `rl36_additions/verify_rl36_g2_excursion_charging.py`
- PASS `rl37_additions/verify_rl37_g2_sign_reversal_bridge.py`
- PASS `rl38_additions/verify_rl38_scaled_gap_telescoping.py`
- PASS `rl38_additions/verify_rl39_odd_or_valuation_charge.py`

New RL40 verifiers:

- PASS `rl40_additions/verify_rl40_crossing_aware_area16.py`
- PASS `rl40_additions/verify_rl40_low_transport_reachability.py`
- PASS `rl40_additions/verify_rl40_single_state_extremizer.py`

The low-transport verifier exactly enumerates 791,755 canonical positive excursions through area 17.

## New theorem A — `rho>=18`

### Area 16

Crossing-aware budget pruning leaves only

`(16)`, `(14,2)`, `(14,1,1)`.

The unrestricted area-16 envelope is below the `G>=8` sign-reversal budget, so `G=4`.  The exact common prefix is `11`, giving first-excursion physical gap `9`.

- The only single area-16 crossing compatible with gap 9 has `J=8192/19683<1`, impossible because with one excursion `J=z>1`.
- The unique budget-viable area-14 crossing requires incoming gap 13.  Exact small-area propagation from gap 9 reaches only 9, 7, 5, or 3 before the crossing.  Hence the two multi-excursion partitions are impossible.

Therefore `rho!=16`.

### Area 17

Crossing-aware partition pruning leaves nine partitions.  Exact physical-gap reachability plus the terminal `-4` endpoint reduces all of them to three distinct physical patterns.  Their total distortion products are respectively

`32768/59049`,

`16384/19683`,

`524288/531441`,

all strictly below 1.  Each contradicts `prod_E J_E=z>1`.

Therefore `rho!=17`, proving `rho>=18`.

## New theorem B — RL39 concentration barrier

For one owned odd state define

`q=lH-alpha*l(l-1)/2`, `alpha=log_3 2`.

Then

`3^H=3^(q/l)2^((l-1)/2)`

and exactly

`R log(1+1/(3y))`
`= -R log(1-(z/R)2^(-(l-1)/2)3^(-q/l))`.

For fixed `l` this is strictly decreasing and strictly convex in `q`.

Hence, with fixed multiplicities and lower charge floors, maximizing the aggregate correction subject to fixed total charge puts all excess charge on one state.  As total charge tends to infinity, the maximal product saving saturates at the loss of only one baseline correction factor.

Therefore no valid universal inequality with a negative linear term `-mu*rho`, `mu>0`, can follow from RL39.14 alone without an additional theorem preventing concentration.

## Area 18 exploratory frontier

A separate exact streaming enumeration found, for area 18,

`E(18)=28793/2160 = 13.3300925925...`,

and crossing-aware maximum

`C(18)=118061/10935 = 10.7966163694...`.

There are 1,036,426 canonical positive area-18 excursions and 568 crossing-capable ones.

Crossing-aware budget pruning at total area 18 leaves 23 integer partitions, including `(9,9)`.  This is the first low-area level in this continuation where the simple one-large-crossing-plus-area<=6 structure is no longer uniformly sufficient.  An uncompressed permutation/type reachability search was exploratory only and did not complete within the run budget.  This is **not** a verifier failure; no area-18 theorem is claimed.

## Strategic consequence

The original RL40 handover suggested optimizing RL38 and RL39 into a uniform coefficient bound.  The new extremizer result shows that a direct linear-in-`rho` version of that plan cannot work from RL39 alone: transport can concentrate in one sacrificial high state.

The strongest next routes are now:

1. **Compressed gap DP for low transport.**  Replace raw word/permutation enumeration by states carrying only `(transport spent, physical gap, crossed/not-crossed, remaining strong budget, distortion product interval)`.  Excursion types are summarized by `(r,D,h,p,strong)`.  This should attack `rho=18` and beyond much more efficiently.

2. **Charge-spread theorem.**  Prove that the actual excursion geometry prevents one state from absorbing arbitrarily large RL39 charge, e.g. by bounding per-state effective charge or forcing many charged owned states.  Only such a theorem can turn RL39 into a positive-density correction saving.

3. **Direct distortion/valuation coupling.**  Relate a concentrated high/long-valuation excursion to its `J_E` distortion.  If concentration forces `J_E` too far from 1, the exact product `prod J_E=z` may require enough compensating excursions to create the missing spread automatically.

4. **Sparse relation for sublinear transport.**  RL36 gives `(X+Y)G` as a signed sum of at most `rho` `2`--`3` monomials.  A uniqueness theorem that excludes this when `rho=o(L)` would pair naturally with an RL39 product theorem for the complementary linear-transport regime.

## Evidence discipline

- RL remains open.
- The full order-2 / `g=2` branch remains open.
- `rho>=18` is an exact branch-specific theorem, not a global RL result.
- The inherited external computational bound `R>=2^71` remains external.
- Older radius-3 leaves elsewhere in the project retain their explicit LMN external dependency where stated.
- The area-18 numbers above are exact exploratory enumeration results, but no area-18 exclusion theorem is frozen here.
