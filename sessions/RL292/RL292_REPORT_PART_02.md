- upstream minimum physical states: `7,396,469`;
- positive-even minimum checkpoints: `320,762`;
- positive-even minimum checkpoints with `H<=22`: `75,232`;
- odd boundary origins: `58,132`;
- maximum retained stay-odd trace: `356`.

Classification:

`EXACT_MINIMUM_HEIGHT_H24_K25_GATE_A_CLOSURE`.

## 7. First-positive analytic over-approximation closes k=27

For the first positive state define

`M=J+2^d-2`, `A=H+d-1`.

RL288 proves

`0<M<3^d`, `nu_2(M)<=A`,

with equality only at `(d,J,H)=(3,2,1)`. Combine this with the promoted mod-3 reachability class and the minimum ascent-area constraint. For a hypothetical `k=27` violator, `H<=26`, hence only `d<=8` can occur.

RL292 deliberately admits every positive physical state satisfying these necessary analytic first-positive constraints, whether or not genuinely fixed-seed reachable, and assigns each its smallest analytically permitted height. This is a strict over-approximation of genuine first-positive ancestry.

There are exactly `6,224` relaxed seed states. Exhaustive positive-future closure through total `H<=26`, retaining only the minimum height for each physical state, contains `11,380,217` positive physical states and no `(1,2^27)`.

The relaxed power minima are

`k1:H2,k3:H2,k5:H8,k7:H14,k9:H14,k11:H17,k13:H17,k15:H21,k17:H24,k19:H25,k21:H23`.

These are deliberately cheaper than genuine fixed-seed minima, so absence of `2^27` on this larger relaxed graph implies absence on the genuine graph. Therefore

`k=27 => H_can>=27`.

Combined with the inherited and RL292 lower-exponent closures, the exact residual becomes

`k>=29`, `k` odd, `H_can<k`.

Classification:

`FIRST_POSITIVE_ANALYTIC_OVERAPPROX_H26_K27_GATE_A_CLOSURE`.

## 8. Checkpoint-8 transformed-shadow resonance normal form

For ordinary Collatz shadow endpoints `a,b`, define

`u=2a+1`, `v=2b+1`, `D=v-3^d u`.

Then exactly

`D=-2J+3^d-2^(d+1)+1 = -2K+3^d-1`,
`K=J+2^d-1`,

and on one paired column ending at depth `d'`,

`2D'=3^y D+1-3^(d')`.

Equivalently, by column type,

- `00`: `D'=-K`;
- `11`: `D'=3^d-1-3K`;
- `01`: `D'=-(3K+1)`;
- `10`: `D'=3^(d-1)-K`.

At a balanced checkpoint, `D=-2J`.

For a future from checkpoint `8`, after the forced first `01` column the state is `(d,J,K,D,A)=(2,15,18,-28,0)`. The strong live candidate `nu_2(J_end)<=A+1` becomes `nu_2(D)<=A+d+1` at all depths.

If this candidate first fails at a child of area `A'` and depth `d'`, then

`D_parent == 3^(-y)(3^d' - 1) (mod 2^(A'+d'+3))`.

Thus every first failure lies in one explicit depth-labelled 2-adic resonance ball. In `K` coordinates the four resonance forms are

`K`, `3K-3^d+1`, `3K+1`, `K-3^(d-1)`.

At the `d=1` wall these reduce exactly to RL283's two complementary boundary-exit hazard templates.

Classification:

`CHECKPOINT8_TRANSFORMED_SHADOW_RESONANCE_NORMAL_FORM_PROVED`.

## 9. Exact checkpoint-8 low-cost kernel gap

Exhausting all first-return excursions from checkpoint `8` of height below eight gives exactly

`8 --001,h=2--> 5`,
`8 --011,h=2--> 12`.

There are no first returns of heights `1,3,4,5,6,7`.

The retained zero-height boundary orbit from odd return `5` is `5 <-> 3`, with complementary even exits exactly `{2,8}`. Therefore every checkpoint-quotient macro from `8` of cost below eight has cost exactly two and lands in `{2,8,12}`; every other checkpoint macro from `8` costs at least eight.

Classification:

`CHECKPOINT8_LOW_COST_KERNEL_GAP_PROVED`.

## 10. Static boundary-hazard preimage tree

