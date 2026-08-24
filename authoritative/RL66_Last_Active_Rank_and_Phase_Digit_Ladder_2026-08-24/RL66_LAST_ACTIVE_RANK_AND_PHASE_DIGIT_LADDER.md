# RL66 — last-active-rank normal form and phase-digit ladder

Date: 2026-08-24

## Status

This note continues from the checksum-clean RL65 state under the **verification economy rule**. It contains new analytic deductions from the frozen RL65 recurrence, rank-defect identity, terminal synchronized-tail theorem, and full-phase quotient identity.

It does **not** prove Gate A for odd `k`, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture. It does prove a stronger structural result for the other parity: **a canonical terminal RL path cannot have even terminal exponent `k` at all**.

---

## 1. Frozen notation

Use RL65 notation:

- internal length `m=a-k-1`;
- internal words `x,y` of common weight `r`;
- one-positions `a_1<...<a_r`, `b_1<...<b_r`;
- `delta_j=a_j-b_j>=0`;
- `H=sum_j delta_j`;
- rank defect
  `mathcalD=sum_j 3^(r-j) 2^(b_j)(2^(delta_j)-1)`;
- canonical internal state starts `(d,T,H)=(1,-14,0)` and a terminal state has
  `(d,T)=(1,2^k-1)` and hence `J=T+3^d-2^d=2^k`;
- terminal synchronized suffix has column length `n` and contains `s` `11` columns;
- full phase, when imposed, has
  `M=2^a-3^ell`, `ell=r+3`, and
  `N=(V+4*3^ell)/M`, with `N>0`, `N==3 (mod 8)`;
- RL65's exact quotient identity is

  `(2-N)M = 12 mathcalD + 2^(a-k+1) - 237*3^r`.        (1.1)

For the RL recurrence itself,

`T' = (3^y T + x 3^(d+y-1) - y)/2`,

`d'=d+y-x`.

Write `J=T+3^d-2^d`.

---

## 2. The last active displacement rank

Let

`j_* = max{j : delta_j>0}`.

### Lemma 2.1 — a canonical terminal path has an active rank

A canonical terminal path cannot be fully synchronized.

At height `d=1`, synchronized columns act on `J` by

- `00: J -> (J+1)/2`;
- `11: J -> (3J+1)/2`.

Starting from canonical `J=-13`, both maps keep `J<=0` whenever they are legal. Therefore a path using only synchronized columns cannot reach terminal `J=2^k>0`.

Any canonical terminal path therefore contains a mismatch. Since it ends again at equal x/y weight and prefix legality gives `delta_j>=0`, at least one `delta_j` is positive, so `j_*` exists.

Classification: **analytic theorem**.

### Lemma 2.2 — no later y-one after `b_(j_*)`

Put

`b_*=b_(j_*)`, `a_*=a_(j_*)`, `delta_*=a_*-b_*>0`.

Then

`y_q=0` for every `b_*<q<=a_*`.

Indeed, a later `y_q=1` would be some y-rank `l>j_*`. Its matching x-rank occurs strictly after `a_*`, so `delta_l>0`, contradicting maximality of `j_*`.

At column `a_*` one therefore has `10`. Immediately after it the x/y prefix counts are equal, so `d=1`.

After `a_*`, all columns are synchronized: any later mismatch would create a later positive rank displacement.

Hence `a_*` is the **last mismatching column of the internal path**.

Classification: **analytic theorem**.

### Corollary 2.3 — exact terminal-tail placement

Because exactly `n` synchronized columns follow the last mismatch,

`a_* = m-n-1`,

`b_* = m-n-1-delta_* = a-k-n-2-delta_*`.       (2.1)

All rank pairs after `j_*` come from the terminal synchronized tail. Therefore

`boxed: j_*=r-s`.                                      (2.2)

Here and below rank indices are one-based.

---

## 3. Last-active-rank mod-3 selector

