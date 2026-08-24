# RL47 Proof State and Progress

Date: 2026-08-22

## Status legend

- **Analytic**: exact symbolic consequence of the retained one-excursion automaton and inherited prefix-cap hypotheses.
- **Exact finite certificate**: exhaustive finite computation with explicitly stated conservative relaxations/pruning.
- **Regression evidence**: independent agreement with previously certified cases.
- **Partial computation**: informative only; not a theorem.
- **Open**: not proved.

## 1. Inherited target

RL46 reduced the live one-excursion excess statement to

`H >= t+3 = v2(T+1)`, where `H=e-z+1=sum(d-1)` and terminal geometry satisfies `q=z+t`.

Thus `e>=q+2` is exactly equivalent to the terminal area/valuation inequality.

RL46 also restored the genuine prefix cap

`2^(n+2) 3^(2 ell) <= 3^(p_alpha+2) 2^(2a)`

for actual retained prefixes, and showed `t` is even and `t>=2` in the retained near-resonant window.

## 2. Cap-death monotonicity — ANALYTIC

Define the exact cap ratio

`R = 3^(p_alpha+2) 2^(2a) / (2^(n+2) 3^(2 ell))`.

Under a transition:

- `x=0` sends `R -> R/2`;
- `x=1` sends `R -> 3R/2`;
- an `x=1` edge is cap-legal only when the current cap requirement is met.

Therefore, once `R<1`, no future `x=1` can be used to restore the cap and every `x=0` makes the ratio smaller. A cap-legal terminal can never be reached from such a state.

This proves that pruning every state with failed current prefix cap is sound, even though older formulations tested the cap only at moved-rank edges.

## 3. Exact phase coordinate — ANALYTIC

Define

`Phi = 2^n (T + 3^d - 1) / 3^(p_alpha+d)`.

For an edge `(x,y)` the exact increment is

`Delta Phi = (2^n / 3^p_alpha) * ((1-x) - (1-y)/3^d)`.

Consequences:

- every neutral `11` edge has `Delta Phi=0` exactly;
- the canonical start has `Phi=-8`;
- at a genuine terminal with `k=t+3` and `zeta=2^a/3^ell`,

  `Phi_terminal = 9 zeta (1+2^-k)`.

The verifier `verify_rl47_phase_coordinate.py` checks the transition identity column-by-column on the audited `(65,41)` minimum-excess witness and checks the exact terminal formula.

This coordinate removes the troublesome neutral `11` direction algebraically rather than by an ad hoc virtual pump.

## 4. Fixed-t future-hull certificate — ANALYTIC PRUNING + EXACT FINITE SEARCH

For fixed even `t`, a strict counterexample must terminate at the unique value

`J_terminal = T+1 = 2^(t+3)`

with terminal zero count `z=q-t` and area budget

`H <= t+2`.

Two exact monotone restrictions follow:

1. `z <= q-t` throughout a candidate path;
2. from current height `d`, returning to terminal height one costs at least

   `d(d-1)/2`

   additional area, so a state is dead if

   `H + d(d-1)/2 > t+2`.

The verifier computes backward, from the single terminal `J`, a conservative interval hull of possible predecessor `J` values. Parity and division-by-3 divisibility are deliberately relaxed by floor/ceiling enlargement. Therefore the hull can keep impossible states but cannot delete a genuine violating path.

The forward search then enforces exact parity, exact integral transitions, exact prefix cap, exact `T/J`, minimum-`H` dominance at identical future-relevant state, and the conservative future hull.

### q=79 result

For `(a,ell,q)=(214,135,79)` every even `t=0,2,...,78` is exhausted. `t=0` fails the exact terminal cap; for the remaining values no strict terminal violation is found.

Recorded summary:

- `any_violation 0`;
- total retained fixed-t states: `16,862,654`;
- maximum single layer: `76,688`;
- conservative future-hull prunes: `1,133,779`.

Hence:

**Exact finite certificate:** the q=79 pair has no retained prefix-cap terminal geometry with `H<t+3`.

This upgrades RL46's partial q=79 computation to a completed exact certificate.

### Regression cases

The same arbitrary-precision implementation agrees with q=17, q=24, and q=55. In particular q=55 returns `any_violation 0` with only `245,609` retained states, independently reproducing the older much larger DP conclusion.

