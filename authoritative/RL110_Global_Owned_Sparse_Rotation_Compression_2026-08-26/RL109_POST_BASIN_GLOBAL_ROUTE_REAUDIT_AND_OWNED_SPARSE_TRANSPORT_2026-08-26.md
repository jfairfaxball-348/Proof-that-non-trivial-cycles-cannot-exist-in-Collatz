# RL109 — post-basin global route re-audit and owned sparse-rotation transport

Date: 2026-08-26

## 0. Executive outcome

RL109 executed the requested post-basin global route re-audit after RL100–RL108.

**No Gate A closure, Gate B closure, RL/nontrivial-cycle exclusion, or Collatz proof is claimed.**

The audit changes the programme ranking. The strongest next route is no longer another local basin equality, another first-Farey refinement, or another raw cascade extension. The highest-ranked live edge is now a **global ordinary-`+1`, full-`D` owned sparse-rotation compression theorem**.

The audit also produces a concrete analytic synthesis supporting that ranking.

For a primitive ordinary shortcut-cycle word `w` of length `A`, weight `L`, and

`D = 2^A - 3^L > 0`,

let `Q(r)` be the ordinary unit-increment affine numerator of a cyclic rotation `r` of `w`. Every owned rotation starts at an actual integer cycle state `x_r`, so

`Q(r) = D x_r`.

Hence for two distinct owned rotations `u,v`,

`Q(v)-Q(u) = D(x_v-x_u)`

is a **nonzero multiple of `D`**.

Under a fixed linear cut, one adjacent `10 -> 01` transposition at positions `i,i+1`, with `t` ones to its right, changes the unit numerator by exactly

`+ 2^i 3^t`,

and the reverse swap changes it by the negative of that monomial. Therefore an `R`-swap path gives an `R`-term signed sparse representation of the owned numerator difference.

The remaining cyclic-cut issue is automatic at the closest owned pair. For every nonconstant binary word,

`dist_cyc(w, rot_1(w)) = min(L,A-L) < A`.

Thus the minimum cyclic rotation radius `R_*` satisfies `R_*<A`. Any integer minimizing cyclic transport flow of total cost `R_*<A` has a zero edge. Cutting at such an edge converts the cyclic minimum into an ordinary linear transposition path of the same length. Consequently every hypothetical primitive ordinary cycle produces a **nonzero signed `R_*`-term sparse multiple of `D`**.

This is not yet a contradiction. Its value is that it identifies, in one exact interface, the two ingredients that previous routes kept separating:

1. **global ordinary ownership:** `D | Q(r)` for every actual rotation;
2. **small-radius sparse geometry:** a short transposition path makes `Q(v)-Q(u)` a short signed sum of `2^a3^b` monomials.

The already-closed radius-3 engine is the extreme `R_*<=3` consumer. On the complementary `R_*>=4` branch, a proof that some such nonzero sparse transport satisfies `|Q(v)-Q(u)|<D` would be an immediate direct contradiction.

RL109 therefore assigns RL110 to the **radius-3-complement sparse-multiple compression theorem** rather than to another local word/basin or Farey calculation.

---

## 1. Incoming authority and verification

The user-supplied RL109 handover was accepted as the direct current instruction over the one-session-lagging GitHub `authoritative/` state.

Incoming bundle:

`RL109_Post_Basin_Global_Route_Reaudit_2026-08-26.zip`

SHA-256:

`6abd08b093ea63b6ad7ea35032485500a1ad5169565437215c655b9617989bc7`.

The outer sidecar, fresh internal manifest, both direct RL108 verifiers, and `run_fast_rl108_verifiers.sh` all pass. The frozen RL108 census remains:

- balanced first-surplus words checked: `3,066,528`;
- capped least-cylinder realizations: `6`;
- nontrivial capped words: `5`;
- common nontrivial capped maximum: `M=890`;
- `kappa_17(890)=34,572,879`.

