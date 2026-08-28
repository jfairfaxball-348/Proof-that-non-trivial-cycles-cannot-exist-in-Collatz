# RL141 — consecutive multiblock contact obstruction

## Outcome and scope

RL141 extends the RL140 height-one affine-numerator obstruction from one
deviant reduced block to a bounded consecutive interface.

Fix the inherited first reduced above-side pair `(A,L)`, write `X=2^A`, and
consider a hypothetical full-count cycle `(gA,gL)` in the height-one branch
`h_j in {0,1}`.  Divide the zero-contact set into the `g` reduced blocks
`C_t={r: h_(tL+r)=0}`.

> Suppose that, outside one consecutive interval of `ell` reduced blocks, all
> contact sets equal a common set `C`.  If the interval contains a genuine
> deviation, `ell<X`, and `g>=ell+3`, then the profile cannot have ordinary
> full ownership.

The conclusion is an analytic bounded-interface family exclusion.  It does
not cover interfaces that wrap the fixed anchored block indexing, intervals of
length at least `X`, profiles with fewer than three untouched blocks,
arbitrary scattered deviations, higher or negative defects, or a whole
multiplicity.  No frontier or global Gate status changes.

## 1. Carried contact polynomial

Retain the RL140 notation

`Y=3^L`,
`F_g=sum_(t=0)^(g-1) X^tY^(g-1-t)`,

`W_r=3^(L-1-r)2^(floor(Ar/L))`, and
`C(S)=sum_(r in S)W_r`.

For a height-one profile, actual full ownership implies

`F_g | sum_(t=0)^(g-1) X^tY^(g-1-t) C(C_t)`.             (1.1)

This is the exact RL140 contact-weight condition obtained from the ordinary
affine numerator, not an independent rotation or normalized-state condition.

The inherited floor lock gives `W_r<X/3` for every residue.  Therefore, with
`Q_0=sum_r W_r`,

`Q_0<LX/3<X^2`.                                           (1.2)

Distinct contact subsets have distinct weights: the values `v_2(W_r)` are
strictly increasing with `r`.

## 2. Consecutive interface reduction

Let the exceptional interval be `s,...,s+ell-1` (with no wrap), and put

`delta_i=C(C_(s+i))-C(C)`, `0<=i<ell`.

Subtracting the periodic baseline from (1.1), then removing the factor
`X^sY^(g-s-ell)`, which is coprime to `F_g`, shows that ownership requires

`F_g | E`,                                                (2.1)

where

`E=sum_(i=0)^(ell-1) X^iY^(ell-1-i) delta_i`.

At least one `delta_i` is nonzero for a genuine deviation.  Let `i` be the
least such index.  Every `W`-subset difference has 2-adic valuation strictly
below `A`; hence

`v_2(X^iY^(ell-1-i)delta_i) < (i+1)A`.

Every later summand is divisible by `2^((i+1)A)`.  Thus

`E != 0`.                                                 (2.2)

This is the non-cancellation step absent from an arbitrary signed block
polynomial: consecutive powers of `X` place the nonzero subset differences in
disjoint 2-adic valuation bands.

## 3. Size obstruction

Let

`F_ell=sum_(i=0)^(ell-1) X^iY^(ell-1-i)`.

Using `|delta_i|<=Q_0` gives

`|E| <= Q_0 F_ell`.

As `Y<X` and `ell<X`,

`F_ell < ell X^(ell-1) < X^ell`.

Together with (1.2),

`0<|E|<X^(ell+2)`.                                        (3.1)

If `g>=ell+3`, then

`F_g>X^(g-1)>=X^(ell+2)>|E|`.

This contradicts (2.1) and (2.2), proving the stated RL141 theorem.

## 4. Verification and red teams

The exact checker `verification/verify_rl141_consecutive_multiblock.py`
enumerates all small contact subsets and all placements of an interface,
checking the factor reduction, the 2-adic non-cancellation, and the strict
size inequality for representative instances.  It is a finite algebraic
cross-check rather than the proof.

RL141 preserves the RL79/RL20 ownership distinction: the only cycle-specific
input is the ordinary full denominator dividing the ordinary affine numerator.
It does not treat (1.1) as sufficient for a cycle, and it does not infer an
ordinary run/CRT fibre population from contacts alone.

## 5. Next target

The remaining multiblock obstruction is a genuinely nonlocal one: scattered
or wrapping deviations can no longer be placed in one short 2-adic block
polynomial.  A successor should either find an exact factor/valuation control
for that geometry or prove a physical ordinary-state/run theorem that bounds
the permitted support.
