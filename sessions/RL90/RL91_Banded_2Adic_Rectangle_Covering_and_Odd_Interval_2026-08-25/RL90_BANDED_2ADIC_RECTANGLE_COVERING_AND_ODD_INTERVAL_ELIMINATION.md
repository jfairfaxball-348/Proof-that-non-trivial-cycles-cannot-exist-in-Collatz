# RL90 — banded 2-adic rectangle covering and odd-interval elimination

Date: 2026-08-25

## 0. Executive outcome

RL90 continued the frozen RL89 near-capacity transition attack under the mandatory sustained-attack and verification-economy rules.

**No Gate A global, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.** Every terminal exclusion here remains conditional on the exact first-Farey/full-phase Gate-A branch inherited from RL87–RL89.

RL89 had raised the surviving odd first-Farey lower endpoint to

`k = 2,921,384,821`

and localized every survivor there to `b=k-2` or `b=k-1`. Its requested RL90 route was to extend the tiny-cofactor 2-adic covering from deficit 28 toward deficits 36 and 51.

RL90 finds a stronger aggregate splice that avoids enumerating the entire `|m|<2^37` or `|m|<2^52` cofactor ranges.

The first-Farey physical maximum bounds not only the synchronized block length `n` but also the number `s` of synchronized `11` columns inside every block:

`boxed: s <= S_* = 26,594,276,905.}`

Writing the ordinary block deficit and exponent deficiency as

`d_i = C-n_i`,

`r_i = S_*-s_i`,

RL88's aggregate reset inequality supplies an explicit global upper budget on `sum r_i`.

This converts the huge cofactor problem into a **two-dimensional covering rectangle**. An exact GMP certificate scans only the consecutive exponent-deficiency band

`0 <= r <= 550,000`

modulo `2^500056`. Across the entire band the balanced residue of

`3^{-(s+1)}`

has bit length at least `500038`; equivalently every such residue has absolute value at least `2^500037`.

Therefore, if also

`d <= 500,036`,

then the inherited physical cofactor bound

`|m| < 2^(d+1) <= 2^500037`

prevents a minimal reset from producing a next block of length `>=500,054`. Hence

`boxed: d<=500,036 and r<=550,000 => n_next<=500,053.}`

Combining the forced population of this rectangle with the RL89 transition-deficit accounting eliminates **every feasible block-count stratum** for every odd

`boxed: 2,921,384,821 <= k <= 2,921,406,839.}`

That is `11,010` consecutive odd terminal values.

The updated branch-specific surviving odd window is therefore

`boxed: 2,921,406,841 <= k <= 42,150,931,559, k odd.}`

At the last eliminated odd value the worst-stratum contradiction margin is still `197,551`. At the next odd value the same fixed rectangle has margin `-67,747`, so the fixed certificate no longer closes the argument. This is a route threshold, not evidence of a survivor.

Larger square and asymmetric exploratory scans were attempted after the first successful band, but did not finish within the reliable session compute window. They are **not** promoted to evidence or certificates. RL91 should optimize the rectangle asymmetrically/tierwise at the new lower endpoint rather than restarting generic cofactor enumeration.

---

## 1. Incoming verification economy gate

The supplied RL90 handover was checked before new mathematics:

- outer SHA-256 sidecar: PASS;
- freshly unpacked internal `SHA256SUMS.txt`: PASS;
- supplied fresh-unpack RL89 verification: PASS;
- `bash verification/run_fast_rl89_verifiers.sh`: PASS.

The reproduced incoming state included:

- `C=42,150,931,628`;
- exact RL89 `|m|<2^29` long-reset certificate;
- eliminated endpoint `k=2,921,384,819`;
- surviving odd lower endpoint `k=2,921,384,821`;
- at that endpoint, `b>=k-2`;
- no global Gate-A promotion.

Under verification economy the frozen RL89 ledger was accepted. No historical expensive suite was recursively replayed.

