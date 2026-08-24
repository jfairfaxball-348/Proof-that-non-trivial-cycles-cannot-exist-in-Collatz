# RL78 — `D|Q`-sensitive rotation defect and corrected block-scale barrier

Date: 2026-08-24

## 0. Executive outcome

RL78 carried out the RL77-selected reconnaissance target:

# **Gate B — genuine `D|Q`-sensitive bounded-radius / owned-rotation reconnaissance**

The incoming RL77 checksum, internal manifest, and fast verifier suite pass. Under the verification-economy rule, the frozen RL77 proof-state ledger is retained.

RL78 does **not** prove an owned radius-`<=3` pair, an absolute radius-`<=4` theorem, Gate B, RL/nontrivial-cycle exclusion, or the Collatz conjecture. The session does, however, produce a useful exact ownership theorem, expose and repair one historical RL20 formula, and identify a common physical-scale barrier in the strict-excursion version of the radius route.

The main results are:

1. **Rotation ownership-defect theorem.** For every binary word `d`, every cyclic rotation transports its word numerator modulo the full denominator by a unit. Consequently

   `gcd(D,Q(rot_m d)) = gcd(D,Q(d))`

   for every rotation. Thus every rational fixed phase has the same reduced denominator

   `s = |D|/gcd(|D|,Q(d))`.

   Genuine full-`D` ownership is exactly the special case `s=1`.

2. **Pairwise normalized-rotation congruences are not ownership-sensitive.** After normalization, all rotation numerators lie in one unit orbit modulo `D` for **every word**, including `D∤Q` words. Therefore any proposed bridge that only subtracts two or more such normalized rotation congruences is automatically true on the RL20 fake and cannot be the missing Gate-B theorem.

3. **RL20 correction.** The canonical narrow-strip lift in `RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md` omitted a factor `3^{-E_{j+1}}` in its displayed increment. The correct identity is

   `H_{j+1}-H_j = z^j 3^{-E_{j+1}} Q(B_j)/Y`.

   The original RL20 verifier did not test this identity. The one-sided imbalance theorem, height bands, endpoint strip, and monotonicity survive; any quantitative strict-excursion argument that prices a block by the factor-free increment must be repaired/demoted.

4. **Exact block scale-trade law.** The corrected increment satisfies

   `(H_{j+1}-H_j)/H_{j+1} = Q(B_j)/(X x_{j+1})`.

   Thus a block's normalized lift cost is discounted by its physical exit scale. Positive imbalance raises the physical state by powers of `3`, and the omitted factor is precisely the corresponding scale discount. This aligns the RL20 strict-excursion route with the RL76/RL77 obstruction: without an independent upper bound on physical scale, repeated/global complexity cannot be uniformly priced by a fixed strip budget.

5. **Mandatory negative control sharpened.** For the exact RL20 length-184 radius-4 fake,

   `gcd(D,Q)=1`.

   Hence its ownership-defect denominator is the maximal value `s=D`. Nevertheless its exact rational fixed orbit is positive, closes rationally, has the designated root phase as its least rational phase, satisfies the inherited local grammar, and has all-rotation minimum word radius exactly `4`. It therefore isolates full integer ownership exceptionally cleanly.

The requested RL78 stop rule is met: a serious `D|Q`-sensitive reconnaissance did not produce an absolute radius theorem, and the most immediate multi-rotation and strict-excursion candidates either collapse to all-word unit transport/coboundaries or expose the same uncontrolled physical-scale reservoir. No generic radius-4 case tree is launched.

---

## 1. Frozen incoming state

Retain the authoritative RL77 ledger exactly:

- primitive/full-`D` radius-3 local obstruction: **closed**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.

RL77 additionally established the full-half product window, the first reduced-CF branch de-scaling `g=1`, the unimodular canonical pump basis, and the exact closed-pump product/physical-scale law. Those results are retained but are not re-audited here.

---

## 2. Selectively recovered Gate-B interfaces

### 2.1 RL18 — full denominator as a global orbit condition

For a binary word `d=(d_0,...,d_{A-1})` of weight `L`, put

`D=2^A-3^L`,

`P_i=sum_{j<i} d_j`,

