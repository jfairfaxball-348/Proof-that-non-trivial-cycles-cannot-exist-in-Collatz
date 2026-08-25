# RL83 — RL♭ segment-product first-surplus gate, exact Farey frontier, and global-slope coupling

Date: 2026-08-24

## 0. Executive conclusion

RL83 continued the RL82 maximum-state route with the required global consumer.  The incoming RL82 outer sidecar, fresh internal manifest, and fast verifier suite all pass.  Under the verification-economy rule, the frozen RL82 ledger was accepted and no historical expensive suite was recursively replayed.

RL83 does **not** prove Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz.  It does, however, replace RL82's weak local first-surplus tolerance by a genuine closed-cycle product bound and pushes the conditional balanced-prefix frontier from depth `183` to more than **114 billion**.

The main new results are:

1. **Exact segment odd-step product identity.**  Every backward prefix from the cycle maximum is also a forward physical segment ending at the maximum.  Its multiplicative defect is controlled by the product of its own odd-step `+1` factors.
2. **Uniform surplus-prefix tube.**  If a prefix of length `i` with `o` odd predecessors is surplus, then
   `0 < i log2-o log3 <= o/(3R#)`.
   After reduction `i/o=p/q`,
   `0 < p log2-q log3 <= q/(3R#)`.
   This is the same least-state scale as the RL20 global CF gate and is dramatically stronger than RL82's `2^e/M` tolerance.
3. **Exact first-surplus Beatty identity.**  At the first surplus index `j`, with `o=o_j`,
   `j=ceil(o log_2 3)` and the last backward symbol is `E`.
4. **Exact optimal frozen-floor Farey frontier.**  Conditional on the inherited external input `R#>=2^71`, the smallest reduced denominator of *any* rational that can satisfy the new surplus tube is
   `q*=72,057,431,991`,
   with first admissible numerator
   `p*=114,208,327,604`.
   The pair is the Farey mediant
   `114208327604/72057431991`
   between a certified lower and upper neighbor around `log_2 3`.
5. **114,208,327,603 forced balanced layers.**  Conditional on the same external floor, every backward prefix from a hypothetical cycle maximum through depth
   `114,208,327,603`
   satisfies `2^i<=3^{o_i}`.  If the first surplus occurs at the very next depth, its reduced count pair is forced to be exactly `(p*,q*)`.
6. **Global RL20 denominator upgrade.**  The same Farey argument applies to the global reduced ratio `A/L`, improving the frozen-floor consequence to
   `L/gcd(A,L) >= 72,057,431,991`
   and
   `A/gcd(A,L) >= 114,208,327,604`.
7. **Proper-prefix overshoot ordering.**  If the first surplus is proper (`j<A`), then its raw multiplicative overshoot is strictly smaller than the full-cycle overshoot:
   `2^j/3^o < 2^A/3^L`.
   Equivalently the complementary count block is itself multiplicatively surplus.
8. **Local/global reduced-slope dichotomy.**  If the local first-surplus reduced slope and global reduced slope are distinct, their denominators `q,Q` obey
   `qQ>3R# log2`.
   If they are equal, the local and global defects have an exact difference-of-powers gcd structure.
9. **First-surplus count-optimization barrier.**  Requiring every proper prefix to be balanced does *not* improve RL82's fixed-count `B_j` envelope.  The word `O^oE^e` is admissible at every first-crossing count pair and still attains the envelope.  Its cylinder is `M==-1 (mod3^o)`, hence for `o>=4` it lies exactly in the surviving top branch `M==80 (mod162)`.  Therefore first-surplus balance plus the current top residue theorem cannot sharpen the numerator envelope.
10. **Arithmetic survivor / route barrier.**  The pair `(p*,q*)` actually satisfies the frozen-floor product tube and the first-crossing inequality.  Thus product/CF arithmetic alone does not close the route.  The next consumer must use word-cylinder ownership, full-cycle divisibility, equal-vs-distinct slope structure, or another genuinely global invariant.

The route decision is therefore:

> **Keep the RL♭ route.  Freeze count-only first-surplus optimization and blind residue extension.  The live RL84 object is the first Farey survivor and its exact 3-adic cylinder / full-cycle slope / denominator ownership interaction.**