Selective GitHub consultation was read-only and restricted to live interfaces:

- RL81 physical common-mode barrier;
- RL87 physical difference ownership / first-Farey maximum;
- RL88 aggregate reset budget;
- RL73 count/skew interface as already consumed by RL88.

---

## 2. A second physical block cap: synchronized `11` count

For a maximal height-one synchronized block, RL89 writes the entry difference as

`delta_entry = 2^n m`,

where `m` is signed odd and nonzero. If the block contains `s` synchronized `11` columns, then

`delta_exit = 3^s m`.

RL87's genuine physical ownership gives

`|delta_exit| < M`,

while the first-Farey logarithmic maximum satisfies

`log_2 M < 42,150,931,628.751333`.

Since `|m|>=1`,

`3^s < M`.

Using the exact 260-term rational enclosure for `log_2 3`, the verifier proves

`boxed: s <= S_* = 26,594,276,905.}`     (2.1)

Classification: **new analytic corollary of RL87 physical ownership + inherited exact rational logarithm enclosure**.

This is distinct from the existing block-length ceiling

`n<=C=42,150,931,628`.

---

## 3. Ordinary deficit and exponent deficiency

For block `i` define

`d_i=C-n_i >=0`,

`r_i=S_*-s_i >=0`.

For `b` nonempty blocks let

`D_b=sum d_i = Cb-Q`.

RL88 proved

`Q - beta sum s_i < log_2 M + beta R_exc + b`,

where `beta=log_2 3` and the complete-excursion odd-count resource satisfies

`R_exc <= H <= k-1`.

Substituting `s_i=S_*-r_i` gives

`sum r_i < (k-1) + b S_* + [log_2 M + b - Q]/beta`.     (3.1)

To obtain a safe explicit upper bound, use

- `log_2 M < LOGM_UP`;
- `Q >= Q_min(k)` from RL88/RL89;
- the exact rational upper endpoint `beta_+` for the negative quotient term.

Thus the integer total exponent deficiency obeys

`boxed: sum r_i <= R_b^max,}`

where

`R_b^max = ceil((k-1)+bS_*+(LOGM_UP+b-Q_min(k))/beta_+) - 1`.     (3.2)

Classification: **new analytic reparameterization of the RL88 aggregate reset theorem**.

---

## 4. Exact banded 2-adic certificate

For a minimal `01,10` reset RL89 proved

`3^(s+1)m - 1 = 2^(n_next+2)m_next`.     (4.1)

Put

`r=S_*-s`.

Then the relevant exponent is

`a=s+1=S_*+1-r`.

The RL90 GMP verifier works modulo

`2^500056`

and checks every integer

`0<=r<=550,000`.

For each `r`, let `mu_r` be the balanced representative of the unique residue

`m == 3^(-a) (mod 2^500056)`.

The exact scan returns:

- global minimum balanced bit length: `500038`;
- attained at `r=298,303`;
- on the extension tail `500001<=r<=550000`, minimum bit length `500041` at `r=519,699`.

Therefore

`boxed: |mu_r| >= 2^500037 for every 0<=r<=550,000.}`     (4.2)

Now use the inherited physical cofactor bound

`|m|<2^(d+1)`.

If

`d<=500,036`,

then

`|m|<2^500037`.

If a minimal reset had

`n_next>=500,054`,

then (4.1) would force divisibility by `2^500056`, hence `m` would equal the forbidden residue class represented by `mu_r`. Contradiction.

### Certificate 4.1 — rectangle short-successor theorem

`boxed: d<=500,036 and r<=550,000 => n_next<=500,053}`

for every minimal reset in the full physical exponent range represented by the band.

Classification: **new exact finite certificate + analytic consequence**.

This is not an enumeration of all cofactors below `2^500037`: it scans `550,001` consecutive exponent deficiencies and uses uniqueness of the inverse residue modulo a power of two.

---

## 5. Two-budget rectangle population