### Theorem 3.1

Let `J_tail` be the height-one `J` state immediately after the last mismatch `a_*`, equivalently the entry state of the terminal synchronized suffix. Then

`boxed: J_tail == 1 + 2^(delta_*) (mod 3)`.             (3.1)

In particular,

- if `delta_*` is odd, `J_tail==0 (mod3)`;
- if `delta_*` is even, `J_tail==2 (mod3)`;
- `J_tail` is never `1 (mod3)`.

### Proof

At the column `b_*`, one has `y=1`. Independently of `x` and the incoming height,

`T_after = (3T + x 3^d - 1)/2 == (-1)/2 == 1 (mod3)`.

For each of the following `delta_*` columns through and including `a_*`, Lemma 2.2 gives `y=0`. The update is

`T'=(T+x3^(d-1))/2`.

If `x=1`, legality has `d>=2`, so `3^(d-1)` is divisible by `3`; if `x=0` the extra term is zero. Thus at every one of those columns

`T'==T/2==2T (mod3)`.

After `delta_*` such steps,

`T_tail==2^(delta_*) (mod3)`.

At the exit height `d=1`, `J_tail=T_tail+1`, proving (3.1). QED.

Classification: **analytic theorem**.

---

## 4. Even terminal exponent is impossible

### Theorem 4.1 — parity elimination

`boxed: every canonical terminal exponent k is odd.`

### Proof

Assume `k` even. RL65 Theorem 7.1 proves that every legal synchronized word obtained by reversing from terminal `J=2^k` is all-`00`. Therefore the terminal synchronized suffix of length `n` is all-`00`, and its entry is exactly

`J_tail = 2^n(2^k-1)+1`.

Since `k` is even, `2^k==1 (mod3)`, so

`J_tail==1 (mod3)`.

This contradicts Theorem 3.1, which says the entry after the last active rank is never `1 mod3`. Lemma 2.1 guarantees that the last active rank exists, including the case `n=0`.

Therefore even `k` cannot occur. QED.

### Consequence for Gate A

The Gate-A terminal inequality `H>=k` is now **vacuously resolved for the even-`k` parity class**, because there are no canonical terminal paths with even `k` to which the inequality must be applied.

This does not resolve odd `k`, and therefore does not close Gate A globally.

Classification: **analytic theorem**, depending on the frozen RL65 even-`k` synchronized-tail theorem.

---

## 5. Exact recursion at the last active rank

Define the individual rank terms

`E_j = 2^(b_j)(2^(delta_j)-1)`.

Then

`mathcalD=sum_j 3^(r-j) E_j`.

By (2.2), the last `s` ranks have zero displacement and `j_*=r-s`. Therefore

`boxed: mathcalD = 3^s mathcalD_*`,

with

`boxed: mathcalD_* = E_(j_*) + 3 E_(j_*-1) + 3^2 E_(j_*-2)+...`.      (5.1)

This is the requested nonseparable last-active-rank recursion. The last coefficient is not a free variable: by (2.1),

`boxed: E_(j_*) = 2^(a-k-n-2-delta_*) (2^(delta_*)-1)`.              (5.2)

Under a hypothetical Gate-A violation `H<k`, one has `delta_*<=H<=k-1`, but the exact location (5.2) still retains the terminal-tail length and full-word length rather than replacing the term by a separable cap.

Classification: **analytic theorem**.

---

## 6. Exact valuation at the first stripped digit

### Theorem 6.1

With `s` terminal tail ones,

- if `delta_*` is odd, `v3(mathcalD)=s` exactly;
- if `delta_*` is even, `v3(mathcalD)>=s+1`.

### Proof

Modulo `3`, (5.1) gives

`mathcalD_* == E_(j_*) == 2^(b_*)(2^(delta_*)-1) (mod3)`.

If `delta_*` is odd, `2^(delta_*)-1==1 (mod3)`, so `mathcalD_*` is a unit modulo `3`.

