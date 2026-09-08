# RL283 — upstream 2-adic equivalence and relaxation barriers

Date: 2026-09-08

## Classification

Primary:

`UPSTREAM_2ADIC_EQUIVALENCE_AND_RELAXATION_BARRIERS_PROVED`

Promoted analytic subordinate results:

- `HIGH_DIVISIBILITY_RECONSTRUCTS_PREFIX_LEGALITY_PROVED`
- `ADJACENT_SWAP_VALUATION_LIPSCHITZ_BARRIER_PROVED`
- `ZERO_RANK_2ADIC_SCALAR_DEPENDENCY_PROVED`
- `TWO_SHADOW_AFFINE_REPRESENTATION_PROVED`
- `TERMINAL_EXTENSION_SINGLE_REVERSED_RANK_REFORMULATION_PROVED`
- `EXACT_ORDERED_RANK_ENDPOINT_REFORMULATION_EQUIVALENT_TO_GATE_A_PROVED`
- `NONCROSSING_RANK_RELAXATION_BARRIER_PROVED`

RL283 does **not** close Gate A.

The preferred upstream theorem remains open:

`d=1, J>0, J even, globally reachable at accumulated height H
 => nu_2(J)<=H`.

At a terminal `J=2^k` it would imply `k<=H`.

The exact authoritative residual inherited from RL282 therefore remains unchanged:

`k>=25`, `k` odd, `H_can<k`.

Gate B remains open/frozen. The fifth selector is not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming state and mission

RL283 inherited the corrected RL282 exact `H<=22` positive-checkpoint certificate:

- nonpositive states: `3,254,996`;
- first-positive entries: `169`;
- positive even checkpoints: `146,341`;
- odd boundary origins macro-closed: `13,583`;
- maximum exact stay-odd trace: `263`;
- power-of-two minima:
  `k5:H9`, `k7:H15`, `k9:H15`, `k11:H18`, `k13:H18`, `k15:H22`;
- no `2^17`, `2^19`, `2^21`, or `2^23` checkpoint under `H<=22`.

Hence every hypothetical Gate-A violator is already restricted to odd `k>=25` with `H_can<k`.

RL283 was tasked with attacking the missing **upstream global reachability** statement rather than extending the raw height cap.

## 2. Finite invariant discovery and immediate falsifications

The exact `H<=22` checkpoint state set was used for discovery only. The following valuation relations survived every positive even checkpoint in that certificate:

- `nu_2(J)<=H`;
- `nu_2(J+2)<=H-1`;
- `nu_2(J+4)<=H-1`;
- for `J!=2`, `nu_2(J-2)<=H-2`.

These observations are **finite evidence only** and are not promoted as global theorems.

The stronger incoming guide

`J<=2^H`

is false. RL283 therefore does not preserve it as a plausible sufficient theorem. This is not a demotion of inherited mathematics because RL282/RL283 authority explicitly labelled it conjectural.

RL282's local obstruction also remains decisive: individual positive excursions can raise `nu_2(J)` by more than their own height, for example the exact legal height-one return `30 -> 24`, so a blockwise monotonicity proof cannot work.

## 3. Boundary shifted-valuation family does not close finitely

The finite certificate suggested several shifted valuations, but exact height-one boundary dynamics make a finite fixed-offset table impossible.

For positive odd `J` at `d=1`, the odd-retaining boundary branch is

- `J==1 (mod 4)`: `J -> (J+1)/2`;
- `J==3 (mod 4)`: `J -> (3J+1)/2`.

Transporting affine shifts through these maps generates an unbounded family (`J+3`, `3J+5`, `9J+5`, ...). Therefore no proof based only on finitely many fixed shifted valuations can be closed under arbitrary zero-height boundary retention.

This is a route barrier, not a theorem about terminal impossibility.

## 4. High divisibility reconstructs legality

Use the RL47 ordered equal-weight rank representation. Let `x,y` be prescribed binary words of common length `m` and common weight, with prefix order ensuring the depth path remains `d>=1` and returns to `d=1`.

Ignore parity legality temporarily and apply the formal affine `J` transition determined by each pair column.

