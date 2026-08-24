# RL65 — rank-tail factorization and full-phase quotient selector

Date: 2026-08-24

## Status

This note contains new RL65 analytic deductions from the checksum-clean RL64 state. It does **not** prove Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The main advance is to connect three exact pieces that were previously kept separate:

1. the RL45/RL64 internal recurrence and area `H`;
2. the RL48 rank polynomials `Qx,Qy` and full-phase quotient;
3. the terminal height-one synchronized suffix.

The resulting selector is genuinely global: it applies only after full-phase extendability is imposed. It also exposes a precise limitation: the terminal all-`11` 3-adic residue information alone is compatible with infinitely many positive phase quotients and therefore cannot by itself prove `H>=k`.

---

## 1. Frozen notation

Take a full-phase extendable one-excursion datum in the exact RL64 sense:

- `k=t+3`;
- internal length `m=a-k-1`;
- internal weight `r=ell-3`;
- `X=2^a`, `Y=3^ell`, `M=X-Y>0`;
- internal words `x,y` of common length `m` and weight `r`;
- internal path starts `(d,T,H)=(1,-14,0)` and ends `(1,2^k-1,H)`;
- full words are `u=110 x 1 0^t`, `v=111 y 0^(t+1)`;
- full phase requires `M | V+4Y`, where `V=Q(v)`.

Let the 1-positions of `x` and `y` be

`a_1<...<a_r`, `b_1<...<b_r`,

and put

`delta_j=a_j-b_j`.

Define

`Qx=sum_j 2^(a_j) 3^(r-j)`,

`Qy=sum_j 2^(b_j) 3^(r-j)`,

and the **rank defect**

`mathcalD=Qx-Qy`.

This `mathcalD` is distinct from RL64's local synchronized-zero defect `D(w)`.

Because `M | V+4Y`, define the positive integer phase quotient

`N=(V+4Y)/M`.

By the exact RL48 four-swap theorem this is the actual smaller value in the full `4`-swap construction, with `N == 3 (mod 8)` and `N+4 == 7 (mod 8)`.

---

## 2. Direct area = rank-displacement theorem

### Theorem 2.1

For every legal internal path in the RL64 definition,

`boxed: H=sum_(j=1)^r delta_j`,

and every `delta_j>=0`.

### Proof

Before internal column `q`, let

`X_q=sum_(h<q) x_h`, `Y_q=sum_(h<q) y_h`.

The height recurrence gives

`d_q=1+Y_q-X_q`.

Hence

`H=sum_(q=0)^(m-1)(d_q-1)`

` =sum_q sum_(h<q)(y_h-x_h)`

` =sum_h (m-1-h)(y_h-x_h)`.

Because `x,y` have the same total weight, the constant `(m-1)` terms cancel, leaving

`H=sum_h h(x_h-y_h)`

` =sum_j a_j-sum_j b_j`

` =sum_j(a_j-b_j)`.

Legality requires `d_q>=1`, so `Y_q>=X_q` at every prefix. Thus the `j`-th `y`-one occurs no later than the `j`-th `x`-one: `b_j<=a_j`. Therefore `delta_j>=0`. QED.

### Corollary 2.2 — support compression under a hypothetical violation

If `H<k`, then

- at most `H` ranks have `delta_j>0`;
- therefore `mathcalD` has at most `H<=k-1` active rank terms.

Explicitly,

`mathcalD=sum_(delta_j>0) 3^(r-j) 2^(b_j)(2^(delta_j)-1)`.

This is exact support compression, not a radius-3 statement.

---

## 3. Terminal rank identity and the exact full-phase defect quotient

RL48's exact terminal identity is

`3Qx-Qy = 14*3^r + 2^(a-1)-2^(a-k-1)`.

Since `Qx=Qy+mathcalD`, this is

`2Qy+3mathcalD = 14*3^r + 2^(a-1)-2^(a-k-1)`.

The exact full second half-word has

`V=19*3^r+8Qy`,

while `4Y=108*3^r`. Therefore

`V+4Y`

`=183*3^r + 2^(a+1)-2^(a-k+1)-12mathcalD`.

Using `MN=V+4Y` and

`2M=2^(a+1)-54*3^r`,

we obtain the exact integer equality

`boxed: (2-N)M = 12mathcalD + 2^(a-k+1)-237*3^r`.      (3.1)

