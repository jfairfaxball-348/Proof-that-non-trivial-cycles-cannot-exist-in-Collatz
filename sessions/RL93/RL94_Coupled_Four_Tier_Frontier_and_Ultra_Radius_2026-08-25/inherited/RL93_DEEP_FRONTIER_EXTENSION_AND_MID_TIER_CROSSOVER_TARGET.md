# RL93 target — deep frontier continuation and middle-tier crossover

Date: 2026-08-25

## Authority

Continue from the frozen RL92 state.

RL92 eliminated every odd exact first-Farey/full-phase terminal value through

`2,921,652,721`.

The first surviving odd candidate for this route is

`k3=2,921,652,723`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or direct enumeration of all odd cofactors.

## Frozen constants and tiers

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- wide: `d<=5,000,030`, `r<=7,000,000`, successor `<=5,000,053`;
- deep: `d<=10,000,032`, `r<=1,100,000`, successor `<=10,000,053`;
- wide modulus `2^5,000,056`;
- deep modulus `2^10,000,056`;
- deep global minimum bit length `10,000,034` at `r=378,722`;
- first-Farey odd upper bound `42,150,931,559`.

At `k3`, `b=k-1` remains the worst stratum. The frozen RL92 margin is `-17,013`.

## 1. Primary target: continue the 10M frontier

Extend the exact consecutive-exponent scan modulo `2^10,000,056` beyond

`r=1,100,000`.

Use completed chunks only. After each extension endpoint `R_d'`, aggregate the exact global minimum balanced residue bit length and update the largest safe deep `D_d'`.

Recompute the exact supporting line and propagate the odd interval immediately.

## 2. Watch the frontier-quality process

Record every new global minimum bit length and its first location. If the deep minimum drops materially, compare the lost `D_d` against the gained `R_d` before extending further.

Do not assume depth remains flat.

## 3. Middle-tier crossover audit

Pure 10M extension is currently productive, but the active support is controlled by the wide-to-deep staircase corner. A fresh smaller-modulus middle tier can become competitive once extending the 10M scan far enough costs more than scanning a shallower modulus from `r=0` to a useful `R_m>R_d`.

For any proposed middle tier `(D_m,R_m)`, require exact completed scanning and verify that the resulting staircase corners genuinely improve the lower convex/supporting envelope. Compare scan work and margin gain before committing to a long range.

## 4. Ultra-deep activation condition

The frozen 15M low-`r` probe is exact but non-load-bearing. With the current wide/deep depths, relaxing the deep depth-axis constraint cannot matter before approximately

`R_d=3,499,990`.

Do not spend large compute on ultra-deep low-`r` scans before the active geometry changes, unless a middle tier creates a new convex corner that makes them relevant earlier.

## 5. Tier-specific transition charging

Do not merely split the union and assume wide blocks exist in force. Any improved successor charging must prove a nontrivial lower bound on the stronger-tier population or derive a valid exact dual inequality that materially improves the endpoint.

## 6. Immediate propagation

If `k3` closes, do not stop.

1. find the exact last odd `k` closed by the improved certificate;
2. record the last positive and first nonpositive margins;
3. update the first-Farey odd lower endpoint;
4. test the strongest adjacent frontier/tier adjustment still justified by compute;
5. then freeze the next handover.

## 7. Red teams

Every promoted theorem must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy.

## 8. Sustained attack protocol

A closed endpoint or interval extension is a checkpoint. Continue until compute/context pressure genuinely threatens reliability, the route is rigorously exhausted, or the target and its immediate consequences are complete.
