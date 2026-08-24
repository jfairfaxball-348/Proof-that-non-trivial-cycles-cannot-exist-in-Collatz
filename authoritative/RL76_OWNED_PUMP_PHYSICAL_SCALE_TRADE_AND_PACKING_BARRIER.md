# RL76 — Owned pump physical-scale trade and packing barrier

Date: 2026-08-24

## 0. Executive outcome

RL76 attacked the RL75 tournament winner: the **owned synchronized-macro periodicity-or-packing** route in the first open Gate-A band

`27<=k<=165`, `k` odd, hypothetical `H<k`.

The incoming RL75 bundle passed its current checksum/manifest/fast-verifier gate and was accepted under the verification-economy rule.

RL76 does **not** prove the target upper bound on the RL73 giant macro. Gate A and Gate B remain open. However, the periodic branch has been sharpened substantially.

The main new theorem is that a closed height-one synchronized pump does not merely hide repeat depth inside RL74's Möbius context coefficients. In a genuine RL64 paired physical realization, repeat depth is stored **exactly as a physical state-scale ratio**, while the RL50 normalized weight changes by the reciprocal ratio. This gives an exact normal form for the paired physical states and for the RL75 Möbius determinant.

For the canonical positive pump `c=10`, the result is especially explicit:

`A_0 = 1+4^q m`, `B_0 = 1+3*4^q m`,

`A_q = 1+3^q m`, `B_q = 1+3^(q+1)m`.

Thus

`(A_0-1)/(A_q-1)=(4/3)^q`.

A uniform repeat-depth bound is therefore equivalent to a uniform bound on this physical excursion ratio. No such bound is present in the inherited ledger.

Moreover, using only the stable state floor `R0=2^71`, the total reciprocal mass of the `2q` odd physical states occurring in the two synchronized halves of a `c=10` repeat is bounded by

`< 4(1-(3/4)^q)/(R0-1) < 4/(R0-1)`,

independently of `q`.

Consequently the inherited RL19/RL20 reciprocal/harmonic state-packing machinery does **not** by itself price `c=10` repeat depth. The repeat can be arbitrarily deep while its reciprocal packing mass remains bounded and can be made arbitrarily small by increasing the physical scale parameter `m`.

This is a new method barrier for the winning hybrid route, not a counterexample to full phase.

Strategically, RL76 therefore recommends the pivot prescribed by RL75: the next session should attack the **product/growth/continued-fraction + modern full-phase** route, now with the new physical-scale normal form as an explicit interface. The key missing theorem is a global full-phase restriction on physical excursion scale, reduced `(a,ell)` data, or the complementary context that prevents the pump scale parameter from being arbitrarily large.

---

## 1. Incoming proof state retained

Retain exactly the RL75 ledger:

- radius-3 primitive/full-`D` theorem: closed local obstruction;
- Gate A even terminal `k`: analytically impossible;
- Gate A `k<=25`: closed by exact finite-certificate corollary;
- first open terminal exponent: odd `k>=27`;
- every hypothetical odd `27<=k<=165` violation contains an RL73 maximal post-first-mismatch height-one block with at least
  `40,249,491,324,522,944` aligned `00` columns;
- RL74 endpoint/`Jg`/`Psi` mechanisms do not price zero-area count;
- RL74 fixed-context full phase sees a repeated pump by an exact Möbius law;
- RL75 proves primitive proper-pump nondegeneracy `D_*!=0` and `N==19 mod24`;
- Gate A globally open; Gate B globally open; RL/nontrivial-cycle exclusion open.

No historical expensive certificate was recursively rerun.

---

## 2. RL50/RL64 paired physical coordinates at height one

Use the inherited paired physical shortcut-Collatz states `A_i,B_i` from the one-excursion construction. At height `d=1`,

`T_i=3A_i-B_i`,

`J_i=T_i+1=3A_i-B_i+1`.                         (2.1)

