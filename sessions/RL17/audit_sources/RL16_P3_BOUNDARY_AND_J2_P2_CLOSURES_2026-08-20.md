# RL-16 — Complete coefficient-5 `P3 [2,1]` boundary closure and complete coprime `j=2, P2` strict-interior closure

Date: 2026-08-20

## Verdict

This note proves two new infinite exclusions in the coprime same-direction radius-3 branch.

1. The entire coefficient-5 `P3 [2,1]` boundary is impossible, for both `j=0` and `j=1`.
2. The entire coprime `j=2, P2, [1,1,1]` strict interior is impossible.

The infinite tails use the same published Laurent–Mignotte–Nesterenko two-logarithm estimate already inherited in RL-11.  All finite remnants are certified exactly by the included standard-library verifier.

These results do **not** prove RL.  The separate `gcd(A,L)=3` cubic-cofactor branch remains live.

---

## 1. Shared setup and the two boundary binomials

As in RL-12--RL-15, put

\[
D=2^A-3^L>0,
\qquad \gcd(A,L)=1,
\]

and choose the common base `theta` modulo `D` with

\[
\theta^L\equiv2,
\qquad
\theta^A\equiv3.
\]

Write

\[
\tau=\theta^3,
\qquad B=A-L.
\]

The `P3 [2,1]` coefficient-5 boundary has two cyclically equivalent presentations

\[
10\tau^t+9\equiv0,
\qquad
4\tau^z+15\equiv0,
\qquad t+z=B,
\tag{RL16.1}
\]

with `t,z>=1`.

The `P2` reciprocal strict-interior form is

\[
H_{x,y}(\tau)=\tau^{x+y}+2\tau^y+4\equiv0,
\qquad x+y+z=L,
\tag{RL16.2}
\]

with `x,y,z>=1`.  Its cyclic presentations satisfy

\[
\tau^c H_{a,b}(\tau)\equiv2H_{b,c}(\tau),
\tag{RL16.3}
\]

because `tau^L=8`.

---

## 2. RL-L99 — the `j=0` boundary minimax barrier

In the `j=0` `P3` branch, `3|L`.  Write

\[
L=3n.
\]

Then

\[
\boxed{\tau^n\equiv2\pmod D}.
\tag{RL16.4}
\]

Let

\[
J_n(X)=X^n-2.
\]

If the first boundary form in (RL16.1) vanishes, then `D` divides the nonzero resultant

\[
R_t=\operatorname{Res}(J_n,10X^t+9),
\]

and if the second vanishes, it divides

\[
R_z=\operatorname{Res}(J_n,4X^z+15).
\]

Both resultants are nonzero: at a `2`-adic valuation a root `alpha` of `J_n` has `v_2(alpha)=1/n`, while the constant terms `9` and `15` are the unique terms of minimal `2`-adic valuation in the respective boundary binomials.

Every complex root of `J_n` has modulus `2^(1/n)`.  Hence

\[
|R_t|\le (10\,2^{t/n}+9)^n,
\qquad
|R_z|\le (4\,2^{z/n}+15)^n.
\tag{RL16.5}
\]

Put

\[
a=2^{t/n},\quad c=2^{z/n},\quad p=ac=2^{B/n}.
\]

Since `A=B+3n`, positivity `2^A>3^L` gives

\[
p>{27\over8}.
\tag{RL16.6}
\]

For fixed `p`, the first base `10a+9` increases with `a`, while the second base `4p/a+15` decreases.  The maximum possible value of their minimum is therefore their crossing value.  Solving

\[
10a+9=4p/a+15
\]

gives

\[
M(p)=12+\sqrt{9+40p}.
\tag{RL16.7}
\]

At `p=27/8`,

\[
M(27/8)=24={64\over9}{27\over8}.
\]

Moreover

\[
{d\over dp}\left({64p\over9}-M(p)\right)
={64\over9}-{20\over\sqrt{9+40p}}>0
\]

for `p>=27/8`.  Therefore, strictly for (RL16.6),

\[
M(p)<{64p\over9}
={8\over9}\,2^{A/n}.
\tag{RL16.8}
\]

Choosing the smaller of the two resultant bounds yields

