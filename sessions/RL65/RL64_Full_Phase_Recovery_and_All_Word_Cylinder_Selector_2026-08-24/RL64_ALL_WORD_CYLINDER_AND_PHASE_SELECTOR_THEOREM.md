# RL64 — all-word synchronized cylinders, historical phase coordinate, and terminal ownership collapse

Date: 2026-08-24

## Status and scope

This file contains new RL64 mathematics proved from the frozen RL45/RL63 height-one quotient plus exact historical RL47/RL48 definitions recovered from the GitHub archive. It does **not** prove Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.

The main results are:

1. RL63's all-`11` local obstruction extends to **every** synchronized word `w in {00,11}^n`: each word has one legal first-even 2-adic entry cylinder, and within it one dangerous lift for each height budget `H`; exact exit valuation is unbounded in every word-cylinder.
2. The exact RL47 phase coordinate is `Phi=2^i(T+3^d-1)/3^(p+d)`. At `d=1`, this gives the exact integer phase numerator `P=3^(p+1)Phi=2^i(J+1)`, so the dangerous selector becomes a congruence directly on historical phase data.
3. If the synchronized block is not merely local but is the **terminal** block of the historical one-excursion geometry, where `J_n=2^k`, `k=t+3`, the unrestricted selector collapses to an exact Diophantine equality. For an all-`11` terminal suffix, `3^n q=2^k+1`; hence `n<=v3(2^k+1)`, and for `n>=1` this forces `k` odd and `n<=1+v3(k)`.

The third result is the first ownership-sensitive restriction on RL63's unrestricted all-`11` counterfamily. It is not yet strong enough to prove `H>=k`.

---

## 1. Frozen height-one maps

At `d=1`, write `x=0` for `00` and `x=1` for `11`. On odd `J`,

`F_x(J)=(3^x J+1)/2`.

Let a synchronized word be

`w=(x_0,...,x_{n-1}) in {0,1}^n`,

and put

`s(w)=sum_r x_r`,

`C(w)=sum_{r=0}^{n-1} 2^r 3^(sum_{q=r+1}^{n-1} x_q)`.

RL63 proved the affine composition identity

`2^n J_n = 3^s J_0 + C(w)`.

RL64 adds a useful `J+1` form. Define the synchronized-zero defect

`D(w)=sum_{r:x_r=0} 2^r 3^(sum_{q=r+1}^{n-1} x_q)`.

This `D(w)` is a new RL64 local notation and must **not** be confused with inherited zero-position/defect quantities such as `E=Zx-Zy`.

For `R=J+1`, one step gives

- `00`: `2R'=R+2`;
- `11`: `2R'=3R`.

Therefore

`boxed: 2^n (J_n+1) = 3^s (J_0+1) + 2D(w)`.

Comparing this with the RL63 affine formula gives

`boxed: C(w)=3^s+2D(w)-2^n`.

All identities are exact over the integers.

---

## 2. The legal first-even cylinder is exactly one odd residue class

### Theorem 2.1 — legal-cylinder bijection

For every synchronized word `w` of length `n>=1`, there is exactly one residue class

`J_0 = r_w (mod 2^(n+1))`

such that the prescribed maps are legal with

`J_0,J_1,...,J_(n-1)` odd

and the first even state is `J_n`.

Equivalently this class is the unique solution of

`boxed: 3^s J_0 + C(w) == 0 (mod 2^(n+1))`.

Moreover `r_w` is odd, and as `w` ranges over the `2^n` synchronized words, the classes `r_w` are exactly all `2^n` odd residue classes modulo `2^(n+1)`.

### Proof

Because `3^s` is odd, the displayed congruence has a unique solution modulo `2^(n+1)`. Also `C(w)` is odd (its `r=0` term is odd and every other term is even), so the solution is odd.

It remains to show that final divisibility forces all earlier prefixes to be legal. Let

`B_j=3^(sum_{r<j}x_r) J_0 + C_j`,

so formally `B_j=2^j J_j` and the one-step relation is

`B_(j+1)=3^(x_j) B_j + 2^j`.

If `B_(j+1)` is divisible by `2^(j+1)`, then, because `3^(x_j)` is odd,

`B_j == 2^j (mod 2^(j+1))`.

Thus `B_j` is divisible by exactly `2^j`, and `J_j=B_j/2^j` is odd. Starting from the final congruence and descending proves legality of every prior prefix. The final congruence has one extra factor of two, so `J_n` is even.