`q_i=2^i 3^{-P_i}` modulo `D`, and `Z=sum_i q_i`.

RL18 gives

`Q(d) = (3^L/4) Z (mod D)`,

so, because `3` and `4` are units modulo `D`,

`D|Q(d) <=> Z=0 (mod D)`.

This is the required global ownership discriminator absent from the RL20 local-grammar fake.

### 2.2 RL19 — arbitrary-rotation weighted difference

For a genuine cycle phase `R` and its rotation phase `R_m`, RL19 gives

`sum_i q_i(3^{-G_i}-1)=4(lambda-1)(R_m-R)`.

This is exact, but its right side is already a state difference. RL72 later proved that applying it to the RL48 half-rotation four-swap pair collapses exactly to the known proper-factor identity. That raw splice is therefore retained as a method barrier, not retried.

### 2.3 RL20 — mandatory fake and block coboundary

The exact RL20 word has `(A,L)=(184,116)`, satisfies the inherited least-root/final-return local grammar, is primitive, and has

`min_{a<b} dist_cyc(rot_a(d),rot_b(d))=4`.

But `D∤Q`. Therefore local grammar alone cannot force a radius-3 pair.

RL20 also gives the correct block coboundary

`3^{-E_{j+1}}Q(B_j)=Xy_{j+1}-Yy_j`,

where `y_j=3^{-E_j}x_j`.

This identity is load-bearing for the correction in Section 5.

### 2.4 RL48/RL49/RL72 — routes already excluded

RL48 reconstructs the full-phase four-swap pair `N <-> N+4`, but RL49 proves the actual half-period word distance is

`dist_cyc(uv,vu)=2(a-t-3+H)`,

so physical closeness is not radius-3 word closeness.

RL72 additionally proves that the RL19 weighted difference on this pair is exactly the RL48 proper-factor identity in different coordinates. Both direct shortcuts remain retired.

---

## 3. New theorem A — exact rotation numerator transport

Let a binary word split at position `m` as

`d = AB`,

where `|A|=m` and `wt(A)=p`. Let `d_m=BA` be the left rotation by `m`. Then the standard concatenation rule for the Collatz word polynomial gives

`Q(AB)=3^{wt(B)}Q(A)+2^m Q(B)`,

`Q(BA)=3^p Q(B)+2^{A-m}Q(A)`.

Multiplying the second identity by `2^m` and subtracting `3^p` times the first gives

`boxed: 2^m Q(d_m)-3^p Q(d)=D Q(A).`                  (3.1)

This is an exact integer identity for **every binary word**; no cycle or divisibility hypothesis is used.

Modulo `D`,

`boxed: 2^m Q(d_m) == 3^p Q(d) (mod D).`              (3.2)

Since `D=2^A-3^L` is coprime to `6`, `2^m` and `3^p` are units modulo `D`. Hence

`boxed: gcd(D,Q(d_m))=gcd(D,Q(d)).`                    (3.3)

Classification: **analytic theorem**.

### 3.1 Ownership-defect denominator

Define

`s(d)=|D|/gcd(|D|,Q(d)).`                                (3.4)

Then (3.3) shows

`boxed: s(rot_m d)=s(d) for every m.`                   (3.5)

The rational fixed phase `R_m=Q(d_m)/D` therefore has reduced denominator exactly `s(d)` at every rotation.

Thus:

- `s=1` iff `D|Q(d)` iff **all** cyclic phases are integral/owned;
- `s>1` iff **no** cyclic phase is integral;
- the failure of ownership is not localized at one rotation: it is a global denominator class carried around the full orbit.

This gives a clean algebraic formulation of the distinction that the RL20 fake is missing.

---

## 4. New theorem B — normalized pairwise rotation residuals are all-word tautologies

Put

`rho_m = 2^m 3^{-P_m} (mod D)`.

Equation (3.2) is equivalent to

`boxed: rho_m Q(d_m) == Q(d) (mod D).`                  (4.1)

Therefore for every pair of rotations `m,n`,

`boxed: rho_m Q(d_m)-rho_n Q(d_n) ==0 (mod D).`        (4.2)

Crucially, (4.2) holds for **every word**, including words with `D∤Q`.

Classification: **analytic method barrier**.

