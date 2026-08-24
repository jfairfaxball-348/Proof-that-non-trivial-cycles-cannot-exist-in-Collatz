# RL82 — RL♭ maximum-state prefix balance, exact backward cylinders, and route barrier

Date: 2026-08-24

## 0. Executive conclusion

RL82 pursued the new maximum-state viewpoint selected by the RL81 route-pivot reissue.
For a hypothetical nontrivial positive cycle of the shortcut Collatz map

- `T(n)=n/2` for even `n`,
- `T(n)=(3n+1)/2` for odd `n`,

write

`RL♭ = M = max C`.

The incoming RL81 gate is clean: outer sidecar, fresh internal manifest, and the fast RL81 verifier suite all pass. Under the verification-economy rule the inherited RL81 ledger was therefore accepted without recursively replaying historical expensive certificates.

RL82 does **not** close RL, Gate A, Gate B, nontrivial-cycle exclusion, or Collatz. It does, however, produce a reusable exact architecture for the maximum route and a clean method barrier.

The main results are:

1. **Exact backward-word affine formula.** Every finite backward parity word from `M` has the form
   `x_i=(2^i M-B_i)/3^{o_i}`
   with an exact integer recurrence for `B_i`.
2. **Unique 3-adic ownership cylinder.** A word containing `o` odd predecessors selects one unique residue class for `M mod 3^o`; with `M` even, one unique class modulo `2*3^o`.
3. **Exact bounded/unbounded cylinder theorem.** A word has arbitrarily large capped realizations iff every prefix satisfies
   `2^i <= 3^{o_i}`.
   If some prefix has `2^i>3^{o_i}`, the maximum ceiling gives an explicit finite upper bound on `M`.
4. **Sharp fixed-count numerator envelope.** For a prefix of length `i` with `o` odd and `e=i-o` even predecessors,
   `B_i <= 2^e(3^o-2^o)`,
   with equality exactly at the word `O^o E^e` up to the obvious zero-count degeneracies.
5. **Prefix near-resonance theorem.** Any surplus prefix `2^i>3^o` satisfies
   `M <= 2^e(3^o-2^o)/(2^i-3^o)`
   and hence
   `0 < i log2-o log3 < 2^e/M`.
6. **Exact top residue sharpening.** The RL81 seed `M==26 or44 (mod54)` strengthens to
   `M == 26, 80, or 152 (mod162)`.
7. **Complete-cycle bridge.** For the full backward cycle word of length `A` with `L` odd predecessors,
   `(2^A-3^L)M=B_A`.
   Maximality at every proper prefix becomes an exact family of word inequalities. Thus the maximum route now has a precise interface to the standard global cycle denominator.
8. **Critical balanced escape rays exist at every depth.** In particular the all-odd ray, and also a minimal-density mechanical balanced word, have arbitrarily deep finite cylinders with arbitrarily large capped realizations. Therefore bounded-depth maximum-only pruning cannot close the problem.
9. **Inherited-floor corollary.** Using only the inherited external cycle-minimum floor `R#>=2^71`, every backward prefix through depth `183` of a hypothetical nontrivial cycle maximum must satisfy `2^i<=3^{o_i}`. Depth `184` is the first count-pair at which the coarse fixed-count envelope alone stops proving this.
10. **Local continued-fraction gate.** A surplus prefix whose reduced count ratio satisfies an explicit size condition is forced to be an above-`log_2 3` continued-fraction convergent. This is the intended global consumer for RL83, not further blind residue expansion.

The route decision is therefore:

> **Keep the maximum-state route, but freeze pure finite-depth residue pruning. The live object is the first multiplicative-surplus prefix and its coupling to the global denominator / inherited continued-fraction and packing machinery.**

---

## 1. Incoming authority and verification

Authoritative incoming bundle:

`RL81_Auxiliary_Basin_Transfer_Physical_Lift_Barrier_RL82_RLflat_Maximum_Pivot_2026-08-24.zip`

Fresh RL82 gate:

- outer RL81 `.sha256`: PASS;
- freshly unpacked internal `SHA256SUMS.txt`: PASS;
- `bash verification/run_fast_rl81_verifiers.sh`: PASS;
- inherited RL81 auxiliary-transfer verifier: PASS;
- inherited RL82 seed verifier: PASS.

Frozen inherited global state remains:

- radius-3 primitive/full-`D` obstruction: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite-certificate corollary;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

