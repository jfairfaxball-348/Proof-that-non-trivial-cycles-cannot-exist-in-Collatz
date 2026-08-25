# RL85 — historical RL# / RL♭ comparison, first-Farey physical-scale closure, and synchronized-return bound

Date: 2026-08-25

## 0. Executive outcome

RL85 continued the frozen RL84 target without changing the global proof status.

**No Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.**

The historical RL#/RL♭ comparison is now sharp enough to separate one negative result from one genuinely productive splice.

### Historical comparison: direct roof transplant is negative

The historical object `R#` was defined as the least positive red integer among all counterexamples, not as the maximum of a chosen hypothetical cycle and not automatically as its cycle minimum. Its strongest lower-barrier/corridor conclusions consume global minimality. They do not transplant to `F=2M`, `M`, or the immediate cycle predecessor `P=(2M-1)/3`.

In fact the immediate roof objects are provably mismatched with historical `R#`:

- `F=2M` is even;
- `M` is even;
- RL82's forced top grammar starts with `OO` in every surviving maximum residue class, so `P=(2M-1)/3 == 2 (mod 3)`;
- historical `R#` is odd and is not `2 mod 3`.

Moreover the owned odd edge `P -> M` has accelerated valuation

`nu_2(3P+1)=nu_2(2M)=1+nu_2(M)>=2`,

so the historical pure-`r=1` corridor mechanism does not attach to the canonical roof fork. The seed-independent 3-adic sibling odometer does transfer, but it is residue-complete and therefore does not provide the missing lower cylinder-height bound.

### New positive splice: RL84 supplies the physical scale RL76 lacked

At the exact RL83 first Farey pair

`p=114,208,327,604`,

`q=72,057,431,991`,

the RL84 ceiling and defect certificate imply the stronger physical bound

`M < 400,000,000,000 (3/2)^q`.

This upper bound is already below the full cylinder modulus `2*3^q`. Therefore the actual maximum `M` equals the least positive even representative of its `q`-digit maximum cylinder.

Put

`h=ceil(3q/8)=27,021,536,997`.

An exact rational comparison gives

`boxed: M < 3^h.`

Hence, when `M` is written as a zero-padded `q`-digit ternary cylinder representative, at least

`q-h = 45,035,894,994`

leading ternary digits are zero.

This is substantially stronger than RL84's conservative half-height statement.

### New RL75/RL76 hybrid consequence

RL76 proved that if a nonempty synchronized height-one word `c` of length `n` closes an odd quotient state `J` inside a genuine paired physical trajectory, then for one occurrence

`A_0=alpha+2^n m`,

`B_0=alpha+3*2^n m`,

where `alpha=(J-1)/2` and, for a proper segment of a primitive cycle, `m!=0`.

Therefore

`B_0-A_0 = 2^(n+1)m`.

If the paired physical states are genuine states of the same hypothetical cycle, they lie in `[R,M]`, so

`boxed: 2^(n+1) <= |B_0-A_0| <= M-R.}`

At the exact first-Farey survivor, `M<3^h` and `3^5<2^8`, hence every proper synchronized quotient return satisfies

`boxed: n <= 43,234,459,194.}`

This is a context-independent physical-scale bound on **every closed quotient return span** in the first-Farey/full-phase intersection. It directly repairs the specific RL76 objection that repeat depth could be hidden in an unbounded physical scale.

For the canonical pumps this gives

- `c=10`: repeat depth `r <= 21,617,229,597`;
- `c=101`: the general span bound gives `r<=14,411,486,398`, while the stronger RL76 exit normal form gives
  `boxed: r <= 13,510,768,498}`.

Thus the unbounded RL74 shrink/growth stress family is no longer scale-free in the exact first-Farey physical branch.

### Aperiodic remainder

Let

`B=43,234,459,194`.

Inside any one synchronized height-one block, two equal quotient values `J_i=J_j` with `j-i>B` would create a forbidden proper closed return of span `>B`. Consequently a block of length `N` contains at least

