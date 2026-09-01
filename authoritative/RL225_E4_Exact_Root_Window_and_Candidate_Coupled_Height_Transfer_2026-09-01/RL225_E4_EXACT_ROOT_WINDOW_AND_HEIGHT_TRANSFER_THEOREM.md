# RL225 e=4 exact root window and candidate-coupled height transfer theorem

Date: 2026-09-01.

All statements remain conditional on the sole inherited high branch and on a physical H21 realization. A necessary arithmetic candidate is not a physical occurrence or charge.

## RL225-T1 — exact finite e=4 root bridge

RL211 proves that the only surviving e=4 absolute prefix has

- `a_0..a_3 = 1,2,1,1`;
- `h_0..h_4 = 0,0,0,0,1`;
- affine numerator `Q=85`;
- `eta = 207 (mod 243)`.

Write `eta=207+243 k`. RL211 also gives

`y_4 = 2^34 eta - 1 - 3^4*2^32`,

`2^5 y_4 = 3^4 y_0 + 85`.

Substitution therefore gives the exact root progression

`y_0 = 1,267,492,570,907 + 1,649,267,441,664 k`

with step `1,649,267,441,664 = 3*2^39`.

RL214/RL215 prove the global H21 root sandwich

`24,913,843,845,551,577,787,381 <= y_0 <= 31,285,589,992,934,194,300,574`.

Intersecting the progression with this interval gives exactly

`15,106,005,985 <= k <= 18,969,385,559`,

hence exactly **3,863,379,575** arithmetic e=4 roots. The first and last roots are

- `24,913,843,845,909,514,929,947`;
- `31,285,589,992,097,449,101,083`.

This is a gap-free finite parameterization for the inherited e=4 necessary terminal rank **31,435,476,727**. No e=16 parameterization is used.

## RL225-T2 — exact terminal-Hensel deletion inside the e=4 window

The inherited terminal condition forbids `nu>=22`, equivalently

`s = (3^34)^(-1) (mod 2^22) = 1,893,305`.

Since `eta=207+243k`, eta is odd exactly when k is even. Applying the inherited parity/orientation definition of s gives exactly two forbidden k cylinders:

- `k = 801,774 (mod 2^22)` on the odd-eta branch;
- `k = 1,785,623 (mod 2^22)` on the even-eta branch.

Each cylinder meets the finite k interval in **921** points. Therefore the terminal-Hensel condition removes exactly **1,842** candidates and leaves **3,863,377,733**.

## RL225-T3 — exact candidate-coupled height contraction through transition 41

Starting at the exact root coordinate above, the accelerated odd trajectory is deterministic. For every k in the finite window, the transition exponents are fixed through transition 35:

`a_0=1`, `a_1=2`, `a_2=...=a_34=1`, `a_35=2`.

At phase 36 this gives

`h_36=19`,

`y_36 = 900,567,811,781,994,726 k + 692,103,040,536,162,613`.

The portable verifier then partitions the full finite k interval into exact dyadic cylinders. On each cylinder it applies only the mandatory recurrence

`a_i=v2(3y_i+1)`,

`y_(i+1)=(3y_i+1)/2^a_i`,

`h_(i+1)=b_(i+1)-b_i+h_i-a_i`,

and rejects exactly when the next height is negative. The gap-free failure counts are:

| transition | newly failed |
|---:|---:|
| 36 | 3,684 |
| 37 | 18,422 |
| 38 | 105,924 |
| 39 | 203,794 |
| 40 | 713,558 |
| 41 | 943,078 |

Thus **1,988,460** candidates fail the mandatory height condition by transition 41, leaving **3,861,391,115** before the terminal filter.

The verifier directly replays every one of the 1,842 terminal-Hensel-forbidden candidates and proves that none has failed the height recurrence by transition 41. The two deletions are therefore disjoint at this certified depth. The combined exact remainder is

**3,861,389,273 candidates**.

## Scope

RL225 constructs and contracts the exact e=4 candidate family but does not empty it. Terminal rank **31,435,476,727 remains live**. The necessary-rank counts therefore remain:

- above-p: **7,091,831,283**;
- below-p: **6,324,034,587**;
- total: **13,415,865,870**.

Physical H21 incidence/charge, whole-branch contradiction, Gate A, Gate B, and global nontrivial-cycle exclusion remain open.
