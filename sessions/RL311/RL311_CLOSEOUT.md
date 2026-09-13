# RL311 closeout — extremal profile compression, Gate-A fallback barriers, and short owned balanced return

Date: 2026-09-13
Status: CLOSED AND FROZEN
Session type: MATHEMATICAL EXECUTION FROM RL310 GLOBAL EXTREMAL ROUTE
Base HEAD: `d54bb13118f6fd80b8fc0632e8441f62c932495c`
Successor: RL312

## 0. Executive conclusion

RL311 does not prove global non-trivial-cycle exclusion. Gate A and Gate B remain open.

It does materially contract the parent global problem in the `lambda<3` one-sided extremal sector. The main late result is an exhaustive owned balanced-return compression theorem:

> For the canonical gcd-block decomposition `A=ga`, `L=g ell`, if `lambda<3` and
> `h=ceil(log_3((4M+1)/(4R+1)))`, then either `g<=h+1`, or there is a proper pair of genuine full-cycle rotations at equal block imbalance level separated by at most `h+1` reduced blocks. Their physical states satisfy
> `1/lambda < (4x_k+1)/(4x_j+1) < lambda < 3`.

This replaces the historical balanced-return / strict-excursion split by a short owned balanced-return extractor or a linearly controlled multiplicity survivor.

RL311 also proves that, in the same one-sided sector, the extremal determinant density, the extremal transport-profile height, and the old Gate-B block-imbalance height are all controlled by the single physical aspect-ratio scale `h`. The remaining obstruction is no longer an independent vertical discrepancy scale; it is the lack of a genuinely ownership-sensitive consumer for the resulting short balanced pair / horizontal replication.

No RL311 result is promoted outside its exact hypotheses.

## 1. Authoritative incoming structure

RL311 inherited from RL310, for every hypothetical primitive positive cycle:

- physical minimum `R` and maximum `M`;
- full shortcut length `A` and odd count `L`;
- `lambda=2^A/3^L`;
- physical forward extremal arc `R -> M` of length `d` and odd count `o`;
- complementary arc `M -> R`;
- canonical slope bracket
  `d/o < log_2 3 < A/L < (A-d)/(L-o)`;
- extremal cross-determinant
  `kappa_ext=Ao-dL>0`;
- exact weighted extremal identity
  `[sum q_i 3^(-G_i)]/[sum q_i]=(4M+1)/(4R+1)`;
- in the sufficient branch `lambda<3`, the one-sided profile
  `P_i=o-W_i(d)>=0`, `sum P_i=kappa_ext`, and `kappa_ext>=h^2` with
  `h=ceil(log_3((4M+1)/(4R+1)))`.

RL311 preserved RL310's explicit rejection of proper-prefix ownership inferred merely from denominator-factor divisibility.

## 2. Complementary one-sidedness branch: exact skew amplification, then frozen

Write

`G_i=W_i(d)-o`, `G_0=0`, `g=max_i G_i`.

If `g=0`, one-sidedness already holds. If `g>=1`, the physical extremal segment comparison gives

`g ln 3 <= S_RM`.

Combining this with the RL310 segment packing estimate yields

`M >= (R-1) 3^(9g) exp(-3/R)`

and

`o >= 1 + (R-1)/3 * (3^(9g) exp(-3/R)-1)`.

With `Q_ext=(4M+1)/(4R+1)` and `h=ceil(log_3 Q_ext)`, one gets

`h>=9g-1`,

so the weighted extremal identity forces

`min_i G_i <= -(9g-1)`.

Hence

`range(G)>=10g-1`,
`A>=20g-2`.

Using

`delta=A ln2-L ln3=ln lambda`,
`a=o ln3-d ln2>0`,

one also has the exact determinant decomposition

`kappa_ext ln2 = o delta + L a`.

Therefore in the same complementary branch

`kappa_ext > g o log_2 3`,

hence