RL81's auxiliary-blue route remains frozen at the physical common-mode transfer barrier. The earlier unit-lattice/content route remains deferred, not disproved.

---

## 2. Backward symbols and exact word coordinates

Fix a positive even candidate maximum `M`.

For a state `x<=M`, write the two inverse shortcut-Collatz branches as

- `E(x)=2x`, allowed only when `2x<=M`;
- `O(x)=(2x-1)/3`, allowed when `x==2 (mod3)`; when integral it is automatically odd.

Let

`w=w_1...w_d`, `w_j in {O,E}`

be a proposed backward word from `M`, and let

- `x_0=M`;
- `x_i=w_i(x_(i-1))`;
- `o_i=# {j<=i : w_j=O}`;
- `e_i=i-o_i`.

Define `B_0=0` and recursively

- if `w_i=E`, `B_i=2 B_(i-1)`;
- if `w_i=O`, `B_i=2 B_(i-1)+3^{o_(i-1)}`.

### Theorem 2.1 — exact affine backward-word formula

For every legal prefix,

`boxed: x_i = (2^i M-B_i)/3^{o_i}.`

**Proof.** Induct on `i`. The `E` step doubles the previous numerator. The `O` step applies `(2x-1)/3`, adding exactly `3^{o_(i-1)}` to the numerator defect and increasing the power of `3` by one. QED.

This formula is ordinary-`+1` specific: the additive term `B_i` is exactly the accumulated cost of the `-1` in the odd inverse.

---

## 3. Unique ownership cylinder

Let `o=o_d` and `B=B_d`.

The endpoint is integral exactly when

`2^d M == B (mod 3^o)`.

Because `2` is invertible modulo `3^o`, this determines a unique residue class

`boxed: M == 2^{-d} B (mod 3^o).}`

Moreover, the final congruence implies every earlier odd inverse is integral. Indeed, for any prefix with `o_i=q`, later odd additions are divisible by `3^q`, so

`B_d == 2^{d-i} B_i (mod 3^q)`.

Reducing the final congruence modulo `3^q` gives

`2^i M == B_i (mod 3^q)`.

Thus every required odd inverse is legal at the arithmetic level.

Since `3^o` is odd, imposing `M` even selects exactly one class modulo

`boxed: 2*3^o.`

### Classification

This is an **analytic theorem**. It turns the symbolic backward tree into a nested 3-adic cylinder tree.

---

## 4. Exact ceiling criterion and the bounded/unbounded dichotomy

From Theorem 2.1,

`x_i<=M`

is equivalent to

`boxed: (2^i-3^{o_i}) M <= B_i.}`

This is the central maximum-state inequality.

### Theorem 4.1 — prefix-balanced/unbounded-cylinder theorem

Call a finite word `w` **prefix-balanced** when

`2^i <= 3^{o_i}`

for every prefix `1<=i<=d`.

Then:

1. if `w` is prefix-balanced, every ceiling inequality is automatic;
2. its unique 3-adic cylinder contains infinitely many even positive `M`;
3. for all sufficiently large such `M`, every state `x_i` is positive;
4. hence `w` has infinitely many arbitrarily large legal capped realizations.

Conversely, if some prefix has

`2^i>3^{o_i}`, then every capped realization satisfies

`M <= B_i/(2^i-3^{o_i})`,

so only finitely many positive `M` can realize that word under the ceiling.

Therefore:

`boxed: a finite backward word has unbounded capped realizations iff it is prefix-balanced.}`

This is a full analytic classification of finite maximum-only cylinders.

---

## 5. Exact fixed-count numerator envelope

For fixed prefix length `i` and fixed odd count `o`, write `e=i-o`.

### Theorem 5.1 — maximum possible `B_i`

Among all `O/E` words of length `i` containing exactly `o` symbols `O`,

`boxed: B_i <= 2^e(3^o-2^o).}`

The maximum is attained by putting every `O` before every `E`, i.e. by `O^o E^e`.

**Proof.** Compare neighboring blocks `EO` and `OE` after a common prefix having `q` previous odd symbols and current defect `B`.

For `EO`, the two steps produce

`4B+3^q`.

For `OE`, they produce

`4B+2*3^q`.

Thus swapping an `O` left across an `E` increases the defect by `3^q>0`. Repeating adjacent swaps puts all `O` symbols first and maximizes the final defect. For `O^o`, induction gives `B=3^o-2^o`; the final `e` even inverses multiply this by `2^e`. QED.

