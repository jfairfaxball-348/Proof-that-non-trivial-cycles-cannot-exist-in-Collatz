# RL42 — prefix-cap bound: the physical gap is paid linearly by moved odd mass

Date: 2026-08-22

## Status

**ANALYTIC** in the inherited near-resonant order-2 / `g=2` balanced-return branch.  The companion verifier checks the exact ordered-rank identities on the retained RL21 proper-factor countermodel and finite word-pair sanity data.

This note strengthens `RL42_MOVED_RANK_SPARSE_BRIDGE.md`.  It gives a uniform analytic lower bound on the number of positively displaced odd ranks, hence on the number of distinct excursion-owned high odd states.  Unlike the RL41 finite area search, it is independent of `rho` cutoffs.

## 1. Setup and orientation

Retain

`X=2^a`, `Y=3^ell`, `z=X/Y>1`, `lambda=z^2<16/15`,

with least state `R`, balanced half-state `x=R+G`, and equal-weight half words `u,v`.

Let

`i_1<...<i_ell`, `j_1<...<j_ell`

be their ordered odd positions.  From RL42.5,

`(X+Y)G = sum_m 3^(ell-m)(2^(i_m)-2^(j_m))`.

Call rank `m` **positive** when `i_m>j_m`.  These are exactly the odd ranks belonging to positive prefix-count excursions (`d=p_v-p_u>0`).  Let their number be `P_+`.

Negative ranks have `i_m<j_m` and contribute negatively to `U-V`; fixed ranks contribute zero.  Since `G>0`,

> **`(X+Y)G <= sum_(i_m>j_m) 3^(ell-m)(2^(i_m)-2^(j_m))`.** (R42G.1)

## 2. A displaced lagging odd position has scale at most `z^2`

Fix a positive rank `m`, so `j_m<i_m`.  At column `i_m`, the `u` trajectory is about to take its `m`-th odd step, hence

`p_u(i_m)=m-1`.

Because the `v` trajectory has already taken its `m`-th odd step, the prefix-count imbalance

`d=p_v(i_m)-p_u(i_m)`

satisfies `d>=1`.

Write

`q_u=2^(i_m)/3^(m-1)`,

`q_v=q_u 3^(-d)`.

RL36.5 gives

`q_v v_(i_m) <= zR`,

while RL36.6 gives

`v_(i_m) >= 3^d R/z`.

Therefore

`q_v <= z^2/3^d`,

and multiplying by `3^d` gives the key rank cap

> **`2^(i_m)/3^(m-1) = q_u <= z^2`.**                     (R42G.2)

Hence every positive moved-rank term obeys

`3^(ell-m)(2^(i_m)-2^(j_m))`
` < 3^(ell-m) 2^(i_m)`
` <= z^2 3^(ell-1)`
` = z^2 Y/3`.                                               (R42G.3)

This is the crucial normalization: every positive moved rank contributes only `O(Y)`, uniformly in its displacement distance.

## 3. Linear gap-to-moved-mass theorem

Since `X+Y=(z+1)Y`, (R42G.1)--(R42G.3) give

`(z+1)YG < P_+ z^2 Y/3`.

Cancel `Y`:

> **`P_+ > 3(z+1)G/z^2`.**                                (R42G.4)

Using only

`z+1>2`,

`z^2<16/15`,

we obtain the completely rational uniform consequence

> **`P_+ > (45/8) G`.**                                   (R42G.5)

The inherited near-minimum integer ownership gives `4|G`.  Therefore

> **`P_+ >= 23`.**                                         (R42G.6)

In particular, since `P>=P_+` and every moved rank travels at least one column,

> **`P>=23` and `rho>=23`.**                               (R42G.7)

This does not supersede the RL41 working finite checkpoint `rho>=28`, but it is a new cutoff-free analytic theorem and is directly expressed in the concentration parameter `P`.

## 4. The near-minimum physical gap is at most linear in odd mass

Rearranging (R42G.5),