\[
\boxed{D<2^A\left({8\over9}\right)^n}
=2^A\left({8\over9}\right)^{L/3}.
\tag{RL16.9}
\]

Thus any `j=0` boundary survivor has

\[
\delta={D\over2^A}<\left({8\over9}\right)^{L/3}.
\tag{RL16.10}
\]

### Infinite cutoff and finite certificate

For `L>=18`, (RL16.10) gives `delta<1/2`, hence

\[
\Lambda=A\log2-L\log3=-\log(1-\delta)<2\delta.
\]

Therefore

\[
\log\Lambda<\log2-{L\over3}\log{9\over8}.
\tag{RL16.11}
\]

Using the inherited LMN estimate, the verifier certifies that (RL16.11) is impossible for

\[
L\ge189000.
\]

For `180<=L<189000`, the same bound is strong enough for Legendre's criterion, so `A/L` must be an upper convergent of `log3/log2`.  With `3|L`, the only possibilities are

\[
(A,L)=(485,306),\quad(125743,79335),
\]

and both fail the exact integer form of (RL16.10).

For `L<180`, (RL16.10) first leaves only eight parameter pairs:

\[
(5,3),(7,3),(11,6),(16,9),(29,18),(34,21),(43,27),(62,39).
\]

The verifier checks every boundary position for those pairs: `73` exact tests, with zero congruence zeros.

> **RL-L99.** No coprime `j=0, P3 [2,1]` coefficient-5 boundary solution exists.

---

## 3. RL-L100 — the `j=1` coefficient-5 boundary closes by the RL15 short defect

RL-L96 gives, in `j=1,P3`,

\[
C=2L-A=3h,
\qquad
\tau^h\equiv{4\over3},
\qquad
h<{B\over4}.
\tag{RL16.12}
\]

Use

\[
J_h(X)=3X^h-4.
\]

Let `s=min(t,z)<=B/2`.  If the shorter exponent is `t`, use `10X^t+9`; if it is `z`, use `4X^z+15`.  Since every root of `J_h` has modulus

\[
r=\left({4\over3}\right)^{1/h}>1
\]

and

\[
4r^s+15<10r^s+9,
\]

both cases obey the single bound

\[
|R|\le3^s(10r^s+9)^h.
\tag{RL16.13}
\]

The relevant resultant is nonzero by the same `2`-adic unique-minimum argument used in RL-L97.

Put `eta=h/B`.  Since `s<=B/2`, comparison with `2^A`, where `A=2B+3h`, gives the gap

\[
\kappa(\eta)
=(2+3\eta)\log2-{1\over2}\log3
-\eta\log\!\left(10e^{\log(4/3)/(2\eta)}+9\right).
\tag{RL16.14}
\]

For

\[
g(x)=\log(10e^x+9)-x{10e^x\over10e^x+9},
\]

we have `g'(x)<0` and `g(x)>log 10>3 log 2`, so `kappa'(eta)<0`.  Hence the worst case is `eta=1/4`, where

\[
\kappa(1/4)
={11\over4}\log2-{1\over2}\log3-{1\over4}\log{241\over9}
>0.5349.
\tag{RL16.15}
\]

Thus every boundary survivor would force

\[
\boxed{\delta<e^{-0.53B}}.
\tag{RL16.16}
\]

Since RL-L96 also gives `B>4L/7`,

\[
\delta<e^{-0.302L}.
\tag{RL16.17}
\]

The inherited LMN bound excludes `L>=25000`.  Since `B>=2`, (RL16.16) already has `delta<1/2`, so below the cutoff only the least `A` with `2^A>3^L` can survive.  The exact parameter-only resultant certificate checks `3,800` coprime `j=1` pairs and leaves zero barrier survivors.

> **RL-L100.** No coprime `j=1, P3 [2,1]` coefficient-5 boundary solution exists.

Combining RL-L99 and RL-L100:

> **RL-L101.** The complete coprime coefficient-5 `P3 [2,1]` boundary is impossible.

---

## 4. RL-L102 — the `j=2, P2` short-defect resultant

In the `j=2` branch,

\[
L+2A\equiv0\pmod3.
\]

Since `L+2A=3L+2(A-L)`, this is equivalent to

\[
B=A-L=3h,
\qquad h\ge1.
\tag{RL16.18}
\]

