# Collatz R# RL-11 — Canonical Mixed Radius-3 Geometry and Complete Mixed-Branch Closure

**Date:** 2026-08-20  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Parent:** RL-10  
**Verdict:** **RL remains open. Radius 3 remains open only in same-direction branches.** RL-11 proves a canonical binary-window normal form for every mixed radius-3 self-rotation and then excludes the entire mixed branch. The infinite tail of the exclusion uses the published Laurent–Mignotte–Nesterenko explicit lower bound for a linear form in two logarithms; the remaining finite range is checked exactly by the included standard-library verifier.

---

## 1. Inherited state

From RL-10, let

`D = 2^A - 3^L > 1`,

and suppose a parity word `d` and a distinct rotation `d' = tau^m d` are at exact cyclic adjacent-transposition distance `3`.

RL-L62 gives exactly three nonzero unit-flow edges. RL-L63 already excludes the connected `[3]` support. RL-L66 gives the discrepancy recurrence

`H_(i+m) = H_i + e + A G_i`,

where

`e = A P_m - mL in {+/-1,+/-3}`.

The mixed direction branch is `e=+/-1`, hence

`gcd(A,L)=gcd(A,m)=1`.

RL-L64 supplies a unit `theta (mod D)` with

`theta^L = 2`, `theta^A = 3`,

and RL-L67 reduces the mixed branch to three sparse trinomials in

`rho = theta^(-1)`.

RL-11 shows that those three trinomials are cyclic presentations of one canonical equation with strong geometric bounds.

---

## 2. RL-L68 — binary sliding-window identity and the canonical triangle

Normalize to `e=+1`. Read cyclic prefix edges in rotation order

`i_t = i_0 + tm (mod A)`,

and write

`g_t = G_(i_t)`.

Since summing RL-L66 around the one rotation orbit gives

`sum_t G_(i_t) = -1`,

the three nonzero `g_t` values consist of two `-1` events and one `+1` event.

Because

`A P_m - mL = 1`,

we have

`mL == -1 (mod A)`,

so natural adjacency `i -> i+1` corresponds in rotation time to

`t -> t-L (mod A)`.

Let

`b_t = d_(i_t)`.

The elementary identity

`d_(i+m)-d_i = G_(i+1)-G_i`

becomes

`b_(t+1)-b_t = g_(t-L)-g_t`.                                  (R68.1)

Now define

`c_t = - sum_(r=1)^L g_(t-r)`.                               (R68.2)

Then `c_(t+1)-c_t` equals the right side of (R68.1). Also

`sum_t c_t = -L sum_t g_t = L = sum_t b_t`.

Hence the additive constant is zero and

> `b_t = - sum_(r=1)^L g_(t-r)` for every `t`.               (R68.3)

Thus binary solvability is equivalent to every cyclic length-`L` window of the three-event sequence having sum `0` or `-1`.

### 2.1 Canonical event order

Cyclically choose the negative event immediately preceding the positive event as time `0`. Then the three events are

`g_0=-1`, `g_x=+1`, `g_s=-1`,

with

`0 < x < s < A`.                                             (R68.4)

For an event at `q`, let

`I(q) = {q+1,...,q+L} (mod A)`.

Equation (R68.3) becomes the indicator identity

`b = 1_(I(0)) + 1_(I(s)) - 1_(I(x))`.                       (R68.5)

For `b` to be binary, exactly two set inclusions are required:

`I(x) subset I(0) union I(s)`,                               (R68.6)

`I(0) intersect I(s) subset I(x)`.                           (R68.7)

If `s>A-L`, the interval `I(s)` wraps around the origin and the initial overlap `I(0) intersect I(s)` is strictly longer than the wrapped initial part of `I(x)` because `x<s`; (R68.7) fails. Therefore

`s <= A-L`.                                                   (R68.8)

With no wrap remaining, if `s>L`, then `I(0)` and `I(s)` are separated by a gap while `I(x)`, with `0<x<s`, necessarily meets that gap; (R68.6) fails. Therefore

`s <= L`.                                                     (R68.9)

Conversely, if

`0<x<s<=min(L,A-L)`,

all three intervals are non-wrapping, `I(0) union I(s)` is contiguous, `I(x)` lies inside that union, and the overlap `I(0) intersect I(s)` lies inside `I(x)`. Hence (R68.6)-(R68.7) hold.

Therefore:

