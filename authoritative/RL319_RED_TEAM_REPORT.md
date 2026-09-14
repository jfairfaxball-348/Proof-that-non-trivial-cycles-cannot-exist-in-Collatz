# RL319 red-team report

Date: 2026-09-14
Status: FROZEN WITH RL319 CLOSEOUT

## 1. Crossing scope

`gcd(delta_j,h)=1`, the first-crossing decomposition, and local congruences do
not force `h=1`. The explicit family `P=hp`, `S=hp-1` realizes the local
reverse crossing for every admissible `h`.

## 2. Suffix inequality direction

The proved inequality is `3^B q<=2^n E`. It forces `q<E` only when the suffix
is ternary-dominant (`3^B>2^n`). It supplies no absolute `q` cap for a
dyadic-dominant suffix.

## 3. Root-transport scope

The half-step transport uses RL135.2 and therefore applies to `g=2` at the
first survivor. It does not promote all-prefix nonnegative defect for other
multiplicities or fibres.

The ordered-row conclusion is a dichotomy. It does not prove that every
balanced cut is rooted at the least state.

## 4. Re-cut warning

Re-cutting at the least state changes the two row words. `epsilon=0` and
rankwise order are not invariant under that operation. The RL317 dichotomy
must be recomputed at the new cut.

## 5. Quantitative-cap scope

`G<2^35`, first difference `<=34`, and `kappa<2^34` require a least-rooted
balanced boundary at the first survivor. They must not be applied to an
arbitrary existential RL315 balanced cut.

The caps are necessary conditions, not a feasible exhaustive certificate.
No fixed-depth prefix scan is promoted.

## 6. Late-row height

The scaled contact `y=3^s m+K` does not bound `s`. The inequality
`|K|<3^s2^35` expands with `s` and is not a finite closure. The congruence
`3` not dividing `K` is likewise nonclosing.

## 7. Inherited barriers

- RL79 blocks homogeneous `T_h` invariants.
- RL206 and RL233 block unowned local-denominator and finite-modulus claims.
- RL263--RL264 block promotion of automatic finite-prefix affine identities.
- RL140--RL142 require their exact height/contact-interface hypotheses.
- RL21 remains the ordered-geometry negative control when `D0` ownership is
  absent.

## 8. Evidence and global scope

Small-word/state enumeration is regression evidence only. The rational-log
endpoint comparisons are exact certificates for the stated single fibre.

The external `2^71` certificate remains conditional. The internal frontier
remains `ell>=190537`.

Gate A and Gate B remain open. Global positive non-trivial-cycle exclusion
remains open. No Collatz-conjecture claim is made, and `g=1` remains separate.
