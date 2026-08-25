# RL100 — first-surplus multiplicity scope repair, structural fallback audit, and resumed exact cascade

Date: 2026-08-25

## 0. Executive outcome

RL100 executed the RL99-selected Farey-branch lifting target and then followed its mandatory pivot rules.

**No Gate A global closure, Gate B global closure, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.**

The primary structural result is a scope repair:

> RL83 reduces a raw first-surplus count pair as `(j,o)=(g p,g q)`.  The physical first-Farey machinery used by RL84–RL97 is proved at the raw pair `(j,o)=(p*,q*)`, i.e. `g=1`, not merely at the reduced slope `p*/q*`.  Therefore the authoritative scope of the existing cascade is the **exact first-Farey, raw-`g=1`, full-phase Gate-A branch** unless a new theorem controls multiplicity.

For the frozen first Farey pair

`(p*,q*)=(114,208,327,604,72,057,431,991)`,

the exact Beatty first-crossing inequality alone allows

`1 <= g <= 125,777,718,029`.

This does **not** certify a word or cycle for any `g>1`; it proves only that the inherited first-crossing/Farey arithmetic does not force `g=1`.

RL100 then parameterized the exact RL82 fixed-count maximum envelope for raw multiplicity `g` and proved that the natural envelope is strictly increasing in `g`.  Thus the existing physical-cap route does not yield the desired monotone domination theorem; `g=1` is the strongest member of that envelope, not a worst-case representative of all multiplicities.

For distinct reduced Farey slopes, RL100 derives the next exact denominator gap

`q >= 78,644,250,661`

for every admissible reduced slope other than the first mediant, but this remains an infinite complement and therefore does not satisfy the RL100 success condition.

The ranked Gate-B and ordinary-`+1` basin fallbacks were then red-teamed.  A new canonical gcd-block width inequality is analytic but generalized-increment homogeneous and therefore fails the RL79 ownership discriminator.  The basin route remains blocked at the equality-to-a-physical-state bridge.

Those failures triggered the saved RL99 cascade-resumption condition.  RL100 resumed exact gap-free 2-adic scans from the RL97 frontier and advanced the branch-specific first surviving odd terminal from

`2,921,801,523`

to

`boxed: 2,921,813,805`.

The resumed final frontier is

- wide `(D_w,R_w)=(5,000,030,7,000,000)`;
- middle `(D_m,R_m)=(7,500,031,4,500,000)`;
- deep `(D_d,R_d)=(10,000,032,3,250,000)`;
- ultra `(D_u,R_u)=(15,000,035,2,005,000)`;
- common successor ceiling `L_common=15,000,053`.

A genuine live-floor event occurred in the middle tier:

`7,500,033 at r=4,478,962`,

forcing the safe middle depth repair

`D_m: 7,500,032 -> 7,500,031`.

No earlier promoted interval is invalidated because the new minimum lies beyond the previously certified middle radius.

The final exact `A-C` support is

`lambda=234375/3281264468752`,

`mu=1/7000001`,

with `floor(lambda*C)=3010`.

Using the repaired final geometry, every odd

`2,921,801,523 <= k <= 2,921,813,803`

is excluded on the exact first-Farey/raw-`g=1`/full-phase branch.  That is **6,141 additional consecutive odd values**.  The last margin is `+10,323`; the next odd `2,921,813,805` has margin `-3,297`.

The numerical cascade remains a rigorous cumulative fallback, but its economics remain poor for global closure: a `250,000` increase in deep certified radius bought only `12,282` units of terminal `k`, i.e. `6,141` odd exclusions.

---

## 1. Incoming authority and verification economy

RL100 used the frozen RL99 proof-state/roadmap as authoritative and consulted GitHub read-only.

Load-bearing repository sources selectively recovered were:

- `sessions/RL99/RL100_FAREY_BRANCH_DOMINATION_AND_GLOBAL_GATE_A_LIFT_TARGET.md`;
- `sessions/RL99/RL98_COUPLED_CASCADE_RESUME_AFTER_RL99.md`;
- `sessions/RL83/RL83_RLFLAT_SEGMENT_PRODUCT_CF_FAREY_FRONTIER_AND_GLOBAL_SLOPE.md`;
- `sessions/RL82/RL82_RLFLAT_PREFIX_BALANCE_AND_MAXIMUM_ROUTE_BARRIER.md`;
- `sessions/RL85/RL85_RLSHARP_RLFLAT_COMPARATIVE_BRIDGE_AND_FIRST_FAREY_PHYSICAL_SCALE.md`;
- `sessions/RL87/RL87_PHYSICAL_DIFFERENCE_VALUATION_PACKING_AND_FIRST_FAREY_WINDOW.md`;
- RL79 generalized-increment barrier material;
- RL20 canonical gcd-block geometry / fake-model material;
- RL80/RL81 basin/common-mode material;
- RL97 exact coupled-cascade report/verifiers.