---

## 1. Incoming authority and selective historical interfaces

Authoritative incoming bundle:

`RL82_RLflat_Prefix_Balance_and_First_Surplus_Barrier_RL83_CF_Global_Consumer_2026-08-24.zip`

Fresh RL83 gate:

- outer RL82 `.sha256`: **PASS**;
- freshly unpacked RL82 `SHA256SUMS.txt`: **PASS**;
- `bash verification/run_fast_rl82_verifiers.sh`: **PASS**.

The frozen RL82 global state remains unchanged:

- radius-3 primitive/full-`D` obstruction: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite-certificate corollary;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

Selective GitHub recovery under the verification-economy rule used only the needed interfaces:

- `sessions/RL20/RL20_GLOBAL_COPRIME6_PACKING_AND_CF_GATE.md`;
- `sessions/RL20/verify_rl20_global_cf_gate.py`;
- `sessions/RL20/RL20_FINAL_RETURN_CF_DECOUPLING.md`;
- `sessions/RL20/RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md`;
- RL72 global audit / lemma catalogue and RL75 route tournament for strategic comparison.

No historical expensive certificate was rerun.

---

## 2. Setup and notation

Use the shortcut Collatz map

- `T(n)=n/2` for even `n`;
- `T(n)=(3n+1)/2` for odd `n`.

Let `C` be a hypothetical nontrivial positive cycle and put

`M=RL♭=max C`, `R#=min C`.

Follow RL82's backward orbit from `M`:

`x_0=M, x_1, ..., x_i, ...`.

For the first `i` backward steps let

- `o_i` be the number of `O` steps / odd forward inputs;
- `e_i=i-o_i`;
- `B_i` be the exact RL82 additive defect, so
  `x_i=(2^i M-B_i)/3^{o_i}`.

Write

`Delta_i = i log2-o_i log3`.

A prefix is **surplus** exactly when `Delta_i>0`, equivalently `2^i>3^{o_i}`.

For the full cycle, with length `A` and odd count `L`, put

`Delta = A log2-L log3 >0`.

---

## 3. Exact segment odd-step product identity

### Theorem 3.1 — product identity for a maximum-ending segment

Fix any backward prefix of length `i`.  Read the same physical states forward from `x_i` to `M`.

For an even forward input `y`,

`T(y)/y=1/2`.

For an odd forward input `y`,

`T(y)/y=(3y+1)/(2y)=(3/2)(1+1/(3y))`.

There are exactly `o_i` odd forward inputs in this segment.  Therefore

`boxed: M/x_i = (3^{o_i}/2^i) prod_(y odd in segment) (1+1/(3y)).`

Taking logarithms gives

`boxed: log(M/x_i) = -Delta_i + S_i,`

where

`S_i = sum_(y odd in segment) log(1+1/(3y)).`

Because `M` is the cycle maximum, `x_i<=M`, so `log(M/x_i)>=0`.  Hence

`boxed: Delta_i <= S_i.}`

Every phase state is at least `R#`, so

`S_i <= o_i log(1+1/(3R#)) <= o_i/(3R#)`.

Thus for **every** prefix,

`boxed: Delta_i <= o_i/(3R#).}`

For a surplus prefix this becomes

`boxed: 0 < i log2-o_i log3 <= o_i/(3R#).}`

### Classification

**Analytic theorem.**  This is a segment version of the global odd-step product mechanism, but the proof above is self-contained and uses the fact that the segment is physically contained in the same closed cycle.

### Why this is stronger than RL82

RL82 had

`0 < Delta_i < 2^{e_i}/M`.

The new bound is

`Delta_i <= o_i/(3R#)`.

It has no exponentially growing `2^{e_i}` cost.  The first-surplus tolerance is now priced by the *least physical cycle state*, exactly the global quantity available to RL20.

---

## 4. Reduced local slope and the inherited CF consumer

Let a surplus prefix have counts `(i,o)` and reduce

`g=gcd(i,o)`, `p=i/g`, `q=o/g`.

Then

