# RL-16 — Cubic-cofactor phase cancellation in the `gcd(A,L)=3` one-orbit branch

Date: 2026-08-20

## Status

**New analytic reduction, not yet a closure.**

This note attacks the main branch left after the RL16 coprime closures.  It proves that, modulo the cubic cofactor, the apparent cube-root phase cancels exactly against the three same-direction jump multipliers.  The resulting necessary congruence is again the sparse `1,3,9` three-jump form.

This sharply narrows the remaining `gcd(A,L)=3` target and explains algebraically why an exact third-repeat automatically vanishes on the cubic cofactor.

---

## 1. Cubic factor and scaled discrepancy

Assume

\[
A=3a,\qquad L=3\ell,\qquad \gcd(a,\ell)=1,
\]

and put

\[
X=2^a,\qquad Y=3^\ell,
\]

so

\[
D=X^3-Y^3=(X-Y)C,
\]

where

\[
\boxed{C=X^2+XY+Y^2}
\tag{RL16.C1}
\]

is the cubic cofactor.

Consider a same-direction radius-3 self-rotation, oriented so that

\[
e=A P_m-mL=3.
\]

Then

\[
aP_m-m\ell=1.
\tag{RL16.C2}
\]

Write `p=P_m`.  The ordinary discrepancy is divisible by `3`:

\[
H_i=A P_i-iL=3K_i,
\qquad
K_i=aP_i-i\ell.
\tag{RL16.C3}
\]

For a one-rotation-orbit case `gcd(A,m)=1`, read indices in rotation order

\[
i_t\equiv tm\pmod{3a},\qquad0\le t<3a.
\]

The radius-3 same-direction flow has exactly three jumps `G=-1`.  If `N_t` counts the jumps that occurred before time `t`, then the scaled discrepancy recurrence is

\[
\boxed{K_{i_t}=t-aN_t}.
\tag{RL16.C4}
\]

---

## 2. The cubic root and the natural common base

Modulo `C`, define

\[
\omega=XY^{-1}.
\]

Then

\[
\omega^2+\omega+1\equiv0,
\qquad
\omega^3\equiv1
\pmod C.
\tag{RL16.C5}
\]

Using the natural Bezout identity (RL16.C2), define

\[
\theta=2^{-m}3^p\pmod C,
\qquad
\rho=\theta^{-1}.
\tag{RL16.C6}
\]

A direct calculation gives

\[
\theta^a\equiv3\omega^{-m},
\qquad
\theta^\ell\equiv2\omega^{-p}.
\tag{RL16.C7}
\]

For every prefix index `i`,

\[
2^i3^{-P_i}
\equiv
\theta^{-K_i}\omega^{T_i},
\qquad
T_i=p i-mP_i.
\tag{RL16.C8}
\]

The determinant-one identity (RL16.C2) also gives

\[
i=mK_i+aT_i.
\tag{RL16.C9}
\]

At `i=i_t`, combine (RL16.C4) and `i_t=tm (mod 3a)` to obtain

\[
T_{i_t}\equiv mN_t\pmod3.
\tag{RL16.C10}
\]

Now (RL16.C7) cancels the entire cubic phase:

\[
\theta^{-K_{i_t}}\omega^{T_{i_t}}
=ho^t\theta^{aN_t}\omega^{mN_t}
\equiv
\boxed{3^{N_t}\rho^t}
\pmod C.
\tag{RL16.C11}
\]

This is the key new identity.

---

## 3. RL-L104 — recovery of the sparse `1,3,9` form on the cofactor

The geometric-sum identity for `Q` itself does not require coprimality:

\[
4Q(d)\equiv3^L\sum_{i=0}^{A-1}2^i3^{-P_i}\pmod C.
\tag{RL16.C12}
\]

Using (RL16.C11), write

\[
S=\sum_{t=0}^{3a-1}3^{N_t}\rho^t.
\tag{RL16.C13}
\]

If the three jump times are

\[
\alpha<\beta<\gamma,
\]

then `N_t` takes the successive values `0,1,2,3`.  Also (RL16.C7) implies

\[
27\rho^{3a}\equiv1\pmod C.
\tag{RL16.C14}
\]

Multiplying the four geometric blocks in (RL16.C13) by `1-rho` and using (RL16.C14) gives the exact identity

\[
(1-\rho)S
\equiv
2\rho\bigl(\rho^\alpha+3\rho^\beta+9\rho^\gamma\bigr)
\pmod C.
\tag{RL16.C15}
\]

Since `2rho` is a unit modulo `C`, `C|Q(d)` implies

\[
\boxed{\rho^\alpha+3\rho^\beta+9\rho^\gamma\equiv0\pmod C}.
\tag{RL16.C16}
\]

> **RL-L104.** In the same-direction `gcd(A,L)=3`, `gcd(A,m)=1` radius-3 branch, cubic-cofactor divisibility forces the same sparse `1,3,9` three-jump congruence as in the coprime branch, but now in the cofactor ring and with
> \[
> \rho^a\equiv{1\over3}\omega^m.
> \]

The included finite structural verifier audits the identities (RL16.C4)--(RL16.C16) on `1,359` exact `gcd(A,L)=3` one-orbit structural solutions through `A<25`.

---

## 4. Why exact third-repetition is the singular configuration

From (RL16.C7),

\[
3\rho^a\equiv\omega^m.
\tag{RL16.C17}
\]

If the jump times are exactly separated by `a`,

\[
\beta=\alpha+a,
\qquad
\gamma=\alpha+2a,
\]

then the sparse form factors as

\[
\rho^\alpha
\left(1+3\rho^a+9\rho^{2a}\right)
\equiv
\rho^\alpha(1+\omega^m+\omega^{2m}).
\tag{RL16.C18}
\]

When `gcd(A,m)=1`, `3` does not divide `m`, so `omega^m` is a primitive cubic root and

\[
1+\omega^m+\omega^{2m}=0.
\]

Thus exact spacing by `a` is automatically singular on the cubic cofactor.  This is precisely the algebraic signature expected from an exact third-repeat.

The next target is the converse:

> show that (RL16.C16), together with the actual binary rotation geometry, forces
> `beta-alpha=gamma-beta=a`.

If this converse is obtained, the inherited repetition theorem RL-L48 excludes every primitive survivor; the only integer finite example remains `(10)^3`.

## Guardrail

RL-L104 is a reduction only.  It does **not** yet prove the cubic-cofactor branch impossible.
