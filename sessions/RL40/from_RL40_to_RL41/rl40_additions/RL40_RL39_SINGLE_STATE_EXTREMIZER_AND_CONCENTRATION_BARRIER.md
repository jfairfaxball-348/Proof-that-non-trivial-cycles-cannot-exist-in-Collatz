# RL40 — exact RL39 single-state extremizer and the concentration barrier

Date: 2026-08-21

## Status

**ANALYTIC.**

This note solves Track A's fixed-multiplicity RL39 extremal problem exactly and records an important negative conclusion: **RL39 transport charge by itself cannot yield a product saving linear in total transport area.**  The obstruction is concentration of arbitrarily large transport charge into one extremely high owned odd state.

This does not weaken RL39.  It identifies precisely what extra theorem is needed to make RL39 branch-closing: a spread condition (many charged owned states), an upper bound on per-state height/charge, or a separate RL38/sparse-relation mechanism that excludes the concentration regime.

## 1. Exact charge variable

For an excursion-owned odd state with assigned multiplicity `l>=1`, retain

`H = log_3(((3y+1)z)/R)`,

`alpha=log_3 2`,

and define its RL39 charge

> `q = l H - alpha*l(l-1)/2`.                              (R40E.1)

This is the summand occurring in RL39.7/RL39.14.

Solving for `H`,

`H = q/l + alpha*(l-1)/2`,

hence exactly

> `3^H = 3^(q/l) * 2^((l-1)/2)`.                          (R40E.2)

## 2. Exact correction contribution as a function of charge

From the definition of `H`,

`3y+1 = R 3^H/z`.

Therefore the odd correction factor satisfies the exact identity

`1+1/(3y) = 1/[1-z/(R 3^H)]`.

Multiplying its logarithm by `R` and using (R40E.2) gives

> **`C_l(q)`**
> `:= R log(1+1/(3y))`
> `= -R log(1 - (z/R) 2^(-(l-1)/2) 3^(-q/l)).`            (R40E.3)

Thus the fixed-`l` extremal problem is not merely bounded: it is explicitly parametrized by the charge `q`.

Equivalently, if one only knows that the charge is at least `q_*`, then because the function below is decreasing,

> `q>=q_*  =>  R log(1+1/(3y)) <= C_l(q_*)`.              (R40E.4)

This is the sharp single-state bound compatible with the RL39 variables, before adding the independent first/later-state floors on `H`.

## 3. Strict monotonicity and convexity

Put

`a_l=(z/R)2^(-(l-1)/2)`,

`b_l=(log 3)/l`,

so

`C_l(q)=-R log(1-a_l exp(-b_l q))`.

In the physical range `0<a_l exp(-b_l q)<1`, direct differentiation gives

> `C_l'(q) = -R b_l u/(1-u) <0`,                           (R40E.5)
>
> `C_l''(q) = R b_l^2 u/(1-u)^2 >0`,                      (R40E.6)

where `u=a_l exp(-b_l q)`.

Hence for every fixed multiplicity `l`, the correction contribution is

> **strictly decreasing and strictly convex in the RL39 charge.**

The convexity direction is crucial.

## 4. Aggregation with fixed multiplicities

Fix owned states `i=1,...,P`, multiplicities `l_i`, and admissible lower charge floors `q_i>=q_i0` coming from RL39.10--RL39.12.

Suppose the total charge is prescribed:

`sum_i q_i = Q >= Q0:=sum_i q_i0`.

The total normalized correction is

`C(q_1,...,q_P)=sum_i C_(l_i)(q_i)`.

Because each summand is convex, `C` is convex on the simplex

`q_i>=q_i0`, `sum q_i=Q`.

A convex function on this compact simplex attains its maximum at an extreme point.  Every extreme point has the form

> all states but one at their minimum charge, with the entire excess
> `Q-Q0` placed on a single state.                         (R40E.7)

Therefore **concentrating transport charge is favorable for maximizing the correction product**.

This is the opposite of the spread heuristic one might initially hope for.

If the multiplicities are equal, the conclusion is especially simple: all excess charge can be placed on any one state.  With unequal multiplicities, the extremizer chooses whichever single state loses the least correction when it absorbs the excess.

## 5. Saturation of the product saving

For every fixed `l`,

`C_l(q) -> 0` as `q->infinity`.

Consequently, with fixed multiplicities and lower floors, as `Q->infinity` the maximal aggregate correction tends to

> `sum_i C_(l_i)(q_i0) - min_j C_(l_j)(q_j0)`.             (R40E.8)

In words: **arbitrarily large total transport charge can be hidden by sacrificing only one owned odd correction factor.**

The total product saving therefore saturates at the loss of one baseline state unless some independent theorem prevents this concentration.

## 6. No linear-in-`rho` consequence from RL39 alone

RL39 gives only

`rho <= sum_i q_i`.

There can be no universal inequality derived from these variables alone of the form

`sum_i C_(l_i)(q_i) <= B(l_1,...,l_P) - mu*rho`

with any fixed `mu>0` valid for arbitrarily large charge: take one `q_j->infinity`.  The left side remains nonnegative and approaches a finite positive limit if `P>=2`, while the proposed right side tends to `-infinity`.

Even for `P=1`, the correction tends to zero only exponentially while a negative linear right side eventually becomes impossible.

Thus a supporting inequality with a genuinely negative linear coefficient of total transport cannot come from RL39.14 alone.

## 7. Interaction with the valuation budget

The exact valuation constraint

`sum l_i <= A`

does not remove the concentration obstruction.  It limits multiplicities but does not upper-bound `H` or `q` for a chosen state.  One state can still absorb arbitrarily large transport charge by becoming arbitrarily high.

A large `l` can make concentration even cheaper in correction-product terms, because the independent RL39 valuation floor forces its baseline correction to be geometrically small already.

Therefore the exact identity

`A/L = log_2 3 + log(lambda)/(L log 2)`

is necessary for self-consistency but is not, by itself, a spread theorem for the RL39 charge.

## 8. What theorem would make RL39 decisive?

At least one of the following would defeat the concentration extremizer:

1. **Charge spread:** prove that a fixed fraction of `rho` must be carried by `Omega(L)` distinct owned odd states, or at least that no one state can absorb more than `O(1)` / `o(L)` effective charge.
2. **Height cap:** bound `H_y` for excursion-owned states in terms of local transport, physical gap, or the global near-resonant geometry strongly enough to cap each `q_y`.
3. **Valuation-height coupling beyond RL39:** show that a state with very large `H` and/or `l` forces additional product loss elsewhere through successor dynamics.
4. **Low-transport elimination:** use RL38 integer-gap reachability / sparse S-unit structure to exclude the regime where only finitely many states carry the transport.  The new RL40 result `rho>=18` is a first step in this direction.
5. **Direct distortion control:** use `lambda=prod_E J_E^2` to rule out the concentrated-height patterns without translating them statewise into correction factors.

The immediate strategic conclusion is that the next productive overlap theorem should not seek a bound linear in raw `rho` from RL39 alone.  It should first prove a spread/cap dichotomy, or continue the RL40 crossing-aware reachability attack on the low-transport concentration regime.