`Delta_i = g(p log2-q log3)`

and `o=gq`.  The segment product bound gives

`boxed: 0 < p log2-q log3 <= q/(3R#).}`      (RL83.1)

Equivalently, for

`beta=log_2 3=log3/log2`,

`boxed: 0 < p/q-beta <= 1/(3R# log2).}`       (RL83.2)

This is exactly the same right-hand approximation tube used by the RL20 global product gate.

Consequently every surplus prefix can consume the already-audited RL20 continued-fraction arithmetic; the RL82 condition

`2^(e+1)q^2 < M o log2`

is no longer the primary gate.

---

## 5. First-surplus geometry

Let

`j=min{i>=1:2^i>3^{o_i}}`

and write `o=o_j`.

RL82 already proved the last symbol is `E`.  Therefore `o_{j-1}=o_j=o` and

`2^{j-1} <= 3^o < 2^j`.

Since `beta=log_2 3` is irrational,

`j-1 < beta o < j` is allowed on the left as equality only in the exponential form; in fact equality cannot occur.  Hence

`boxed: j = ceil(beta o).}`

This is the exact Beatty/first-crossing identity.

If `j/o=p/q` in lowest terms, with `j=gp`, `o=gq`, then

`0 < g(p-beta q) < 1`.

The product bound gives the much stronger least-state restriction (RL83.2).

---

## 6. Exact frozen-floor Farey frontier

Now use only the inherited external computational input retained by RL20/RL72:

`R# >= R0 := 2^71 = 2361183241434822606848`.

Every surplus reduced ratio must satisfy

`0 < p/q-beta <= C0`,

where

`C0=1/(3R0 log2)`.

RL20's exact CF verifier already identified the nearby consecutive convergents.  RL83 uses the following two exact rationals:

Lower neighbor

`L0 = 103768467013 / 65470613321 < beta`,

upper neighbor

`U0 = 10439860591 / 6586818670 > beta`.

They are Farey neighbors because

`10439860591*65470613321 - 103768467013*6586818670 = 1`.

The RL83 rational-interval verifier proves exactly that

`U0-beta > C0`.

Therefore the entire allowed tube `(beta,beta+C0]` lies strictly between `L0` and `U0`.

A standard Farey-neighbor lemma says that every reduced rational strictly between `a/b<c/d` with `bc-ad=1` has denominator at least `b+d`.  Thus every allowed reduced denominator obeys

`q >= 65470613321+6586818670`.

Define

`boxed: q* = 72057431991.}`

The mediant is

`S0 = (103768467013+10439860591)/(65470613321+6586818670)`

so

`boxed: S0 = 114208327604/72057431991.}`

The exact verifier proves

`beta < S0 <= beta+C0`.

Hence the denominator bound is **sharp for the frozen product tube**:

### Theorem 6.1 — exact minimal product-tube denominator at `R0`

Conditional on `R#>=2^71`, every reduced surplus-prefix ratio satisfies

`boxed: q >= 72,057,431,991.}`

Moreover `72,057,431,991` is the smallest denominator not excluded by the uniform product-tube arithmetic, and at that denominator the unique first Farey entry is

`boxed: p/q = 114,208,327,604 / 72,057,431,991.}`

Classification: **exact finite arithmetic certificate + inherited external computational input + analytic Farey lemma**.

This strictly strengthens RL20's earlier Legendre-only frozen-floor threshold

`q>=49,547,666,544`.

---

## 7. 114-billion forced balanced-prefix theorem

The verifier also proves exactly

`(p*-1) log2 < q* log3 < p* log2`,

where

`p*=114208327604`, `q*=72057431991`.

Thus

`p*=ceil(beta q*)`.

For any allowed reduced surplus ratio `p/q`, Theorem 6.1 gives `q>=q*`.  Since `p/q>beta`,

`p > beta q >= beta q* > p*-1`,

so `p>=p*`.

Every surplus prefix length is `i=gp` with `g>=1`.  Therefore:

### Theorem 7.1 — frozen-floor RL♭ balance frontier

Conditional on the inherited external input `R#>=2^71`, no backward prefix from a hypothetical nontrivial cycle maximum can be surplus before depth

