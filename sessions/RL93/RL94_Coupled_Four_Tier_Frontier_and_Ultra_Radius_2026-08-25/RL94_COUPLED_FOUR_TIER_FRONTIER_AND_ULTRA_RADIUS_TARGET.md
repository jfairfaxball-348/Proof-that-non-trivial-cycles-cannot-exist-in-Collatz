# RL94 target — coupled four-tier frontier and ultra-radius replenishment

Date: 2026-08-25

## Authority

Continue from the frozen RL93 state.

RL93 eliminated every odd exact first-Farey/full-phase terminal value through

`2,921,750,255`.

The first surviving odd candidate for this route is

`k4=2,921,750,257`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or direct enumeration of odd cofactors.

## Frozen constants

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- wide `(D_w,R_w,L_w)=(5,000,030,7,000,000,5,000,053)`;
- middle `(D_m,R_m,L_m)=(7,500,032,3,525,000,7,500,053)`;
- deep `(D_d,R_d,L_d)=(10,000,032,1,775,000,10,000,053)`;
- ultra `(D_u,R_u,L_u)=(15,000,038,35,000,15,000,053)`;
- current support `lambda=5225000/52500238500033`, `mu=1/7000001`;
- corrected conservative common successor `L_common=15,000,053`;
- first-Farey odd upper bound `42,150,931,559`.

At `k4`, `b=k-1` remains the worst stratum. The frozen corrected RL93 margin is `-10,779`.

## 1. Primary target: replenish ultra radius

The current `A-C` support has only `1,659` units of ultra-radius slack. Before or alongside the next deep step, extend the exact `2^15,000,056` scan beyond

`r=35,000`.

A practical first target is `r≈70,000`, because a 25,000-step deep extension to `R_d=1,800,000` would require `R_u>=66,675` if the certified depths stay unchanged.

Use completed exact chunks only. Record every new global ultra minimum and update `D_u=B_u-2` immediately if the bit-length floor falls.

## 2. Continue the 10M deep frontier

Once ultra support is sufficient, extend modulo `2^10,000,056` beyond

`r=1,775,000`.

Prefer 25,000-step completed chunks for compatibility with the frozen ledger. After every chunk or coupled batch, recompute the combined global deep minimum and safe `D_d`.

## 3. Keep the 7.5M middle corner feasible

For the current `A-C` line, a deep step changes the minimum middle radius needed to keep corner `B` above the support line.

At `R_d=1,800,000`, unchanged-depth geometry requires

`R_m>=3,533,328`.

The frozen `R_m=3,525,000` is slightly below that requirement, so a middle extension is also needed. A single additional 25,000-step middle chunk to `3,550,000` would clear this particular step if its bit-length floor preserves `D_m`.

Do not assume the same line remains optimal after depth changes; solve the exact convex/supporting-envelope problem each time.

## 4. Four-tier coupling formulas

For the present `A-C` candidate line

`mu=1/(R_w+1)`,

`lambda=(R_w-R_d)/[(R_w+1)(D_m+1)]`,

corner feasibility requires

`lambda(D_w+1)+mu(R_m+1)>=1`,

`lambda(D_d+1)+mu(R_u+1)>=1`,

`lambda(D_u+1)>=1`.

Use these exact inequalities to determine which frontier is limiting before starting an expensive scan batch.

Under unchanged depths, the ultra depth-axis remains nonbinding until approximately deep radius `3,499,993`. The immediate bottleneck is therefore ultra **radius**, not ultra depth.

## 5. Exact interval propagation

After every meaningful coupled improvement:

1. prove the active supporting line over all staircase complement corners;
2. verify `floor(lambda*C)>2` or otherwise redo the block-count optimization;
3. use the weakest load-bearing successor ceiling as the conservative common charge — currently `15,000,053`;
4. evaluate the exact worst-stratum margin at `k4`;
5. if positive, find the exact last consecutive odd value eliminated and the first failure;
6. continue the coupled frontier while the route remains productive.

## 6. Tier-specific charging remains optional, not assumed

The final RL93 repair demonstrates why load-bearing tiers must control the common successor ceiling. Do not revert to `10,000,053` merely because the deep tier dominates most of the staircase.

A stronger mixed charge is allowed only if a rigorous lower bound on the populations of the stronger tiers is proved or an exact dual inequality is derived.

## 7. Red teams

Every promoted theorem must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy;
8. load-bearing successor-charge consistency.

## 8. Sustained attack protocol

A closed endpoint or individual frontier extension is a checkpoint. Continue through the coupled ultra/middle/deep cascade until compute/context pressure genuinely threatens reliability, the route is rigorously exhausted, or the target and its immediate consequences are complete.
