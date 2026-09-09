# RL290 — gauge-invariant seam barriers, Bellman threat, and exact height-one checkpoint kernel

Date: 2026-09-09

## Closed classification

Primary:

`GAUGE_INVARIANT_BELLMAN_CHECKPOINT_KERNEL_AND_HEIGHT_ONE_LAUNCHPAD_BARRIERS_PROVED`

Promoted analytic subordinate results:

- `POST_DEPARTURE_ODD_ODD_SEAM_NORMAL_FORM_PROVED`
- `NEUTRAL_SEED_PREFIX_GAUGE_INVARIANCE_OF_NORMALIZED_SEAM_PROVED`
- `POSITIVE_BOUNDARY_LOOP_SEAM_GAUGE_BARRIER_PROVED`
- `ZERO_AREA_LOOP_ERASURE_ENDPOINT_HEIGHT_PRESERVATION_PROVED`
- `FIXED_SEED_BRANCH_MERGER_AND_ACYCLIC_EQUAL_AREA_SEAM_GAUGE_BARRIERS_PROVED`
- `MINIMAL_FUTURE_REJECTED_TUBE_BELLMAN_ENVELOPE_CHARACTERIZED`
- `PURE_ZERO_FINAL_TAIL_MINIMAL_HEIGHT_ONE_LOCAL_REALIZABILITY_PROVED`
- `HEIGHT_ONE_LAUNCHPAD_AFFINE_RAY_PROVED`
- `POSITIVE_CHECKPOINT_ZERO_HEIGHT_GAUGE_QUOTIENT_BELLMAN_OPERATOR_PROVED`
- `HEIGHT_ONE_CHECKPOINT_SUCCESSOR_KERNEL_EXACTLY_CLASSIFIED`
- `STRIPPED_UNIT_SYNCHRONIZED_LABELLED_ACCELERATED_RENORMALIZATION_PROVED`
- `ONE_GENERATION_BOUNDARY_HAZARD_STRICTLY_INSUFFICIENT_FOR_FULL_BELLMAN_THREAT_PROVED`

Gate A remains open. The exact authoritative residual remains

`k>=25`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. The fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and outcome

RL290 inherited RL289's fixed-seed affine ballot bijection

`zeta_y == 3 zeta_x + 14 (mod 2^n)`

and the geometric equivalence

`nu_2(J) = depth of the complete adjacent rejected d=0 tube`

at a positive even balanced checkpoint.

The incoming mission was to find a gauge-invariant seam/history theorem pricing rejected-tube depth by accumulated legal ballot area.

RL290 does not close Gate A. It does, however, substantially sharpen the state of the problem:

1. it derives an exact normalized odd/odd seam normal form;
2. it proves that neutral seed prefixes, genuine positive boundary cycles, branch mergers, and acyclic equal-area diamonds all create history gauges that defeat chosen-history seam charges;
3. it identifies the canonical gauge-free object as a Bellman future-threat envelope on physical states;
4. it quotients all zero-height positive-boundary dynamics into an exact positive-even checkpoint Bellman graph with strictly positive edge costs;
5. it completely classifies the height-one part of that checkpoint kernel;
6. it proves that every odd terminal exponent has infinitely many locally admissible height-one launchpads of valuation one;
7. it identifies the stripped-unit hazard exactly with one event of RL283's boundary hazard and with RL284's labelled accelerated Collatz inverse ray;
8. it proves by genuine reachable examples that one-generation boundary hazard is strictly weaker than the recursively propagated Bellman threat.

The surviving issue is global fixed-seed reachability into high Bellman-threat states as a function of already-paid area.

## 2. Post-departure seam normal form

Use RL289 notation after the common first deviation from the seed itinerary `(101)^infinity`:

- `s` = common first-deviation position;
- `n` = current common word length;
- `q=n-s`;
- `R_x=U_x/2^s`, `R_y=U_y/2^s`;
- `X=R_x+2^q`, `Y=R_y+2^q`.

