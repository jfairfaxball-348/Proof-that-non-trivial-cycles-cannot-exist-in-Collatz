# RL84 — RL♭ first-Farey cylinder height, RL#/RL♭ extremal ownership comparison, and canonical low/high arc

Date: 2026-08-24

## 0. Executive conclusion

RL84 continued the authoritative RL83 first-Farey-survivor / cylinder-ownership target and added the requested comparison with the earlier RL# / first-number / entry-side viewpoint before any strategic reversion to RL75.

No Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.

The comparison is productive enough that **the RL♭ route should not yet be killed or reverted**.  It yields a new owned extremal bridge and a compressed first-survivor cylinder target:

1. At the cycle **minimum** and **maximum**, inverse-branch ownership is exactly opposite.
2. The maximum has a canonical external feeder tower `2^k M`, tied to the owned maximum with no 3-adic freedom.
3. Every backward prefix from the true cycle minimum is multiplicatively surplus, while RL83 forces more than 114 billion initial backward layers from the maximum to be non-surplus at the inherited floor.
4. Splitting the same cycle at its minimum and maximum gives an exact canonical high/low arc decomposition.  The maximum-to-minimum forward arc has raw factor strictly larger than `M/R > 3/2`.
5. Therefore either the complementary minimum-to-maximum arc is a **canonical owned low-excess block**, or the whole cycle has `lambda>3/2`, forcing
   `L > 3 R log(3/2)`.
   Under inherited `R>=2^71`, this gives the exact integer consequence
   `L >= 2,872,132,254,754,669,047,880`.
6. At the exact RL83 first Farey pair, cylinder plus ceiling plus the fixed-count `B` envelope forces the least positive cylinder representative into an exponentially tiny normalized window.  A conservative exact consequence is that, writing the least even representative as `m=2n`,
   `n < 3^((q+1)/2)`
   although the modulus is `3^q`, with `q=72,057,431,991`.
7. The RL83 red-team maximizer `O^q E^(p-q)` is therefore **excluded at the first Farey pair** once its exact cylinder is combined with the first-surplus ceiling.  RL83's barrier remains correct: balance + count envelope + `mod162` alone did not exclude it; RL84 adds the missing cylinder-height consumer.
8. Doubling from `M` to the canonical feeder `F=2M` preserves the normalized cylinder height exactly.  Thus historical RL# feeder-side lemmas can now be screened for genuinely new information: only constraints that are not dyadically neutral, or that use entry ownership / `+1` / relative size / full-cycle anchoring, can improve the RL84 survivor.

The selected RL85 target is therefore an **RL#/RL♭ comparative ownership bridge**: audit the historical first-number/entry-side lemmas specifically against the forced pair `(F,M)=(2M,M)` and the canonical minimum/maximum arc, before any return to the RL75 hybrid route.

---

## 1. Incoming authority and verification economy

Authoritative incoming bundle:

`RL83_RLflat_Segment_Product_CF_Farey_Frontier_RL84_Cylinder_Global_Slope_2026-08-24.zip`

The supplied RL83 fresh-unpack record states:

- outer sidecar: PASS;
- internal manifest: PASS;
- RL83 fast verifier: PASS.

A local selective recheck confirmed the outer sidecar and internal manifest.  Under the verification-economy rule the frozen RL83 ledger is accepted; no historical expensive certificate is recursively replayed.

Frozen global state remains:

- radius-3 primitive/full-`D`: closed local theorem;
- Gate A even terminal `k`: closed analytically;
- Gate A terminal `k<=25`: closed by inherited exact finite certificate;
- Gate A odd `k>=27`: open;
- Gate A globally: open;
- Gate B globally: open;
- RL/nontrivial-cycle exclusion: open;
- Collatz conjecture: not proved.

---

## 2. Notation hygiene: three objects must not be conflated

Use the ordinary shortcut map

- `T(n)=n/2` for even `n`;
- `T(n)=(3n+1)/2` for odd `n`.

For a hypothetical nontrivial positive cycle `C`, define

- `R = min C` — this is the **current RL83 least-state variable** (written `R#` in RL83/RL20);
- `M = max C = RL♭` — the RL82–RL84 maximum-state object;
- historical `RL#` / “first-number” / entry-side constructions — retain their historical hypotheses exactly.  In particular, where an older RL# object is only an entry/feeder object, do not silently promote it to `R`; where an older theorem assumes a genuine least root, do not silently apply it to an arbitrary feeder.

