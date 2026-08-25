# RL91 target — tiered/asymmetric 2-adic rectangle covering and next-odd continuation

Date: 2026-08-25

## Authority

Continue from the frozen RL90 state.

RL90 eliminated all odd first-Farey/full-phase terminal values through

`2,921,406,839`

using a two-budget `(d,r)` covering rectangle and exact consecutive-exponent 2-adic certificate.

The first surviving odd candidate for this route is

`k2=2,921,406,841`.

Do not restart generic quotient packing, independent midpoint congruence accumulation, or direct enumeration of all odd cofactors.

## Frozen constants

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- current rectangle `d<=500,036`, `r<=550,000`;
- current forced successor ceiling `500,053`;
- current modulus `2^500056`;
- current first-Farey odd upper bound `42,150,931,559`.

At `k2`, `b=k-1` is the worst block-count stratum. The fixed RL90 rectangle has margin `-67,747`, so only a modest improvement in the population/short-successor balance is required to eliminate this endpoint.

## 1. Primary target: optimize the deficit-deficiency frontier

Work with

`d_i=C-n_i`,

`r_i=S_*-s_i`.

The two available aggregate budgets are

`sum d_i = D_b`,

and the RL90 safe bound

`sum r_i <= R_b^max`.

Rather than one square-like rectangle, build a nested family such as

`d<=D_1, r<=R_1`,

`d<=D_2, r<=R_2`, ...

with thresholds chosen from the exact endpoint budgets.

The objective is to maximize the number of blocks that receive a useful short-successor theorem per unit of finite-certificate cost.

## 2. Certificate design

For a minimal reset

`3^(s+1)m-1=2^(n_next+2)m_next`.

For each tier choose a desired successor cap `L_j`. Then it suffices to work modulo

`2^(L_j+3)`.

If `d<=D_j`, the physical cofactor bound gives

`|m|<2^(D_j+1)`.

Certify that the balanced inverse residues for the relevant exponent-deficiency band exceed that cofactor range.

Prefer:

1. consecutive-exponent GMP scans;
2. asymmetric `D_j,R_j` choices;
3. nested residue reuse between tiers;
4. exact output frozen as finite certificates.

Do not scan all `m`.

## 3. Population accounting

For each tier use exact Markov bounds from `D_b` and `R_b^max`. Avoid double counting by expressing the tiers as nested differences or by proving a direct staircase covering inequality.

Every certified block must still be charged through the RL89 transition framework:

- nonminimal/zero-return exceptions at most `k-1-b`;
- a successor of length `<=L_j` costs at least `C-L_j` ordinary deficit.

At `b=k-1` the area exception is zero, which should be exploited fully.

## 4. Immediate propagation

If `k2` closes, do not stop.

1. find the exact last odd `k` closed by the new tiered certificate;
2. record the last positive contradiction margin and first nonpositive margin;
3. update the first-Farey odd lower endpoint;
4. test whether a small threshold adjustment extends the interval further;
5. only then consider a new route.

## 5. Red teams

Every promoted theorem must pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity;
3. RL20 physical representative/packing separation;
4. primitivity;
5. first-Farey scope;
6. RL88 arbitrary-reset family;
7. verification economy.

## 6. Sustained attack protocol

A closed endpoint or interval extension is a checkpoint. Continue through the strongest adjacent tier/threshold adjustment until compute/context pressure genuinely threatens reliability, the route is rigorously exhausted, or the target and its immediate consequences are complete.