On a synchronized internal word, the same binary shortcut word is applied to both physical states.

For a binary word `c` of length `n` and weight `s`, write

`P=2^n`, `R=3^s`, `C=Q(c)`.

The physical affine map is

`F_c(X)=(R X+C)/P`.                                  (2.2)

The RL50 height-one quotient synchronized dynamics is conjugate to the physical shortcut map by

`J=2z+1`.

Indeed, for one synchronized bit,

`G_b(2z+1)=2F_b(z)+1`,

for both `b=0` and `b=1`.

This elementary conjugacy is the key to the new pump normal form.

---

## 3. New theorem A — closed-pump physical fixed point

Assume `c` is a nonempty synchronized word that closes an odd height-one quotient state `J`:

`G_c(J)=J`.

Let

`alpha=C/(P-R)`                                           (3.1)

be the affine fixed point of the **physical** map `F_c`.

Because `J=2z+1` conjugates the synchronized quotient dynamics to `F_c`, closure gives

`boxed: alpha=(J-1)/2`.                                  (3.2)

In particular `alpha` is an integer for every odd closed quotient state, and

`boxed: C=(P-R)alpha`.                                   (3.3)

This also follows directly from the paired relation. If `J` is unchanged by applying `F_c` to both `A,B`, then

`P(J-1)=R(J-1)+2C`.

Classification: **analytic theorem**.

### Special pumps

- `c=10`: `P=4`, `R=3`, `C=1`, so `alpha=1`, `J=3`.
- `c=101`: `P=8`, `R=9`, `C=7`, so `alpha=-7`, `J=-13`.

This simultaneously explains the RL50 quotient cycles and the RL75 physical affine fixed points.

---

## 4. New theorem B — exact paired-state repeat normal form

Suppose the closed synchronized word `c` is repeated `q>=1` times inside a genuine integral paired physical trajectory at height one.

At pump entry, (2.1) and `J=2alpha+1` give

`B_0-alpha = 3(A_0-alpha)`.                              (4.1)

After `q` copies,

`A_q-alpha=(R/P)^q(A_0-alpha)`,

`B_q-alpha=(R/P)^q(B_0-alpha)`.                         (4.2)

Since `A_0,A_q,alpha` are integers and `gcd(P,R)=1`, integrality forces

`P^q | (A_0-alpha)`.

Hence there is an integer `m` such that

`boxed: A_0=alpha+P^q m`,                               (4.3)

`boxed: B_0=alpha+3P^q m`,                              (4.4)

`boxed: A_q=alpha+R^q m`,                               (4.5)

`boxed: B_q=alpha+3R^q m`.                              (4.6)

For a primitive proper pump, `m!=0`; `m=0` is exactly physical pump closure.

Classification: **analytic theorem**.

### Canonical positive pump `c=10`

Here `alpha=1`, so positivity/nontriviality gives `m>=1` and

`A_0=1+4^q m`,

`B_0=1+3*4^q m`,

`A_q=1+3^q m`,

`B_q=1+3^(q+1)m`.                                      (4.7)

Therefore

`boxed: (A_0-1)/(A_q-1)=(4/3)^q`.                       (4.8)

A uniform `q` bound is therefore equivalent to a uniform physical excursion-ratio bound.

### Canonical negative pump `c=101`

Here `alpha=-7`, so for positive physical states `m>=1` and

`A_0=-7+8^q m`,

`B_0=-7+3*8^q m`,

`A_q=-7+9^q m`,

`B_q=-7+3*9^q m`.                                      (4.9)

The physical scale grows by `(9/8)^q` while the RL50 normalized weight shrinks by `(8/9)^q`.

---

## 5. New theorem C — exact weight/physical-scale conservation on a closed pump

The inherited normalized weight is

`g=2^i/3^(p_x)`.

Across a synchronized word of length `n`, weight `s`,

`g` is multiplied by

`P/R`.