This distinction is essential.  The comparison below first proves facts about the genuine extrema `R,M`; it then identifies which historical RL# statements could transfer to a forced feeder attached to `M`.

---

## 3. Extremal inverse-ownership inversion

### Theorem 3.1 — the cycle minimum is odd and its on-cycle predecessor is the even inverse

Since `R=min C`, `R` cannot be even: otherwise `T(R)=R/2<R` would be a cycle state below the minimum.

Hence `R` is odd.

Let `P_R` be the preceding state on the cycle.  The even inverse `2R` always exists.  Any odd inverse, when integral, is

`(2R-1)/3 < R` for `R>1`,

so it cannot be a state of a nontrivial cycle having minimum `R`.

Therefore

`boxed: P_R = 2R.`

If the odd inverse of `R` exists, it is necessarily external to the cycle.

Classification: **analytic theorem**.

### Theorem 3.2 — the cycle maximum has the opposite ownership split

RL82 proved that `M` is even and that its preceding cycle state is

`P_M=(2M-1)/3`,

forcing `M==2 (mod3)`.

The competing even inverse is `2M>M`, so it is external.

Thus at the maximum

`boxed: internal inverse = O, external inverse = E,}`

whereas at the minimum

`boxed: internal inverse = E, external odd inverse (if legal) = O.}`

Classification: **analytic theorem + inherited RL82 maximum theorem**.

### Interpretation

This is a genuine structural difference between the low/entry and high/extremal viewpoints, not a naming difference.  The two extrema force opposite branches of the same inverse Collatz fork to be cycle-owned.

---

## 4. Canonical feeder attached to RL♭

### Theorem 4.1 — forced external dyadic feeder tower

For every `k>=1`,

`F_k = 2^k M`

satisfies

`T^k(F_k)=M`.

Because `F_k>M=max C`, none of the `F_k` lies on the cycle.

Hence every hypothetical cycle maximum has the canonical external feeder ray

`... -> 8M -> 4M -> 2M -> M`.

Classification: **analytic theorem**.

### Corollary 4.2 — exact sibling relation at the maximum

Let

`P=(2M-1)/3`, `F=2M`.

Then

`boxed: F=3P+1,}`

and both `P` and `F` map to `M` in one shortcut step, with `P` the owned cycle predecessor and `F` the forced external feeder.

This is the smallest paired object on which an old feeder-side RL# statement and a current full-cycle RL♭ statement could potentially meet.

---

## 5. Exact transfer of the RL82/RL83 word cylinder to the feeder

For a backward word `w` of length `i` from `M`, with `o` odd inverse steps and exact RL82 defect `B_w`,

`x_i=(2^i M-B_w)/3^o`

and the word cylinder is

`M == 2^(-i) B_w (mod 3^o)`,

with evenness selecting one class modulo `2*3^o`.

Let `m_w` be its least positive even representative modulo `2*3^o`.

For the canonical feeder `F=2M`, multiplication by two gives

`boxed: F == 2m_w (mod 4*3^o).}`

Moreover the normalized cylinder height is preserved exactly:

`boxed: (2m_w)/(4*3^o) = m_w/(2*3^o).}`

Classification: **analytic theorem**.

### Strategic consequence

The feeder `F=2M` has **no independent 3-adic address freedom** relative to the maximum.  Therefore:

- an old RL# theorem that only changes a 3-adic address by dyadic scaling is unlikely to add information;
- an old theorem that imposes a genuinely non-dyadic entry condition, physical-size condition, `+1` condition, or ownership condition can now be intersected with the RL♭ cylinder exactly.

This gives a clean audit filter for historical RL# material.

---

## 6. Minimum-side prefix theorem: every backward prefix is surplus

Take any backward prefix of length `i>=1` from the cycle minimum `R`.  Let its endpoint be `z_i`, and let `o_i` be the number of odd forward inputs on the physical segment from `z_i` to `R`.

Exactly as in RL83, write

`Delta_i = i log2-o_i log3`,

`S_i = sum_(odd y in segment) log(1+1/(3y))`.

The segment product identity gives

`log(R/z_i) = -Delta_i + S_i`.

Because `R` is the cycle minimum, `z_i>=R`.  For a proper prefix `z_i>R`, so

`log(R/z_i)<0`.

Therefore

