# RL108 — word-sensitive physical equality classification and ordinary-basin barrier

Date: 2026-08-26

## 0. Executive outcome

RL108 executed the authoritative word-sensitive physical-equality target from the checksum-clean RL107 handover.

**No Gate A, Gate B, RL/nontrivial-cycle exclusion, or Collatz closure is claimed.**

The session does not force an actual first-Farey physical state into the certified ordinary basin. It does, however, close the requested local equality investigation sharply enough to freeze the present basin architecture.

The principal outcomes are:

1. **Provenance repair.** The statement that, for every raw first-Farey multiplicity `g`, the actual maximum equals the least positive even representative of its complete word cylinder is **not new in RL108**. It is already RL101 Corollary RL101.3. The early RL108 checkpoint incorrectly described this as a new extension of RL85; that unpromoted wording is repaired here. No authoritative theorem is demoted.
2. **Proper-prefix extremality collapse.** At a first-surplus word, every proper-prefix maximum inequality is automatic. Only the terminal first-surplus inequality can numerically cut the owned cylinder. Thus exact proper-prefix ordering cannot provide a hidden second representative-selection mechanism.
3. **LTE roof-depth rigidity.** If a physical roof predecessor with exactly `r` consecutive odd steps is an RL80 LTE-comb node `B(j,k)`, deterministic parity forces `j=r`, and the roof endpoint is exactly `2^k`. For the two-odd roof `Q=(4M-5)/9`, every LTE-comb equality therefore reduces to the already isolated dyadic-maximum case.
4. **Exact word-arithmetic classifier.** Because `2` is a primitive root modulo `3^O`, the actual word cylinder has a unique base-2 discrete-log address `kappa(W)`. Under first-crossing geometry, the physical maximum is dyadic exactly when `kappa(W)<=N`. The address lifts one ternary digit at a time from the ordered word. This is genuinely word-sensitive, but it is a classifier, not a basin-forcing theorem.
5. **Fresh gap-free finite census.** RL108 independently enumerated every balanced first-surplus inverse word with odd count `1<=O<=19` (terminal length through `31`): exactly `3,066,528` words. Exactly six have their least even cylinder representative physically capped by the terminal inequality. One is the trivial word `10` with `M=2`; the other five are length `27`, weight `17`, all have `M=890`, and are non-dyadic. No other capped realization occurs in the certified range.
6. **Sharp route barrier.** Prefix balance, exact maximum capping, complete word-cylinder ownership, least-representative collapse, surviving top residue, and even a full ordered word can coexist locally without forcing the representative into the dyadic/LTE basin interface. Existing full-cycle rotation transport and affine-cylinder consumers were already frozen by RL102–RL104. The missing step is therefore a genuinely new global ordinary-ownership theorem, not a deeper local prefix or alternate-LTE calculation.

RL108 therefore freezes the present **direct word-to-basin equality route** and hands RL109 a post-basin global route re-audit.

---

## 1. Incoming authority and verification economy

The incoming RL108 package passed:

- outer SHA-256 sidecar;
- fresh internal `SHA256SUMS.txt`;
- `verify_odd_core_collision_geometry.py`;
- `verify_roof_blue_alignment.py`.

The frozen RL107 state was then accepted under the verification-economy rule. No historical expensive certificate was recursively rerun.

The live target required a genuinely word-sensitive exact physical equality, using actual maximum-rooted first-Farey states and information beyond raw counts, residue compatibility, bare cylinder minimality, CRT matching, quotient proximity, or generalized-increment population estimates.

Frozen global status remains unchanged:

- primitive/full-`D` radius-3 obstruction: **closed local theorem**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A terminal `k<=25`: **closed by inherited exact finite-certificate corollary**;
- Gate A odd terminal `k>=27`: **open globally**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

---

## 2. Provenance repair: least-cylinder ownership was already RL101

At the fixed first-Farey reduced pair

`p=114,208,327,604`,

`q=72,057,431,991`,

the raw first-surplus counts are `(N,O)=(gp,gq)`.

RL101 already proved, uniformly in every admissible raw multiplicity `g`, that the physical maximum lies below one full cylinder modulus and hence equals the least positive even representative of the exact maximum word cylinder modulo

`2*3^O`.

In RL101 notation this is Corollary RL101.3:

`M = m_(W,g)`.

### Correction ledger

The first local RL108 checkpoint called this a new raw-multiplicity extension of the RL85 `g=1` result. That was a provenance error caused by recovering the later RL106 envelope before recovering the full RL101 report.

**Repair:** classify least-cylinder ownership as **inherited RL101 analytic mathematics**, not a new RL108 theorem.

No promoted repository theorem depended on the mistaken checkpoint wording, so no authoritative demotion is required.

---

