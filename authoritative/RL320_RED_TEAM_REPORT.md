# RL320 red-team report

Date: 2026-09-14
Status: FROZEN WITH RL320 CLOSEOUT

## 1. Conditional scope

The bounded-surrogate proof uses `2^71<=m<2^75` and is conditional on the
externally inherited `2^71` least-state certificate. It is not an internal
least-state theorem. The internal and external frontiers remain distinct.

## 2. Weighted versus ordinary ownership

The late-row identities own `U_s+3^sV_s` and `U_s-3^sV_s`. They do not give
an unweighted balanced-row factorization for the actual two half words.

The extracted positive `(Z,W)` pair satisfies the algebra of a balanced
return, but it is not parity-owned. Direct ownership from `m` is impossible:
the deterministic actual next `a` phases have weight `ell+s`, not `ell`.
No least-state descent, root-aligned return, row repetition, or new cycle is
inferred from `(Z,W)`.

## 3. Residue and height

The fixed-residue lift count is independent of `s`, but the residue itself is
support-sensitive. `0<|theta|<3^s` is not a finite certificate and does not
bound `s`.

The word family `1^(2ell)0^(2a-2ell)` is only a geometry countermodel. It is
not claimed to be an ordinary cycle. Its role is to prove that all-prefix
nonnegative defect plus ordered balanced rows cannot yield a bounded height.

## 4. Three-clock scope

For `kappa>0`, `min(v2(E),v2(rho))<=33` bounds the earliest mismatch among
three coupled paths. It does not force the physical/coprime-shadow pair to
mismatch by phase 33 and does not place the first reverse crossing there.
For `kappa=0`, no clock cap is obtained.

## 5. Contact barriers

RL140--RL146 require height-one/contact hypotheses not proved here. The
general mixed-height owned identity is subject to RL147's combined-layer
barrier; binary layers are not independently owned. No contact theorem is
silently extended.

## 6. Inherited negative controls

- RL21 blocks order-only conclusions without genuine ownership.
- RL79 blocks homogeneous generalized-increment invariants.
- RL206 and RL233 block local-denominator ownership claims.
- RL263--RL264 block finite-prefix affine-ray promotion.
- RL147 blocks the inherited scalar carry-order lift to mixed height.

## 7. Verification and global claims

Small exact loops are regression evidence. The rational-log comparison is an
exact certificate only for the stated first-survivor constants.

No mathematical correction or demotion occurs. Gate A, Gate B, the global
positive non-trivial-cycle exclusion, and `g=1` remain open.