`boxed: Delta_i > S_i >= 0}`

for every proper backward prefix from `R`.

For the full return, `z_A=R` and `Delta_A=S_A>0`.

Hence:

### Theorem 6.1 — all minimum-rooted prefixes are multiplicatively surplus

For every nonzero backward prefix from the genuine cycle minimum,

`boxed: 2^i > 3^(o_i).}`

Classification: **analytic theorem**.

### Contrast with RL♭

RL83 proves, conditional on inherited `R>=2^71`, that every backward prefix from `M` through depth

`114,208,327,603`

is non-surplus.

Thus the same cyclic parity word admits two extremal rotations with radically opposite prefix behavior:

- minimum-rooted rotation: **every** nonzero prefix is surplus;
- maximum-rooted rotation: the first **114,208,327,603** prefixes are forced non-surplus at the inherited floor.

This is a new comparative object and should be treated as a possible global consumer, not as two unrelated local facts.

---

## 7. Exact minimum/maximum arc factorization

Let `d` be the backward distance from `M` to `R`; equivalently it is the forward length of the physical arc

`R -> ... -> M`.

Let that arc contain `o` odd forward inputs.  The complementary forward arc

`M -> ... -> R`

has length `A-d` and odd count `L-o`.

Define the raw count factors

`u = 2^d/3^o`,

`v = 2^(A-d)/3^(L-o)`.

Then the full-cycle raw factor is

`lambda=2^A/3^L = uv`.

Let `S_RM`, `S_MR` be the odd-step `+1` logarithmic sums on the two physical arcs, and put

`H=log(M/R)>0`.

The two segment product identities give exactly

`boxed: log u = S_RM - H,}`

`boxed: log v = S_MR + H.}`

The `H` terms cancel in the full cycle:

`log lambda = S_RM+S_MR`.

Classification: **analytic theorem**.

### Theorem 7.1 — the maximum-to-minimum arc is canonically high

Since `R` is odd,

`T(R)=(3R+1)/2`

is a cycle state and therefore at most `M`.  Hence

`M/R >= (3R+1)/(2R) > 3/2`.

Since `S_MR>=0`,

`boxed: v = exp(S_MR) M/R > 3/2.}`

Thus the `M -> R` arc is an **owned, canonical high-excess block** with raw multiplicative factor greater than `3/2`.

Classification: **analytic theorem**.

---

## 8. New global dichotomy: canonical low arc or huge odd count

There are two cases for the complementary `R -> M` raw factor `u`.

### Branch L — `u<1`

Then

`2^d<3^o`.

So the physical arc from the actual minimum to the actual maximum is a **canonical owned low-excess block**.  Its complement is the canonical high block from Theorem 7.1.

This is structurally close to the missing object in the older RL20 global programmes: a low/high decomposition whose endpoints are not chosen ad hoc but are the two extrema of the actual cycle.

No claim is made yet that this arc automatically satisfies every RL20 “plateau”, balanced-return, or strict-excursion hypothesis; those interfaces must be checked exactly in RL85.

### Branch H — `u>1`

Then, because `v>3/2`,

`lambda=uv>3/2`.

The uniform odd-step product bound inherited from RL19/RL20/RL83 is

`log lambda <= L/(3R)`.

Therefore

`boxed: L > 3R log(3/2).}`

Conditional on inherited `R>=R0=2^71`, the exact RL84 verifier certifies

`floor(3R0 log(3/2))`

`= 2,872,132,254,754,669,047,879`.

Hence the integer consequence is

`boxed: L >= 2,872,132,254,754,669,047,880.}`

Classification: **analytic theorem + exact finite logarithm certificate + inherited external floor**.

### Additional RL83 consequence in Branch H

If `u>1`, then the depth `d` from the maximum to the minimum is itself a surplus prefix from `M`.  Therefore the RL83 first-surplus theorem implies, under the same inherited floor,

`boxed: d >= 114,208,327,604.}`

After reduction, its odd-count denominator is at least

`72,057,431,991`.

Thus the non-low extremal branch pays both a huge global odd-count cost and the RL83 Farey-prefix cost.

---

## 9. First-Farey cylinder-height compression

Return to the exact RL83 earliest arithmetic pair

`p=114,208,327,604`,

`q=72,057,431,991`,

`e=p-q`,

`D=2^p-3^q>0`,

`Delta=p log2-q log3`.