`kappa_ext > g log_2 3 * [1 + (R-1)/3 * (3^(9g) exp(-3/R)-1)]`.

Classification: analytic. Parent delta: LATERAL.

Barrier: this strongly amplifies discrepancy but still supplies only a lower bound. RL274's determinant/discrepancy consumer also weakens as counterflow grows. After two consecutive non-improving extremal checkpoints, this branch was frozen under the RL311 pivot rule.

## 3. Gate-A fallback: exact dependency contraction

RL311 next activated the parent-near Gate-A fallback without reopening the older local programmes wholesale.

Exact physical Bellman paths were found from the already-required source `(2,-84)`:

`(2,-84) --101011101100000, cost 8--> U=(4,21)`,

`(2,-84) --101001000, cost 11--> V=(5,104)`.

Together with the already-frozen first-positive front door for `(3,-28)`, this gives

`B(3,-28) <= max(B(2,-17)+2, B(2,-84)+6)`.

Under the required Gate-A ceilings

`B(2,-17)<=1`, `B(2,-84)<=2`,

this yields only

`B(3,-28)<=8`.

It nevertheless removes `X,Y,R1,R2,(4,39)` as independent dependencies for the `(3,-28)` node.

Classification: exact Bellman reduction. Parent delta: EASIER.

## 4. V/Y contraction and exact 21-unit D0-tail barrier

For

`V=(5,104)`, `Y=(6,504)`,

exact first-bit decomposition gives

`B(V) <= max(B(Y)-4, B(4,39)-1)`.

Hence `B(Y)<=12` would imply `B(V)<=8` under the already-required `B(4,39)<=3`.

For `Y`, exact first-bit decomposition gives

`Y --0,+5--> S0=(7,1817)`,
`Y --1,+5--> (5,252)`.

An exact same-state owner path

`8 --0000100,+14--> (5,252)`

implies, under `B(8)<=3`,

`B(Y) <= max(12, B(7,1817)-5)`.

Thus the live sufficient target became

`B(7,1817)<=17`.

The all-zero ray from `Y` has exact wall-deficit recurrence

`e_{n+1}=(e_n+1)/2` for odd `e_n`,
`e_{n+1}=3e_n/2` for even `e_n`,

starting at `e_1=243`. Exact iteration reaches

`Y 0^62 = V_41 = (41, K=3^41-3)`

at added area `1528`.

The D0 spine reaches the same `V_41` at cost `1558`, so Y arrives exactly 30 units cheaper. Native D0 ownership therefore gives only the normalized bound 33 where Y needs 12: an exact deficit of 21.

Classification: exact Bellman/cascade reduction and quantified barrier. Parent delta: LATERAL.

## 5. High-index A/F surplus route: exact saturation barrier

For the D0 departure families

`A_d=(d,K=(3^(d+1)-9)/2)`,
`F_d=(d-1,K=(3^d-3)/2)`,

with native D0 costs

`C_A(d)=d^2-2d-1`,
`C_F(d)=d^2-d-2`,

Y's 30-unit advantage at the common spine would require, for all relevant `d>=41`, bounds stronger than D0 by 21 units.

The natural boundary checkpoints are

`E_A(d)=(1,3*2^(2d-5))`,
`E_F(d)=(1,3*2^(2d-4))`.

Exact induction gives

`E_A(d) 0^(2d-4)=A_d` with added area `(d-2)^2`,

`E_F(d) 0^(2d-3)=F_d` with added area `(d-2)(d-1)`.

The credits saturate exactly:

`(2d-5)+(d-2)^2=C_A(d)`,
`(2d-4)+(d-2)(d-1)=C_F(d)`.

Therefore the natural high-index boundary ancestry has no hidden large-d surplus. Trying to obtain the needed 18-unit normalized improvement through these owners would require a Bellman value below the empty-future valuation of the boundary checkpoint itself.

This identifies the route with the already-known upstream reachability obstruction rather than bypassing it.