Let

`D_*=500,036`,

`R_*=550,000`,

`L_*=500,053`.

At most

`floor(D_b/(D_*+1))`

blocks have `d_i>D_*`.

At most

`floor(R_b^max/(R_*+1))`

blocks have `r_i>R_*`.

Hence at least

`boxed: G_rect >= b - floor(D_b/500037) - floor(R_b^max/550001)}`     (5.1)

actual blocks lie in the certified rectangle.

Every such block followed by a minimal complete excursion and a nonempty synchronized return forces a successor of length at most `L_*`.

As in RL89, exceptional transitions are bounded by

`H-b <= k-1-b`.

Every genuinely short successor consumes at least

`C-L_*`

ordinary deficit, so their number is at most

`floor(D_b/(C-L_*) )`.

Therefore every survivor must satisfy

### Theorem 5.1 — rectangle transition necessary condition

`boxed:`

`b - floor(D_b/500037) - floor(R_b^max/550001)`

`<= (k-1-b) + floor(D_b/(C-500053)).`     (5.2)

Classification: **new analytic counting theorem consuming Certificate 4.1**.

---

## 6. Worst block-count stratum is always `b=k-1`

For fixed `k`, incrementing `b` by one increases

`D_b`

by exactly `C`.

Thus

`floor(D_(b+1)/500037)-floor(D_b/500037)`

is at least

`floor(C/500037)=84,295`.

The exponent-deficiency penalty and short-successor penalty are nondecreasing in `b`. Meanwhile the explicit `b-(k-1-b)` part of the contradiction margin gains only `2`.

Hence the margin decreases by at least

`84,295-2 = 84,293`

when `b` increases by one.

### Theorem 6.1 — top-stratum reduction

For every fixed `k`, if (5.2) fails at `b=k-1`, it fails for every feasible lower `b` as well.

Classification: **new analytic monotonicity theorem**.

This removes the need to enumerate all block-count strata at each terminal `k`.

---

## 7. Exact odd interval elimination

The bundled exact rational verifier evaluates the top stratum

`b=k-1`

for every odd

`2,921,384,821 <= k <= 2,921,406,839`.

Every one violates the necessary condition (5.2).

There are exactly

`11,010`

odd values in this interval.

At the final eliminated value

`k=2,921,406,839`, `b=k-1`,

the exact arithmetic is:

- `Q_min(k)=123,139,091,657,886,183,891`;
- `D_b=928,228,223,488,373`;
- `R_b^max=585,678,568,122,399`;
- ordinary-deficit bad blocks `1,856,319,079`;
- exponent-deficiency bad blocks `1,064,868,187`;
- forced rectangle blocks `219,572`;
- short-successor capacity `22,021`;
- contradiction margin `197,551`.

Therefore:

### Theorem 7.1 — RL90 odd-interval exclusion

No exact first-Farey/full-phase Gate-A survivor has odd

`boxed: 2,921,384,821 <= k <= 2,921,406,839.}`

Since even terminal `k` remains closed analytically in the inherited ledger, the updated branch-specific odd window is

`boxed: 2,921,406,841 <= k <= 42,150,931,559.}`

Classification: **new analytic theorem + exact banded finite certificate + exact rational interval audit**.

---

## 8. Exact failure point of the fixed rectangle

At the next odd value

`k=2,921,406,841`, `b=k-1`,

the same fixed rectangle gives:

- `Q_min(k)=123,139,091,657,886,183,744`;
- `D_b=928,312,525,351,776`;
- `R_b^max=585,731,756,676,305`;
- ordinary-deficit bad count `1,856,487,670`;
- exponent-deficiency bad count `1,064,964,894`;
- raw rectangle lower bound `-45,724`;
- short-successor capacity `22,023`;
- fixed-certificate margin `-67,747`.

So Certificate 4.1 alone does not eliminate this value.

This is a **method threshold**, not a counterexample and not evidence for survival.

