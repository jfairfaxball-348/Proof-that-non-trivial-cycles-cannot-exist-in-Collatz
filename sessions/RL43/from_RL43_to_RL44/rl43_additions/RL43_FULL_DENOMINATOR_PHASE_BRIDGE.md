# RL43 — full-denominator phase bridge for the one-excursion branch

Date: 2026-08-22

## Status

Sections 1–6 are **ANALYTIC** in the inherited near-resonant order-2 / `g=2`, `G=4` one-excursion branch.  Section 7 gives an exact explicit countermodel showing why the earlier proper-factor resultant alone cannot close the branch.  The companion verifier checks the identities and the countermodel from source.

This note sharpens the radius-3 bridge in an important way:

> the proper factor `X+Y` is not enough; full `D=(X-Y)(X+Y)` divisibility supplies a second, nondegenerate sparse phase relation modulo `X-Y`.

The inherited RL21 work already established the simultaneous factor decomposition

`X-Y | U+V`,   `X+Y | U-V`,

and showed that the `X+Y` condition by itself is insufficient.  Sections 1–2 below are the `G=4` one-sided rewriting of that inherited decomposition.  **The new RL43 content begins with the defect-controlled run/phase compression in Sections 3–6.**

For one excursion that second relation has support controlled by excursion excess.

## 1. Half-word factorization of full divisibility

Retain

`X=2^a`, `Y=3^ell`, `F_+=X+Y`, `F_-=X-Y`,

with `X>Y`, `gcd(a,ell)=1`, and equal-weight half words `u,v` of length `a`, weight `ell`.

Let

`U=Q(u)`, `V=Q(v)`.

In the `G=4` branch the inherited proper-factor identity is

`U-V=F_+ G`, with `G=4`.                                  (R43F.1)

For concatenation in the inherited `Q` convention,

`Q(uv)=Y U + X V`.

Insert (R43F.1):

`Q(uv)=Y(V+F_+G)+XV`

`      =F_+(V+YG)`.                                       (R43F.2)

Because `X` is even and `Y` is odd, both `F_+` and `F_-` are odd, and

`gcd(F_+,F_-)=1`.

Therefore

> **`D | Q(uv)` iff `F_- | V+YG`.**                        (R43F.3)

This is the missing factor condition hidden by the proper-factor equation.

The same conclusion is obtained from `Q(vu)`; the two full numerators differ by `DG`.

## 2. The exact phase modulo `X-Y`

Choose integers `m_0,p_0` with

`a p_0 - m_0 ell = 1`,                                    (R43F.4)

and define the unit

`rho = 2^(m_0) 3^(-p_0) (mod F_-)`.

Since `X/Y=1 (mod F_-)`, (R43F.4) gives

> **`rho^a = 1/3 (mod F_-)`,**
>
> **`rho^ell = 1/2 (mod F_-)`.**                           (R43F.5)

More generally, for all integers `i,j`, the determinant identity gives

`2^i 3^(-j)`

`=(X/Y)^(p_0 i-m_0 j) rho^(a j-ell i)`.

Hence modulo `F_-`,

> **`2^i 3^(-j) = rho^(a j-ell i)`.**                     (R43F.6)

This is exactly the sort of Bezout phase conversion used in the closed radius-3 proof.

## 3. Run compression of a half numerator

Let one maximal run of `k` ones in `v` start at bit position `t` and at global odd rank `m` (one-based).

After division by `Y=3^ell`, that run contributes

`sum_(s=0)^(k-1) 2^(t+s) 3^(-(m+s))`

`=3[2^t 3^(-m) - 2^(t+k)3^(-(m+k))]`.                    (R43F.7)

Define the two determinant exponents

`b = a m - ell t`,

`c = a(m+k)-ell(t+k)`.

Then

`c-b = k(a-ell)>0`.                                        (R43F.8)

By (R43F.6), modulo `F_-` the run contributes

> **`3(rho^b-rho^c)`.**                                   (R43F.9)

## 4. Why the exponents are positive in the inherited branch

For the two initial common odd ranks positivity is immediate.

Every later run starts at a moved rank on the earlier `v` side of the unique positive excursion.  If its position is `j_m`, the inherited RL42 prefix cap on the later positive rank `i_m` gives

`2^(j_m)/3^(m-1) <= 2^(i_m)/3^(m-1) <= zeta^2 < 3`,

where `zeta=X/Y` and `zeta^2<16/15`.

Thus

`2^(j_m) < 3^m`.

Since also `3^ell<2^a`, raising these inequalities to powers `ell` and `m` gives

`2^(ell j_m) < 3^(ell m) < 2^(a m)`.

Therefore

> **`a m-ell j_m>0`.**                                    (R43F.10)

So every run-start exponent `b` is a positive integer, and every `c>b` is positive as well.

## 5. Defect controls the phase support

Write the unique local excursion as `alpha,beta`, with common local weight `p`, length `h`, and excess `e`.  Let

`z_0=h-p`

be the number of zero columns in each local word.

The RL43 defect lemma gives

`z_0<=e+1`.                                                 (R43F.11)

In the one-excursion `G=4` branch, the full half word `v` consists of

- the two common leading odd bits `11`;
- the local word `beta`, which begins with `1` and ends with `0`;
- a terminal synchronized all-zero suffix.

The leading `11` merges into the first 1-run of `beta`, and the trailing zeros create no new 1-run.  Since `beta` has `z_0` zeros and ends with zero, the number `R` of maximal 1-runs in the full half word satisfies

> **`R<=z_0<=e+1`.**                                       (R43F.12)

