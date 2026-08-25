# RL92 — deep 2-adic frontier extension and geometric tier audit

Date: 2026-08-25

## 0. Executive outcome

RL92 continued the frozen RL91 multiscale 2-adic frontier target under the sustained-attack and verification-economy rules.

**No Gate A global, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.** Every terminal exclusion remains conditional on the exact first-Farey/full-phase Gate-A branch inherited through RL91.

RL91 left the first route survivor

`k0=2,921,630,975`

with frozen two-tier contradiction margin `-23,150`, using

- wide tier `d<=5,000,030`, `r<=7,000,000`, successor `<=5,000,053`;
- deep tier `d<=10,000,035`, `r<=300,000`, successor `<=10,000,053`.

RL92 extended the exact `2^10,000,056` deep scan gap-free from `r=300,001` through `r=1,100,000`. A new minimum balanced-residue bit length

`10,000,034 at r=378,722`

appeared, so the safe deep ordinary-deficit depth becomes

`d<=10,000,032`.

The much larger deep `r` frontier more than compensates for this three-unit depth loss. With

`R_d=1,100,000`, `D_d=10,000,032`,

and the frozen wide tier, the exact optimal active supporting line used in this route is

`mu = 1/7,000,001`,

`lambda = 5,900,000 / 35,000,222,000,031`.

The weighted bad-block floor rises by at least `7,105` when `b` rises by one, so `b=k-1` remains the worst block-count stratum.

The exact interval verifier eliminates all `10,874` consecutive odd values

`2,921,630,975 <= k <= 2,921,652,721`.

At the last eliminated odd value the margin is `+4,796`. At the next odd

`k=2,921,652,723`

the margin is `-17,013`.

Hence the updated branch-specific odd surviving window is

`2,921,652,723 <= k <= 42,150,931,559`, `k` odd.

RL92 also tested a `15,000,056`-bit ultra-deep tier over `r=0..1,000`. Its exact minimum is `15,000,048` bits at `r=88`, giving a potential local depth `d<=15,000,046`. This tier is **not load-bearing**: at the present deep frontier, the existing wide-to-deep supporting line already clears the deeper staircase corners, so the ultra-deep tier does not improve the one-line population bound. The depth-axis relaxation cannot become active before approximately `R_d=3,499,990` for the current wide/deep depths.

---

## 1. Incoming verification economy gate

The supplied RL92 handover was checked before new mathematics:

- outer SHA-256 sidecar: PASS;
- fresh internal manifest: PASS;
- supplied fresh-unpack verification: PASS;
- RL91 fast verifier suite: PASS.

The frozen RL91 proof-state ledger was accepted. No recursive historical expensive certificate replay was performed.

GitHub was consulted read-only for provenance. The latest matching authoritative handover commit found was

`2c881c7e1493fffb9c45133fff314498125602e6`

with message

`RL91_Banded_2Adic_Rectangle_Covering_and_Odd_Interval_2026-08-25`.

No repository write was performed.

---

## 2. Exact deep-frontier extension

The inherited exact minimal-reset interface is unchanged:

`3^(s+1)m - 1 = 2^(n_next+2)m_next`,

with `d=C-n`, `r=S_*-s`, and physical cofactor bound

`|m| < 2^(d+1)`.

For modulus `2^N`, if every balanced inverse residue in a certified `r` band has bit length at least `B`, then

`|mu_r| >= 2^(B-1)`

and every block with

`d <= B-2`

cannot support a reset requiring `n_next+2>=N`. Thus

`d<=B-2 => n_next<=N-3`.

RL92 ran completed exact GMP chunks modulo

`2^10,000,056`

through `r=1,100,000`.

The global minimum over the complete range `0..1,100,000` is

`boxed: min bitlen(|mu_r|)=10,000,034 at r=378,722.}`

Therefore:

### Certificate 2.1 — extended deep rectangle

`boxed: d<=10,000,032 and r<=1,100,000 => n_next<=10,000,053}`

under a minimal reset.

Classification: **new exact finite certificate + inherited-interface analytic consequence**.

Timed-out scan attempts were not promoted. Every range used in this certificate is represented by a completed exact chunk, and the close-out verifier checks gap-free coverage.

---

## 3. Updated two-tier supporting line

Keep the frozen wide tier

