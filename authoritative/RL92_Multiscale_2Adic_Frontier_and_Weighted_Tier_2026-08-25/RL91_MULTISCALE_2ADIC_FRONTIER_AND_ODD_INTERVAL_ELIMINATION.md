# RL91 — multiscale 2-adic frontier and odd-interval elimination

Date: 2026-08-25

## 0. Executive outcome

RL91 continued the frozen RL90 tiered/asymmetric 2-adic rectangle target under the sustained-attack and verification-economy rules.

**No Gate A global, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.** Every terminal exclusion remains conditional on the exact first-Farey/full-phase Gate-A branch inherited from RL87–RL90.

RL90 had eliminated every odd terminal value through

`k=2,921,406,839`

and left the first route survivor

`k0=2,921,406,841`,

where its fixed `d<=500,036`, `r<=550,000` rectangle had contradiction margin `-67,747`.

RL91 first showed that the correct optimization is not a symmetric enlargement. The 2-adic inverse-residue frontier remains extremely deep over long exponent-deficiency bands, so increasing the modulus buys almost one-for-one ordinary-deficit depth while the successor charge changes negligibly relative to the physical block cap `C`.

Two exact finite certificates are frozen:

1. **Wide tier.** Modulo `2^5,000,056`, every balanced inverse residue for `0<=r<=7,000,000` has bit length at least `5,000,032`, with the minimum attained at `r=2,595,446`. Therefore

   `d<=5,000,030 and r<=7,000,000 => n_next<=5,000,053`.

2. **Deep low-r tier.** Modulo `2^10,000,056`, every balanced inverse residue for `0<=r<=300,000` has bit length at least `10,000,037`, with the minimum attained at `r=33,524`. Therefore

   `d<=10,000,035 and r<=300,000 => n_next<=10,000,053`.

The union of these two rectangles is converted into a single exact weighted covering theorem. Any block outside the union pays at least one unit of

`lambda*d + mu*r`,

where

`mu = 1/7,000,001`,

`lambda = 6,700,000 / (7,000,001 * 5,000,031)`.

Hence the number of blocks outside the certified union is at most

`floor(lambda*D_b + mu*R_b^max)`.

Conservatively charging every certified block with the weaker deep-tier successor ceiling `10,000,053` yields a new transition necessary condition. Its contradiction margin is strictly decreasing in block count; the weighted bad-block term alone rises by at least `8,068` when `b` rises by one, so `b=k-1` remains the worst stratum.

The exact rational interval verifier then eliminates every odd

`boxed: 2,921,406,841 <= k <= 2,921,630,973.}`

That is **112,067 consecutive odd values**.

At the last eliminated odd value the multiscale contradiction margin is `+586`. At the next odd

`k=2,921,630,975`,

the frozen two-tier certificate has margin `-23,150`.

The updated branch-specific odd surviving window is therefore

`boxed: 2,921,630,975 <= k <= 42,150,931,559, k odd.}`

The next productive route is to extend and optimize the multiscale frontier, especially the 10-million-bit low-`r` tier, and then consider a genuine three-tier convex/supporting-line cover rather than returning to a single rectangle.

---

## 1. Incoming verification economy gate

The supplied RL91 handover was checked before new mathematics:

- outer SHA-256 sidecar: PASS;
- fresh internal manifest: PASS;
- supplied fresh-unpack verification: PASS;
- RL90 fast verifier suite: PASS.

The reproduced incoming state included:

- `C=42,150,931,628`;
- `S_*=26,594,276,905`;
- RL90 rectangle `d<=500,036`, `r<=550,000`;
- RL90 successor ceiling `500,053`;
- eliminated endpoint `k=2,921,406,839`;
- surviving odd lower endpoint `k=2,921,406,841`;
- fixed RL90 margin at that endpoint `-67,747`;
- no global Gate-A promotion.

Under verification economy the frozen RL90 ledger was accepted. No historical expensive suite was recursively replayed.

GitHub consultation was read-only and used only to confirm the authoritative incoming RL91 commit/provenance.

---

## 2. Why modulus scale is the real optimization variable

For a minimal reset the inherited exact relation is

`3^(s+1)m - 1 = 2^(n_next+2)m_next`.     (2.1)

Put

`d=C-n`,

`r=S_*-s`.

The inherited physical cofactor bound is

`|m|<2^(d+1)`.     (2.2)

If one works modulo `2^N`, and the balanced representative `mu_r` of

`m == 3^(-(S_*+1-r)) (mod 2^N)`

satisfies

`|mu_r| >= 2^T`,

then every block with `d+1<=T` cannot support a reset with

`n_next+2>=N`.

Equivalently,

`d<=T-1 => n_next<=N-3`.     (2.3)

RL90 used `N=500,056`. RL91 observed that increasing `N` greatly enlarges the ordinary-deficit depth `T-1`, while the transition charge changes from roughly `C-500,000` to `C-N`, still essentially `C` at the million-bit scales relevant here.

Classification: **new route optimization / analytic reformulation of the inherited reset certificate interface**.

---

## 3. Exact wide-tier 5-million-bit certificate