> **RL-L68. In the mixed `e=+1` branch, after cyclic normalization the three jump times are exactly**
>
> `-1, +1, -1` at `0<x<s`,
>
> **and binary solvability is equivalent to**
>
> `0 < x < s <= min(L,A-L)`.                                 (R68.10)

The `e=-1` case is the reversed orientation.

**Status: PROVED ANALYTIC THEOREM.**

---

## 3. RL-L69 — the three RL-10 sparse forms are one canonical trinomial

RL-L67 gave, depending on where the cyclic cut lands, one of

`rho^a + 3rho^b - 3rho^c = 0`,

`rho^a - rho^b + rho^c = 0`,

`-rho^a + rho^b + 3rho^c = 0`.                              (R69.1)

But

`rho^A = theta^(-A) = 1/3`.                                  (R69.2)

If the sign order is already `(-,+,-)`, divide by the first power of `rho`.

If the cut gives `(-,-,+)`, start instead at the second negative event. The wrapped earlier negative contributes

`(1/3) rho^(a-b) = rho^(A+a-b)`.

If the cut gives `(+,-,-)`, start at the second negative event and use the same identity for both wrapped terms.

In every case the sparse relation becomes, up to multiplication by a unit,

> `1 - rho^x + rho^s == 0 (mod D)`,                          (R69.3)
>
> with `0<x<s<=min(L,A-L)`.

Conversely, this canonical relation is exactly the RL-L67 geometric-sum divisibility criterion in the normalized event coordinates.

Therefore:

> **RL-L69. Every mixed radius-3 `D|Q` self-rotation is equivalent to one canonical trinomial (R69.3) in the sharp triangle (R68.10).**

**Status: PROVED ANALYTIC REDUCTION.**

---

## 4. RL-L70 — exact `[2,1]` boundary geometry

In the mixed branch the only same-sign pair is the two negative events. Hence a `[2,1]` support occurs exactly when those two negative flow edges are naturally adjacent.

Natural adjacency changes rotation time by `-L mod A`, so the two negative event times `0,s` are adjacent iff

`s in {L,A-L}`.

Together with `s<=min(L,A-L)`, this forces

> `s = min(L,A-L)`.                                          (R70.1)

The source middle bit of the length-two transport is also forced.

### 4.1 `L<A/2`

Then `s=L`. In natural edge order the negative pair is `t=s` followed by `t=0`; the middle source bit is `b_s`. From (R68.5),

`b_s = 1 - 1 = 0`.

Hence the local move is

`100 -> 001`,                                                 (R70.2)

whose RL-10 length-two coefficient is `3`.

### 4.2 `L>A/2`

Put `B=A-L`, so `s=B`. The natural pair is `t=0` followed by `t=B`; the middle source bit is `b_0`. The interval `I(B)` ends at `0 mod A`, while neither `I(0)` nor `I(x)` contains `0`, so

`b_0=1`.

Hence the local move is

`110 -> 011`,                                                 (R70.3)

whose length-two coefficient is `5`.

Therefore:

> **RL-L70. The disconnected `[2,1]` mixed branch has no free local shape: it is `100->001` when `L<A/2`, and `110->011` when `L>A/2`.**

**Status: PROVED ANALYTIC THEOREM.**

---

## 5. RL-L71 — elementary elimination of the `s=L` boundary

Assume `L<A/2`, so `s=L`. The canonical relation gives

`rho^x = 1 + rho^L = 1 + 1/2 = 3/2`.                        (R71.1)

Also

`rho^(A-L)=rho^A/rho^L=(1/3)/(1/2)=2/3`.

Hence

`rho^(A-L+x)=1`.                                              (R71.2)

Raising to the `L`th power and using `rho^L=1/2` gives

`2^(A-L+x) == 1 (mod D)`,

so

`D | 2^(A-L+x)-1`.                                           (R71.3)

But `x<L`, so

`A-L+x <= A-1`.                                              (R71.4)

And `L<A/2` implies `L<=(A-1)/2`, hence

`3^L < 2^(A-1)`,

so

`D=2^A-3^L > 2^(A-1)`.                                      (R71.5)

Therefore

`0 < 2^(A-L+x)-1 < 2^(A-1) < D`,

contradicting (R71.3).

Thus the entire `L<A/2` `[2,1]` branch is impossible.

**Status: PROVED ANALYTIC THEOREM.**

---

## 6. RL-L72 — resultant/AM-GM denominator barrier for every remaining mixed case

After RL-L71, every remaining canonical mixed case has