## 5. Rank-transport identity — ANALYTIC

Let `a_j` be the zero-based column of the j-th `x=1` transition and `b_j` the zero-based column of the j-th `y=1` transition. Prefix positivity gives

`b_j <= a_j`.

The area is exactly

`H = sum_j (a_j-b_j)`.

Thus `H` is literally total displacement between matched moved ranks.

Unrolling the exact `T` recurrence gives, with `r=ell-3`, `k=t+3`, and `m=a-k-1`,

`2^m T_m = -14*3^r + sum_{j=1}^r 3^(r-j) (3*2^a_j - 2^b_j)`.

At terminal `T_m=2^k-1`. Normalizing gives the exact identity

`14 + (27/2) zeta (1-2^-k)`

`= sum_{j=1}^{ell-3} (2^a_j / 3^j) * (3 - 2^-(a_j-b_j))`.

The `(65,41)` audited witness satisfies `H=sum(a_j-b_j)=104` and both the integer and normalized identities exactly.

## 6. Relaxed rank-transport upper bound — ANALYTIC

At the j-th moved rank, the exact prefix cap gives

`2^(a_j+3) 3^(2 ell) <= 3^(j+1) 2^(2a)`.

Also, strict ordering of moved ranks and the finite terminal length force coordinatewise room bounds on `a_j`.

Under a hypothetical strict violation, `sum(a_j-b_j)<=t+2`. The normalized rank-position right side is monotone in each `a_j` and concave in each displacement `delta_j=a_j-b_j`.

RL47 therefore enlarges the admissible class by:

- replacing the true coupled `a_j` values by their coordinatewise cap/room upper envelope;
- retaining only the total displacement budget;
- distributing that budget by the exact decreasing marginal gains of the separable concave relaxation.

If this enlarged maximum is still below the exact terminal left side, a genuine strict violation is impossible.

The rational-arithmetic verifier proves:

- `(46,29,17)`: every admissible even `t=2..16` excluded analytically;
- `(65,41,24)`: every admissible even `t=2..22` excluded analytically;
- `(149,94,55)`: every even `t>=32` excluded analytically;
- `(214,135,79)`: every even `t>=60` excluded analytically;
- `(363,229,134)`: every even `t>=116` excluded analytically.

This is the strongest cutoff-free analytic compression obtained in RL47.

## 7. Height-one macro and residue stress test — EXACT FINITE CERTIFICATE

At height one with odd `J`, exactly one of `00` and `11` keeps the next `J` odd while the other produces the even exit. Hence a zero-area height-one segment is a deterministic continuation orbit with an option to exit at each step, not a genuine binary tree.

`verify_fixed_t_hull_budgetres64.cpp` quotients these runs into exact macro traversal and adds a conservative future residue sieve modulo 64. The residue dynamic relaxes divisibility when needed, so it can retain false possibilities but cannot remove a genuine violating path.

For the next stress pair `(363,229,134)` the exact verifier excludes strict violations for

`t=2,4,6,8,10,12,14,16`.

The `t=16` run retained about `3.89 million` states and returned `hit 0`.

Combined with the analytic high-t rank bound, the currently unresolved q=134 strip is

`18 <= t <= 114`, `t` even.

No t=18 attempt completed to an independently trusted certificate in RL47. Do not promote the t=18 scratch/partition experiments.

## 8. Updated proof ledger

### Analytic

- all inherited RL46 analytic identities, subject to their inherited hypotheses;
- cap-death monotonicity;
- exact `Phi` coordinate and neutral-`11` cancellation;
- exact terminal `Phi` identity;
- exact rank displacement identity `H=sum(a_j-b_j)`;
- exact normalized rank-position terminal identity;
- rigorous relaxed rank-transport exclusion described above.

### Exact finite certificates

- inherited `(46,29,17)` cutoff-free structural elimination;
- inherited `(65,41,24)` unique structural terminal and exact minimum excess `125`;
- inherited `(149,94,55)` no terminal with `H<=t+3`;
- new `(214,135,79)` no strict terminal violation `H<t+3`;
- new `(363,229,134)` no strict violation for even `t<=16`.

### Open

- uniform `H>=t+3` for every retained coprime near-resonant pair;
- q=134 middle strip `18..114` absent a uniform theorem;
- same-root radius-3 arithmetic bridge;
- global RL closure.