No stop-and-repair condition was triggered by the incoming mathematics.

GitHub was one completed transaction behind the user-supplied handover: repository HEAD still carried the RL107->RL108 authoritative state. Under the repository conveyor protocol, RL108 and RL109 are therefore to be promoted as two separate atomic transactions, not collapsed into one commit.

---

## 2. Frozen global closure tree after RL108

Retain the following proof-state classifications exactly.

```text
Inherited primitive/full-D cycle architecture
|
+-- radius <=3 primitive/full-D owned contradiction regime ---- CLOSED LOCAL ENGINE
|      |
|      +-- global theorem forcing an owned small-radius pair --- OPEN
|
+-- Gate A ------------------------------------------------------ OPEN GLOBALLY
|      |
|      +-- even terminal k ------------------------------------- CLOSED ANALYTIC
|      +-- terminal k <=25 ------------------------------------- CLOSED EXACT-CERT COROLLARY
|      +-- odd terminal k >=27 -------------------------------- OPEN GLOBALLY
|             |
|             +-- exact first-Farey/raw-g=1 branch ------------ STRONGLY SIEVED, RESTRICTED
|             +-- raw multiplicity g>1 ------------------------- OPEN
|             +-- distinct larger Farey slopes ---------------- OPEN
|
+-- Gate B ------------------------------------------------------ OPEN GLOBALLY
|      |
|      +-- local grammar -> radius <=3 ------------------------- DEAD (RL20 fake)
|      +-- normalized/raw coboundary transport ---------------- RETIRED ALONE
|      +-- D|Q-sensitive ordinary-owned transport ------------- REOPENED / RANK 1
|
+-- direct ordinary +1 full-phase bypass ----------------------- OPEN
       |
       +-- raw basin saturation ------------------------------- DEAD
       +-- local dyadic/LTE equality -------------------------- FROZEN AFTER RL108
       +-- affine/prime-prefix/roof-content variants ---------- FROZEN RL102-RL105
       +-- new global unscaled integer-content route ---------- OPEN VIA RANK 1
```

The exact first-Farey/raw-`g=1` numerical cascade remains frozen at the RL100 checkpoint:

- wide `(D_w,R_w)=(5,000,030,7,000,000)`;
- middle `(D_m,R_m)=(7,500,031,4,500,000)`;
- deep `(D_d,R_d)=(10,000,032,3,250,000)`;
- ultra `(D_u,R_u)=(15,000,035,2,005,000)`;
- `L_common=15,000,053`;
- active support `lambda=234375/3281264468752`, `mu=1/7000001`;
- `floor(lambda*C)=3010`;
- first live odd raw-`g=1` branch terminal `k=2,921,813,805`;
- branch upper endpoint `42,150,931,559`.

No RL109 result globalizes that branch.

---

## 3. What RL100–RL108 changed relative to RL99

### 3.1 Gate-A/Farey scope became harder, not easier

RL100 repaired a major scope shorthand. A reduced first-surplus slope `(p,q)` does not determine raw counts: the raw pair is `(gp,gq)`. At the first reduced Farey pair, the inherited Beatty condition allows

`1 <= g <= 125,777,718,029`.

The natural absolute RL82 maximum envelope `U_(p,q)(g)` is strictly increasing in `g`. Therefore the raw-`g=1` branch is not a proved worst-case representative of larger multiplicities.

RL100 also proved the next reduced-denominator floor for distinct slopes, but the complementary slope family remains infinite.

### 3.2 RL101 produced real multiplicity structure but no global consumer

RL101 proved:

- exponentially decreasing normalized cylinder height with `g`;
- physical maximum equals the least positive even full-cylinder representative;
- every internal primitive boundary has excess odd count;
- a proper balanced sliding primitive window exists;
- for `g>=2`, an actual physical state occurs below `M/2`;
- in the equal-slope near-resonant branch, a two-sided owned excursion runs from above `15M/16` to below `M/2`.