Every formal column has the form

`J_(i+1)=(c_i J_i+q_i)/2`

with `c_i` odd.

Define

`P_i=2^i J_i`.

Then

`P_(i+1)=c_i P_i+2^i q_i`.

Suppose the final cleared numerator is divisible by the full denominator:

`2^m | P_m`.

Backward reduction gives

`P_m == c_(m-1) P_(m-1) (mod 2^(m-1))`.

Since `c_(m-1)` is odd,

`2^(m-1) | P_(m-1)`.

Iterating yields

`2^i | P_i`

for every prefix `i`.

Therefore every formal prefix `J_i` is integral. For each prescribed pair column, integrality is exactly the parity compatibility condition needed by the canonical recurrence. Together with `d>=1`, the whole pair is a genuine legal canonical trajectory from `J=-13`.

### Consequence

Any positive ordered-rank counterexample to

`nu_2(Xi)<=m+H`

with `Xi=2^m J`

and `nu_2(Xi)>m+H` automatically satisfies `2^m|Xi`, hence reconstructs a genuine reachable positive checkpoint with

`nu_2(J)>H`.

Conversely, every genuine checkpoint violation gives such an ordered-rank violation.

Thus the dangerous high-divisibility region of the relaxed ordered-rank cancellation problem is **equivalent to the original RL283 reachability problem**. It is not a genuinely easier superset.

This corrects the earlier exploratory interpretation of bounded ordered-pair searches: they are regression evidence, not evidence from a broader dangerous algebraic class.

## 5. Single adjacent displacement can create arbitrarily large-looking cancellation

The sharp reachable equality witness has

- `m=10`, `r=5`;
- `a=(2,6,7,8,9)`;
- `b=(1,5,6,8,9)`;
- `H=3`;
- `Xi=8192=2^13`.

Its exact pair-column sequence is

`00,01,10,00,00,01,11,10,11,11`

with exact `J` trajectory

`-13 -> -6 -> -6 -> -3 -> -1 -> 0 -> 3 -> 6 -> 3 -> 5 -> 8`.

Undo only the first one-cell displacement:

`a^-=(1,6,7,8,9)`.

Then

`H^-=2`,
`Xi^-=7706=2*3853`,
`nu_2(Xi^-)=1`.

Restoring that single cell adds

`486=2*3^5`

and

`7706+486=8192`.

Hence one displacement cell raises the valuation from `1` to `13`.

Therefore no induction of the form

"each displacement cell adds at most one 2-adic bit"

can prove Gate A.

This is an exact route barrier.

## 6. Zero-rank integerization is not an independent scalar constraint

RL279 uses zero ranks

`u_t`, `v_t`, `h_t=v_t-u_t>=0`

with

`H=sum h_t`,
`rho=2/3`,
`c_t=2^(t-1)rho^(u_t)`.

The exact identity

`2S+D=12+X(1/2+2^(-k-1))`

can be integerized termwise. Multiplying by `3^r`, the t-th term is

`2^(t-1+u_t) 3^(r-v_t) [3^(h_t+1)-2^h_t]`.

For `h_t>=1`, the bracket is odd; for `h_t=0`, it equals `2`.

This initially appears to expose a new 2-adic grouped structure. However, after simplification at a `d=1` checkpoint it gives exactly

`Q(J+1)=2S+D-12`.

RL281 already has

`B+6=S+D/2`,
`B=Q(J+1)/2`.

Therefore the proposed zero-rank "new 2-adic scalar" is precisely the inherited `B` telescope in rearranged form.

It must not be counted as an independent global constraint.

The missing information is therefore not another aggregate scalar in `(S,D,Q)`, but genuinely non-separable reachability information.

## 7. Two-shadow affine representation

For a binary word `w` of length `n`, define the formal Collatz affine map

`C_w(z)=(3^r z+Q_w)/2^n`

where `r` is the weight and `Q_w` is the usual parity-word numerator.

For every canonical prefix with paired words `x,y`, current depth `d`, and normalized variable

`T=J-3^d+2^d`,

exact induction gives