`D_w=5,000,030`, `R_w=7,000,000`, `L_w=5,000,053`,

and use the RL92 deep tier

`D_d=10,000,032`, `R_d=1,100,000`, `L_d=10,000,053`.

The certified staircase union is

`U={(d,r): d<=D_d, r<=R_d} union {(d,r): d<=D_w, r<=R_w}`.

Set

`mu=1/(R_w+1)=1/7,000,001`,

`lambda=(R_w-R_d)/[(R_w+1)(D_w+1)]`

`      =5,900,000/35,000,222,000,031`.

Every integer point outside `U` satisfies

`boxed: lambda*d + mu*r >= 1.}`

Indeed the complement corners obey

1. `mu(R_w+1)=1`;
2. `lambda(D_w+1)+mu(R_d+1)=1`;
3. `lambda(D_d+1)>1`.

Hence the number of blocks outside the certified union obeys

`B_bad <= floor(lambda D_b + mu R_b^max)`.

Classification: **updated analytic staircase covering theorem consuming the new exact deep certificate**.

---

## 4. Transition necessary condition and top-stratum reduction

Conservatively charge every block in the union at the weaker deep successor ceiling

`L=10,000,053`.

The inherited exception accounting then gives the necessary condition

`b - floor(lambda D_b + mu R_b^max)`

`<= (k-1-b) + floor(D_b/(C-10,000,053)).`

For fixed `k`, raising `b` by one raises `D_b` by exactly `C`, while `R_b^max` is nondecreasing. The weighted bad-block floor therefore rises by at least

`floor(lambda*C)=7,105`.

The explicit `2b` contribution can improve the contradiction margin by only `2`, and short-successor capacity is nondecreasing. Therefore the contradiction margin strictly decreases with `b`.

### Theorem 4.1 — RL92 top-stratum reduction

It remains sufficient to test `b=k-1`.

Classification: **new parameterized analytic monotonicity theorem**.

---

## 5. Exact odd-interval propagation

The exact rational verifier evaluates the worst stratum `b=k-1` for every odd

`2,921,630,975 <= k <= 2,921,652,721`.

All `10,874` odd values violate the necessary condition.

At the final eliminated value

`k=2,921,652,721`, `b=k-1`,

the exact arithmetic is:

- `Q_min(k)=123,139,091,657,868,082,208`;
- `D_b=11,292,383,612,145,952`;
- `R_b^max=7,124,732,573,899,516`;
- weighted bad-block bound `2,921,379,957`;
- forced multiscale-good blocks `272,763`;
- short-successor capacity `267,967`;
- contradiction margin `+4,796`.

At the next odd

`k=2,921,652,723`,

the exact arithmetic is:

- `Q_min(k)=123,139,091,657,868,082,061`;
- `D_b=11,292,467,914,009,355`;
- `R_b^max=7,124,785,762,453,422`;
- weighted bad-block bound `2,921,401,766`;
- forced multiscale-good blocks `250,956`;
- short-successor capacity `267,969`;
- contradiction margin `-17,013`.

Therefore:

### Theorem 5.1 — RL92 odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`boxed: 2,921,630,975 <= k <= 2,921,652,721.}`

Since the inherited ledger still closes even terminal `k`, the updated branch-specific odd window is

`boxed: 2,921,652,723 <= k <= 42,150,931,559.}`

Classification: **new analytic theorem + exact finite 2-adic certificate + exact rational interval audit**.

---

## 6. Ultra-deep 15M probe and geometric barrier

RL92 tested an additional exact modulus scale:

`N=15,000,056`, `0<=r<=1,000`.

The exact scan gives

`min bitlen(|mu_r|)=15,000,048 at r=88`,

so locally

`d<=15,000,046 => n_next<=15,000,053`.

This is an **exact finite exploratory certificate**, but it is not used in Theorem 5.1.

Why it does not help yet: adding an ultra-deep tier below the current deep `r` band leaves the two active complement corners

`(0,R_w+1)` and `(D_w+1,R_d+1)`

unchanged. The current supporting line through those corners already satisfies the later depth constraints. In particular

`lambda(D_d+1)>1`.

The old deep depth-axis constraint becomes potentially active only when

`(R_w-R_d)(D_d+1) <= (R_w+1)(D_w+1)`.