This is stronger than the old RL48 congruence: the quotient of the congruence is identified exactly as `2-N`.

Equivalently,

`boxed: (N-2)M = 237*3^r-12mathcalD-2^(a-k+1)`.      (3.2)

No phase-polynomial or common-root language is needed for (3.1); it follows directly from the exact RL48 full-word reconstruction now frozen in RL64.

---

## 4. Rank-tail factorization from a terminal synchronized suffix

Suppose the final internal height-one block contains a terminal synchronized suffix `w` of length `n`, with `s` occurrences of `11` and `n-s` occurrences of `00`.

Because the suffix starts at `d=1` and every suffix column has `x=y`, the cumulative x/y weights agree at suffix entry and throughout the suffix. Every suffix `11` therefore creates a matched rank pair at the same position. Since the suffix is terminal, these are the last `s` rank pairs.

Thus

`delta_(r-s+1)=...=delta_r=0`.

Consequently

`boxed: 3^s | mathcalD`.

More explicitly, if `s<r`,

`mathcalD=3^s mathcalD_*`,

where

`mathcalD_* = sum_(j<=r-s, delta_j>0) 3^((r-s)-j) 2^(b_j)(2^(delta_j)-1)`.

If `H<k`, `mathcalD_*` still has at most `k-1` active terms.

This is the exact rank-side meaning of stripping the terminal synchronized suffix: the suffix contributes zero area, zero rank defect, and only a factor `3^s` on the earlier defect.

---

## 5. New full-phase 3-adic quotient selector

### Theorem 5.1

Under the hypotheses of section 4,

`boxed: N == 2-2^(1-k) (mod 3^(s+1))`,

where the negative power of 2 means the inverse of `2^(k-1)` modulo the odd modulus `3^(s+1)`.

### Proof

In (3.1), `3^s | mathcalD`, so

`3^(s+1) | 12mathcalD`.

Also `r>=s` and `237=3*79`, so

`3^(s+1) | 237*3^r`.

Reducing (3.1) modulo `3^(s+1)` gives

`(2-N)M == 2^(a-k+1) (mod 3^(s+1))`.

Because `ell=r+3>=s+3`,

`M=2^a-3^ell == 2^a (mod 3^(s+1))`.

Cancel the unit `2^a` to obtain

`2-N == 2^(1-k) (mod 3^(s+1))`.

QED.

### Corollary 5.2 — all-`11` suffix

For a terminal all-`11` suffix of length `n>=1`, `s=n`. RL64 already proves

`3^n | 2^k+1`,

with `k` odd and `n<=1+v3(k)`.

RL65 adds

`boxed: N == 2-2^(1-k) (mod 3^(n+1))`.      (5.2)

Reducing one power lower and using `2^k == -1 (mod 3^n)` recovers

`N == 4 (mod 3^n)`.

The extra modulus `3^(n+1)` is the genuinely new digit supplied by the full-phase/rank-defect coupling.

### Corollary 5.3 — quantitative size of the all-`11` selector modulus

Since `n<=1+v3(k)`,

`3^(n+1) <= 9*3^(v3(k)) <= 9k`.

Thus the new all-`11` residue modulus grows at most linearly in `k`.

---

## 6. Independent full-word derivation of the suffix selector

The same selector can be seen directly from the final part of the full word `u`.

For a synchronized suffix word `w=(w_0,...,w_(n-1))`, define its one-polynomial

`R(w)=sum_(q:w_q=1) 2^q 3^(number of 1s after q in w)`.

The last `s+1` ones of the full word `u` are the `s` suffix ones plus the mandatory terminal `1` before `0^t`. Earlier ones carry at least a factor `3^(s+1)` in `Q(u)`. Therefore, modulo `3^(s+1)`,

`Q(u) == 2^(a-k+2-n) [2^n+3R(w)]`.

From the exact half-return

`3^ell N+Q(u)=2^a(N+4)`,

we obtain

`boxed: N == -4 + 2^(2-k-n)[2^n+3R(w)] (mod 3^(s+1))`.      (6.1)

Consistency of (6.1) with Theorem 5.1 is equivalent, after cancelling one factor of 3, to RL64's exact terminal compatibility condition for `w`.

For `w=11^n`, `R(w)=3^n-2^n`, and (6.1) becomes

`N == -4-2^(3-k) (mod 3^(n+1))`,