`boxed: T = 3^d C_x(-7) - C_y(-7)`.

Equivalently,

`J = 3^d C_x(-7) - C_y(-7) + 3^d - 2^d`.

At a `d=1` equal-weight checkpoint,

`boxed: J = 3 C_x(-7) - C_y(-7) + 1`.

Let

`U_x=-7*3^r+Q_x`,
`U_y=-7*3^r+Q_y`.

Then at a common-length `m`, equal-weight `d=1` prefix,

`boxed: 2^m J = 3U_x-U_y+2^m`.

Each shadow numerator has the elementary recurrence

`U_(w0)=U_w`,
`U_(w1)=3U_w+2^n`.

The seed `-7` is structurally natural because the inherited boundary conjugacy has the exact negative neutral cycle

`-7 -> -10 -> -5 -> -7`

with word `101`.

This representation gives a compact finite-dimensional joint state, but RL283 did not obtain a monotone joint 2-adic invariant from it.

## 8. Terminal extension and the single reversed rank

At a terminal `d=1,J=2^k`, extend the paired words by the forced tails

`X = x 1 0^k`,
`Y = y 0^k 1`.

Let the extended words have length

`L=m+k+1`

and common weight `R=r+1`, with one-rank positions `a_j,b_j`.

For every original rank `j<R`, canonical prefix order gives

`b_j<=a_j`.

The final ranks are

`a_R=m`,
`b_R=m+k=L-1`.

Thus the final rank is the **only reversed rank** and

`sum_(j<R)(a_j-b_j)=H`,
`a_R-b_R=-k`.

The full signed displacement is `H-k`.

The fixed endpoint gives the exact identity

`boxed: 3Q_X-Q_Y = 14*3^R + 2^L`.

So Gate A is exactly the ordered-rank statement

`sum_(j<R)(a_j-b_j) >= k`

under this fixed-endpoint identity and the single-final-reversal structure.

However, by Section 4, full endpoint divisibility reconstructs prefix legality. Therefore this ordered-rank formulation is an **exact re-encoding of Gate A in its dangerous region**, not a simpler algebraic relaxation.

A compact regression search over every genuine terminal with extended length `L<=16` finds exactly `379` terminals and zero `H<k` violations. This is finite regression evidence only.

## 9. Strict noncrossing does not rescue the old separable relaxation

RL48 proved a barrier for the separable cap/room plus total-displacement rank relaxation when terminal zero parameter `z>=42`.

That relaxation discarded strict ordering of the displaced `b_j` ranks. RL283 tested whether restoring that coupling could save the method.

Retain RL48 notation

`C=(3/8) zeta^2`,
`U_j=floor(log_2(C 3^j))`.

For `z>=42`, RL48 proves the first 72 ranks are cap-limited:

`A_j=U_j`.

Also

`U_(j+1)-U_j in {1,2}`.

Among the first eight ranks there are at least four jumps of size `2`: since

`3^7>2^11`,

one has

`U_8-U_1>=11`;

seven increments in `{1,2}` totaling at least `11` require at least four `2`-jumps.

Choose four such ranks and assign one-cell displacement there:

`delta_j=1`

at those ranks and zero elsewhere. Put

`a_j=A_j`,
`b_j=a_j-delta_j`.

Whenever `delta` enters `1`, the selected `a`-gap is `2`, so the new `b`-gap remains at least `1`. All other transitions remain strictly ordered. Thus **both** rank sequences are strictly increasing and total displacement is only

`H_relax=4`.

For every one of the first 72 cap-limited ranks,

`w_j=2^U_j/3^j > C/2`.

The synchronized contribution is `2w_j>C`, so those ranks already contribute `>72C`.

Each of the four one-cell displacements increases its contribution by

`w_j/2 > C/4`.

Hence the noncrossing relaxed right side is

`>73C=(219/8)zeta^2`.

RL48's terminal target obeys for `k>=5`

`Lambda <= 14+(837/64)zeta`.

For `zeta>=1`,

`(219/8)zeta^2 -14 -(837/64)zeta`

is increasing, and at `zeta=1` equals

`19/64>0`.

Therefore