RL289 gives

`3^d X - Y = 2^q K`

where `K=J+2^d-1`.

For `q>=2` define

`C=(Y-3^(d-1)X)/2`

and

`B=3^(d-1)X-2^(q-1)`.

Then `B` and `C` are odd and

`boxed: B-C = 2^(q-1)(K-1)`.

Hence

`nu_2(K-1)=nu_2(B-C)-(q-1)`.

At `d=1`, with the fixed-seed conjugate endpoints

`p_x=F_x(-6)=X/2^q`,
`p_y=F_y(-6)=Y/2^q`,

one has

`B=2^(q-1)(2p_x-1)`

and

`C=2^(q-1)(p_y-p_x)`.

Thus `B` is the cleared fixed-seed-center/reference contribution and `C` is the cleared translation/Ferrers contribution.

Using RL287's global defect `D` and RL285/RL287 shifted shadows,

`C = -3^r D / 2^(s+1)`.

So the seam translation is the odd 2-adic unit part of the inherited Ferrers/coupon defect after fixed-departure normalization. This is a coupling of old objects, not a new independent scalar reserve.

## 3. Exact seam recurrences

Let `P=2^(q-1)`. On one canonical pair column:

`00`:
- `C' = C-(3^(d-1)-1)P`
- `B' = B+(2*3^(d-1)-1)P`

`11`:
- `C'=3C`
- `B'=3B+P`

`01`:
- `C'=3C-3^d P`
- `B'=3B+(2*3^d+1)P`

`10`:
- `C'=C+P`
- `B'=B-P`

and `P'=2P`.

Modulo already-earned precision `P`:

- if `y=0`, `(B',C') == (B,C) (mod P)`;
- if `y=1`, `(B',C') == (3B,3C) (mod P)`.

The preserved scratch regression checked 39,118 post-departure transitions in the RL289 depth-16 canonical tree with zero recurrence failures.

## 4. Neutral seed prefix gauge is exactly removed

The neutral seed word `(101)` acts in shifted coordinate `u=z+1` as

`F_101(u)=-6+(9/8)(u+6)`.

It fixes `-6` and commutes with the fixed affine map

`A_*(u)=3u+12`.

Prepending `(101)^m` increases both `n` and `s` by `3m` and multiplies both `U_x,U_y` by `8^m`.

Therefore `q`, `R_x`, `R_y`, `X`, `Y`, `B`, and `C` are unchanged.

This is an exact analytic removal of the original neutral-prefix gauge.

## 5. Positive boundary cycles create a second seam gauge

At `d=1`, a zero-height boundary word `w` of length `L`, weight `r`, and affine numerator `Q_w` transports

`(B,C,P) -> (3^r B + P Q_w, 3^r C, 2^L P)`.

If the word is a boundary cycle based at `J_0`, then

`Q_w=(2^L-3^r)J_0`

and therefore

`C -> 3^r C`,
`P -> 2^L P`,
`B-J_0 P -> 3^r(B-J_0 P)`.

The globally reachable positive loop at `J=3` has word `10` in the single-word boundary conjugacy and pair columns `11,00`; in seam coordinates it gives

`(B,C,P) -> (3B+3P, 3C, 4P)`.

Repeated insertion preserves the physical state and accumulated height while changing seam scale.

Any rational scalar invariant of a fixed nontrivial return action `(C,P)->(3^r C,2^L P)` is constant on its rational seam plane: distinct monomials have distinct eigenvalues because powers of `2` and `3` are multiplicatively independent. Therefore another rational ratio/cross-product cannot quotient this cycle gauge.

## 6. Zero-area chronological loop erasure is valid but insufficient

If a genuine canonical history visits the same physical `(d,J)` state twice with no increase in `H`, every intervening starting depth must be `d=1`, since each edge costs `d-1>=0`.

The intervening segment is therefore a zero-height boundary cycle.

Deleting it preserves:

- the splice state;
- legality of every future transition;
- final physical endpoint;
- accumulated height.

