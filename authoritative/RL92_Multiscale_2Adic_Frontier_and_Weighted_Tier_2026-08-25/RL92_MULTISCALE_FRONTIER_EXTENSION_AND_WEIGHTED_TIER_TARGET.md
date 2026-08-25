# RL92 target — multiscale 2-adic frontier extension and weighted-tier continuation

Date: 2026-08-25

## Authority

Continue from the frozen RL91 state.

RL91 eliminated all odd exact first-Farey/full-phase terminal values through

`2,921,630,973`

using a two-tier multiscale 2-adic cover.

The first surviving odd candidate for this route is

`k2=2,921,630,975`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or direct enumeration of all odd cofactors.

## Frozen constants and tiers

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- wide tier: `d<=5,000,030`, `r<=7,000,000`, successor `<=5,000,053`;
- deep tier: `d<=10,000,035`, `r<=300,000`, successor `<=10,000,053`;
- wide modulus `2^5,000,056`;
- deep modulus `2^10,000,056`;
- first-Farey odd upper bound `42,150,931,559`.

At `k2`, `b=k-1` is the worst block-count stratum. The frozen two-tier certificate has margin `-23,150`, so only a modest improvement is required to eliminate the endpoint.

## 1. Primary target: extend the deep frontier

Continue the exact consecutive-exponent scan modulo `2^10,000,056` beyond

`r=300,000`.

Use completed chunks only. After every extension endpoint `R_d'`, determine the new global minimum balanced residue bit length and therefore the largest safe deep ordinary-deficit threshold `D_d'`.

Recompute the staircase supporting line against the frozen wide tier rather than retaining stale weights.

## 2. Competing route: widen the 5M tier

If deep extension becomes inefficient, extend the exact `2^5,000,056` scan beyond

`r=7,000,000`.

Compare gain per scan cost using the actual endpoint budgets at `k2`.

Do not enlarge both dimensions blindly.

## 3. Three-tier convex cover

Test at least one additional modulus scale if it can create a favorable frontier corner.

For nested staircase corners `(D_j,R_j)`, derive an exact lower convex/supporting-line cover of the complement. Prefer a direct weighted inequality or a piecewise supporting envelope that avoids double counting.

Promote only completed exact scan ranges.

## 4. Tier-specific transition charging

RL91 conservatively charged every covered block at successor ceiling `10,000,053`, even though wide-tier blocks have the stronger ceiling `5,000,053`.

Investigate whether separating the populations by tier and charging them at their own `C-L_j` deficit costs materially improves the endpoint margin.

Any such refinement must avoid double counting and preserve the inherited exception accounting.

## 5. Immediate propagation

If `k2` closes, do not stop.

1. find the exact last odd `k` closed by the improved multiscale certificate;
2. record the last positive contradiction margin and first nonpositive margin;
3. update the first-Farey odd lower endpoint;
4. test a small adjacent frontier extension before declaring a route threshold;
5. then freeze the next handover.

## 6. Red teams

Every promoted theorem must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy.

## 7. Sustained attack protocol

A closed endpoint or interval extension is a checkpoint. Continue through the strongest adjacent frontier/tier adjustment until compute/context pressure genuinely threatens reliability, the route is rigorously exhausted, or the target and its immediate consequences are complete.
