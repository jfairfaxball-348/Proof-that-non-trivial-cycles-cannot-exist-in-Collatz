# RL268 mandatory red team

Date: 2026-09-06

## Coverage

- All four cyclic sign orders of `[2,1,1,1]` are enumerated after anchoring the unique length-two component.
- Every zero-flow gap is required nonempty; all positive four-part compositions of `A-5` are enumerated.
- The complete finite size cover contains 967 determinant pairs and is generated independently by the analytic verifier.
- Bracketing coverage is an exact Stern-Brocot traversal using integer comparisons `2^n ? 3^d`, not floating-point branch decisions.

## Full `D` / numerator

- Every theorem test is divisibility by the entire positive `D=2^A-3^L`.
- No proper divisor is substituted.
- The complete certificate evaluates the exact five-edge residue after reconstructing a binary word from the flow recurrence.
- Independent brute force through `A<=18` evaluates `Q(tau^m x)-Q(x)` directly and obtains zero full-`D` hits.
- The same brute force records 1,608 proper-factor-only numerator-difference instances, confirming that a nontrivial gcd is not a theorem hit.

## Orientation and cyclic cut

- Main finite enumeration is oriented to `kappa=+1`.
- Independent brute force checks both orientations and obtains exact symmetry 10,798 / 10,798.
- The edge identity is checked only after rotating to a legal zero-flow cut; the corrected check has zero mismatches.

## Primitive / nonprimitive

Primitivity is not used as a finite-certificate filter. Therefore omitted nonprimitive repetitions cannot create a false closure; the certificate is stronger than the written primitive theorem scope.

## Negative domain

The permanent sentinel is reproduced exactly:
`A=11,L=7,D=-139,Q=18904`.
It is outside the promoted `D>1` scope.

Result: **PASS**.
