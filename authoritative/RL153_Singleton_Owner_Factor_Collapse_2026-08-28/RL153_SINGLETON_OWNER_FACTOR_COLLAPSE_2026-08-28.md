# RL153 — singleton owner-factor collapse and the residual one-block congruence

Date: 2026-08-28

## Status

**Proved analytic reduction / method barrier.**  RL153 does not exclude the
`g=1` survivor.  It identifies the exact point at which the inherited
RL140--RL147 repeated-block contact/carry machinery loses all force at one
block, and isolates the original full-denominator congruence which any direct
singleton attack must use instead.

No Gate A or Gate B closes.  No non-trivial-cycle or Collatz conclusion is
claimed.

## 1. Frozen setting

Use the first above-side reduced survivor

`(A,L)=(217,976,794,617,137,528,045,312)`

and put `X=2^A`, `Y=3^L`.  In the `g=1` physical branch, RL133 supplies a
nonnegative integer defect path

`h_j=floor(Aj/L)-S_j`, `0<=j<=L`,

with `h_0=h_L=0`.  RL133.5 has already excluded only the identically-zero
path.  Thus the surviving singleton subcase has a nonzero nonnegative defect
excursion.  The full ordinary affine numerator is

`Q_h=sum_(j=0)^(L-1) 3^(L-1-j)2^(floor(Aj/L)-h_j)`,

and actual cycle ownership requires

`X-Y | Q_h`.                                                     (1.1)

This is the original ordinary `+1` condition.  It is necessary only; no
converse is used.

## 2. Exact factor collapse

The repeated-block method factors the full denominator as

`X^g-Y^g=(X-Y)F_g`,

where

`F_g=sum_(t=0)^(g-1)X^tY^(g-1-t)`.                         (2.1)

For height one, RL140 converts full ownership into the necessary contact
condition `F_g | R_0`; RL147 gives the corresponding combined-level
condition for a bounded nonnegative profile.  Both mechanisms then compare
the `g` cyclic block interfaces.

At one block, however,

`F_1=1`.                                                    (2.2)

Therefore every statement of the form `F_1 | R` is the tautology `1 | R`.
There is no nontrivial quotient, no second block interface, and no cyclic
carry vector.  In particular, the RL146 strict-order/cyclic-order argument
cannot be specialized to `g=1`: its endpoint carries are variables indexed
by block interfaces, of which there is only one, while the divisibility input
used to define them has become vacuous.

This is a precise scope boundary, not a weakness in RL146.  RL146 remains a
valid `g>1` primitive height-one theorem; it simply has no singleton premise
from which to start.

## 3. The residual one-block congruence

Let `H=max h_j`, let

`B_j=3^(L-1-j)2^(floor(Aj/L))`,

`Q_c=sum_j B_j`, and, for `1<=ell<=H`, let

`R_ell=sum_(h_j<ell) B_j`.

The elementary digit identity used in RL147 remains valid at one block:

`2^H Q_h = Q_c + sum_(ell=1)^H 2^(H-ell) R_ell`.          (3.1)

Since `X-Y` is odd, (1.1) is equivalent to the non-vacuous congruence

`Q_c + sum_(ell=1)^H 2^(H-ell)R_ell == 0 (mod X-Y)`.      (3.2)

For height one this is simply

`Q_c+R_1 == 0 (mod X-Y)`.                                 (3.3)

Equation (3.2), rather than the cancelled `F_1` condition, is the exact
remaining owner-level datum for the singleton branch.  It couples all defect
levels at once.  It does not authorize separate congruences for the sets
`{h<ell}`.

## 4. Consequence for the live route

The requested direct attack has therefore reduced the live singleton
obligation to a genuinely one-block problem: turn (3.2), together with the
physical least-state inequalities and nonnegative excursion grammar, into an
exclusion or a smaller exact residual class.

The repeated-block routes are now frozen for `g=1`:

- do not import RL146's `g>1` cyclic repetition contradiction;
- do not treat `F_1|R` as a restriction;
- do not split (3.2) into independently owned level congruences.

The smallest explicit surviving class is a physical `g=1` owner with a
nonzero nonnegative defect excursion satisfying (3.2).  A successor must
attack the full modulus `X-Y`, for example through a certified finite prefix
state/residue transfer that retains the physical `+1` recurrence.  Broad
unstructured state enumeration remains outside scope.

## 5. Red teams

- The full ordinary denominator `X-Y`, not merely `F_1`, is retained in
  (1.1)--(3.3).
- No divisibility converse or cycle construction is asserted.
- The defect-level sets are explicitly coupled; no independent layer
  ownership is inferred.
- RL133's nonnegative-defect theorem and its zero-defect exclusion are used
  only in the singleton branch.
- RL146 is not applied at `g=1`.

