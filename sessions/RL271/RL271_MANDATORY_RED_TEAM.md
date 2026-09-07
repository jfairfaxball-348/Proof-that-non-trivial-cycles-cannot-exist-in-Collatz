# RL271 mandatory red team

Date: 2026-09-07

Result: **PASS** for the promoted flat `|kappa|=3` closures.

## Orientation
`kappa=-3` is covered by exact source/target reversal: `m' = A-m`, `q'=L-q`, and the flow changes sign. Distance, topology, and full-`D` divisibility are preserved. The independent `A<=18` replay gives exact orientation symmetry in all five flat families.

## Determinant endpoints
The early scratch scan's `q<L` restriction was rejected. Exact covers use `1<=q<=L`. Restored `q=L` endpoint tuples are retained in every relevant certificate and reconstruct to zero structural states.

## gcd-three sectors
No determinant-one coprimality is assumed. `gcd(A,L)` and `gcd(m,A)` may be 3. The finite solvers explicitly include one-cycle and three-cycle reconstruction. Large gcd-three state populations are present in every multi-component certificate, so this is not a vacuous regression.

## Full D versus proper factors
All theorem hit tests use the complete positive `D=2^A-3^L`. The direct replay exhibits proper-factor-only false positives while full-`D` hits remain zero. In particular the all-flat `A<=18` replay records proper-factor-only counts 514, 2,116, 718, 2,294, and 614 for `[4,1]`, `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, and `[1,1,1,1,1]` respectively. For `[3,1,1]` this is 1,058 in each orientation.

## Cyclic order and wrap
Every anchored sign/order family required by the flat topology is enumerated without using a reflection quotient:
- `[3,1,1]`: two orders;
- `[2,2,1]`: one order;
- `[2,1,1,1]`: three orders;
- singleton: all feasible boundary-event matching families in gcd one plus the separate gcd-three residue-row reconstruction.
Orbit-weighted small-range anchored counts reproduce the independent raw-word counts.

## Numerator indexing
The direct replay applies the five-edge identity only after a zero-flow cut and reports zero edge-identity mismatches. The singleton replay additionally checks the sparse modular polynomial exactly modulo `D`, including all small gcd-three words.

## Negative domain
The permanent sentinel `A=11,L=7,D=-139,Q=18904` is reproduced and excluded by the promoted positive-domain hypothesis.

## Primitivity
No finite certificate filters candidates by primitivity. The promoted zero-hit statements are therefore not artifacts of a primitive-word prefilter.