## 3. Proper-prefix maximum extremality is automatic at first surplus

Let `W` be a first-surplus maximum-rooted inverse word of terminal length `N`. Let `o_i` and `B_i` be the RL82 odd-count and affine-defect coordinates.

RL82 gives the exact physical maximum inequality at every prefix:

`(2^i-3^(o_i)) M <= B_i`.                                  (3.1)

By definition of first surplus,

`2^i <= 3^(o_i)`

for every proper prefix `i<N`, while

`2^N > 3^O`, `O=o_N`.

Also `B_i>=0`.

Therefore for every proper prefix the left coefficient in (3.1) is non-positive and (3.1) is automatic for every positive `M`. Only the terminal inequality

`(2^N-3^O)M <= B_N`                                         (3.2)

has a positive coefficient and can numerically restrict the representative.

### Theorem RL108.1 — proper-prefix extremality collapse

For a first-surplus maximum-rooted word, exact proper-prefix maximum ordering contributes **no additional numerical upper constraint on `M`** beyond legality/integrality. All numerical capping enters at the terminal first-surplus prefix.

Classification: **new analytic synthesis / method barrier**.

### Consequence

RL101's least-representative theorem is not secretly strengthened by many independent proper-prefix caps. Once the word cylinder is fixed, local prefix extremality supplies no second arithmetic selector that could force the representative to be dyadic or another special basin type.

---

## 4. LTE-comb equality is rigid in roof depth

Use the ordinary shortcut map

- even: `T(n)=n/2`;
- odd: `T(n)=(3n+1)/2`.

RL80's LTE comb node `B(j,k)` is an odd integer whose first `j` shortcut steps are odd and whose `j`-th image is the even power `2^k`.

Now let `Q_r` be an actual physical roof predecessor whose path to the even physical maximum `M` consists of exactly `r>=1` consecutive odd shortcut steps.

Suppose

`Q_r = B(j,k)`.

If `j<r`, the common deterministic orbit reaches the even value `2^k` before the physical `r`-odd roof run has ended, impossible. If `j>r`, after `r` steps the comb orbit is still at an odd node, while the physical endpoint `M` is even, impossible.

Hence `j=r`. Determinism then gives

`M=2^k`.

### Theorem RL108.2 — pure-roof LTE depth rigidity

`Q_r=B(j,k)` implies

`j=r` and `M=2^k`.

Conversely, whenever the `r`-odd inverse roof is integral above `M=2^k`, it is exactly the corresponding depth-`r` LTE-comb node.

Classification: **new analytic ordinary-`+1` theorem / route classification**.

For RL107's two-odd roof

`Q=(4M-5)/9`,

an LTE-comb equality is therefore possible only at `j=2`, and then exactly when `M` is dyadic. Trying a shallower or deeper LTE comb cannot broaden the equality interface.

This is ordinary-`+1` specific and passes the RL79 discriminator, but it does not force a dyadic maximum.

---

## 5. A word-sensitive arithmetic-type address

Let a first-surplus word have terminal length `N`, odd count `O`, and actual least even cylinder representative `M`. On the genuine maximum branch `M==2 (mod3)`, so `M` is a unit modulo every `3^r`, `1<=r<=O`.

The elementary LTE identity

`v_3(2^(2*3^t)-1)=t+1`

shows that the multiplicative order of `2` modulo `3^O` is

`2*3^(O-1)`.

Since the unit group modulo `3^O` has that same size, `2` is a primitive root. Therefore there is a unique exponent

`kappa_O(W) in [0,2*3^(O-1))`

such that

`2^kappa_O(W) == M (mod 3^O)`.                              (5.1)

### 5.1 Exact dyadic criterion

First crossing gives

`2^(N-1) <= 3^O < 2^N`,

hence

`2^N < 2*3^O`.                                               (5.2)

If `M=2^k`, then `M<2*3^O` and (5.2) imply `k<=N`; uniqueness in (5.1) gives `k=kappa_O(W)`.

Conversely, if `kappa_O(W)<=N`, then by (5.2)

`2^kappa_O(W) < 2*3^O`.

It is a positive even representative of the same residue class modulo `3^O` as `M`. Because the parity condition selects one class modulo `2*3^O`, and both representatives lie in one full modulus, RL101 least-representative ownership gives

`M=2^kappa_O(W)`.

### Theorem RL108.3 — small discrete-log criterion

For an owned first-surplus maximum word,

`boxed: M is dyadic iff kappa_O(W) <= N.}`

Classification: **new analytic arithmetic classifier using inherited RL101 physical ownership**.

It is not a contradiction theorem: a nontrivial physical cycle maximum is already known not to be dyadic. Thus a genuine survivor must satisfy

`kappa_O(W)>N`.

The value of RL108.3 is that it identifies exactly what a word-to-dyadic theorem would have to prove.

