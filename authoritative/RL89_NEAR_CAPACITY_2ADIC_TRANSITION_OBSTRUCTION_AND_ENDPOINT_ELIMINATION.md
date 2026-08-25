# RL89 — near-capacity 2-adic transition obstruction and lower-endpoint elimination

Date: 2026-08-25

## 0. Executive outcome

RL89 executed the authoritative near-capacity block-rigidity / odd-cofactor packing target from a checksum-clean RL89 handover.

**No Gate A global, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.** All new terminal statements below remain conditional on the exact first-Farey/full-phase Gate-A branch inherited from RL87/RL88.

The main new result is stronger than the requested repeated-type multiplicity route and avoids the common-mode problem entirely.

RL88 forced the first surviving odd endpoint

`k0 = 2,921,384,819`

into an almost saturated block regime. RL89 proves that, in the saturated-area grammar, a near-maximal block with small odd exit cofactor cannot be followed by another long block through the ordinary minimal `01,10` reset.

The exact minimal-reset recurrence is

`3^(s+1)m - 1 = 2^(n_next+2)m_next`.

An exact finite 2-adic discrete-log certificate checks **every signed odd**

`0 < |m| < 2^29`

and every physical exponent

`1 <= s+1 <= C+1 = 42,150,931,629`.

It proves

`v2(3^(s+1)m - 1) <= 65`.

Therefore every block with deficit

`C-n <= 28`

followed by a minimal excursion must be followed by a synchronized block of length at most

`63`.

At `k0`, the aggregate block deficit permits at most zero or one such short nonempty block, depending on the exact block count, while hundreds of millions to billions of deficit-`<=28` blocks are forced. The number of nonminimal/zero-successor exceptions is bounded by the tiny area slack. This eliminates **all** endpoint block-count cases.

Hence:

`boxed: k = 2,921,384,819 is impossible on the exact first-Farey/full-phase branch.}`

Since even terminal `k` is already closed analytically, the surviving odd first-Farey window improves to

`boxed: 2,921,384,821 <= k <= 42,150,931,559, k odd.}`

RL89 then continues rather than closing at that milestone.

At the next odd value

`k1=2,921,384,821`,

the same transition/deficit theorem eliminates the two lower block-count cases and forces

`boxed: b >= k1-2 = 2,921,384,819.}`

Consequently every putative `k1` survivor again has saturated excursion grammar: all complete excursions are minimal `01,10`, except that one height-two plateau `01,00,10` or `01,11,10` is allowed in the unique `H=e+1` case, and at most one height-one return can have a zero-length synchronized block.

The endpoint transition obstruction also yields nontrivial fixed-block-count exclusion intervals:

- exactly `b=2,921,384,817` blocks is impossible through `k=3,527,154,083`;
- exactly `b=2,921,384,818` blocks is impossible through `k=3,116,403,917`.

This does not eliminate those entire `k` intervals because larger `b` remains available. It is a structural interval theorem, not a terminal interval closure.

The new strategic boundary is clear. At `k1`, after the low-`b` cases are removed, the two surviving block counts have average deficits about `36.58` and `51.01`. Closing `k1` by the same method therefore requires extending the exact 2-adic cofactor covering from `|m|<2^29` to roughly the deficit-36 and deficit-51 regimes, or adding a new selector that bounds the sparse long-reset cofactor exceptions.

---

## 1. Incoming verification economy gate

The supplied RL89 handover was checked before new mathematics:

- outer SHA-256 sidecar: PASS;
- freshly unpacked internal `SHA256SUMS.txt`: PASS;
- `bash verification/run_fast_rl88_verifiers.sh`: PASS.

The incoming RL88 verifier reproduced:

- 30,420 exact `(d,T)` arithmetic checks;
- 625 complete excursion words;
- 711 midpoint-congruence checks;
- 600 arbitrary-reset-family checks;
- exact first-Farey raw threshold `2,921,384,818`;
- odd threshold `2,921,384,819`;
- `Q(k0)>=123,139,091,657,887,804,990`;
- minimum nonempty block count `k0-2`;
- `225,242,372` deficit-`<=23` blocks under the padded `k0-1` slot count.

Under the verification-economy rule the frozen RL88 ledger was accepted. Historical expensive certificates were not recursively replayed.

Selective GitHub consultation was read-only and limited to the live interfaces:

