# RL206 candidate: exact finite-arc lattice and bounded rational-residual barrier

Date: 2026-08-31. Classification: **proved analytic mathematics / method
barrier**, independently reviewed at the exact stated scope.

This theorem concerns an explicitly delimited natural family. It does not rule out
nonlinear arithmetic of full owned cycles, a proof of full-`D` ownership, an independently
proved global inequality, or a bounded reduction obtained using global closure.

## 1. Family and hypotheses

Fix a binary parity arc `e_0,...,e_(m-1)` of finite length `m>=1`, without imposing
periodic closure. Its integer states satisfy

`2x_(j+1)=3^(e_j)x_j+e_j` for `0<=j<m`.

Let `P_j=sum_(i<j)e_i`, and let `Q_j` be the usual affine numerator of the first
`j` bits, so `Q_0=0` and

`2^j x_j=3^(P_j)x_0+Q_j`.

The residual family consists of rational functions `F(x_0,...,x_m)` with rational
coefficients fixed once the arc and any fixed external parameters have been chosen.
It includes arbitrary fixed-degree polynomial combinations, rational normalizations,
state differences, and weighted sums of the corrected block-lift increments wherever
their denominators do not vanish. It excludes floor, remainder, valuation, and other
nonrational operations. Coefficients may not vary with the free initial-state parameter.

A conclusion is called **arc-local** here only if it is asserted from the displayed
integer recurrence and positivity alone, uniformly for all its compatible integer
initial states. A full-cycle ownership or least-state condition is additional data;
the theorem does not assume that arbitrary arc extensions are owned cycles.

## 2. Exact integer-state parameterization

Put `q=Q_m`, `p=P_m`, and let `a_0` be the unique residue in `[0,2^m)` satisfying

`3^p a_0+q=0 (mod 2^m)`.

This exists uniquely because `3^p` is invertible modulo `2^m`. Propagate the recurrence
from `a_0` to get `a_j`, and set

`b_j=3^(P_j)2^(m-j)` for `0<=j<=m`.

**Theorem 1.** Every integer trajectory with this exact parity arc, and only those
trajectories, has the form

`x_j(t)=a_j+b_j t`, `t in Z`.

Every `a_j` is an integer and has parity `e_j` for `j<m`. All states in the arc are
strictly positive for every sufficiently large integer `t`.

**Proof.** Integral `x_m` forces `3^p x_0+q` to be divisible by `2^m`, hence
`x_0=a_0+2^m t`. Conversely, split the word at any prefix `j`. The composition identity

`q=3^(p-P_j)Q_j+2^j Q(e_j...e_(m-1))`

shows that `3^(P_j)a_0+Q_j` is divisible by `2^j`: the full numerator is divisible
by `2^j` and its remaining factor `3^(p-P_j)` is odd. Thus every `a_j` is an integer.
Subtract the trajectories from `x_0` and `a_0`; prefix transport gives the stated
coefficient `b_j`. The recurrence modulo 2 forces `x_j` to be even if `e_j=0` and odd
if `e_j=1`; conversely those parities make the prescribed affine branches the ordinary
shortcut map on this finite arc. Every `b_j` is positive, so a sufficiently large `t`
makes all finitely many `a_j+b_jt` positive. This proves both directions. QED.

This is an exact affine lattice, not a finite experiment and not an existence theorem
for any periodic cycle.

## 3. Bounded integer rational residuals are constant

**Theorem 2.** Restrict a residual `F` in section 1 to the affine lattice of Theorem 1.
Assume it is defined and integer-valued for every sufficiently large integer `t`.
If there is a fixed finite constant `M` such that

`|F(x_0(t),...,x_m(t))|<M`

for all these `t`, then its restriction is a constant rational function of `t`, and
that constant is an integer.

**Proof.** Substitution gives a one-variable rational function `f(t)=U(t)/V(t)` with
`U,V in Q[t]` and `V` not the zero polynomial. For all sufficiently large integers,
the values lie in the finite set of integers in `(-M,M)`. At least one integer `c`
is attained infinitely often. The polynomial `U-cV` therefore has infinitely many
distinct zeros and is identically zero. Hence `f=c` as a rational function, with
removable zeros of its presentation irrelevant. QED.

For a polynomial residual, the same conclusion follows because every nonconstant
real polynomial is unbounded on this integer ray. The rational-function proof shows
why integrality is essential: `1/(1+x_0)` is a bounded nonconstant rational function
on positive arcs, but is not integer-valued there.

**Corollary 2a (recurrence elimination).** A bounded integer rational residual from
this family loses all dependence on the free quotient-state scale. After substituting
the affine transport equations it is the same constant on every rational trajectory
of that fixed arc where the expression is defined. If that arc occurs in the RL20
rational fake, with identical fixed external coefficients and a defined evaluation,
the residual has the same value there. An arbitrary arc need not occur in that fake.
This does not remove a separately imposed ownership premise; it only classifies
what the residual value contains. The constant can depend on the word and the fixed
external parameters, including any independently supplied global data.

**Corollary 2b (small-multiple trap).** Let `M` be a fixed positive integer used as
both the divisibility modulus and the strict-bound scale. If `M` divides this residual
on every sufficiently large compatible integer arc and the strict bound is `|F|<M`,
then `F` is identically zero on the affine arc. It cannot
also be nonzero there. A nonzero contradiction must use a hypothesis which excludes
these free arc states; the displayed local recurrence, integrality and positivity
alone do not do that.

## 4. Exact scope relative to RL206

Theorem 2 does **not** let one replace an owned cycle by arbitrary large arc states.
For a fixed complete word, closure imposes `D x_0=Q`, fixing the initial state uniquely
over the rationals, and possibly excluding all integer states. A proof that exploits
that closure, an exhaustive canonical-witness theorem, independently established
least-state inequalities, or arithmetic such as residues/valuations is outside this
arc-local uniform-bound no-go.

Likewise, this theorem does not establish that a bounded integer residual derived
using additional global hypotheses must be constant across different words. It only
retires the explicitly specified finite-arc rational family when the claimed size bound
comes solely from its local integer transport. The missing full-cycle information must
be stated and proved rather than silently supplied as a bound on free context.

## 5. Verification contract

The analytic proofs above establish all lengths and states. A standalone exact verifier
checks the complete finite population of binary arcs of lengths 1 through 10 and
the specified integer parameters `t=0,1,2,17`. That finite check is regression evidence
for the formulas, not the proof of Theorems 1 and 2 and not a cycle/rank exclusion.

The residual family, universal quantifiers, nonzero-denominator premise, and the
absence of full-cycle closure are required red-team checks before promotion.
