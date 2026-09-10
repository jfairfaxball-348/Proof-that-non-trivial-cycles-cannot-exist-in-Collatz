# RL293 — fixed-seed min-plus ownership, danger-tree geometry, and k=29 contraction

Date: 2026-09-10

Primary classification:

`FIXED_SEED_MINPLUS_OWNER_DANGER_TREE_REDUCTION_AND_K29_CONTRACTION_PROVED`

Gate A remains open, but the exact terminal residual contracts from

`k>=29`, `k` odd, `H_can<k`

to

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming state and outcome

RL293 inherited RL292's exact five-state Bellman front door, checkpoint-8 transformed-shadow resonance normal form, low-cost checkpoint-8 kernel, static boundary-hazard preimage tree, and exact residual `k>=29` odd.

The incoming mission was to couple paid fixed-seed/ballot ancestry to the infinite static boundary danger tree without returning to finite shifted templates or endpoint-only local potentials.

RL293 does not prove the full global Gate-A theorem and does not prove `Bcal(2,3)<=1`. It does prove several structural reductions that make the remaining infinite problem substantially smaller, and it closes the next residual exponent `k=29` by an exact compact splice plus a one-source positive certificate.

New promoted items are classified explicitly below as proved analytic mathematics, exact finite certificates, or method barriers.

## 2. Exact pullback of the static danger tree through any fixed legal segment

RL292 represents the positive odd boundary hazard in the coordinate

`n=(J-1)/2`

by the static centres

`rho_(w,alpha)=(2^t alpha-Q_w)/3^r`,

where `w` has length `t`, weight `r`, and `alpha` is one of the two roots `-1,-2/3`.

RL287 gives the cylinder-isometry theorem for any fixed legal canonical segment `S` of length `L`:

`2^L J_out=c J_in+b`

with `c` odd. If `J_*` is one realizing input, then every lift `J_*+2^L t` follows the same itinerary and

`J_out(J_*+2^L t)=J_out,*+c t`.

If the endpoint is required odd, write `t=2u`. Then

`n=n_*+c u`.

For each static hazard centre define the pulled-back centre

`sigma_(w,alpha)=(rho_(w,alpha)-n_*)/c`.

Because `c` is odd,

`nu_2(n-rho_(w,alpha))=nu_2(u-sigma_(w,alpha))`.

Therefore exactly

`Beta(n_*+c u)=sup_(w,alpha)[nu_2(u-sigma_(w,alpha))-|w|]`.

Every danger ball pulls back through a fixed legal segment with exactly the same 2-adic precision. No bounded correction or loss of radius appears.

If the segment is itself a retained boundary word, composition simply prefixes/reindexes the same RL292 static tree. Arbitrarily long zero-height boundary retention therefore grafts the same tree rather than generating a new finite phase table.

Classification — proved analytic mathematics:

`FIXED_SEGMENT_STATIC_DANGER_TREE_ODD_AFFINE_PULLBACK_ISOMETRY_PROVED`.

## 3. Merger-invariant min-area static-ball formulation

For a positive odd boundary origin `n`, define

`mu(n)=minimum historical H`

over all genuine fixed-seed histories reaching `(d,J)=(1,2n+1)`, with `mu=+infinity` when unreachable.

For a static node `(w,alpha)` of depth `t` and threshold `R`, put

`B(w,alpha,R)={n:nu_2(n-rho_(w,alpha))>=R+t}`.

RL292 gives

`{Beta>=R}=union_(w,alpha) B(w,alpha,R)`.

Hence the boundary-hazard portion of Gate A is exactly equivalent to the family of min-plus inequalities

`inf_{n reachable in B(w,alpha,R)} mu(n)>=R`

for every `(w,alpha,R)`.

This formulation performs all branch mergers before comparing danger with cost. It therefore avoids the chosen-history seam problem from RL289/RL290. Under Section 2 each `B` remains a same-precision ball in the unresolved fixed-seed lift coordinate.

Scope qualification: this equivalence is the zero-height boundary-hazard subproblem. It is not by itself the full five-state Bellman theorem because direct positive excursions and the fixed-seed front door remain part of the global Bellman graph.

Classification — proved analytic mathematics:

`MERGER_INVARIANT_MIN_AREA_STATIC_DANGER_BALL_SEPARATION_EQUIVALENCE_PROVED`.

## 4. Support-count and excursion-count charging are false even on a genuine fixed-seed history

The genuine canonical pair

`x=10000011`,
`y=10010010`

replays from `(d,J,H)=(1,-13,0)` through

`(1,-19,0),(1,-9,0),(1,-4,0),(2,-3,0),(2,1,1),(2,3,2),(2,6,3),(1,3,4)`.

The matched one positions are

`a=(1,7,8)`, `b=(1,4,7)`,

so the rank displacements are `(0,3,1)`. The full Ferrers area is `H=4`, but only two ranks are displaced and there is only one off-boundary excursion.

