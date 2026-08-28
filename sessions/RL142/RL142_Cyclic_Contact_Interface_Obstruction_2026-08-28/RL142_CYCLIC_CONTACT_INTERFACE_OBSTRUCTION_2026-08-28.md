# RL142 — cyclic contact-interface obstruction

## Outcome and scope

RL142 removes the fixed-indexing limitation from RL141 for height-one contact
profiles.  Let the `g` reduced blocks be viewed cyclically.  If all blocks
outside a cyclic consecutive interval of `ell` blocks have the same
zero-contact set, the interval differs genuinely, `ell<2^A`, and
`g>=ell+3`, then the profile cannot have ordinary full ownership.

This includes an interface that crosses the originally anchored last/first
block boundary.  It still does not cover scattered support, `ell>=2^A`, too
few exterior blocks, higher/negative original defect paths, a whole
multiplicity, or global closure.

## 1. Exact block-boundary re-anchoring

Let `h_j in {0,1}` be the original height-one defect path and cut the
accelerated exponent word at a block boundary `kL`.  Put `H=h_(kL)` and rotate
the word.  With the mechanical word re-anchored at that boundary, its defect
path is exactly

`h'_j=h_(kL+j)-H`,                                         (1.1)

using the periodic extension of `h`.  The mechanical increments repeat at a
block boundary, so the new accelerated exponents are precisely the rotated
old exponents.  Since `H` is 0 or 1, the new values are either `{0,1}` or
`{-1,0}`.  No nonnegativity is silently retained when `H=1`.

The standard concatenation identity for the affine numerator shows that
full-denominator divisibility is invariant under this word rotation; for an
actual cycle this is also immediate from rotating the physical cycle state.

## 2. The shifted two-level numerator

Retain `B_j=3^(gL-1-j)2^(floor(Aj/L))`, the mechanical numerator `Q_c`, and
`F_g=(2^(gA)-3^(gL))/(2^A-3^L)`.

For the `{0,1}` normalization, RL140 gives

`2Q=Q_c+sum_(h'_j=0)B_j`,

so full ownership forces `F_g` to divide the displayed low-level sum.

For the `{-1,0}` normalization, direct substitution instead gives

`Q=Q_c+sum_(h'_j=-1)B_j`,

and full ownership forces `F_g` to divide the negative-level sum.  In both
cases the active set is exactly the original zero-contact set, merely viewed
from the new block boundary.

## 3. Cyclic reduction to RL141

Choose the cut just before the cyclic exceptional interval.  The interval is
then non-wrapping in the re-anchored indexing.  Section 2 supplies the same
block polynomial used in RL141, either with the zero-contact weights or with
the negative-level weights.  RL141's valuation-band and size proof therefore
applies verbatim: a genuine interval polynomial is nonzero and has absolute
value strictly below `F_g`, contradicting the required divisibility.

Thus the stated cyclic RL142 exclusion follows.

## 4. Verification and limits

`verification/verify_rl142_cyclic_reanchor.py` exhaustively checks, in small
mechanical examples, the block-boundary exponent rotation, invariance of
full-denominator divisibility, and both exact two-level numerator identities.
It is an algebraic cross-check, not the proof.

The argument retains ordinary affine ownership and does not promote a generic
contact count, normalized state identity, or CRT/run-fibre claim.  Scattered
block deviations remain the live target.
