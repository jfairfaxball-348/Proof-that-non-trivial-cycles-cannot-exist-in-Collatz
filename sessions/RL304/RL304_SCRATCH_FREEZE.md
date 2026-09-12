# RL304 scratch freeze

Date: 2026-09-12
Status: NON-AUTHORITATIVE DERIVATIONAL STATE

This file preserves useful exploratory work from RL304 that is not promoted unless restated in the report/proof ledger.

## A. Exact finite whole-stack witnesses

For `C_n=Q^(n-1) o P o Q` and `T_n=Q^n o P`, exact physical witness words found were:

| n | word | length | cost |
|---:|---|---:|---:|
| 1 | `01110` | 5 | 14 |
| 2 | `00101110001` | 11 | 53 |
| 3 | `010011111001001001` | 18 | 127 |
| 4 | `100011101110111000001` | 21 | 187 |
| 5 | `100001110101010000001110` | 24 | 260 |
| 6 | `0110100000111110110010001` | 25 | 339 |
| 7 | `1001111100110001100001010110` | 28 | 413 |

These are replayable certificates, not an all-n language theorem. Search for `n=8` hit a state/resource limit before producing a result and is not a negative statement.

## B. Q-return-compositional witnesses

A stronger structural search constrained outer Q factors to return physically before emitting the residual commute. Exact witnesses:

| n | word | length | cost |
|---:|---|---:|---:|
| 1 | `01110` | 5 | 14 |
| 2 | `00101110001` | 11 | 53 |
| 3 | `001011000111101010001` | 21 | 143 |
| 4 | `000011010100100011111100100` | 27 | 249 |
| 5 | `011010001000110110000111110001001` | 33 | 373 |
| 6 | `101110000011001110010101101100100101011100` | 42 | 582 |

For n=2:
- outer `Q` returns to `Q` on input `00101110001`;
- it emits `01001101001`;
- the residual `P o Q` reaches `Q o P` on that emitted word.

For n=3 the same compositional principle succeeds with a longer outer-Q return. These examples motivated, but are superseded analytically by, the fixed-96 theorem.

## C. Failed recurrence

The n=3,4,5 compositional data suggested

`length=6n+3`

and

`cost=9n^2+43n-67`.

The n=6 witness is length 42, cost 582, while that extrapolation predicts 39 and 515. Treat the guessed recurrence as false/unsupported.

## D. Fixed-defect discovery

Direct cascade algebra showed the target minus source K-coordinate is exactly 96 for every stack height. This became promoted theorem in the report.

The key lesson for future resumption is: do not search witness words first. Work on the fixed translation pair `C_n` / `C_n o H_96`.

## E. Six-column residual first-step table

The promoted residual factors are

`F_m=(1,3(3^m+1)/2)`,
`G_m=(1,3(1-3^m)/2)`.

Their immediate formal/canonical one-column successors are:

| m | F_m | F_m on 0 | F_m on 1 | G_m | G_m on 0 | G_m on 1 |
|---:|---|---|---|---|---|---|
| 1 | `(1,6)` | `(1,4)` | `(1,9)` | `(1,-3)` | `(2,0)` | `(0,-2)` |
| 2 | `(1,15)` | `(2,27)` | `(0,7)` | `(1,-12)` | `(1,-5)` | `(1,-18)` |
| 3 | `(1,42)` | `(1,22)` | `(1,63)` | `(1,-39)` | `(2,-54)` | `(0,-20)` |
| 4 | `(1,123)` | `(2,189)` | `(0,61)` | `(1,-120)` | `(1,-59)` | `(1,-180)` |
| 5 | `(1,366)` | `(1,184)` | `(1,549)` | `(1,-363)` | `(2,-540)` | `(0,-182)` |
| 6 | `(1,1095)` | `(2,1647)` | `(0,547)` | `(1,-1092)` | `(1,-545)` | `(1,-1638)` |

Rows ending at depth zero are formal wall hits, not physical continuations. RL295 normalization must be used before any future attempt to price them.

The immediately notable physical sinks are:
- `F_1 --1--> 8`;
- `F_2 --0--> R3`.

No broader ownership claim is made.

## F. 2-adic / residue observations

The special source family `C_n` has structured residues modulo powers of two, and bounded searches suggested that short translation words depend on such residue information. No residue-period theorem or finite automaton was completed. This is an optional resumption lead only.

## G. Strategic warning

RL304 is the latest instance of a pattern that may or may not be genuine convergence:

`global obstruction -> exact coordinates -> local normal form -> finite residual`.

The successor audit is explicitly tasked with deciding whether this sequence has objectively reduced Gate-A complexity or merely repackaged it.