`s < L`, `s <= B=A-L`.                                      (R72.1)

Let

`F(X)=1-X^x+X^s`,

`f(X)=2X^L-1`.                                                (R72.2)

Modulo `D`, the canonical unit `rho` satisfies both

`F(rho)=0`, `f(rho)=0`.                                      (R72.3)

Hence

`D | Res(F,f)`.                                               (R72.4)

The resultant is nonzero. Indeed, the reciprocal of `f` is, up to sign,

`X^L-2`,

which is Eisenstein at `2`, so `f` is irreducible over `Q`. Since `deg F=s<L`, `F` and `f` cannot share a complex root.

Let

`r=2^(-1/L)`

and let `zeta` run over the `L`th roots of unity. The roots of `f` are `r zeta`, so

`|Res(F,f)| = 2^s product_zeta |1-r^x zeta^x+r^s zeta^s|`.   (R72.5)

Because `0<x<s<L`, root-of-unity orthogonality gives

`(1/L) sum_zeta |1-r^x zeta^x+r^s zeta^s|^2`

` = 1+r^(2x)+r^(2s) < 3`.                                   (R72.6)

AM-GM applied to the squared absolute values yields

`|Res(F,f)| < 2^s 3^(L/2) <= 2^B 3^(L/2)`.                 (R72.7)

Since the nonzero resultant is divisible by `D`,

> `D < 2^B 3^(L/2)`.                                        (R72.8)

Equivalently, with

`delta = D/2^A = 1-3^L/2^A`,

> `0 < delta < (sqrt(3)/2)^L`.                              (R72.9)

Thus any remaining mixed radius-3 survivor would force an exponentially small denominator defect.

**Status: PROVED ANALYTIC THEOREM.**

---

## 7. RL-L73 — complete mixed radius-3 exclusion using LMN + exact finite certificate

Set

`Lambda = A log 2 - L log 3 > 0`.                            (R73.1)

Then

`delta = 1-exp(-Lambda)`.                                    (R73.2)

For `L>=5`, (R72.9) gives `delta<1/2`, hence

`Lambda = -log(1-delta) < delta/(1-delta) < 2delta`

`< 2 (sqrt(3)/2)^L`.                                         (R73.3)

So with

`c = log(2/sqrt(3))`,

`log Lambda < log 2 - cL`.                                   (R73.4)

### 7.1 External explicit two-logarithm lower bound

RL-11 uses the published Laurent–Mignotte–Nesterenko estimate for

`Lambda=b1 log a1-b2 log a2 !=0`:

`log|Lambda| >= -22 M^2 log H(a1) log H(a2)`,                (R73.5)

where

`M=max(log(|b1|/log H(a2)+|b2|/log H(a1))+0.06,21)`.         (R73.6)

Apply it to

`a1=2`, `a2=3`, `b1=A`, `b2=L`.

From `delta<1/2`, `A` is the least integer with `2^A>3^L`, so certainly `A<=2L`. Hence

`A/log3 + L/log2 < 4L`.                                      (R73.7)

The included verifier certifies the safe numerical inequalities

`log2<0.694`, `log3<1.099`,

`c>0.1438`,

and checks at `L=52000` that both possible LMN branches are already strictly stronger than (R73.4):

- the `M=21` lower-bound magnitude is `<7400`;
- `cL-log2 >7476`;
- the logarithmic `M` branch has magnitude `<2600` at `L=52000`, and its ratio to `L` decreases thereafter.

Therefore

> any remaining mixed survivor has `L<52000`.                (R73.8)

### 7.2 Exact finite denominator-barrier certificate

For `L>=5`, (R72.9) also forces `A` to be the least exponent with `2^A>3^L`. The verifier scans all `L<52000` exactly using integer arithmetic and the squared form of (R72.8):

`D^2 < 2^(2B) 3^L`.                                         (R73.9)

After imposing `gcd(A,L)=1` and the existence of a canonical triple with `s<L`, the only parameter pairs surviving the coarse denominator barrier are

`(A,L,B,D) =`

`(5,3,2,5)`,

`(7,4,3,47)`,

`(8,5,3,13)`,

`(13,8,5,1631)`,

`(27,17,10,5077565)`.                                       (R73.10)

For each of these five pairs, the verifier constructs `rho` from the Bézout common base and checks every

`0<x<s<=min(L,B)`, `s<L`.

There are `62` such canonical triples in total, and none satisfies