### 4.1 Gate-B consequence

This immediately rejects a large family of tempting “use two or more owned rotations” candidates. If the construction only:

1. writes the rotation numerators;
2. rescales them by the natural `2^m/3^{P_m}` units; and
3. subtracts them modulo `D`,

then the resulting divisibility is not consuming ownership at all. It is simply the universal transport identity (4.2), so it also holds on the RL20 fake.

A successful `D|Q` bridge must use the **absolute zero class** `Q==0 (mod D)` / `s=1`, actual integer phase ordering/packing, or another property unavailable to a common nonzero residue class.

This is stronger than the existing RL72 half-rotation diagnosis: it shows why a whole natural class of multi-rotation congruence differences cannot discriminate genuine ownership.

---

## 5. Stop-and-repair event — RL20 canonical lift increment

RL20's correct block coboundary is

`3^{-E_{j+1}}Q(B_j)=Xy_{j+1}-Yy_j`,                    (5.1)

with

`X=2^a`, `Y=3^ell`, `z=X/Y`,

`y_j=3^{-E_j}x_j`,

`H_j=z^j y_j`.

Multiplying (5.1) by `z^j/Y` gives

`boxed: H_{j+1}-H_j`

`boxed: = z^j 3^{-E_{j+1}}Q(B_j)/Y.`                   (5.2)

The historical RL20 near-resonant geometry note instead displayed

`H_{j+1}-H_j = z^j Q(B_j)/Y`,

omitting `3^{-E_{j+1}}`.

The historical verifier `verify_rl20_near_gcd_block_geometry.py` does not test the increment identity; it tests the one-sided integer imbalance implication, balanced-cut oddness, a finite rescue threshold, and the CF-induced block-length floor. Thus the missing factor was not caught by that verifier.

Classification: **historical analytic formula corrected**.

### 5.1 What survives

The following RL20 facts do not depend on the omitted factor and remain valid:

- near resonance / least-state suffix domination gives `E_j>=0` at proper canonical cuts under the stated hypotheses;
- the physical height sandwich
  `R# < z^j x_j/3^{E_j} <= lambda R#`;
- balanced `E_j=0` cuts lie in the near-minimum strip;
- positive imbalance forces separated physical height bands;
- `H_j` is monotone, because the corrected increment (5.2) is still nonnegative;
- `H_0=R#`, `H_g=lambda R#` and the global narrow-strip endpoint budget remain exact.

### 5.2 What is demoted/repaired

Any strict-excursion quantitative argument that treats a positive-imbalance block as costing

`z^j Q(B_j)/Y`

in the strip is invalid as stated. The correct cost is smaller by `3^{-E_{j+1}}`.

No already-closed radius-3 theorem or Gate-A theorem is affected by this correction. It repairs an open RL20 Gate-B programme.

---

## 6. New theorem C — exact block lift / physical-scale trade

Divide (5.2) by

`H_{j+1}=z^{j+1}3^{-E_{j+1}}x_{j+1}`.

Because `zY=X`, the imbalance factors cancel exactly:

`boxed: (H_{j+1}-H_j)/H_{j+1}`

`boxed: = Q(B_j)/(X x_{j+1}).`                          (6.1)

Equivalently,

`boxed: x_{j+1}(H_{j+1}-H_j)=H_{j+1}Q(B_j)/X.`        (6.2)

Classification: **analytic synthesis**.

### 6.1 Strategic meaning

The narrow lift does not charge a block independently of physical scale. A large block-exit state makes its relative strip cost small.

In the strict-excursion regime, positive `E_{j+1}` is precisely what raises the physical state into a band of size roughly `3^{E_{j+1}}R#`. Equation (5.2) then discounts the strip increment by the reciprocal factor `3^{-E_{j+1}}`.

So the discrete height excursion and the narrow-strip cost are not competing effects; they are paired by an exact scale trade.

This is structurally parallel to RL76/RL77:

- RL76 found a free physical scale parameter in repeated synchronized pumps;
- RL77 found that the full-phase product budget prices pump depth by physical entry scale rather than repeat count;
- RL78 finds that the corrected canonical-block strip budget prices block complexity by physical exit scale rather than block count alone.