These are strong physical statements. But they do not consume full-cycle `D|Q`, and the absolute maximum scale still grows with multiplicity. No multiplicity exclusion followed.

### 3.3 RL102–RL105 exhausted the obvious numerator-content splices

The subsequent sessions recovered exact prefix/suffix and rotation transport, tested direct affine-cylinder content, direct prime-prefix unit-increment content, and a roof factor-5 relation. Those identities were exact but did not escape rotation transport/coboundary or generalized-increment scaling without an additional global consumer.

RL109 therefore does not classify the bare identity `Q(v)-Q(u)` as new. The new point is the **combined selection of an owned closest pair, a zero-flow cut, and the ordinary unscaled full-`D` divisibility as one theorem interface**.

### 3.4 RL106–RL108 close the current basin-equality branch

RL106 excluded sufficiently long aligned all-even block runs but did not create a basin equality. RL107 classified odd-core collisions exactly and showed the resulting distinct-core population is only constant. RL108 then proved:

- proper-prefix extremality is automatic before first surplus;
- LTE roof equality has rigid depth and reduces to the dyadic maximum;
- the discrete-log word address classifies dyadicity but does not force it;
- an exact bounded census contains five non-dyadic capped local words at `M=890`.

Thus deeper local word arithmetic does not presently force the needed physical basin equality. The direct word-to-basin route is frozen unless a genuinely new global consumer appears.

---

## 4. New analytic synthesis: owned sparse-rotation transport

### 4.1 Unit-increment word numerator

Let `w=d_0...d_(A-1)` be a binary shortcut word, where `d_i=1` denotes an odd shortcut step and `d_i=0` an even step. Let `L=sum d_i`.

For the generalized odd increment `s`, define

`T_s(x)=x/2` on even `x`,

`T_s(x)=(3x+s)/2` on odd `x`.

After applying the word,

`T_{s,w}(x) = (3^L x + Q_s(w))/2^A`,

where

`Q_s(w) = s Q_1(w)`

and

`Q_1(w) = sum_(i:d_i=1) 2^i 3^(# ones strictly after i)`.

The scaling `Q_s=sQ_1` is exact.

### 4.2 Single-swap formula

Suppose a rooted word has `10` at positions `i,i+1`, and there are `t` ones strictly to the right of the pair. Let `w'` be obtained by changing this local pattern to `01`.

All contributions to `Q_1` except the moved odd symbol are unchanged. Hence

`Q_1(w') - Q_1(w) = 2^(i+1)3^t - 2^i3^t`

`= 2^i 3^t`.                                                (4.1)

The reverse transposition contributes `-2^i3^t`.

Therefore any fixed-cut adjacent-transposition path of length `R` from `u` to `v` gives

`Q_1(v)-Q_1(u) = sum_(j=1)^R epsilon_j 2^(a_j)3^(b_j)`,     (4.2)

with `epsilon_j in {+1,-1}`.

Classification: **analytic identity; constituent transport algebra is historical, reassembled here as the live global interface**.

### 4.3 One-step rotation-radius identity

Let `rot_1(w)` be the left cyclic shift by one place. For equal-weight binary words, the exact cyclic adjacent-transposition distance is the minimum `L1` norm of an integer edge flow.

For `w` and `rot_1(w)`, the cumulative discrepancy through position `i` telescopes to

`S_i = d_0 - d_(i+1)`.

If `d_0=0`, choosing zero circulation gives one unit of flow exactly at the `L` positions whose shifted symbol is `1`, hence cost `L`; shifting the circulation by `+1` gives cost `A-L`. If `d_0=1`, the two costs are reversed. Therefore

### Lemma RL109.1 — one-step rotation radius

For every nonconstant binary word,

`boxed: dist_cyc(w,rot_1(w)) = min(L,A-L).}`                (4.3)

In particular,

