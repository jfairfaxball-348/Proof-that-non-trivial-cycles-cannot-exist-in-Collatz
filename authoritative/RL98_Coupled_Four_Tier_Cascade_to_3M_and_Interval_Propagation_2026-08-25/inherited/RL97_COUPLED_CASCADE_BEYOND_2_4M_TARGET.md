# RL97 target — corrected coupled cascade beyond deep radius 2,400,000

Date: 2026-08-25

## Authority

Continue from the frozen RL96 state.

RL96 eliminated every odd exact first-Farey/full-phase terminal value through

`2,921,774,729`.

The first surviving odd candidate for this route is

`k7=2,921,774,731`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or direct enumeration of odd cofactors.

## Frozen constants

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- wide `(D_w,R_w,L_w)=(5,000,030,7,000,000,5,000,053)`;
- middle `(D_m,R_m,L_m)=(7,500,032,3,950,000,7,500,053)`;
- deep `(D_d,R_d,L_d)=(10,000,032,2,400,000,10,000,053)`;
- ultra `(D_u,R_u,L_u)=(15,000,035,870,000,15,000,053)`;
- current support `lambda=4,600,000/52,500,238,500,033`, `mu=1/7,000,001`;
- conservative common successor `L_common=15,000,053`;
- first-Farey odd upper bound `42,150,931,559`.

At `k7`, `b=k-1` remains the worst stratum. Frozen RL96 margin: `-3,972`.

## 1. Immediate next checkpoint

For `R_d=2,425,000`, unchanged depth floors under the current `A-C` support require

- `R_m>=3,949,995`;
- `R_u>=900,007`.

Current middle radius `3,950,000` already clears the requirement by five.

Natural completed batch:

- ultra `r=870,001..905,000`;
- deep `r=2,400,001..2,425,000`;
- no middle extension for this first step unless a floor/support event changes the geometry.

Use completed exact scans only.

## 2. Second checkpoint

For `R_d=2,450,000`, current depths require

- `R_m>=3,966,662`;
- `R_u>=933,341`.

Natural targets:

- middle to `3,975,000`;
- ultra to `935,000`;
- deep to `2,450,000`.

Then continue the same coupled logic through adjacent 25,000-step deep batches rather than stopping at the first restored endpoint.

## 3. Live floor policy

The frozen global bit-length minima are

- ultra `15,000,037 at r=575,974` => `D_u=15,000,035`;
- middle `7,500,034 at r=1,635,300` => `D_m=7,500,032`;
- deep `10,000,034 at r=378,722` => `D_d=10,000,032`.

Every new completed scan band must be compared against these global minima. If a new lower minimum appears, update `D=B-2` before rebuilding geometry.

## 4. Exact support re-optimization

At the frozen RL96 frontier, feasible pair supports are

`A-C`, `C-D`, `D-E`,

with `A-C` optimal in the live aggregate direction.

After every material frontier or depth move:

1. rebuild all staircase-complement corners using actual certified radii and depths;
2. enumerate every exact feasible nonnegative supporting edge;
3. select the support minimizing the live weighted aggregate;
4. prove validity over all corners;
5. check for an edge crossover.

Do not inherit `A-C` blindly.

## 5. Interval propagation

After each coupled improvement:

1. verify `floor(lambda*C)>2` or redo the block-count optimization;
2. retain `L_common=15,000,053` unless a rigorous stronger population theorem is proved;
3. evaluate the exact worst-stratum margin at `k7`;
4. if positive, locate the exact final consecutive odd exclusion and first failure;
5. continue the cascade while productive.

## 6. Long-range geometry watch

At the frozen state:

- `floor(lambda*C)=3,693`;
- ultra depth-axis remains nonbinding through deep radius floor `3,499,992`;
- final `E`-axis ultra-depth reserve is `3,586,940`.

The route is not currently close to an ultra depth-axis failure, but the declining weighted decrement and the `A-C`/`C-D` competition should be tracked exactly.

## 7. Optional stronger route

Do not assume a stronger mixed successor charge.

If a rigorous tier-specific population theorem can be derived from the exact dual weights while preserving physical-representative separation, test whether it materially improves propagation. Demote immediately if it relies on quotient-address counting or unproved population balance.

## 8. Red teams

Every promoted theorem must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy;
8. load-bearing successor-charge consistency;
9. exact support-edge re-optimization;
10. live bit-length floor update before geometry.

## 9. Sustained attack protocol

A successful 25,000-step deep move is a checkpoint, not a close trigger.

Continue through adjacent coupled batches, exact support re-optimization, interval propagation, floor changes, and nearby edge crossovers until compute/context pressure genuinely threatens reliability or the route is exhausted.
