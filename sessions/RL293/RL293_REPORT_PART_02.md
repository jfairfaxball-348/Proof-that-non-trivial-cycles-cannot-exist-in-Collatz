## 8. Compact first-checkpoint splice through H<=28

To close the next terminal exponent without extending the enormous full first-positive closure, RL293 uses RL288's promoted necessary conditions for the first positive state.

At first positivity put

`M=J+2^d-2`, `A=H+d-1`.

Every genuine first-positive state satisfies

- `0<M<3^d`;
- `nu_2(M)<=A`, with equality globally unique at `(d,J,H)=(3,2,1)`;
- `J mod 3 in {0,(-1)^d}`;
- `H >= (d-1)(d-2)/2`.

For total historical height `H<=28`, these conditions give a finite over-approximation of exactly `19,005` possible first-positive seed states. Assigning each state its smallest analytically permitted height can only make the relaxed model more dangerous than genuine fixed-seed ancestry.

Instead of closing all positive futures, stop at the first positive even `d=1` checkpoint. A positive odd `d=1` return is followed along its unique retained zero-height boundary orbit, collecting all complementary even exits until repetition.

The complete compact transient contains:

- `21,787` positive `d>1` physical states;
- `23` positive odd boundary origins;
- `94` possible first positive even checkpoints.

Let `P=(d,J)=(2,3)`, reached genuinely from the fixed seed at historical height one. An independent exact positive closure from `P` through added cost 14 contains 2,509 physical states and reaches all 94 candidate checkpoints.

For 91 of them,

`1+m_P(E)<=H_rel(E)`.

The only relaxed exceptions are

- `E=2`: `H_rel=2`, `m_P=2`;
- `E=8`: `H_rel=2`, `m_P=2`;
- `E=6`: `H_rel=5`, `m_P=8`.

The first two are repaired by RL281's promoted theorem that every genuine positive `d=1` state has historical height at least three. For `E=6`, an exact fixed-seed search stopping at the first positive even checkpoint through historical height eight contains 225 transient states and finds only `2@H=3` and `8@H=3`. Therefore a genuine first checkpoint `6` has height at least nine, exactly matching `1+m_P(6)=9`.

Consequently every genuine first positive even checkpoint occurring by historical height 28 can be replaced by a genuine prefix through `P` reaching the identical checkpoint at no greater total height.

Classification — exact finite certificate plus inherited analytic envelope:

`FIXED_SEED_FIRST_CHECKPOINT_H28_MINPLUS_SPLICE_TO_2_3_PROVED`.

Portable verifier: `verification/verify_rl293_first_checkpoint_splice.py`.

## 9. Exact P-source closure closes k=29

Close every legal positive physical future from `P=(2,3)` through added height 27, retaining only the minimum cost for each physical `(d,J)` state. Positivity is forward invariant and future legality depends only on the physical state, so shortest-path dominance is exact.

The portable C++ verifier gives:

- positive physical states: `23,652,724`;
- positive even checkpoints through added cost 23: `320,762`;
- positive even checkpoints through added cost 26: `2,865,881`;
- positive even checkpoints through added cost 27: `5,962,876`.

The complete power minima are

`k1:A2,k3:A2,k5:A8,k7:A14,k9:A14,k11:A17,k13:A17,k15:A21,k17:A24,k19:A25,k21:A23`.

The cost-23 checkpoint count reproduces RL292's independent genuine H<=24 checkpoint count under the one-unit `P` normalization, and the power minima through cost 26 reproduce RL292's independent relaxed-first-positive calculation.

Crucially,

`(d,J)=(1,2^29)`

is absent through added cost 27.

Classification — exact finite certificate:

`P_SOURCE_A27_K29_EXCLUSION_PROVED`.

Now suppose a genuine terminal `J=2^29` had `H_can<29`; then `H_can<=28`. Take its first positive even checkpoint `E`, at height `H_E<=28`. Section 8 supplies a genuine replacement prefix through `P` reaching the same `E` at height at most `H_E`. Copy the original suffix from `E` onward. The resulting positive future from `P` reaches `2^29` with added cost at most

`H_can-1<=27`,

contradicting the exact P-source certificate.

Therefore

`k=29 => H_can>=29`.

Combined with RL292, the exact residual is now

`k>=31`, `k` odd, `H_can<k`.

Classification — derived Gate-A contraction:

`FIRST_POSITIVE_CHECKPOINT_MINPLUS_SPLICE_AND_P_SOURCE_K29_GATE_A_CLOSURE_PROVED`.

Portable verifier: `verification/verify_rl293_p_source_k29.cpp` with frozen output.

## 10. First-boundary normalized-K corridor

RL288's first-positive theorem gives `0<M<3^d`, where `M=K-1`. Hence at the first positive state, integrally,

`0<K<=3^d`.

Define

`q=K/3^d`.

Using RL279's exact normalized recurrence, every legal transition satisfies:

- if `x=1`, `q' <= (3/2)q`;
- if `x=0`, `q' <= max(1,q)`.

