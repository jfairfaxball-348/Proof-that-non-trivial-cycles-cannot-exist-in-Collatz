# RL-15 — Complete closure of the coprime `j=1, P3, [1,1,1]` strict interior

Date: 2026-08-20

## Verdict

This note closes the entire coprime one-orbit same-direction

`j=1, P3, [1,1,1]`

strict-interior branch.  In particular, the scalene target left live by RL-14 is impossible.

The proof uses one new short-defect binomial resultant, the same published Laurent–Mignotte–Nesterenko two-logarithm estimate already inherited in RL-11/RL-14, and an exact finite parameter certificate.  No simplex enumeration is needed in the finite step.

RL itself remains open, and radius 3 is not yet completely closed because other same-direction branches remain.

---

## 1. Inherited `j=1, P3` setup

Write

\[
B=A-L,
\qquad
D=2^A-3^L>0,
\qquad
\gcd(A,L)=1,
\]

and assume the `P3` side

\[
A<2L.
\]

For `j=1`,

\[
A+L\equiv0\pmod3.
\]

Let

\[
\tau=\theta^3,
\qquad
\theta^L\equiv2\pmod D,
\qquad
\theta^A\equiv3\pmod D.
\]

A strict `[1,1,1]` simplex has positive gaps

\[
x+y+z=B,
\]

and the reciprocal `P3` congruence is

\[
H_{x,y}(\tau)
=4\tau^{x+y}+6\tau^y+9
\equiv0\pmod D.
\tag{RL15.1}
\]

RL-14 also gives

\[
\tau^B\equiv{27\over8}\pmod D.
\tag{RL15.2}
\]

The three cyclic presentations are equivalent.  Indeed, if `a+b+c=B`, then

\[
{2\over3}\tau^c H_{a,b}(\tau)
\equiv
9+4\tau^{b+c}+6\tau^c
=H_{b,c}(\tau)
\pmod D,
\tag{RL15.3}
\]

using (RL15.2).

---

## 2. RL-L96 — the short-defect binomial `3 tau^h = 4`

Set

\[
C=2L-A.
\]

Since

\[
C=3L-(A+L),
\]

`j=1` implies that `C` is divisible by `3`.  Since `P3` has `A<2L`, write

\[
C=3h,
\qquad h\ge1.
\tag{RL15.4}
\]

Then

\[
B=A-L,
\qquad
L=B+3h,
\qquad
A=2B+3h.
\tag{RL15.5}
\]

More importantly,

\[
\tau^h
=\theta^{3h}
=\theta^{2L-A}
\equiv {4\over3}\pmod D.
\tag{RL15.6}
\]

Thus `tau` is a common root modulo `D` of the short binomial

\[
J_h(X)=3X^h-4
\tag{RL15.7}
\]

and one of the cyclic `P3` trinomials.

This is much shorter than the side-`B` binomial `8X^B-27` used in RL-14.

Also positivity of `D` forces

\[
\left({4\over3}\right)^B>
\left({27\over8}\right)^h.
\tag{RL15.8}
\]

If `h>=B/4`, then the right side is at least `(27/8)^(B/4)`, but

\[
\left({27\over8}\right)^{1/4}>{4\over3}
\]

because

\[
2187>2048.
\]

Hence

\[
\boxed{h<{B\over4}}.
\tag{RL15.9}
\]

Equivalently,

\[
L=B+3h<{7B\over4},
\qquad
B>{4L\over7}.
\tag{RL15.10}
\]

> **RL-L96.** Every coprime `j=1,P3` parameter pair has a short modular binomial
> \[
> \boxed{3\tau^h\equiv4\pmod D},
> \qquad h={2L-A\over3}<{B\over4}.
> \]

---

## 3. RL-L97 — a universal short-resultant envelope independent of simplex shape

Take any positive simplex triple `x+y+z=B`.  Choose a largest gap `c`.  By cyclic rotation, use a presentation

\[
H_{a,b}(X)=4X^{a+b}+6X^b+9
\]

which omits `c`.  Put

\[
s=a+b=B-c.
\]

Since `c>=B/3`,

\[
s\le {2B\over3},
\qquad
b\le s.
\tag{RL15.11}
\]

Consider

\[
R_h=\operatorname{Res}(3X^h-4,H_{a,b}).
\tag{RL15.12}
\]

### 3.1 The resultant is always nonzero

If a complex root `alpha` were common to both polynomials, then at a `2`-adic valuation

\[
v_2(\alpha)={2\over h}.
\]

The three terms of `H(alpha)` would have valuations

\[
2+{2s\over h},
\qquad
1+{2b\over h},
\qquad
0.
\]

The minimum is uniquely the constant term.  A nonarchimedean sum with a unique minimum cannot vanish.  Therefore

\[
\boxed{R_h\ne0}.
\tag{RL15.13}
\]

Since `tau` is a common root modulo `D`,

\[
\boxed{D\mid R_h}.
\tag{RL15.14}
\]

### 3.2 Archimedean bound

Every complex root of `3X^h-4` has modulus

\[
r=\left({4\over3}\right)^{1/h}.
\]

Using the product formula for the resultant,

\[
|R_h|
=3^s\prod_{J_h(\alpha)=0}|H_{a,b}(\alpha)|.
\]

For each root,

\[
|H_{a,b}(\alpha)|
\le4r^s+6r^b+9
\le10r^s+9.
\]

Therefore, using (RL15.11),

\[
|R_h|
\le
3^{2B/3}
\left(
10\left({4\over3}\right)^{2B/(3h)}+9
\right)^h
=:U(B,h).
\tag{RL15.15}
\]

This bound is independent of the detailed simplex geometry.  No orthogonality assumption and no residue-class case split are needed.

### 3.3 Uniform exponential margin below `2^A`

Put