`boxed: 114,208,327,604.}`

Equivalently every prefix through depth

`boxed: 114,208,327,603}`

satisfies

`2^i<=3^{o_i}`.

If the first surplus occurs exactly at depth `114,208,327,604`, then necessarily

- `g=1`;
- `o=q*=72,057,431,991`;
- `j=p*=114,208,327,604`;
- the reduced ratio is exactly the Farey mediant `S0`.

This replaces RL82's coarse fixed-count frontier at depth `183` by a global-product/CF frontier more than eight orders of magnitude deeper.

Classification: **analytic consequence of Theorem 3.1 + exact finite Farey certificate + inherited external floor**.

No finite word/cylinder at the new depth is claimed to exist.

---

## 8. Upgrade of the global RL20 reduced-denominator floor

For the complete cycle, RL20's odd-step product gives

`0 < P log2-Q log3 <= Q/(3R#)`

for the reduced global ratio

`P/Q = A/L`, `G=gcd(A,L)`.

This is the same tube as (RL83.1).  Therefore Theorem 6.1 applies unchanged:

### Corollary 8.1

Conditional on `R#>=2^71`,

`boxed: L/gcd(A,L) >= 72,057,431,991,}`

and

`boxed: A/gcd(A,L) >= 114,208,327,604.}`

In particular

`L>=72,057,431,991`, `A>=114,208,327,604`.

This is a new exact finite arithmetic strengthening of the RL20 frozen-floor denominator certificate; it does not alter the analytic global product identity itself.

---

## 9. Proper first surplus is smaller than the global overshoot

Let the first surplus occur at a proper prefix `j<A`, with state `x_j<M` by primitivity.

Split the full set of odd forward inputs into the segment from `x_j` to `M` and its complementary segment from `M` back to `x_j`.

For the first segment,

`Delta_j = S_j - log(M/x_j)`.

For the full cycle,

`Delta = S_j+S_comp`.

Therefore

`Delta-Delta_j = S_comp+log(M/x_j) >0`.

Hence:

### Theorem 9.1 — strict overshoot ordering

For every proper first-surplus prefix,

`boxed: 0<Delta_j<Delta.}`

Equivalently

`boxed: 1 < 2^j/3^o < 2^A/3^L.}`

Also

`Delta_comp=(A-j)log2-(L-o)log3=Delta-Delta_j>0`,

so

`boxed: 2^(A-j)>3^(L-o).}`

Thus a proper first-surplus cut decomposes the closed cycle into two multiplicatively surplus count blocks.

If `j=A`, the first-surplus prefix is the full return and equality replaces the strict local/global comparison.

Classification: **analytic theorem**.

---

## 10. Local/global reduced-slope dichotomy

Let

`p/q=j/o`

be the reduced first-surplus slope and

`P/Q=A/L`

the reduced global slope.

Both lie in the same tube

`beta < r <= beta + 1/(3R# log2)`.

### Theorem 10.1 — distinct-slope denominator product

If

`p/q != P/Q`,

then reduced rational separation gives

`|p/q-P/Q| >= 1/(qQ)`.

Because both rationals lie on the same side of `beta` inside a tube of width `1/(3R# log2)`,

`|p/q-P/Q| < 1/(3R# log2)`.

Therefore

`boxed: qQ > 3R# log2.}`

At the frozen floor, the verifier certifies

`floor(3*2^71*log2)=4,909,942,519,757,819,773,358`.

So distinct local/global slopes require the exact integer consequence

`qQ >= 4,909,942,519,757,819,773,359`.

Classification: **analytic theorem + exact evaluation of the frozen numerical threshold**.

### Theorem 10.2 — equal-slope defect gcd structure

If instead

`p/q=P/Q`,

write

`(j,o)=g(p,q)`, `(A,L)=G(p,q)`.

For a proper prefix Theorem 9.1 forces `g<G`.

Put

`a=2^p`, `b=3^q`.

Then

`D_j=2^j-3^o=a^g-b^g`,

`D=2^A-3^L=a^G-b^G`.

The standard gcd identity for coprime `a,b` gives