Let first positivity occur at historical height `H0`, and let the first subsequent `d=1` boundary state occur at height `H`. Before that return every step begins at depth at least two and therefore costs at least one. The number of `x=1` steps is at most `H-H0`. Thus at first boundary entry

`J_b+1 <= 3(3/2)^(H-H0)`.

Equivalently, with

`u_b=(J_b+1)/2`,

`u_b <= (3/2)^(H-H0+1)`.

This is substantially sharper than the elementary `J<2^(H+1)` magnitude box.

On a positive odd boundary state put `u=(J+1)/2=n+1`. The retained boundary map is

- `u` even: `u'=(3/2)u`;
- `u` odd: `u'=(u+1)/2`.

For odd `u>=3`, the latter is at most `(2/3)u`. The exceptional `u=1` transition is the zero-height self-loop and can be erased at witness level by RL290's exact zero-area loop-erasure theorem.

Take a loop-erased retained boundary prefix with `r` one-steps and `z` zero-steps. Then

`u_t <= u_b (3/2)^(r-z)`.

Any complementary even exit `E` at its endpoint obeys `E<3u_t`. If it is a first Gate-A failure at historical height `H`, then `nu_2(E)>=H+1`, hence `E>=2^(H+1)`. Combining inequalities gives

`r-z+2 > H0 + lambda H`,

where

`lambda=log_(3/2)(4/3)=0.7095112913514545...`.

Thus shallow or low-signed-drift boundary words are analytically incapable of producing the first checkpoint violation. A dangerous boundary prefix must have approximately `0.71 H` excess retained one-steps over zero-steps, strengthened by the height already paid before positivity.

Classification — proved analytic mathematics:

`FIRST_BOUNDARY_NORMALIZED_K_CORRIDOR_AND_HIGH_SIGNED_DRIFT_DANGER_TREE_REDUCTION_PROVED`.

The explicit local immediate-danger family

`n_R=(2^R-2)/3`,
`J_R=(2^(R+1)-1)/3`,
`H=R-1`

for odd `R` has complementary exit exactly `2^R`, and for `R mod 6 in {3,5}` passes the inherited mod-3 filter. It shows why the old magnitude box plus mod 3 is insufficient. But the new normalized-K corridor excludes every member with `R>=5` at that putative historical height.

Portable regression: `verification/verify_rl293_first_boundary_corridor.py`.

## 11. Dangerous first checkpoints force principal parity-cylinder representatives

Let `w` be the loop-erased retained boundary word before a first checkpoint failure; let its length be `t=r+z`. Section 10 gives

`t+2 >= r-z+2 > H0+lambda H`,

hence

`t>H0+lambda H-2`.

Also

`u_b <= (3/2)^(H-H0+1)`.

Every genuine first-positive state has `H0>=1`. Put `a=log_2(3/2)`. For `H>=9` and `H0>=1`,

`H0+lambda H-2 - a(H-H0+1)
 = H(lambda-a)+H0(1+a)-2-a >0`.

Therefore

`log_2 u_b < t`,

so

`u_b<2^t`.

Since `n_b=u_b-1` is nonnegative and its first `t` retained parity bits are exactly `w`, RL289's parity-cylinder bijection says

`n_b mod 2^t = zeta_w`,

where `zeta_w` is the least nonnegative representative of that cylinder. But `0<=n_b<2^t`, so in fact

`n_b=zeta_w`.

Thus a dangerous first checkpoint cannot use RL287's arbitrary higher-lift freedom. It is forced onto the principal representative of its own parity cylinder.

Classification — proved analytic mathematics:

`FIRST_CHECKPOINT_DANGER_FORCES_PRINCIPAL_PARITY_CYLINDER_REPRESENTATIVE_PROVED`.

Let

`e_w=C_w(zeta_w)`

be RL289's endpoint code, satisfying `0<=e_w<3^r`. If the hazardous complementary exit is the terminal `2^k`, there are only two possibilities:

- the `alpha=-1` hazard: `e_w=2^k-1`;
- the `alpha=-2/3` hazard: `e_w=(2^k-2)/3`.

Hence respectively `2^k<=3^r` or `2^k<3^(r+1)`.

For the second root, if `3e+2=2^R q` with odd `q`, then

`e=(2^R q-2)/3`,

which is exactly the RL284/RL290 labelled height-one predecessor ray. Retaining rather than taking the hazardous exit gives the next `R` boundary parity bits `01 0^(R-2)` and reaches the reduced checkpoint `q+1`. For a terminal power, `q=1`, so the alternative zero-height branch reaches checkpoint `2`.

Important non-claim: numerical equality with the predecessor ray does not by itself transfer fixed-seed ancestry. No reverse-reachability theorem is inferred.

## 12. Bellman front door reduces to first-d=1 minimum ownership

Let `P=(2,3)`. Consider any one of RL292's reachable front-door states `s` with its historical credit/threshold `T_s`. For a future from `s` which eventually reaches a positive checkpoint, let `B` be the first positive `d=1` physical state on that future and let `c_s(B)` be the cost from `s` to `B`.

