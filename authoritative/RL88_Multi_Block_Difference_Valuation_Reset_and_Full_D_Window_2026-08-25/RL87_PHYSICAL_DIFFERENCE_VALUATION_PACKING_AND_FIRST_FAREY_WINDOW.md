# RL87 — physical difference valuation packing and the first-Farey finite window

Date: 2026-08-25

## 0. Executive outcome

RL87 executed the authoritative aperiodic quotient-complexity / physical-packing target from a checksum-clean RL87 handover.

**No Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.**

The primary RL87 target succeeds on the exact RL83/RL84 first-Farey/full-phase intersection, but by a simpler and stronger physical consumer than the requested 930,959-state finite-fiber lift.

The key observation is that the two RL48/RL81 physical coordinates already carry a dyadic resource that the quotient `J=3A-B+1` hides.

For a synchronized physical column, put

`delta=B-A`.

Then exactly

- `00: delta -> delta/2`;
- `11: delta -> 3delta/2`.

Hence every synchronized column removes exactly one factor of `2` from the paired-state difference.  If a genuine synchronized block has length `n`, then

`boxed: 2^n | (B_0-A_0).`

Since the paired states are distinct states of the same primitive cycle,

`boxed: 2^n <= |B_0-A_0| <= M-R < M.}`

At the exact first Farey pair, RL85 proved

`M < 400,000,000,000 (3/2)^q`,

`q=72,057,431,991`.

Using the inherited exact certificate

`3^1,000,000 < 2^1,584,963`

and `400,000,000,000<2^39`, RL87 gets the context-free physical block cap

`boxed: n <= 42,150,931,628.}`

This immediately consumes the RL73 low-`k` giant macro: RL73 proved that every hypothetical Gate-A violation with odd `27<=k<=165` contains one maximal post-first-mismatch height-one synchronized block with at least

`40,249,491,324,522,944`

aligned `00` columns.  Such a block has length at least that count, which is more than 954,889 times the new physical cap.

Therefore:

> **The RL73 giant-macro / exact first-Farey/full-phase intersection is impossible for the entire old low-`k` laboratory `27<=k<=165`.**

This does **not** close that Gate-A band globally, because the RL85 maximum cap belongs to the exact first-Farey branch, not to every possible maximum branch.

RL87 then extends the splice beyond the historical `k<=165` numerical laboratory.  Reusing RL73's global skew/count identities, any Gate-A violation on the exact first-Farey branch must satisfy

`boxed: k >= 156,601,916,}`

and, since inherited Gate A leaves only odd `k`,

`boxed: k >= 156,601,917.}`

At the other end, RL81's exact terminal physical state

`B_j=2^(k-2)N`

combined with the inherited physical state floor `N>=2^71` and the same first-Farey maximum cap gives

`boxed: k <= 42,150,931,559.}`

Thus any surviving Gate-A violation in the exact first-Farey/full-phase intersection is forced into the finite odd window

`boxed: 156,601,917 <= k <= 42,150,931,559.}`

The original 930,959 spaced-distinct quotient-state theorem remains correct, but it is no longer load-bearing on the eliminated low-`k` first-Farey branch.  The stronger physical consumer is the 2-adic valuation budget of the genuine paired-state difference.

The remaining first-Farey obstruction is **multi-block valuation recycling**: for larger `k`, RL73 can distribute the forced aligned-zero mass over up to `e<=H<k` separate height-one synchronized blocks, each individually short enough to fit below the physical maximum.  RL88 should attack the exact `01/10` reset of the difference/common mode and ask whether those high dyadic valuations can be recycled across many genuine full-`D` blocks.

---

## 1. Incoming authority and verification economy

The supplied RL87 handover was checked before new mathematics:

- outer SHA-256 sidecar: PASS;
- fresh internal `SHA256SUMS.txt`: PASS;
- `bash verification/run_fast_rl86_verifiers.sh`: PASS.