which is equivalent to (5.2) because `3^n | 2^k+1`.

This gives an independent semantic check of the rank-defect derivation.

---

## 7. New terminal-word parity split

### Theorem 7.1 — even terminal exponent forces an all-`00` synchronized block

Work backward from the terminal state `J=2^k` using the exact RL64 inverse synchronized maps

- inverse `00`: `J -> 2J-1`;
- inverse `11`: `J -> (2J-1)/3`, allowed only when `J==2 (mod 3)`.

If `k` is even, then `2^k==1 (mod3)`. Inverse `00` sends residue `1` to

`2*1-1==1 (mod3)`.

Therefore after any number of inverse `00` steps the state remains `1 mod3`, and inverse `11` is never legal.

Hence:

`boxed: if k is even, every legal terminal synchronized word is all-00.`

For an all-`00` terminal block of length `n`, its entry is exactly

`boxed: J_0=2^n(2^k-1)+1`.

This is a structural split in the broad RL64 full-phase-extendable definition. It does **not** say that the historically retained near-resonance branch actually contains even `k`; older RL47 relaxations often imposed branch-specific even `t` (hence odd `k`). Those older hypotheses must not be silently globalized.

---

## 8. What the all-`11` attack does and does not achieve

The terminal all-`11` suffix is now much more rigid than in RL63:

- `3^n q=2^k+1` fixes the local entry;
- `n<=1+v3(k)` makes the suffix short in 3-adic length;
- `H` is unchanged across the suffix;
- the exact historical phase `Phi` is unchanged across the suffix;
- the last `n` rank displacements vanish;
- `mathcalD=3^n mathcalD_*`;
- the global phase quotient obeys one extra digit,
  `N==2-2^(1-k) mod3^(n+1)`.

But these facts still do **not** imply `H>=k`.

Indeed, the two residue conditions

`N==3 (mod8)`

and

`N==2-2^(1-k) (mod3^(n+1))`

always have exactly one residue class modulo `8*3^(n+1)` by the Chinese remainder theorem, hence infinitely many positive solutions. Therefore a proof that uses only these local/full-phase residue selectors, without the exact size/order/path information in `mathcalD_*`, cannot close Gate A.

Moreover, by Corollary 5.3 the all-`11` selector modulus is at most `9k`; the LTE restriction makes the final all-`11` suffix too short to generate a rapidly growing 3-adic obstruction by itself.

This is a **method barrier**, not a counterexample to Gate A.

---

## 9. Exact reduced obstruction after RL65

For a terminal synchronized suffix with `s` ones, a hypothetical violation `H<k` now reduces to the existence of data satisfying all RL64 full-phase extendability constraints together with

`mathcalD=3^s mathcalD_*`,

where `mathcalD_*` has at most `k-1` active positive rank terms, and the exact quotient equality

`boxed: (2-N)M = 12*3^s mathcalD_* + 2^(a-k+1)-237*3^r`,

with

`N>0`, `N==3 (mod8)`,

and

`N==2-2^(1-k) (mod3^(s+1))`.

For an all-`11` suffix, additionally

`3^n q=2^k+1`, `n<=1+v3(k)`.

The unresolved analytic content is therefore no longer the terminal suffix itself. It is to control the **earlier sparse rank defect with order/prefix/path coupling** strongly enough to rule out the exact quotient equality when `H<k`.

A particularly sharp next lemma would bound the last active displacement rank, or the exact value/residue of `mathcalD_*` modulo `M`, using the canonical-start path rather than only the separable cap/room relaxation. RL48's barrier theorem already shows that the old separable rank relaxation cannot do this uniformly.

---

## 10. Classification

**New analytic theorems in RL65**

- direct derivation `H=sum delta_j`, `delta_j>=0` from the RL64 recurrence;
- terminal synchronized suffix implies `3^s | mathcalD`;
- exact full-phase quotient equality (3.1), promoting the old defect congruence to an exact quotient identity under RL64's recovered full-word source;
- phase quotient selector `N==2-2^(1-k) mod3^(s+1)`;
- independent full-word suffix selector (6.1);
- even `k` terminal synchronized words are necessarily all-`00`.

**Still open**

- `H>=k` for the all-`11` terminal class;
- `H>=k` for mixed/all-`00` terminal classes;
- uniform Gate A;
- Gate B and any RL/radius-3 closure.