`floor(N/(B+1))+1`

pairwise distinct quotient values at the sampled positions `0,B+1,2(B+1),...`.

If the RL73 giant macro and the exact first-Farey branch occur in the same hypothetical object, then `N` is at least its inherited aligned-zero count

`Z=40,249,491,324,522,944`,

so the macro contains at least

`boxed: 930,959}`

spaced-distinct quotient states.

This is not yet a contradiction. It is the first quantitative periodic/aperiodic bridge produced by the RL84 scale cap:

- long closed returns are uniformly bounded;
- the surviving alternative must exhibit explicit quotient-state complexity.

The missing consumer is still a global ownership-sensitive packing theorem that turns that complexity into an impossible physical/state-weight budget.

---

## 1. Incoming authority and verification economy

Authoritative incoming state:

- RL84 outer sidecar: PASS in the current session;
- RL84 internal manifest: PASS;
- inherited RL83 sidecar check: PASS;
- RL84 fast verifier: PASS.

The frozen RL84 ledger is therefore accepted under the verification-economy rule. No historical expensive certificate was recursively replayed.

Retain unchanged:

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

The inherited external cycle-minimum floor `R>=2^71` remains an **external computational input**, not an analytic theorem of RL85.

---

## 2. Historical RL# hypothesis audit

### 2.1 Exact historical object

The early R# programme defined

`R# = least positive integer in R`,

where `R` is the full hypothetical set of nonconvergent/red integers, including both loop (`RL`) and unbounded/nonperiodic (`RO`) possibilities.

Therefore, if a nontrivial cycle exists, historical `R#` exists, but it need not lie on that particular cycle unless no smaller red feeder or other red orbit exists.

The historical minimality consequences include

- `T^k(R#)>=R#` for every `k>=0`;
- `R#` is odd;
- `R# != 2 (mod3)`;
- every legal inverse predecessor of a red node is red, and any red predecessor below `R#` contradicts global minimality.

These are load-bearing global-minimality hypotheses. They may not be relabelled onto an arbitrary red feeder.

### 2.2 Immediate roof objects fail the historical minimality hypotheses

Use RL84/RL82 notation

`M=max C`,

`F=2M`,

`P=(2M-1)/3`.

Then:

1. `F` is even, so `F!=R#`.
2. `M` is even, so `M!=R#`.
3. RL82's three surviving maximum residue classes are
   `M == 26,80,152 (mod162)`, and every corresponding top grammar begins with `OO`.
   Hence the immediate predecessor `P` admits an odd inverse and
   `P==2 (mod3)`.
   More explicitly
   `P == 17,53,101 (mod108)`.
   Therefore `P!=R#`.

This is a new exact **historical-hypothesis mismatch theorem** for the canonical roof fork.

### 2.3 The ordinary `+1` relation is genuine but not an `r=1` corridor

The sibling relation

`F=3P+1=2M`

is non-homogeneous and ordinary-`+1` specific. However

`nu_2(3P+1)=1+nu_2(M)>=2`

because `M` is even.

Therefore the roof edge is not one of the historical pure accelerated `r=1` transitions. The q=24 leak/proliferation certificate and the long pure-`r=1` corridor machinery cannot be transplanted to `P->M` merely because `F=3P+1`.

### 2.4 What does transfer

The following survive without historical least-red minimality:

- local inverse/preimage algebra;
- red inheritance under legal inverse predecessors;
- exact 3-adic sibling recurrence `y_(i+1)=4y_i+1` inside the old inverse-tree machinery;
- the complete-residue odometer fact for sibling families.

But the odometer is **residue-complete** through increasing ternary depth. It does not force a positive normalized cylinder height and therefore supplies no lower bound competitive with RL84's exponentially tiny first-Farey upper height.

### 2.5 What does not transfer

The following remain restricted to historical `R#` / RO hypotheses:

- no-red-node-below-the-barrier arguments;
- record-scale trapped inverse-closure leakage below `R#`;
- the pure `r=1` lower-barrier corridor as a minimality contradiction engine;
- positive-density conclusions from an injective infinite RO trajectory with bounded discrepancy.