Suppose one proves the owner inequality

`m_P(B)<=c_s(B)+T_s-1`

for every such `B`, where `m_P(B)` is the minimum positive cost from `P` to the identical physical state `B`.

Splice the `P` owner path to `B` onto the unchanged suffix from `B` to any future checkpoint `q`. Then

`nu_2(J(q))-cost_s(q)
 <= Bcal(P)+T_s-1`.

Taking the supremum over futures gives

`Bcal(s)<=Bcal(P)+T_s-1`.

Therefore the single tight inequality

`Bcal(P)<=1`

would imply `Bcal(s)<=T_s` for each slack front-door state satisfying the owner hypothesis. This is an exact min-plus reduction; it does not assert the owner hypothesis all-depth.

Classification — proved analytic mathematics:

`BELLMAN_FRONT_DOOR_REDUCES_TO_FIRST_D1_MINIMUM_OWNER_DOMINATION_PROVED`.

## 13. Exact first-d=1 owner certificate through H<=60

RL293 tests the owner hypothesis on a much wider but still compact finite cut. Using RL288's first-positive necessary conditions through historical height 60 gives a deliberate over-approximation with

- `525,986` relaxed first-positive seed states;
- `608,084` positive transient physical states before first `d=1`;
- only `865` possible first positive `d=1` states.

Independently, the `P=(2,3)` owner cone through added cost 22 contains `619,141` stored physical/boundary states sufficient to compare all 865 arrivals.

The relaxed owner inequality `1+m_P(B)<=H_rel(B)` fails only at

`(J,H_rel,m_P)=(2,2,2),(3,2,2),(6,5,8)`.

The first two are repaired by RL281's analytic `H>=3` theorem for genuine positive `d=1` states. The third is repaired by the exact fixed-seed first-checkpoint cut through H<=8: it has 225 transient states and only `2@3,8@3`, so a genuine first checkpoint `6` has height at least nine and `1+m_P(6)=9`.

Therefore every genuine first positive `d=1` state reached by historical height 60 satisfies

`m_P(B)<=H(B)-1`.

Classification — exact finite certificate:

`FIXED_SEED_FIRST_D1_MINIMUM_OWNER_H60_CERTIFICATE_PROVED`.

Mechanical repair at closeout: the packaged verifier originally asserted `len(dist)==225` for the tiny H<=8 fixed-seed cut. The map also stores its two terminal checkpoint states, so its total size is 227 while the transient count is 225. The assertion was corrected to record both numbers. The endpoint set, heights, mathematical claim, and all other counts were unchanged. This is a bookkeeping repair, not a mathematical correction/demotion.

Portable verifier: `verification/verify_rl293_first_d1_owner_h60.py`.

## 14. What remains open

RL293 does not prove:

- `Bcal(2,3)<=1`;
- the all-depth first-d=1 owner theorem `m_P(B)<=H(B)-1`;
- the full static danger-ball separation `mu(Ball)>=R`;
- the checkpoint-8 excess-one inequality beyond the certified `A<=7` region;
- any terminal contraction at `k>=31`;
- Gate B, the fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

Checkpoint `8` remains a sharp local branch, not a mandatory universal gateway. The new principal-cylinder theorem is restricted to dangerous first-checkpoint geometry, not arbitrary later boundary visits.

## 15. Strategic successor

The preferred successor is no longer a generic search over all static danger-tree lifts. Two reductions now point to one precise target:

1. prove the all-depth first-positive `d=1` minimum-owner theorem with root `P=(2,3)`, or isolate the first exact counterexample and the minimal missing ancestry coordinate;
2. use that reduction to collapse the five-state Bellman front door to the tight `P` source and prove `Bcal(P)<=1` by intersecting fixed-seed ballot ancestry with the principal-representative/high-signed-drift sector of the static danger tree.

The `alpha=-2/3` root is exactly aligned with the labelled height-one predecessor ray and should be treated separately from `alpha=-1` if useful.

Do not make a raw H<=30/H<=31 expansion the principal route. The k=29 certificate demonstrates that compact first-checkpoint cuts can close finite residuals when needed, but the next principal objective remains scalable.

## 16. Verification summary

Frozen portable verification under `sessions/RL293/verification/`:

- `verify_rl293_pullback_barrier.py` — PASS;
- `verify_rl293_checkpoint8_lowarea.py` — PASS;
- `verify_rl293_checkpoint2_domination.py` — PASS;
- `verify_rl293_first_checkpoint_splice.py` — PASS;
- `verify_rl293_p_source_k29.cpp` — PASS;
- `verify_rl293_first_boundary_corridor.py` — PASS;
- `verify_rl293_first_d1_owner_h60.py` — PASS after the mechanical 225/227 repair;
- all Python sources compile cleanly.

The target-specific red-team ledger is `verification/RL293_RED_TEAM.md`.
