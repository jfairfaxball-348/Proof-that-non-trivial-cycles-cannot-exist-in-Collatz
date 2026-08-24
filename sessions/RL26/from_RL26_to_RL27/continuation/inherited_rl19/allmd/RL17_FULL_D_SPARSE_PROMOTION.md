# RL17 — Full-discrepancy promotion of the cubic sparse relation

## Status

**Analytic lemma, newly frozen in RL17.**

This strengthens RL-L104 from the cubic cofactor `C` to the full discrepancy `D`.  It does not prove sparse uniqueness.

## 1. Normalization

Assume

\[
A=3a,\qquad L=3\ell,\qquad \gcd(a,\ell)=1,
\]

and the one-orbit same-direction radius-3 condition

\[
\gcd(A,m)=1,\qquad ap-m\ell=1,
\]

where `p=P_m`.

Set

\[
X=2^a,\qquad Y=3^\ell,
\]

so

\[
D=X^3-Y^3=(X-Y)C,
\qquad
C=X^2+XY+Y^2.
\]

Modulo `D`, define

\[
\omega=XY^{-1},
\qquad
\theta=2^{-m}3^p,
\qquad
\rho=\theta^{-1}=2^m3^{-p}.
\]

All inverses exist because `D` is coprime to 6.

Since `X^3=Y^3 (mod D)`,

\[
\omega^3=1\pmod D.
\]

Unlike modulo `C`, we do **not** assume `1+omega+omega^2=0`.

## 2. Bezout identities still hold modulo D

From `ap-mell=1`,

\[
\theta^a
=2^{-am}3^{ap}
=3\left(\frac{Y}{X}\right)^m
=3\omega^{-m}\pmod D,
\]

and similarly

\[
\theta^\ell=2\omega^{-p}\pmod D.
\]

For a prefix index `i`, with

\[
K_i=aP_i-i\ell,
\qquad
T_i=pi-mP_i,
\]

the same determinant identity gives

\[
i=mK_i+aT_i,
\]

and therefore

\[
2^i3^{-P_i}=\theta^{-K_i}\omega^{T_i}\pmod D.
\]

## 3. One-orbit phase cancellation needs only omega^3=1

Read indices in rotation order `i_t=tm mod 3a`.  If `N_t` counts the three same-direction jumps already passed, the radius-3 recurrence gives

\[
K_{i_t}\equiv t-aN_t\pmod{3a},
\]

and the determinant identity gives

\[
T_{i_t}\equiv mN_t\pmod3.
\]

Using `theta^a=3omega^{-m}` and `omega^3=1`,

\[
2^{i_t}3^{-P_{i_t}}
=\theta^{-K_{i_t}}\omega^{T_{i_t}}
\equiv 3^{N_t}\rho^t\pmod D.
\]

Thus the RL-L104 phase cancellation survives on the full modulus.

## 4. Telescoping the four blocks

Let the three jump times be

\[
\alpha<\beta<\gamma,
\]

and define

\[
S=\sum_{t=0}^{3a-1}3^{N_t}\rho^t.
\]

From `theta^a=3omega^{-m}` and `omega^3=1`,

\[
27\rho^{3a}=1\pmod D.
\]

The same four-block geometric telescoping used in RL-L104 therefore gives

\[
(1-\rho)S
\equiv
2\rho\left(
\rho^\alpha+3\rho^\beta+9\rho^\gamma
\right)
\pmod D.
\]

The standard `Q` geometric-sum identity also holds modulo `D`:

\[
4Q(d)\equiv3^L S\pmod D.
\]

If `D|Q(d)`, then `S=0 (mod D)` because `3^L` and 4 are units modulo `D`.  Hence

\[
2\rho\left(
\rho^\alpha+3\rho^\beta+9\rho^\gamma
\right)=0\pmod D.
\]

Since `2rho` is a unit,

\[
\boxed{
D\mid Q(d)
\Longrightarrow
\rho^\alpha+3\rho^\beta+9\rho^\gamma\equiv0\pmod D.
}
\]

This is the full-D promotion.

## 5. Equal spacing becomes arithmetically rigid

If the cyclic jump gaps are exactly `a,a,a`, then after factoring a unit the sparse expression is

\[
1+3\rho^a+9\rho^{2a}
\equiv
1+\omega^m+\omega^{2m}
\pmod D.
\]

Because `gcd(3a,m)=1`, `m` is not divisible by 3, so the right side equals

\[
1+\omega+\omega^2
=
\frac{X^2+XY+Y^2}{Y^2}
=C Y^{-2}
\pmod D.
\]

Therefore an equal-gap sparse zero modulo `D` forces `D|C`.  Since

\[
D=(X-Y)C>0,
\]

we get

\[
X-Y=1,
\qquad
2^a-3^\ell=1.
\]

If `a>=3`, reduction modulo 8 would require `3^ell=7 (mod 8)`, impossible because powers of 3 modulo 8 are only 3 and 1.  Hence `a=2`, and then `ell=1`.

Thus

\[
\boxed{
\text{equal-gap full-D sparse zero}
\Longrightarrow
(a,\ell)=(2,1).
}
\]

This is the nonprimitive third-repeat exception.

## 6. What remains open

The missing infinite theorem is not the equal-gap consequence; it is **uniqueness**:

\[
1+3\rho^u+9\rho^{u+v}=0\pmod D
\Longrightarrow
u=v=w=a
\]

for positive `u+v+w=3a`, with the genuine rotation-geometry constraints.

The finite `a<=80` experiment strongly supports this but does not prove it.