`dist_cyc(w,rot_1(w)) < A`.

Classification: **analytic lemma**.

### 4.4 Zero-flow cut for every closest pair

Let `R_*` be the minimum cyclic adjacent-transposition distance between two distinct rotations of a primitive word.

By Lemma RL109.1,

`R_* <= min(L,A-L) < A`.                                    (4.4)

An integer minimizing cyclic flow `f_0,...,f_(A-1)` has

`sum_i |f_i| = R_*`.

If every edge had nonzero integer flow, then every `|f_i|>=1`, giving total at least `A`, contrary to (4.4). Thus at least one minimizing-flow edge has `f_i=0`.

Cut the cyclic word at that edge. The same minimizing transport is now a linear adjacent-transposition path of length `R_*` and does not cross the cut.

### Lemma RL109.2 — closest-pair sparse cut

Every primitive nonconstant binary word has a closest pair of distinct rotations for which a common cyclic cut converts a minimum cyclic path into a fixed-cut linear path of exactly `R_*` adjacent swaps. Consequently (4.2) applies with exactly `R_*` signed monomials.

Classification: **analytic lemma**.

### 4.5 Full ordinary ownership turns the sparse transport into a nonzero `D`-multiple

Now assume `w` is the primitive parity word of a hypothetical positive ordinary shortcut cycle. For every cyclic rotation `r`, the corresponding actual physical state `x_r` satisfies

`2^A x_r = 3^L x_r + Q_1(r)`.

Thus

`Q_1(r)=D x_r`,                                             (4.5)

where `D=2^A-3^L`.

For distinct owned rotations `u,v`, primitivity/simple-cycle ownership gives distinct physical states, so

`Q_1(v)-Q_1(u) = D(x_v-x_u) != 0`.                         (4.6)

Combining Lemma RL109.2 with (4.2):

### Theorem RL109.3 — owned closest-pair sparse full-`D` multiple

Every hypothetical primitive ordinary shortcut cycle has two distinct owned rotations and a zero-flow cut such that

`boxed: 0 != S = sum_(j=1)^(R_*) epsilon_j 2^(a_j)3^(b_j),}`

and

`boxed: D | S,}`                                            (4.7)

where `R_*` is the minimum cyclic rotation radius.

Equivalently `S=D(x_v-x_u)` for two actual physical cycle states.

Classification: **new analytic synthesis/interface theorem from inherited full-cycle ownership plus Lemmas RL109.1–RL109.2**.

This theorem does **not** prove that `R_*<=3` and does **not** prove `|S|<D`. It identifies exactly what remains to be compressed.

---

## 5. Mandatory red teams for Theorem RL109.3

### RL20 fake-model discriminator — PASS

The frozen RL20 length-184, weight-116 local-grammar countermodel has minimum cyclic rotation radius exactly `4`, but its standard ordinary word numerator satisfies

`Q mod D = 322171738410077807581692882247758374512983113782519312 != 0`.

Therefore it fails the owned premise (4.5). RL109.3 does not promote the false local-grammar implication that RL20 killed.

### RL79 generalized-increment discriminator — PASS as a discriminator, not a closure

For generalized increment `s`,

`Q_s=sQ_1`.

Owned generalized cycles only give

`D | s Q_1(r)`

and therefore `D | sS`. The ordinary unscaled conclusion `D|S` follows automatically at `s=1` but cannot be stripped uniformly for arbitrary `s` without an extra coprimality fact.

Thus the live consumer is genuinely ordinary-increment-sensitive. A future proof must retain the **unscaled** divisibility and must not normalize the factor `s` away.

### RL81 physical-vs-quotient discriminator — PASS

Equation (4.5) identifies `Q_1(r)/D` with the actual owned physical cycle state `x_r`. No auxiliary quotient coordinate is treated as a physical state.

### Primitivity — PASS / load-bearing