---

## 6. Surplus-prefix upper bound and near resonance

Suppose a prefix has

`D_i := 2^i-3^o > 0`,

where `o=o_i` and `e=i-o`.

The ceiling plus Theorem 5.1 gives

`boxed: M <= U(i,o) := 2^e(3^o-2^o)/(2^i-3^o).}`

Since `3^o-2^o<3^o`,

`M < 2^e / (2^i/3^o-1)`.

Therefore every surplus prefix satisfies

`0 < 2^i/3^o-1 < 2^e/M`,

and hence, using `log(1+t)<t`,

`boxed: 0 < i log 2-o log 3 < 2^e/M.}`

This is the first scalable global consumer produced by the maximum route: a prefix can cross the multiplicative threshold only through an explicit two-logarithm near resonance whose tolerance is priced by the number `e` of even predecessors and by the absolute maximum `M`.

### First-surplus observation

If `j` is the first index with `2^j>3^{o_j}`, then `w_j=E`.

An `O` step changes the multiplicative ratio by a factor `2/3`, so it cannot create the first crossing from `<=1` to `>1`.

---

## 7. Exact top residue sharpening: mod 162

RL81 proved the seed

`M=18r+8`,

with

`Q=8r+3 -> P=12r+5 -> M=18r+8`,

and extendability forces

`r==1 or2 (mod3)`,

hence `M==26 or44 (mod54)`.

RL82 pushes the ownership one exact layer farther.

### Short-cycle precondition

A positive nontrivial cycle cannot have period `<=4`:

- period `2` is exactly `{1,2}`;
- period `3` would have full backward word `OOE`, for which `2^3-3^2<0`;
- period `4` has only `OOOE` (negative denominator) or `OOEE`, for which the full-cycle equation gives `M=20/7`.

Thus a nontrivial cycle has enough predecessor layers for the following argument.

### Branch A: `r=3s+1`

Then

`M=54s+26`,
`Q=24s+11`.

The actual predecessor of `Q` is forced to be the odd inverse

`R=16s+7`.

At `R`:

- the odd predecessor exists iff `s==1 (mod3)`;
- the even predecessor is `2R=32s+14`, which lies above `M/2`; if this branch is used it can extend only by an odd predecessor, requiring `s==0 (mod3)`.

Therefore `s==2 (mod3)` is impossible, leaving

`M==26 or80 (mod162)`.

### Branch B: `r=3s+2`

Then

`M=54s+44`,
`Q=24s+19`.

The predecessor of `Q` is forced even:

`R=48s+38 > M/2`.

Its predecessor is forced odd:

`S=32s+25 > M/2`.

The next predecessor is again forced odd, so `S==2 (mod3)`. This gives

`s==2 (mod3)`,

hence

`M==152 (mod162)`.

### Theorem 7.1

Every hypothetical nontrivial positive shortcut-Collatz cycle maximum satisfies

`boxed: M == 26, 80, or 152 (mod162).}`

The corresponding forced initial backward grammars are:

- `M==26 (mod162)`: begins `OOOEO`;
- `M==80 (mod162)`: begins at least `OOOO`;
- `M==152 (mod162)`: begins `OOEOO`.

Classification: **elementary analytic theorem**.

---

## 8. Full-cycle denominator bridge and maximum-rotation inequalities

Let the complete backward word have length `A` and contain `L` odd predecessors. Returning to the maximum gives `x_A=M`. Therefore Theorem 2.1 yields

`3^L M = 2^A M-B_A`,

so

`boxed: (2^A-3^L)M=B_A.}`

In particular

`2^A>3^L`.

This is the standard cycle denominator relation, now recovered directly from the maximum-state word coordinates.

For every proper prefix `i`, maximality says

`(2^i-3^{o_i})M <= B_i`.

Substituting `M=B_A/(2^A-3^L)` gives the pure word inequality

`boxed: (2^i-3^{o_i}) B_A <= B_i(2^A-3^L).}`

These are the **maximum-rotation inequalities**.

They identify exactly what maximum geometry contributes beyond the global denominator:

- if `2^i<=3^{o_i}`, the prefix inequality is automatic;
- only surplus prefixes `2^i>3^{o_i}` contain nontrivial maximum information.

This is the desired exact bridge from top geometry to a genuine global cycle invariant.

It is not yet a contradiction.

