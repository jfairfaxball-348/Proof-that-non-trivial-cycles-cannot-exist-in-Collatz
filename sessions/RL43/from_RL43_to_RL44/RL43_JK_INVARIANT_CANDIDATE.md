# RL43 candidate `J_d/K` invariant — UNPROVED

Date: 2026-08-22

## Status

**CONJECTURAL.** This note records the strongest current route to a uniform one-excursion transport theorem. It must be red-teamed before use.

## 1. State variables

Use the cutoff-free excursion automaton state `(d,e,T,z,...)`, where `d>0` is prefix imbalance, `e` is accumulated excursion excess, `z` is the zero count in the chosen local word convention, and `T` is the normalized 2-adic gap state.

Define

`H := e-z+1`.

From the exact transition laws

`e' = e+d-x`,
`z' = z+1-x`,

one gets

> `H' = H+d-1`.

Thus `H` measures accumulated area above the baseline imbalance `d=1`; neutral height-one pumping costs no `H`.

For a terminal power-of-two outgoing gap `g_out=4*2^t`, the preterminal `d=1` state has

`T+1 = 2*g_out = 2^(t+3)`.

In the one-excursion `G=4` geometry, `q=a-ell=z+t`. Hence

`e >= q+2`

is equivalent to

`H >= t+3`.

So a valuation bound `v2(T+1)<=H` at terminal height one would prove the desired theorem.

## 2. Proposed normalization

Define

`J_d := T + 3^d - 2^d`,

`K := H + d(d+1)/2 - 1`.

At `d=1`,

`J_1=T+1`, `K=H`.

For a descending `10` transition, direct algebra gives

> `J_{d-1}' = J_d/2`,
>
> `K' = K-1`.

Therefore `J/2^K` is exactly preserved along descent whenever the quotient is defined.

## 3. Candidate invariant

The experimentally observed statement is

> **If `2^K` divides `J_d`, then `J_d/2^K <= 1`.**

At terminal `d=1`, if `H<t+3`, then

`J_1/2^K = 2^(t+3-H) > 1`,

contradicting the candidate invariant. Thus it would imply

`H>=t+3`, hence `e>=q+2`, hence `rho_E>=a`.

## 4. What is proved versus observed

Proved algebraically:

- `H'=H+d-1`;
- terminal `J_1=T+1=2^(t+3)` for the relevant power-of-two outgoing gap;
- descending `10` normalization `J' = J/2`, `K'=K-1`.

Observed in exact state exploration, not proved:

- no state tested violates the candidate divisibility/quotient implication;
- the resulting margin `e-(z+t)>=2` is sharp in observed gap-9 families.

## 5. RL44 proof tasks

1. Derive exact `(J,K)` transformations for `00`, `11`, and `01`.
2. Search for an induction region/order condition stronger than the bare quotient inequality.
3. Attempt a minimal-counterexample proof: identify what a first state with divisible `J` and quotient `>1` would imply about its predecessor.
4. If the invariant fails, quantify the smallest failure and test whether a weaker terminal-only valuation theorem survives.
5. Do not infer truth from finite exploration.