> **`G < (8/45) P_+ <= (8/45) P <= (8/45) ell`.**          (R42G.8)

Thus the balanced near-minimum state gap is not merely `G<R/15`; in the surviving `g=2` branch it is bounded linearly by the number of displaced odd ranks, and hence by the half-block odd count.

This removes a large endpoint-valuation loophole in RL36.18.  Indeed

`v2(G) <= log_2 G`,

`v3(G) <= log_3 G`,

so for `G>=4`,

> `v2(G)+v3(G)`
> `< log_2(8P/45)+log_3(8P/45)`                            (R42G.9)

(with the obvious integer-floor interpretation when desired).

Combining with RL36.18,

`P+C >= ell-v2(G)-v3(G)`,

gives the scalable endpoint-loss estimate

> **`P+C >= ell-O(log P)`.**                               (R42G.10)

More explicitly one may use

`P+C >= ell-floor(log_2(8P/45))-floor(log_3(8P/45))`

whenever the logarithm arguments are at least one; small `P` is already excluded by (R42G.6).

Hence if `P=o(ell)`, then all but `o(ell)` of the half-block odd mass lies in synchronized interior anchors.  At the same time RL42.5 has support at most `2P=o(L)`.  The sparse and synchronized-anchor descriptions now coincide on the same regime.

## 5. Interaction with the RL40 concentration barrier

RL40's abstract extremizer allowed one state to absorb arbitrarily large charge by becoming arbitrarily high.  The exact order-2 word geometry now imposes two independent restrictions on that picture:

1. there are at least `23` positively displaced ranks / distinct positive-excursion owned odd states, regardless of how transport distance is concentrated;
2. if the number `P` of such moved ranks is sublinear, the full `X+Y` proper-factor equation is itself sublinear-support, while the endpoint common-prefix/suffix loss is only logarithmic in `P`.

The remaining scalable closure target is therefore sharper than the RL41 kickoff formulation:

> **Sparse-or-dense moved-rank target.** Exclude `P=o(L)` through the exact proper-factor relation RL42.5, and derive a correction-product saving for `P>=eta L`.  The dangerous large-`rho`, few-state concentration regime now belongs entirely to the sparse side.

## 6. Evidence discipline

- RL remains open.
- The `g=2` branch remains open.
- `rho>=28` remains a working RL41 finite checkpoint pending reconstruction of areas 26--27.
- R42G.4--R42G.10 are analytic consequences of inherited RL36 scaled-state windows, the exact rank formula, `z^2<16/15`, and `4|G`.

## 7. Immediate low-transport simplification

Because every moved rank contributes at least one unit to transport,

`P_+ <= P <= rho`.

Combining this with (R42G.5) yields the uniform analytic gap-area floor

> **`rho > (45/8) G`.**                                   (R42G.11)

Since `4|G`, this has useful exact consequences:

- if `rho<=45`, then `G=4`;
- if `rho<=67`, then `G` is only `4` or `8`;
- a branch with `G>=8` requires `rho>=46`;
- a branch with `G>=12` requires `rho>=68`.

Thus every RL41 finite search through area 27 may be reconstructed with **`G=4` only**.  The earlier `G=8` / `G=12` zero-path computations are now logically redundant in that range.

For `G=4`, the exact form (R42G.4) is

> **`P_+ > 12(z+1)/z^2`.**                                (R42G.12)

At the two low-area resonances already isolated in RL41,

`z=2^46/3^29` and `z=2^65/3^41`,

exact rational arithmetic gives

`12(z+1)/z^2 > 23`

in both cases.  Hence

> **at either `(46,29)` or `(65,41)`, `P_+>=24`.**         (R42G.13)

In particular, the abstract area-23 `(46,29)` configurations reported in RL41 cannot be genuine integer-cycle configurations even before the absolute numerator-residue check: `P_+<=rho=23` contradicts (R42G.13).

This does not replace the retained RL41 area-24--27 congruence work, but it removes one entire frontier and sharply reduces the reconstruction search space.