Together with (4.2), every closed synchronized pump satisfies

`boxed: g_out (A_out-alpha)=g_in(A_in-alpha)`,          (5.1)

and likewise

`boxed: g_out (B_out-alpha)=g_in(B_in-alpha)`.          (5.2)

After `q` copies,

`g_q=g_0(P/R)^q`,

while physical deviation from the pump fixed point scales by `(R/P)^q`.

This is the exact scale-trade hidden behind the RL74 canonical shrink/growth family. A pump can make `g` exponentially small or large only by making the corresponding physical state deviation exponentially large or small.

Classification: **analytic synthesis** of the RL50 normalization with the RL74/RL75 pump architecture.

### Strategic meaning

The old phrase “context can be arbitrary” can now be sharpened:

> **repeat depth is paid for by unbounded physical excursion scale.**

A theorem that bounds `g` but has no upper control on physical phase states cannot by itself bound the number of zero-area repeats.

The stable external cycle verification floor supplies only a **lower** bound on physical states; it does not cap this excursion ratio.

---

## 6. New theorem D — RL75 determinant normal form on an owned closed pump

Use the RL75 notation for a full half-word

`v_q=A_ctx c^q B_ctx`,

with

`M_q=X0 P^q-Y0 R^q`.

RL75 proves

`D_*=2^|A_ctx| 3^wt(B_ctx) (delta x+C) M_q/P^q`,       (6.1)

where `delta=R-P` and `x` is the physical pump-entry state on the `v` half.

For the synchronized paired realization, `x=B_0`. By (3.3) and (4.4),

`delta x+C`

`=(R-P)(x-alpha)`

`=3(R-P)P^q m`.

Therefore

`boxed: D_* = 3m(R-P) 2^|A_ctx| 3^wt(B_ctx) M_q`.      (6.2)

This is an exact cancellation of the apparent `P^q` denominator in the RL75 physical-drift factorization.

Classification: **analytic theorem/synthesis**.

### Corollaries

1. `D_*=0 <=> m=0`, recovering RL75 primitive nondegeneracy in the paired normal form.
2. For `c=10`, `R-P=-1`, `m>0`, so `D_*<0`.
3. For `c=101`, `R-P=1`, positive-state `m>0`, so `D_*>0`.
4. For every genuine completion of a **fixed** context,

   `boxed: m_q M_q = K_ctx`,                            (6.3)

   where

   `K_ctx=D_*/[3(R-P)2^|A_ctx|3^wt(B_ctx)]`

   is independent of repeat count.

Thus fixed-context finiteness becomes an exact divisibility statement rather than merely an injective-convergent-sequence statement.

If `P>R`, then

`M_(q+1)=P M_q+(P-R)Y0 R^q > P M_q`.                  (6.4)

Hence a fixed context can support only finitely many contraction-pump depths because the positive denominators `M_q` grow at least geometrically while each must divide the fixed scale integer `K_ctx` through (6.3).

This is stronger fixed-context control than RL74, but `K_ctx` is still globally unbounded in the present ledger.

---

## 7. New theorem E — `c=10` reciprocal-packing mass is uniformly bounded in repeat depth

Now use the stable inherited nontrivial-cycle state floor

`R0=2^71`.

For a `c=10` repeat of depth `q`, the odd physical states at the start of each `1` step in the two synchronized halves are

`A_j=1+4^(q-j)3^j m`,

`B_j=1+3*4^(q-j)3^j m`,

for `j=0,...,q-1`.                                      (7.1)

The pump exit is

`A_q=1+3^q m >= R0`.                                    (7.2)

Since

`A_j-1=(4/3)^(q-j)(A_q-1)`,

we get

`sum_(j=0)^(q-1) 1/A_j`

`< [3/(R0-1)] [1-(3/4)^q]`.                            (7.3)

Also `B_j-1=3(A_j-1)`, so

`sum_(j=0)^(q-1) 1/B_j`

