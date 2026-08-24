# RL23 — asymptotic barrier for purely local least-state trajectory packing

Date: 2026-08-21

## Status

**ANALYTIC META-LEMMA / METHOD OBSTRUCTION.** This is not a theorem about complete cycles. It constructs arbitrarily long exact integer Collatz trajectory segments whose least state is their initial state and whose local packing coefficient approaches a fixed constant.

Therefore any proposed packing argument that is required to hold uniformly on arbitrary finite least-respecting odd trajectory segments, without using global cycle closure or RL-specific ownership outside the segment, cannot beat that constant.

## 1. Greedy multiplicative itinerary

Let

`beta=log_2(3)`.

For `i>=0`, put

`A_i=floor(i beta)`,

and define odd-to-odd exponents

`nu_i=A_(i+1)-A_i`,

so every `nu_i` is `1` or `2`.

In the multiplicative large-state limit, the normalized odd states are

`t_i=3^i/2^(A_i)=2^{ {i beta} }`,                          (R23B.1)

hence

`1 <= t_i < 2`,

with `t_0=1` and `t_i>1` for every `i>0` because `beta` is irrational.

This is exactly the greedy itinerary that keeps the normalized state as low as possible while never dropping below `1`.

## 2. Exact integer realization of every finite greedy cylinder

Fix any finite length `n`. Prescribe the exponents `nu_0,...,nu_(n-1)` above and construct backward from an odd terminal state by

`x_i=(2^(nu_i) x_(i+1)-1)/3`.                              (R23B.2)

The `n` integrality conditions determine one residue class for the terminal state modulo `3^n`. Hence there are infinitely many exact odd integer trajectories realizing the prescribed exponent word.

As the terminal representative tends to infinity inside this residue class,

`x_i/x_0 -> 3^i/2^(A_i)=t_i`.                              (R23B.3)

For fixed `n`, all `t_i` with `i>0` are strictly above `1`; choosing a sufficiently large representative therefore gives

`x_i>x_0` for all `1<=i<=n`.

Thus `R:=x_0` is the least state of the whole finite segment. The initial residue can also be chosen nonzero modulo `3`, while every later phase is automatically nonzero modulo `3` for an actual Collatz trajectory.

The verifier `verify_rl23_local_dynamical_barrier.py` constructs exact examples for several lengths and checks every transition.

## 3. Limiting local packing coefficient

For `F(x)=1+1/(3x)`, along such a large exact representative,

`R log F(x_i) -> 1/(3 t_i) = (1/3) 2^{-{i beta}}`.          (R23B.4)

Therefore the asymptotic coefficient of the length-`n` cylinder is

`C_n=(1/(3n)) sum_(i=0)^(n-1) 2^{-{i beta}}`.              (R23B.5)

Since `beta` is irrational, the fractional parts `{i beta}` are equidistributed modulo `1`. Hence

`C_n -> (1/3) integral_0^1 2^{-u} du`
`    = 1/(6 log 2)`
`    = 0.24044917348...`.                                  (R23B.6)

So arbitrarily long exact least-respecting integer trajectory segments have local logarithmic packing coefficient as close as desired to

> **`C_local = 1/(6 log 2) ~= 0.24044917`.**                (R23B.7)

## 4. What this obstructs

This does **not** say that a complete Collatz cycle can realize the greedy infinite itinerary. Closure is precisely the missing global condition.

It does say that any proof whose only input is a bounded/local odd-trajectory window, the least-state floor, and the ordinary Collatz transition law cannot establish a universal asymptotic coefficient below `1/(6 log 2)` on all such windows. To go lower, one must exploit genuinely global information: cycle closure, the global valuation sum, balanced-return ownership, RL root/final-return grammar, cubic/factor arithmetic, or another nonlocal constraint.

The current RL23 coefficient `319/1280 ~=0.24921875` therefore still has some local room for improvement, but only down toward a natural local scale around `0.24045`.

## 5. Why Track A alone is unlikely to cross the next CF denominator

Under the inherited external floor `R0=2^71`, a pure coefficient model

`log(lambda)/L <= C/R`

would need approximately

`C < R0 log(2) / [2*(65,470,613,321)^2]`
`  ~= 0.190912`                                             (R23B.8)

to push the Legendre window through the next continued-fraction denominator `65,470,613,321`.

That target is far below the local dynamical scale `1/(6 log 2) ~=0.240449`.

Thus even a near-optimal exploitation of **local** least-state transition packing is not expected to cross the next qualitative CF threshold. This is strong strategic evidence that the main bridge must use nonlocal ownership/arithmetic, with the strengthened cubic mode the most natural current candidate.

## Evidence discipline

- The finite-cylinder integer realization and limiting ratios are **ANALYTIC**.
- The limit (R23B.6) uses the standard equidistribution of irrational rotations.
- The bundled verifier is a finite exact sanity check, not the proof of equidistribution.
- The CF comparison in Section 5 is a strategic numerical threshold comparison, not a new cycle exclusion.
