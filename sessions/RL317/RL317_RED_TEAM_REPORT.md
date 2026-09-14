# RL317 red-team report

Date: 2026-09-14
Status: PASS

## Scope and factor ownership

1. The composition theorem uses genuine `D0|U+V` and `H|U-V` in distinct
   roles. `D0` ownership alone does not reduce the remaining factor to
   `epsilon mod H` unless the physical boundary states are integral.
2. No local segment denominator ownership is inferred.
3. The late and early one-row shadows remain rational. Only their full
   concatenation is declared an integer cycle when `D|Q` is proved.
4. `q_sigma/D0<R` is not used as a leastness contradiction.

The first composition harness deliberately failed when it tested the final
equivalence with only `D0` ownership. The test was repaired to include the
inherited physical `H` premise. This was a verifier-premise defect and is now
an explicit red team.

## Descent and primitivity

When `epsilon=kH>0`, positivity is exact and the new lower fixed state is
`R-k>0`. A repetition count for the length-`2a`, weight-`2ell` word divides
two. Repetition twice would make `tau=sigma`, contradicting their positive
numerator gap. Thus descent stays in primitive `g=2`; no cross-multiplicity
minimality is assumed.

At `epsilon=0`, the conclusion is only rankwise ordered rows. RL21's frozen
`(65,41)` model has exactly this saturation but fails `D0` ownership, so row
repetition is not asserted.

## Rational/integer mismatch

The mismatch theorem is a 2-adic parity statement for an odd-denominator
rational shadow and a neighboring positive integer. It does not assert that
the smaller integer converges, belongs to the physical cycle, or contradicts
leastness. The boundary case `v2(r)=a` is separately audited and forces `r=X`.

## Generalized-increment barrier

The content computation proves exactly
`gcd(D,Q(tau sigma))=D0 gcd(H,epsilon)`. The resulting increment is
`h=H/gcd(H,epsilon)`. RL79 is applied only after this equality. Homogeneous
`T_h` invariants are explicitly rejected as ownership tests; the remaining
cross-content coupling is open.

## First-fibre certificate

1. Coverage is gap-free: exactly 190,497 integer `ell` values from 41 through
   190537.
2. All logarithmic decisions use exact rational enclosures; floating-point is
   never used for certification.
3. The saved JSON certificate matches the regenerated object and its sidecar.
4. The cap `9,355,556` uses the already-frozen RL131 descent certificate
   through `23,506,639,475`; the expensive descent scan is accepted under
   verification economy.
5. RL315's claimed run through `19,671,092,983` is not promoted. It is
   mathematically superseded by RL131's larger certified range.
6. The exact first-fibre ceilings do not themselves exclude the fibre.

## Global scope

The bounded row regressions are not global certificates. `g=1` is separate.
Gate A, Gate B, and global positive non-trivial-cycle exclusion remain open.
No Collatz conjecture claim is made.

## Required verifier commands

```sh
python3 -I verification/verify_rl317_dual_shadow_composition.py
python3 -I verification/verify_rl317_cofactor_mismatch.py
python3 -I verification/verify_rl317_generalized_increment_reduction.py
python3 -I verification/verify_rl317_first_reduced_fibre.py
```

All must pass in the candidate and again after clean fresh unpack.