### 5.2 Online Hensel/discrete-log lift

Because `M==2 (mod3)`, start with

`kappa_1=1`.

Given the unique address modulo `3^r`, there is a unique digit `d_r in {0,1,2}` such that

`kappa_(r+1)=kappa_r+d_r*2*3^(r-1)`                         (5.3)

satisfies

`2^kappa_(r+1) == M (mod 3^(r+1))`.

The first `r` odd inverse choices determine the maximum cylinder modulo `3^r`, so (5.3) turns the ordered inverse word into an exact base-3 lift of its arithmetic type. This is genuinely word-sensitive rather than a raw-count invariant.

Finite checks reproduce:

- `M=26 (mod162)` -> `kappa_4=9`;
- `M=80 (mod162)` -> `kappa_4=27`;
- `M=152 (mod162)` -> `kappa_4=51`;
- RL107 local `M=512`, `O=6`: `kappa_6=9<=10`;
- RL107 local `M=1106`, `O=6`: `kappa_6=45>10`;
- RL108 witness `M=890`, `O=17`: `kappa_17=34,572,879>27`.

### Barrier

No inherited maximum/minimum, full-return, or first-Farey theorem currently controls the lift digits `d_r` strongly enough to force `kappa_O(W)<=N` or membership in another independently certified basin arithmetic type. The classifier makes the missing statement exact; it does not supply it.

---

## 6. Fresh gap-free first-surplus census through odd count 19

RL107 explicitly left an interrupted leading-`11` enumeration **NOT PROMOTED**. RL108 does not reuse it.

A fresh exact verifier independently enumerates every word satisfying:

1. total odd count `O`, `1<=O<=19`;
2. terminal length `N` equal to the least integer with `2^N>3^O`;
3. final symbol `E`;
4. every proper prefix multiplicatively balanced, `2^i<=3^(o_i)`;
5. exact RL82 word cylinder;
6. `M` chosen as the least positive even cylinder representative;
7. terminal maximum cap `(2^N-3^O)M<=B_N`.

By Theorem RL108.1, item 7 is the only nonautomatic maximum inequality after the word is first-surplus balanced. The verifier nevertheless reconstructs each promoted capped trajectory exactly to confirm integrality, positivity, and `x_i<=M` at every step.

### Exact census

| `O` | `N` | balanced first-surplus words | capped least-cylinder words |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 1 | 0 |
| 3 | 5 | 2 | 0 |
| 4 | 7 | 3 | 0 |
| 5 | 8 | 7 | 0 |
| 6 | 10 | 12 | 0 |
| 7 | 12 | 30 | 0 |
| 8 | 13 | 85 | 0 |
| 9 | 15 | 173 | 0 |
| 10 | 16 | 476 | 0 |
| 11 | 18 | 961 | 0 |
| 12 | 20 | 2,652 | 0 |
| 13 | 21 | 8,045 | 0 |
| 14 | 23 | 17,637 | 0 |
| 15 | 24 | 51,033 | 0 |
| 16 | 26 | 108,950 | 0 |
| 17 | 27 | 312,455 | 5 |
| 18 | 29 | 663,535 | 0 |
| 19 | 31 | 1,900,470 | 0 |

Total balanced first-surplus words:

`boxed: 3,066,528.`

Total capped least-cylinder realizations:

`boxed: 6.`

The `O=1` survivor is the trivial word

`10`, `M=2`,

corresponding to the trivial `{1,2}` cycle geometry.

The only five nontrivial local survivors all have `(N,O)=(27,17)` and `M=890`:

- `111101110110101111001100100`, terminal state `884`;
- `111101110110101111001110000`, terminal state `880`;
- `111101110110101111101000010`, terminal state `874`;
- `111101110110101111101001000`, terminal state `872`;
- `111101110110101111101100000`, terminal state `864`.

For all five:

- `M=890 == 80 (mod162)`;
- `M` is non-dyadic;
- `kappa_17(M)=34,572,879>27`;
- the two-odd roof predecessor is `Q=395`;
- terminal state gaps `M-x_N` are respectively `6,10,16,18,26`.

Since

`B_N-(2^N-3^O)M = 3^O(M-x_N)`,                         (6.1)

the terminal slack can be many full `3^O` units even after least-cylinder selection and all proper-prefix geometry are imposed.

### Classification and scope

This census is an **exact finite certificate**, not computational evidence and not an asymptotic theorem.

It is also intentionally local. The actual first-Farey branch has enormous inherited counts, and no extrapolation from `O<=19` is made. The five `M=890` words are not claimed to be cycle segments satisfying the inherited external cycle floor or full-cycle ownership. They are finite witnesses showing that the local first-surplus/least-cylinder/max-capping package does not logically force dyadicity or exact return.