---

## 9. Red-team audit

### RL81 common-mode barrier

Passed. The argument never reconstructs a physical cycle state from `J` or repeated difference data. The new cap on `s` and the cofactor bound use genuine physical difference ownership already established in RL87.

### RL79 generalized-increment homogeneity

Passed for the composite theorem. The local synchronized difference transport is homogeneous, but the load-bearing finite physical maximum and the minimal-reset constant `-1` belong to the ordinary `+1` map.

### RL20 physical packing separation

Passed. No quotient/address count is promoted to a count of physical representatives. Physical information enters only through the owned difference scale and first-Farey maximum.

### Primitivity

Passed. No repeated cofactor or difference is interpreted as a repeated cycle state.

### First-Farey scope

Preserved. The new interval is branch-specific.

### RL88 arbitrary-reset family

Passed. Arbitrarily high reset valuation remains possible with sufficiently large odd cofactor. RL90 only excludes it inside a certified cofactor/exponent rectangle forced in bulk by physical and aggregate budgets.

### Verification economy

Passed. Historical suites were not recursively replayed.

---

## 10. Exploratory continuations not promoted

After obtaining the first successful band certificate, RL90 attempted larger square and asymmetric extensions. Those explorations exceeded the reliable session compute window before a complete exact certificate was produced.

They are recorded only as route guidance:

- larger square bands have unnecessary quadratic-style cost relative to the actual bottleneck;
- near the new endpoint, the ordinary-deficit and exponent-deficiency budgets are asymmetric;
- a tiered union of rectangles or an optimized asymmetric rectangle should buy more terminal range per modulus bit / exponent scan than a naive larger square.

No numerical result from an incomplete scan is retained as evidence.

---

## 11. Proof-state ledger additions

### New proved analytic mathematics

1. Per-block synchronized-`11` cap `s<=26,594,276,905` on the exact first-Farey physical branch.
2. Exact exponent-deficiency budget (3.1) and safe integer form (3.2).
3. Two-budget rectangle population inequality (5.1).
4. Rectangle transition necessary condition (5.2).
5. Strict block-count monotonicity: top stratum `b=k-1` is worst.
6. Elimination of every odd `k` from `2,921,384,821` through `2,921,406,839`.
7. Updated branch-specific surviving odd lower endpoint `2,921,406,841`.

### New exact finite certificate

Modulo `2^500056`, for every `0<=r<=550,000`, the balanced representative of `3^{-(S_*+1-r)}` has absolute value at least `2^500037`. Consequently

`d<=500,036` and `r<=550,000` under a minimal reset force `n_next<=500,053`.

### New exact finite arithmetic audit

All `11,010` odd values in the eliminated interval were checked using exact rational arithmetic after the analytic reduction to `b=k-1`.

### Route barrier / limitation

The fixed rectangle ceases to contradict at `k=2,921,406,841`; its margin is `-67,747` there. A larger or tiered covering theorem is required.

No inherited theorem is demoted.

---

## 12. RL91 route selection

Continue the same route at

`k2=2,921,406,841`.

Do **not** restart generic quotient packing or brute-force `2^d` cofactor scans.

The best next target is an optimized **tiered/asymmetric 2-adic rectangle covering**:

1. calculate the exact deficit-deficiency trade curve at `b=k-1`;
2. choose two or more rectangles `(d<=D_j, r<=R_j)` that maximize forced population per certificate cost;
3. scan only the necessary exponent bands modulo the smallest powers of two that force useful successor caps;
4. combine rectangle populations without double-counting, preferably by nested thresholds;
5. eliminate `k2`, then propagate to the next odd interval until a genuinely new threshold is reached;
6. only if sparse exceptional cofactors become the bottleneck, consider a common-mode selector and re-run RL81/RL20/primitivity red teams.

The sustained-attack rule remains mandatory: a newly eliminated endpoint is a checkpoint, not an automatic close condition.