If `delta_*` is even, `3 | 2^(delta_*)-1`, so both the last term and all earlier terms in (5.1) are divisible by `3`.

QED.

For even `delta_*`, LTE gives the local valuation

`v3(2^(delta_*)-1)=1+v3(delta_*)`,

but cancellation with the earlier `3 E_(j_*-1)+...` terms can affect higher digits, so RL66 does not promote a stronger general equality without extra rank-gap information.

Classification: **analytic theorem**.

---

## 7. Rank-tail phase-digit ladder

For `1<=q<=j_*`, define the last-`q` rank truncation

`C_q = sum_(h=0)^(q-1) 3^h E_(j_*-h)`.

Thus

`mathcalD = 3^s(C_q + 3^q Z_q)`

for some integer `Z_q`.

### Theorem 7.1 — exact phase-digit ladder

Under full-phase extendability,

`boxed: N == 2 - 2^(1-k) - 4*3^(s+1) 2^(-a) C_q`

`       (mod 3^(s+q+1))`.                              (7.1)

The negative power denotes the inverse of `2^a` modulo the odd modulus.

### Proof

Reduce RL65 identity (1.1) modulo `3^(s+q+1)`.

Because `q<=j_*=r-s`,

`r+1>=s+q+1`,

so `237*3^r` vanishes modulo this modulus. Also `ell=r+3>s+q+1`, hence

`M=2^a-3^ell == 2^a`.

Finally,

`12 mathcalD = 4*3^(s+1)(C_q+3^q Z_q)`

and the `Z_q` term vanishes modulo `3^(s+q+1)`. Cancelling the unit `2^a` yields (7.1). QED.

This is an exact digit-by-digit re-expression of the full-phase quotient that keeps the ordered rank tail; it is not the old RL47 separable rank relaxation.

Classification: **analytic theorem**.

---

## 8. The new universal next 3-adic digit

Take `q=1`. From (5.2),

`4*2^(-a) E_(j_*)`

`= 4*2^(b_*-a)(2^(delta_*)-1)`

`= 2^(-(k+n+delta_*))(2^(delta_*)-1)`.

Therefore:

### Theorem 8.1 — next-digit selector

`boxed: N == 2-2^(1-k)`

`       - 3^(s+1) 2^(-(k+n+delta_*))(2^(delta_*)-1)`

`       (mod 3^(s+2))`.                                (8.1)

By Theorem 4.1, terminal `k` is odd. Reducing only the correction coefficient modulo `3` gives the particularly simple form

`boxed: N == 2-2^(1-k) - epsilon*2^n*3^(s+1)`

`       (mod 3^(s+2))`,                                (8.2)

where

`epsilon = 0` if `delta_*` is even,

`epsilon = 1` if `delta_*` is odd.

Thus RL65's modulus `3^(s+1)` always gains one explicitly determined 3-adic digit in RL66:

- even `delta_*`: the RL65 residue simply lifts unchanged to `3^(s+2)`;
- odd `delta_*`: the new digit is the nonzero correction `-2^n*3^(s+1)`.

Classification: **analytic theorem**.

---

## 9. Zero-rank gap amplification

Let `g` be the number of consecutive zero-displacement ranks immediately preceding `j_*`:

`delta_(j_*-1)=...=delta_(j_*-g)=0`,

with `g=0` if the immediately preceding rank is active or does not exist.

Then in (5.1),

`mathcalD_* = E_(j_*) + 3^(g+1) W`

for some integer `W`.

Taking `q=g+1` in Theorem 7.1 gives:

### Theorem 9.1 — last-active zero-gap selector

`boxed: N == 2-2^(1-k)`

`       - 3^(s+1) 2^(-(k+n+delta_*))(2^(delta_*)-1)`

`       (mod 3^(s+g+2))`.                              (9.1)

So every consecutive zero-displacement rank immediately before the last active one supplies another exact phase digit without exposing the earlier prefix.

