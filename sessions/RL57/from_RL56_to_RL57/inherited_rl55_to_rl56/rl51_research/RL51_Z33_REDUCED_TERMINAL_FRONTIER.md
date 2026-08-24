# RL51 — z=33 reduced terminal frontier

Date: 2026-08-23

## Status

**EXACT ANALYTIC REDUCTION; z=33 NOT YET ELIMINATED.**

After eliminating `z=29` and `z=31`, parity leaves `z>=33`. The same mass/defect coupling sharply reduces the first open odd case.

At `z=33` there are 32 internal x-zeros and y-zeros.

## 1. Prefix bound

For fixed `P=p_26`, maximize the first 25 zero weights greedily and maximize zeros 27--32 greedily from `P`.

At `P=57`, this relaxed maximum is

`11.91656227117... < 143/12`.

Hence any survivor has

`p_26<=56`, so `u_26<=81`.

## 2. Defect localization

If at least eleven of the first 26 matching y-zeros occur after `u_26`, order forces indices 16--26 to be delayed. The same cancellation used at `z=31` gives

`E > 143/12 - M_15 - F_27..32(P) - C_11(P)`.

For every `P=45,...,56`, exact rational evaluation gives

`E > 1.99029021235... > 5/3`.

Therefore at most ten of `y_1,...,y_26` lie after `u_26`.

Since six x-zero indices remain, the entire suffix after `u_26` has the bounded budgets

`x-zero <=6`,

`y-zero <=16`.

The required suffix is still astronomical: because `u_26<=81` and the internal length is `ell+29`, it has length at least `ell-53`.

## 3. Live target

The next exact problem is therefore:

> Starting from terminal `Q_1=2^k+1` at the z=33 exponent, prove that a backward suffix with at most 6 x-zero edges and at most 16 y-zero edges has bounded length far below `ell-53`.

A raw column-by-column BFS grows rapidly and is not yet a practical certificate. The next implementation should use an accelerated 3-adic/event automaton, jumping maximal `11` runs and carrying only zero-event states, ideally with the mass/defect residual budget incorporated into the state.

This note does **not** claim z=33 is excluded.

## Verification

Run:

`python3 rl51_research/verify_rl51_z33_reduced_frontier.py`
