# RL93 — coupled four-tier 2-adic frontier and ultra activation

Date: 2026-08-25

## 0. Executive outcome

RL93 continued the frozen RL92 deep-frontier target under the verification-economy and sustained-attack rules.

**No Gate A global, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.** All terminal exclusions below remain conditional on the inherited exact first-Farey/full-phase Gate-A branch.

RL92 left the first route survivor

`k0=2,921,652,723`

with margin `-17,013` under its wide/deep two-tier support.

RL93 extended the exact `2^10,000,056` deep scan gap-free from `r=1,100,001` through `r=1,775,000`. No new global deep minimum appeared: the RL93-added band has minimum bit length `10,000,036` at `r=1,693,348`, while the inherited global minimum remains `10,000,034 at r=378,722`. Hence the deep tier remains

`d<=10,000,032, r<=1,775,000 => n_next<=10,000,053`.

RL93 then introduced an exact `2^7,500,056` middle tier. The completed scan covers `r=1,250,001..3,525,000` and has minimum balanced-residue bit length `7,500,034`, first at `r=1,635,300`. Because the deeper 10M rectangle already covers all `r<=1,775,000`, this combines into the effective middle staircase rectangle

`d<=7,500,032, r<=3,525,000 => n_next<=7,500,053`.

The middle tier became genuinely load-bearing and carried the support geometry to the point where the inherited 15M ultra tier also became relevant. RL93 therefore extended the exact `2^15,000,056` probe from `r<=1,000` to `r<=35,000`. The combined ultra minimum becomes `15,000,040 at r=2,900`, giving

`d<=15,000,038, r<=35,000 => n_next<=15,000,053`.

At the final coupled frontier

- wide: `(D,R,L)=(5,000,030, 7,000,000, 5,000,053)`;
- middle: `(7,500,032, 3,525,000, 7,500,053)`;
- deep: `(10,000,032, 1,775,000, 10,000,053)`;
- ultra: `(15,000,038, 35,000, 15,000,053)`,

the active supporting line is

`mu = 1/7,000,001`,

`lambda = 5,225,000 / 52,500,238,500,033`.

The weighted floor rises by `floor(lambda*C)=4,195` per increment of `b`, still far above the explicit `2` improvement, so `b=k-1` remains the worst stratum.

Using the **correct conservative common successor ceiling `15,000,053`**, the exact rational interval verifier eliminates all `48,767` consecutive odd values

`2,921,652,723 <= k <= 2,921,750,255`.

At the final eliminated odd value the contradiction margin is `+5,210`; at the next odd

`k=2,921,750,257`

the margin is `-10,779`.

Therefore the updated branch-specific odd surviving window is

`2,921,750,257 <= k <= 42,150,931,559`, `k` odd.

---

## 1. Incoming verification economy gate

The supplied RL93 handover was checked before new mathematics:

- outer RL93 SHA-256 sidecar: PASS;
- fresh internal manifest: PASS;
- supplied fresh-unpack verification: PASS;
- RL92 fast verifier suite: PASS.

The frozen RL92 proof-state ledger was accepted. No recursive replay of historical expensive finite certificates was performed.

GitHub provenance was checked read-only. The matching authoritative commit was

`1d42e2f93e4a5c182c09e671a66daaab430cfbbe`

with message

`RL93_Deep_2Adic_Frontier_Extension_and_Mid_Tier_Crossover_2026-08-25`.

No repository write was performed during the research attack.

---

## 2. Exact 10M deep-frontier continuation

The inherited minimal-reset interface is unchanged. For modulus `2^N`, a certified balanced inverse-residue bit-length floor `B` on an `r` band excludes resets with `n_next+2>=N` whenever `d<=B-2`.

RL93 completed 27 exact 25,000-step GMP chunks modulo `2^10,000,056` over

`1,100,001 <= r <= 1,775,000`.

The new-band minimum is

`min bitlen(|mu_r|)=10,000,036 at r=1,693,348`.

This is above the inherited global minimum `10,000,034 at r=378,722`. Thus the combined exact certificate is

### Certificate 2.1 — RL93 deep rectangle

`d<=10,000,032 and r<=1,775,000 => n_next<=10,000,053`

under a minimal reset.

Classification: **new exact finite certificate + inherited-interface analytic consequence**.

---

## 3. Exact middle-tier crossover

RL93 scanned modulo `2^7,500,056` in 91 completed 25,000-step chunks over

`1,250,001 <= r <= 3,525,000`.

The scan minimum is

`min bitlen(|mu_r|)=7,500,034 at r=1,635,300`,

with another chunk minimum of the same bit length at `r=1,819,885`.

Hence wherever this middle scan is required,