`1-rho^x+rho^s == 0 (mod D)`.                               (R73.11)

Combining RL-L71 with RL-L72 and this exact finite certificate gives:

> **RL-L73. No `D`-divisible mixed-direction exact radius-3 self-rotation exists.**

This closes both disconnected mixed support types `[2,1]` and `[1,1,1]`.

**Status: PROVED THEOREM USING ONE EXTERNAL PUBLISHED LMN ESTIMATE + EXACT FINITE CERTIFICATE.**

---

## 8. RL-L74 — same-direction one-orbit arc-cover normal form

RL-11 also records a structural lemma for the next branch.

Assume

`e=+3`, `gcd(A,L)=gcd(A,m)=1`.

All three nonzero flow values are `-1`. Let

`kappa = m^(-1) (mod A)`,

and choose `r in {1,...,A-1}` with

`r == -kappa (mod A)`.                                      (R74.1)

Since

`mL == -3 (mod A)`,

we have

`3r == L (mod A)`.                                           (R74.2)

If the three negative events occur at times `q1,q2,q3`, let

`I_r(q)={q+1,...,q+r} (mod A)`

and let `u_t` be the number of these three arcs covering `t`.

The bit recurrence is

`b_(t+1)-b_t = g_(t-r)-g_t`,                                 (R74.3)

so `u_t` has the same discrete derivative as `b_t`. Write

`3r = L + jA`, `j in {0,1,2}`.                               (R74.4)

Because `sum u_t=3r` and `sum b_t=L`,

> `b_t = u_t-j`.                                             (R74.5)

Therefore binary solvability is equivalent to

> `u_t in {j,j+1}` for every `t`.                            (R74.6)

So:

- `j=0`: the three `r`-arcs are pairwise disjoint;
- `j=1`: every point is covered once or twice;
- `j=2`: every point is covered twice or three times; equivalently the three complementary arcs are pairwise disjoint.

Natural adjacent flow edges correspond exactly to event times separated by `r` modulo `A`.

This converts the remaining coprime same-direction one-orbit branch from an arbitrary three-event placement into an equal-arc covering problem.

**Status: PROVED ANALYTIC STRUCTURAL THEOREM.**

---

## 9. Radius-3 status after RL-11

The mixed branch is now closed.

The only analytically unresolved exact radius-3 branches are same-direction (`e=+/-3`):

1. `gcd(A,L)=1`, `gcd(A,m)=1`: RL-L67's sparse form

   `sigma^a+3sigma^b+9sigma^c == 0 (mod D)`,

   now supplemented by RL-L74's equal-arc cover geometry;

2. `gcd(A,L)=1`, `gcd(A,m)=3`: the three-orbit branch not yet reduced to one sparse norm;

3. `gcd(A,L)=3`: the cubic-cofactor branch, including the finite nonprimitive survivor `(10)^3` already identified in RL-10.

The connected `[3]` geometry remains excluded by RL-L63, so all remaining same-direction work is disconnected.

---

## 10. Strategic consequence

RL-11 removes the highest-priority RL-10 target completely. There is no reason to revisit the three mixed sparse trinomials.

The best next attack is now:

1. combine RL-L74's equal-arc cover cases with

   `sigma^a+3sigma^b+9sigma^c=0`

   to derive a canonical same-direction sparse form with bounded gap geometry;

2. examine whether a resultant/linear-forms barrier analogous to RL-L72 can be obtained after exploiting that geometry;

3. derive the `gcd(A,m)=3` three-orbit analogue;

4. attack `gcd(A,L)=3` via the cubic factorization

   `2^(3a)-3^(3ell)`

   `=(2^a-3^ell)(2^(2a)+2^a3^ell+3^(2ell))`,

   aiming to force an exact third-repeat.

---

## 11. External dependency and guardrails

- **RL remains open.**
- **Radius 3 remains open in same-direction branches.**
- RL-L68 through RL-L72 and RL-L74 are self-contained analytic results within the inherited framework.
- RL-L73 uses the published Laurent–Mignotte–Nesterenko explicit estimate for a nonzero linear form in two logarithms and an exact finite integer certificate through `L<52000`.
- The finite scan is not being promoted by itself to an infinite theorem; the LMN estimate supplies the infinite cutoff.
- The LMN source and exact formula used are recorded in `EXTERNAL_SOURCES.md`.
- The inherited finite survivor `(10)^3` lies in the same-direction `gcd(A,L)=3` branch, not in the mixed branch.