- RL73's exact area/block-return counting framework;
- RL81's physical common-mode barrier, used as a red team.

---

## 2. Excess-area decomposition and saturated excursion grammar

Let the post-first-mismatch height be `d_i>=1`, and let

`H=sum_i (d_i-1)`

be the inherited area. Let `e` be the number of `10` columns. Every `10` has pre-height at least two.

Define the excess area

`E = H-e`.

Then exactly

`boxed: E = sum_(10 columns)(d_i-2) + sum_(non-10 columns)(d_i-1).}`     (2.1)

Every summand is a nonnegative integer.

### Theorem 2.1 — zero-excess grammar

If `H=e`, every complete height-one excursion is exactly

`boxed: 01,10.}`

#### Proof

Equality in (2.1) forces every `10` to have pre-height exactly two and every non-`10` column to have pre-height one. A complete excursion leaves height one by `01`, reaching height two. At height two the next column cannot be `00` or `11` because either would contribute positive excess, and cannot be another `01` for the same reason. Hence it is `10`, returning immediately to height one. QED.

### Theorem 2.2 — one-excess grammar

If `H=e+1`, every complete excursion is minimal `01,10` except exactly one excursion, which is one of

`boxed: 01,00,10}`

or

`boxed: 01,11,10.}`

#### Proof

If any `10` had pre-height at least three, its term `(d_i-2)` in (2.1) would contribute at least one. Reaching height three requires an earlier `01` at pre-height at least two, which contributes at least one more through the non-`10` sum. That would force `E>=2`.

Hence all `10` columns still occur at pre-height two. The unique excess unit must therefore come from exactly one non-`10` column at height two. It cannot be `01`, because that would reach height three and force a later `10` at height three. It is therefore `00` or `11`, after which the excursion must return by `10`. QED.

Classification: **new analytic grammar theorem**.

The bundled verifier exhausts all complete excursions through length eight and confirms that these are exactly the `E<=1` words.

---

## 3. Exact cofactor recurrences

For a maximal height-one synchronized block write

`delta_entry = 2^n m`,

where `m` is signed, odd, and nonzero. If the synchronized block contains `s` `11` columns, then its exit difference is exactly

`boxed: delta_exit = 3^s m.}`     (3.1)

The synchronized `00` columns divide the difference by two and the synchronized `11` columns multiply it by `3/2`; after `n` synchronized columns the factor `2^n` is exhausted.

### Minimal excursion

For a `01,10` excursion, direct ordinary shortcut-Collatz algebra gives

`delta_next = (3 delta_exit -1)/4`.

Thus

`boxed: 3^(s+1)m -1 = 2^(n_next+2)m_next.}`     (3.2)

### One-extra-area plateau excursions

For `01,00,10`,

`delta_next = 3(delta_exit-1)/8`,

so

`boxed: 3^(s+1)m -3 = 2^(n_next+3)m_next.}`     (3.3)

For `01,11,10`,

`delta_next = (9 delta_exit-5)/8`,

so

`boxed: 3^(s+2)m -5 = 2^(n_next+3)m_next.}`     (3.4)

Classification: **new analytic recurrence family**.

The ordinary constants `-1,-3,-5` are essential. This is not a homogeneous generalized-increment argument.

---

## 4. 2-adic exponent uniqueness

For `t>=3`,

`ord_(2^t)(3)=2^(t-2)`.

Equivalently, by the standard 2-adic LTE identity,

`v2(3^(2^j)-1)=j+2` for `j>=1`.

Therefore if fixed odd `m` satisfies

`3^a m == 1 (mod 2^t)`,

then `a` is unique modulo `2^(t-2)` whenever a solution exists.

In the physical range `a=s+1<=C+1`, once `t>=39` the modulus period is already vastly larger than `C+1`; hence there is at most one physical exponent `a` for a fixed `m`.

This uniqueness alone is not enough for closure, but it makes an exact finite discrete-log scan possible without enumerating the `~4.2e10` physical exponents.

Classification: **analytic multiplicative-order lemma**.

---

## 5. Exact finite 2-adic cofactor certificate

The RL89 C verifier exhausts every signed odd

`0<|m|<2^29`

and reconstructs the unique discrete logarithm `a` satisfying

`3^a = m^(-1) (mod 2^64)`

when it exists. The bit-lift uses the exact order structure from Section 4 and rejects any lifted exponent outside