\[
\eta={h\over B},
\qquad 0<\eta<{1\over4}.
\]

Since `A=2B+3h`, define

\[
\kappa(\eta)
=(2+3\eta)\log2
-{2\over3}\log3
-\eta\log\left(
10\left({4\over3}\right)^{2/(3\eta)}+9
\right).
\tag{RL15.16}
\]

Then (RL15.15) gives

\[
{U(B,h)\over2^A}
\le e^{-\kappa(\eta)B}.
\tag{RL15.17}
\]

The function `kappa` is decreasing on `(0,1/4]`.  To see this, set

\[
t={2\log(4/3)\over3\eta}
\]

and

\[
g(t)=\log(10e^t+9)-t{10e^t\over10e^t+9}.
\]

Then

\[
g'(t)=-t{90e^t\over(10e^t+9)^2}<0,
\]

and

\[
\lim_{t\to\infty}g(t)=\log10>\log8=3\log2.
\]

Hence

\[
\kappa'(\eta)=3\log2-g(t)<0.
\]

At the endpoint,

\[
\kappa(1/4)
=0.3190179770821818\ldots>0.31.
\tag{RL15.18}
\]

Thus universally

\[
\boxed{|R_h|<2^A e^{-0.31B}}.
\tag{RL15.19}
\]

> **RL-L97.** Every strict `j=1,P3,[1,1,1]` simplex admits a nonzero short resultant divisible by `D` and satisfying (RL15.19).

---

## 4. RL-L98 — complete `j=1,P3,[1,1,1]` strict-interior exclusion

Assume a survivor exists.  From `D|R_h` and (RL15.19),

\[
\delta:={D\over2^A}<e^{-0.31B}.
\tag{RL15.20}
\]

A strict three-gap interior has `B>=3`, so the right side is below `1/2`.  Let

\[
\Lambda=A\log2-L\log3>0.
\]

Since

\[
\delta=1-e^{-\Lambda},
\]

we obtain

\[
\Lambda=-\log(1-\delta)
<{\delta\over1-\delta}
<2\delta.
\]

Therefore

\[
\log\Lambda
<\log2-0.31B.
\tag{RL15.21}
\]

Using `B>4L/7` from RL-L96,

\[
\boxed{
\log\Lambda<\log2-0.177L.
}
\tag{RL15.22}
\]

### 4.1 LMN tail

Use the same published Laurent–Mignotte–Nesterenko estimate already inherited in RL-11/RL-14:

\[
\log|\Lambda|
\ge
-22M^2\log2\log3,
\]

where

\[
M=\max\left(
\log\left({A\over\log3}+{L\over\log2}\right)+0.06,
21
\right).
\]

Since `A<2L`,

\[
{A\over\log3}+{L\over\log2}<4L.
\]

The included verifier checks at

\[
L=42000
\]

that both LMN branches already contradict (RL15.22):

- the `M=21` lower-bound magnitude is `<7400`, while `0.177L-log2>7433`;
- the logarithmic branch is `<2500` at `L=42000`, and its ratio to `L` decreases thereafter.

Hence every hypothetical survivor must have

\[
\boxed{L<42000}.
\tag{RL15.23}
\]

### 4.2 Exact finite certificate

For a survivor, (RL15.20) gives `delta<1/2`.  Therefore, for each fixed `L`, only the least exponent `A` satisfying

\[
2^A>3^L,
\qquad
A+L\equiv0\pmod3
\]

can survive.  Any later congruent exponent is at least `A+3`, making `3^L/2^A<1/8` and hence `delta>7/8`.

The finite check therefore scans only one congruence-compatible `A` per `L`.

To keep the certificate exact, let

\[
S=\left\lfloor{2B\over3}\right\rfloor,
\qquad
q=\left\lceil{S\over h}\right\rceil,
\qquad
N=10\cdot4^q+9\cdot3^q.
\]

From the same triangle estimate,

\[
|R_h|
\le
3^S\left({N\over3^q}\right)^h.
\tag{RL15.24}
\]

Thus a survivor would require the exact integer inequality

\[
D\,3^{qh}
\le
3^S N^h.
\tag{RL15.25}
\]

The standard-library verifier scans every `L<42000`, imposes `P3`, `j=1`, and coprimality, and checks (RL15.25) with exact integers.

It checks

\[
19161
\]

coprime first-congruence parameter pairs and finds

\[
\boxed{0}
\]

finite resultant-barrier survivors.

Therefore:

> **RL-L98.** The complete coprime one-orbit same-direction
> \[
> \boxed{j=1,\ P3,\ [1,1,1]}
> \]
> strict-interior branch is impossible.

This includes every scalene simplex and independently subsumes the equal-gap closure RL-L95.

**Dependency:** the infinite tail uses the same external published LMN theorem already recorded in the RL-11 baseline.  The finite certificate is exact integer arithmetic.

---

## 5. Radius-3 status after RL-15

Closed same-direction/coprime interior pieces now include:

1. `gcd(A,m)=3` same-direction radius-3 branch (RL-12);
2. `j=0, P3, [1,1,1]` one-orbit interior (RL-13);
3. `j=1, P2, [1,1,1]` one-orbit interior (RL-14);
4. **all** `j=1, P3, [1,1,1]` one-orbit interiors (RL-L98).

The strongest live one-orbit targets are now:

- the coefficient-5 `P3 [2,1]` boundary;
- the `j=2, P2` lift;
- the separate `gcd(A,L)=3` cubic-cofactor branch.

The new short-defect identity `3 tau^h=4` should be tested first against the coefficient-5 `P3 [2,1]` boundary, because it does not rely on scalene geometry and may survive boundary degeneration with only a changed sparse polynomial.

## Guardrail

RL remains open.  Radius 3 remains open in the branches listed above.
