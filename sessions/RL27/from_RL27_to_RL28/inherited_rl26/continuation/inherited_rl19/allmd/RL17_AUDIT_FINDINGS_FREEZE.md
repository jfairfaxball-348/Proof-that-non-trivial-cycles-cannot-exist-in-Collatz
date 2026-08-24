# RL17 frozen audit findings

Date: 2026-08-20

This note freezes the skeptical review conclusions that should govern the next research session.

## A. What survived the audit

1. The supplied RL16 package passed its SHA-256 manifest check.
2. Both RL16 verifiers reran to PASS with their packaged counts.
3. No substantive flaw was found in the new RL16 resultant-nonvanishing arguments, monotonicity/envelope directions, LMN cutoff logic, continued-fraction tail reduction, or exact finite coverage for:
   - `j=0, P3 [2,1]` coefficient-5 boundary;
   - `j=1, P3 [2,1]` coefficient-5 boundary;
   - coprime `j=2, P2, [1,1,1]` strict interior.
4. RL-L104 is sound as a one-orbit `gcd(A,L)=3` reduction to a sparse `1,3,9` congruence modulo the cubic cofactor `C`.

## B. What was overstated or incomplete

The inherited claim that only one radius-3 branch remained is not certified.

### B1. Dropped coefficient-3 P2 boundary

The coprime canonical `P2 [2,1]` boundary contains the coefficient-3 form

\[
3+4\sigma^t\equiv0\pmod D,
\]

equivalently, using the complementary exponent,

\[
1+6\sigma^z\equiv0\pmod D.
\]

The inherited roadmap closed `P2` strict interiors but did not supply a closure for this boundary.  It occurs in the `j=1` and `j=2` canonical P2 sectors and must be handled explicitly.

### B2. Dropped `gcd(A,L)=3, gcd(A,m)=3` sector

RL-L104 assumes `gcd(A,m)=1`; RL12's three-orbit work assumes `gcd(A,L)=1`.  Neither covers their intersection.

The sector is nonempty at the structural level: the nonprimitive word `(10)^3=101010` has

\[
A=6,\quad L=3,\quad D=37,\quad m=3,
\]

hence

\[
\gcd(A,L)=3,\qquad \gcd(A,m)=3.
\]

Primitivity may ultimately kill the sector, but that requires a theorem rather than deletion by symmetry.

### B3. RL12 and RL13 proof provenance is incomplete

The recursive baseline retains verifier scripts/logs for RL12 and RL13, but not the corresponding analytic proof reports.  In particular, the verifiers use substantive infinite reductions such as the RL12 envelope `D^2<61^a` and the RL13 near-density envelope `D^6<569^L` plus far-density resultant estimates.  The finite scripts do not prove those analytic reductions by themselves.

Treat those closures as **inherited claims requiring reconstruction**, not as fully audited theorems, until proof notes are restored or rederived.

## C. Two former session leads are now reproduced

### C1. Full-D sparse promotion

The one-orbit cubic phase cancellation works modulo the full discrepancy

\[
D=2^{3a}-3^{3\ell},
\]

not only modulo the cubic cofactor.  The analytic proof is in `RL17_FULL_D_SPARSE_PROMOTION.md`; `verify_rl17_full_D_sparse.py` checks the identities on the same 1,359 constructive structural cases used by RL16.

Thus, under RL-L104's one-orbit hypotheses,

\[
D\mid Q(d)
\Longrightarrow
\rho^\alpha+3\rho^\beta+9\rho^\gamma\equiv0\pmod D.
\]

### C2. `a<=80` uniqueness scan

The pure arithmetic scan has been independently reproduced:

- 2,785 admissible `(a,ell,m,p)` choices;
- 39,719,443 ordered positive gap triples;
- modulo `C`: exactly one sparse zero per parameter choice, always `(a,a,a)`;
- no skew zero;
- modulo full `D`: only two zeros, both the trivial `(a,ell)=(2,1)` equal-gap case with the two allowed orientations `m=1,5`.

This is **computational evidence only**.

## D. Equal spacing implication strengthened

In the full-D formulation, equal spacing gives

\[
1+3\rho^a+9\rho^{2a}
\equiv 1+\omega^m+\omega^{2m}
\equiv C\,Y^{-2}\pmod D,
\]

where `X=2^a`, `Y=3^ell`, `C=X^2+XY+Y^2` and `D=(X-Y)C`.

Therefore an equal-gap full-D sparse zero forces `D|C`, hence `X-Y=1`, so

\[
2^a-3^\ell=1.
\]

An elementary mod-8 argument gives the only positive solution compatible with `X>Y`:

\[
(a,\ell)=(2,1).
\]

Thus if a future theorem proves that every one-orbit full-D sparse zero has equal gaps, the branch collapses immediately to the nonprimitive third-repeat case.

## E. Global correction

Even a complete exact-radius-3 exclusion is not an RL proof.  A separate bridge is required, for example a theorem that the RL least-root/final-return grammar forces a pair of distinguished `D`-divisible rotations into transposition distance at most 3.  No such theorem is currently frozen.