The exact GMP scanner evaluates balanced representatives modulo

`2^5,000,056`

for every integer

`0<=r<=7,000,000`.

The complete gap-free chunk aggregation gives

`boxed: min bitlen(|mu_r|) = 5,000,032,}`

attained at

`r=2,595,446`.

Hence

`|mu_r| >= 2^5,000,031`

throughout the band.

By (2.2), if

`d<=5,000,030`,

then

`|m|<2^5,000,031`,

so the forbidden residue class cannot be occupied when a reset would require divisibility by `2^5,000,056`.

### Certificate 3.1 — wide rectangle

`boxed: d<=5,000,030 and r<=7,000,000 => n_next<=5,000,053.}`

Classification: **new exact finite certificate + analytic consequence**.

---

## 4. Exact deep low-r 10-million-bit certificate

A second exact GMP scan works modulo

`2^10,000,056`

for

`0<=r<=300,000`.

The three complete chunks are:

- `0..100,000`: minimum bit length `10,000,037` at `r=33,524`;
- `100,001..200,000`: minimum `10,000,041` at `r=117,716`;
- `200,001..300,000`: minimum `10,000,038` at `r=222,706`.

Thus globally

`boxed: |mu_r| >= 2^10,000,036 for 0<=r<=300,000.}`

### Certificate 4.1 — deep low-r rectangle

`boxed: d<=10,000,035 and r<=300,000 => n_next<=10,000,053.}`

Classification: **new exact finite certificate + analytic consequence**.

---

## 5. Weighted staircase covering theorem

Let

`D_w=5,000,030`, `R_w=7,000,000`,

`D_d=10,000,035`, `R_d=300,000`.

The certified union is

`U = {(d,r): d<=D_d, r<=R_d} union {(d,r): d<=D_w, r<=R_w}.`

Define

`mu = 1/(R_w+1) = 1/7,000,001`,

`lambda = (R_w-R_d)/[(R_w+1)(D_w+1)]`

`       = 6,700,000 / [7,000,001 * 5,000,031].`

Every integer point outside `U` has

`boxed: lambda*d + mu*r >= 1.}`     (5.1)

It is enough to check the three lower corners of the complement:

1. `r>=R_w+1`: `mu*r>=1`;
2. `r>=R_d+1`, `d>=D_w+1`: equality holds at `(D_w+1,R_d+1)`;
3. `r<=R_d`, `d>=D_d+1`: `lambda(D_d+1)>1.91>1`.

Therefore if `B_bad` is the number of actual blocks outside `U`, then

`B_bad <= floor(lambda sum d_i + mu sum r_i)`

and hence, using the frozen aggregate budgets,

### Theorem 5.1 — two-tier weighted population

`boxed: G_multi >= b - floor(lambda D_b + mu R_b^max).}`     (5.2)

This avoids double counting entirely; it is a direct supporting-line bound for the staircase complement.

Classification: **new analytic covering theorem consuming Certificates 3.1 and 4.1**.

---

## 6. Multiscale transition necessary condition

Every block in the certified union forces, under a minimal complete reset, a successor of length at most

`L=10,000,053`,

because the wide tier actually gives the stronger `5,000,053` ceiling.

As in RL89–RL90:

- nonminimal/zero-return exceptional transitions are at most `k-1-b`;
- every genuinely short successor of length at most `L` consumes at least `C-L` ordinary deficit;
- the number of such successors is therefore at most `floor(D_b/(C-L))`.

Thus every survivor must satisfy

### Theorem 6.1 — multiscale transition necessary condition

`boxed:`

`b - floor(lambda D_b + mu R_b^max)`

`<= (k-1-b) + floor(D_b/(C-10,000,053)).`     (6.1)

Classification: **new analytic counting theorem**.

---

## 7. Top block-count stratum remains worst

For fixed `k`, increasing `b` by one increases `D_b` by exactly `C`.

The safe exponent-deficiency budget `R_b^max` is nondecreasing in `b`.

Therefore the weighted bad-block quantity grows by at least

`floor(lambda*C)=8,068`

per added block.

The explicit term `b-(k-1-b)` can improve the contradiction margin by only `2`, while the short-successor capacity is nondecreasing.

Hence the contradiction margin decreases by at least

`8,068-2 = 8,066`

when `b` increases by one.

### Theorem 7.1 — multiscale top-stratum reduction

For every fixed `k`, if (6.1) fails at `b=k-1`, it fails for every feasible lower `b` as well.

Classification: **new analytic monotonicity theorem**.

---

## 8. Exact odd-interval elimination

The exact rational verifier evaluates only the worst stratum

`b=k-1`

for every odd

`2,921,406,841 <= k <= 2,921,630,973`.

Every one violates the necessary condition (6.1).

There are exactly

`boxed: 112,067}`

odd values in this interval.

At the final eliminated value

`k=2,921,630,973`, `b=k-1`,

the exact arithmetic is:

- `Q_min(k)=123,139,091,657,869,683,283`;
- `D_b=10,375,685,149,499,133`;
- `R_b^max=6,546,360,238,723,941`;
- weighted bad-block bound `2,921,384,173`;
- forced multiscale-good blocks `246,799`;
- short-successor capacity `246,213`;
- contradiction margin `586`.

