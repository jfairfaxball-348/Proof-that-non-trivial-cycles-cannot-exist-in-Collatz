# RL43 — cutoff-free gap-9 excursion automaton

Date: 2026-08-22

## Status

**ANALYTIC REDUCTION + EXACT FINITE CERTIFICATE** in the inherited near-resonant order-2 / `g=2`, `G=4` balanced-return branch.

This note upgrades the earlier exploratory statement

> no incoming-gap-9 positive crossing of excess `e<=7` was seen through `p<=240`

to a **cutoff-free theorem**:

> **Every canonical positive excursion entering with physical odd gap 9 and crossing to the negative side has excess `e>=8`.**

No bound on excursion weight `p`, length `h`, or transport radius is used.

Companion verifier: `verify_rl43_gap9_cutofffree.py`.

## 1. Prefix normalization

For a canonical positive excursion, after `n` processed local columns let

- `p_alpha`, `p_beta` be the two prefix weights;
- `d=p_beta-p_alpha>0` be the internal prefix imbalance;
- `e` be the accumulated excursion excess;
- `S_n` be the normalized local numerator difference used in the RL43 2-adic classifier.

The first canonical column is `(alpha,beta)=(0,1)`, so

`n=1`, `d=1`, `e=0`, `S_1=-1/3`.

Fix an incoming odd physical gap `g`.  Compatibility through `n` columns is

`S_n == g (mod 2^n)`

in the 2-adic integers.  Since every denominator in `S_n` is odd, define

> `T_n := 3^(p_beta) (S_n-g) / 2^n`.

Whenever the prefix is compatible, `T_n` is an ordinary integer.

For `g=9`, the initial state is

`T_1 = 3(-1/3-9)/2 = -14`.

Thus the whole unbounded-length problem starts from the finite integer state

> `(d,e,T)=(1,0,-14)`.

## 2. Exact transition law

Append a bit-pair `(x,y)` with `x,y in {0,1}`.  Then

`d' = d+y-x`,

and the inherited excursion-area bookkeeping gives

`e' = e+d-x`.

The normalized numerator updates by

`S' = S + x 2^n / 3^(p_alpha+1) - y 2^n / 3^(p_beta+1)`.

Using `d=p_beta-p_alpha`, direct substitution into the definition of `T` gives

> **`T' = [3^y T + x 3^(d+y-1) - y]/2`.**                 (R43G.1)

A transition is 2-adically compatible exactly when the numerator in (R43G.1) is even.

Internal excursion states must also satisfy `d'>0`.

The four transitions are therefore

- `00`: `T'=T/2`, excess cost `d`;
- `11`: `T'=(3T+3^d-1)/2`, excess cost `d-1`;
- `01`: `T'=(3T-1)/2`, excess cost `d`;
- `10`: `T'=(T+3^(d-1))/2`, excess cost `d-1`.

The key point is that **none of these formulas depends on `n`, `p_alpha`, `p_beta`, or the total excursion length**.

## 3. Terminal crossing criterion

The canonical terminal column is `(1,0)` from an internal state with `d=1`.  It closes the prefix imbalance to zero.

If the preterminal state is `(1,e,T)`, then

`T_out=(T+1)/2`.

At the completed excursion this is exactly

`T_out = (D_E-3^p g)/2^h`.

Hence a physical positive-to-negative crossing occurs exactly when

> `T` is odd and `(T+1)/2 > 0`,                           (R43G.2)

with outgoing gap magnitude

> `g_out=(T+1)/2`.                                         (R43G.3)

## 4. Why the bounded-excess state search is genuinely finite

Every transition has nonnegative excess cost.  The only zero-cost internal transition is `11` at height `d=1`.

At `d=1`, write

`phi(T)=(3T+2)/2`.

Repeated compatible `11` columns satisfy

`phi^k(T)=3^k(T+2)/2^k - 2`.                               (R43G.4)

Therefore:

- if `T != -2`, at most `v2(T+2)` consecutive zero-cost `11` steps are compatible;
- if `T=-2`, then `phi(T)=-2`, giving one neutral self-loop.

All other internal steps consume at least one unit of excess.  Reaching imbalance height `d` costs at least

`1+2+...+(d-1)=d(d-1)/2`,

so `d` is bounded for fixed `e`.

Consequently, after identifying the single neutral self-loop `(d,T)=(1,-2)`, the state graph below any fixed excess bound is finite.  This is an **infinite-length reduction**, not a scan with a hidden `p` cutoff.

## 5. Exact gap-9 certificate

Starting from

`(d,e,T)=(1,0,-14)`,

the companion verifier exhausts every compatible state with `e<=8`.

State counts by excess ceiling are

```text
E=0: 3 states
E=1: 9
E=2: 18
E=3: 31
E=4: 49
E=5: 72
E=6: 100
E=7: 134
E=8: 180
```

There is **no** terminal state satisfying (R43G.2) with `e<=7`.

At `e=8` the first terminal state is

`(d,e,T)=(1,8,7)`,

which gives

`g_out=(7+1)/2=4`.

Therefore:

> ## **Gap-9 excess theorem**
>
> **Every canonical positive excursion entering with gap `9` and physically crossing to the negative side has `e>=8`.**      (R43G.5)

This is cutoff-free.

## 6. Consequence for the one-excursion branch

In the inherited `G=4` one-excursion branch, the first two common odd columns evolve the physical gap

`4 -> 6 -> 9`.

The unique excursion must then cross to the negative side.  Hence (R43G.5) strengthens the previous analytic floor

`e>=4`

to

> **`e>=8` for every genuine one-excursion return.**        (R43G.6)

This still does not close the one-excursion branch by itself.  Its importance is that the theorem is independent of excursion length and exposes the neutral pump state `T=-2`, which is used in the full-denominator phase bridge.