`< [1/(R0-1)] [1-(3/4)^q]`.                            (7.4)

Therefore

`boxed:`

`sum_j (1/A_j+1/B_j)`

`< 4[1-(3/4)^q]/(R0-1)`

`< 4/(R0-1)`.                                          (7.5)

Classification: **analytic theorem under the retained stable external state floor**.

### Product-bound corollary

RL19's odd-step product uses terms

`log(1+1/(3x)) < 1/(3x)`.

Thus the entire `2q`-odd-state contribution of this repeated pump to the full-cycle logarithmic product is

`boxed: < 4/[3(R0-1)]`,                                (7.6)

again independent of `q`.

Numerically,

`4/[3(2^71-1)] < 5.647e-22`.

RL73's full-phase squeeze gives

`2 log zeta < 158/[9(R0-2)] < 7.436e-21`.              (7.7)

The important point is not the numerical ratio. It is that the pump's reciprocal/product mass has **no growing lower cost in `q`**. Indeed, for fixed `q`, taking the scale parameter `m` larger makes the contribution arbitrarily small.

Therefore the inherited RL19/RL20 reciprocal/harmonic population packing cannot, by itself, provide the missing uniform `c=10` repeat-depth bound.

This is a **method barrier**, not a genuine full-phase countermodel.

---

## 8. Mandatory stress tests

### 8.1 RL74 canonical fixed-area shrink/growth family

The new scale-conservation theorem explains rather than eliminates the RL74 stress family.

- `c=101` multiplies `g` by `8/9` and physical deviation from `-7` by `9/8`.
- `c=10` multiplies `g` by `4/3` and physical deviation from `1` by `3/4`.

Thus the RL74 choice of a deep negative shrink pump followed by a deep positive growth pump is an exact exchange between normalized weight and physical scale. The inherited lower state floor does not prevent this because the physical scale may grow without a known upper bound.

So the new theorem **passes the stress test as a barrier diagnosis**: it identifies the missing hypothesis rather than falsely contradicting the canonical family.

### 8.2 RL20 radius-4 local-grammar fake model

The new theorem is not a radius/ownership closure theorem and is not expected to reject the RL20 `D∤Q` fake word. Its role is to show that local synchronized pumping plus reciprocal packing remains insufficient. Any future contradiction that uses (4.8), (5.1), or (6.3) must still insert genuine full-phase/`D|Q` information absent from the RL20 fake model.

---

## 9. Periodic branch assessment after RL76

The periodic branch is now sharper but still open.

For a contraction pump `P>R`, repeat depth is exactly

`q = log_(P/R) |(A_0-alpha)/(A_q-alpha)|`.              (9.1)

Therefore a uniform repeat-depth theorem requires at least one of:

1. a uniform upper bound on the physical state excursion ratio;
2. a uniform upper bound on the scale integer `K_ctx=mM` from (6.3);
3. a new full-phase congruence that bounds `m` or forces `M_q` incompatible with `mM_q=K_ctx`;
4. a complementary-context product/Diophantine theorem that prevents the rest of the half-cycle from compensating the pump scale.

None is currently in the frozen ledger.

The canonical `c=10` branch is therefore **not closed uniformly**.

---

## 10. Aperiodic branch assessment after RL76

No quantitative aperiodic packing theorem was obtained.

RL50's exact conjugacy says a positive height-one synchronized block, before its even exit, is simply a shortcut-Collatz orbit segment in

`n=(J-1)/2`.

If there is no repeated quotient state, the block is an injective Collatz segment in this quotient coordinate. The present physical relation

`J=3A-B+1`

and positivity yield only lower-scale information on the physical states when `J` is large. Reciprocal/harmonic packing needs the opposite kind of control—an upper bound on enough physical states—to force a growing cost.

Thus the current RL19/RL20 packing tools do not yet turn “many distinct quotient contexts” into a global contradiction.