With the RL92 depths this requires

`R_d >= ceil(7,000,000 - (7,000,001*5,000,031)/10,000,033)`

`    = 3,499,990`.

Thus the 15M low-`r` tier is geometrically premature for the present one-line cover.

Classification: **exact exploratory certificate + analytic method barrier / activation threshold**.

---

## 7. Tier-specific successor charging audit

RL91 asked whether wide-tier blocks could be charged at the stronger `C-5,000,053` successor-deficit cost instead of charging the whole union at `C-10,000,053`.

RL92 tested this direction. With only the inherited aggregate `D`/`R` budgets and the staircase population lower bound, no substantial forced wide-tier population is available: the relaxed resource model can place the currently forced covered blocks in the deep-only portion without exhausting the aggregate deficit budget. An optimized two-charge dual gives only a small numerical improvement at the live boundary and does not compete with frontier extension.

No tier-specific charging theorem is promoted as load-bearing in RL92.

Classification: **method audit / non-load-bearing negative result**.

---

## 8. Red-team audit

### RL81 common-mode freedom
Passed. No quotient state is promoted to a physical state. The new finite certificate consumes only the inherited physical cofactor bound and minimal-reset relation.

### RL79 generalized-increment homogeneity
Passed. The ordinary `+1` minimal-reset constant and physical maximum remain essential; no generalized-increment theorem is inferred.

### RL20 physical representative/packing separation
Passed. The weighted cover counts actual inherited synchronized blocks and does not convert quotient-address counts into physical representatives.

### Primitivity
Passed. No repeated cofactor or residue is interpreted as a repeated cycle state.

### First-Farey scope
Preserved. The interval theorem remains branch-specific.

### RL88 arbitrary-reset family
Passed. Arbitrarily high reset valuation is not denied globally; it is excluded only inside the certified `(d,r)` rectangles.

### Verification economy
Passed. Inherited expensive wide/deep scans were accepted after checksum/manifest/fast-verifier passage; only new frontier ranges were scanned.

---

## 9. Proof-state ledger additions

### New proved analytic mathematics

1. Updated staircase supporting line for `R_d=1,100,000`, `D_d=10,000,032`.
2. Updated top-stratum monotonicity with weighted decrement floor `7,105`.
3. Elimination of all `10,874` odd values from `2,921,630,975` through `2,921,652,721` on the exact first-Farey/full-phase branch.
4. Ultra-deep-tier geometric activation threshold `R_d>=3,499,990` for relaxing the current deep depth-axis constraint in the one-line cover.

### New exact finite certificates

1. Modulo `2^10,000,056`, all `r=0..1,100,000` have balanced inverse-residue bit length at least `10,000,034`, minimum at `r=378,722`; consequence `d<=10,000,032`, `r<=1,100,000` forces `n_next<=10,000,053`.
2. Exploratory, non-load-bearing: modulo `2^15,000,056`, all `r=0..1,000` have balanced inverse-residue bit length at least `15,000,048`, minimum at `r=88`; consequence `d<=15,000,046`, `r<=1,000` forces `n_next<=15,000,053`.

### Exact finite arithmetic audit

All `10,874` odd values in the new interval are checked using exact rational arithmetic after analytic reduction to `b=k-1`.

### Route limitation

The RL92 certificate has margin `-17,013` at `k=2,921,652,723`. The deep frontier route remains productive and is not exhausted.

---

## 10. RL93 route selection

Continue at

`k3=2,921,652,723`.

Priority order:

1. extend the exact `2^10,000,056` deep frontier beyond `r=1,100,000` in completed chunks;
2. after every meaningful extension, recompute the global minimum and exact supporting line, then propagate immediately through the odd interval;
3. watch for the deep global minimum dropping enough to alter the safe `D_d` threshold materially;
4. compare continued 10M extension against a fresh smaller-modulus middle tier once the work required to reach a useful `R_m>R_d` becomes competitive;
5. revisit ultra-deep/three-tier convexification only as the active staircase geometry approaches the `R_d≈3.5M` depth-axis activation regime, or if a middle tier changes the active corners earlier;
6. retain the conservative common successor charge unless new structure forces a nontrivial wide-tier population;
7. do not return to brute-force cofactor enumeration.

The sustained-attack rule remains mandatory.
