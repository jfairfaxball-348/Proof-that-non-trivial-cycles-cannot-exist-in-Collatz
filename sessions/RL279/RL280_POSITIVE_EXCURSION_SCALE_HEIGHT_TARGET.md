# RL280 — positive-excursion scale-versus-height theorem target

Date prepared: 2026-09-08
Status: PREPARED, NOT STARTED

## Incoming classification

RL279 closed as

`SCALABLE_ZERO_RANK_RUN_COMPRESSION_PROVED`

with subordinate

- `HEIGHT_BUDGET_ZERO_RANK_IDENTITY_PROVED`;
- `UNIFORM_ZERO_MASS_CORRIDOR_PROVED`;
- `BOUNDARY_CYCLE_SCALE_SIGN_THEOREM_PROVED`;
- `ZERO_BUDGET_ONLY_HEIGHT_GROWTH_BARRIER_PROVED`;
- `EXACT_SEVEN_ZERO_GATE_A_CONTRACTION_PROVED`.

Gate A remains

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator now satisfies

`m0>=8`, equivalently `z>=k+6`.

## Exact inherited compressed state

Preserve:

1. `K=J+2^d-1` and the four affine `(d,K)` transitions.
2. All-one run macro:
   at `K!=0`, let `s=nu_2(K)`; at `d>1`, an all-one descent macro has length `s+1` and height charge `(s+1)(d-1)`.
3. Prefix potential
   `P=2^(H+n)/3^r`
   with column multiplier `2^d/3^x`.
4. At retained terminals,
   `P/X=2^(H_can-k-1)`,
   with dangerous `P<40/3` and safe `P>27/2`.
5. Height budget:
   `H_can=sum(v_t-u_t)`,
   and exact coupon decomposition
   `D=sum c_t(1-(2/3)^h_t)`.
6. Uniform zero mass:
   `17/2<S<21`.
7. Zero-to-zero scalar multiplier:
   `c_t/c_(t-1)=2(2/3)^g`.
8. Terminal scale:
   `X=2^(k+2)c_last(2/3)^tau`.
9. Boundary subsystem on even `K`, `d=1`:
   accelerated `3n+1` with endpoint monotonicities.
10. Every positive neutral boundary cycle is scale-expanding; every negative neutral boundary cycle is scale-contracting.
11. `J>0` is forward invariant.
12. Infinite equality family with `H_can=k=3` and unbounded zero count: zero-budget-only height growth is impossible.
13. Exact seven-zero safety:
    `H_can<k => m0>=8 => z>=k+6`.

## Mission

Prove a scalable theorem for a **height-positive excursion**

`d=1 -> d>1 -> d=1`.

Preferred order:

1. Parameterize an excursion by its boundary entry state, zero/run interruptions, and the exact `nu_2(K)` descent macros.
2. Derive its exact net multiplier in `P`, `X`, or the final zero weight `c`, together with its exact `Delta H`.
3. Prove the strongest valid inequality pricing excursion scale/state change by `2^(Delta H)`.
4. Quotient neutral boundary loops using only their already-proved scalar sign:
   negative loops contract, positive loops expand. Do not classify possible Collatz cycles.
5. Combine the excursion inequality with
   `17/2<S<21`,
   the height-coupon budget,
   the terminal scale formula, and `m0>=8`.
6. If a uniform excursion inequality fails, isolate the exact recurrent excursion type and prove the strongest correct finite-dimensional alternative.

## Preferred success criterion

Close Gate A by proving that a terminal with `H_can<k` cannot satisfy the compressed excursion/scale constraints.

A strong contraction of the remaining dangerous excursion state space is also meaningful if it is genuinely scalable.

## Forbidden repeats

Do not:

- make flat eight-zero enumeration the principal programme;
- attempt to solve or classify all Collatz cycles in the boundary subsystem;
- revive zero-budget-only unbounded height growth;
- restart selector enumeration;
- merge Gate B into Gate A without a new proved coupling;
- start Radius 6+;
- universalize branch-specific historical counterflow theorems.

Gate B remains frozen unless a new proved coupling requires it.