`boxed: gcd(D_j,D)=a^d-b^d,  d=gcd(g,G).}`

In particular, if `g|G`, then

`boxed: D_j | D.}`

This is a genuine, though conditional, local-to-global divisibility interface.  It does not by itself contradict cycle closure.

Classification: **analytic theorem**.

---

## 11. First-surplus optimization barrier: the coarse `B` envelope cannot improve

RL83 was explicitly asked to optimize `B_j` subject to the first-crossing condition and all earlier prefixes being balanced.

That hoped-for count-only sharpening is impossible.

Fix any first-crossing count pair `(j,o)`:

`2^(j-1)<=3^o<2^j`, `e=j-o`.

Consider

`w=O^o E^e`.

For the initial `O` block every prefix satisfies `2^i<=3^i`.  During the following `E` block, every proper prefix has length at most `j-1` and still has odd count `o`, so

`2^i<=2^(j-1)<=3^o`.

Thus **every proper prefix is balanced**, and the final `E` is the first surplus crossing.

RL82's exact adjacent-swap theorem gives

`B_j(w)=2^e(3^o-2^o)`,

which is the unrestricted fixed-count maximum.

Therefore:

### Theorem 11.1 — first-surplus fixed-count barrier

Imposing

- first surplus at the final step;
- all previous prefixes balanced

does **not** lower the RL82 fixed-count envelope at all.

Moreover for `w=O^oE^e`,

`B_j == -2^j (mod3^o)`,

so its ownership cylinder is

`boxed: M == -1 (mod3^o).}`

For `o>=4`, this gives `M==80 (mod162)` after imposing `M` even.  Hence the exact envelope-maximizing word also matches the RL82 surviving top grammar `OOOO...` and top residue branch `80 mod162`.

### Consequence

Neither

- first-surplus prefix balance alone, nor
- first-surplus balance plus the current `mod162` maximum seed

can sharpen the count-only numerator envelope.

The missing information must be the **interval/cylinder collision itself** or a stronger full-cycle ownership/divisibility condition.

Classification: **analytic method-barrier theorem**.

---

## 12. The first Farey survivor is a real arithmetic survivor

The pair

`(p*,q*)=(114208327604,72057431991)`

satisfies, exactly,

`(p*-1)log2 < q*log3 < p*log2`

and

`0 < p*log2-q*log3 <= q*/(3*2^71)`.

Thus it is simultaneously:

- an above-`beta` reduced rational;
- a valid first-crossing **count pair**;
- compatible with the uniform segment-product bound at the inherited floor.

It is **not** claimed to correspond to a legal backward word/cylinder in a genuine cycle.

The verifier also certifies that this particular arithmetic survivor would be excluded if the actual least state satisfied

`R# >= 4,358,487,209,795,430,953,243`.

Equivalently, if a first surplus occurs at the exact earliest arithmetic pair, then necessarily

`2^71 <= R# <= 4,358,487,209,795,430,953,242`.

This is a useful sensitivity bound, not a closure theorem.

### Method barrier

The new product/CF consumer has therefore reached a sharp arithmetic frontier under the frozen external floor.  Continuing only by extending a generic CF list would move the frontier but would not consume the word cylinder or full-cycle ownership.

---

## 13. Relation to the inherited RL20 decoupling warning

RL20 already proved that a naive splice

`global CF class -> final-return 3-adic endpoint address -> contradiction`

decouples without an additional global ownership/divisibility input.

RL83 does **not** revive that dead route.

The new local first-surplus tube is stronger because it is attached to a physical maximum-ending segment, but after the Farey frontier the same strategic warning applies: the slope arithmetic and the 3-adic word cylinder must be coupled by a theorem that knows they belong to the **same closed cycle**.

---

## 14. Critical balanced-ray red team

RL82's mechanical balanced ray can still be shadowed for arbitrarily many finite layers.  RL83 now explains quantitatively what a genuine closed cycle must do when it finally exits that balanced regime:

- the first exit cannot occur before depth `114,208,327,604` under the inherited floor;
- its reduced slope must enter an ultra-thin right-hand Farey/CF tube;
- the first arithmetic entry into that tube is the single pair `(p*,q*)` above.

