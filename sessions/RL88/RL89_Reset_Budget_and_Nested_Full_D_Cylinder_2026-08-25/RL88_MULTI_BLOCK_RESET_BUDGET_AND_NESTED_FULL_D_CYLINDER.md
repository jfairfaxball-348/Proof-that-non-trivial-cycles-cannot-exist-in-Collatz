# RL88 — multi-block reset budget and nested full-D cylinder

Date: 2026-08-25

## 0. Executive outcome

RL88 executed the authoritative multi-block difference-valuation reset / full-`D` non-recycling target from a checksum-clean RL88 handover.

**No Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.**

RL88 obtains a genuine new aggregate consumer.  A single mismatch can indeed regenerate arbitrarily large dyadic valuation locally, so a per-reset prohibition is false.  However, after compressing each complete height-one excursion, the physical common mode cancels and the reset is an affine map of the paired difference.  The amount by which all excursions can collectively replenish the logarithmic difference potential is charged to the inherited excursion/area budget.

Combining that reset budget with

- the RL73 exponent-skew floor
  `Delta>=13,201,833,154,443,526,323`,
- the RL73 post-prefix count identity and `H<k`,
- the RL87 first-Farey single-block cap
  `n<=42,150,931,628`,
- and the exact first-Farey logarithmic maximum bound,

raises the necessary first-Farey Gate-A terminal lower bound from

`k>=156,601,917` (odd)

to

`boxed: k>=2,921,384,819, k odd.}`

The inherited upper bound remains

`k<=42,150,931,559`.

Thus the surviving exact first-Farey/full-phase Gate-A window is now

`boxed: 2,921,384,819 <= k <= 42,150,931,559, k odd.}`

This is a factor of about `18.65` improvement in the lower endpoint.

At the new lower endpoint the aggregate block capacity is nearly saturated.  Any survivor there must have total post-first-mismatch height-one synchronized length at least

`123,139,091,657,887,804,990`,

must use at least

`2,921,384,817 = k-2`

nonempty height-one synchronized blocks, and, even when padded to the maximal `k-1` block slots, has average block length at least

`42,150,931,605`,

only `23` below the absolute first-Farey cap.

A distributional corollary forces at least

`225,242,372`

blocks with length at least

`42,150,931,605 = C-23`.

For such a maximal block, writing the RL87 entry difference as

`delta=2^n m`, `m` odd,

the physical maximum gives `|m|<2^24`.  Across deficit values `0<=C-n<=23` there are at most `2^25-2=33,554,430` signed `(deficit,m)` types.  Therefore, at the new lower endpoint, some exact `(n,m)` / entry-difference type repeats at least **7 times**.  Primitivity does not by itself forbid repeated differences, so this is a next-route rigidity statement, not closure.

RL88 also derives the requested full-`D` midpoint congruence.  A height-one block entry of depth `n` after `i` internal columns forces one residue class for `N` modulo `2^(i+n+2)`.  But that congruence is already implied by the two ordinary parity cylinders through the end of the block, which fix `N` one dyadic level more deeply.  Successive block congruences are therefore nested prefix information, not independent CRT constraints.  Since `D` is odd, multiplying by `D` preserves this fact rather than creating a new obstruction.

The route decision is:

> **Keep the new aggregate reset budget.  Freeze “independent full-`D` congruence accumulation” as a dead subroute.  RL89 should exploit the near-capacity regime forced by the new lower endpoint: billions of almost-maximal blocks, tiny odd cofactors, and near-minimal excursion area.**

---

## 1. Incoming authority and verification economy

The supplied RL88 handover was verified before new mathematics:

- outer SHA-256 sidecar: PASS;
- freshly unpacked internal `SHA256SUMS.txt`: PASS;
- `bash verification/run_fast_rl87_verifiers.sh`: PASS.

The inherited first-Farey constants reproduced exactly:

- first Farey pair `(114208327604,72057431991)`;
- physical block cap `C=42,150,931,628`;
- old first-Farey odd lower bound `156,601,917`;
- first-Farey upper bound `42,150,931,559`.

Under the verification-economy rule the frozen RL87 ledger was accepted.  No historical expensive suite was recursively replayed.

Selective GitHub consultation was read-only and limited to exact interfaces needed by the live obstruction:

- RL73 count identity / area definition / exponent-skew floor;
- RL81 exact physical lift and common-mode barrier;
- RL50 exact height convention and complete height-one excursion interface;
- RL73's exact atanh logarithm-interval verifier method.

---

## 2. Exact one-column reset laws in `(d,T,J,g)`

Use the ordinary shortcut map

`F(z)=z/2` for even `z`,

`F(z)=(3z+1)/2` for odd `z`.

For the paired physical states let the current parity symbol be `(x,y) in {0,1}^2`, with `x` the parity of `A` and `y` the parity of `B`.

The inherited height convention is

`d_i=1+p_y(i)-p_x(i)`.

Put

`T=3^d A-B`.

Then

`d'=d+y-x`,

and direct substitution gives the exact universal law

`boxed: T'=[3^y T + x 3^(d+y-x)-y]/2.}`

Thus

- `00: d'=d, T'=T/2`;
- `01: d'=d+1, T'=(3T-1)/2`;
- `10: d'=d-1, T'=(T+3^(d-1))/2`;
- `11: d'=d, T'=(3T+3^d-1)/2`.

At height one, `J=T+1`, so synchronized motion gives the inherited exact conjugacy

- `00: J'=(J+1)/2`;
- `11: J'=(3J+1)/2`.

A height-one `01` departure gives

`d'=2`, `T'=(3J-4)/2`.

A `10` return from height two gives

`d'=1`, `J_new=(T+5)/2`.

For the prefix scalar

`g=2^i/3^(p_x)`,

one has exactly

- `x=0: g'=2g`;
- `x=1: g'=2g/3`.

Classification: **exact analytic reset law; direct reconstruction consistent with the inherited RL50/RL81 coordinates**.

---

## 3. Complete excursion difference reset: the common mode cancels

For a finite binary word `w=(w_0,...,w_(L-1))` define its odd count `r(w)` and affine constant `Q(w)` by

`F_w(z)=[3^r z+Q(w)]/2^L`.

The constants obey the exact recurrence

`Q_(j+1)=3^(w_j) Q_j + w_j 2^j`, `Q_0=0`.

Equivalently,

`Q(w)=sum_(j:w_j=1) 2^j 3^(# later 1s)`.

Hence

`boxed: 0<=Q(w)<2^L 3^r.}`

Now take a complete excursion from height one back to height one.  Let `x` and `y` be the two physical parity words over that excursion.  Since the height returns to one,

`r(x)=r(y)=r`.

If `delta=B-A` at excursion departure and `delta^+=B^+-A^+` at the next height-one return, then

`boxed: delta^+=[3^r delta + K]/2^L,}`

where

`K=Q(y)-Q(x)`

and

`boxed: |K|<2^L 3^r.}`

This is the exact reset compression requested by RL88.

### Structural meaning

A single `01` or `10` mismatch depends on the physical common mode.  But over a **complete** height-one-to-height-one excursion the two words have equal odd count, so their common linear mode has the same coefficient and cancels in the difference.

The reset is not homogeneous—the additive `K` is an ordinary `+1` word constant—but it is independent of the free physical common mode once the full excursion word is fixed.

Classification: **new analytic excursion reset theorem**.

---

## 4. Logarithmic reset-potential budget

Let a complete excursion be followed by a maximal height-one synchronized block.

Write

- `X_(r-1)` for the nonzero difference immediately before that excursion;
- `E_r` for the next height-one block-entry difference;
- `X_r` for the difference after the synchronized block;
- `n_r` for the block length;
- `s_r` for the number of `11` columns inside the block;
- `rho_r` for the common odd count in the preceding complete excursion.

The excursion theorem gives

`|E_r| < 3^(rho_r)(|X_(r-1)|+1)`.

Because the paired primitive states never coalesce, `|X_(r-1)|>=1`, hence

`boxed: log_2|E_r| < log_2|X_(r-1)| + rho_r beta +1,}`

where

`beta=log_2 3`.

Inside the synchronized block RL87 gives exactly

`X_r=3^(s_r) E_r / 2^(n_r)`.

Therefore

`boxed: n_r-beta s_r = log_2|E_r|-log_2|X_r|.}`

Summing over all post-first-mismatch height-one blocks telescopes the physical difference scale:

`boxed: sum n_r - beta sum s_r < log_2 M + beta R + b,}`

where