Primitivity/simple-cycle ownership is used to make distinct selected rotations correspond to distinct states, hence `S!=0`. A periodic repeated word would require separate treatment and is outside the primitive input contract.

### Raw multiplicity/Farey scope — PASS

Theorem RL109.3 is global in the full cycle word and contains no first-Farey reduced-slope or raw-`g` assumption. It does not inherit the RL100 raw-multiplicity scope restriction.

### External-input dependency — PASS

No external least-cycle floor, LMN estimate, first-Farey certificate, or numerical cascade constant is used in Lemmas RL109.1–RL109.3.

### Closure scope — PASS

RL109.3 is an interface theorem only. It does not close Gate A, Gate B, RL, or Collatz. The missing quantitative compression theorem remains open.

---

## 6. Exact finite verifier supporting the audit

`verification/verify_rl109_owned_sparse_transport.py` performs independent exact checks of the elementary identities and the RL20 discriminator:

- `4,097` adjacent `10->01` numerator-change identities through word length 10;
- `12,264` generalized-increment scaling identities;
- `8,513` equal-weight cyclic pairs through length 8 for the `R<A => zero-flow cut` conversion;
- `2,026` nonconstant words through length 10 for `dist_cyc(w,rot_1(w))=min(L,A-L)`;
- the exact RL20 length-184 fake, reproducing minimum cyclic radius `4` and the quoted nonzero `Q mod D`.

The verifier is an **exact finite sanity certificate** for the formulas and red-team witness. The lemmas themselves are analytic and do not depend on the finite bounds.

---

## 7. Ranked global route table after RL109

| Rank | Route class | Exact success condition | Current obstruction | Audit verdict |
|---|---|---|---|---|
| **1** | **C — Gate-B/full-`D` ordinary-owned sparse rotation compression** | For the RL109.3 selected owned pair (or another owned pair), prove either `R<=3` or `0<|S|<D`; more generally derive an impossible full-`D` sparse multiple | Bare equality `S=D(x_v-x_u)` is tautological; a new structural size/packing/valuation bound must constrain the signed monomials without normalizing away ordinary `+1` ownership | **PRIMARY. Reopened with a concrete global interface** |
| **2** | **A — global owned access to the closed radius-3 engine** | Prove every hypothetical primitive/full-`D` object has owned rotations satisfying the inherited small-radius input contract | RL20 proves local least-root/final-return grammar alone can have minimum radius 4. Any proof must use `D|Q`, physical ownership, or an equally global discriminator | **RETAINED, now best viewed as the short-radius success branch of Rank 1** |
| **3** | **B — Gate-A multiplicity/Farey/global branch coverage** | Eliminate all raw `g>1` and larger Farey slopes, prove domination, or reduce complement to a feasible exact finite family | RL100 raw multiplicity range is huge; absolute envelope worsens with `g`; distinct slopes remain infinite; RL101 compression lacks a global `D|Q` consumer; RL102–RL108 did not supply one | **RETAINED BUT DEMOTED** |
| **4** | **D — genuinely new direct full-phase ordinary-`+1` bypass** | Produce a non-homogeneous physical equality, valuation, lattice, or integer-content contradiction that closes without the Gate split | RL103–RL108 froze the obvious affine, prime-prefix, roof, LTE, collision, and discrete-log variants | **OPEN, exploratory only after Rank 1 is red-teamed** |

The numerical cascade is not assigned a live rank. It remains a preserved exact fallback and must not resume unless a structural theorem gives global leverage or a quantitatively new tier/support mechanism.

---

## 8. Retired, retained, and reopened route decisions

### Newly frozen / retired

1. **Direct word-to-basin equality through deeper prefix extremality or alternate LTE depth:** frozen by RL108.
2. **Rebranding least-cylinder ownership as a new RL108 mechanism:** repaired; it is inherited RL101.
3. **Immediate return to Farey enumeration or raw multiplicity tables:** not justified; RL100 already exposed the scope barrier.
4. **Immediate cascade resumption:** not justified; no new structural trigger appears in RL109.

