# RL268 mandatory red team

Date: 2026-09-06

## Four-component bound

- RL267's three-component support constant is not reused.
- `[2,1,1,1]` is re-cut at a longest of four positive zero gaps.
- The resulting bound is `U4=floor((3A+1)/4)`.
- The naive replacement of RL267's old support estimate is insufficient in the worst `m≈A/2` regime.
- The promoted reduction instead uses the exact determinant-window count `r`, producing the mixed bound `5*3^(7+r)*2^(U4-r)`.

## Infinite coverage

- Non-bracketing determinant-one pairs are excluded for `A>=375`.
- Bracketing pairs use the exact Stern-Brocot path around `log(3)/log(2)`, with branch decisions made by integer comparisons `2^n ? 3^d`.
- The audited RL238 LMN theorem is reused only with its inherited exact hypotheses.
- The bracketing cutoff is `A<=163052`; large-`A` re-entry is excluded by the same safe `M` upper-bound/derivative argument as RL266.
- The exact mixed-size survivor list has 967 determinant pairs and maximum `A=174`.

## Cyclic order / orientation

For `kappa=+1`, all four anchored sign/order cases are enumerated:
1. positive length two, singleton signs `+,-,-`;
2. positive length two, singleton signs `-,+,-`;
3. positive length two, singleton signs `-,-,+`;
4. negative length two, singleton signs `+,+,+`.

The independent `A<=18` replay checks both orientations and gives exact symmetry 10,798 / 10,798.

## Full D / numerator indexing

- Every theorem hit test uses the complete positive `D=2^A-3^L`.
- No proper divisor is substituted.
- The edge formula is applied only after a zero-flow cut.
- Independent small-range direct numerator replay reports zero edge-identity mismatches after that cut.

## Primitive / nonprimitive

Primitivity is not used as a finite-certificate filter. A nonprimitive candidate therefore cannot be omitted by the certificate.

## Negative domain

The inherited sentinel

`A=11,L=7,D=-139,Q=18904`

is retained as a scope regression and remains outside the promoted `D>1` theorem.

Result: **PASS**.