Classification: analytic structural barrier. Parent delta: HARDER.

This second consecutive non-improving Gate-A checkpoint triggered the mandatory pivot away from the local Gate-A attack.

## 6. Gate-B / global pivot and historical scope correction

The Gate-B re-audit recovered the correct parent obligation:

- branch-specific counterflow escalation, selector eliminations, and Radius-4/5 consumers are not exhaustive Gate-B closure;
- the live historical global candidates are balanced-return weighted difference and strict-excursion packing;
- any viable result must remain genuinely exhaustive and ownership-sensitive.

RL311 did not reactivate Radius 6+, fixed-depth grammar, H21, or the old doubled-word Radius-5 bridge.

## 7. Universal prefix-flow coordinate

For any rooted genuine cycle rotation, with prefix weights

`q_i=2^i 3^(-C_i)`

and physical state `x_i`, define

`U_i=q_i(4x_i+1)`.

Directly from either parity update,

`U_(i+1)=U_i+q_i`.

Hence

`U_i=4x_0+1+sum_(t<i) q_t`,

and over the whole cycle

`U_A=lambda(4x_0+1)`.

This identity is recurrence algebra and is not by itself an independent obstruction. Its value in RL311 is in combination with genuine physical extrema and owned block cuts.

## 8. Extremal control of gcd-block imbalance

Let

`A=ga`, `L=g ell`, `z=2^a/3^ell`, `z^g=lambda`,

and at canonical block cuts put

`E_j=K_j-j ell`.

At the minimum root, the `U` identity and `x_j<=M` give

`3^(E_j) < z^j Q_ext`,

where

`Q_ext=(4M+1)/(4R+1)`.

Let

`c=ceil(log_3 lambda)`,
`h=ceil(log_3 Q_ext)`.

Combined with the inherited least-state suffix lower bound, this yields for every proper gcd-block cut

`1-c <= E_j <= h+c-1`.

RL310's `lambda<M/R` implies `c<=h+1`, hence universally

`-h <= E_j <= 2h`.

In the one-sided sector `lambda<3`, `c=1`, so this sharpens to

`0 <= E_j <= h`.

Classification: analytic global splice. Parent delta: EASIER.

### Correction to unpromoted scratch

An earlier RL311 scratch inequality attempted to lower-bound the total normalized block-strip width by assigning a positive numerator contribution to every canonical block. RL206's correction requires strict positivity only for a block containing a `1`. Therefore that scratch strip-width lower bound is DEMOTED and is not part of the promoted RL311 result set.

## 9. Reduced global gap from the full prefix-flow mass

RL19 gives

`Z=sum_(i=0)^(A-1) q_i=(lambda-1)(4R+1)`.

The `g` canonical block-start terms alone give

`Z >= sum_(j=0)^(g-1) z^j 3^(-E_j)`.

Using the universal `E_j<=2h`,

`z-1 >= 1/[3^(2h)(4R+1)]`.

In the one-sided sector `lambda<3`, using `E_j<=h`,

`z-1 >= 1/[3^h(4R+1)]`.

Also `g|kappa_ext`, since

`kappa_ext=Ao-dL=g(ao-d ell)`.

These bounds constrain the old Gate-B arithmetic geometry but do not alone give contradiction.

Classification: analytic. Parent delta: EASIER as a parameter contraction, not closure.

## 10. Exact extremal determinant-density identity

Let

`Z_d=sum_(i=0)^(d-1) q_i`,
`theta=Z_d/Z`,
`rho=d/A`,
`delta=log_3 lambda`,
`Q_ext=(4M+1)/(4R+1)`.

At the physical maximum time `d`, the `U` identity gives exactly

`q_d Q_ext = 1 + theta(lambda-1)`.

Since `q_d=2^d/3^o`, one obtains

`kappa_ext/A`
` = log_3 Q_ext + rho delta - log_3(1+theta(lambda-1))`.

Equivalently, with