Repeated deletion yields a cycle-reduced representative for every reachable endpoint.

However this does not fix history uniquely.

## 7. Fixed-seed branch mergers and acyclic equal-area diamonds

There are exact one-step physical mergers.

For even `d>=2`, put

`K_d=(3^d-1)/2`,
`J_d=(3^d-2^(d+1)+1)/2`.

Both diagonal columns are legal and give the same child because

`3K_d/2 = (K_d+3^d-1)/2`.

Thus `00` and `11` are distinct labelled histories with the same child and the same height cost.

A genuine fixed-seed instance occurs after `x=0001`, which reaches `(d,J,H)=(2,1,3)`; both next bits reach `(2,3,4)`.

There is also a loop-free equal-area diamond from the globally reachable state

`(d,J,H)=(2,3,1)`:

- suffix `01` reaches `(1,2,3)`;
- suffix `110` also reaches `(1,2,3)`.

Both pay exactly two units of area and contain no repeated physical state.

Their frozen seam endpoints are:

- `01`: `(q,P,B,C)=(8,128,205,-51)`;
- `110`: `(q,P,B,C)=(9,256,423,-89)`.

Both satisfy `B-C=PJ`, but the individual seam coordinates differ.

With `t=C/P`, the two representatives obey

`t_B+1/2 = (3/2)(t_A+1/2)`.

Therefore even loop-erased chosen-history seam/rank data are not physical invariants.

Classification:

`FIXED_SEED_BRANCH_MERGER_AND_ACYCLIC_EQUAL_AREA_SEAM_GAUGE_BARRIERS_PROVED`.

## 8. Minimal future-threat Bellman envelope

For a physical state `s=(d,J)`, define

`Bcal(s) = sup_sigma [nu_2(J_end)-Delta H_sigma]`

over legal future segments `sigma` ending at a positive even `d=1` checkpoint. The empty segment is allowed when the current state is already such a checkpoint.

For a fixed legal segment of length `L`, RL287 gives

`2^L J_end = c_sigma J + b_sigma`

with `c_sigma` odd. Hence equivalently

`Bcal(d,J) = sup_sigma [nu_2(c_sigma J+b_sigma)-L_sigma-Delta H_sigma]`.

It obeys the exact Bellman equation

`Bcal(s)=max(current checkpoint hazard, max_(s->s') [Bcal(s')-(d(s)-1)])`.

Any Bellman dual/subsolution `Phi` satisfying

`Phi(s')-Phi(s) <= d(s)-1`

on each legal edge and

`Phi(1,J)>=nu_2(J)`

at positive even checkpoints must dominate `Bcal`.

Thus `Bcal` is the minimal possible future rejected-tube reserve.

Gate A is equivalent to

`Bcal(1,-13)<=0`.

## 9. Universal height-one terminal launchpads

RL282 proved pure-zero terminal-tail local families for every odd `k>=3` and every prescribed one-zero excursion height `h>=2`.

RL290 closes the missing `h=1` case.

For odd `k>=3` and odd `q>=1`, put

`J_0(k,q)=1+2^q(2^k-1)`

and

`J_in(k,q)=(2^(q+2)(2^k-1)-2)/3`.

Then

`3(J_in+4)=2(2J_0+3)`

so the genuine positive one-zero word `01` takes `J_in` to `J_0` with exact height one.

Appending `q` boundary zeros gives

`T_0^t(J_0)=1+2^(q-t)(2^k-1)`

and terminates at `2^k`.

The one-zero shell condition is exact:

`nu_3(J_0)=1 <=> q != k+2 (mod 6)`.

For every odd `k`, two of the three odd classes `q mod 6` survive. Hence there are infinitely many positive locally admissible exact height-one terminal blocks

`J_in --01--> J_0 --0^q--> 2^k`.

Every launchpad has

`nu_2(J_in)=1`

and the affine ray law

`J_in(k,q+2)=4J_in(k,q)+2`.

