# RL61 radius-3 and Gate-B audit

## Audit conclusion

The historical exact radius-3 theorem survives the audit as a **closed local obstruction**. The present failure is not inside radius 3; it is the lack of a valid **global Gate-B theorem that forces a genuine RL object into radius 3 (or otherwise contradicts it)**.

The RL48 direct half-period invocation is invalid for a clean, exact reason discovered in RL49: the constructed cyclic distance is always even, so it cannot be exactly 3.

## 1. What the exact radius-3 theorem says

The recovered RL18/RL19 ledgers define a case tree for primitive, `D`-divisible self-rotations separated by exact cyclic adjacent-transposition radius 3. The theorem is conditional: it excludes every object satisfying that local configuration and the branch-specific support/orientation/gcd hypotheses.

It is therefore best understood as a **trap** that is known to be fatal once a global RL object is proved to enter it. It does not by itself prove that every global RL object enters it.

## 2. Reconstruction of the final open radius-3 leaf before RL19

After the RL18 repairs, the remaining leaf was the same-direction cubic sector
\[
\gcd(A,L)=3,\qquad \gcd(A,m)=1.
\]
Writing
\[
A=3a,\qquad L=3\ell,
\]
the retained arithmetic included
\[
\gcd(a,\ell)=1,\qquad \gcd(3a,m)=1,\qquad ap-m\ell=1.
\]
With
\[
D=2^{3a}-3^{3\ell},
\]
and the phase element `rho`, the exact sparse full-denominator condition was
\[
1+3\rho^u+9\rho^{u+v}\equiv0\pmod D,
\qquad u+v+w=3a,
\]
for positive gaps `u,v,w`.

RL19 closes this leaf analytically in the primitive setting. The proof architecture is:

1. **Weak interlacing geometry.** The possible gap orderings are reduced to structured boundary, interior skew, extreme, and equal-gap cases.
2. **One-gap-`a` boundary.** The short-order/binomial obstruction rules out the boundary configuration.
3. **Interior skew.** Elimination of the cubic phase produces an Eisenstein-norm divisibility condition. The lifted norm is shown strictly between zero and the divisor, giving contradiction.
4. **Extreme cases.** The `k=1` and `k=3` possibilities reduce to explicit resultants; exact nonvanishing and size bounds exclude them.
5. **Equal gaps.** Equality forces periodic/nonprimitive structure, contrary to the primitive hypothesis.

The final RL19 cubic leaf uses neither the LMN two-logarithm theorem nor a finite scan cutoff. Older branches in the full radius-3 tree retain their explicitly audited dependencies.

## 3. Radius-3 dependency note

The recovered historical external-dependency audit identifies the Laurent–Mignotte–Nesterenko two-logarithm theorem as an active deep input in some older radius-3 branches. Classical continued fractions, Legendre-type approximation facts, integer resultants, and exact finite certificates occur elsewhere.

No recovered radius-3 proof depends on the Jacobian conjecture.

## 4. Why local grammar is not enough: RL20

RL20 directly tests the hoped-for implication

> local least-root/final-return grammar ⇒ some pair lies at radius at most 3.

It constructs an exact packed countermodel with

- endpoint distances `20, 48, 28`;
- minimum over all rotations equal to **4**;
- nonzero `Q mod D`.

Thus the countermodel satisfies the relevant local-looking packing grammar but is **not** a genuine RL object because the full divisibility condition fails.

This result kills a proof route, not the desired global theorem. Its positive lesson is exact: **a valid Gate-B argument must use global information capable of distinguishing `D|Q` objects from the RL20 countermodel.**

## 5. RL43–RL48: stronger phase structure

The later bridge programme rebuilt more of the global structure:

- same-root ownership/selector information;
- full-denominator phase relations;
- sparse phase polynomial identities;
- the RL48 four-swap construction.

For the RL48 object the phase maps can be written in the form
\[
F_u(N)=N+4,\qquad F_v(N+4)=N,
\]
under the full phase conditions. This made the half-period swap look like a candidate for the already-closed radius-3 theorem.

## 6. RL49 correction: why the direct RL48 invocation fails

Let `d=uv` and compare the half-rotation `vu`. RL49 computes the actual cyclic adjacent-transposition distance as
\[
\operatorname{dist}_{cyc}(uv,vu)=2(a-t-3+H).
\]
The right-hand side is always even. Therefore it can never be exactly 3.

This is a decisive geometry mismatch. It does **not** undermine the full-phase identities used to construct the pair; it invalidates only the direct claim that this pair lands in the exact radius-3 theorem.

Accordingly:

- **the primitive hypothesis was not the fatal issue;**
- **the radius condition was.**

The RL48 direct half-period bridge is therefore a **dead route**.

## 7. What Gate B actually needs now

A genuine global RL→radius-3 lemma must start with the hypotheses of a real RL object—including the global ownership/divisibility/full-phase information—and produce **two primitive `D`-divisible rotations** for which all of the following are proved, not inferred by analogy:

1. exact cyclic adjacent-transposition distance **3**;
2. correct orientation/support pattern for one of the closed radius-3 branches;
3. required gcd hypotheses;
4. primitivity/nonperiodicity;
5. full `D`-divisibility/ownership inherited by both objects.

If any one of these properties is absent, the radius-3 theorem cannot be invoked.

A theorem yielding a contradiction directly from the same global information would also discharge Gate B without explicitly manufacturing a radius-3 pair.

## 8. Gate-B routes that remain alive

### A. Balanced-return weighted-difference

RL19/RL20 established exact global odd-step product and weighted-population identities. A balanced cut/return may force a weighted difference whose sign, divisibility, or size is incompatible with full ownership.

**Status:** open programme.  
**Why still alive:** the RL20 radius-4 countermodel does not satisfy the full RL divisibility, so a weighted-difference theorem using that missing information is not refuted by the countermodel.

### B. Strict-excursion packing

The global orbit can be viewed as weighted populations packed around a strict excursion. A sufficiently sharp packing theorem might rule out the required return geometry or force a locally closed configuration.

**Status:** open programme.  
**Why still alive:** it is genuinely global and need not identify the RL48 half-period pair with radius 3.

### C. New full-phase/ownership radius-3 construction

Instead of using the half-period swap, derive a different pair or short chain of owned rotations from the full phase, then prove the exact distance-3 geometry.

**Status:** open theorem target.  
**Primary risk:** reproducing a local grammar statement already defeated by RL20.

### D. Direct full-phase impossibility

Use the coupled phase, terminal power, telescoping identities, and global divisor to derive contradiction without radius 3.

**Status:** open, high-risk/high-leverage alternative.  
**Effect if successful:** Gate B is bypassed rather than bridged.

## 9. Dead vs live statements

| Statement | Audit status |
|---|---|
| Exact radius-3 local theorem | **Closed** |
| “Every local endpoint grammar object has radius <=3” | **False / dead route** |
| RL48 half-period pair has exact radius 3 | **False / dead route** |
| “No global RL object can ever be linked to radius 3” | **Not established** |
| Balanced-return weighted-difference bridge | **Open** |
| Strict-excursion packing bridge | **Open** |
| A new full-ownership exact-radius-3 bridge | **Open** |
| Direct full-phase contradiction | **Open** |

## 10. Gate-B closure criterion

Gate B should be declared closed only after one of the following is proved under an exhaustive retained RL hypothesis set:

- a theorem that constructs a configuration satisfying an already-closed local obstruction such as exact radius 3; or
- a direct contradiction from the global full-phase/ownership/divisibility data.

Reusing the phrase “radius-3 bridge” is not enough. The theorem must state and verify the exact target hypotheses line by line.
