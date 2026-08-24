# RL-11 Roadmap Update — 2026-08-20

## Rank 1 — same-direction coprime one-orbit branch

The mixed branch is closed and should not be revisited.

For `e=+3`, `gcd(A,L)=gcd(A,m)=1`, combine:

- RL-L67: `sigma^a+3sigma^b+9sigma^c=0 (mod D)`;
- RL-L74: the three negative events generate three equal `r`-arcs, with cover multiplicity exactly `{j,j+1}` where `3r=L+jA`.

Goal: turn the arbitrary three times `a<b<c` into a canonical gap region analogous to RL-L68, then test a resultant/linear-forms barrier.

## Rank 2 — `gcd(A,m)=3` three-orbit same-direction branch

Derive the orbitwise analogue of RL-L74/RL-L67. Determine whether each rotation orbit contributes exactly one negative jump and whether the three orbit sums combine into a cubic norm.

## Rank 3 — `gcd(A,L)=3` cubic cofactor

Write `A=3a`, `L=3ell` and

`D=(2^a-3^ell)(2^(2a)+2^a3^ell+3^(2ell))`.

Target theorem: a primitive radius-3 same-direction survivor cannot be supported by the cubic cofactor. The only finite survivor from RL-10 is `(10)^3`, where the shorter denominator is `1`; aim to prove cofactor divisibility forces exact third-repetition.

## Rank 4 — distinguished-rotation route

If same-direction radius 3 resists complete arithmetic closure, return to the inherited least-state/root-return rotations and use their prefix/suffix envelopes to exclude radius 3 specifically for the distinguished rotations required by RL.

## Guardrails

- RL remains open.
- Radius 3 is now closed only for the mixed branch and the connected `[3]` branch.
- RL-L73 depends on the published Laurent–Mignotte–Nesterenko two-logarithm estimate plus the included exact finite certificate.
- Do not re-enumerate generic mixed three-edge paths.
