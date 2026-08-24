# RL24 — type-I high-start ownership sharpens the valuation supporting line

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** for `R>=161`. Section 6 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This supersedes the numerical constant in the earlier RL24 tilted-valuation note.  The key repair is that the first high state after a type-I low-chain core is not an arbitrary threshold-high state: its exact trajectory formula places it much higher.  The generic RL23 high/high bound was therefore unnecessarily weak on precisely the nonexceptional seed that supported the previous tilted line.

## 1. Type-I terminal highs start above `9R/4`

For a low chain starting at `x_0>=R`, write

`f(x)=(9x+5)/8`.

RL22's type-I terminal high is

`h_0=2 f^k(x_0)`, `k=1,2,3`.                               (R24H.1)

Since `f` is increasing and `k>=1`,

> **`h_0 >= (9R+5)/4`.**                                   (R24H.2)

This is much stronger than the generic high threshold

`H=(4R-1)/3`.

## 2. Improved first high/high pair bound for type I

Let `a,b` be consecutive high odd states with

`a>=A_0:=(9R+5)/4`,

and `b=(3a+1)/2^nu >=H`.

RL23 proved the exact identity

`F(a)F(b)=1+(2^nu+3)/(9a)`.                                (R24H.3)

For `nu=1,2`, the lower bound `a>=A_0` applies directly, and the worse case is `nu=2`:

`F(a)F(b) <= 1+28/[9(9R+5)]`.                              (R24H.4)

For `nu>=3`, the condition `b>=H` gives

`a >= (2^nu H-1)/3`.

The resulting excess

`(2^nu+3)/[2^nu(4R-1)-3]`

is decreasing in `2^nu`, so its maximum occurs at `nu=3`, where it is

`11/(32R-11)`.                                              (R24H.5)

For `R>=161`, exact cross multiplication gives

`11/(32R-11) <= 28/(81R+45)`.                              (R24H.6)

Therefore every first type-I high/high pair satisfies

> **`F(a)F(b) <= P_I := (81R+73)/(81R+45)`.**              (R24H.7)

Its two-state asymptotic excess is `28/81`, compared with the generic RL23 pair excess `7/16`; this is the structural gain.

For type-II chains the terminal high can genuinely approach the generic threshold, so the RL23 bound

`P_HH=16R/(16R-7)`                                         (R24H.8)

is retained.

## 3. Re-optimize the valuation supporting line

Let

`C(R)=(27R+19)/(27R)`                                      (R24H.9)

be the type-I `k=1,m=0` three-state core product, and retain

`T(R)=256R/(256R-319)`                                     (R24H.10)

for the exceptional type-II `k=2,m=0` five-state core.

The corresponding certified valuation sums are

- `C`: `n=3`, `V>=4`;
- `T`: `n=5`, `V>=8`.

Define

`J(R)=T(R)^3/C(R)^5`.                                      (R24H.11)

For `R>=161`, `J(R)>1`.

The supporting line through these two anchors is the following local theorem.  For every extended RL23 block with product `P`, odd-state length `n`, and actual outgoing valuation sum `V`,

> **`P^12 <= C(R)^(4n) J(R)^(3V-4n)`.**                   (R24H.12)

Because every extended block has `V>=4n/3`, the exponent is nonnegative.

### Finite proof reduction

For a high run of `h>=1` high states, the inherited valuation argument gives

`V_H >= ceil((4h+2)/3)`.                                   (R24H.13)

Before that run the stripped chain contributes `3k-1` valuations in type I and `3k` in type II.

For `h=1`, use the six exact core products.

For `h>=2`:

- type I: use the stripped core, the improved first pair `P_I`, then generic `P_HH` pairs, and one `F_H` if a final high remains unpaired;
- type II: use the stripped core and the generic RL23 high-run pairing.

Under `h -> h+6`, the product bound gains exactly `P_HH^3`, the block length gains `6`, and the certified valuation gains `8`.  Thus `3V-4n` is unchanged.  It is enough to check `h=1,...,6` for each of the six chain types plus

> **`P_HH^36 <= C^24`.**                                   (R24H.14)

The verifier proves all 36 seed inequalities and the extension inequality by exact polynomial positivity after `R=t+161`.

The two support anchors are exact equalities at the level of the comparison line:

- type-I `k=1,m=0`: `(n,V,P)=(3,4,C)`;
- type-II `k=2,m=0`: `(n,V,P)=(5,8,T)`.

## 4. Global theorem

The extended blocks partition the `L` odd states and their outgoing valuations sum exactly to `A`.  Multiplying (R24H.12) gives

`lambda^12 <= C^(4L) J^(3A-4L)`.                           (R24H.15)

Put

`beta=log3/log2`.

Using

`A=beta L + log(lambda)/log2`,                             (R24H.16)

we obtain

> **`log(lambda)/L <= C_H,exact(R)`,**                     (R24H.17)

with

`C_H,exact(R)`
` = [4 log C +(3 beta-4) log J]`
`   / [12 -3 log J/log2]`.                                 (R24H.18)

Its asymptotic coefficient is

`19/81 + [(3 beta-4)/12]*(1519/6912)`
` = 0.248392579520957...`.                                 (R24H.19)

This is a much larger gain than the earlier RL24 supporting line.

## 5. Rational monotone majorant

Use again

`beta<317/200`,

`log u<=u-1`,

`log2>2/3`.

Then

`C_H,exact(R) <= C_H(R)`,                                  (R24H.20)

where

> **`C_H(R)`
> ` = [4(C-1)+(151/200)(J-1)]`
> `   / [12-(9/2)(J-1)]`.**                                (R24H.21)

The verifier proves that `C_H(R)` is strictly decreasing for every `R>=161`.

Its asymptotic coefficient is

> **`lim_(R->infty) R C_H(R)`
> ` = 457841/1843200`
> ` = 0.248394639756944...`.**                             (R24H.22)

Comparison of certified rational coefficients:

- RL22: `0.25`;
- RL23: `0.24921875`;
- RL24 first tilted bound: `0.249173177...`;
- **RL24 type-I high-start bound: `0.248394640...`**.

The apparent reversal versus the first tilted bound is because the old supporting compensator was itself bounded too weakly; after the type-I repair, the true upper hull is supported by the low three-state type-I core and the high-valuation exceptional type-II core.

## 6. Continued-fraction consequence under the inherited floor

Under the inherited external computational input

`R>=R0=2^71`,

monotonicity of (R24H.21) yields a rigorous Legendre window.  The exact verifier reconstructs the above-`beta` convergents and proves

> **`L/gcd(A,L) >= 57,397,300,723`.**                      (R24H.23)

This improves the RL23 floor

`57,302,322,170`

by

`94,978,553`,

and improves the previous RL24 tilted floor by about `89.7 million`.

The next relevant convergent denominator is still

`65,470,613,321`,

so the qualitative CF threshold is not crossed.

## 7. Strategic consequence

This result shows that there was materially more Track-A information left in the existing block partition once **trajectory-determined high starting heights** were retained instead of collapsed to the generic threshold.

The new supporting anchors are now structurally meaningful:

1. the type-I one-low core at valuation density `4/3`;
2. the type-II two-low exceptional core at density `8/5`.

Further improvement from this exact partition must move one of those anchors or add another global moment/ownership constraint.  The local `1/(6 log2)` barrier still remains well above the coefficient needed for the next qualitative CF crossing, so Track B remains necessary.

Verifier: `verify_rl24_typeI_high_start_supporting_line.py`.