For any first-surplus word `w` with these counts, RL82 gives the ceiling

`D M <= B_w`.

RL83's fixed-count theorem gives

`B_w <= B_max = 2^e(3^q-2^q) < 2^e 3^q`.

Therefore

`M < 2^e 3^q / D`.

Let `m_w` be the least positive even representative of the word cylinder modulo `2*3^q`.  Any physical `M` in that cylinder satisfies `M>=m_w`, so necessarily

`m_w < 2^e 3^q/D`.

Define the normalized cylinder height

`theta_w = m_w/(2*3^q)`.

Then

`boxed: theta_w < 2^(e-1)/D.}`

Now

`D/2^e = 2^q(1-exp(-Delta)).`

For `0<Delta<1`,

`1-exp(-Delta) > Delta/(1+Delta) > Delta/2`.

Hence

`D/2^e > 2^(q-1) Delta`

and therefore

`boxed: theta_w < 1/(2^q Delta).}`

The exact RL84 verifier, using the inherited RL83 logarithm interval machinery, certifies

`Delta > 1/(200,000,000,000)`.

So every physical word at the first Farey pair must obey

`boxed: theta_w < 200,000,000,000 / 2^q.}`

This is an exponentially tiny fraction of the entire cylinder modulus.

Classification: **analytic theorem + exact finite logarithm certificate**.

---

## 10. Conservative half-height corollary

Because `q=72,057,431,991` is odd, put

`h=(q-1)/2`.

The verifier checks the exact fixed threshold

`2(4/3)^89 > 200,000,000,000`,

and `h>>89`.  Therefore

`200,000,000,000/2^q < 3^(-h)`.

Write the least even cylinder representative as

`m_w=2n_w`.

Then

`m_w/(2*3^q)=n_w/3^q < 3^(-h)`,

so

`boxed: n_w < 3^(q-h)=3^((q+1)/2).}`

Thus a first-Farey physical survivor cannot occupy a generic residue class modulo `3^q`: its least representative has less than roughly half the full ternary height.

This is not yet an exclusion theorem for all words, but it is the requested compressed cylinder/interval consumer.

---

## 11. The RL83 envelope adversary is killed at the first Farey pair

RL83's count-only red team used

`w=O^q E^e`.

It is prefix-balanced before the final crossing, attains the fixed-count `B` maximum, and has exact cylinder

`M == -1 (mod 3^q)`.

The least positive even representative is therefore

`m_w=3^q-1`.

Its normalized height is

`theta_w=(3^q-1)/(2*3^q) > 1/3`.

But Theorem 9 requires

`theta_w < 200,000,000,000/2^q`,

and the latter is already below `1/3` for the present gigantic `q`.

Therefore:

### Theorem 11.1 — first-Farey exclusion of the envelope maximizer

`boxed: O^q E^e cannot be the physical first-surplus word at the RL83 earliest Farey pair.}`

Classification: **analytic theorem + exact first-pair logarithm certificate**.

### Relation to the RL83 barrier

This does **not** correct or demote RL83.  RL83 proved that prefix balance + count envelope + current `mod162` maximum residue alone cannot exclude this family.  RL84 adds precisely the missing information: the *full* word cylinder height together with the physical ceiling.

---

## 12. RL#/RL♭ transplant matrix

The comparison should now be used selectively.

| Historical ingredient | Can it transfer to `F=2M` / `M`? | RL84 judgement |
|---|---|---|
| Local inverse/preimage algebra | Yes | Exact; useful for sibling/entry identities. |
| Pure dyadic-feeder membership | Yes, but neutral | RL80 already proves dyadic/backward saturation is cycle-intersection neutral. Not a contradiction by itself. |
| 3-adic word address | Yes | Transfers bijectively; normalized cylinder height is unchanged by `M -> 2M`. |
| Physical entry-size or `+1` condition | Potentially | Promising, because `F=3P+1=2M` is exact and non-homogeneous. |
| Least-state packing / minimum-state facts | Apply to genuine `R`, not arbitrary `F` | Use in the extremal arc, not by relabeling feeder as minimum. |
| Full-`D`, cyclic rotation, primitive ownership | Apply to `M` / actual cycle only | Do not apply directly to external feeder `F`. Couple through `F=2M` if possible. |
| RL48/RL50 auxiliary `J,N,U,V` facts | No automatic transfer | RL81 physical-lift barrier remains in force. |
| Count-only first-surplus optimization | Already barriered | RL84's new cylinder-height theorem is the needed stronger consumer. |