No inherited theorem provides the required global upper bound on that physical scale.

---

## 7. Exact stress family for the corrected strict-excursion cost

This subsection is a **method stress test**, not a candidate RL object and not a full-`D` construction.

Take fixed block dimensions `(a,ell)` with `z=2^a/3^ell>1`. Consider an imbalance pattern

`0 -> h -> h -> ... -> h -> 0`,

and choose each block with its `r` ones at the earliest positions, so

`Q(B)=3^r-2^r`.

For the entry block of weight `ell+h`, each middle block of weight `ell`, and the exit block of weight `ell-h`, formula (5.2) gives exactly:

- entry cost:
  `1-(2/3)^(ell+h)`;
- middle cost at index `j`:
  `z^j 3^{-h}[1-(2/3)^ell]`;
- exit cost:
  `z^j 3^{-h}[1-(2/3)^(ell-h)]`.

Thus once a height `h` has been paid for, every subsequent plateau block carries the explicit discount `3^{-h}`. The RL78 verifier checks this family exactly over thousands of block instances.

This does not show that such a family has genuine full phase or `D|Q`. It shows only that the corrected strip identity itself cannot furnish a height-independent per-block cost. A successful strict-excursion theorem must consume an additional global ownership restriction that bounds or penalizes the physical scale.

---

## 8. Mandatory RL20 fake negative control — strengthened exact audit

For the exact RL20 word

`A=184`, `L=116`,

`D=2^184-3^116`

and the frozen word polynomial `Q`, RL78 verifies

`Q mod D = 322171738410077807581692882247758374512983113782519312`,

and newly records

`boxed: gcd(D,Q)=1.`                                      (8.1)

Therefore

`boxed: s(d)=D`

is maximal: the fake is as far from full integer ownership as the denominator ideal permits.

The exact rational fixed state

`R=Q/D`

has reduced denominator `D`. Iterating the 184 prescribed affine parity steps over `Q` returns exactly to `R`; every phase is positive; and the designated root phase is the least rational phase of this fixed orbit.

At the canonical `gcd(A,L)=4` block scale,

`(a,ell)=(46,29)`

and the exact imbalance path is

`boxed: E=(0,1,1,1,0).`                                  (8.2)

On its first three blocks, the corrected increment (5.2) is exactly one third of the historically printed factor-free value. On the final block, where `E_{j+1}=0`, the two formulas coincide.

The inherited all-rotation minimum radius remains exactly

`boxed: 4.`                                               (8.3)

Classification:

- radius-4 packing and `D∤Q`: **inherited exact finite certificate**;
- `gcd(D,Q)=1`, maximal reduced denominator, exact rational least-orbit audit, and corrected block increment audit: **new exact finite certificate**.

### Why this is a strong negative control

The fake now demonstrates simultaneously that:

- local least-root/final-return grammar can hold;
- all rotations can stay outside radius 3;
- a positive rational least fixed orbit can exist;
- canonical one-sided imbalance / strict excursion can occur;
- normalized rotation congruences can hold universally;

while integer ownership fails maximally.

Any candidate Gate-B theorem that cannot distinguish `s=1` from this `s=D` example is not consuming the missing global condition.

---

## 9. Candidate reconnaissance ledger

### Candidate 1 — RL19 weighted difference on RL48 half rotation

**Result:** reject / inherited exact collapse.

RL72 already proves it is exactly the RL48 proper-factor identity.

### Candidate 2 — subtract two or more normalized rotation numerators

**Result:** reject / new all-word transport barrier.

Equation (4.2) holds for every binary word, including the RL20 fake. Pairwise normalized congruence cancellation is therefore not `D|Q`-sensitive.

### Candidate 3 — canonical block strict-excursion strip pricing

**Result:** repair and demote in factor-free form.

The historical increment omitted `3^{-E_{j+1}}`. The corrected scale-trade (6.1) shows that high physical states discount strip cost. No uniform radius or block-count theorem follows from the narrow strip without an independent scale cap.

### Candidate 4 — the absolute ownership-defect class `s`

**Result:** survives as a genuine discriminator, but does not yet force radius.

`s=1` is exactly genuine full-`D` ownership and the fake has `s=D`. However, RL78 has no theorem converting `s=1` into a bounded cyclic adjacent-transposition radius.

