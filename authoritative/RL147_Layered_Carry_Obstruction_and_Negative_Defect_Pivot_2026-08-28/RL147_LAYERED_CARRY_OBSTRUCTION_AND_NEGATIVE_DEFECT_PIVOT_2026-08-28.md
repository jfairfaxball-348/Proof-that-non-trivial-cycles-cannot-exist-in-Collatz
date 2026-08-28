# RL147 — Layered carry obstruction and negative-defect pivot

Date: 2026-08-28

## Status

**Proved analytic algebraic reduction and method barrier, conditional on the
ordinary full-ownership setting.**  RL147 does not exclude a mixed-height
owner.  It proves exactly why the RL146 carry-order proof does not extend by
binary layering alone, then pivots the live target to genuine negative defect.

## 1. General bounded nonnegative profile

Let a hypothetical ordinary full-count cycle have `N=gL`, mechanical floor
`b_j=floor(Aj/L)`, and nonnegative defect `h_j=b_j-S_j`.  Since the cycle is
finite, put `H=max_j h_j`.  Thus `0<=h_j<=H`, and

`a_j=b_(j+1)-b_j+h_j-h_(j+1)`.

With `B_j=3^(N-1-j)2^(b_j)`, the ordinary affine numerator is

`Q_h=sum_j B_j 2^(-h_j)`.

For `ell=1,...,H`, write `E_ell={j:h_j<ell}`.  The sets are nested, but are
not separately owned.  The elementary identity

`2^(H-h)-1=sum_(ell=1)^H 2^(H-ell) 1_(h<ell)`

gives the exact numerator identity

`2^H Q_h = Q_c + sum_(ell=1)^H 2^(H-ell) R_ell`,

where `Q_c=sum_j B_j` and `R_ell=sum_(j in E_ell) B_j`.

Because the ordinary denominator divides `Q_h`, and
`2^(gA)-3^(gL)=(X-Y)F_g` while `F_g|Q_c`, full ownership implies only

`F_g | sum_(ell=1)^H 2^(H-ell) R_ell`.                         (1)

This is one combined divisibility statement.  In particular, (1) does not
license a quotient/carry for an individual superlevel set `E_ell`; any such
factorization would require a new theorem.

## 2. The exact combined carry ladder

For a reduced block, define the digit

`u_(t,r)=2^(H-h_(tL+r))-1`

and its combined weight `v_t=sum_r W_r u_(t,r)`.  Equation (1) is precisely

`F_g | sum_t X^tY^(g-1-t)v_t`.

The RL145 shift calculation therefore yields integer carries `d_t` with

`v_(t+1)-v_t=Y d_t-X d_(t+1)`,  and  `sum_t d_t=0`.            (2)

Set `epsilon_(t,r)=u_(t+1,r)-u_(t,r)` and

`z_(t,0)=d_t`,  `z_(t,r+1)=3z_(t,r)-epsilon_(t,r)2^(b_r)`.

Exactly as in RL146, unrolling (2) gives `z_(t,L)=2^A d_(t+1)`.
Backward descent proves `2^(b_r)|z_(t,r)`, so `y_(t,r)=z_(t,r)/2^(b_r)` is
integral and satisfies

`3y_(t,r)+u_(t,r)=2^(b_(r+1)-b_r)y_(t,r+1)+u_(t+1,r)`.       (3)

Thus a layer decomposition does preserve one *combined* carry ladder.

## 3. Exact obstruction to the RL146 order step

For height one, the possible digit values are `{0,1}`.  RL146 used the fact
that a unit carry gap contributes `3`, while the two digit errors total at
most `2`.

For `H>=2`, the allowed digit set is

`U_H={2^k-1:0<=k<=H}`;

already `U_2={0,1,3}`.  Equation (3) no longer preserves strict scalar order.
At either permitted mechanical increment `a=1` or `a=2`, the following exact
local data obey (3):

`(y,u,u_next)=(1,0,3)` maps to `y_next=0`,

`(y,u,u_next)=(0,3,3)` maps to `y_next=0`.

The input carries are strictly ordered, but the outputs are equal.  This is a
counterexample to the local implication used in RL146, not a claimed cycle.
It also shows why replacing scalar digits by their binary layers cannot by
itself give the previous cyclic order lock: the ownership relation supplies
only their weighted sum, and its local transition admits this collapse.

No impossibility theorem for every conceivable vector or lexicographic
invariant is asserted.  The proved conclusion is narrower: the inherited
RL146 mechanism has no coefficient-independent lift from the currently
available combined layer identity.

## 4. Pivot and scope

The primary RL147 phase is therefore complete.  The exact obstruction is
frozen as a method barrier.  Per the inherited target, the next live frontier
is **genuine negative defect**, using RL136's owned isolated-excursion
signature rather than reopening the saturated RL145 local population route.

Nothing here closes mixed nonnegative height, `g=1`, negative defect, Gate A,
Gate B, non-trivial cycles, or the Collatz conjecture.

## 5. Red teams

- The ordinary `+1` affine numerator and full denominator remain load-bearing.
- The layer identity is an equality; no independent ownership is assumed.
- The local collapse is labelled a mechanism obstruction, never evidence of a
  physical cycle.
- Physical-state assertions remain restricted to the inherited RL136
  negative-excursion results.
- RL145's saturated local population route is not reopened.