`Phi_lambda(theta)=ln(1+theta(lambda-1))/ln lambda`,

`kappa_ext/A`
` = log_3 Q_ext + log_3 lambda * (rho-Phi_lambda(theta))`.

Therefore

`log_3(Q_ext/lambda) < kappa_ext/A < log_3(lambda Q_ext)`.

In the one-sided sector `lambda<3`,

`h-2 < kappa_ext/A < h+1`.

Thus the determinant mass density is controlled by the same physical aspect-ratio scale `h`; `kappa_ext` is not an independent vertical scale.

Classification: exact analytic identity plus corollary. Parent delta: EASIER.

## 11. Pointwise contraction of the one-sided extremal profile

In the one-sided sector `lambda<3`, RL310 gives

`P_i=o-W_i(d)>=0`.

For the minimum-root word, monotonicity of `U` gives

`q_i > 1/Q_ext`

at every proper prefix.

For the same word rooted at the maximum,

`q_i^(M)=q_i 3^(P_i)`.

Using `U_i<U_A` and every physical state at least `R` gives

`q_i^(M) < lambda Q_ext`.

Hence

`3^(P_i) < lambda Q_ext^2`.

With `lambda<3` and `Q_ext<=3^h`,

`0 <= P_i <= 2h`.

Together with RL310's weighted identity,

`max P_i >= h`.

So the full one-sided profile obeys

`min P=0`,
`h <= max P <= 2h`,
`h-2 < (1/A) sum_i P_i < h+1`.

Classification: analytic. Parent delta: EASIER.

## 12. Full-resolution centered-discrepancy squeeze

Put

`alpha=log_3 2`,
`delta=A alpha-L=log_3 lambda`,
`T_i=C_i-iL/A`.

At the physical minimum, `U_i<U_A` and `x_i>=R` give `q_i<lambda`; hence

`T_i > -delta(1-i/A)`.

In particular, if `lambda<3`,

`T_i>-1` for every proper prefix.

Rotate the genuine cycle to its physical maximum. For every proper rotated prefix, monotonicity of `U` and the physical upper bound by `M` give `qhat_t>1`. Therefore its centered discrepancy satisfies

`That_t < t delta/A < delta`.

By cyclic transport of centered discrepancy and

`T_d=kappa_ext/A`,

one obtains, in the `lambda<3` sector,

`-1 < T_i < kappa_ext/A + 1`

for every phase.

At gcd-block cuts `T_(ja)=E_j`. The exact conclusion from this squeeze is

`0 <= E_j <= ceil(kappa_ext/A)`.

### Correction to checkpoint scratch

RL311 checkpoint scratch had stated the stronger bound

`E_j <= floor(kappa_ext/A)`.

That rounding step is not justified. It is explicitly CORRECTED here. No promoted consequence relies on it.

The stronger independent checkpoint-7 result

`0<=E_j<=h`

remains valid and is used below.

## 13. Short owned balanced-return extractor

In the `lambda<3` sector, the `g+1` canonical block levels

`E_0,E_1,...,E_g`

all lie in the `h+1` integer values `{0,1,...,h}`.

Therefore either

`g<=h+1`,

or among the first `h+2` block cuts there are two equal levels. Thus there exist

`0<=j<k<=g`,
`m=k-j`,

with

`1<=m<=h+1`,
`E_j=E_k`.

If `g>h+1`, this pair can be chosen proper (`m<g`).

Equality of levels means the segment from block cut `j` to `k` has exactly

`length=ma`,
`odd count=m ell`,

so it has the exact reduced global slope.

Because both endpoints are genuine rotations of the same primitive full-D cycle, the pair is genuinely owned at the global modulus; no local-prefix denominator ownership is asserted.

For endpoint states `x_j,x_k`, equal level gives

`q_(ka)/q_(ja)=z^m`.

Strict monotonicity of `U` gives

`1 < U_(ka)/U_(ja) < lambda`.

Therefore