`1<=a<=C+1=42,150,931,629`.

There are exactly two candidates modulo `2^64` in that entire range:

`(m,a)=(101,319,985, 27,039,197,284)`,

`(m,a)=(303,959,955, 27,039,197,283)`.

The second is simply the first multiplied by `3` with the exponent reduced by one. Exact modular evaluation gives

`v2(3^a m-1)=65`

for both.

Hence:

### Certificate 5.1 — near-cap minimal-reset ceiling

For every signed odd `m` with

`0<|m|<2^29`

and every integer

`1<=a<=C+1`,

`boxed: v2(3^a m-1)<=65.}`

Therefore, under the minimal recurrence (3.2),

`boxed: C-n <=28  ==>  n_next<=63.}`     (5.1)

The implication uses RL88's physical cofactor bound: a block of deficit `d=C-n` has

`|m|<2^(d+1)`.

Classification: **new exact finite certificate + analytic consequence**.

This certificate is deliberately finite and auditable. It is not promoted to a general theorem for arbitrary cofactor size.

---

## 6. Transition-deficit counting lemma

Let a survivor have `b` nonempty height-one synchronized blocks, total synchronized length `Q`, and actual block-capacity deficit

`boxed: D_b = Cb-Q.}`     (6.1)

### Near-cap population

If `G_28` is the number of actual blocks with deficit at most 28, then every other block consumes at least 29 deficit units. Therefore

`boxed: G_28 >= b - floor(D_b/29).}`     (6.2)

### Short-block capacity

By Certificate 5.1, a deficit-`<=28` block followed by a minimal excursion and then a nonempty synchronized block forces the next block to have length at most 63.

Every such short nonempty block consumes at least `C-63` deficit units, so their number is at most

`boxed: S <= floor(D_b/(C-63)).}`     (6.3)

### Exceptional transitions

A near-cap block can avoid the minimal-reset implication only if

1. its following complete excursion is nonminimal; or
2. the following height-one synchronized block has zero length.

Each nonminimal excursion consumes at least one unit of `H-e`; the number of zero-length return slots is at most `e-b`. Thus the total number `X` of exceptional block transitions satisfies

`X <= (H-e)+(e-b)=H-b <= k-1-b`.

Therefore every survivor must satisfy the necessary inequality

### Theorem 6.1 — transition-deficit necessary condition

`boxed: G_28 <= (k-1-b) + floor(D_b/(C-63)).}`     (6.4)

where `G_28` may be replaced by the lower bound in (6.2).

Classification: **new analytic counting theorem consuming the exact finite certificate**.

This is the central RL89 splice. It does not identify or pack physical states, so the RL81 common-mode barrier is not triggered.

---

## 7. Elimination of the RL88 lower endpoint

Set

`k0=2,921,384,819`,

`Q0=123,139,091,657,887,804,990`.

RL88 gives

`b>=ceil(Q0/C)=2,921,384,817=:B0`.

Also `b<=e<=H<=k0-1`, so only two block counts are possible:

`b=B0` or `b=B0+1=k0-1`.

### Case A: `b=B0=2,921,384,817`

Exact actual deficit:

`D_b=22,556,487,086`.

Hence

`G_28 >= 2,143,574,918`,

while

`floor(D_b/(C-63))=0`

and

`k0-1-b=1`.

The necessary margin in (6.4) fails by

`2,143,574,917`.

Impossible.

### Case B: `b=B0+1=2,921,384,818`

Exact actual deficit:

`D_b=64,707,418,714`.

Hence

`G_28 >= 690,094,518`,

while at most one short nonempty block fits:

`floor(D_b/(C-63))=1`,

and there is no area/block-count exception:

`k0-1-b=0`.

The necessary margin fails by

`690,094,517`.

Impossible.

### Theorem 7.1 — endpoint elimination

`boxed: k=2,921,384,819 is impossible on the exact first-Farey/full-phase Gate-A branch.}`

Since inherited Gate A already eliminates even terminal `k`, the updated exact first-Farey odd window is

`boxed: 2,921,384,821 <= k <= 42,150,931,559.}`

Classification: **new analytic theorem + exact finite certificate**.

---

## 8. Continue-through-milestone propagation to the next odd k

RL89 does not stop at Theorem 7.1.

Set

`k1=2,921,384,821`.