This does **not** eliminate long shadowing.  It converts the eventual exit into a much more rigid global arithmetic event.

---

## 15. Ordinary `+1` sensitivity

The segment theorem retains genuine ordinary-Collatz additive information.

For the generalized odd rule

`T_s(y)=(3y+s)/2`,

the odd multiplier is

`T_s(y)/y=(3/2)(1+s/(3y))`.

The RL83 segment sum becomes

`sum log(1+s/(3y))`.

Thus the exact `1/(3R#)` tube is specific to `s=1`; a homogeneous count argument would not produce it.

---

## 16. Route decision and RL84 handoff

### Keep

- RL82 exact backward affine/cylinder coordinates;
- RL83 segment-product surplus tube;
- exact Farey frontier `(p*,q*)`;
- proper local/global overshoot ordering;
- equal/distinct reduced-slope dichotomy.

### Freeze / do not repeat

- blind `mod162 -> mod486 -> ...` expansion;
- count-only `B_j` optimization under first-surplus balance;
- naive final-return-address + CF splicing already barriered by RL20;
- treating the 114-billion frontier as a proof of nonexistence.

### Live RL84 object

The first useful unresolved object is the first Farey survivor together with the exact word cylinder:

`p*/q* = 114208327604/72057431991`.

The next session should test whether one can prove an incompatibility between

- first-surplus balanced-prefix word ownership;
- `M==26,80,152 (mod162)`;
- the unique cylinder `M==m_w (mod2*3^o)`;
- the physical minimum/maximum bounds;
- the full denominator `D=2^A-3^L`;
- the equal-vs-distinct global slope dichotomy.

If the cylinder and slope remain independent after a serious exact attack, freeze the RL♭ route at that barrier and return to the RL75 ranked hybrid owned-macro periodicity/packing route rather than extending local residues.

---

## 17. Proof-state ledger additions

### New proved analytic mathematics

- maximum-ending segment odd-step product identity;
- uniform surplus-prefix least-state bound `Delta_i<=o_i/(3R#)`;
- reduced local CF tube `0<p log2-q log3<=q/(3R#)`;
- exact first-surplus Beatty identity `j=ceil(beta o)`;
- Farey-neighbor denominator lemma application;
- proper first-surplus overshoot ordering and complementary surplus;
- distinct local/global slope denominator-product theorem;
- equal-slope local/global defect gcd theorem;
- first-surplus fixed-count-envelope barrier;
- compatibility of the envelope maximizer with `M==80 mod162`.

### New exact finite certificates

- rational intervals for `log2`, `log3`, and `beta` around the frozen Farey pair;
- exact determinant-one check for the Farey neighbors;
- exact exclusion of the upper neighbor from the `R0` tube;
- exact inclusion of the mediant in the `R0` tube;
- exact values
  `q*=72,057,431,991`,
  `p*=114,208,327,604`;
- exact first-survivor least-state threshold floor
  `4,358,487,209,795,430,953,242`;
- exact frozen value
  `floor(3*2^71*log2)=4,909,942,519,757,819,773,358`;
- finite algebra spot-audit of the `O^oE^e` barrier formulas.

### Externally inherited certificate/input used

- `R#>=2^71`, retained by RL20/RL72 and not recursively re-audited under the verification-economy rule.

### Computational evidence only

No new bounded search pattern is promoted as mathematical evidence.  The bundled program is an exact arithmetic verifier for the finite constants above.

### New method barriers / dead routes

- first-surplus balanced-prefix optimization does not reduce the fixed-count `B` maximum;
- the exact maximizer is compatible with the surviving `80 mod162` top branch;
- product/CF arithmetic alone has a genuine first Farey survivor at the frozen floor;
- a closure proof must now couple the slope to word-cylinder/full-cycle ownership, not merely compute more approximants.

### Corrections / demotions

None to the frozen RL82 ledger.  The depth-183 statement remains correct but is superseded numerically, under the same inherited floor, by the stronger RL83 segment-product/Farey theorem.

### Global closure status

Unchanged: no Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.