No GitHub writes were made.

The verification-economy rule was retained: historical expensive certificates were not recursively replayed.  Exact new scan bands were compared against their inherited global minima before promotion.

---

## 2. Scope repair: reduced Farey slope does not fix raw first-surplus counts

RL83 writes a surplus prefix count pair `(i,o)` as

`i=g p`, `o=g q`,

with `g=gcd(i,o)` and `gcd(p,q)=1`.

At the first surplus,

`j=ceil(beta o)`, `beta=log_2 3`,

so if `(j,o)=(g p,g q)`, then

`0 < g(p-beta q) < 1`.                                      (2.1)

The reduced product tube

`0 < p log2-q log3 <= q/(3R#)`

contains no `g` and therefore does not force `g=1`.

At the first reduced Farey pair

`p*=114,208,327,604`,

`q*=72,057,431,991`,

an exact 260-term rational atanh enclosure for `log_2 3` certifies

`125,777,718,029 (p*-beta q*) < 1`

but

`125,777,718,030 (p*-beta q*) > 1`.

Hence the Beatty condition itself permits exactly the integer range

`boxed: 1 <= g <= 125,777,718,029.}`

Classification: **analytic scope theorem + exact finite logarithm certificate**.

### What this does and does not mean

This does not construct a legal backward word, a full-phase object, or a Collatz cycle for `g>1`.

It means that the implication

`reduced slope = p*/q*  =>  raw first-surplus counts = (p*,q*)`

is not available from RL83.

RL85's physical scale is explicitly derived at raw counts

`p=114,208,327,604`, `q=72,057,431,991`.

Therefore every downstream theorem whose numerical scale enters through that RL85 cap must retain the raw-`g=1` qualification unless multiplicity is separately controlled.

Classification: **scope clarification / correction to inheritance wording; no demotion of the branch theorems themselves**.

---

## 3. General raw-multiplicity physical envelope

RL82 proves that for a surplus prefix of length `i` and odd count `o`, with `e=i-o`,

`M <= 2^e(3^o-2^o)/(2^i-3^o)`.                             (3.1)

Put

`i=g p`, `o=g q`, `e=g(p-q)`

for a fixed reduced surplus slope `p/q`.

Define

`rho=2^p/3^q >1`,

`A=2^(p-q)`.

Then (3.1) becomes the exact safe envelope

`boxed:`

`U_(p,q)(g)`

`= 2^(g(p-q))(3^(gq)-2^(gq))/(2^(gp)-3^(gq))`

`= (A^g-rho^g)/(rho^g-1).`                                 (3.2)

Equivalently

`U_(p,q)(g)+1 = (A^g-1)/(rho^g-1).`                         (3.3)

Because `q>0`,

`A/rho=(3/2)^q>1`,

so `A>rho>1`.

### Theorem 3.1 — multiplicity makes the RL82 envelope weaker

For every fixed reduced surplus pair `(p,q)`, `U_(p,q)(g)` is strictly increasing for integer `g>=1`.

Proof: write

`(A^g-1)/(rho^g-1)`

`= (A-1)/(rho-1) * [sum_(t=0)^(g-1) A^t]/[sum_(t=0)^(g-1) rho^t]`.

The second factor is the `rho^t`-weighted average of `(A/rho)^t`.  Since `A/rho>1`, adding the `t=g` term adds a value strictly above the previous weighted average.  Thus the ratio, and hence `U`, strictly increases.

Classification: **new analytic theorem**.

### Consequence for RL100 Form B

The natural inherited physical envelope cannot establish that raw `g=1` dominates the same reduced Farey slope with `g>1`.  It moves in the wrong direction: larger multiplicity permits a larger absolute maximum under this envelope.

This does not prove an actual `g>1` physical object is harder; it proves the current envelope is insufficient for a universal domination theorem.

For continuity, RL100 did **not** silently replace the frozen RL87 conservative constants by a tighter `g=1` evaluation of (3.2).  The resumed cascade retained

`C=42,150,931,628`,

`S*=26,594,276,905`,

and `L_common=15,000,053`.

---

## 4. Distinct Farey slopes: exact next-denominator gap, but no finite complement

RL83's frozen-floor Farey neighbors are

`L0=103768467013/65470613321 < beta`,

`U0=10439860591/6586818670 > beta`,

with determinant one.  Their mediant is the first allowed reduced pair

`S0=p*/q*=114208327604/72057431991`.

`S0` is a Farey neighbor of both `L0` and `U0`.

Any different reduced rational in the allowed tube and above `S0` has denominator at least

`q* + 6,586,818,670 = 78,644,250,661`.