- `b` is the number of such blocks;
- `R=sum rho_r` is the total x-odd count in their preceding complete excursions.

Put

`z = # height-one 00 columns after the first mismatch`,

`s = # height-one 11 columns after the first mismatch`,

`Q=z+s=sum n_r`.

Then

`boxed: z-(beta-1)s < log_2 M + beta R + b.}`     (4.1)

This is the missing aggregate reset budget.  It does not bound `sum n_r` by `O(log M+k)` by itself—the synchronized `11` mass is a genuine replenishing resource—but it couples that resource to the RL73 skew identity.

Classification: **new analytic multi-block physical theorem**.

---

## 5. Area charges the complete reset complexity

Let `u_00,u_11` count post-first-mismatch synchronized columns whose pre-height is above one.

RL73's area is

`H=sum(d_i-1)`.

Every `10` has pre-height at least two, and there are exactly `e` such internal columns.  Therefore

`boxed: e+u_00+u_11 <= H < k.}`     (5.1)

Every complete excursion's x-odd columns are among the above-height `10` and `11` columns.  Hence

`R <= e+u_11`.

Also

`b<=e`.

At the exact first-Farey branch RL87 gives

`log_2 M < Lambda`,

with exact rational

`Lambda=42,150,931,628.751333`.

Thus (4.1) implies the permissive upper budget

`boxed: z-(beta-1)s < Lambda + beta(e+u_11)+e.}`     (5.2)

This is where the reset theorem consumes the physical maximum and the RL73 area simultaneously.

---

## 6. Splice with the RL73 skew/count identity

RL73 gives after the canonical synchronized prefix

`Delta-2k+7 = P + 2c_00^+ - c_11^+ + e`,

with

`P in {-2,2,3}`

and

`Delta>=Delta0`,

`Delta0=13,201,833,154,443,526,323`.

Decompose

`c_00^+=z+u_00`,

`c_11^+=s+u_11`.

Using `P<=3`,

`boxed: 2z-s >= Delta0-2k+4-e-2u_00+u_11.}`     (6.1)

Now let `beta_+` be the exact rational upper endpoint for `log_2 3` generated by the inherited 260-term atanh interval method.  The bundled verifier proves the interval width is below `10^-150`.

Replacing `beta` by `beta_+` only weakens (5.2).  Put

`gamma_+=2beta_+-3>0`.

The key linear combination is exact:

`gamma_+(z+s)`

`= beta_+(2z-s) - 3[z-(beta_+-1)s]`.

Using (5.2) and (6.1),

`gamma_+ Q`

`> beta_+(Delta0-2k+4)`

`  -3Lambda`

`  -(4beta_++3)e`

`  -2beta_+(u_00+u_11).`                           (6.2)

But (5.1) gives

`e+u_00+u_11 <= k-1`.

Since `4beta_++3 > 2beta_+`, the most permissive possible allocation of this area budget is to put all available units into `e`.  Therefore every survivor must satisfy

`boxed: gamma_+ Q > beta_+(Delta0-2k+4)-3Lambda-(4beta_++3)(k-1).}`     (6.3)

This is the new global lower bound on total height-one synchronized length.

Classification: **new analytic splice + exact rational logarithm enclosure**.

---

## 7. New first-Farey terminal lower bound

RL87 proves each height-one synchronized block has

`n_r<=C=42,150,931,628`.

There are at most

`b<=e<=k-1`

such blocks.  Hence

`boxed: Q<=C(k-1).}`     (7.1)

Combining (6.3) and (7.1) gives a necessary linear inequality in `k`.

The bundled exact verifier solves it with rational arithmetic and proves:

- every integer `k<=2,921,384,817` is impossible on the exact first-Farey/full-phase Gate-A branch;
- the first raw integer where the permissive inequality can hold is
  `2,921,384,818`;
- inherited Gate A already eliminates even `k`.

### Theorem 7.1 — reset-budget lower terminal barrier

Any Gate-A violation on the exact first-Farey/full-phase branch must satisfy

`boxed: k>=2,921,384,819, k odd.}`

This replaces the RL87 lower endpoint `156,601,917`.

Classification: **new analytic theorem + exact finite arithmetic certificate**.

---

## 8. Updated finite first-Farey window

RL87's independent terminal ownership theorem remains unchanged:

`k<=42,150,931,559`.

Therefore:

### Corollary 8.1 — surviving reset-budget window

Any remaining Gate-A violation on the exact first-Farey/full-phase branch must have odd

`boxed: 2,921,384,819 <= k <= 42,150,931,559.}`

This is still far too large for direct enumeration.

No statement is promoted to Gate A globally: the first-Farey maximum cap remains branch-specific.

---

## 9. Near-capacity rigidity at the new lower endpoint

Set

`k0=2,921,384,819`.

The exact reset-budget verifier gives

`boxed: Q>=123,139,091,657,887,804,990.}`

The maximal `k0-1` block capacity is

`C(k0-1)=123,139,091,722,595,223,704`.

The total capacity deficit is therefore at most

`64,707,418,714`.

Consequences:

1. The number of nonempty blocks satisfies

   `boxed: b>=2,921,384,817=k0-2.}`

2. Since `b<=e<=H<=k0-1`, necessarily

   `e>=k0-2`, `H>=k0-2`.

   Thus at the lower endpoint the area/mismatch architecture is forced into the last two possible integer levels:

   `H in {k0-2,k0-1}`.

3. Padding to `k0-1` possible block slots, the average block length is at least

   `42,150,931,605`,

   only `23` below `C`.

4. If a padded slot has deficit

   `d=C-n>=24`,

   it consumes at least `24` units of the total capacity deficit.  Therefore at least

   `boxed: 225,242,372}`

   actual blocks satisfy

   `boxed: n>=C-23=42,150,931,605.}`

This is the strongest structural localization produced by RL88.

---

## 10. Tiny odd-cofactor multiplicity near the lower endpoint

For a maximal height-one block RL87 gives

`delta_entry=2^n m`,

with `m` odd and nonzero.

Write the block deficit

`d=C-n`.

The exact first-Farey logarithmic cap is

`M<2^(C+0.751333)`.

Hence, if `0<=d<=23`,

`|m| < 2^(d+0.751333) < 2^(d+1)`.

For fixed `d`, the number of possible signed odd `m` with that bound is at most `2^(d+1)`.  Summing over `0<=d<=23`, the total number of signed `(d,m)` types is at most

`sum_(d=0)^23 2^(d+1)=2^25-2=33,554,430`.

But Section 9 forces at least `225,242,372` blocks in this deficit range.

### Corollary 10.1 — repeated near-maximal entry difference type

At `k=k0`, some exact pair `(d,m)`—equivalently some exact `(n,delta_entry)` type—occurs at least

`boxed: 7}`

distinct height-one synchronized blocks.

Classification: **new exact pigeonhole corollary**.

### Primitivity red team

This does **not** imply a repeated paired physical state.  Repeated differences, even repeated `(n,m)`, can occur at distinct common modes.  Therefore Corollary 10.1 is a genuine rigidity input for RL89, not a cycle-return contradiction.

---

## 11. Exact full-D midpoint congruence at a high-valuation block

RL81's canonical internal entrance gives, in the physical coordinates,

`A_0=(9N+5)/8`,

`B_0=(27N+127)/8`.

Let `x,y` be the two internal parity prefixes of length `i`, with affine word constants `Q_x,Q_y` and prefix weights `p_x,p_y`.

Then

`2^(i+3) A_i = 3^(p_x)(9N+5)+8Q_x`,

`2^(i+3) B_i = 3^(p_y)(27N+127)+8Q_y`.

At height one the inherited convention

`d_i=1+p_y-p_x=1`

forces

`p_x=p_y=p`.

Subtracting gives

`boxed: 2^(i+2)(B_i-A_i)`

`= 3^p(9N+61)+4(Q_y-Q_x).}`                     (11.1)

Therefore a block-entry valuation

`2^n | (B_i-A_i)`

is equivalent to

`3^p(9N+61)+4(Q_y-Q_x) == 0 (mod 2^(i+n+2)).`

Since `9*3^p` is odd, this is exactly one residue class:

### Theorem 11.1 — midpoint residue forced by block depth

A height-one block of depth at least `n` after `i` internal columns forces

`boxed: N == c_(i,n) (mod 2^(i+n+2))}`

for an explicit word-determined residue `c_(i,n)`.

Because

`D=2^a-3^ell`

is odd, the same statement is equivalently one residue class for

`DN=Q(v)+4*3^ell`