The inherited RL86 roof-feeder verifier reproduced the first Farey pair, the first-Farey physical constants, and the retained RL85 fallback numbers.

Under the verification-economy rule, the frozen RL86/RL85 theorem ledger was accepted.  No historical expensive finite suite was recursively replayed.

Selective GitHub consultation was read-only and limited to the exact interfaces needed here:

- RL73 commit `454c828d3f9d9961a868737542de4422e07d12e6` — giant height-one synchronized block and the global skew/count identities;
- RL81 commit `86be41e05a3d5c8966a843539df8a722ff39775c` — exact lift `J=3A-B+1` and terminal physical state `B_j=2^(k-2)N`;
- RL79 commit `347a8408646dd39156c5b805bb45f62056125617` — generalized-increment/homogeneity red team;
- RL20 source — physical-state packing/product interface and the rule that physical ownership cannot be inferred from quotient/address information alone.

Global frozen status entering RL87:

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

---

## 2. Exact physical lift and the missing coordinate

At height one, RL81 gives

`boxed: J=3A-B+1,}`

where `A,B` are genuine shortcut-Collatz states on the paired RL48 physical trajectories.

Solving for `B`,

`B=3A+1-J`.

Define the physical separation

`delta=B-A`.

Then

`boxed: delta=2A+1-J.}`

For odd synchronized `J`, put

`alpha=(J-1)/2`.

Then

`boxed: delta=2(A-alpha).}`

This is the coordinate that the quotient finite-fiber formulation was missing.  `J` removes a physical common mode, but it does not remove the paired-state difference.  Synchronized dynamics price that difference 2-adically.

Classification: **new elementary reconstruction from the inherited RL81 lift**.

---

## 3. Synchronized difference law

Let a genuine height-one synchronized block have physical states

`(A_i,B_i)`, `0<=i<=n`,

and synchronized column symbols `epsilon_i in {0,1}` for `0<=i<n`, with `0=00` and `1=11`.

Set

`delta_i=B_i-A_i`.

If the column is `00`,

`A_(i+1)=A_i/2`,

`B_(i+1)=B_i/2`,

so

`delta_(i+1)=delta_i/2`.

If the column is `11`,

`A_(i+1)=(3A_i+1)/2`,

`B_(i+1)=(3B_i+1)/2`,

so the ordinary `+1` cancels and

`delta_(i+1)=3delta_i/2`.

Therefore, if the block contains `s` `11` columns,

`boxed: delta_n = 3^s delta_0 / 2^n.}`

Since `delta_n` is an integer and `gcd(3^s,2^n)=1`,

### Theorem 3.1 — universal synchronized divisibility

For every genuine synchronized block of length `n`,

`boxed: 2^n | delta_0.}`

Classification: **new analytic physical theorem**.

### Corollary 3.2 — arbitrary-block entry normal form

At height one write `alpha=(J_0-1)/2`.  Since

`delta_0=2(A_0-alpha)`,

there is an integer `m` such that

`boxed: A_0=alpha+2^(n-1)m,}`

`boxed: B_0=alpha+3*2^(n-1)m,}`

and

`boxed: B_0-A_0=2^n m.}`

For the genuine paired full-phase trajectories, `m!=0` because the two physical coordinates are distinct phase states of the same primitive cycle.

If the maximal synchronized block exits through the usual height-one mismatch, the exit difference is odd, so in that case `m` is odd and

`boxed: n=v_2(B_0-A_0).}`

This is the non-closed analogue of the RL76 closed-return normal form.  RL76 gained one additional factor of two from the return condition; RL87 needs no return.

---

## 4. Why the paired difference is nonzero

The full-phase physical pair originates from the distinct midpoint states `N+4` and `N`.

Both coordinates are genuine states of the same hypothetical primitive cycle in the RL48/RL64 ownership setting.  The shortcut map restricted to a finite cycle is a cyclic permutation and hence injective.