The same exact reset-budget lower function gives

`Q(k1)>=123,139,091,657,887,804,843`.

Thus the minimum block count remains

`B0=2,921,384,817`.

The possible block counts are now `B0,B0+1,B0+2,B0+3`.

Applying (6.4):

### `b=B0`

- `D_b=22,556,487,233`;
- `G_28>=2,143,574,913`;
- short-block allowance `0`;
- exception allowance `3`;
- violation margin `2,143,574,910`.

Impossible.

### `b=B0+1`

- `D_b=64,707,418,861`;
- `G_28>=690,094,513`;
- short-block allowance `1`;
- exception allowance `2`;
- violation margin `690,094,510`.

Impossible.

Therefore:

### Theorem 8.1 — next-odd block-count localization

Any exact first-Farey/full-phase survivor at

`k=2,921,384,821`

must satisfy

`boxed: b>=2,921,384,819=k-2.}`

Since `b<=e<=H<=k-1`, any such survivor has only the following structural possibilities:

1. `b=k-1`, hence `e=H=k-1`: all excursions minimal;
2. `b=k-2`, `e=H=k-2`: all excursions minimal;
3. `b=k-2`, `e=k-2`, `H=k-1`: exactly one plateau excursion `01,00,10` or `01,11,10`;
4. `b=k-2`, `e=H=k-1`: all excursions minimal, with at most one zero-length synchronized return slot.

Thus the saturated-area grammar survives one full odd step beyond the eliminated endpoint.

Classification: **new analytic localization theorem**.

---

## 9. Fixed-block-count interval exclusions

The transition-deficit inequality can be propagated in `k` without holding `k` at the endpoint.

Keep the exact RL88/RL89 lower function `Q_min(k)` and fix the block count.

The bundled exact rational verifier proves:

### Theorem 9.1

A survivor with exactly

`b=2,921,384,817`

blocks is impossible for every integer

`2,921,384,819 <= k <= 3,527,154,083`.

### Theorem 9.2

A survivor with exactly

`b=2,921,384,818`

blocks is impossible for every integer

`2,921,384,819 <= k <= 3,116,403,917`.

These are **not** elimination intervals in `k`: larger block counts may still survive. They are structural exclusions of two entire block-count strata over large parameter intervals.

Classification: **new analytic inequality + exact finite arithmetic thresholds**.

---

## 10. Why the original endpoint pigeonhole does not extend directly

RL88's padded `k-1`-slot deficit at `k0` is only about `22.15` per slot, which creates hundreds of millions of tiny-cofactor blocks.

The capacity `C(k-1)` grows by about `4.2e10` when `k` is incremented, whereas the reset-budget lower bound `Q_min(k)` changes by only about `74` per increment. Consequently the padded average deficit jumps by about `14.43` for each unit increase in `k` near `k0`.

At the next odd `k1`, the fully padded `k-1` capacity has average deficit about `51.01`, so there is no forced deficit-`<=28` population at the top block-count stratum.

Thus a global tiny-cofactor pigeonhole is intrinsically endpoint-local.

The productive repair is the case-sensitive actual-block deficit `D_b=Cb-Q`, which still eliminates the low-`b` strata and recovers saturated grammar at `k1`.

Classification: **new route diagnosis**.

---

## 11. Red-team audit

### RL81 common mode

Passed. The endpoint contradiction never promotes repeated differences to repeated physical states. It applies the 2-adic reset obstruction independently to each near-cap transition and charges the forced short successors to aggregate capacity deficit.

### RL79 generalized increment

Passed. The critical recurrences contain the ordinary-map constants `-1`, `-3`, and `-5`. The exact discrete-log certificate is tied to `3^a m-1` and is not homogeneous under a generalized odd increment.

### RL20 physical packing

Passed. No `O(M)` representative count is used. The physical first-Farey cap enters only through the already-owned per-block length ceiling `C` and the cofactor bound inherited from RL88.

### Primitivity

Passed. No repeated difference, cofactor, or quotient is interpreted as a repeated paired physical state.

### First-Farey scope

Preserved. The new lower endpoint and all interval/block-count results are branch-specific.

### RL88 arbitrary-reset family

Passed. RL88's local family regenerates arbitrarily high valuation by choosing a correspondingly huge odd pre-reset difference. RL89 only obstructs high reset depth when the **odd exit cofactor is tiny**, as forced by near-capacity physical packing.

