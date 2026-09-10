# RL292 — fixed-seed Bellman front door, danger-tree geometry, and residual contractions

Date: 2026-09-10

Primary classification:

`FIXED_SEED_BELLMAN_FRONT_DOOR_STATIC_BOUNDARY_DANGER_TREE_AND_K25_K27_CONTRACTIONS_PROVED`

Gate A remains open. RL292 contracts the exact terminal residual to

`k>=29`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Scope and outcome

RL292 inherited RL291's recommendation to combine fixed-seed ballot ancestry with RL290's physical Bellman threat rather than restart a local-charge programme.

It does not prove `Bcal(1,-13)<=0`. It does, however, produce:

1. exact Rank-1 danger-ball and phase-reset barriers showing why local endpoint potentials fail;
2. an exact first-positive Bellman reduction and then an exact five-state fixed-seed Bellman front door;
3. an exact `H<=24` minimum-height certificate closing residual exponent `k=25`;
4. a stronger first-positive analytic over-approximation through `H<=26` closing `k=27`;
5. a transformed-shadow resonance normal form for first Bellman failure;
6. an exact low-cost kernel gap at checkpoint `8`;
7. an exact static 2-adic preimage-tree representation of the positive-boundary hazard `Beta`;
8. a theorem that no finite maximum of affine 2-adic valuation templates can dominate that hazard, even after the promoted local mod-3 filter.

The surviving scalable target is therefore not another finite affine potential. It is a tree-separation theorem coupling paid fixed-seed/ballot ancestry to the static boundary danger tree.

## 2. Rank-1 homogeneous danger balls and 2-adic singularity

Define the exact cost-one stripped-unit map

`T(J)=(3J+10)/8`

on the `t=3` branch, and for `R>=1`

`N_R(J)=3^R(J-2)+2*8^R`,
`lambda_R=2-2(8/3)^R`.

Then `T^R(J)=N_R(J)/8^R` and `N_R(J)=3^R(J-lambda_R)`.

If `J>=2` is even and

`n=nu_2(N_R(J)) >= 3R+1`,

then `(010)^R` is automatically a genuine sequence of positive-even cost-one checkpoint macros; all intermediate nonterminal checkpoints have valuation one and the endpoint has valuation `n-3R`. Hence

`V(J) >= n-4R = nu_2(J-lambda_R)-4R`.

For odd `k` with `v_3(2^k-2)>=R+1`, the exact tower

`M_j(k)=2+(8/3)^j(2^k-2)`

is positive, locally legal, lies in the inherited checkpoint mod-3 class, passes the RL282 one-zero output shell at every level, and satisfies

`M_j --010--> M_(j-1)`, `M_0=2^k`, `V(M_R)>=k-R`.

For fixed `R`, these states converge 2-adically to `lambda_R` while their future threat is unbounded. Thus the full physical Rank-1 threat is not locally bounded near these centres. Endpoint-only continuous potentials, finite-residue tables and finite shifted-valuation tables cannot dominate the full local Bellman graph.

Global fixed-seed reachability of the general tower is not claimed. The `R=1,k=13` member `21842 -> 8192` is genuinely present in RL290's fixed-seed chain.

Classification:

`RANK1_HOMOGENEOUS_DANGER_BALL_AND_2ADIC_SINGULARITY_PROVED`.

## 3. Exact shifted fixed-point phase-reset barrier

For every odd `N>=3` with `N==3 or 5 (mod 6)`, put

`J_N=(2^(N+4)-2)/3`,
`M_N=3*2^N+2`.

Then `J_N` is positive even, in the inherited checkpoint residue class, and `nu_2(J_N-2)=3`. The exact cost-one macro `0101` sends `J_N` to `M_N`, the intervening one-zero return satisfies the promoted `nu_3=1` shell, but

`nu_2(M_N-2)=N`.

Thus a single height-one physical macro can reset the fixed-point shifted phase to arbitrary depth. In particular no edge-Lipschitz proof based on `nu_2(J-2)` plus bounded local correction can close Gate A.

The `N=11` member is genuinely fixed-seed reachable: a canonical prefix reaches `(1,10922,17)` and appending `0101` reaches `(1,6146,18)`, raising `nu_2(J-2)` from `3` to `11`.

The related label `t(J)=nu_2(3J+2)` is a genuine pulled-back future-template overlap depth, but finite evidence `t(J)<=mu(J)` does not control recursive Bellman threat: the homogeneous danger towers keep `t=3` at nonterminal levels while future threat diverges. It is not promoted as a global bound.