Distinct words cannot give the same legal odd class because starting from an odd residue class, each parity decision (`00` versus `11`) is recovered uniquely from the successive legal state modulo the next power of two. Since there are `2^n` words and `2^n` odd classes modulo `2^(n+1)`, the map is a bijection. QED.

---

## 3. Every synchronized word has a dangerous lift; exact excess is unbounded

### Theorem 3.1 — dangerous refinement

Fix a synchronized word `w` of length `n` and a height budget `H>=0`. Then

`v2(J_n)>H`

is equivalent to

`boxed: 3^s J_0 + C(w) == 0 (mod 2^(n+H+1))`.

Because `3^s` is invertible modulo powers of two, this is exactly one residue class modulo `2^(n+H+1)`. Its reduction modulo `2^(n+1)` is the legal first-even cylinder from Theorem 2.1. Consequently every synchronized word, including every mixed `00/11` word, contains infinitely many positive legal local entries whose first even exit is dangerous.

Stronger: for every integer `L>=1`, every word-cylinder contains infinitely many positive entries with exact exit valuation

`v2(J_n)=L`.

### Proof

The first statement follows immediately from `2^n J_n=3^sJ_0+C(w)`. The unique higher-modulus class reduces to the unique lower-modulus legal class, so all prior states remain odd. Adding positive multiples of the modulus gives infinitely many positive representatives.

For exact valuation `L`, first impose divisibility by `2^(n+L)`. There is one solution class modulo that power. It has two lifts modulo `2^(n+L+1)`. Since the coefficient `3^s` is odd, exactly one lift gains the extra factor of two and exactly one does not. The latter has exact valuation `L`; adding multiples of `2^(n+L+1)` gives infinitely many positive examples. QED.

### Consequence

RL63's all-`11` obstruction was not exceptional. **No local theorem depending only on the unrestricted height-one synchronized dynamics can establish Gate A.** Any successful theorem must restrict which macro entries are globally extendable/owned by the full phase geometry.

---

## 4. All-`11` is recovered as a special case

For `w=11^n`, `s=n` and `D(w)=0`. The `J+1` identity becomes

`2^n(J_n+1)=3^n(J_0+1)`.

If `11^n` is maximal first-even, write

`J_0+1=2^n q`, with `q` odd.

Then

`J_r=2^(n-r)3^r q-1` for `0<=r<=n`,

and

`J_n=3^n q-1`.

Thus `v2(J_n)>H` iff

`q == 3^(-n) (mod 2^(H+1))`,

exactly reproducing RL63.

---

## 5. Exact historical RL47 phase-coordinate interface

The recovered historical verifier `RL47_verify_rl47_phase_coordinate.py` defines

`boxed: Phi(d,T,i,p)=2^i(T+3^d-1)/3^(p+d)`.

For a pair column `(x,y)`, it proves the exact telescope

`Delta Phi = (2^i/3^p) * ((1-x) - (1-y)/3^d)`.

In particular, at `d=1`:

- `11`: `Delta Phi=0`;
- `00`: `Delta Phi=2^(i+1)/3^(p+1)`.

Using the frozen RL45 definition `J=T+3^d-2^d`, at `d=1` we have `J=T+1`, hence

`boxed: Phi = 2^i(J+1)/3^(p+1)`.

Define the integer historical phase numerator

`boxed: P = 3^(p+1) Phi = 2^i(J+1)`.

Now let a local synchronized word `w` of length `n`, weight `s`, start at global phase coordinates `(i,p,d=1,J_0)`. Multiplying the RL64 `J+1` identity by `2^i` gives

`2^(i+n)(J_n+1)=3^s P + 2^(i+1)D(w)`.

Therefore the dangerous condition `v2(J_n)>H`, equivalently `J_n+1 == 1 (mod 2^(H+1))`, is exactly

`boxed: 3^s P + 2^(i+1)D(w) == 2^(i+n) (mod 2^(i+n+H+1))`.

This is the desired exact arithmetic interface between RL63's 2-adic dangerous cylinder and the recovered historical full-phase coordinate. It is an identity/congruence theorem, not yet an exclusion theorem.

### All-`11` phase normalization

For a maximal `11^n` block, `P=2^(i+n)q`, so

`Phi/2^(i+n)=q/3^(p+1)` in the 2-adic localization (the denominator is odd).

Hence the dangerous condition becomes

`boxed: Phi/2^(i+n) == 3^(-(p+n+1)) (mod 2^(H+1))`.

Again, this identifies the dangerous class; it does not prove a genuine full-phase entry cannot occupy it.

