# RL269 mandatory red team

Date: 2026-09-06

## Five-component bound

- No RL267 three-component or RL268 four-component support constant is reused.
- `[1,1,1,1,1]` is cut at a longest of five positive zero gaps.
- The resulting exact support cut is `U5=floor(4A/5)`.
- The determinant-window count is retained in the mixed bound `5*3^(7+r)*2^(U5-r)` rather than discarded.

## Infinite coverage

- The promoted normalized constant is deliberately enlarged to `C0=5*3^(15/2)` by dropping a favorable factor.
- Non-bracketing determinant-one pairs are excluded for `A>=1713`.
- Bracketing pairs use the exact Stern-Brocot path around `log(3)/log(2)`.
- The exact path verifier maintains the integer comparisons `2^n ? 3^d` incrementally; branch decisions are not floating-point decisions.
- The audited RL238 LMN theorem is reused only with its inherited hypotheses.
- The bracketing cutoff is `A<=690205`; large-`A` re-entry is excluded by the inherited safe `M` upper-bound/derivative argument.
- The exact mixed-size survivor list has 2,234 determinant pairs and maximum `A=690`.

## Cyclic order / orientation

For `kappa=+1`, the five singleton components contain three positive and two negative signs. Up to cyclic rotation there are exactly two sign necklaces:
1. negative components adjacent;
2. negative components separated.

No reflection quotient is required. The independent `A<=18` replay checks both orientations and gives exact symmetry 4,498 / 4,498.

## Full D / proper factor

- Every theorem hit test retains the complete positive `D=2^A-3^L`.
- The independent replay finds 714 instances where the numerator difference shares a nontrivial proper factor with `D` but is not divisible by full `D`.
- None of those 714 is counted as a theorem hit.
- Full-`D` hits: 0.

## Numerator indexing / cyclic cut

On every one of the 4,498 small-range `kappa=+1` instances, the replay cuts after a zero-flow edge, recomputes the ordinary prefix discrepancy, reconstructs the exact five-edge numerator difference and compares it with direct `Q(tau^m x)-Q(x)`.

Mismatches: 0.

## Determinant identity

All 8,996 small-range `|kappa|=1` instances satisfy the correct signed relation `qA-mL=kappa`.

Mismatches: 0.

## Primitive / nonprimitive

Primitivity is not used as a filter in the promoted determinant-pair reduction. The reduction therefore does not silently discard nonprimitive repetitions.

## Negative domain

The inherited sentinel

`A=11,L=7,D=-139,Q=18904`

is retained as a scope regression and remains outside the promoted `D>1` theorem.

## Deliberate non-claim

The exact finite cover contains a naive 618,391,058,390 two-order gap configurations. RL269 does not claim these have been exhausted. Any RL270 compression (including an alternation/interlacing argument from `x_i-x_(i+m)=g_i-g_(i-1)`) must be proved before it is used as a certificate filter.

Result: **PASS for the promoted finite reduction**.