Therefore two distinct paired phase states cannot coalesce under equal forward time.  At every paired physical position,

`A_i != B_i`, so `delta_i!=0`.

Consequently Theorem 3.1 gives the owned physical inequality

`boxed: 2^n <= |B_0-A_0| <= M-R < M.}`

Classification: **analytic ownership consequence**.

This is exactly where unrestricted local quotient countermodels fail: they can pay for arbitrary synchronized depth by moving the physical pair arbitrarily far apart, while a genuine first-Farey cycle cannot exceed its owned maximum.

---

## 5. First-Farey physical synchronized-block cap

RL85 proved at the exact first Farey pair

`p=114,208,327,604`,

`q=72,057,431,991`,

that

`boxed: M < 400,000,000,000 (3/2)^q.}`

RL86 retained the exact arithmetic certificate

`3^1,000,000 < 2^1,584,963`.

Thus

`(3/2)^1,000,000 < 2^584,963`,

so

`log_2(3/2) < 584,963/1,000,000`.

Also

`400,000,000,000 < 2^39`.

Hence

`M < 2^[39 + q*(584,963/1,000,000)].`

The rational exponent is exactly

`42,150,931,628.751333`.

Combine with Section 4:

`2^n < 2^42,150,931,628.751333`.

### Theorem 5.1 — first-Farey synchronized-block ceiling

Every genuine synchronized physical block in the exact first-Farey/full-phase intersection satisfies

`boxed: n <= C=42,150,931,628.}`

Classification: **new analytic theorem + inherited exact finite logarithm certificate**.

This is stronger than RL85's closed-return span bound

`43,234,459,194`

because no quotient return is required and the sharper rational logarithm certificate is used.

---

## 6. Direct elimination of the RL73 low-k giant macro on the first-Farey branch

RL73 proved that every hypothetical low-`k` Gate-A violation with

`27<=k<=165`, `k` odd, `25<=H<k`,

contains one post-first-mismatch maximal height-one synchronized block with at least

`boxed: Z=40,249,491,324,522,944}`

aligned `00` columns.

Those `00` columns need not be consecutive because `11` columns may interleave, but every one of them lies inside the same synchronized block.  Therefore the block length `n` obeys

`n>=Z`.

The first-Farey physical theorem gives instead

`n<=42,150,931,628`.

Since

`40,249,491,324,522,944 > 42,150,931,628`,

there is a contradiction.

### Theorem 6.1 — low-k first-Farey giant-macro exclusion

No genuine full-phase Gate-A violation with odd

`27<=k<=165`

can simultaneously lie in the exact RL83/RL84 first-Farey maximum branch.

Classification: **new analytic exclusion theorem**.

### Scope warning

This does **not** close odd `27<=k<=165` globally.  The physical maximum cap used in Theorem 5.1 belongs to the exact first-Farey branch.  Other maximum/first-surplus branches are not silently assigned the same cap.

### Strategic correction

RL85's 930,959 spaced-distinct quotient theorem remains valid, but on this exact low-`k` intersection it is now superseded by the stronger direct physical difference consumer.  No RL85 theorem is demoted; only the route priority changes.

---

## 7. Extension of the RL73 count algebra beyond k=165

RL73's published numerical giant-block theorem stopped at the deliberate laboratory `k<=165`, but its preceding identities are global under the same full-phase one-excursion hypotheses.

Retain the RL73 exact skew floor

`Delta>=Delta0`,

`Delta0=13,201,833,154,443,526,323`.

For a Gate-A violation, inherited structure gives

`H<k`, hence `H<=k-1`,

`e<=H<=k-1`,

and the canonical prefix skew satisfies `P<=3`.

RL73 equation (6.1) gives

`c00+ >= ceil[(Delta-2k+7-P-e)/2]`.

Therefore

`c00+ >= ceil[(Delta0-3k+5)/2]`.

