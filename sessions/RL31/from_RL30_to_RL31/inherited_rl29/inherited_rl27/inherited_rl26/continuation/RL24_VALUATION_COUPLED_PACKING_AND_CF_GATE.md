# RL24 — valuation-coupled high-run packing improves the RL23 global factor

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** for `R>=160`. Section 6 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This note couples the RL23 high-run product partition to the exact global valuation identity

`A = sum_(odd phases x) nu(x)`.

The point is that the unique RL23 product extremizer, the type-II two-low block with no extra high state, is valuation-expensive: its five odd states consume at least eight powers of `2`.  The rest of the cycle cannot consist arbitrarily densely of such blocks because all other extended blocks still have a definite valuation floor.  This converts the local saturation witness into a genuine global packing gain.

## 1. Recall the RL23 partition and its exceptional block

Use the odd-state induced map

`x -> (3x+1)/2^nu`,

and put

`F(x)=1+1/(3x)`.

RL23 partitions the odd cycle into extended maximal low-chain/high-run blocks.  Its global target factor is defined by

`T(R)=256R/(256R-319)`,

so the old theorem is

`lambda <= T(R)^(L/5)`.

The only seed attaining the target mean is the type-II `k=2`, `m=0` block.  Call such a block **exceptional**.  It contains five odd states.

The chain transition valuations inside an exceptional block are

`1,2,1,2`,

through the first four odd states, and its terminal high state must use valuation at least `2` to reach the next low state.  Hence every exceptional block has total outgoing valuation at least

> **`8` on its `5` odd states.**                                      (R24V.1)

The RL23 exact saturation family realizes equality `8`.

## 2. A global `4/3` valuation floor for every extended block

Consider any extended block.  Let its low chain have `k in {1,2,3}` low states, and let the following high run contain

`h=m+1 >=1`

high odd states `h_0,...,h_(h-1)` before the next low odd state `ell`.

Let `V_H` be the sum of the outgoing odd-map valuations on these `h` high states.  The exact odd-segment product identity is

`prod_(i=0)^(h-1) F(h_i)`
` = 2^(V_H) ell / [3^h h_0]`.                              (R24V.2)

Every factor on the left is `>1`.  Also `h_0` is high while `ell` is low, so `ell<h_0`.  Therefore

`2^(V_H) > 3^h`.                                           (R24V.3)

A convenient integer consequence is

> **`V_H >= ceil((4h+2)/3)`.**                             (R24V.4)

Indeed, writing `h=3q+r`, `r=0,1,2`, the contrary upper exponents reduce respectively to

`2^(4q) < 3^(3q)`,

`2^(4q+1) < 3^(3q+1)`,

`2^(4q+3) < 3^(3q+2)`,

which follow from `16<27`, `2<3`, and `8<9`.

Before the high run begins, the stripped low-chain part has outgoing valuation

- type I: `3k-1`;
- type II: `3k`.

The full extended block has `n=2k+h` odd states.  Thus for type I,

`V >= 3k-1 + (4h+2)/3`
`  = (9k+4h-1)/3`
` >= (8k+4h)/3 = 4n/3`,                                   (R24V.5)

because `k>=1`.  Type II is stronger by an additional unit.

Hence every extended block satisfies

> **`V_block >= (4/3) n_block`.**                          (R24V.6)

This is a blockwise statement; summing all outgoing valuations over the partition gives exactly the global exponent `A`.

## 3. A strictly better product factor for every nonexceptional block

Retain the RL23 notation

`F_H=4R/(4R-1)`,

`P_HH=16R/(16R-7)`.

For the stripped type-I `k=1` core,

`Q_I1=(9R+5)/(9R)`.

Define the five-state comparison product

`S_5(R) = Q_I1 * P_HH * F_H`

so explicitly

> **`S_5(R)=64R(9R+5)/[9(4R-1)(16R-7)]`.**                 (R24V.7)

Its per-state asymptotic coefficient is

`(1/5) lim_(R->infty) R(S_5-1)`
` = 179/720`
` = 0.248611111...`.                                       (R24V.8)

The verifier clears denominators and proves for every `R>=160`:

1. every RL23 core except type-II `k=2,m=0` has product `P` and length `n` satisfying
   `P^5 <= S_5^n`;
2. every `m=1` and `m=2` high-run seed, including those built from the type-II `k=2` stripped core, satisfies the same comparison;
3. `P_HH^5 <= S_5^2`, so appending arbitrarily many paired high states preserves the comparison.