### Candidate 5 — balanced-cut integrality quantization

At a genuine balanced canonical cut `E_j=0`, both the least state `R#` and the distinct balanced phase `x_j` are odd integers. Hence

`x_j-R# >=2`.

Combined with the exact balanced-cut height bound, this gives a genuine integrality gap unavailable to a generic rational fake. It is ownership-sensitive in the correct direction, but the current bound is far too weak to force a radius-3/4 pair or a small nonzero full-`D` multiple.

**Result:** live observation / non-closing.

---

## 10. RL78 route decision

The target asked for a genuinely non-coboundary `D|Q`-sensitive invariant forcing:

1. an owned radius-`<=3` pair;
2. an absolute owned radius `<=4`; or
3. a direct contradiction.

RL78 does not obtain any of these.

The serious reconnaissance instead establishes two negative structural facts:

- natural multi-rotation normalized numerator differences are universal unit-transport identities, not ownership consumers;
- the historical strict-excursion strip pricing omitted the exact physical-scale discount, and after repair it encounters the same unbounded scale reservoir already exposed by RL76/RL77.

The RL20 fake remains a decisive discriminator, but no theorem currently converts the absolute condition `s=1` into bounded radius.

Therefore the RL78 stop criterion is satisfied. Do **not** launch a generic radius-4/5/6 local case tree.

The next session should return to the RL75 global route map with the accumulated RL76–RL78 barriers and perform a post-tournament synthesis: identify a genuinely new theorem architecture that simultaneously avoids

- state/proper-factor/unit-transport coboundaries;
- free physical-scale absorption;
- local-grammar countermodels lacking full ownership.

---

## 11. Correction / demotion ledger additions

Retain all RL72–RL77 corrections and add:

1. **RL20 narrow-strip increment corrected.** Replace
   `H_{j+1}-H_j=z^jQ(B_j)/Y`
   by
   `H_{j+1}-H_j=z^j3^{-E_{j+1}}Q(B_j)/Y`.
2. **RL20 strict-excursion per-block pricing demoted unless repaired.** Monotonicity and height bands survive; any quantitative use of the factor-free increment does not.
3. **Normalized rotation-difference divisibility demoted as an ownership test.** The natural unit-normalized residue is constant modulo `D` for every word, so pairwise subtraction also holds on `D∤Q` fakes.
4. **Ownership defect localized correctly.** The meaningful global discriminator is the absolute residue ideal / common reduced denominator `s`, not pairwise normalized rotation congruences.
5. **RL20 fake sharpened.** It has `gcd(D,Q)=1`, so its ownership defect is maximal, despite having a positive rational least fixed orbit and radius-4 packing.
6. **No radius-4 inference.** The fake's minimum radius `4` remains a negative-control boundary, not evidence that genuine objects have radius at most `4`.

---

## 12. Exact proof state after RL78

### New proved analytic mathematics

- exact rotation numerator transport (3.1)–(3.2);
- rotation invariance of `gcd(D,Q)` and common ownership-defect denominator (3.3)–(3.5);
- universal normalized multi-rotation congruence barrier (4.1)–(4.2);
- corrected canonical-block narrow-strip increment (5.2);
- exact block lift/physical-scale trade (6.1)–(6.2);
- exact algebraic plateau stress-family cost formulas.

### New exact finite certificate / audit

The RL78 verifier checks:

- `9,212` exact rotation transport identities;
- `8,192` rotation gcd-invariance cases;
- `75,287` corrected block-lift identities;
- `70,374` block scale-trade identities;
- `4,176` stress-family block identities;
- the exact RL20 fake remainder `Q mod D`;
- `gcd(D,Q)=1` for the fake;
- its exact rational fixed orbit positivity and least-root property;
- its canonical imbalance path `(0,1,1,1,0)`;
- the corrected-vs-printed factor discrepancy on positive-imbalance exits;
- all-rotation minimum radius `4`.

The verifier is an audit/falsification certificate, not the proof of the infinite analytic statements.

### Global closure state

Unchanged:

- primitive/full-`D` radius-3 local obstruction: **closed**;
- Gate A even terminal `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite-certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.