At most `H` of these post-first-mismatch `00` columns can lie above height one, so the number `Z1(k)` of post-first-mismatch height-one aligned `00` columns obeys

`boxed: Z1(k) >= ceil[(Delta0-5k+7)/2].}`

The height-one synchronized motion is partitioned into at most `e<=k-1` maximal synchronized blocks.

If every such block has length at most `C`, then it contains at most `C` aligned `00` columns, so

`Z1(k) <= C(k-1)`.

A necessary condition for a first-Farey Gate-A violation is therefore

`ceil[(Delta0-5k+7)/2] <= C(k-1)`.

It follows that

`Delta0+2C+7 <= (2C+5)k`.

### Theorem 7.1 — first-Farey lower terminal-k barrier

With

`C=42,150,931,628`,

any Gate-A violation in the exact first-Farey/full-phase intersection must satisfy

`boxed: k >= 156,601,916.}`

Since inherited Gate A already eliminates even `k`, any survivor must satisfy

`boxed: k >= 156,601,917, k odd.}`

The fast verifier checks that the general block lower bound specializes exactly at `k=165` to RL73's frozen number

`40,249,491,324,522,944`.

Classification: **new analytic extension of inherited RL73 identities + exact integer arithmetic**.

---

## 8. Independent first-Farey upper terminal-k barrier

RL81 proved the exact terminal physical geometry.  Immediately before the omitted terminal `(1,0)` pair,

`boxed: B_j=2^(k-2)N.}`

The inherited full-phase state floor is

`N>=2^71`.

Because `B_j` is a genuine cycle state,

`B_j<=M`.

Hence

`2^(k+69) <= M`.

Use again

`M < 2^42,150,931,628.751333`.

Therefore

`k+69 < 42,150,931,628.751333`.

### Theorem 8.1 — first-Farey upper terminal-k barrier

Any genuine first-Farey/full-phase terminal object satisfies

`boxed: k <= 42,150,931,559.}`

Classification: **new analytic splice of inherited RL81 terminal ownership + RL85/RL86 physical cap**.

---

## 9. Combined exact first-Farey Gate-A window

Combine Theorems 7.1 and 8.1 with the inherited odd-`k` theorem.

### Corollary 9.1 — surviving finite terminal window

Any remaining Gate-A violation on the exact first-Farey/full-phase branch must have odd

`boxed: 156,601,917 <= k <= 42,150,931,559.}`

This is a finite window, but it still contains roughly twenty-one billion odd candidates.  RL87 does not propose direct enumeration.

The correct next problem is structural: consume the **sum/recycling of block-entry dyadic valuations** across the `01/10` active resets.

---

## 10. Finite-fiber quotient lifting: proved, but quantitatively weak

RL87 also completed the target's requested direct finite-fiber audit.

For fixed `J`, solve

`B=3A+1-J`.

With

`R<=A,B<=M`,

one has the exact feasible interval

`boxed: max(R, ceil[(J+R-1)/3]) <= A <= min(M, floor[(J+M-1)/3]).}`

Hence the number of physical lifts of one fixed `J` is at most

`boxed: floor[(M-R)/3]+1.}`

This is a genuine finite-fiber theorem, but the multiplicity is `O(M)` and therefore useless at first-Farey scale.

Across the whole physical box,

`3R-M+1 <= J <= 3M-R+1`.

Thus the complete possible `J` range contains at most

`4(M-R)+1`

integer values.  Consequently `D_J` distinct quotient states force only

`M-R >= ceil[(D_J-1)/4]`.

For the inherited

`D_J=930,959`,

this gives merely

`boxed: M-R >= 232,740.}`

The physical cycle already lives on vastly larger scales.  Quotient-count packing without synchronized depth remains nondecisive.

Classification: **new analytic finite-fiber theorem + quantitative barrier**.

---

## 11. Why the direct difference consumer evades the RL81 common-mode barrier