modulo `2^(i+n+2)`.

Classification: **new exact full-`D` congruence theorem**.

---

## 12. Why the successive full-D congruences do not accumulate independently

For any binary word `w` of length `L`, the ordinary shortcut parity cylinder is one residue class modulo `2^L` for its starting state, because

`F_w(z)=[3^r z+Q(w)]/2^L`

and `3^r` is invertible modulo `2^L`.

At the canonical internal entrance, `A_0=(9N+5)/8` and `B_0=(27N+127)/8`.  Therefore fixing either physical parity prefix through internal time `L` fixes `N` modulo `2^(L+3)`; a genuine paired prefix is exactly the compatibility of the two such classes.

If a block begins at time `i` and has length `n`, then the two paired parity words through the end of that block are already known through time

`L=i+n`.

Their common physical cylinder therefore fixes `N` modulo

`2^(i+n+3)`.

The valuation congruence of Theorem 11.1 uses only modulus

`2^(i+n+2)`.

Hence it is one dyadic level **weaker** than information already encoded by the genuine pair word through the block.

Successive block congruences are chronological prefix extensions.  Their moduli increase, and the later full parity cylinder reduces automatically to every earlier one.  They are not independent CRT conditions whose exponents can be summed.

### Route barrier 12.1

> **High block-entry valuations do force exact congruences on the shared midpoint `N`, but those congruences are already contained in the ordinary full-phase parity cylinders.  Odd full-`D` multiplication preserves them but does not create an independent non-recycling budget.**

Therefore a successful full-`D` continuation must add a new restriction on the allowed word numerator/content, not merely restate the same prefix cylinder modulo larger powers of two.

Classification: **new analytic method barrier / dead subroute**.

---

## 13. Explicit local counterfamily: one reset can regenerate arbitrary valuation

The aggregate theorem must not be misread as a per-reset bound.

For any `t>=1`, choose odd

`m=1` if `t` is odd,

`m=5` if `t` is even,

and put

`delta_0=[1+2^(t+2)m]/3`.

Then `delta_0` is an odd integer with `delta_0==3 (mod4)` and

`3delta_0-1=2^(t+2)m`.

Choose

`A_0=2+h 2^(t+2)`,

`B_0=A_0+delta_0`,

for any integer `h>=0`.

The first two parity columns are exactly

`01,10`.

After those two ordinary shortcut steps,

`boxed: B_2-A_2=2^t m.}`

Therefore the next `t` columns are synchronized, and after exactly `t` such columns the difference is odd, so the synchronized block ends by mismatch.

Thus a **minimal two-column excursion can regenerate an arbitrarily prescribed block valuation `t`**.  Moreover the common shift parameter `h` is unbounded while the entire finite parity pattern is unchanged.

The bundled verifier checks this family for `1<=t<=200` and several common-mode shifts; the algebra above proves it for all `t`.

### Scope

This is a local ordinary-`s=1` physical family.  It is not claimed to complete a primitive full-`D` cycle or to obey the first-Farey maximum.

Its role is a red team:

- no theorem can forbid large reset valuation from the local mismatch grammar alone;
- the successful RL88 theorem works only because it couples **many** resets to the global area and first-Farey physical cap.

Classification: **new analytic counterfamily / route barrier**.

---

## 14. RL79, RL81, RL20, and primitivity red teams

### RL81 common mode

Individual mismatch formulas retain common-mode dependence, and Section 13 gives an explicit unbounded common-mode family.  RL88 does not infer physical states from quotient data.  The common mode cancels only after a complete height-one return excursion, where the two physical words have equal odd count.

**Passed.**

### RL79 generalized increment

The homogeneous synchronized difference law survives a generalized odd increment, but the complete excursion affine constant `K` records the ordinary additive word increments, and the numerical contradiction additionally consumes the absolute ordinary-`s=1` first-Farey physical maximum.

The final lower-`k` theorem is not a scale-free homogeneous statement.

**Passed for the composite theorem.**

### RL20 physical packing

No `O(M)` state-count or raw residue packing is used.  The only physical upper resource is the already-owned maximum scale, consumed logarithmically through the difference potential and the RL87 block cap.

**Passed.**

### Primitivity

Repeated differences/cofactors are not promoted to repeated physical states.  Corollary 10.1 is explicitly left as rigidity, not closure.

**Passed.**

