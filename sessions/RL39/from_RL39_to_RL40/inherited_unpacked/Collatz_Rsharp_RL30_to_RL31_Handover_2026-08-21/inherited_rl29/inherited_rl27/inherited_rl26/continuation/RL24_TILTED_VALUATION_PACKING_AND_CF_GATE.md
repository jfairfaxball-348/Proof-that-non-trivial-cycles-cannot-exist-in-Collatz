# RL24 — tilted valuation packing: a stronger global coefficient from the exact valuation budget

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** for `R>=160`. Section 6 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This strengthens `RL24_VALUATION_COUPLED_PACKING_AND_CF_GATE.md`.  The coarse two-class count is correct, but it throws away the actual valuation density of each nonexceptional block.  A supporting-line inequality across the RL23 extended-block family retains that information and gives a better global coefficient.

## 1. Two exact comparison factors

Keep the RL23 notation

`F_H=4R/(4R-1)`,

`P_HH=16R/(16R-7)`,

and the exceptional type-II `k=2,m=0` product

`T(R)=256R/(256R-319)`.                                    (R24T.1)

Define

`S_5(R)`
` = [(9R+5)/(9R)] * P_HH * F_H`
` = 64R(9R+5)/[9(4R-1)(16R-7)].                           (R24T.2)

This is exactly the RL23 product bound for the type-I `k=1,m=2` extended seed, which has five odd states.

Finally put

`K(R)=T(R)/S_5(R)`
` = 36(4R-1)(16R-7)/[(9R+5)(256R-319)]`.                  (R24T.3)

For `R>=160`, `K(R)>1`.

The two five-state anchor points are:

- type-I `k=1,m=2`: product `S_5`, valuation sum at least `7`;
- type-II `k=2,m=0`: product `T=S_5 K`, valuation sum at least `8`.

This suggests pricing one extra unit of valuation by the multiplicative factor `K`.

## 2. High-run valuation floor

Let an extended block have a low chain of length `k in {1,2,3}` followed by a high run of `h=m+1>=1` high odd states before the next low state.

If `V_H` is the outgoing valuation sum on those `h` high states, the exact odd-segment identity gives

`prod F(h_i)=2^(V_H) ell/[3^h h_0] >1`,                    (R24T.4)

with `ell<h_0`. Hence

`2^(V_H)>3^h`.                                              (R24T.5)

As in the coarse RL24 note, this implies the useful periodic lower bound

> **`V_H >= ceil((4h+2)/3)`.**                             (R24T.6)

The valuation sum before the high run is

- type I: `3k-1`;
- type II: `3k`.

Therefore define the certified lower valuation

`V_*(I,k,h)=3k-1+ceil((4h+2)/3)`,

`V_*(II,k,h)=3k+ceil((4h+2)/3)`.                           (R24T.7)

Every actual block valuation `V` satisfies `V>=V_*`.

## 3. The tilted local inequality

Let `P` be the product of `F` over an extended block, `n` its number of odd states, and `V` its actual outgoing valuation sum.

The new local theorem is

> **`P^5 <= S_5(R)^n K(R)^(5V-7n)`.**                     (R24T.8)

Because `K>1`, it suffices to prove this with `V=V_*`.

### Finite reduction

For `h=1`, use the six exact RL22/RL23 core products.

For `h>=2`, with stripped core `Q`, the RL23 high-run bound is

`P <= Q P_HH^(h/2)` if `h` is even,

`P <= Q P_HH^((h-1)/2) F_H` if `h` is odd.                 (R24T.9)

The lower valuation (R24T.7) satisfies

`V_*(h+6)=V_*(h)+8`,                                       (R24T.10)

while `n(h+6)=n(h)+6`.  Hence the exponent

`E=5V_*-7n`

changes by

`E(h+6)=E(h)-2`.                                           (R24T.11)

The high-run product bound acquires exactly three extra `P_HH` factors.  Thus it is enough to check the six residue classes `h=1,...,6` for each of the six chain types, together with the single extension inequality

> **`P_HH^15 K^2 <= S_5^6`.**                              (R24T.12)

The bundled verifier clears positive denominators, substitutes `R=t+160`, and checks nonnegative polynomial coefficients for all 36 seed inequalities and (R24T.12).

The two intended anchor equalities are reflected by the supporting line: the type-I `k=1,m=2` product is `S_5`, while the exceptional type-II `k=2,m=0` product is `S_5K`.

## 4. Sum the tilted inequality over the whole cycle

The extended blocks partition all `L` odd states, and their outgoing valuation sums partition the exact global sum `A`.

Multiplying (R24T.8) over all blocks gives

`lambda^5 <= S_5^L K^(5A-7L)`.                             (R24T.13)

Taking logs and writing

`beta=log3/log2`,

`A = beta L + log(lambda)/log2`,                            (R24T.14)

we obtain

`log(lambda)`
` <= (L/5) log S_5 + (A-7L/5) log K`.

Therefore

> **`log(lambda)/L <= C_tilt,exact(R)`,**                  (R24T.15)

where

`C_tilt,exact(R)`
` = [ (log S_5)/5 + (beta-7/5) log K ]`
`   / [ 1 - (log K)/(log2) ]`.                             (R24T.16)

This is the valuation-supporting-line analogue of the coarse two-class estimate.

## 5. Rational monotone majorant and asymptotic coefficient

Use the exact integer comparison

`3^200<2^317`,

so

`beta<317/200`

and hence

`beta-7/5 <37/200`.                                        (R24T.17)

Also use `log u<=u-1` and `log2>2/3`.  Then

`C_tilt,exact(R) <= C_tilt(R)`,                            (R24T.18)

where

`C_tilt(R)`
` = [ (S_5-1)/5 + (37/200)(K-1) ]`
`   / [ 1 - (3/2)(K-1) ]`.                                 (R24T.19)

Exact simplification gives

`C_tilt(R)`
` = [66135744 R^3 - 12111620 R^2 - 68717407 R + 8324757]`
`   / [900(4R-1)(16R-7)(4608R^2-3203R-8731)]`.             (R24T.20)

The verifier proves that this rational function is strictly decreasing for every `R>=160`.

Its asymptotic coefficient is

> **`lim_(R->infty) R C_tilt(R)`
> ` = 38273/153600`
> ` = 0.249173177083333...`.**                             (R24T.21)

The exact logarithmic supporting-line coefficient is slightly smaller,

`0.249173063153...`.

For comparison:

- RL22 terminal-high: `1/4 =0.25`;
- RL23 high-run: `319/1280 =0.24921875`;
- coarse RL24 valuation count: `51033/204800 =0.2491845703125`;
- tilted RL24: `38273/153600 =0.2491731770833...`.

Thus the exact global valuation budget gives a second strict improvement beyond the local RL23 saturation factor.

## 6. Continued-fraction gate under the inherited external floor

Under the inherited external computational input

`R>=R0=2^71`,

monotonicity gives

`log(lambda)/L <= C_tilt(R0)`.                              (R24T.22)

For

`g=gcd(A,L)`, `p=A/g`, `q=L/g`,

`0<p/q-beta <= C_tilt(R0)/log2`.                            (R24T.23)

The exact verifier uses rigorous rational intervals for `log2,log3`, applies Legendre's criterion, and checks all above-`beta` convergents in the certified window.  It proves

> **`L/gcd(A,L) >= 57,307,562,130`.**                      (R24T.24)

This improves

- RL23: `57,302,322,170`, by `5,239,960`;
- the coarse RL24 count: `57,306,252,005`, by another `1,310,125`.

The next relevant continued-fraction denominator is still

`65,470,613,321`.

## 7. Strategic consequence

This is close to the natural endpoint of the present finite-block valuation coupling.  The supporting line is already anchored by two concrete five-state patterns, so further Track-A gains from the same partition will require either

1. a stronger high-run valuation lower bound than (R24T.6) that uses actual height/return information;
2. an exclusion or frequency restriction on one of the two supporting anchor patterns; or
3. a larger global variable than total valuation, such as blockwise valuation variance or root/final-return ownership.

The improvement is real but still far from the `~0.1909` coefficient scale needed to cross the next qualitative CF denominator solely by local/valuation packing.

Verifier: `verify_rl24_tilted_valuation_packing.py`.