Any different reduced rational between `beta` and `S0` has denominator at least

`q* + 65,470,613,321 = 137,528,045,312`.

Therefore:

### Theorem 4.1 — distinct-slope denominator gap

Conditional on the inherited external floor `R#>=2^71`, every admissible reduced first-surplus slope distinct from `p*/q*` satisfies

`boxed: q >= 78,644,250,661.}`

Classification: **analytic Farey consequence + inherited exact rational/log certificate**.

This is not an RL100 success theorem.  It leaves infinitely many larger reduced branches and supplies no physical upper cutoff.

---

## 5. Primary route verdict

The RL100 target allowed success through:

- first-Farey exhaustivity;
- universal first-Farey worst-case domination;
- a finite explicit complementary branch cover.

None was proved.

Two independent obstructions remain:

1. the same reduced first-Farey slope has a large unresolved raw multiplicity range, and the RL82 physical envelope becomes weaker with multiplicity;
2. distinct reduced slopes have a clean next-denominator floor but no finite upper cutoff or monotone physical domination theorem.

This meets the explicit RL100 pivot condition: the first branch is not demonstrated to be universally worst-case and the complement is not finite.

Classification: **method barrier / route decision, not a theorem of nonexistence**.

---

## 6. Ranked Gate-B fallback: new width inequality, but ownership red-team failure

Use RL20's canonical gcd-block decomposition

`A=g a`, `L=g ell`,

`z=2^a/3^ell>1`, `lambda=z^g`,

and let `Q_j` be the ordinary `+1` affine word numerator of block `j`.

RL20's normalized monotone lift gives

`H_(j+1)-H_j = z^j Q_j/3^ell`,

with

`H_0=R`, `H_g=lambda R`.

Hence

`(lambda-1)R = sum_(j=0)^(g-1) z^j Q_j/3^ell`.             (6.1)

For every binary word of weight `ell`, the ordinary word numerator obeys

`Q_j >= 3^ell-2^ell`,

with equality when all odd symbols occur as early as possible.  Since `z^j>=1`, (6.1) yields

`boxed: (lambda-1)R >= g(1-(2/3)^ell).}`                   (6.2)

Classification: **new analytic canonical-block width inequality**.

However, under RL79's generalized odd increment `s`, every block numerator acquires the same factor `s`, while the physical scale transforms compatibly.  After normalization by `s`, (6.2) is unchanged.  It therefore cannot distinguish ordinary `s=1` ownership from the generalized fake family.

The proper-factor/coboundary refinements inspected in the same fallback likewise reduced to already-known normalized block transport rather than producing an absolute owned close-pair radius.

Therefore the ranked Gate-B fallback did not close Gate B.

---

## 7. Ordinary-`+1` basin fallback

RL80's analytic blue LTE comb and certified backward basin genuinely consume the ordinary `+1` map and pass the RL79 discriminator.

But RL80/RL81 already isolate the remaining problem: basin membership of an auxiliary quotient coordinate, or arbitrarily fine physical proximity to certified blue rays, does not imply equality with an actual owned cycle state.  RL81 common-mode freedom blocks that inference.

RL100 found no new equality-level physical bridge in this fallback.

Classification: **route remains open but current architecture blocked at physical equality/ownership**.

---

## 8. Resumed exact coupled cascade

After the higher-ranked structural routes met their failure conditions, RL100 resumed the saved RL97 cascade exactly as permitted by the RL99 roadmap.

Incoming frozen branch state:

- first live odd `k=2,921,801,523`, margin `-3,549`;
- wide `(5,000,030,7,000,000)`;
- middle `(7,500,032,4,350,000)`;
- deep `(10,000,032,3,000,000)`;
- ultra `(15,000,035,1,680,000)`;
- feasible supports `A-C`, `C-D`, `D-E`;
- `L_common=15,000,053`.

### 8.1 New exact gap-free scan coverage

RL100 completed exact extensions through:

- ultra: `1,680,001..2,005,000` modulo `2^15,000,056`;
- middle: `4,350,001..4,500,000` modulo `2^7,500,056`;
- deep: `3,000,001..3,250,000` modulo `2^10,000,056`.

Notable exact events:

- ultra first resumed band: `15,000,041 at r=1,692,530`;
- deep first resumed band: `10,000,039 at r=3,022,568`;
- ultra near-floor event: `15,000,038 at r=1,820,306`;
- ultra tie with the inherited global minimum: `15,000,037 at r=1,919,735`;
- middle genuine new minimum: `7,500,033 at r=4,478,962`.

Thus:

- `D_u=15,000,035` remains valid;
- `D_d=10,000,032` remains valid;
- middle must be repaired to `D_m=7,500,031`.

The middle repair is forward-local to the newly extended radius; it does not invalidate previously promoted results.