`F=2M` is preperiodic into a finite loop, not an injective infinite RO orbit.

### Historical transplant verdict

**Direct RL# -> roof-feeder transplant is frozen negative.**

The only surviving information is generic inverse algebra and residue completeness. No historical least-root theorem gives a new non-dyadic lower-height constraint on `F`, `M`, or `P`.

---

## 3. First-Farey physical maximum theorem

Use the RL84 exact first pair

`p=114,208,327,604`,

`q=72,057,431,991`,

`e=p-q`,

`D=2^p-3^q`,

and the exact inherited finite certificate

`Delta=p log2-q log3 > 1/200,000,000,000`.

RL84 proved

`M < 2^e 3^q / D`.

Also

`D/2^e = 2^q(1-exp(-Delta)) > 2^(q-1) Delta`.

Therefore

`D/2^e > 2^(q-1)/200,000,000,000`

and hence

`boxed: M < 400,000,000,000 (3/2)^q.}`

Classification: **analytic consequence + inherited exact finite logarithm certificate**.

### 3.1 The actual maximum is the least cylinder representative

RL84's word cylinder has modulus `2*3^q`. Since `q` is enormous and already `2^39>200,000,000,000`,

`400,000,000,000 (3/2)^q < 2*3^q`.

Thus

`0<M<2*3^q`.

If `m_w` is the least positive even representative of the maximum word cylinder, then `M==m_w (mod 2*3^q)` and both are positive below one modulus. Therefore

`boxed: M=m_w.}`

Classification: **new analytic theorem**.

This upgrades RL84's statement about the least representative into a statement about the physical cycle maximum itself.

### 3.2 Strong ternary-height compression

Set

`h=ceil(3q/8)=27,021,536,997`.

Then

`q-h=floor(5q/8)=45,035,894,994`.

Write `q=8a+r`, `0<=r<8`. Since

`2^q/3^(q-h)
 = (256/243)^a * 2^r/3^floor(5r/8)`

and the finite remainder factor is at least `1` for every `r=0,...,7`, it is enough to compare `(256/243)^a` with `400,000,000,000`.

The RL85 exact verifier checks

`256^513 > 400,000,000,000 * 243^513`,

while `a=floor(q/8)>>513`.

Hence

`2^q/3^(q-h) > 400,000,000,000`,

which is equivalent to

`400,000,000,000(3/2)^q < 3^h`.

Therefore

`boxed: M < 3^27,021,536,997.}`

Classification: **analytic theorem + exact finite rational threshold certificate**.

### 3.3 Ternary leading-zero corollary

Because `M<3^h<3^q`, the zero-padded `q`-digit ternary representation of the actual cylinder representative `M` has at least

`boxed: 45,035,894,994}`

leading zero digits.

This is an exact structural consequence of the first-Farey survivor, not a numerical search over the word.

---

## 4. Uniform synchronized-return span in the first-Farey/full-phase intersection

This section deliberately reconnects the RL84 maximum branch to the RL75/RL76 hybrid route.

Assume a hypothetical genuine full-phase object has an RL64/RL76 paired physical height-one segment and also lies in the exact first-Farey maximum branch above.

Let a nonempty synchronized word `c` of length `n` take an odd height-one quotient state `J` back to itself. Let `A_0,B_0` be the two genuine physical cycle states at its entry.

RL76 gives, for one occurrence of the closed word,

`alpha=(J-1)/2`,

`A_0=alpha+2^n m`,

`B_0=alpha+3*2^n m`.

For a nonempty proper segment of a primitive cycle, `m!=0`; `m=0` is physical pump closure and is excluded by RL75 primitivity.

Subtracting gives

`boxed: B_0-A_0=2^(n+1)m.}`

Since both physical states lie in the same cycle interval `[R,M]`,

`|B_0-A_0|<=M-R`.

Thus

`boxed: 2^(n+1)<=M-R.}`

