# RL42 — moved-rank sparse bridge and first concentration exclusion

Date: 2026-08-22

## Status

Sections 1--5 are **ANALYTIC** in the inherited order-2 / `g=2` balanced-return setup.  The accompanying verifier is an **EXACT FINITE sanity certificate** over all equal-weight binary word pairs through length 10; it is not a substitute for the analytic proof.

This note does **not** close RL or the full `g=2` branch.  It strengthens the RL36 packing-or-sparse interface in exactly the direction required by the RL40 concentration barrier: sparsity is controlled by the number of *displaced odd ranks / excursion-owned odd states*, not by the transport area `rho`.  Hence a very long displacement absorbed by only a few odd states is automatically a genuinely low-support exponential relation.

## 1. Ordered-rank formula for the affine numerator

Retain the half-balanced notation

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`,

with equal-weight half words `u,v` of length `a` and weight `ell`.  Write their ordered odd positions as

`i_1<...<i_ell` in `u`,

`j_1<...<j_ell` in `v`.

For any length-`a`, weight-`ell` word `w` with ordered odd positions `r_1<...<r_ell`, the standard affine numerator is exactly

> **`Q(w)=sum_(m=1)^ell 3^(ell-m) 2^(r_m)`.**              (R42.1)

Therefore

> **`U-V = sum_(m=1)^ell 3^(ell-m)(2^(i_m)-2^(j_m))`.**    (R42.2)

Let

`D_rank={m: i_m != j_m}`,

and put

> **`P_rank=|D_rank|`.**                                   (R42.3)

All ranks outside `D_rank` cancel term-by-term in (R42.2), giving

> **`U-V = sum_(m in D_rank) 3^(ell-m)(2^(i_m)-2^(j_m))`.** (R42.4)

After expanding each difference, this is a signed `2`--`3` relation with at most `2P_rank` monomials before collection.

Combining with the exact proper-factor identity `U-V=(X+Y)G` gives

> **`(X+Y)G = sum_(m in D_rank) 3^(ell-m)(2^(i_m)-2^(j_m))`,** (R42.5)
>
> with support cardinality at most **`2P_rank`**.           (R42.6)

This is strictly stronger than RL36.24 when a small number of odd ranks move a long distance.

## 2. Displaced ranks are exactly excursion-owned odd mass

Let

`d_j=p_v(j)-p_u(j)`

be the aligned prefix-count difference, and decompose the nonzero set of `d_j` into maximal excursions.  If excursion `E` has common local odd weight `p_E`, RL36 denotes

`P=sum_E p_E`.

Then

> **`P_rank=P`.**                                          (R42.7)

Proof.  Suppose rank `m` is fixed: `i_m=j_m=t`.  Immediately before column `t`, each word has exactly `m-1` odd bits, hence `d_t=0`.  Thus a fixed rank lies in a synchronized column and cannot belong to the odd mass of a maximal excursion.

Conversely, let a maximal excursion start at a synchronized prefix count `c` and end at count `c+p_E`.  Its local odd ranks are exactly `c+1,...,c+p_E`.  If one of these ranks had `i_m=j_m`, then at that common odd column both prefixes would contain exactly `m-1` previous odd bits, so `d=0` at an interior excursion column, contradicting maximality.  Hence all `p_E` local ranks are displaced.  Summing over disjoint excursions proves (R42.7).

Consequently the exact gap-factor relation is supported on at most

> **`2P` monomials, where `P` is also the number of distinct excursion-owned leading odd states.** (R42.8)

This aligns the algebraic and packing sides on one and the same parameter.

## 3. Transport is displacement size, not support size

RL36 already gives

`rho=sum_(m=1)^ell |i_m-j_m|`.

Using `D_rank`, this is simply

> **`rho=sum_(m in D_rank)|i_m-j_m|`.**                    (R42.9)

Thus

`P<=rho`,

but there is no converse bound of the form `rho=O(P)`: one rank can move arbitrarily far at the level of word combinatorics.

The new point is that this extreme RL40 concentration pattern is no longer invisible.  If `rho` is huge because only a few ranks move very far, (R42.5) remains low-support.  If many ranks move, RL36 owns exactly that many distinct high odd states.

So the natural two-regime parameter is **`P`**, not raw `rho`:

- `P=o(L)`  => an `o(L)`-support exact `2`--`3` proper-factor relation, even if `rho` is large;
- `P=Omega(L)` => a positive density of distinct excursion-owned high odd states, directly defeating the one-sacrificial-state interpretation of RL40.

A future sparse-uniqueness theorem should therefore target (R42.5) as a function of `P`.

## 4. The maximally concentrated case `P=1` is impossible

Assume now an actual surviving near-minimum `g=2` balanced return, so the inherited facts include

`U-V=(X+Y)G`,

`4|G`,

and RL36.17: every common terminal suffix of odd weight `q` satisfies `q<=v3(G)`.

Suppose `P=1`.  Then there is one displaced rank, say `m`, and (R42.4) becomes

`(X+Y)G = 3^q (2^i-2^j)`,

where

`q=ell-m`.

Because every later rank is fixed, the suffix after `max(i,j)` is common and contains exactly `q` odd bits.  RL36.17 therefore gives

`3^q | G`.                                                 (R42.10)

On the other hand `max(i,j)<=a-1`, so

`|2^i-2^j| < 2^(a-1)`.

Since `X+Y>2^a`, taking absolute values in the factor equation gives

`G < 3^q/2`.                                               (R42.11)

But (R42.10) and `G>0` imply `G>=3^q`, contradicting (R42.11).

Hence

> **every genuine surviving `g=2` balanced return has `P>=2`.** (R42.12)

This is a scalable analytic exclusion of the literal one-state moved-rank concentration pattern; it is independent of the finite `rho>=28` computation.

## 5. Stronger one-excursion floor: `p>=3`

Suppose there is exactly one maximal excursion and its common odd weight is `p`.  Then its `p` displaced ranks are consecutive in rank number.  Let `q` be the common terminal suffix odd weight.  Factoring `3^q` from (R42.4), and using `|2^i-2^j|<2^(a-1)` termwise, gives

`(X+Y)G`
` < 3^q 2^(a-1) (1+3+...+3^(p-1))`
` = 3^q 2^(a-1) (3^p-1)/2`.

Since `X+Y>2^a`,

> **`G/3^q < (3^p-1)/4`.**                                (R42.13)

The terminal suffix has weight `q`, so `3^q|G`.  Because `4|G` and `3^q` is odd,

`G/3^q` is a positive multiple of `4`.

For `p=1`, the right side of (R42.13) is `1/2`; for `p=2` it is `2`.  Both are below the smallest possible positive value `4` of `G/3^q`.  Therefore

> **every one-excursion genuine return has `p>=3`.**        (R42.14)

This is weaker than the low-area RL40/RL41 floors, but unlike those floors it is uniform in transport distance and exposes the proper-factor mechanism directly.

## 6. Why this matters for the RL38/RL39 concentration barrier

RL40 showed that the RL39 charge variable can be made arbitrarily large on one sacrificial high state if one forgets the exact word/numerator geometry.  R42.7--R42.8 restore that geometry:

- a small number of excursion-owned states means a small number of displaced ordered odd ranks;
- those ranks give a low-support exact equation for the full relative proper factor `X+Y`;
- a large number of displaced ranks means many distinct owned high odd states before any RL39 charge optimization is performed.

Thus the relevant concentration dichotomy is now

> **few moved ranks => sparse proper-factor arithmetic; many moved ranks => genuine state spread.** (R42.15)

This is stronger and better aligned than the earlier `rho=o(L)` versus `rho=Omega(L)` split, because it catches the dangerous regime `rho` large but concentrated into a few very long displacements.

## 7. Next theorem target

The highest-value continuation is to quantify one of the two sides of (R42.15):

1. **Sparse side.** Prove that (R42.5) has no surviving near-resonant solution when `P=o(L)` (or first for fixed `P=2,3,...`).  Endpoint `2`- and `3`-adic ownership should be built into the normalization, not added afterward.
2. **Spread side.** Reinsert the `P` distinct RL36 high odd states into the strongest global correction-product supporting line and determine the density `P/L` needed to cross the next CF gate.
3. **Overlap.** Seek a threshold `eta` for which sparse arithmetic excludes `P<eta L` while product packing excludes `P>=eta L`.

The finite area-26/27 reconstruction remains required before `rho>=28` is called artifact-audited, but it is logically independent of this new scalable bridge.
