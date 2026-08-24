# RL17 proof-status and radius-3 branch ledger

## 1. Evidence hierarchy

| Item | Status | Audit action |
|---|---|---|
| RL7--RL10 local transposition structure | Analytic/inherited | Reuse after checking exact hypotheses when cited |
| RL11 mixed-direction closure | Analytic + external two-log theorem + exact finite certificate | Retain explicit external LMN dependency |
| RL12 coprime three-orbit same-direction closure | Inherited analytic claim + verifier | **Reconstruct missing analytic proof report** |
| RL13 `j=0,P3` strict interior | Inherited analytic claim + verifier | **Reconstruct missing analytic proof report** |
| RL14 `j=1,P2` strict interior | Analytic/inherited | Closed, but does not cover the `[2,1]` boundary |
| RL15 `j=1,P3` strict interior | Analytic + external LMN + exact certificate | Closed conditional on external theorem |
| RL16 coefficient-5 P3 boundaries | Analytic + external LMN + CF + exact certificate | Audit survived |
| RL16 `j=2,P2` strict interior | Analytic + external LMN + exact certificate | Audit survived |
| RL-L104 modulo `C` | Analytic reduction | Sound, not a closure |
| RL17 promotion to full `D` | **Analytic lemma + finite structural audit** | New frozen result in this bundle |
| `a<=80` sparse uniqueness | Exact computation | Evidence only; no infinite promotion |
| Sparse uniqueness for all parameters | Open | Prime theorem target |
| Coefficient-3 `P2 [2,1]` boundary | Open | Omitted branch; repair target |
| `gcd(A,L)=3,gcd(A,m)=3` | Open | Omitted branch; repair target |
| Radius-3 exclusion => RL contradiction | Open/absent | Global strategy target |

## 2. Radius-3 branch ledger

| Direction/gcd sector | Support/canonical sector | Current status |
|---|---|---|
| connected same-direction | `[3]` | closed at RL10 |
| mixed direction | disconnected `[2,1]`, `[1,1,1]` | closed at RL11 |
| same direction, coprime, `j=0,P3` | strict `[1,1,1]` | RL13 inherited closure; proof note must be reconstructed |
| same direction, coprime, `j=0,P3` | coefficient-5 `[2,1]` boundary | closed RL16 |
| same direction, coprime, `j=1,P2` | strict `[1,1,1]` | closed RL14 |
| same direction, coprime, `j=1,P2` | coefficient-3 `[2,1]` boundary | **OPEN / previously omitted** |
| same direction, coprime, `j=1,P3` | strict `[1,1,1]` | closed RL15 |
| same direction, coprime, `j=1,P3` | coefficient-5 `[2,1]` boundary | closed RL16 |
| same direction, coprime, `j=2,P2` | strict `[1,1,1]` | closed RL16 |
| same direction, coprime, `j=2,P2` | coefficient-3 `[2,1]` boundary | **OPEN / previously omitted** |
| same direction, `gcd(A,L)=1,gcd(A,m)=3` | three-orbit sector | RL12 inherited closure; proof note must be reconstructed |
| same direction, `gcd(A,L)=3,gcd(A,m)=1` | one-orbit cubic sector | full-D sparse reduction proved; sparse uniqueness OPEN |
| same direction, `gcd(A,L)=3,gcd(A,m)=3` | three-orbit cubic sector | **OPEN / previously omitted** |

This table is the authoritative repair ledger until a new exhaustive case-tree proof supersedes it.

## 3. Clean theorem statements still wanted

### T1. Coefficient-3 P2 boundary exclusion

Under the coprime canonical P2 hypotheses, prove for the `j=1` and `j=2` sectors that no `1<=t<L` satisfies

\[
3+4\sigma^t\equiv0\pmod D.
\]

A useful equivalent root form inherited from RL12 is to show that the induced exponent relation `theta^k=-1` cannot occur under the relevant parity/canonical constraints.

### T2. Full-D one-orbit cubic sparse uniqueness

With

\[
A=3a,\quad L=3\ell,\quad \gcd(a,\ell)=1,
\]

`gcd(3a,m)=1`, and

\[
ap-m\ell=1,
\]

put

\[
D=2^{3a}-3^{3\ell},\qquad \rho=2^m3^{-p}\pmod D.
\]

For positive gaps

\[
u+v+w=3a,
\]

prove, under the genuine rotation-geometry constraints,

\[
1+3\rho^u+9\rho^{u+v}\equiv0\pmod D
\quad\Longrightarrow\quad
u=v=w=a.
\]

The equal-gap conclusion then forces `(a,ell)=(2,1)`, hence the nonprimitive third-repeat case.

### T3. Cubic three-orbit exclusion

Close or reduce the sector

\[
\gcd(A,L)=3,\qquad \gcd(A,m)=3
\]

without assuming one-orbit phase coordinates.  First test whether division by 3 reduces it to an RL12-type three-orbit theorem on `(a,ell,m/3)`, and identify exactly what happens to primitivity and `D`-divisibility under that normalization.
