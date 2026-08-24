# RL45 — terminal valuation reduction to the `(d,H,J)` automaton

Date: 2026-08-22

## Status

**ANALYTIC REDUCTION + EXACT FINITE CERTIFICATE.**

The uniform terminal valuation theorem is **not proved**.  RL45 does, however, remove two inessential state variables and isolates a strictly weaker valuation invariant than the failed RL44 size bound.

For a canonical positive excursion entering physical gap `9`, the target remains

`v2(D_E-9*3^p) <= rho_E`.

At terminal height one this is equivalent to

`v2(T+1) <= H`, where `H=rho_E-h+1`.

The new exact quotient state is only `(d,H,J)`, with

`J := T + 3^d - 2^d`.

No excursion weight, length, zero count, or excess is needed to propagate this state.

## 1. Exact Markov reduction

RL44 already proved

`H' = H+d-1`.

Put

`A_d=3^d-2^d`,
`B_d=2^d-1`,
`C_d=3^(d+1)-2^d-1`.

Because `A_d` is odd,

`J = T + A_d`

has parity opposite to `T`.  The exact compatibility rules therefore collapse to two edges determined only by the parity of `J`.

If `J` is odd (`T` even), the only compatible internal edges are the same-bit edges:

- `00`: `J'=(J+A_d)/2`, `d'=d`;
- `11`: `J'=(3J+B_d)/2`, `d'=d`.

If `J` is even (`T` odd), the only compatible edges are the skew edges:

- `01`: `J'=(3J+C_d)/2`, `d'=d+1`;
- `10`: `J'=J/2`, `d'=d-1` (internal only when `d>1`).

Every internal edge has the same area update

`H'=H+d-1`.

Thus `(d,H,J)` is an exact Markov quotient of the terminal-valuation problem.

For incoming gap `9`, after the mandatory first local column `(0,1)`,

`(d,H,T,J)=(1,0,-14,-13)`.

## 2. The correct valuation invariant

Retain

`K := H + d(d+1)/2 - 1`.

RL44 tested the stronger divisibility/size statement

`2^K | J  =>  J/2^K <=1`.

A still weaker statement is enough:

> **RL45 valuation candidate.**  Every reachable state with `J>0` satisfies
>
> `v2(J) <= K`.

At terminal height `d=1`, one has `K=H` and `J=T+1`, so this gives exactly

`v2(T+1)<=H`.

This candidate deliberately does **not** assert the false unconditional inequality `J<=2^K`.

## 3. Exact descent preservation

For an internal `10` descent,

`J'=J/2`, `K'=K-1`.

Hence, whenever `J!=0`,

`v2(J')-K' = v2(J)-K`.

In particular a positive violation `v2(J)>K` at height `d>1` has enough 2-adic divisibility to make all `d-1` successive `10` descents compatible, and the violation margin is preserved until height one.

Therefore:

> **It is enough to exclude positive valuation violations at height one.**

This is a sharper reduction than the RL44 `J/2^K` quotient candidate because only valuation, not quotient size, is retained.

## 4. Exact `H<=23` certificate, independent of excursion length

The companion verifier `verify_rl45_terminal_H23.py` explores the quotient state directly by `H`, not by excess `e`.

State counts for exact levels `H=0,...,23` are

`[9,10,9,32,26,49,90,105,172,270,549,859,1768,3578,6906,13642,26624,53758,109744,222460,458460,950914,1987355,4152245]`.

No positive reachable state satisfies `v2(J)>K` through `H=23`.

Even more sharply, the only positive equality state is

`(H,d,J,K)=(3,1,8,3)`,

which is the sharp gap-9 crossing state `T=7`, outgoing gap `4`.

This certificate is stronger in a different direction than the inherited `e<=40` phase certificate: once `(d,H,J)` is fixed, arbitrary excursion weight, zero count, and neutral/zero-cost pumping are already quotiented out.  It is still only a **finite certificate in H**, not a proof for all `H`.

## 5. Why this is the right next proof target

The exact transition ratios show where a proof can and cannot live.

At heights `d>=2`, `K` grows on every same-height/up step and the normalized real size `J/2^K` is strongly contracted, while a `10` descent preserves the normalized quotient.  The difficult behavior is concentrated at `d=1`, where `H` and `K` do not grow under same-height `00/11` steps.

At `d=1` the horizontal maps on odd `J` are exactly

`00: J -> (J+1)/2`,
`11: J -> (3J+1)/2`.

This zero-cost height-one dynamics is the obstruction to a naive one-step induction.  It contains exact cycles such as `J=3 <-> 5` (using `11` then `00`) and fixed states such as `J=1` under `00`.  Any uniform proof must either quotient this height-one dynamics analytically or find a potential that controls its even exits.

This explains why the failed unconditional `J<=2^K` route was too strong while the valuation statement can still survive.

## 6. Consequence for the live one-excursion branch

In the live one-excursion branch,

`D_E=2^a+3^ell`, `p=ell-2`.

Therefore

`D_E-9*3^p = 2^a`.

So the uniform terminal theorem would give

`a <= rho_E`,

or equivalently

`e>=q+2`, `q=a-ell`.

That consequence remains **conjectural**.  RL45 has improved the exact proof target and its state space, but has not closed it.