Classification: **analytic synthesis of RL75/RL76 with genuine maximum ownership**.

### 4.1 First-Farey numerical span bound

From `M<3^h` and the exact elementary inequality

`3^5<2^8`,

we get

`2^(n+1)<3^h<2^(8h/5)`.

Hence

`n+1<8h/5`.

With `h=27,021,536,997`, the exact integer consequence is

`boxed: n<=43,234,459,194.}`

Classification: **analytic theorem + exact integer arithmetic**.

### Interpretation

RL76's central barrier said a closed pump can hide arbitrarily large repeat depth by paying with an arbitrarily large physical state scale. In the exact first-Farey maximum branch, that free scale is gone: the genuine cycle maximum caps every physical paired state, uniformly over the surrounding full-phase context.

This is the first theorem in the project that directly consumes RL84's cylinder height to repair the specific RL76 physical-scale obstruction.

---

## 5. Canonical pump corollaries

### 5.1 Positive pump `c=10`

A run of `r` copies has total closed quotient span `n=2r`, so Theorem 4.1 gives

`boxed: r<=21,617,229,597.}`

This agrees with the direct RL76 normal form

`A_0=1+4^r m`,

`B_0=1+3*4^r m`.

### 5.2 Negative pump `c=101`

The general span theorem gives `3r<=43,234,459,194`, hence

`r<=14,411,486,398`.

RL76's exit states sharpen this. At the end of `r` copies,

`A_r=-7+9^r m`,

`B_r=-7+3*9^r m`,

so

`|B_r-A_r|=2*9^r|m|<=M-R<3^h`.

Therefore `2r<h`, giving

`boxed: r<=13,510,768,498.}`

Classification: **analytic corollary**.

### 5.3 RL74 stress-family consequence

RL74's canonical shrink/growth family relied on letting the `101` and `10` pump depths grow without a physical upper scale. At the exact first-Farey physical maximum, both depths are now uniformly finite.

This does not close arbitrary periodic structure, but it removes the **unbounded-scale** version of that stress test in this branch.

---

## 6. Quantitative periodic/aperiodic consequence for a giant macro

Let

`B=43,234,459,194`.

Consider one synchronized height-one block with quotient states

`J_0,J_1,...,J_N`.

If `J_i=J_j` for `0<=i<j<=N`, the intervening synchronized word closes `J_i`. If it is a proper segment of the primitive full-phase cycle, Theorem 4.1 gives

`j-i<=B`.

Therefore the sampled states

`J_0, J_(B+1), J_(2(B+1)), ...`

are pairwise distinct.

Hence

`boxed: #distinct sampled J >= floor(N/(B+1))+1.}`

Classification: **new analytic packing consequence**.

### 6.1 RL73 intersection

For a hypothetical odd `27<=k<=165` Gate-A violation, RL73 guarantees a maximal post-first-mismatch height-one block with at least

`Z=40,249,491,324,522,944`

aligned `00` columns. Its total synchronized length satisfies `N>=Z`.

If that same hypothetical object lies in the exact first-Farey maximum branch, then

`floor(Z/(B+1))+1 = 930,959`.

Thus

`boxed: the giant macro contains at least 930,959 spaced-distinct quotient states.}`

This is **not** a closure theorem. RL81 already warns that quotient-state information does not automatically become a basin theorem for either physical coordinate, and the current global packing ledger has no upper budget excluding 930,959 such quotient values.

### What has been achieved

The periodic/aperiodic hybrid is now quantitative in this branch:

- any single proper quotient return has span at most `B`;
- a giant macro necessarily exposes at least 930,959 spaced-distinct quotient values;
- the remaining missing theorem is a physical/full-`D` consumer for those distinct quotient states or their paired physical coordinates.

---

## 7. Extremal low/high arc versus RL20

RL84 Branch L supplies an owned extremal arc `R->M` with raw factor `u<1` and a complementary owned arc `M->R` with raw factor `v>3/2`.

RL85 checked the exact historical interfaces rather than relabelling this arc.

