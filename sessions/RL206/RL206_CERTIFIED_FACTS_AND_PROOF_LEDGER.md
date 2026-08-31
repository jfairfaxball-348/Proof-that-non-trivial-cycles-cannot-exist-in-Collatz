# RL206 certified facts and proof ledger

Date: 2026-08-31. Canonical proof-state record.

## Proved analytic mathematics and exact scope

**RL206-T1 — full-word additive compatibility classification.** For every binary
word with `0<L<A` and `D=2^A-3^L>0`, the cyclic integer matrix
`(Bx)_i=2x_(i+1)-3^(d_i)x_i` has cokernel `Z/DZ` and Smith form
`diag(1,...,1,D)`. The complete compatibility map is
`f -> sum_i 2^i 3^(L-P_(i+1)) f_i modD`. For physical forcing `f=d` it is
exactly `Q(d) modD`. Every additive RHS congruence annihilating `BZ^A` is
a factor projection of this map, and every universal formal affine zero
identity is a combination of recurrence rows. Complete proofs, including
constructive integer reduction, are in `proofs/QUOTIENT_MODULE_THEOREM.md`.

**RL206-T2 — finite-arc integer lattice.** Every prescribed length-m parity arc
without periodic closure has all integer trajectories
`x_j(t)=a_j+3^(P_j)2^(m-j)t`, `t in Z`, with an exactly specified endpoint
residue and positive states for all sufficiently large t.

**RL206-T3 — bounded integer rational residual constancy.** A fixed rational
function of those arc states, defined and integer-valued for every sufficiently
large compatible t and bounded in absolute value by a fixed finite M, is
constant as a rational function on that arc. The proof uses finite integer
image and polynomial identity, not extrapolation from a computation.
T2/T3 proofs are in `proofs/FINITE_ARC_SCALE_THEOREM.md`.

## Method barriers; excluded enlargements

T1 closes the entire specified additive compatibility/recurrence-zero family;
T3 closes the specified arc-local uniform rational-bound family. Neither
classifies residues of owned solutions, such as `Q/D modD`, modulo-D-squared
information, nonrational operations, or bounds using extra global hypotheses.
A constant on one fixed arc may depend on its word and fixed external data.
No exhaustive canonical Gate-B witness, nonzero small modulus residual, or
global finite reduction was proved. The H21 pivot is a strategic use of the
inherited fallback after these scoped barriers, not an all-quotient no-go.

## Explicit corrections

**RL206-C1:** R20G.12 must read
`H_(j+1)-H_j=(z^j/Y)3^(-E_(j+1))Q(B_j)`.
Strictness requires a block containing a 1. Height bounds, nonnegative lift,
endpoints and total strip width survive. Raw unnormalized population bounds
may not use the old coefficient.

**RL206-C2:** RL203 compared a tau34 source rank with a terminal-rank core.
The terminal phase is `a+34`, so the corrected below-p necessary-source
bounds are `p-a>=37`, normalized root-prefix depth `>=60`, and first
root-normalization depth `>=97`. The previous stronger 39/63/100 claims are
withdrawn at that scope. Both corrected depths still exceed 56, so the
qualitative one-sided Hensel-resolution boundary remains proved.

## Exact finite verification

The portable scripts certify their exact declared finite populations:
- matrix identities for all 778 eligible words of lengths 2–9; all 159,975
  coefficient vectors in the stated lengths-2–4/moduli-1–9 annihilator test;
  all 6,984 stated small formal forcings;
- all 2,046 binary arcs of lengths 1–10 at t=0,1,2,17, with 81,920 phase
  checks; all 940 eligible rational block words and 2,880 corrected increments;
- prescribed RL20 fake arithmetic, without replaying its inherited distance scan;
- complete offsets 34–39 for C2 and exact necessary-predicate witness e=37.
Outputs are frozen in `certificates/`. These finite checks supplement the
analytic proofs; they do not certify unknown cycles or unscanned rank deletion.

## Frozen inherited frontier

Exact necessary-rank count **16,188,727,234** and predicate unchanged;
eta classes `0,8,9,17 mod18` unchanged; no state/sign/valuation selected;
no physical H21 occurrence or charge; no sole-high-branch contradiction.
All physical H21 conclusions remain conditional on `(37,0,23,-1)`.
Gate A globally open; Gate B globally open; nontrivial-cycle exclusion open.
Current incoming checks permit acceptance of unaffected historical certificates
under verification economy. No whole 16-billion-rank recount is claimed.