This is potentially useful because zero-displacement ranks cost no area. It is not by itself a Gate-A proof: synchronized rank pumping can make `g` large, while `N` and earlier canonical data are not a priori bounded by `k` alone.

Classification: **analytic theorem plus method limitation**.

---

## 10. Odd-`k` terminal-tail consequences

Even `k` has been eliminated, so only odd `k` remains.

### 10.1 All-`00` terminal tail

If the terminal synchronized suffix is all-`00` of length `n`, then

`J_tail=2^n(2^k-1)+1`.

For odd `k`, `2^k==2 (mod3)`, hence

`J_tail==1+2^n (mod3)`.

Comparing with Theorem 3.1 yields

`boxed: n == delta_* (mod2)`.                           (10.1)

Consequently:

- even `n` gives even `delta_*` and the unchanged lift of the phase selector to modulo `9`;
- odd `n` gives odd `delta_*` and the explicit nonzero modulo-`9` correction in (8.2).

Classification: **analytic theorem**.

### 10.2 All-`11` terminal tail: maximality dichotomy

Suppose the entire terminal synchronized suffix is `11^n`, `n>=1`. RL65 gives

`3^n | 2^k+1`.

Put `e=v3(k)` and `nu=v3(2^k+1)`. Lemma 10.3 below proves self-containedly that `nu=e+1`. Also put

`q_n=(2^k+1)/3^n`.

The exact synchronized reverse formula is

`boxed: J_tail = 2^n q_n - 1`.                         (10.2)

If `n<nu`, then `3|q_n`, so

`J_tail==2 (mod3)`.

Theorem 3.1 therefore forces

`boxed: delta_* even`,

and hence, by Theorem 6.1 and (8.2),

`3^(n+1)|mathcalD`

and

`boxed: N == 2-2^(1-k) (mod 3^(n+2))`.                (10.3)

So every **nonmaximal** all-`11` tail gains a second digit beyond RL65's original `3^(n+1)` selector.

If `n=nu`, then `q_n` is a 3-adic unit. Since Theorem 3.1 forbids `J_tail==1 (mod3)`, (10.2) forces

`boxed: q_n == 2^n (mod3)`,                           (10.4)

and then `J_tail==0 (mod3)`, so `delta_*` is odd.

### Lemma 10.3 — normalized 3-adic quotient digit

Let `e=v3(k)` and `m_0=k/3^e`. Then

`boxed: v3(2^k+1)=e+1`,

and

`boxed: (2^k+1)/3^(e+1) == m_0 (mod3)`.                (10.5)

#### Proof

Set

`A_e=(2^(3^e)+1)/3^(e+1)`.

`A_0=1`. If `x=2^(3^e)`, then

`A_(e+1)=A_e * (x^2-x+1)/3`.

Since `x==-1 (mod 3^(e+1))`, the second factor is `1 mod3`; hence by induction `A_e==1 mod3` for all `e`.

Now write `k=3^e m_0`. With `m_0` odd,

`x^(m_0)+1=(x+1)(x^(m_0-1)-x^(m_0-2)+...-x+1)`.

Modulo `3`, the second factor is `m_0`, which is nonzero modulo `3`. Since `A_e` is also a 3-adic unit, the factorization shows both that the exact valuation is `e+1` and that dividing by `3^(e+1)` gives (10.5). QED.

Combining (10.4) and (10.5), a **maximal** all-`11` terminal tail is possible only if

`boxed: m_0 == 2^(e+1) (mod3)`,                        (10.6)

where `m_0=k/3^e`.

If (10.6) fails, the maximal all-`11` terminal class is analytically eliminated. If it holds, `delta_*` is odd and Theorem 8.1 gives

`N == 2-2^(1-k)-2^n 3^(n+1) (mod3^(n+2))`.