The RL282 scale/zero-mass/F barriers extend to this minimal-height case:

`Q_in = Q_T * 3 / 2^(q+2)`,

`S_block = Q_T[1-2^(-q)+3/2^(q+2)] -> Q_T`,

`F_T-F_in = Q_T[4-7/2^(q+2)] -> 4Q_T`.

Thus the old "cheap final tail" obstruction persists at absolute minimum positive excursion height.

## 10. Stripped-unit renormalization and exact hazard meaning

For a positive even checkpoint `J`, define

`t=nu_2(3J+2)`,
`u=(3J+2)/2^t`.

If `t>=3`, the canonical suffix

`01 0^(t-2)`

is automatically legal, costs exactly one unit of height, and reaches

`J# = u+1 = (3J+2)/2^t + 1`.

Therefore the nested valuation

`nu_2(u+1)`

is exactly the rejected-tube depth of a specific future checkpoint exposed after one paid excursion and a free boundary run.

Writing `J=2n`,

`3n+1=2^(t-1)u`.

So `u` is precisely the accelerated odd Collatz image of `n` with exact removal label `t-1`, matching RL284's labelled accelerated bijection.

For a prescribed successor `M=u+1`, the physical predecessor ray is

`J_t(M)=(2^t(M-1)-2)/3`

with

`J_(t+2)(M)=4J_t(M)+2`.

This is exactly twice RL284's affine accelerated-predecessor ray.

## 11. Exact fixed-seed ballot action of stripped-unit suffix

At a balanced checkpoint let

`a=C^n(z)`,
`b=C^n(A(z))`

be the two ordinary Collatz shadow endpoints, so

`J=3a-b+1`.

The hazard-extraction suffix above sends them to

`a'=(3a+2)/2^t`,
`b'=(3b+1)/2^t`

and exactly

`3a'-b'+1 = (3J+2)/2^t + 1 = J#`.

The map is labelled-invertible:

`a=(2^t a'-2)/3`,
`b=(2^t b'-1)/3`.

Thus the stripped-unit operation is itself a synchronized labelled accelerated-Collatz renormalization inside the fixed-seed ballot pair.

## 12. Positive-even checkpoint Bellman quotient

Define a macro-edge between positive even `d=1` checkpoints as follows:

1. leave the even checkpoint through its forced off-boundary launch;
2. follow one genuine first return to `d=1`;
3. if the return is odd, allow an arbitrary zero-height retained boundary run;
4. take a complementary even exit.

Give the macro-edge the positive height `h` paid by the excursion.

Every edge has `h>=1`; all zero-height boundary gauges are compiled into the edge relation.

For a positive even checkpoint define

`V(J)=sup_future [nu_2(J_f)-Delta H]`.

Then

`boxed: V(J)=max(nu_2(J), sup_((J',h) in Gamma(J)) [V(J')-h])`.

This is the exact gauge-invariant Bellman operator on positive checkpoints.

## 13. Complete height-one kernel

A first-return excursion of height exactly one has no off-boundary freedom: its `x` word is `01`.

For `J == 6 (mod 8)`, it returns directly to the even checkpoint

`J' = 3(J+2)/4`.

For `J == 2 (mod 8)`, it returns to an odd boundary state

`J_0=3(J+2)/4`

with RL283 boundary coordinate

`n_0=(J_0-1)/2=(3J+2)/8`.

Let `C` be RL283's unique odd-retaining boundary map and `E` the complementary even exit.

Then the entire cost-one successor set is exactly

`boxed: Gamma_1(J)={E(C^s(n_0)):s>=0}`.

Therefore RL283's one-generation boundary hazard

`Beta(n)=sup_s nu_2(E(C^s(n)))`

is exactly the one-generation terminal-valuation projection of the height-one Bellman kernel.

## 14. One-generation boundary hazard is strictly weaker than Bellman threat

The distinction is genuine on globally reachable certified states.

