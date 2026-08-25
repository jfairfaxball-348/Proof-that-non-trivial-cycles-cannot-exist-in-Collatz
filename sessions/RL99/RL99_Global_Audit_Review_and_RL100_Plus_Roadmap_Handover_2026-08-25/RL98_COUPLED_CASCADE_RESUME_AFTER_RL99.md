# RL98 — coupled-cascade resume point after RL99

Date: 2026-08-25

## Status

This file preserves the exact live coupled-cascade attack that was intentionally deferred in order to run RL99 as a global audit / roadmap-setting session.

The route is **paused, not abandoned**.

Do not treat RL99's strategic pivot as evidence that this attack failed or was exhausted.

## 1. Frozen prerequisite state

Latest completed mathematics is RL97.

Exact tiers:

- wide `(D_w,R_w,L_w)=(5,000,030,7,000,000,5,000,053)`;
- middle `(D_m,R_m,L_m)=(7,500,032,4,350,000,7,500,053)`;
- deep `(D_d,R_d,L_d)=(10,000,032,3,000,000,10,000,053)`;
- ultra `(D_u,R_u,L_u)=(15,000,035,1,680,000,15,000,053)`.

Frozen exact support:

- `mu=1/7,000,001`;
- `lambda=4,000,000/52,500,238,500,033`;
- feasible pair supports `A-C`, `C-D`, `D-E`;
- `A-C` optimal at the frozen live endpoint;
- `floor(lambda*C)=3,211`;
- `b=k-1` worst stratum.

Conservative successor charge:

`L_common=15,000,053`.

First live branch candidate:

`k8=2,921,801,523`.

Frozen margin at `k8`:

`-3,549`.

The previous odd `2,921,801,521` is excluded with margin `+10,473`.

## 2. Exact scan minima that must be inherited

Do not restart historical scans unless an audit repair requires it.

- middle global minimum: `7,500,034 at r=1,635,300`, hence `D_m=7,500,032`;
- deep global minimum: `10,000,034 at r=378,722`, hence `D_d=10,000,032`;
- ultra global minimum: `15,000,037 at r=575,974`, hence `D_u=15,000,035`.

Additional known near-floor/tie events:

- ultra `15,000,037 at r=905,728`;
- ultra `15,000,037 at r=1,368,912`;
- deep `10,000,036 at r=2,955,163`.

## 3. Immediate resume checkpoint

For `R_d=3,025,000`, unchanged depth floors under the current geometry require:

- `R_m>=4,349,996`;
- `R_u>=1,700,006`.

Current middle radius `4,350,000` already clears the first requirement by four.

Resume with:

1. exact ultra scan `1,680,001..1,705,000` (or a small rounded extension beyond);
2. compare the completed band minimum with the frozen global minimum immediately;
3. exact deep scan `3,000,001..3,025,000`;
4. rebuild all staircase-complement corners from the actual certified radii/depths;
5. enumerate every exact feasible nonnegative pair support;
6. select the support minimizing the live aggregate;
7. verify `floor(lambda*C)>2` or redo block-count optimization;
8. evaluate the exact margin at `k8`;
9. if positive, propagate to the exact final consecutive odd exclusion and first failure.

No middle extension is needed for this first step if the frozen floors survive.

## 4. Second checkpoint

For `R_d=3,050,000`, unchanged floors require:

- `R_m>=4,366,662`;
- `R_u>=1,733,340`.

Natural completed targets:

- middle `R_m>=4,375,000`;
- ultra `R_u>=1,740,000`;
- deep `R_d=3,050,000`.

Then continue through adjacent `25,000`-step deep batches while the route remains productive.

## 5. Medium-range watch

With current floors, the ultra depth-axis remains nonbinding through deep radius floor

`3,499,992`.

Track exactly:

- live bit-length floor changes after every completed scan band;
- `A-C` versus `C-D` support competition;
- the `E`-axis ultra-depth reserve;
- any change in the worst block-count stratum;
- interval-propagation efficiency as `floor(lambda*C)` decreases;
- whether a stronger rigorously justified tier-specific successor population theorem emerges.

Do not jump over unscanned gaps merely to reach the `3.5M` region.

## 6. Red-team requirements on resumption

Every promoted result must still pass:

1. RL81 common-mode freedom;
2. RL79 generalized-increment homogeneity barrier;
3. RL20 physical representative / packing separation;
4. primitivity;
5. exact first-Farey/full-phase scope;
6. RL88 arbitrary-reset family;
7. verification economy;
8. successor-charge consistency;
9. exact support-edge re-optimization;
10. live bit-length floor update;
11. exact handling of equal minima versus genuine floor drops.

## 7. Strategic status

This attack has demonstrated sustained exact branch narrowing: RL97 alone eliminated `13,396` consecutive odd branch candidates and advanced the deep certified radius from `2.4M` to `3.0M`.

What remains unresolved is not whether the engine can make local progress, but how its branch-specific hypotheses relate to a global Gate-A or RL closure route.

RL99 is explicitly tasked with judging that question before RL100+ commits further sustained compute.