RL81 proved that fixing `J` leaves a free physical common mode.  RL87 does not infer `A` or `B` from `J`.

Instead, it uses the second physical coordinate

`delta=B-A`.

The quotient relation is

`J=2A-delta+1`.

Varying the common mode can still make `delta` arbitrarily large in unrestricted local lift families, which is exactly why RL74/RL76 could construct arbitrarily long synchronized blocks.

The first-Farey theorem removes that escape only for a genuine cycle: both coordinates must lie in `[R,M]`, and the owned maximum is absolutely capped.

So the logical chain is:

`full physical ownership -> |delta|<M -> dyadic depth cap`.

It is not

`quotient state -> physical state`.

This passes the RL81 red team.

---

## 12. RL79 generalized-increment red team

The local difference law itself is homogeneous and survives generalized odd increment `s`:

`T_s(B)-T_s(A)` still equals `delta/2` on `00` and `3delta/2` on `11`, because the additive `s` cancels.

Therefore the local valuation theorem alone is **not** an `s=1` ownership discriminator.

The full RL87 contradiction, however, also consumes the RL85 first-Farey physical maximum theorem.  That theorem is an absolute ordinary-Collatz (`s=1`) cylinder/ownership statement.  Under the RL79 scaling

`(states,s)->(c*states,c*s)`,

the physical maximum scales by `c`; there is no inherited scale-covariant theorem giving the same fixed first-Farey cap to every generalized fake.

Thus the successful composite argument is not a purely homogeneous normalized identity:

`homogeneous difference transport + non-homogeneous s=1 physical cap`.

Classification: **RL79 red team passed for the composite theorem**.

---

## 13. Weighted-mass, phase-slot, and full-D audit after the direct splice

### 13.1 Weighted physical mass

The RL19/RL20 product identity remains exact, but the 930,959 quotient samples do not automatically identify 930,959 odd physical states at a controlled low scale.  The first-Farey maximum is still astronomically large, so a crude lower weight such as `D/M` is negligible.

No new weighted-mass contradiction is claimed.

### 13.2 Primitive phase slots

Distinct `J` values force distinct paired physical states, because one paired state determines `J`.  This gives only a lower bound on the number of phase positions.  No inherited first-Farey theorem gives a useful upper period budget.

No phase-slot contradiction is claimed.

### 13.3 Full-D content

RL87 did not find a second exact content condition that makes the surviving high-`k` multi-block valuations incompatible.  The direct physical theorem already solves the low-`k` first-Farey consumer more efficiently.

The full-`D` layer is therefore reserved for the remaining reset/recycling problem, where an absolute lattice condition may be necessary to couple several block entries at once.

---

## 14. New route barrier: single-block scale is solved; multi-block recycling remains

Before RL85, RL74/RL76 showed that synchronized depth could be hidden in arbitrarily large physical scale.

RL87 now resolves that objection at the exact first-Farey branch for **each individual block**:

`n_block <= 42,150,931,628`.

The residual obstruction is different.

For large `k`, the RL73 global count can be split across up to

`e<=H<k`

separate height-one synchronized blocks.  Every block can individually obey the physical cap while the total aligned-zero count remains enormous.

At each block entry,

`n_block <= v_2(B-A)`,

and for a standard maximal mismatch exit in fact

`n_block=v_2(B-A)`.

The active `01/10` excursions can reset the difference and potentially regenerate high 2-adic valuation.  No theorem currently proves that this reset resource is non-recyclable.

This is the exact RL88 obstruction.

---

## 15. Proof-state ledger additions

### New proved analytic mathematics

1. Synchronized physical difference law:
   `00: delta->delta/2`, `11: delta->3delta/2`.
2. Every genuine synchronized block of length `n` satisfies
   `2^n | (B_0-A_0)`.
3. Arbitrary-block entry normal form
   `A_0=alpha+2^(n-1)m`,
   `B_0=alpha+3*2^(n-1)m`.