---

## 13. Connection to older RL20 route architecture

Two older global observations are especially relevant.

1. RL20's hard-root/weak-close work found a “second low block or enormous length” dichotomy and explicitly identified **ownership of the compensating low block** as the useful next question.
2. RL72's global audit later identified the missing common issue as an ownership-sensitive coupling rather than another local residue digit.

RL84 now manufactures a new candidate without choosing a plateau by hand:

- `R -> M` is a canonical extremal arc;
- `M -> R` is canonically high by more than `3/2`;
- either `R -> M` is canonically low, or the cycle pays the huge Branch-H length cost.

The exact hypothesis match to RL20's balanced-return / strict-excursion interfaces is **open**.  This is selected for RL85 rather than assumed.

---

## 14. Route barriers retained

The following remain dead or insufficient alone:

- generic CF extension past the first Farey mediant;
- blind `mod162 -> mod486 -> ...` residue ladders;
- count-only `B` optimization;
- dyadic feeder abundance / blue saturation by itself;
- applying full-cycle divisibility directly to an external feeder;
- identifying RL♭ or the feeder `2M` with RL48 auxiliary coordinates without proof;
- treating the new low extremal arc as an RL20 canonical plateau without checking its exact definition.

---

## 15. Proof-state ledger additions

### New proved analytic mathematics

- minimum inverse-ownership theorem: `R` odd, preceding cycle state `2R`;
- extremal ownership inversion between minimum and maximum;
- canonical external feeder tower `2^k M`;
- exact sibling relation `2M=3((2M-1)/3)+1`;
- exact cylinder transfer `M mod 2*3^o -> 2M mod 4*3^o` with normalized-height invariance;
- every backward prefix from the genuine minimum is surplus;
- exact minimum/maximum arc factorization and logarithmic cancellation;
- canonical `M -> R` raw factor `>M/R>3/2`;
- low-extremal-arc-or-`L>3R log(3/2)` dichotomy;
- first-Farey normalized cylinder-height bound;
- conservative half-height cylinder representative theorem;
- exclusion of `O^qE^e` at the exact first Farey pair.

### New exact finite certificates

- rigorous interval certificate for
  `floor(3*2^71*log(3/2)) = 2,872,132,254,754,669,047,879`;
- rigorous first-Farey defect lower bound
  `Delta > 1/(200,000,000,000)`;
- fixed exact threshold used for the half-height consequence;
- finite sanity audits of extremal predecessor identities and cylinder doubling.

### Externally inherited input used

- `R>=2^71` external computational least-state floor, inherited through RL20/RL72/RL83.

### Computational evidence

No bounded numerical Collatz search is promoted.  The bundled program checks exact rational/logarithmic constants and finite algebra sanity ranges only.

### New method barriers / triage rules

- canonical feeder `2M` adds no independent 3-adic degree of freedom;
- dyadically neutral historical RL# lemmas cannot by themselves exploit the feeder/max pairing;
- the promising historical imports are exactly those using physical entry ownership, non-dyadic `+1`, size, or a full-cycle anchor;
- the extremal low arc must be checked against RL20 definitions before being used as a plateau/excursion.

### Corrections / demotions

None to the frozen RL83 ledger.

RL83's `O^oE^e` method-barrier theorem remains correct at its stated information level.  RL84 adds a stronger consumer and excludes that family only at the first Farey pair under the full cylinder-height/ceiling constraints.

### Global closure status

Unchanged: no Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure is claimed.

---

## 16. Route decision

**Do not pivot back to RL75 yet.**

The user-requested RL#/RL♭ comparison has exposed a genuinely new structural object: the *owned extremal pair of arcs* plus the *canonical maximum feeder with preserved cylinder height*.

One focused RL85 comparison/bridge session is justified before declaring the RL♭ architecture exhausted.

If RL85 shows that:

- old RL# feeder/entry lemmas are all dyadically neutral or require hypotheses unavailable at `F=2M`;
- the canonical low extremal arc does not satisfy any live RL20 balanced-return/strict-excursion consumer;
- the first-Farey small-cylinder-height condition has no independent lower-height/ownership consumer;

then freeze RL♭ cleanly and return to the RL75 hybrid owned-macro periodicity/packing route.