`d<=7,500,032 => n_next<=7,500,053`.

The 10M deep rectangle already subsumes the middle depth for every `r<=1,775,000`. Therefore the union of the deep certificate and the scanned middle band rigorously supplies the effective staircase rectangle

### Certificate 3.1 — effective middle rectangle

`d<=7,500,032 and r<=3,525,000 => n_next<=7,500,053`.

This is not an extrapolation of the middle scan into an unscanned low-`r` interval: the low-`r` portion is covered by the strictly deeper 10M rectangle.

Classification: **new exact finite middle-band certificate + analytic rectangle union**.

---

## 4. Geometric crossover and ultra-tier activation

The final four-tier staircase complement has relevant integer corners

`A=(0,7,000,001)`,

`B=(5,000,031,3,525,001)`,

`C=(7,500,033,1,775,001)`,

`D=(10,000,033,35,001)`,

`E=(15,000,039,0)`.

Set

`mu=1/7,000,001`,

`lambda=(7,000,000-1,775,000)/[(7,000,001)(7,500,033)]`

`      =5,225,000/52,500,238,500,033`.

Then `A` and `C` lie exactly on `lambda d + mu r = 1`; direct exact arithmetic gives

- `B`: `5840309533337/5833359833337` > 1;
- `D`: `52512681080033/52500238500033` > 1;
- `E`: `2902785325000/1944453277779` > 1.

Thus every integer point outside the four-tier certified union obeys

`lambda*d + mu*r >= 1`.

At the final deep radius, feasibility of the same `A-C` line requires at least

- middle radius `R_m >= 3,516,661`;
- ultra radius `R_u >= 33,341`.

The certified values `R_m=3,525,000` and `R_u=35,000` clear those thresholds, but the ultra slack is now only `1,659`. This explains why the next deep advance is no longer a cheap one-tier extension.

For a next `25,000` deep step to `R_d=1,800,000`, the current depths would require approximately

- `R_m >= 3,533,328`;
- `R_u >= 66,675`.

The ultra depth-axis itself remains nonbinding until approximately `R_d<=3,499,993` with the current depths.

Classification: **new analytic four-tier supporting-line theorem + exact activation/coupling thresholds**.

---

## 5. Exact ultra extension

The inherited exact 15M probe covered `0<=r<=1,000` with minimum bit length `15,000,048 at r=88`.

RL93 completed seven further exact chunks modulo `2^15,000,056` over

`1,001 <= r <= 35,000`.

The new-band minimum is

`15,000,040 at r=2,900`.

Therefore the combined ultra certificate is

### Certificate 5.1 — RL93 ultra rectangle

`d<=15,000,038 and r<=35,000 => n_next<=15,000,053`.

Classification: **new exact finite certificate + inherited-interface analytic consequence**.

---

## 6. Top-stratum reduction

Using the final four-tier support,

`floor(lambda*C)=4,195`.

When `b` rises by one, the weighted bad-block floor therefore rises by at least `4,195`, while the explicit `2b` term can improve the contradiction margin by only `2`, and the short-successor capacity is nondecreasing. Hence the contradiction margin strictly decreases with `b`.

### Theorem 6.1 — RL93 top-stratum reduction

It remains sufficient to test `b=k-1`.

Classification: **updated analytic monotonicity theorem**.

---

## 7. Conservative successor-charge repair

During the live RL93 attack, preliminary endpoint arithmetic continued to use the inherited common successor ceiling `10,000,053` after the ultra tier had become load-bearing.

That is too strong: an ultra-only covered block is certified only at successor ceiling `15,000,053`. Therefore the correct conservative common charge for the final four-tier union is

`L_common=15,000,053`.

The close-out verifier repairs this before promotion.

At `k=2,921,750,255`, the preliminary `10M` charge gave capacity `365,524` and margin `+5,253`. The correct `15M` charge gives capacity `365,567` and margin `+5,210`.

At `k=2,921,750,257`, the preliminary values were capacity `365,526`, margin `-10,736`; the correct values are capacity `365,569`, margin `-10,779`.

**The sign pattern and therefore the exact eliminated interval are unchanged.** No theorem endpoint is demoted; only the two displayed preliminary margin/capacity tuples are repaired.

Classification: **close-out correction / bookkeeping repair**.

---

## 8. Exact odd-interval propagation

The final verifier evaluates the worst stratum `b=k-1` for every odd

`2,921,652,723 <= k <= 2,921,750,255`

using exact rational arithmetic and `L_common=15,000,053`.

All `48,767` values violate the necessary condition.

At the final eliminated odd `k=2,921,750,255`:

- `Q_min=123,139,091,657,860,901,815`;
- `D_b=15,403,532,584,731,697`;
- `R_b^max=9,718,578,782,241,181`;
- weighted bad-block bound `2,921,379,477`;
- forced multiscale-good blocks `370,777`;
- short-successor capacity `365,567`;
- contradiction margin `+5,210`.

At the next odd `k=2,921,750,257`:

- `Q_min=123,139,091,657,860,901,667`;
- `D_b=15,403,616,886,595,101`;
- `R_b^max=9,718,631,970,795,087`;
- weighted bad-block bound `2,921,395,466`;
- forced multiscale-good blocks `354,790`;
- short-successor capacity `365,569`;
- contradiction margin `-10,779`.

### Theorem 8.1 — RL93 odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`2,921,652,723 <= k <= 2,921,750,255`.

The updated branch-specific odd window is therefore

`2,921,750,257 <= k <= 42,150,931,559`, `k` odd.

Classification: **new analytic theorem + exact finite 2-adic certificates + exact rational interval audit**.

---

## 9. Red-team audit

### RL81 common-mode freedom
Passed. No quotient state is promoted to a physical state; all finite certificates consume only the inherited physical cofactor bound and minimal-reset relation.

### RL79 generalized-increment homogeneity
Passed. The ordinary `+1` minimal-reset constant remains essential.

### RL20 physical representative/packing separation
Passed. The weighted cover counts inherited synchronized physical blocks, not quotient-address multiplicity.

### Primitivity
Passed. Repeated residues/cofactors are not interpreted as repeated cycle states.

### First-Farey scope
Preserved. Every new interval exclusion remains branch-specific.

### RL88 arbitrary-reset family
Passed. High reset valuation is excluded only inside certified `(d,r)` regions.

### Verification economy
Passed. Historical expensive scans were not recursively replayed. New RL93 ranges alone were scanned; inherited exact certificates were accepted after the incoming gate.

### Conservative successor charging
Repaired at close-out. Final theorem uses `15,000,053` as required by the load-bearing ultra tier.

---

## 10. Proof-state ledger additions

### New proved analytic mathematics

1. Middle-band plus deep-rectangle union gives an effective `D_m=7,500,032`, `R_m=3,525,000` tier.
2. Four-tier supporting-line theorem with `lambda=5225000/52500238500033`, `mu=1/7000001`.
3. Coupling thresholds for the middle and ultra radii as the deep frontier advances.
4. Updated top-stratum monotonicity with weighted decrement floor `4,195`.
5. Elimination of `48,767` additional odd first-Farey/full-phase terminal values through `2,921,750,255`.

### New exact finite certificates

1. New 10M band: `r=1,100,001..1,775,000`, minimum `10,000,036 at r=1,693,348`; combined global deep minimum remains `10,000,034 at r=378,722`.
2. 7.5M middle band: `r=1,250,001..3,525,000`, minimum `7,500,034 at r=1,635,300`.
3. 15M ultra extension: `r=1,001..35,000`, minimum `15,000,040 at r=2,900`; combined with inherited `r<=1,000` probe.

### Exact finite arithmetic audit

All `48,767` odd values in the RL93 interval are checked after analytic reduction to `b=k-1`.

### Correction ledger

The preliminary live-session use of `L_common=10,000,053` after ultra activation is repaired to `15,000,053`. Endpoint unchanged; exact final margins corrected.

### Route limitation

The final margin at `k=2,921,750,257` is `-10,779`. The route remains productive but now requires a coupled deep/middle/ultra scan rather than a cheap single-frontier continuation.

---

## 11. RL94 route selection

Continue at

`k4=2,921,750,257`.

Priority order:

1. replenish the exact 15M ultra radius from `35,000` to at least about `70,000`, recomputing its global bit-length minimum;
2. extend the 10M deep frontier in completed 25,000-step chunks beyond `1,775,000`;
3. keep the 7.5M middle frontier above the exact `A-C` feasibility threshold after each deep step (for `R_d=1,800,000`, current-depth geometry requires `R_m>=3,533,328`);
4. after each coupled advance, recompute the exact four-tier convex envelope rather than assuming `A-C` stays active;
5. propagate the odd interval immediately after every materially improved support;
6. if the ultra minimum drops, update `D_u` but note that the ultra depth-axis has very large current slack; the immediate load-bearing condition is chiefly the `D=(D_d+1,R_u+1)` corner;
7. continue the cascade while productive, watching the later ultra-depth-axis transition near deep radius `~3.5M` under unchanged depths;
8. retain the conservative common successor ceiling `15,000,053` unless a rigorous tier-specific population theorem justifies stronger charging;
9. do not return to brute-force odd cofactor enumeration.

The sustained-attack rule remains mandatory.