### First-Farey scope

The maximum cap and all resulting new terminal bounds remain conditional on the exact first-Farey/full-phase branch.

**Passed.**

---

## 15. Proof-state ledger additions

### New proved analytic mathematics

1. Exact all-symbol `(d,T)` reset law
   `T'=[3^yT+x3^(d+y-x)-y]/2`.
2. Exact complete-excursion affine difference reset
   `delta^+=(3^r delta+K)/2^L`, with `|K|<2^L3^r`.
3. Multi-block logarithmic reset-potential budget
   `z-(beta-1)s < log_2 M + beta R + b`.
4. Area control of reset complexity via
   `R<=e+u_11`, `b<=e`, `e+u_00+u_11<=H<k`.
5. Combined reset/skew lower bound on total height-one block length.
6. New exact first-Farey necessary raw terminal bound
   `k>=2,921,384,818`.
7. New odd first-Farey Gate-A lower bound
   `k>=2,921,384,819`.
8. Updated surviving exact first-Farey odd window
   `2,921,384,819<=k<=42,150,931,559`.
9. New-lower-endpoint aggregate block-length floor
   `Q>=123,139,091,657,887,804,990`.
10. At that endpoint, at least `k-2` nonempty height-one synchronized blocks.
11. At least `225,242,372` blocks have length at least `C-23`.
12. Some exact near-maximal `(deficit,m)` type repeats at least 7 times.
13. Exact full-`D` midpoint congruence
    `N mod 2^(i+n+2)` from a depth-`n` block entry.
14. Exact cylinder-domination theorem: that congruence is already implied by the paired parity prefix through the block.
15. Explicit minimal-excursion family regenerating arbitrary valuation `t` with unbounded common mode.

### Exact finite arithmetic/certificate checks

The RL88 fast verifier checks:

- 30,420 exact `(d,T)` one-column arithmetic cases;
- 625 complete excursion words at small depth and the equal-weight / affine-constant laws;
- 711 canonical midpoint-congruence identity checks;
- 600 instances of the explicit arbitrary-reset family;
- an exact atanh enclosure of `log_2 3` with width `<10^-150`;
- raw threshold `2,921,384,818`;
- odd threshold `2,921,384,819`;
- endpoint aggregate block floor and capacity;
- minimum block count `k-2`;
- endpoint average block-slot floor;
- `225,242,372` near-cap blocks;
- `33,554,430` signed near-cap `(deficit,m)` types;
- repetition multiplicity at least 7.

### New barriers / dead subroutes

1. **Independent midpoint-congruence accumulation:** dead.  Successive high-valuation congruences are nested parity-cylinder information.
2. **Per-reset valuation prohibition:** false.  Minimal `01,10` excursions can regenerate arbitrary valuation locally.
3. **Repeated difference -> primitivity contradiction:** invalid without an additional common-mode/paired-state selector.

### Surviving live route

The aggregate reset budget is productive.  Its new lower endpoint forces a near-capacity regime in which billions of blocks must be almost as long as the absolute first-Farey ceiling and therefore have very small odd cofactors.

No inherited theorem is demoted.

---

## 16. RL89 route selection

RL89 should attack the **near-capacity block-rigidity regime** produced here, not restart generic reset congruences.

Primary objects:

- block deficit `d_r=C-n_r`;
- odd entry cofactor `m_r` from `delta_r=2^(n_r)m_r`;
- excursion area/mismatch data between repeated near-cap blocks;
- exact minimal-excursion reset
  `delta_next=(3 delta_exit-1)/4`
  when the area is saturated by `e=H`;
- the fact that at the new lower endpoint `b,e,H` are forced to lie within one unit of their absolute maxima.

Preferred next theorem forms:

1. show that near-capacity forces almost all excursions to be minimal `01,10` and derive a recurrence on the small odd cofactors;
2. combine the order of `3 mod 2^t` with `|m|<2^(d+1)` to bound multiplicity of near-cap reset types;
3. add an exact common-mode selector (`J`, `L`, full-`D` numerator, or primitive phase offset) so repeated `(n,m)` becomes repeated paired physical data;
4. if this fails, construct a genuine full-phase counterfamily showing repeated near-cap differences can occur at distinct common modes, and freeze the route cleanly.

Do not claim closure unless the common-mode/primitivity step is actually proved.