Classification:

`SHIFTED_FIXED_POINT_ARBITRARY_PHASE_RESET_BARRIER_PROVED`.

## 4. First-positive Bellman domination is equivalent to the global target

Let `s_*` be the first state with `J>0` on a genuine fixed-seed path. Positivity is forward invariant. For any later positive-even checkpoint `q`, write the historical cost as

`H(q)=H(s_*)+DeltaH(s_*->q)`.

Then

`nu_2(J(q))-H(q) = [nu_2(J(q))-DeltaH]-H(s_*)`.

Taking the supremum over finite checkpoint-ending positive futures gives

`Bcal(s_*)-H(s_*)`.

Therefore the global fixed-seed Bellman domination target is equivalent to

`every globally reachable first-positive state s_* satisfies Bcal(s_*)<=H(s_*)`.

This reduction is exact and does not assume `Bcal` is finite.

At a balanced checkpoint with paired prefix length `n`, common weight `r`, and parity numerators `Q_x,Q_y`, the two pulled-back stripped-unit future-template centres satisfy

`p_x-p_y = -2^n(3J+2)/3^(r+2)`

and hence

`nu_2(p_x-p_y)=n+nu_2(3J+2)`.

So the stripped-unit label is exactly extra common 2-adic cylinder overlap beyond the already fixed prefix.

Classification:

`FIRST_POSITIVE_BELLMAN_DOMINATION_REDUCTION_AND_TEMPLATE_OVERLAP_IDENTITY_PROVED`.

## 5. Exact five-state fixed-seed Bellman front door

The complete zero-height fixed-seed boundary component has six `d=1` physical states and, modulo neutral `(101)` repetitions, exactly three off-boundary departures:

`R6=(2,-6)`, `R39=(2,-39)`, `R3=(2,-3)`.

At witness level,

`Bcal(1,-13)=max(Bcal(R6),Bcal(R39),Bcal(R3))`.

The `R3` branch has a cost-one physical self-loop and then a cost-one exit to `(2,1)`; both legal bits from `(2,1)` merge at equal cost into `(2,3)`. Thus

`Bcal(2,-3)=Bcal(2,3)-2`.

For `R6`, exact boundary quotienting through `(1,-3)` and domination of the `R3` exit gives

`Bcal(2,-6)=max(Bcal(3,2)-1,Bcal(2,3)-1)`,

while

`Bcal(3,2)=max(Bcal(4,39)-2,Bcal(2,3)-3)`.

For `R39`, the exact word `101` returns to the seed at cost three. Deleting completed renewals strictly improves any subsequent counterexample witness. First deviation from that renewal goes to `(2,-17)` at cost 1, `(2,-84)` at cost 2, or `(3,-28)` at cost 3.

Consequently

`Bcal(1,-13)<=0`

is equivalent to the five fixed-state inequalities

1. `Bcal(2,3)<=1`;
2. `Bcal(4,39)<=3`;
3. `Bcal(2,-17)<=1`;
4. `Bcal(2,-84)<=2`;
5. `Bcal(3,-28)<=3`.

This is an exact infinite-horizon physical-state cutset theorem, not a bounded certificate. The H<=22 falsification oracle found only `(2,3)` tight among these five states.

Classification:

`FIXED_SEED_NEUTRAL_GAUGE_AND_RENEWAL_FIVE_STATE_BELLMAN_FRONT_DOOR_PROVED`.

## 6. Exact minimum-height H<=24 certificate closes k=25

RL292 uses shortest-path dominance on physical states: transitions depend only on `(d,J)` and every height increment is nonnegative, so if the same physical state is reached at heights `H1<=H2`, retaining the `H2` copy can never improve any future minimum-height target.

The portable exact verifier reproduces the repaired RL282 power minima through `H<=22`:

`k1:H3,k3:H3,k5:H9,k7:H15,k9:H15,k11:H18,k13:H18,k15:H22`.

Extending exactly to `H<=24` gives

`k1:H3,k3:H3,k5:H9,k7:H15,k9:H15,k11:H18,k13:H18,k15:H22,k21:H24`

and no `2^17,2^19,2^23,2^25` checkpoint under the cap.

A `k=25` Gate-A violator would require integer height `H<=24`, contradiction. Thus `k=25` is closed.

Frozen counts:

