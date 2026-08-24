# RL17 — reproduced finite arithmetic evidence for cubic sparse uniqueness

## Status

**Exact finite computation only.  Not an infinite theorem.**

The former conversation-only claim has been independently reconstructed and frozen with an executable verifier.

## Parameter domain

For

\[
1\le a\le80,
\quad 1\le\ell<a,
\quad \gcd(a,\ell)=1,
\quad 2^a>3^\ell,
\]

scan every

\[
1\le m<3a,
\quad \gcd(3a,m)=1,
\]

for which

\[
p=\frac{1+m\ell}{a}
\]

is integral.  The binary-prefix feasibility inequalities

\[
0\le p\le m,
\qquad
0\le3\ell-p\le3a-m
\]

are asserted in the verifier and hold automatically for every retained choice.

This gives exactly

\[
\boxed{2785}
\]

admissible parameter quadruples `(a,ell,m,p)`.

For each quadruple, scan every ordered positive gap triple

\[
u,v,w\ge1,
\qquad
u+v+w=3a.
\]

The total is

\[
\boxed{39,719,443}
\]

gap triples.

## Cofactor result

With

\[
C=2^{2a}+2^a3^\ell+3^{2\ell},
\qquad
\rho=2^m3^{-p}\pmod C,
\]

the normalized sparse equation is

\[
1+3\rho^u+9\rho^{u+v}\equiv0\pmod C.
\]

The exact scan finds:

- 2,785 zeros total;
- exactly one zero for every parameter quadruple;
- every zero is

\[
(u,v,w)=(a,a,a);
\]

- no skew zero.

## Full-D result

Repeating the same scan modulo

\[
D=2^{3a}-3^{3\ell}
\]

finds only two zeros in the entire domain:

\[
(a,\ell,m,p,u,v,w)
=(2,1,1,1,2,2,2),
\]

and

\[
(2,1,5,3,2,2,2).
\]

These are the two orientations of the trivial equal-gap third-repeat parameter set.  No skew full-D zero occurs through `a=80`.

## Interpretation

The cofactor experiment suggests a strong algebraic uniqueness phenomenon.  The full-D experiment is even sharper: after promotion to the full discrepancy, the equal-gap singular family disappears except for the nonprimitive `(a,ell)=(2,1)` case.

Do **not** extrapolate either finite statement to all `a`.  Use the data to search for a factorization, norm, resultant, order, or descent theorem that explains the observed uniqueness.