This is recorded as a **method barrier / failed route in the present form**, not as a proof that no stronger packing theorem exists.

---

## 11. RL76 route decision

The RL75 winning route has not closed the low-`k` Gate-A band.

What RL76 has established is a precise reason the obvious periodicity/packing splice stalls:

- the periodic branch hides depth in an unbounded physical excursion scale, with exact weight-scale conservation;
- the reciprocal packing mass of the canonical positive repeat is uniformly bounded in depth;
- the aperiodic branch remains Collatz-conjugate and lacks a global state ceiling/consumer.

This triggers the RL75 stop/pivot criterion.

The next deliberate route is therefore:

# **Product/growth/continued-fraction + modern full phase**

The new RL76 theorem should be carried into that route as the required scale interface.

---

## 12. Proposed RL77 theorem target

Seek a theorem that couples the reduced near-resonant exponent data to the physical excursion scale.

A useful target is:

> **Full-phase scale/CF coupling theorem.** For a genuine full-phase one-excursion datum, prove that a proper closed synchronized pump with scale ratio `(P/R)^q` forces either
> 1. an impossible restriction on the reduced ratio `a/ell` / its continued-fraction convergent data, or
> 2. a complementary-context population/product cost exceeding the RL73 phase-resonance budget.

For the `c=10` branch, the exact input is

`A_0-1=(4/3)^q(A_q-1)`,

`m M_q=K_ctx`,

with the RL73 global denominator/skew floors and `N==19 mod24`.

Do not return to raw endpoint `Psi`, q-digit extension, or determinant-zero descent.

---

## 13. Correction/demotion ledger additions

Retain all RL72–RL75 corrections and add:

1. **“Context variability” sharpened.** On a closed synchronized pump, the unbounded context freedom can be represented concretely by an unbounded physical scale parameter `m` / excursion ratio.
2. **Reciprocal packing does not price `c=10` depth.** The exact reciprocal mass of the two synchronized odd-state chains is bounded independently of repeat count.
3. **Normalized-weight caps alone cannot control a closed pump.** `g(A-alpha)` and `g(B-alpha)` are exactly conserved across the pump, so small `g` can be exchanged for large physical state scale.
4. **Fixed-context finiteness strengthened.** For an owned closed pump, `m_q M_q=K_ctx`; for `P>R`, `M_q` grows faster than `P^q`. The remaining obstruction is uniform control of `K_ctx`, not merely injectivity of the Möbius function.
5. **No aperiodic packing theorem claimed.** Distinct height-one quotient states remain a shortcut-Collatz segment; current harmonic physical-state packing has no upper-state interface that charges their number.

---

## 14. Exact proof state after RL76

### New proved analytic mathematics

- closed synchronized quotient pump fixed point satisfies `alpha=(J-1)/2` for the physical affine map;
- exact paired physical repeat normal form (4.3)–(4.6);
- exact normalized-weight / physical-scale conservation (5.1)–(5.2);
- owned-pump RL75 determinant normal form (6.2);
- fixed-context scale-divisibility invariant `m_q M_q=K_ctx`;
- geometric growth of `M_q` for contraction pumps `P>R`;
- exact `c=10` reciprocal-mass bound (7.5) and q-independent product-mass ceiling (7.6).

### New method barriers

- RL19/RL20 reciprocal/harmonic packing alone cannot bound canonical `c=10` repeat depth;
- the periodic branch requires a global physical excursion/scale control not currently present;
- the aperiodic branch remains without a quantitative global consumer.

### Global closure state

Unchanged:

- radius-3 primitive/full-`D` local obstruction: **closed**;
- Gate A even `k`: **closed analytically**;
- Gate A `k<=25`: **closed by exact finite certificate corollary**;
- Gate A odd `27<=k<=165`: **open**;
- Gate A globally: **open**;
- Gate B globally: **open**;
- RL/nontrivial-cycle exclusion: **open**;
- Collatz conjecture: **not proved**.