---

## 9. Two analytic escape rays and the maximum-only barrier

### 9.1 The all-odd ray

For `w=O^d`, repeated odd inversion gives

`x_i+1=(2/3)^i(M+1)`.

Thus the depth-`d` cylinder is

`M == -1 (mod 3^d)`.

Choose any odd positive `q` and set

`M=3^d q-1`.

Then `M` is even and

`x_i=2^i 3^{d-i}q-1`

is positive, odd, and strictly below `M` for every `1<=i<=d`.

Hence for every depth `d` there are infinitely many arbitrarily large maxima passing `d` maximum-only predecessor layers.

### 9.2 Critical minimal-density balanced ray

Let

`alpha=log 2/log 3`.

Define

`o_i=ceil(alpha i)`

and put an `O` at position `i` exactly when `o_i>o_(i-1)`; otherwise put `E`.

Then by construction

`3^{o_i}>=2^i`

for every prefix, so every finite prefix is prefix-balanced and therefore has arbitrarily large capped realizations.

The word begins

`OOEOOEOOEOEOOEOOEOEOO...`

and its depth-5 cylinder is exactly the new survivor class

`M==152 (mod162)`.

Thus the mod-162 Branch B is not an isolated nuisance residue: it lies on a canonical critical balanced ray with asymptotic odd-predecessor density `log 2/log 3`.

No claim is made that one positive integer realizes the entire infinite ray. The theorem is that **every finite prefix** has an unbounded cylinder; equivalently the symbolic maximum-only tree has an immortal nested ray.

### Barrier theorem

Any argument that inspects only a fixed finite number of backward layers using

- inverse integrality,
- predecessor parity,
- positivity,
- the ceiling `x<=M`, and
- residue-cylinder pruning

cannot eliminate all candidate maxima.

A successful maximum-state proof must therefore import a genuinely global consumer: cycle closure/divisibility, a minimum-state coupling, packing, a continued-fraction restriction, or another invariant that is not present in a finite capped inverse tree.

Classification: **analytic method-barrier theorem**.

---

## 10. Exact inherited-floor consequence: 183 forced balanced layers

RL20's audited global CF work retained the external computational input

`R# >= 2^71`

for the least state of any hypothetical nontrivial positive cycle.

Since `M>=R#`, every hypothetical cycle maximum also satisfies

`M>=2^71`.

For a surplus prefix with counts `(i,o)`, Section 6 gives

`M <= U(i,o)`.

The RL82 verifier checks by exact integer arithmetic that for **every** pair

`1<=i<=183`, `0<=o<=i`, `2^i>3^o`,

one has

`U(i,o)<2^71`.

Therefore:

### Theorem 10.1 — 183-step top prefix balance

Conditional only on the inherited external floor `R#>=2^71`, every backward prefix of a hypothetical nontrivial cycle maximum through depth `183` satisfies

`boxed: 2^i <= 3^{o_i}.}`

Equivalently

`o_i >= ceil(i log 2/log 3)`

for `1<=i<=183`.

At depth `184`, the count pair

`(i,o,e)=(184,116,68)`

has

`U(184,116)>2^71`.

Thus `183` is the exact frontier of this **coarse fixed-count envelope**. This does **not** mean an actual depth-184 word/cylinder survives all arithmetic; only that the count-only `B_i` envelope can no longer exclude it.

Classification:

- analytic prefix bound: proved;
- `R#>=2^71`: externally inherited computational input;
- finite `i<=183` inequality audit: exact finite certificate.

---

## 11. Red-team: surplus prefixes really can occur locally

It would be false to promote prefix balance to an unconditional theorem for arbitrary capped Collatz excursions.

The verifier records the exact ordinary-Collatz segment with

`M=890`

and backward word

`OOOOEOOOEOOEOEOOOOEEOOEEOEE`

of length `27`, containing `17` odd predecessors. It yields the exact states

`593,395,263,175,350,233,155,103,206,137,91,182,121,242,161,107,71,47,94,188,125,83,166,332,221,442,884`.

Every state is positive and `<=890`, but

`2^27 > 3^17`.

So the maximum ceiling alone does allow a genuine surplus excursion; the external size floor and/or global cycle closure are substantive ingredients.

Classification: **exact finite computational counterexample** to any proposed universal local prefix-balance theorem.

---

## 12. Local continued-fraction gate for a surplus prefix