4. Under primitive paired ownership, `m!=0` and
   `2^n<=|B_0-A_0|<=M-R`.
5. First-Farey physical synchronized-block ceiling
   `n<=42,150,931,628`.
6. Exact first-Farey exclusion of the RL73 low-`k` giant macro for odd `27<=k<=165`.
7. Generalized RL73 height-one `00` lower bound
   `Z1(k)>=ceil[(Delta0-5k+7)/2]` for a Gate-A violation under the inherited full-phase hypotheses.
8. First-Farey necessary Gate-A lower terminal bound
   `k>=156,601,916`, hence odd `k>=156,601,917`.
9. First-Farey terminal physical upper bound
   `k<=42,150,931,559`.
10. Combined surviving first-Farey Gate-A window
    `156,601,917<=k<=42,150,931,559`, `k` odd.
11. Exact fixed-`J` physical feasible interval and `O(M)` multiplicity bound.
12. Quotient-only range packing gives only
    `M-R>=232,740` from `D_J=930,959`.

### Exact finite arithmetic certificates/checks

The RL87 fast verifier checks:

- `3^1,000,000 < 2^1,584,963`;
- `400,000,000,000<2^39`;
- exact rational exponent numerator
  `42,150,931,628,751,333 / 1,000,000`;
- block cap `42,150,931,628`;
- RL73 giant count and its ratio to the cap;
- recovery of RL73's exact `k=165` giant block count from the generalized formula;
- lower terminal threshold `156,601,916`;
- odd lower threshold `156,601,917`;
- upper terminal threshold `42,150,931,559`;
- quotient-only span floor `232,740`;
- exhaustive small-box checks of the finite-fiber formula;
- exact difference-law arithmetic checks on audited sample parameters.

### Externally inherited inputs

Unchanged:

- accepted nontrivial-cycle physical state floor `>=2^71` remains external computational input where inherited RL73/RL81 use it;
- RL83/RL84/RL85 logarithm/Farey/cylinder certificates retain their inherited evidence labels.

### New barriers / dead subroutes

1. quotient distinctness alone -> `O(M)` physical-box packing: quantitatively dead;
2. fixed-`J` finite fibers without synchronized-depth information: quantitatively dead;
3. primitive paired-state count without an upper period budget: dead at current scale;
4. weighted mass from the 930,959 quotient samples without a low-scale ownership theorem: not decisive;
5. single-block free-scale objection on the exact first-Farey branch: **closed**;
6. surviving obstacle: repeated active resets may recycle high block-entry 2-adic valuation across many blocks.

### Corrections / demotions

No inherited theorem is demoted.

Strategic correction only: on the exact first-Farey low-`k` intersection, the direct physical difference budget is stronger than the RL85 periodic/aperiodic quotient-state consumer and should be used first.

---

## 16. RL88 route selection

RL88 should not restart generic quotient packing, dyadic funnels, residue ladders, or first-Farey finite-fiber counting.

The new authoritative obstruction is:

> **Can the `01/10` active excursions repeatedly regenerate large `v_2(B-A)` at the entries of many distinct maximal height-one synchronized blocks, while all blocks belong to one genuine primitive full-`D` cycle inside the first-Farey physical maximum?**

The target should derive exact reset laws for the paired difference/common mode and seek one of:

1. a bound on the sum of block-entry valuations, not just each valuation;
2. a bounded multiplicity theorem for high-valuation reset states;
3. a full-`D` congruence showing that several high valuations impose incompatible conditions on the same physical midpoint `N`;
4. a primitive-cycle non-recycling theorem for repeated difference/common-mode data;
5. a proof that the reset map has enough common-mode freedom to realize the remaining finite window, thereby freezing this branch as a sharp barrier.

Mandatory red teams remain RL81 common mode and RL79 generalized-increment homogeneity.