Now divide (R43F.3) by the unit `Y` and insert the run decomposition (R43F.9).  Full `D`-divisibility forces

> ## **One-excursion full-denominator phase relation**
>
> **`G + 3 sum_(r=1)^R (rho^(b_r)-rho^(c_r)) = 0 (mod X-Y)`,**
>
> **with `R<=e+1`.**                                       (R43F.13)

For the live branch `G=4`, this is

`4+3 sum (rho^b-rho^c)=0 (mod X-Y)`.                       (R43F.14)

Its support is at most

> **`2e+3` terms.**                                        (R43F.15)

Unlike the earlier proper-factor relation, (R43F.14) uses the **missing factor `X-Y`**, so it genuinely remembers full denominator divisibility.

## 6. Nondegenerate radius-3-style resultant

Form

`P(T)=G+3 sum_(r=1)^R (T^(b_r)-T^(c_r))`                  (R43F.16)

and

`B_-(T)=3T^a-1`.                                           (R43F.17)

By (R43F.5) and (R43F.13), `rho (mod X-Y)` is a common root, so the integer resultant satisfies

> **`X-Y | Res(B_-,P)`.**                                  (R43F.18)

This resultant is **nonzero**.

Indeed, `B_-(T)` is irreducible over `Q`: its reciprocal is `T^a-3`, Eisenstein at 3.  If the resultant vanished, `B_-` would divide `P` over `Q`.

Let

`s=3^(-1/a) in (0,1)`

be the positive real root of `B_-`.  By (R43F.8) and positivity of all `b_r`,

`s^(b_r)-s^(c_r)>0`.

Hence

`P(s)>G>0`,

contradiction.

Therefore

> ## **`0 != Res(3T^a-1,P(T))`, and `X-Y` divides it.**     (R43F.19)

There is a sharper, shorter binomial.  Put

`q=a-ell`.

Dividing the two phase identities in (R43F.5) gives

> **`3 rho^q = 2 (mod X-Y)`.**                              (R43F.20)

Thus `rho` is also a common root modulo `X-Y` of

`C_-(T)=3T^q-2`                                            (R43F.21)

and `P(T)`, so

> **`X-Y | Res(3T^q-2,P(T))`.**                            (R43F.22)

This shorter resultant is again nonzero.  The reciprocal polynomial `2T^q-3` is Eisenstein at 3, hence `3T^q-2` is irreducible.  If the resultant vanished, `3T^q-2` would divide `P`.  At its positive root

`s=(2/3)^(1/q) in (0,1)`,

all paired differences `s^b-s^c` are positive, so again `P(s)>G>0`, a contradiction.  Hence

> ## **`0 != Res(3T^q-2,P(T))`, `q=a-ell`, and `X-Y` divides it.**  (R43F.23)

This is especially significant because **`3T^q-2` is exactly the short Bezout binomial used in the inherited RL19 exact-radius-3 `k=1` extreme sector.**  The arbitrary-radius one-excursion branch has therefore been reduced to a sparse phase polynomial against the same binomial anchor that already appears in the closed radius-3 proof.

The remaining difference is quantitative: here `P` may have up to `2e+3` terms and larger determinant exponents, whereas radius 3 had uniformly tiny support.

## 7. Exact countermodel to the bare proper-factor bridge

The inherited RL21 analysis had already proved that the proper-factor relation alone is not strong enough.  The following RL43 example specializes that obstruction to the **one-excursion near-resonant geometry**, so it directly tests the present bridge.

The companion verifier constructs the explicit half words

`u = 11000101111111111111110011101010101010101010101010101010101010111`,

`v = 11101001111111111111110110101010101010101010101010101010101010110`.

They have

`a=65`, `ell=41`, `gcd(a,ell)=1`,

and satisfy the required near-resonance window

`1 < 2^65/3^41`,

`15*2^130 < 16*3^82`.

They share exactly the inherited two leading odd bits and then form one canonical positive excursion with

`p=39`, `rho_exc=65`, `e=26`.

Their proper-factor numerator satisfies exactly

> **`U-V=4(2^65+3^41)`.**                                 (R43F.24)

The full 130-bit word `uv` is primitive.

However

> **`D does not divide Q(uv)`.**                            (R43F.25)

Equivalently, `X-Y` does not divide `V+4Y`, and the phase polynomial (R43F.14) is nonzero modulo `X-Y`.

This is **not an RL counterexample**; it deliberately fails the global `D|Q` condition.  Its role is diagnostic:

> **near resonance + primitivity + one-excursion geometry + the sparse `X+Y` proper-factor identity do not by themselves close the branch.**

The missing ingredient is exactly the new `X-Y` phase relation (R43F.14).

## 8. Strategic consequence

The live radius-3 bridge should now be formulated as a **two-factor bridge**, not as proper-factor sparse uniqueness alone:

1. `X+Y` is controlled by the sparse excursion-difference relation;
2. `X-Y` is controlled by the new sparse half-numerator phase relation;
3. the second relation yields nonzero resultants against both `3T^a-1` and, more sharply, the short binomial `3T^(a-ell)-2`; the latter is the same anchor used in the RL19 radius-3 `k=1` sector.

For one excursion, the hard target is now precise:

> exploit the paired phase polynomial
>
> `4+3 sum(T^b-T^c)`
>
> with `R<=e+1`, the ordering `0<b<c`, the physical gap automaton, and the near-resonant Bezout data to contradict `X-Y | Res(3T^(a-ell)-2,P)`.

This is materially closer to the analytic machinery that closed exact radius 3 than the previous arbitrary sparse `2^r3^s` resultant.