### 7.1 Balanced-return branch: no hypothesis match

RL20 balanced return is defined at canonical gcd-block cuts for

`A=ga`, `L=g ell`,

with a proper canonical cut satisfying exact imbalance

`E_j=K_j-j ell=0`.

An extremal endpoint `M` supplies neither

- that its phase index is a multiple of the reduced block length `a`, nor
- that the odd count on the extremal arc is exactly `j ell`.

The condition `u<1` is a strict slope inequality, not exact zero imbalance.

Therefore the extremal low arc is **not** an RL20 balanced-return block by current hypotheses.

### 7.2 Strict-excursion branch: no implication

RL20 strict excursion requires every proper canonical block boundary to have `E_j>=1`. The extremal condition `u<1` concerns one physical arc between extrema and does not determine the canonical gcd-block excursion path.

No implication in either direction is available.

### 7.3 Hard-root / second-low plateau: no automatic plateau ownership

RL20's second-low theorem is formulated in the compressed plateau factorization. RL84's extremal arc may cut across that decomposition. Without a proof that `R` and `M` align with the relevant plateau boundaries, the composite low factor `u<1` cannot be promoted to the specific second-low plateau required by that theorem.

### 7.4 Arbitrary-rotation weighted difference: exact match, no contradiction

RL19/RL20's arbitrary-rotation identity does apply exactly to the two genuine rotations at `R` and `M`:

`sum_i q_i(3^(-G_i)-1)
 = 4(lambda-1)(M-R)`.

This is a legitimate full-ownership consumer. But its right-hand side is the positive physical height difference itself, so the identity supplies a sign/height law rather than a contradiction.

### RL20 verdict

The extremal arc is a useful owned object, but no existing balanced-return, strict-excursion, or second-low theorem consumes it without an additional boundary-alignment lemma.

---

## 8. Opposite prefix rotations

RL84 established:

- every nonzero backward prefix from the genuine minimum `R` is raw-surplus;
- the maximum-rooted backward rotation has an enormous initial raw non-surplus interval under the inherited floor.

The corrected prefix quantity is

`Delta_i-S_i = log(x_i/anchor)`.

Thus:

- at the minimum rotation it is positive at every proper prefix because `x_i>R`;
- at the maximum rotation it is negative at every proper prefix because `x_i<M`.

This opposite corrected sign pattern is exact, but it is also the direct logarithmic expression of extremal ordering.

At the raw-word level, cycle-lemma/mechanical-word phenomena can support rotations with very different initial partial-sum behavior. The pure cyclic-word comparison therefore does not force a contradiction. The ordinary `+1` correction is load-bearing, but after it is restored the sign is exactly the known physical height relative to the chosen extremum.

**Route status:** useful structural description, but no new consumer. Do not launch a generic Christoffel/residue ladder without a new physical term.

---

## 9. First-Farey lower-height consumer search

RL85 tested the historical entry-side machinery against the new physical maximum cap.

No inherited theorem provides the desired lower bound

`legal first-surplus word => cylinder height >= H(q)`

at the scale needed to exceed RL84's upper height.

Reasons:

1. historical least-red minimality does not apply to `F`, `M`, or `P`;
2. doubling `M->2M` preserves normalized 3-adic cylinder height exactly;
3. the seed-independent sibling odometer is residue-complete, so it does not forbid small cylinder representatives;
4. the maximum top grammar constrains low-order ternary/residue data but does not produce a positive normalized height of order `2^-q`;
5. full-`D` ownership still attaches to on-cycle rotations, not directly to the external feeder.

**Status:** no lower-height theorem found. This remains open rather than falsified.

---

## 10. Branch H

Retain RL84 Branch H exactly:

- `d>=114,208,327,604`;
- reduced local denominator `>=72,057,431,991`;
- `L>=2,872,132,254,754,669,047,880` under inherited `R>=2^71`;
- `v>3/2`.

Because a primitive cycle has at most `M` distinct positive phase states below its maximum, `L<=A<=M`. Thus Branch H also gives the simple physical lower bound

