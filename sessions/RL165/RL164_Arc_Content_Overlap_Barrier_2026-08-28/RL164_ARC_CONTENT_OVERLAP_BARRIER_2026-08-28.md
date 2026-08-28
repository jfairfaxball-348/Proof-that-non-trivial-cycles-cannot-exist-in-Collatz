# RL164 — phase-arc content overlap barrier

Date: 2026-08-28

## Outcome and classification

RL164 tests whether RL163's positive ordinary numerators on inverse-phase arcs can be consumed using the existing least-state and shallow-defect information. It proves an exact barrier for the direct small-representative congruence approach.

New results:

1. **RL164.1 — shallow phase inverse-cylinder theorem** (analytic, ordinary `+1`, coprime `g=1` first-survivor branch).
2. **RL164.2 — overlapping arc-content recurrence** (analytic, ordinary `+1`, same scope).
3. **RL164.3 — non-independence barrier** (analytic): the aggregate of these sliding inverse-cylinder congruences yields no independent CRT modulus or capacity loss.

No frontier changes. No cycle is excluded. `g>1`, Gate A, Gate B, nontrivial-cycle exclusion, and Collatz remain open.

## 1. Scope and inherited data

Use only the RL133/RL134 coprime `g=1` branch at

`(A,L)=(217,976,794,617,137,528,045,312)`.

Let `p=A^(-1) mod L=65,470,613,321`. RL163 gives a `p`-step physical arc

`2^(B_j)y_(j+p)=3^p y_j+C_j`,                             (1.1)

with `C_j>0` odd and `B_j` its actual exponent sum. RL133 supplies the state band

`y_j < lambda 2^(h_j)m/rho_j`,

while RL134 gives `m<2^75`. For proper phases, the RL133 floor lock gives `rho_j=2^(-{j beta})>1/2`; also `lambda<2` follows from the inherited `L Delta<log 2`.

## 2. RL164.1 — shallow inverse-cylinder representative

Every arc has `B_j>=p`, since it contains `p` positive exponents. Reducing (1.1) modulo `2^(B_j)` yields

`y_j == -3^(-p)C_j (mod 2^(B_j))`.                       (2.1)

If `h_j<=4`, then the physical band gives

`y_j < 2 * 2^4 * 2 * 2^75 = 2^81 < 2^p <= 2^(B_j)`.      (2.2)

Hence `y_j` is the unique nonnegative representative below `2^(B_j)` of the residue in (2.1). This is a genuine ordinary, word-content condition, but it is an inverse-cylinder condition rather than a new global ownership relation.

## 3. RL164.2 — exact overlap recurrence

Compare `p+1` physical steps from `j` in two ways: the `p`-arc then its last step, or one first step then the shifted `p`-arc. Writing `a_i` for the ordinary accelerated exponents gives

`B_j+a_(j+p)=a_j+B_(j+1)`,

and comparison of affine numerators gives

`3C_j+2^(B_j)=3^p+2^(a_j)C_(j+1)`.                      (3.1)

This is an exact identity. In particular, the inverse-cylinder contents of consecutive long arcs are linked by the very ordinary recurrence that generated them.

## 4. RL164.3 — what the existing bounds cannot consume

Equations (2.1) across the cycle are not independent congruences that may be multiplied by CRT: the overlapping physical words obey (3.1), and their exponent totals have the companion overlap identity. Summing or chaining only these identities merely transports existing word content.

Therefore the existing shallow-state window plus direct inverse-cylinder residues supplies no new independent modulus, state-count loss, or global exclusion. This is consistent with the inherited RL104/RL108 barriers against bare affine inverse-cylinder and local word-residue routes. It is not a claim that every content-sensitive method is impossible: a successor would need a genuinely additional nonlocal ownership or separation property not implied by (3.1).

## 5. Exact audit and red teams

`RL164_CERTIFICATES/verify_arc_content_overlap.py` exhaustively checks the overlap exponent and numerator identities, oddness, and inverse-cylinder congruence over 1,055 local arcs arising from bounded endpoint-zero positive-exponent defect words at five small coprime slopes.

- **Ordinary versus generalized increment:** PASS. The `+1` affine numerators are essential.
- **Physical versus quotient:** PASS. `y_j` denotes an assumed physical cycle state.
- **Residue scope:** PASS. The report calls (2.1) an inverse-cylinder condition and does not promote residue compatibility to ownership.
- **Phase order:** PASS. Each phase edge remains its RL163 `p`-step physical arc.
- **Multiplicity:** PASS. All claims are `g=1` only.
- **Aggregate red team:** PASS. The recurrence proves the non-independence needed to reject a spurious CRT/counting conclusion.

No inherited result is demoted.

## 6. Next target

Seek a genuinely nonlocal physical ownership relation among multiple shallow inverse-phase arcs, if one exists; it must not reduce to the consecutive overlap recurrence, bare residue matching, or an aggregate of local arc contents. Otherwise formulate a precise further barrier.