`boxed: noncrossing relaxed maximum > Lambda`

throughout the same `z>=42` regime.

So restoring strict noncrossing rank order is still insufficient. Any successful rank relaxation must preserve more of the exact synchronized `d=1` arithmetic than:

- coordinatewise prefix caps;
- terminal room;
- total displacement;
- strict ordering of both rank sequences.

This strengthens the RL48 proof-method barrier.

## 10. Boundary two-template hazard formulation — retained as promising formulation, not closure

At positive odd boundary state write

`n=(J-1)/2`.

The unique odd-retaining branch is the ordinary half-step Collatz map

`C(n)=n/2` if `n` is even,
`C(n)=(3n+1)/2` if `n` is odd.

The complementary even exit is

`E(n)=3n+2` for even `n`,
`E(n)=n+1` for odd `n`.

The exit valuation is a 2-adic longest-prefix match with one of two fixed templates:

- root `alpha_1=-1`, parity itinerary `1^infinity`;
- root `alpha_0=-2/3`, parity itinerary `01000...`.

This motivates the exact boundary hazard

`Beta(n)=sup_t nu_2(E(C^t(n)))`.

A sufficient upstream theorem would be

`globally reachable positive odd boundary origin (n,H)
 => Beta(n)<=H`.

RL283 did not prove this. It is retained only as a precise alternate formulation of the remaining upstream obstruction.

## 11. What RL283 ruled out

RL283 gives decisive reasons not to pursue the following as principal Gate-A routes:

1. the stronger size claim `J<=2^H`;
2. local/blockwise `nu_2` monotonicity;
3. finitely many fixed shifted valuations closed under arbitrary boundary retention;
4. per-displacement-cell valuation Lipschitz bounds;
5. treating the integerized zero-rank scalar as independent of the `B` telescope;
6. regarding the dangerous ordered-rank endpoint problem as an easier relaxation;
7. repairing RL47's separable rank relaxation merely by adding strict noncrossing order;
8. larger raw height-cap enumeration as a substitute for a scalable theorem.

RL282's final-tail 3-adic route barrier remains in force.

## 12. Proof state after RL283

### Promoted analytic

- high final 2-adic divisibility forces prefix integrality/parity legality;
- the adjacent-swap valuation-Lipschitz route is false, with an exact `1 -> 13` valuation-jump witness;
- the integerized zero-rank scalar is algebraically dependent on the inherited `B` telescope;
- the exact two-shadow affine representation about seed `-7`;
- terminal extension has exactly one reversed final one-rank, of displacement `-k`;
- the exact fixed-endpoint ordered-rank formulation is equivalent to the original dangerous Gate-A problem once high divisibility is imposed;
- strict noncrossing order does not repair the RL48 large-`z` separable rank-relaxation barrier.

### Regression evidence only

- the checkpoint inequality `nu_2(J)<=H` survives every inherited exact `H<=22` positive even checkpoint;
- several shifted variants also survive that finite state set;
- exhaustive genuine-terminal regression with extended length `L<=16` has `379` solutions and no `H<k` case.

### Open

The preferred Gate-A upstream theorem remains

`d=1, J>0, J even, globally reachable at height H
 => nu_2(J)<=H`.

No residual contraction beyond the inherited odd `k>=25`, `H_can<k` is promoted.

## 13. Strategic handover

RL283 ends with the Gate-A upstream programme mathematically intact but without a scalable proof.

By direct user instruction, RL284 is deliberately prepared as a **separate exploratory strategic pivot**: investigate whether non-trivial Collatz cycles admit a scale-independent structural/irreversibility contradiction (cocycle, winding, labelled event ordering, exact Lyapunov quantity, entropy-like increment, orientation/refinement obstruction), with a critical prime-factor overlay.

This pivot must **not** demote, overwrite, or silently replace the RL283 upstream theorem. If RL284 does not earn promotion through a theorem-sized advance, scalable structural reduction, or decisive barrier, the successor should recommend returning to the frozen Gate-A upstream-reachability programme.

Gate B, the fifth selector, Radius 6+, and unrelated work remain frozen.