### Retained

1. Closed primitive/full-`D` small-radius engine.
2. Gate-A even-`k` and `k<=25` closures.
3. RL101 physical multiplicity/excursion lemmas as potential future consumers.
4. RL20 strict-excursion/packing idea, but only if coupled to genuine full-`D` ordinary ownership rather than normalized block algebra.
5. The frozen exact raw-`g=1` first-Farey cascade state.

### Reopened / upgraded

**Full-`D`, ordinary-unit, owned rotation transport** is upgraded to the top route, but only in the strengthened RL109.3 form. Bare rotation transport remains frozen; the reopened object is the selected closest-pair sparse multiple together with unscaled ordinary divisibility and physical state ownership.

---

## 9. RL110 theorem target

RL110 should attack the complement of the already-closed small-radius regime directly.

### Target — global owned sparse-rotation compression

Let `w` be the primitive parity word of a hypothetical positive ordinary shortcut Collatz cycle. Let

- `A=|w|`;
- `L=#1(w)`;
- `D=2^A-3^L>0`;
- `R_*` be the minimum cyclic adjacent-transposition distance among distinct rotations;
- `u,v` be an owned closest pair after the zero-flow cut supplied by RL109.2;
- `S=Q_1(v)-Q_1(u)`, written as the `R_*`-term signed sparse transport of RL109.3.

Work under the radius-3-complement hypothesis

`R_* >= 4`.

**Prove a global structural inequality forcing**

`boxed: 0 < |S| < D,}`                                      (9.1)

or an equally strong contradiction to `D|S`.

Because RL109.3 already gives `0!=S` and `D|S`, (9.1) is impossible. If instead the analysis forces `R_*<=3`, hand the object immediately to the inherited closed small-radius engine.

### Required consumers

The RL110 proof must use at least one piece of genuine global information beyond the bare transport identity, preferably a combination of:

- least-root/final-return prefix/suffix order;
- actual physical state ordering `x_u,x_v`;
- full ordinary `D|Q` ownership;
- primitivity;
- RL101 two-sided physical excursion where its hypotheses apply;
- a new strip/packing or valuation bound on the signed monomial support.

### Mandatory failure tests

Reject any candidate argument that:

- also proves the same conclusion for the RL20 `D∤Q` fake;
- normalizes the generalized increment `s` away;
- treats `Q/D` as physical without owned divisibility;
- silently restricts to raw `g=1`/first Farey while claiming global scope;
- imports the external least-cycle floor without recording it;
- merely rewrites `S=D(x_v-x_u)` without bounding either side independently.

### First milestone

Before broad exploration, derive the strongest available **a priori upper bound on the canonical closest-pair sparse sum `|S|/D`** using only globally valid owned data, and identify exactly which coefficient/support statistic prevents that bound from falling below `1`.

That obstruction, if sharp, should determine whether RL111 continues this route or pivots.

---

## 10. Final RL109 proof-state update

### New analytic mathematics / synthesis

- Lemma RL109.1: `dist_cyc(w,rot_1(w))=min(L,A-L)`.
- Lemma RL109.2: every closest rotation pair has `R_*<A` and therefore admits a zero-flow cut realizing the cyclic minimum as a linear adjacent-transposition path.
- Theorem RL109.3: every hypothetical primitive ordinary cycle yields a nonzero `R_*`-term signed sparse multiple of the full denominator `D`, with actual physical-state interpretation.

### New exact finite certificate

- `verify_rl109_owned_sparse_transport.py` passes all bounded identity checks and reproduces the RL20 radius-4 fake discriminator exactly.

### No new closure

- Gate A: open globally.
- Gate B: open globally.
- RL/nontrivial-cycle exclusion: open.
- Collatz conjecture: not proved.

The main advance is a sharper global theorem interface and route ranking, not a closure claim.
