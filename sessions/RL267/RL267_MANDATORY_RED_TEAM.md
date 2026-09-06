# RL267 mandatory red team

Date: 2026-09-06

## Coverage checks

- Full determinant-one size cover recomputed from `qA-mL=1`, `D>1`, `gcd(A,L)=1` and the exact normalized edge bound.
- Total size-surviving pairs: 2,683; structural-capable `A>=8` pairs: 2,673.
- Exact Stern-Brocot traversal uses integer comparisons `2^A ? 3^L`, not floating-point branch decisions.
- `[3,1,1]` covers the unique cyclic order up to exchange of its identical singleton negative components.
- `[2,2,1]` explicitly covers both distinct cyclic component orders after anchoring the positive length-two component.

## Full-D / numerator checks

- Every finite theorem test is `delta % D == 0` against the entire positive `D=2^A-3^L`.
- No proper divisor of `D` is substituted.
- Direct word reconstruction checks the exact five edge monomials.
- Independent whole-certificate implementations reconstruct the bit state by a different residue-event method and reproduce zero full-`D` hits.
- Small-range direct `Q(tau^m x)-Q(x)` checks agree with the edge identity.

## Primitive / nonprimitive

Primitivity is not used as a finite-certificate filter. Therefore a missed nonprimitive repetition cannot create a false closure; the finite certificates are stronger than the written primitive theorem scope.

## Orientation / cyclic wrap

- Main finite certificates orient to `kappa=+1`.
- Independent brute-force replay through `A<=18` checks both orientations and obtains exact positive/negative symmetry:
  - `[3,1,1]`: 2,572 / 2,572;
  - `[2,2,1]`: 5,146 / 5,146.
- `[2,2,1]` canonical positive small-range count is exactly 165 per cyclic component order.

## Domain sentinel

The inherited negative-domain regression is reproduced exactly:
`A=11,L=7,D=-139,Q=18904`.
It is outside the promoted `D>1` scope.

Result: **PASS**.
