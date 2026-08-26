# RL110 — sparse-diameter baseline and support-selection barrier

Date: 2026-08-26

## Scope and classification

Assume a hypothetical primitive positive ordinary shortcut cycle. Let its parity word have `A=L+Z`, with `L` odd and `Z` even symbols, put `D=2^A-3^L>0`, and write `rho=3^L/2^A`.

RL109 supplies distinct owned rotations, a common zero-flow cut, and a minimum fixed-cut adjacent-swap path of length `R=R_*` such that

`0 != S=Q(v)-Q(u)=sum_j epsilon_j 2^(a_j)3^(b_j)` and `D|S`.

This report studies the complement `R>=4`. Its new statements are analytic numerator/support bounds and a method barrier. It proves no Gate closure, no nontrivial-cycle exclusion, and no Collatz result.

## Exact fixed-content diameter

Use `Q(w)=sum_(i:w_i=1) 2^i 3^(# ones strictly after i)`. An adjacent `10 -> 01` swap at position `i` with `t` ones on its right increases `Q` by `2^i3^t>0`. These swaps connect all fixed-content words, so their extrema occur at `1^L0^Z` and `0^Z1^L`:

`3^L-2^L <= Q(w) <= 2^Z(3^L-2^L)`.

Every fixed-content pair, and therefore every rotation pair, obeys

`|Q(v)-Q(u)| <= B(A,L):=(2^Z-1)(3^L-2^L)`.                 (1)

This is sharp over arbitrary fixed-content pairs; no claim says the extremizers are rotations of one word.

## Maximum single support coefficient

For a legal swap at position `i` with `t` ones right of it, the paired zero and those `t` ones occur afterwards. Hence `i+t+2<=A` and `t<=L-1`, giving

`2^i3^t <= 2^(A-t-2)3^t <= M(A,L):=2^(Z-1)3^(L-1)`.       (2)

Equality is attainable in elementary word geometry. Since the RL109 sparse difference has exactly `R` signed terms,

`|S| <= R M(A,L)`.                                         (3)

Thus the current purely geometric baseline is

`|S| <= U(A,L,R):=min(B(A,L),R M(A,L))`.                   (4)

It is independent of the tautology `S=D(x_v-x_u)`.

## Radius-three complement obstruction

RL109 gives `R_*<=min(L,Z)`, so `R>=4` forces `L,Z>=4`. Division by `D` yields

`B/D = (1-2^(-Z))*((3/2)^L-1)/(1-rho)`,

`R M/D = R*(3/2)^L/(6*(1-rho))`.

As `0<rho<1`, the live complement has

`B/D > (15/16)*(81/16-1)=975/256`,

`R M/D > 4*(3/2)^4/6=27/8`.

Therefore `U/D>27/8`. This is not a lower bound on `|S|`; it proves only that fixed-content diameter and termwise support bounds cannot show `|S|<D`. The obstruction is the admissible coefficient scale

`M/D=(3/2)^L/(6*(1-rho))`.

Any continuation needs an actual-owned support restriction or physical-strip bound, not a bound valid for all legal swaps.

## Mandatory red teams

### RL20 — PASS as discriminator

The inherited exact radius-four local fake has `Q mod D` nonzero. Its minimum radius-four sparse difference is larger than `D`; it confirms that local geometry cannot supply compression, but it is not treated as an owned cycle.

The small primitive word `00010111` has `(A,L,D)=(8,4,175)`, minimum rotation radius four, and maximum legal support `M=216>D`; every radius-four rotation difference exceeds `D`. Yet its `Q=824=124 (mod 175)`. This is a geometry-only red team, not an ordinary-owned counterexample.

### RL79, RL81, primitivity, raw scope, external input — PASS

For generalized increment `s`, numerator differences scale by `s` and only `D|sS` is available; no `s` is cancelled. No quotient is called physical absent full ownership. Primitivity remains load-bearing for distinct states and `S!=0`. Neither a raw/Farey restriction nor an external least-cycle floor is used.

## Exact finite red team (strictly finite)

`verification/scan_rl110_pairwise_divisibility.py` exhausts primitive canonical necklaces of lengths `8..17`, with `D>1` and `R_*=4`, checking every closest rotation pair. It checks 1,580 necklaces and 27,866 pairs and finds no `D`-divisible pair. This is a gap-free certificate for that finite scope only; it neither proves a global theorem nor licenses a larger scan.

## RL110 outcome

RL110 establishes the first-milestone barrier: unconditioned geometry and termwise support cannot compress the RL109 sparse multiple below `D` on the radius-three complement. The desired ordinary-owned support-selection theorem remains open. Do not resume generic radius-four casework, local grammar, normalized coboundaries, or bulk cascade scanning.