`z^(-m) < (4x_k+1)/(4x_j+1) < lambda z^(-m)`.

For a proper return `m<g`, `1<z^m<lambda`, hence

`1/lambda < (4x_k+1)/(4x_j+1) < lambda < 3`.

This is the strongest RL311 global compression theorem.

Classification: analytic owned compression. Parent delta: EASIER.

## 14. Failed stronger mass-share inequality

RL311 tested the tempting claim that the physical `R->M` `+1` logarithmic mass is at least its proportional share of the whole-cycle mass, equivalently a stronger direct upper bound on `kappa_ext/A` by the physical aspect ratio.

Positive rational fixed-orbit counterexamples exist, so this is not a consequence of recurrence/extremal geometry alone. It is not promoted. Any revival would need a genuinely integer/full-D ownership-sensitive ingredient.

Classification: method barrier / negative control.

## 15. Frozen proof state and exact remaining obstruction

Promoted within RL311 scope:

1. complementary-branch skew/determinant amplification, retained as a frozen lower-bound tool;
2. exact Gate-A dependency contraction and Y/D0 quantitative barrier;
3. exact high-index A/F saturation barrier;
4. universal prefix-flow coordinate `U_i`;
5. universal gcd-block imbalance control, and `0<=E_j<=h` for `lambda<3`;
6. reduced-gap lower bound from full prefix-flow mass;
7. exact determinant-density identity;
8. pointwise one-sided profile bound `0<=P_i<=2h`;
9. full-resolution centered-discrepancy squeeze, with corrected rounding;
10. short owned balanced-return extractor:
   `g<=h+1` OR a proper equal-level balanced pair within at most `h+1` reduced blocks and physical ratio in `(1/lambda,lambda)`.

Explicitly NOT promoted:

- the demoted strip-width lower bound that assumed every block contains a `1`;
- `E_j<=floor(kappa_ext/A)`;
- the proposed extremal-arc above-average mass inequality;
- any proper-prefix ownership modulo a local denominator;
- any claim that large counterflow alone closes Gate B;
- any global Collatz/non-trivial-cycle exclusion.

Open:

- consume the short owned balanced-return pair with genuinely full-D information;
- or close the complementary survivor `g<=h+1` by an independent global argument;
- Gate A;
- Gate B;
- global positive non-trivial-cycle exclusion.

## 16. Successor direction

RL312 should not restart the frozen P/Q, H21, Radius6+, raw Gate-A Bellman, or finite Farey programmes.

Its parent-nearest target is now:

> **SHORT OWNED BALANCED-RETURN CONSUMER / CONTROLLED-MULTIPLICITY CLOSURE.**

Start from the exact RL311 dichotomy in the `lambda<3` sector:

`g<=h+1`

or a proper pair of genuine full-D owned rotations at equal gcd-block level separated by at most `h+1` reduced blocks, with

`1/lambda < (4x_k+1)/(4x_j+1) < lambda < 3`.

The first priority is to find an independent full-D / quotient / weighted-difference consumer for that pair that does not collapse to RL206 recurrence compatibility or the RL20 block coboundary.

Any result must be audited for exhaustiveness and must not infer local denominator ownership from global ownership.

If two meaningful RL312 checkpoints remain LATERAL/HARDER, freeze this route and step back to the universal parent obstruction rather than grinding the balanced-pair grammar.

## 17. Verification / transport

RL311 contains analytic proofs/reductions rather than a new large finite certificate. `verify_rl311_closeout.py` is a portable sanity/regression verifier for the load-bearing algebraic identities, rounding correction, profile/block-level combinatorics, and Bellman-path replays stated above. It is supplementary to the analytic proofs.

The repository paths in `sessions/RL311/` plus `SHA256SUMS.txt` are the documented lossless transport for this connector-worker transition. No ZIP bundle is required for this generation. Knowledge catalogues are `stale/deferred` and are not part of the mathematical authority boundary.