---

## 6. Terminal ownership collapses the unrestricted selector

The exact historical RL48 full-phase reconstruction has full words

`u=110 x 1 0^t`,

`v=111 y 0^(t+1)`,

with the internal RL path starting from `(d,T)=(1,-14)` and ending, before the omitted terminal `(1,0)` column, at

`T=2^(t+3)-1`.

Put

`k=t+3`.

At terminal `d=1`, therefore

`boxed: J_terminal=T+1=2^k`.

This is an exact historical ownership/extendability condition on any synchronized block that is the final first-even height-one block.

### Theorem 6.1 — terminal-owned synchronized selector

If a legal synchronized word `w` of length `n` is the final height-one block and exits at the canonical terminal state `J_n=2^k`, then its entry is not a free 2-adic lift. It satisfies the exact equality

`boxed: 3^s J_0 + C(w)=2^(n+k)`.

Equivalently,

`boxed: 3^s(J_0+1)+2D(w)=2^n(2^k+1)`.

Thus a necessary and sufficient arithmetic condition for the backward synchronized word to have an integral entry is

`boxed: 3^s | [2^n(2^k+1)-2D(w)]`.

When this divisibility holds,

`J_0+1 = [2^n(2^k+1)-2D(w)]/3^s`.

The word can also be checked backward from `J_n=2^k` by the exact inverse rules

- inverse `00`: `J_prev=2J-1` (always integral odd);
- inverse `11`: `J_prev=(2J-1)/3`, requiring `J == 2 (mod 3)`.

These are equivalent descriptions of terminal synchronized ownership.

### Corollary 6.2 — all-`11` terminal collapse

For a terminal all-`11` suffix of length `n>=1`, `D=0`, `s=n`, and

`boxed: 3^n q=2^k+1`,

where `J_0+1=2^n q` and `q` is odd.

Hence

`q=(2^k+1)/3^n`

is completely fixed by `(k,n)`; the arbitrary choice `q == 3^(-n) (mod 2^(H+1))` from the unrestricted RL63 counterfamily is no longer available.

Moreover, `3 | 2^k+1` forces `k` odd. For odd `k`, the lifting-the-exponent lemma gives

`v3(2^k+1)=v3(2+1)+v3(k)=1+v3(k)`.

Therefore

`boxed: n <= 1+v3(k)`.

If `k` is even, no positive-length terminal all-`11` suffix is possible.

### What this does and does not prove

The dangerous terminal condition is `k>H`, because `v2(J_terminal)=k` and terminal `K=H`. Corollary 6.2 sharply restricts the all-`11` suffix geometry, but it does **not** imply `H>=k`. The remaining proof obligation is to combine this terminal collapse with the globally accumulated height/phase/rank-displacement constraints before the final synchronized block.

---

## 7. Mixed terminal words: exact 3-adic compatibility condition

For a mixed synchronized terminal word, Theorem 6.1 yields

`D(w) == 2^(n-1)(2^k+1) (mod 3^s)`

when `s>=1`.

This is a useful complement to RL63's 2-adic selector: **local danger is a 2-adic cylinder, while terminal ownership imposes an exact 3-adic/equality condition through `D(w)`.** The two conditions should not be conflated.

A productive next attack is to combine this exact terminal condition with the inherited rank-displacement identity `H=sum delta_j` and the exact RL47 phase telescope. The target is to show that `k>H` is incompatible with a globally completable internal pair word, first for the restricted all-`11` terminal suffix above and then for mixed words satisfying the `D(w)` congruence.

---

## 8. Classification ledger for this file

### Analytic theorems proved here

- `J+1` synchronized composition with `D(w)` and `C=3^s+2D-2^n`.
- unique legal first-even cylinder for every synchronized word.
- unique dangerous lift for every `(w,H)` and unbounded exact exit valuation in every local word-cylinder.
- exact historical phase-numerator selector congruence after recovering RL47 `Phi`.
- terminal-owned exact equality and backward inverse criterion.
- all-`11` terminal collapse `3^n q=2^k+1` and bound `n<=1+v3(k)` for odd `k`.

### Exact finite/computational evidence

The bundled RL64 verifier exhaustively checks these formulas for bounded word lengths/heights and verifies the recovered historical RL47 phase-coordinate script. These finite checks audit implementations; they are not substitutes for the proofs above.

### Still open

- exclusion of all dangerous **globally full-phase-owned** entries;
- `H>=k` uniformly (Gate A);
- Gate B and all larger closure claims.