Let a surplus prefix have counts `(i,o,e)` with `e=i-o`, and set

`g=gcd(i,o)`,
`p=i/g`,
`q=o/g`,
`beta=log 3/log 2`.

Section 6 gives

`0 < p/q-beta < 2^e/(M o log2)`.

Therefore, whenever

`boxed: 2^(e+1) q^2 < M o log 2,}`

we have

`0 < p/q-beta < 1/(2q^2)`.

By Legendre's theorem:

### Theorem 12.1 — RL♭ prefix CF gate

Under the displayed size condition, the reduced prefix ratio

`p/q=i/o`

must be an above-`beta` continued-fraction convergent of

`beta=log_2 3`.

Equivalently, using `o=gq`, the sufficient condition is

`2^(e+1) q < M g log2`.

This is analytic and preserves the absolute maximum `M`. It is the cleanest available interface between RL82 top geometry and the inherited RL20 continued-fraction programme.

No convergent exclusion is claimed here beyond the inherited RL20 global results.

---

## 13. Ordinary `+1` red-team

For the generalized odd rule

`T_s(n)=(3n+s)/2`,

the odd inverse is

`O_s(x)=(2x-s)/3`.

Repeated odd inversion satisfies

`O_s^i(M)+s=(2/3)^i(M+s)`.

Thus the all-odd depth-`d` cylinder becomes

`M == -s (mod3^d)`.

The absolute increment changes the entire residue ray. The RL82 cylinder architecture therefore retains genuine `+1` dependence and is not merely a homogeneous scaling argument.

---

## 14. Route decision

### What worked

The maximum viewpoint produced a clean exact object:

- symbolic backward word;
- unique ownership cylinder;
- exact ceiling inequality;
- bounded/unbounded classification;
- top-to-global denominator bridge;
- local near-resonance / CF gate.

This is substantially stronger than continuing to print deeper residue classes.

### What does not work alone

Pure maximum-only finite-depth pruning cannot close the problem. Prefix-balanced cylinders survive to arbitrary depth, including a critical minimal-density ray already passing through the `M==152 (mod162)` seed branch.

Therefore do **not** spend RL83 merely extending

`mod162 -> mod486 -> mod1458 -> ...`

without a global consumer.

### Live RL83 consumer

The correct next object is the **first surplus prefix**

`j=min{i:2^i>3^{o_i}}`.

For a genuine cycle such an index exists by the full denominator `2^A>3^L`.

The live question is whether the combination of

- the exact maximum-prefix bound;
- the inherited `R#>=2^71` floor;
- the RL82 local CF gate;
- RL20/RL19 packing and near-resonance facts;
- the full-cycle denominator and maximum-rotation inequalities;
- possibly minimum/maximum coupling

can force an impossible first-surplus configuration.

---

## 15. Proof-state ledger additions

### New proved analytic mathematics

- exact affine backward-word formula;
- unique 3-adic ownership cylinder;
- prefix-balanced iff unbounded finite cylinder theorem;
- exact ceiling criterion;
- fixed-count maximum `B_i` theorem;
- surplus-prefix maximum upper bound;
- prefix two-logarithm near-resonance inequality;
- first-surplus-is-even-symbol lemma;
- exact mod-162 maximum residue theorem;
- full-cycle denominator reconstruction from the maximum word;
- maximum-rotation inequalities;
- all-odd immortal finite-depth cylinder theorem;
- critical mechanical balanced-ray theorem;
- finite-depth maximum-only method barrier;
- generalized `+s` all-odd cylinder identity;
- local prefix continued-fraction gate.

### New exact finite certificates

- fast verifier audit of the analytic formulas and case splits;
- exact `i<=183` fixed-count envelope audit conditional on the inherited external `2^71` floor;
- exact `M=890` capped-surplus counterexample to unconditional local prefix balance.

### Externally inherited certificate/input used

- `R#>=2^71`, as retained by RL20/RL72; not re-audited in RL82 under the verification-economy rule.

### Computational evidence only

No new bounded numerical pattern is promoted beyond the explicitly labelled exact finite audits above.

### New method barriers / demotions

- a deeper residue ladder by itself is not a closure route;
- finite-depth maximum-only predecessor pruning cannot eliminate all candidates;
- prefix balance is **not** universally true for arbitrary capped excursions;
- the depth-184 count pair is only a failure of the coarse envelope, not evidence of a cycle.

### Global closure status

Unchanged: no Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.
