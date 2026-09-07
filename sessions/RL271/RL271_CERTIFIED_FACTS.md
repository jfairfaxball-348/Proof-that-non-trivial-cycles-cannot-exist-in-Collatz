# RL271 certified facts

Date: 2026-09-07

Classification: **RADIUS5_KAPPA3_FLAT_SECTOR_CLOSED_HEIGHT2_MASS4PLUS1_OPEN**.

RL271 works in the inherited positive-domain Radius-5 `|kappa|=3` sector. It orients to `kappa=+3` by exact source/target reversal; the opposite orientation is thereby covered without a median-sign assumption.

Promoted flat-leaf results:
- `[4,1]`: **CLOSED**. Exact reconstruction gives 10,762 binary structural states over `A=8..56`, of which 7,748 have positive `D`; zero full-`D` hits. The positive states split `gcd(A,L)=1/3` as 5,909 / 1,839 and `gcd(m,A)=1/3` as 6,296 / 1,452. The corrected exponent estimate is `L-v <= (A-u)+2`; the stronger naive `L-v<=A-u` is false.
- `[3,1,1]`: **CLOSED**. The exact three-component determinant cover has 3,514 structurally capable tuples, including 77 restored `q=L` endpoints, maximum `A=335`. Across two cyclic sign orders there are 69,057,294 gap/order configurations and 6,857,644 binary states, split 3,428,822 / 3,428,822, with zero full-`D` hits. Endpoint states: zero.
- `[2,2,1]`: **CLOSED**. On the same corrected 3,514-tuple cover, one anchored cyclic order gives 34,528,647 gap configurations and 3,302,985 binary states, with zero full-`D` hits. Endpoint states: zero.
- `[2,1,1,1]`: **CLOSED**. A topology-specific four-component cut gives `U4=floor((3A+1)/4)` and the determinant-three mixed bound. The exact finite cover has 1,332 structurally capable tuples, maximum `A=195`, including 90 `q=L` endpoints. Three cyclic orders give 182,221,338 gap/order configurations and 9,673,883 binary states, split 3,198,979 / 3,275,925 / 3,198,979, with zero full-`D` hits. Endpoint states: zero.
- `[1,1,1,1,1]`: **CLOSED**. A five-component cut gives `U5=floor(4A/5)`. The determinant-three finite cover has 3,009 tuples, maximum `A=650`, with `gcd(m,A)=1/3` split 2,255 / 754 and 112 `q=L` endpoints. Exact boundary-event compression gives 7,839,862,799 structural states: 6,583,755,516 in the gcd-one sector and 1,256,107,283 in the gcd-three sector. Complete sparse modular certificates use 13,640,991 primary side entries and 11,626,528 independently split alternate side entries; both have zero structurally admissible low-64 residue collisions and hence zero full-`D` hits.

General determinant-three facts promoted in this generation:
- `qA-mL=3`, hence `gcd(A,L)` and `gcd(m,A)` divide 3;
- the determinant-window identity is valid in this sector in the form `W_i(m)=q-g_(i-1)`;
- proper factors of `D` are never substituted for the complete positive `D=2^A-3^L`;
- no primitivity filter is used in any finite certificate.

Independent direct-word replay through `A<=18` gives, by flat topology:
- `[4,1]`: 4,798 raw instances, 2,399 / 2,399 orientations, zero full-`D` hits;
- `[3,1,1]`: 14,672 raw, 7,336 / 7,336, zero hits;
- `[2,2,1]`: 6,736 raw, 3,368 / 3,368, zero hits;
- `[2,1,1,1]`: 16,632 raw, 8,316 / 8,316, zero hits;
- `[1,1,1,1,1]`: 4,354 raw, 2,177 / 2,177, zero hits.

The negative-domain sentinel `A=11,L=7,D=-139,Q=18904` is reproduced and remains outside the positive-domain theorem scope.

**Not closed:** the inherited height-two mass-four-plus-one `|kappa|=3` family. Therefore the complete `|kappa|=3` sector is not yet closed. `|kappa|=5` remains frozen.