At the endpoint `J=3`, `n=1`. The retained boundary orbit is `1->2->1`; its complementary hazards have valuations `1` and `3`, so `Beta(1)=3`.

Thus both proposed simplifications are false:

- `Beta <= number of displaced ranks` fails because `3>2`;
- `Beta <= number of excursions` fails because `3>1`.

The multiplicity-weighted Ferrers/ballot area, or an equivalent min-plus cost, cannot be replaced by support size or skeleton component count.

Classification — method barrier:

`DANGER_TREE_SUPPORT_COUNT_AND_EXCURSION_COUNT_CHARGE_BARRIER_PROVED`.

Portable regression: `verification/verify_rl293_pullback_barrier.py`.

## 5. Checkpoint-8 area-two equality mechanism is rigid

RL292 proved that the only first returns from checkpoint `8` below height eight are

- `x=001`, cost `2`, return `J=5`;
- `x=011`, cost `2`, return `J=12`.

The corresponding paired words are `001/100` and `011/110`.

From odd boundary `J=5`, the retained zero-height orbit is `5->3->5`, with complementary even exits `8` from `5` and `2` from `3`. Therefore every balanced suffix from checkpoint `8` having total added area exactly two is, for some `q>=0`, one of

- return to `8`:
  `x=001(01)^q1`, `y=100(01)^q1`;
- exit to `2`:
  `x=001(01)^q00`, `y=100(01)^q00`;
- direct exit to `12`:
  `x=011`, `y=110`.

No other positive-cost excursion can occur without raising the area above two. Hence the entire arbitrary-length area-two class is exact.

For the checkpoint-8 candidate inequality

`nu_2(J_end)<=A+1`,

the only sharp area-two endpoint is the return `J=8`, because

`nu_2(8)=3=2+1`.

Classification — proved analytic mathematics:

`CHECKPOINT8_AREA_TWO_RENEWAL_EQUALITY_RIGIDITY_PROVED`.

## 6. Complete checkpoint-8 low-area closure through A<=7

Exact shortest-path closure in the positive physical graph, with zero-height boundary loops quotiented by physical-state dominance, gives the complete nontrivial checkpoint frontier below added area eight:

- cost `2`: `{2,12}`;
- cost `6`: `{6,14,18,20,26,30,32,62,68,80,134}`;
- cost `7`: `{24,48,102}`.

Checkpoint `8` itself has minimum cost zero, but its minimum nonempty return has cost two by Section 5.

There are no other nonempty balanced checkpoint futures of total area at most seven. Every endpoint in this complete closure satisfies

`nu_2(J)<=A+1`.

The largest nontrivial valuation is `nu_2(32)=5` at cost six; the sole equality is the nonempty cost-two return to `8`.

Classification — exact finite certificate:

`CHECKPOINT8_FULL_LOWAREA_A_LE_7_EXCESS_ONE_CLOSURE_PROVED`.

Portable verifier: `verification/verify_rl293_checkpoint8_lowarea.py`.

## 7. Checkpoint 2 is min-plus dominated by checkpoint 8 through cost 29

Let `m_J(T)` be the minimum added canonical height from positive even checkpoint `J` to positive even checkpoint `T` in the exact RL290 physical graph.

Checkpoint `2` has a forced zero-cost launch to the special tower

`R_d=(d,K=3^d)`.

At `R_d`:

- `x=0` sends `R_d` to `R_(d+1)` at cost `d-1`;
- `x=1` sends it to `S_d=(d-1,K=(3^d-1)/2)` at cost `d-1`.

If the first `1` after launch occurs at depth `d`, the source-2 cost to `S_d` is

`d(d-1)/2`.

For `d=3,4,5`, checkpoint `8` reaches the identical physical states `S_d` by the legal words

- `00`, cost `1`;
- `0100`, cost `4`;
- `010100`, cost `9`.

These save respectively `2,2,1` units over the source-2 tower path, so every continuation from those merger states is strictly cheaper from `8`.

At `d>=6`, merely descending from `S_d` to depth one gives the lower bound `(d-1)^2` on the complete first-return cost. Thus `d>=7` cannot return by cost 29.

For `d=6`, the generic bound 25 is sharpened because `S_6` has even `K=364`, so a same-depth cost-four column is compulsory before any descent. The first possible return therefore has cost at least 29. Equality is rigid and returns to odd boundary `J=17`; its retained boundary trace has complementary even exits exactly `{2,8,14,26}`, all already reachable from checkpoint `8` with cost at most six.

The `d=2` departure returns through boundary `3`, whose checkpoint exits are `{2,8}`; for a non-self minimum path it enters `8`.

Hence for every positive even `T!=2` with `m_2(T)<=29`,

`m_2(T)=m_8(T)+1`.

Classification — proved analytic mathematics:

`CHECKPOINT2_TO_CHECKPOINT8_STRICT_MINPLUS_DOMINATION_THROUGH_COST29_PROVED`.

Portable regression: `verification/verify_rl293_checkpoint2_domination.py`.