Therefore:

### Theorem 8.1 — RL91 odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`boxed: 2,921,406,841 <= k <= 2,921,630,973.}`

Since even terminal `k` remains closed analytically in the inherited ledger, the updated branch-specific odd window is

`boxed: 2,921,630,975 <= k <= 42,150,931,559.}`

Classification: **new analytic theorem + two exact finite 2-adic certificates + exact rational interval audit**.

---

## 9. Exact failure point of the frozen two-tier certificate

At the next odd value

`k=2,921,630,975`, `b=k-1`,

the exact arithmetic is:

- `Q_min(k)=123,139,091,657,869,683,136`;
- `D_b=10,375,769,451,362,536`;
- `R_b^max=6,546,413,427,277,847`;
- weighted bad-block bound `2,921,407,909`;
- forced multiscale-good blocks `223,065`;
- short-successor capacity `246,215`;
- frozen multiscale margin `-23,150`.

This is a **method threshold**, not a counterexample and not evidence of survival.

---

## 10. Red-team audit

### RL81 common-mode freedom

Passed. The argument does not reconstruct a physical cycle state from quotient data. The finite certificates consume the already-owned physical cofactor bound and exact minimal-reset relation.

### RL79 generalized-increment homogeneity

Passed. The synchronized local transport is homogeneous, but the finite physical maximum and the minimal-reset constant `-1` are ordinary-`+1` resources. No generalized-increment theorem is silently promoted.

### RL20 physical packing separation

Passed. No quotient/address count is promoted to a count of physical representatives. The weighted covering counts actual synchronized blocks already present in the inherited physical decomposition.

### Primitivity

Passed. No repeated cofactor or repeated difference is interpreted as a repeated cycle state. The inherited nonzero odd cofactor condition is used only in the local reset relation.

### First-Farey scope

Preserved. The interval theorem remains branch-specific.

### RL88 arbitrary-reset family

Passed. Arbitrarily high reset valuation remains possible with sufficiently large odd cofactor. RL91 excludes high resets only inside two certified `(d,r)` regions forced in bulk by aggregate budgets.

### Verification economy

Passed. Historical expensive suites were not recursively replayed.

---

## 11. Exploratory checkpoints and correction ledger

Several intermediate certificates were obtained during the sustained attack, including lower modulus scales and narrower `r` bands. They are superseded by the final two-tier theorem and are not separately load-bearing.

Incomplete/timed-out parallel scan chunks were never treated as evidence. Every range used in the frozen wide-tier certificate is covered by a completed exact chunk; the close-out aggregation checks the union is gap-free.

No inherited theorem is demoted.

The earlier provisional close-out endpoint `2,921,598,921` from the `5,000,056`-bit / `r<=5,100,000` checkpoint is superseded by Theorem 8.1.

---

## 12. Proof-state ledger additions

### New proved analytic mathematics

1. Modulus-scale optimization principle for the inherited minimal-reset certificate interface.
2. Two-tier supporting-line/staircase covering theorem (5.1)–(5.2).
3. Multiscale transition necessary condition (6.1).
4. Multiscale top-stratum monotonicity with weighted decrement floor `8,068`.
5. Elimination of every odd `k` from `2,921,406,841` through `2,921,630,973` on the exact first-Farey/full-phase branch.
6. Updated branch-specific surviving odd lower endpoint `2,921,630,975`.

### New exact finite certificates

1. Modulo `2^5,000,056`, all `r=0..7,000,000` have balanced inverse-residue bit length at least `5,000,032`; consequence `d<=5,000,030`, `r<=7,000,000` forces `n_next<=5,000,053`.
2. Modulo `2^10,000,056`, all `r=0..300,000` have balanced inverse-residue bit length at least `10,000,037`; consequence `d<=10,000,035`, `r<=300,000` forces `n_next<=10,000,053`.

### New exact finite arithmetic audit

All `112,067` odd values in the eliminated interval are checked using exact rational arithmetic after the analytic reduction to `b=k-1`.

### Route limitation

The frozen two-tier certificate has margin `-23,150` at `k=2,921,630,975`. The multiscale route remains productive; a larger deep tier, wider tier, or three-tier convex cover is required.

---

## 13. RL92 route selection

Continue at

`k2=2,921,630,975`.

Priority order:

1. extend the `2^10,000,056` deep low-`r` tier beyond `r=300,000` in completed exact chunks;
2. recompute the optimal supporting line after every meaningful deep-tier extension;
3. widen the `2^5,000,056` tier beyond `r=7,000,000` only when its gain/cost beats deep-tier extension;
4. promote a three-tier convex/staircase covering if another modulus scale yields a favorable corner;
5. improve transition charging by retaining tier-specific successor ceilings rather than always charging the union at the weaker `10,000,053` ceiling, if this buys material range;
6. if `k2` closes, propagate immediately to the exact next failure point;
7. do not return to brute-force cofactor enumeration.

The sustained-attack rule remains mandatory.