A simple special case is `3 not| k` (`e=0`, `nu=1`): a nonempty all-`11` terminal tail then has `n=1` and is possible only when

`k==2 (mod3)`, i.e. `k==5 (mod6)`.

Thus odd `k==1 (mod6)` cannot have an all-`11` terminal synchronized tail.

Classification: **analytic theorem**.

---

## 11. Exact finite audit

`verification/verify_rl66_last_active_rank.py` is an independent exact-integer audit built directly from the frozen RL recurrence and full-word `Q` construction. It is a falsification/audit tool, not a proof of the infinite theorems.

Fresh bounded results at `MAX_M=17`:

- canonical terminal paths checked: `1,421`;
- last-active normal-form checks: `1,421`;
- defect-valuation checks: `1,421`;
- next-digit phase-selector checks: `1,206`;
- even-delta lifted-selector checks: `659`;
- rank-tail digit-ladder checks: `4,792`;
- last-active zero-gap selector checks: `1,206`;
- odd-k all-`00` tail checks: `235`;
- all-`11` refinement checks: `773`;
- normalized LTE quotient checks: `500`;
- sampled maximal all-`11` normalized classes allowed: `250`;
- sampled maximal all-`11` normalized classes forbidden: `250`;
- even-k all-`00` reverse contradiction checks: `220`;
- status: `RL66 last-active-rank verifier: PASS`.

The phase-selector checks use the exact rational residue `(V+4Y)M^(-1)` modulo powers of `3`; when full-phase divisibility holds this is exactly the integer `N` residue. As in RL65, bounded examples are not used to establish the infinite full-phase theorem.

---

## 12. What RL66 changes in the live obstruction

RL66 removes one entire parity class:

`boxed: terminal k must be odd`.

For odd `k`, the terminal rank tail now determines strictly more than RL65 knew:

1. the last mismatch is exactly the x-occurrence `a_(j_*)` of the last positive displacement rank;
2. `J_tail mod3` determines the parity of `delta_*`;
3. `v3(mathcalD)` is exact at the first stripped digit when `delta_*` is odd and gains at least one digit when it is even;
4. the global phase quotient has an explicit next 3-adic digit modulo `3^(s+2)`;
5. a zero-displacement rank gap of length `g` before `j_*` extends the explicit selector to `3^(s+g+2)`;
6. all-`11` tails split into nonmaximal tails with an automatic selector lift and maximal tails subject to the normalized congruence (10.6).

The remaining obstruction is still the **earlier odd-`k` canonical prefix**. The digit ladder is exact but does not by itself bound `N`, and height-one synchronized pumping can create arbitrarily many zero-area matched ranks. Therefore RL66 does not convert the new congruences into `H>=k` for every odd `k`.

---

## 13. Recommended RL67 attack

The most promising next target is a two-case attack on the rank immediately before `j_*`.

1. Let `g` be the zero-rank gap before `j_*`. If `g` is large, use the high-modulus selector (9.1) together with the exact terminal-tail reverse value and the full phase quotient to seek a size/order contradiction, rather than merely invoking CRT.
2. If `g` is small, expose the previous active rank in `C_(g+2)` and derive its exact canonical state transition. This retains the ordered recurrence and avoids the RL48 separable-relaxation barrier.
3. Keep the odd-`k` tail split explicit: all-`00`, mixed, nonmaximal all-`11`, maximal all-`11` satisfying (10.6).
4. Use `H<k` only as support/area compression (`delta_*<k`, at most `k-1` active ranks); do not convert zero-rank gaps into an artificial finite-depth bound.
5. Keep Gate B frozen unless Gate A closes or the new rank-tail ladder yields a directly reusable radius-3 hypothesis.

A strong RL67 result would eliminate one of the remaining odd-`k` terminal-tail classes or derive an exact recurrence for the previous active rank that closes the small-`g` case. A meaningful partial result would turn (9.1) into a genuine size restriction on `N` or on the previous height-one canonical state.