---

## 7. Why the next obvious global splices are not reopened

RL108 tested whether its local barrier should be followed immediately by a second-extremal/full-rotation splice. Historical recovery shows that this would duplicate already-frozen work:

- RL102 proves the exact prefix/suffix transport and first-surplus rotation identities and records that equal-slope factor reduction merely transports full-word divisibility;
- RL103 freezes direct affine use of the maximum cylinder, including the generalized-increment scaling form;
- RL104 freezes direct prime-prefix content and explicitly requires materially new non-homogeneous input.

Therefore RL108 does **not** restart bare rotation transport, affine-cylinder congruences, or prime-local prefix content under new notation.

This is a verification-economy decision, not a claim that every conceivable cyclic theorem is impossible.

---

## 8. Red-team ledger

### RL20 denominator/full-ownership test

RL108.1 is a local exact maximum statement; RL108.3 uses the full physical cylinder but does not claim full-cycle `D|Q` closure. The finite witnesses are explicitly non-cycle local models. No `D∤Q` fake is promoted to a cycle.

### RL79 generalized-increment test

RL108.2 uses the ordinary `+1` LTE basin. RL108.3 classifies the ordinary physical maximum supplied by RL101. The finite verifier uses the ordinary odd inverse `(2x-1)/3`. Nevertheless, none of these ingredients forces basin equality; generalized-increment-insensitive word structure alone is not upgraded.

### RL81 physical/quotient separation

Every equality target and every `M` in the analytic statements is a physical integer. No quotient coordinate is treated as an owned cycle state.

### Primitivity

No periodic word repetition, repeated physical state, or primitive-block conclusion is inferred from the local census. The global non-dyadic consequence uses only that a cycle state equal to a power of two reaches the trivial orbit.

### Raw multiplicity and scope

Raw `(gp,gq)` and reduced `(p,q)` remain distinct. RL108 makes no `g=1` substitution and no branch-specific statement is promoted globally.

### External input

The inherited first-Farey setup and RL101 physical representative theorem retain their external-cycle-floor provenance. RL108.1 and RL108.2 are analytic independently of that floor; the finite census is an exact local calculation and does not consume it.

---

## 9. Correction/demotion ledger

1. **Checkpoint provenance repair:** “raw-`g` least-cylinder ownership is new in RL108” -> **reclassified as inherited RL101 Corollary RL101.3**.
2. **Checkpoint metadata repair:** the local checkpoint recorded the root tree SHA as `BASE_HEAD`; the correct base commit is `98878095f93860ebd41a2d17982753a14e6d5f2f`.
3. No authoritative mathematical theorem is demoted.
4. The interrupted RL107 enumeration remains discarded/unpromoted; RL108's finite certificate is a fresh independent gap-free run.

---

## 10. RL108 route verdict

The RL108 success target was an exact physical equality to a certified ordinary basin node. That equality was **not proved**.

What is now proved is a sharper failure classification:

- the physical maximum already has no residual cylinder-lift ambiguity (RL101);
- proper first-surplus prefix maxima give no additional numerical selector (RL108.1);
- changing LTE comb depth cannot evade the dyadic-max interface (RL108.2);
- the ordered word has an exact arithmetic-type address, but current ownership theorems do not force its small-discrete-log/basin condition (RL108.3);
- a fresh exhaustive bounded census supplies explicit ordinary capped non-dyadic local realizations under the full local package.

Therefore the current direct route

`first-surplus word -> local extremality/cylinder -> LTE or dyadic basin equality`

is frozen as a **method barrier at the present architecture**.

This does not say no word-sensitive basin theorem can ever exist. Reopening it requires genuinely new global information that controls the arithmetic-type lift or identifies a physical state with a different certified basin family—not another local prefix cap, raw-count condition, residue match, alternate LTE depth, or bare full-word rotation identity.

---

## 11. RL109 handover decision

The programme has now spent RL100–RL108 repairing first-Farey scope/multiplicity and testing multiple ordinary-ownership/basin/content bridges. Several formerly promising local consumers are now sharply frozen.

RL109 should therefore be a **post-basin global route re-audit**, using RL99 as the strategic baseline and incorporating RL100–RL108's new theorems and route barriers.

Its job is to rank the smallest remaining theorem edges capable of global progress, especially:

1. a global owned bridge into the already-closed radius-3 contradiction engine;
2. a Gate-A branch/multiplicity/Farey coverage theorem with genuine global scope;
3. a Gate-B `D|Q`-sensitive ordinary-owned obstruction;
4. a genuinely new direct full-phase ordinary-`+1` bypass.

RL109 must not restart the numerical cascade merely because RL108's basin route closed negative. It may recommend resumption only if the audit identifies a structural trigger that changes its global leverage.