---

## 12. Proof-state ledger additions

### New proved analytic mathematics

1. Exact excess-area decomposition `H-e`.
2. `H=e` complete-excursion grammar: every excursion is `01,10`.
3. `H=e+1` grammar: exactly one `01,00,10` or `01,11,10` plateau excursion, all others minimal.
4. Exact minimal cofactor recurrence `3^(s+1)m-1=2^(n_next+2)m_next`.
5. Exact plateau recurrences (3.3) and (3.4).
6. Multiplicative-order uniqueness of the physical exponent for fixed cofactor at high 2-adic depth.
7. Transition-deficit necessary inequality (6.4).
8. Elimination of the exact RL88 lower odd endpoint `k=2,921,384,819`.
9. Updated exact first-Farey odd lower endpoint `k>=2,921,384,821`.
10. At `k=2,921,384,821`, every survivor has `b>=k-2`.
11. Exact saturated grammar classification for every remaining `k1` block-count case.
12. Fixed block-count stratum exclusions through `3,527,154,083` and `3,116,403,917`.

### New exact finite certificate

For every signed odd `0<|m|<2^29` and every `1<=a<=42,150,931,629`, the exact modulo-`2^64` discrete-log scan finds only two candidates; both have valuation exactly 65. Therefore deficit `<=28` under a minimal reset forces next block length `<=63`.

### New route barriers / limitations

1. The padded tiny-cofactor population collapses immediately above the endpoint because capacity grows with slope `C` while `Q_min(k)` is almost flat.
2. The next surviving `k1` strata have average actual deficits about `36.58` (`b=k-2`) and `51.01` (`b=k-1`). The current `|m|<2^29` finite certificate does not reach those regimes.
3. Repeated cofactor/difference data remains insufficient for primitivity without a valid common-mode selector; RL89's endpoint theorem succeeds precisely because it avoids that step.

No inherited theorem is demoted.

---

## 13. RL90 route selection

RL90 should continue the **same** 2-adic transition attack rather than restart generic packing.

At `k1=2,921,384,821`, the low block-count escape has been removed. Only `b=k-2` or `b=k-1` remains, with minimal excursions except at most one plateau/zero-return exception.

For `b=k-2`,

`D_b=106,858,350,489`,

so at least

`33,321,293`

blocks have deficit `<=36`.

A cofactor-covering theorem strong enough to force almost all such blocks to have short successors would eliminate this stratum immediately: the total deficit can pay for only about two `O(1)`-length successors.

For `b=k-1`, the average deficit is about `51.01`; this is the second covering threshold.

Primary RL90 tasks:

1. extend the exact 2-adic long-reset exclusion from `|m|<2^29` toward the deficit-36 range `|m|<2^37` using a **covering/sieve**, not a brute scan over `2^37` cofactors;
2. normalize powers of `3` in the cofactor, since the first larger exact scan candidates occur in one `3`-orbit;
3. bound the number/multiplicity of sparse long-reset cofactor exceptions rather than requiring zero exceptions;
4. eliminate the `b=k-2` stratum at `k1`, then attack `b=k-1` at the deficit-51 threshold;
5. only if the sparse-exception route requires repeated-state information, introduce a common-mode selector and re-run the RL81/RL20/primitivity red teams.

Do not revert to independent midpoint-congruence accumulation.

---

## 14. Sustained-attack operating rule adopted from RL89 onward

A proved milestone is now a **checkpoint, not a session stop condition**.

After each new theorem/certificate, the active session should automatically continue through the following ladder while the route remains productive:

1. propagate the result through every surviving local case;
2. sharpen constants and replace padded bounds with actual-case bounds where possible;
3. push to the next admissible parameter value or a nontrivial interval;
4. splice the result into inherited global constraints;
5. red-team against the frozen barrier ledger;
6. test the strongest adjacent continuation before declaring the route exhausted.

Close-out should occur only when one of the following is true:

- context/compute pressure is high enough that further work would materially reduce reliability;
- the current route has reached a rigorous barrier and the most natural adjacent continuations have also been tested;
- a verifier failure/apparent contradiction triggers stop-and-repair;
- the target is actually closed and its immediate downstream consequences have been propagated.

This rule is subordinate to the verification-economy rule: sustained attack means **more new mathematics**, not recursively rerunning old expensive certificates.