Therefore

\[
\boxed{\tau^h=\theta^{A-L}\equiv{3\over2}\pmod D}.
\tag{RL16.19}
\]

Let

\[
J_h(X)=2X^h-3.
\tag{RL16.20}
\]

For a strict `P2` simplex choose a largest gap `c`.  By (RL16.3), rotate to

\[
H_{a,b}(X)=X^{a+b}+2X^b+4
\]

with

\[
s=a+b=L-c\le{2L\over3}.
\tag{RL16.21}
\]

The resultant

\[
R=\operatorname{Res}(J_h,H_{a,b})
\]

is nonzero.  Indeed, at a `3`-adic valuation a root `alpha` of `J_h` has `v_3(alpha)=1/h`, while in `H(alpha)` the constant term `4` has uniquely minimal valuation.

Every complex root of `J_h` has modulus

\[
r=\left({3\over2}\right)^{1/h},
\]

so

\[
|R|\le2^s(r^s+2r^b+4)^h
\le2^s(3r^s+4)^h.
\tag{RL16.22}
\]

Put `eta=h/L`.  Positivity

\[
2^{L+3h}>3^L
\]

forces

\[
\eta>\eta_0={\log(3/2)\over3\log2}.
\tag{RL16.23}
\]

Using `s<=2L/3`, the normalized gap below `2^A` is

\[
\kappa(\eta)
=\left({1\over3}+3\eta\right)\log2
-\eta\log\!\left(3e^{2\log(3/2)/(3\eta)}+4\right).
\tag{RL16.24}
\]

For

\[
g(x)=\log(3e^x+4)-x{3e^x\over3e^x+4},
\]

`g'(x)<0` and `g(x)<=g(0)=log7<log8=3log2`.  Hence `kappa'(eta)>0`, so the worst case is the positivity threshold `eta_0`.  There the exponential inside is exactly `4`, and

\[
\boxed{\kappa(\eta_0)={1\over3}\log{4\over3}}
>0.0958.
\tag{RL16.25}
\]

Thus any strict-interior `j=2,P2` survivor forces

\[
\boxed{\delta<e^{-0.095L}}.
\tag{RL16.26}
\]

This is the `j=2` analogue of the RL15 short-defect mechanism.

---

## 5. RL-L103 — complete `j=2, P2, [1,1,1]` strict-interior exclusion

For `L>=8`, (RL16.26) gives `delta<1/2`, hence `A` is the least integer with `2^A>3^L` and in particular `A<2L`.  The inherited LMN estimate contradicts (RL16.26) for

\[
L\ge78000.
\]

Below that cutoff the verifier uses an exact rational envelope.  Put

\[
S=\left\lfloor{2L\over3}\right\rfloor,
\qquad
Q=\left\lceil{S\over h}\right\rceil,
\qquad
N=3\cdot3^Q+4\cdot2^Q.
\]

Then (RL16.22) implies the exact necessary condition

\[
D\,2^{Qh}\le2^S N^h.
\tag{RL16.27}
\]

The exact scan checks `11,852` coprime parameter pairs.  Only

\[
(A,L)=(8,5),\qquad(65,41)
\]

survive the coarse resultant envelope.  Direct evaluation of every strict simplex for these two pairs checks respectively `6` and `780` compositions and finds no zero.

> **RL-L103.** No coprime `j=2, P2, [1,1,1]` strict-interior solution exists.

---

## 6. Radius-3 status after RL16

The high-priority coprime one-orbit targets from RL15 are now closed:

- complete `j=1,P3,[1,1,1]` strict interior — RL-L98;
- complete coefficient-5 `P3 [2,1]` boundary — RL-L101;
- complete `j=2,P2,[1,1,1]` strict interior — RL-L103.

The strongest remaining roadmap target is the separate

\[
\boxed{\gcd(A,L)=3\text{ cubic-cofactor branch}.}
\]

A new reduction for its one-rotation-orbit subbranch is recorded in the companion RL16 cofactor note.

## Guardrail

RL remains open.  No claim is made here that every radius-3 branch is closed until the cubic-cofactor branch has been eliminated (and any inherited boundary bookkeeping has been reconciled explicitly).
