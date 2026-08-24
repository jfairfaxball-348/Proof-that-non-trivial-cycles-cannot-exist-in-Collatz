# RL23 — high-run ownership pushes global odd-state packing strictly below 1/4

Date: 2026-08-21

## Status

Sections 1--4 are **ANALYTIC** for `R>=160`. Section 5 is an **EXACT FINITE CERTIFICATE conditional on the inherited EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`.

This sharpens RL22's terminal-high theorem

`log(lambda)/L <= log(1+1/(4R-1))`

by using the transitions among the high odd states that RL22 had bounded individually.

## 1. Consecutive high odd states have a strong two-state product bound

Let

`H0=(4R-1)/3`,

and let `a,b` be consecutive odd states in the induced odd-state cycle with

`a>=H0`, `b>=H0`.

Write

`nu=v2(3a+1)`, `b=(3a+1)/2^nu`,

and as before put

`F(s)=1+1/(3s)`.

A direct cancellation gives the exact identity

`F(a)F(b)=1+(2^nu+3)/(9a)`.                              (R23P.1)

If `nu=1`, then `a>=H0`, so

`F(a)F(b) <= 1+5/(12R-3)`.

If `nu>=2`, the condition `b>=H0` gives

`a >= (2^nu H0-1)/3`,

hence

`F(a)F(b) <= 1+(2^nu+3)/[2^nu(4R-1)-3]`.

The last excess is strictly decreasing as a function of `2^nu`; its maximum is therefore at `nu=2`. Also

`5/(12R-3) <= 7/(16R-7)`.

Thus every consecutive high/high pair satisfies

> **`F(a)F(b) <= P_HH := 16R/(16R-7)`.**                  (R23P.2)

Asymptotically its two-state logarithmic coefficient is only `7/32`, far below the single high-state coefficient `1/4` used in RL22.

## 2. Extend each maximal low-chain block through its whole following high run

Use the RL22 maximal short-linked low chains. A chain has `k=1,2,3` low states. RL22 attaches the first terminal high odd state `h_0`, producing one of six core blocks of length `2k+1`.

Let `m>=0` be the number of additional consecutive high odd states after `h_0` before the next low-chain start. Thus the full high run is

`h_0,h_1,...,h_m`,

and the extended blocks obtained this way partition the odd cycle.

RL22 gives the following core-product bounds `C`, while the same telescoping argument with the terminal factor removed gives `Q`:

| type | `k` | core length | `C` | stripped `Q` |
|---|---:|---:|---|---|
| I | 1 | 3 | `(27R+19)/(27R)` | `(9R+5)/(9R)` |
| I | 2 | 5 | `(243R+287)/(243R)` | `(81R+85)/(81R)` |
| I | 3 | 7 | `(2187R+3511)/(2187R)` | `(729R+1085)/(729R)` |
| II | 1 | 3 | `32R/(32R-23)` | `8(4R-1)/(32R-23)` |
| II | 2 | 5 | `256R/(256R-319)` | `64(4R-1)/(256R-319)` |
| II | 3 | 7 | `(2187R+3767)/(2187R)` | `(729R+1085)/(729R)` |

When `m=0`, use the core bound `C`.

When `m>=1`, pair `h_0` with `h_1`, then pair successive high states. If one final high state is left unpaired, bound it by

`F_H=4R/(4R-1)`.

So arbitrarily long high gaps reduce to a finite list of seed inequalities plus the high/high pair estimate (R23P.2).

## 3. The new global factor

Define

`T(R)=256R/(256R-319)`,

`G(R)=T(R)^(1/5)`.                                        (R23P.3)

For every `R>=160`, exact rational comparison proves:

1. for each six-state type with core length `n`,
   `C^5 <= T^n`;
2. for each stripped product `Q` with `k` low states,
   `(Q P_HH)^5 <= T^(2k+2)`;
3. for the one-unpaired-high case,
   `(Q P_HH F_H)^5 <= T^(2k+3)`;
4. `P_HH^5 <= T^2`.

The type-II `k=2`, `m=0` core is the equality case defining `T`; every other displayed comparison is strict.

The verifier `verify_rl23_high_run_packing_cf_gate.py` clears positive denominators, substitutes `R=t+160`, and checks that every resulting numerator polynomial has nonnegative coefficients (with at least one positive coefficient outside the defining equality).

Therefore every extended low-chain/high-run block has geometric-mean factor at most `G(R)`, and multiplying the disjoint blocks gives

> **`lambda <= G(R)^L`.**                                  (R23P.4)

Equivalently,

> **`log(lambda)/L <= (1/5) log(256R/(256R-319))`.**       (R23P.5)

Using `log(1+u)<=u`,

> **`log(lambda)/L <= 319/[5(256R-319)]`.**                (R23P.6)

Its asymptotic coefficient is

`319/1280 = 0.24921875 < 1/4`.                              (R23P.7)

Thus the local integer packing method does not literally saturate at `1/4`; high-run transition ownership gives a rigorous, radius-independent strict improvement.

## 4. Relation to the previous theorem

The verifier also checks

`G(R) < F_H`

for every `R>=160`, so (R23P.5) strictly supersedes RL22's terminal-high bound on that range.

The asymptotic improvement is small:

`1/4 - 319/1280 = 1/1280`.

The bottleneck is now the type-II, two-low core with no extra high state. Further Track-A progress must exploit information not used in the six independent core means, for example the outgoing valuation/transition of that extremal core, restrictions on consecutive core types, or the global average `sum nu_i/L=A/L`.

## 5. Continued-fraction consequence under the inherited external floor

Let

`g=gcd(A,L)`, `p=A/g`, `q=L/g`, `beta=log(3)/log(2)`.

From (R23P.6),

`0 < p/q-beta <= c(R)/log(2)`,

where

`c(R)=319/[5(256R-319)]`.                                  (R23P.8)

Under the inherited external computational input

`R>=R0=2^71`,

`verify_rl23_high_run_packing_cf_gate.py` uses rigorous rational intervals for `log 2` and `log 3`, proves the Legendre window through

`q <= 57,302,322,169`,

and checks every above-`beta` convergent in that range against (R23P.8).

Therefore, conditional on `R>=2^71`,

> **`L/gcd(A,L) >= 57,302,322,170`.**                      (R23P.9)

This improves the RL22 floor `57,212,717,233` by `89,604,937`, but the next relevant convergent denominator is still

`65,470,613,321`.

So this is a genuine analytic advance, not yet a qualitative CF-threshold crossing.

## Evidence discipline

- R23P.1--R23P.8: **ANALYTIC** for `R>=160` where stated; the bundled symbolic verifier is an exact algebra sanity/certificate check.
- R23P.9: **EXACT FINITE CERTIFICATE + inherited EXTERNAL COMPUTATIONAL INPUT `R>=2^71`**.