`M>=2,872,132,254,754,669,047,880`.

This is still astronomically below the first-Farey upper cap `3^h` and yields no contradiction.

Further RL19/RL20 packing manipulations only inflate length/size lower bounds with the current inputs. RL85 therefore freezes Branch H as a **method barrier** until a genuinely upper physical/state budget appears.

---

## 11. Proof-state ledger additions

### New proved analytic mathematics

1. Immediate roof historical-mismatch theorem: `F`, `M`, and `P` cannot be historical `R#` under the inherited top grammar.
2. Roof edge valuation theorem: `nu_2(3P+1)=1+nu_2(M)>=2`; no pure-`r=1` roof corridor.
3. Exact first-Farey physical upper bound
   `M<400,000,000,000(3/2)^q`.
4. At the exact first pair, the physical maximum equals the least positive even maximum-cylinder representative.
5. Strong ternary-height theorem
   `M<3^27,021,536,997`.
6. At least `45,035,894,994` leading zero ternary digits in the zero-padded `q`-digit representative.
7. General proper synchronized quotient-return divisibility
   `2^(n+1)<=|B_0-A_0|<=M-R` in the genuine paired full-phase setting.
8. First-Farey return-span bound
   `n<=43,234,459,194`.
9. Canonical pump bounds for `10` and `101`.
10. Spaced-distinct quotient packing lower bound, with `930,959` states on the RL73 giant-macro / first-Farey intersection.
11. Branch-H physical lower bound `M>=L` specialized to the inherited huge `L` bound.

### New exact finite certificates / arithmetic checks

The RL85 fast verifier checks:

- `h=27,021,536,997` and the exact leading-zero count;
- the rational threshold
  `256^513 > 400,000,000,000*243^513`;
- all eight remainder factors needed for the `3q/8` exponent comparison;
- exact return-span and canonical-pump integer bounds;
- exact `930,959` distinct-state count;
- transformation of RL82 maximum residue classes to `P ==17,53,101 (mod108)` and hence `P==2 mod3`.

These are finite arithmetic/transcription guards. The analytic proofs are in this note.

### Externally inherited input

- `R>=2^71`: inherited external computational cycle-minimum floor.
- RL83/RL84 rigorous first-Farey logarithm interval / defect lower bound.

### Computational evidence

No new bounded Collatz search is promoted in RL85.

### New barriers / dead subroutes

- direct historical least-red/corridor transplant to `F=2M`, `M`, or `P`: dead under current hypotheses;
- historical sibling odometer as a cylinder-height lower bound: dead (it is residue-complete);
- extremal low arc => RL20 balanced return / strict excursion / compressed plateau: not established; current direct transplant rejected;
- raw opposite-prefix/cycle-lemma comparison: insufficient without a new physical consumer;
- Branch H packing by further length inflation: deprioritized.

### Corrections / demotions

No inherited RL84 theorem is demoted.

One notation normalization is frozen for the next target: the roof predecessor is

`P=(2M-1)/3`,

consistent with `F=3P+1=2M`. Any typography resembling `32M-1` is to be read as the fraction `(2M-1)/3`, not as a new formula.

---

## 12. Route decision and live obligation

RL85 does **not** justify abandoning the RL♭ work as empty, but it does close the direct historical-RL# transplant route.

The strongest surviving bridge is now very specific:

> **First-Farey physical-scale -> bounded synchronized-return span -> aperiodic quotient-complexity consumer.**

The periodic side of the RL75/RL76 scale obstruction is materially repaired in the exact first-Farey branch. The missing theorem is the aperiodic/global consumer:

> turn bounded quotient return span (or the resulting spaced-distinct quotient values) into an ownership-sensitive physical/full-`D` packing contradiction, or prove that no such consumer exists.

Per the user-requested strategy, RL86 will first interrogate the distinct roof-feeder ray `RL↑`. If that route is neutral, this RL85 obligation is the primary fallback.

Global closure status remains unchanged.