Classification: **new exact finite certificates + live floor repair**.

### 8.2 Final repaired four-tier geometry

Final staircase-complement corners are

`A=(0,7,000,001)`

`B=(5,000,031,4,500,001)`

`C=(7,500,032,3,250,001)`

`D=(10,000,033,2,005,001)`

`E=(15,000,036,0)`.

The exact feasible nonnegative pair supports remain precisely

- `A-C`;
- `C-D`;
- `D-E`.

The terminal-direction optimal support is `A-C`:

`boxed: lambda=234375/3281264468752,}`

`boxed: mu=1/7000001.}`

Its exact values at the five corners are

- `A: 1`;
- `B: 3281266734377/3281264468752 >1`;
- `C: 1`;
- `D: 3283605963127/3281264468752 >1`;
- `E: 878908359375/820316117188 >1`.

Also

`floor(lambda*C)=3010>2`,

so the inherited top-stratum monotonicity remains safe.

Classification: **updated exact four-tier supporting-line theorem + exact convex-envelope audit**.

### 8.3 Exact interval propagation

At the previously live odd

`k=2,921,801,523`,

the repaired final support gives margin

`+83,636,507`.

The exact rational verifier checks every odd through

`k=2,921,813,803`.

All **6,141** values are excluded.

At the last excluded odd:

`k=2,921,813,803`,

`Q_min=123,139,091,657,856,223,450`,

`D_b=18,082,139,992,506,206`,

`R_b^max=11,408,591,894,055,483`,

weighted bad-block bound `2,921,374,341`,

forced multiscale-good blocks `439,461`,

short-successor capacity `429,138`,

margin `+10,323`.

At the next odd:

`k=2,921,813,805`,

`Q_min=123,139,091,657,856,223,302`,

`D_b=18,082,224,294,369,610`,

`R_b^max=11,408,645,082,609,389`,

weighted bad-block bound `2,921,387,961`,

forced multiscale-good blocks `425,843`,

short-successor capacity `429,140`,

margin `-3,297`.

Therefore the updated branch-specific window is

`boxed: 2,921,813,805 <= k <= 42,150,931,559, k odd,}`

under the exact first-Farey/raw-`g=1`/full-phase qualification.

Classification: **new exact finite 2-adic certificates + exact rational interval audit**.

---

## 9. Proof-state ledger additions and correction ledger

### New proved analytic mathematics

1. Raw first-surplus multiplicity is a separate parameter after reducing the Farey slope.
2. Exact general RL82 multiplicity envelope (3.2).
3. Strict monotonic worsening of that envelope with `g`.
4. Distinct admissible reduced slopes satisfy `q>=78,644,250,661` under the inherited external floor.
5. Canonical gcd-block width inequality (6.2).

### New exact finite certificates

1. Beatty multiplicity ceiling `g<=125,777,718,029` at the first reduced pair.
2. Gap-free ultra/middle/deep scan extensions to radii `2,005,000 / 4,500,000 / 3,250,000` respectively.
3. Middle floor event `7,500,033 at r=4,478,962` and repaired safe depth `7,500,031`.
4. Exact elimination of 6,141 additional odd raw-`g=1` first-Farey branch terminals.

### New method barriers / route decisions

1. The natural physical maximum envelope does not dominate larger multiplicities; it weakens with `g`.
2. A larger Farey denominator floor alone leaves an infinite complement.
3. The new Gate-B gcd-block width theorem is generalized-increment homogeneous and not ownership-sensitive enough.
4. The blue-basin route still lacks equality with an actual owned physical cycle state.
5. The resumed cascade remains cumulative but has poor long-range global economics.

### Correction / scope repair

Replace any shorthand statement

“RL84–RL100 covers the exact first-Farey branch”

by the more precise

“RL84–RL100 covers the exact first-Farey **raw-`g=1`** full-phase branch, unless a separate theorem has first reduced the multiplicity.”

No theorem proved within that branch is demoted.

### External input retained

Any statement using `R#>=2^71` remains conditional on that inherited **external computational input**.

---

## 10. Strategic conclusion and RL101 selection

RL100 shows that the missing first-Farey lifting problem is not merely “what happens at the next continued-fraction entry?”  There is already an unresolved dimension at the same reduced slope: raw multiplicity.

The best RL101 target is therefore:

> **Raw first-surplus multiplicity / cylinder / full-ownership theorem.**  Use the full `3^(gq)` word cylinder, ordinary `+1` content, global `D|Q` ownership, and equal-vs-distinct local/global slope structure to force `g=1`, eliminate `g>=2`, or reduce `g` to a finite explicitly eliminable set.

The saved cascade should remain a checkpointed fallback at the repaired `R_d=3.25M` state.  Do not make blind scan extension the primary RL101 task.