At a positive odd boundary state put `n=(J-1)/2`. The retained boundary map is the ordinary half-step Collatz map `C`, and the complementary exit hazard is

`h(n)=max(nu_2(n+1),nu_2(n+2/3))`.

The two fixed hazard roots are

`alpha_1=-1`, `alpha_0=-2/3`.

For a binary word `w` of length `t`, weight `r`, and ordinary Collatz numerator `Q_w`, define

`rho_(w,alpha)=(2^t alpha-Q_w)/3^r`.

Then `C_w(rho)=alpha` and

`nu_2(C_w(n)-alpha)=nu_2(n-rho)-t`.

If `w` is not the actual first `t` parity bits of `n`, RL289's phase-vector isometry gives `nu_2(n-rho)<t`; such a branch cannot realize the positive hazard supremum. Therefore RL283's dynamic boundary hazard has the exact static form

`Beta(n)=sup_(t,w,alpha) [nu_2(n-rho_(w,alpha))-t]`.

Equivalently,

`{Beta>=R}=union_(t,w,alpha) {nu_2(n-rho_(w,alpha))>=R+t}`.

Thus arbitrary future zero-height boundary danger is a fixed weighted infinite binary tree of 2-adic balls.

Classification:

`STATIC_BOUNDARY_HAZARD_PREIMAGE_TREE_PROVED`.

## 11. No finite affine valuation family can dominate Beta

Fix `L>=2` and positive odd `q`, and put

`n_(R,q)=2^L(2^R q-1)`.

The first `L` retained boundary bits are zero and

`C^L(n_(R,q))=2^R q-1`,

so `Beta(n_(R,q))>=R`.

For any finite collection of nonzero affine rational/integer forms `f_i(n)`, choose `L` so that none vanishes at `-2^L`. Then `n_(R,q)` tends 2-adically to `-2^L`, so every `nu_2(f_i(n_(R,q)))` eventually stabilizes while `Beta(n_(R,q))` tends to infinity. The odd parameter `q` can simultaneously be chosen so the associated positive boundary state lies in the promoted mod-3 admissible classes.

In particular, the four transformed-D/K wall forms stay at valuations `(1,2,0,0)` on an explicit all-zero family while `Beta` grows arbitrarily.

Therefore no finite maximum of affine 2-adic valuation templates can dominate the full boundary hazard, even after the local mod-3 filter.

Classification:

`FINITE_AFFINE_TEMPLATE_DOMINATION_OF_BOUNDARY_BETA_IMPOSSIBLE_PROVED`.

## 12. Corrections, demotions, and failed shortcuts

The following exploratory statements are explicitly NOT promoted:

- `nu_2(3J+2)<=mu(J)` and finite combinations such as `max(nu_2(J-2)+2,nu_2(3J+2))<=mu(J)` survive bounded data only;
- minimum-area height-one-arrival safety was superseded as principal strategy by the exact front door;
- crude real-magnitude / `log(J+c)` Bellman potentials fail, already on genuine low-cost edges;
- the statement that a first valuation failure from checkpoint `8` must be exactly a prescribed power of two is valid only when it is also the first magnitude escape; harmless earlier magnitude escapes prevent globalization;
- the finite observation that low-height positive checkpoint closures generated from `8` reproduce the full low-height checkpoint set does NOT mean all genuine terminal paths pass through `8`; `32` is reachable at height `13` while avoiding checkpoint `8`;
- the checkpoint-8 excess-one ballot inequality remains conjectural despite strong finite evidence;
- universal checkpoint-8 domination and equality classifications remain unproved;
- an attempted H<=28 computation did not complete and is not promoted;
- finite renewal grammars proliferate and do not by themselves replace the static boundary phase tree.

These corrections are route discipline, not demotions of previously authoritative theorems.

## 13. Mandatory red-team ledger

RL292's promoted results were checked against the inherited failure mechanisms as follows.

- arbitrary positive boundary retention / zero-cost phase reset: incorporated explicitly in the physical checkpoint quotient and then exactly represented by the static `Beta` tree;
- branch mergers and equal-area diamonds: Bellman statements are on physical states; no chosen-history charge is promoted;
- neutral `(101)` seed-prefix gauge: quotiented explicitly in the three-root/five-state front door;
- RL287 cylinder isometry and RL289 suffix transparency: used positively in the static-tree proof and the finite-affine-template barrier;
