# RL18 cubic phase / Eisenstein-norm reduction

## Scope

This note concerns the **only remaining radius-3 leaf** after the RL18 repairs:

`A=3a`, `L=3ell`, `gcd(a,ell)=1`, `gcd(3a,m)=1`,

with

`a p - m ell = 1`.

Let

`X=2^a`, `Y=3^ell`,

`D=X^3-Y^3=(X-Y)C`,

`C=X^2+XY+Y^2`,

and

`rho=2^m 3^(-p)`.

RL17 already promoted the one-orbit cubic sparse relation from modulo `C` to modulo the full `D`:

`1+3rho^u+9rho^(u+v)=0 (mod D)`,

for positive `u+v+w=3a`.

RL18 derives a sharper necessary condition modulo `C`.

## Cubic phase

Modulo `C`, put

`omega=X/Y`.

Since `X^2+XY+Y^2=0`, `omega` is a nontrivial cubic phase:

`omega^2+omega+1=0`.

The parameter relation implies

`epsilon := 3rho^a = omega^m (mod C)`.

Because `gcd(m,3)=1`, `epsilon` is again a primitive cubic phase:

`epsilon^2+epsilon+1=0`.

## Center the gaps

Write

`d=u-a`,

`t=a-w`.

Since `u+v+w=3a`,

`u+v=2a+t`.

The sparse polynomial becomes exactly

`P = 1 + epsilon rho^d + epsilon^2 rho^t (mod C)`.

Subtract the equal-gap identity `1+epsilon+epsilon^2=0`.  Put

`A0=rho^d-1`, `B0=rho^t-1`.

Then

`P=epsilon A0 + epsilon^2 B0`.

So a sparse zero implies

`A0 + epsilon B0 = 0 (mod C)`

(after multiplying by the unit `epsilon^(-1)`).

Conjugating the cubic phase and multiplying eliminates it:

**`A0^2 - A0 B0 + B0^2 = 0 (mod C)`.**

This is the Eisenstein norm of `A0+epsilon B0`.

## Positive rational lift

Let

`q=2^m/3^p > 0`.

Define the rational quantities

`Aq=q^d-1`, `Bq=q^t-1`.

Their Eisenstein norm is

`Nq=Aq^2-Aq Bq+Bq^2`.

The quadratic form is positive definite:

`x^2-xy+y^2 = (x-y/2)^2 + 3y^2/4`.

Therefore

`Nq>=0`,

with equality iff `Aq=Bq=0`.  Since `q!=1`, this means `d=t=0`, hence

`u=a`, `w=a`, and therefore `v=a`.

Thus **every skew triple has a strictly positive rational norm**.

After clearing powers of 2 and 3 from its denominator (units modulo `C`), a skew modular sparse zero forces `C` to divide a **nonzero positive integer numerator** of this norm.

This is analytically stronger than merely knowing the resultant is nonzero: the nonvanishing is automatic from positivity.

## What remains to prove

A radius-3 closure would follow from any theorem proving that, for every genuine skew rotation triple,

`0 < NormNumerator < C`,

or more generally that the norm numerator cannot be divisible by `C`.

Promising avenues:

1. bound the norm numerator using the signed centered exponents `d,t` and the Diophantine relation `ap-mell=1`;
2. factor the numerator into short binomial factors and compare each to `X-Y` and `C`;
3. take a second resultant/norm using `q^a=X^m/Y^p` and the cubic phase relation;
4. exploit genuine jump-geometry constraints to restrict which `(d,t)` can occur, rather than proving the arithmetic statement for all skew triples.

## Finite sanity check

`verify_rl18_cubic_norm_reduction.py` verifies the phase-centered identity, norm factorization, and rational positivity for all declared parameter quadruples with `a<=30`:

- 398 parameter quadruples;
- 789,950 gap triples;
- 789,552 skew rational norm positivity checks;
- all 398 cofactor zeros are equal-gap.

This finite check is **not** an infinite uniqueness proof.  Its role is to red-team the algebraic reduction.