The type-I `k=1,m=2` seed is the defining equality case.  Consequently every **nonexceptional** extended block obeys

> **`P_block <= S_5(R)^(n_block/5)`.**                     (R24V.9)

The exceptional block retains the sharper exact bound

`P_exc <= T(R)`.                                           (R24V.10)

Moreover `T(R)>S_5(R)` for `R>=160`.

## 4. Count the exceptional blocks using the global valuation sum

Let `N` be the number of exceptional five-state blocks.  They contribute at least `8N` to `A`.  By (R24V.6), the remaining `L-5N` odd states contribute at least `(4/3)(L-5N)`.  Therefore

`A >= 8N + (4/3)(L-5N)`
`  = 4L/3 + 4N/3`.                                        (R24V.11)

Hence

> **`N <= (3A-4L)/4`.**                                    (R24V.12)

This is the new global coupling.  The local RL23 extremizer can occur, but its valuation cost prevents it from filling the whole cycle.

## 5. New global logarithmic bound

Put

`K(R)=T(R)/S_5(R)>1`.

Multiplying (R24V.9)--(R24V.10) over the block partition and using (R24V.12),

`lambda`
` <= S_5^(L/5) K^N`
` <= S_5^(L/5) K^((3A-4L)/4)`.                             (R24V.13)

Write

`beta=log(3)/log(2)`.

Since

`A = beta L + log(lambda)/log(2)`,                         (R24V.14)

letting `s=log S_5`, `k=log K` and rearranging (R24V.13) gives the exact self-consistent estimate

> **`log(lambda)/L <= C_exact(R)`,**                       (R24V.15)

where

`C_exact(R)`
` = [ s/5 + (3 beta-4) k/4 ]`
`   / [ 1 - 3k/(4 log 2) ]`.                               (R24V.16)

For a simple rational monotone majorant, use

`beta < 317/200`,                                           (R24V.17)

which is the exact integer comparison `3^200<2^317`, together with

`log u <= u-1` for `u>1`, and `log 2>2/3`.

Then

`C_exact(R) <= C_bar(R)`,                                  (R24V.18)

with

`C_bar(R)`
` = [ (S_5-1)/5 + (151/800)(K-1) ]`
`   / [ 1 - (9/8)(K-1) ]`.

Exact simplification gives

`C_bar(R)`
` = [264555072 R^3 - 45263180 R^2 - 277062541 R + 33648111]`
`   / [900(4R-1)(16R-7)(18432R^2-12791R-29383)]`.          (R24V.19)

The verifier proves by exact polynomial positivity that `C_bar(R)` is strictly decreasing for `R>=160`.

Its asymptotic coefficient is

> **`lim_(R->infty) R C_bar(R) = 51033/204800`
> `=0.2491845703125 < 319/1280`.**                         (R24V.20)

The exact self-consistent coefficient in (R24V.16) is slightly better asymptotically,

`0.249184484864...`,

but (R24V.19) is a convenient fully rational global theorem.

Thus RL23's `319/1280=0.24921875` is not globally saturable once the valuation budget is imposed.

## 6. Continued-fraction consequence under the inherited floor

Under the inherited external input

`R>=R0=2^71`,

monotonicity of `C_bar` gives

`log(lambda)/L <= C_bar(R0)`.

For the reduced pair

`p=A/g`, `q=L/g`, `g=gcd(A,L)`,

`0 < p/q-beta <= C_bar(R0)/log 2`.                          (R24V.21)

The exact verifier uses rigorous rational intervals for `log2` and `log3`, applies Legendre's criterion, and checks every above-`beta` convergent in the resulting window.  It proves

> **`q=L/gcd(A,L) >= 57,306,252,005`.**                    (R24V.22)

This improves the RL23 floor

`57,302,322,170`

by

`3,929,835`.

The next relevant continued-fraction denominator remains

`65,470,613,321`,

so this is a real analytic/global gain but not a qualitative CF-threshold crossing.

## 7. Strategic consequence

The exact RL23 local saturation witness did not kill Track A; instead it identified the missing global variable.  The valuation sum is already enough to prove that the saturating core cannot dominate arbitrarily.

The present two-class argument is deliberately coarse: all nonexceptional blocks are compressed to the single factor `S_5` and the single valuation floor `4/3`.  A sharper supporting-line/linear-programming treatment of `(product coefficient, valuation density)` across the finite seed family should improve the constant again, though the RL23 local dynamical barrier still indicates that Track A alone is unlikely to reach the next qualitative CF gate.

Verifier: `verify_rl24_valuation_coupled_packing.py`.