Inside the exact RL282 `H<=22` positive-checkpoint certificate there is the cost-one chain

`(2514,15) -> (5378,16) -> (21842,17) -> (8192,18)`.

The frozen macro words for the final three edges are:

- `2514 -> 5378`: `0111110101`;
- `5378 -> 21842`: `01101011110110111`;
- `21842 -> 8192`: `010`.

The final state is `8192=2^13`, and `H=18` is the certified minimum height for `k=13`.

At `J=21842`,

`nu_2(J)=1`,
`3J+2=8*8191`,

and the cost-one stripped-unit successor is exactly `8192`. Hence

`V(21842)>=12`.

At `J=5378`, the immediate stripped-unit depth is only `1`. After its `01` excursion the odd boundary coordinate is `n_0=2017`; the complete one-generation RL283 boundary hazard is only

`Beta(2017)=5`.

Nevertheless one of the corresponding even exits is `21842`, whose own valuation is only one but whose future Bellman threat is large. Therefore

`V(5378)>=11`.

Thus

`ONE_GENERATION_BOUNDARY_HAZARD_STRICTLY_INSUFFICIENT_FOR_FULL_BELLMAN_THREAT_PROVED`.

The recursive Bellman hierarchy is genuinely stronger than a one-generation hazard maximum.

## 15. Nested valuation is not an inductive potential

A globally reachable positive checkpoint `J=1074` has nested hazard

`nu_2((3J+2)/2^nu_2(3J+2)+1)=2`.

The legal positive-phase cost-one macro

`1074 --011101--> 1364`

reaches a checkpoint whose same nested hazard is `11`.

Thus the nested coordinate can gain nine arithmetic bits for one unit of area.

It is useful as one exact Bellman successor selector, not as a standalone edge-Lipschitz potential.

## 16. Finite evidence only

The following was observed on the exact RL282 `H<=22` positive-even checkpoint set (146,341 checkpoints):

`nu_2((3J+2)/2^nu_2(3J+2)+1) <= H-2`.

No violation was found; equality occurred only at `(J,H)=(2,3)` and `(8,3)`.

The same inequality was checked on ordinary fixed-length canonical trees through depth 33 with no observed violation.

This is explicitly

`UNPROMOTED_FINITE_EVIDENCE_ONLY`.

It does not narrow the residual and is not recommended as the principal successor route because the coordinate is not inductive.

## 17. Strategic conclusion

RL290 began by trying to price rejected-tube depth with a gauge-invariant seam/history charge.

The seam normal form is exact and useful, but successively stronger gauge obstructions were proved:

1. neutral seed-prefix insertion;
2. genuine positive boundary cycles;
3. physical one-step branch mergers;
4. acyclic equal-area history diamonds.

Chosen-history seam/rank observables therefore do not provide a robust physical charge.

The canonical replacement is the Bellman future-threat envelope.

Quotienting zero-height boundary motion yields a positive-even checkpoint graph with strictly positive costs. Its height-one kernel is completely classified and already contains all of:

- RL282 terminal-tail launchpads;
- RL283 boundary hazard;
- RL284 labelled accelerated inverse rays;
- RL289 fixed-seed ballot shadows.

The core open problem can now be phrased as:

`fixed-seed minimum historical area needed to enter states of Bellman threat >= k`.

The current Bellman/checkpoint-kernel route is live and has considerable momentum, but RL290 does not claim it is the unique or best route.

## 18. Scope and successor policy

No Gate-A closure is claimed.

Gate B, fifth selector, and Radius 6+ remain frozen.

The user has explicitly requested that the successor NOT simply continue this route immediately. RL291 must first perform a broad programme-wide audit and synthesis, reviewing the full research history era-by-era, identifying overlaps, changed significance, dormant lemmas, contradictions/corrections, and possible shortcuts or fast tracks.

The Bellman route must be preserved in that audit as an important live late-stage option.

Generated knowledge catalogues are unchanged and remain `stale/deferred` under connector-worker closeout policy.
