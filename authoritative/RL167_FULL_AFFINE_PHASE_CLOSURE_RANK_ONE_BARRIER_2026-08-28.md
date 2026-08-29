# RL167 — full-affine phase-closure rank-one barrier

Date: 2026-08-28

## Outcome and classification

RL167 resolves the stated full-affine phase-distribution target negatively for
the proposed source of extra information.  For a fixed positive accelerated
word, the ordinary full affine closing equations at all cyclic phases are
equivalent to one divisibility condition.  Once that condition holds, every
rotated affine quotient is automatically a positive integral physical state
and the ordinary `+1` equations hold at every phase.

New results:

1. **RL167.1 — cyclic full-affine propagation theorem** (analytic, ordinary
   `+1`, any positive word with `D=2^A-3^L>0`).
2. **RL167.2 — rank-one phase-closure corollary** (analytic): phase-by-phase
   physical integrality adds no independent closing congruence after one full
   affine closing divisibility is imposed.
3. **RL167.3 — corrected defect-phase factorization** (analytic, coprime
   `g=1` least-root first-survivor scope): that sole closure condition is
   exactly the existing dense corrected phase-polynomial condition
   `P_h(rho)=0 (mod D)`.

This is a method barrier, not an existence result for a word satisfying the
divisibility, and not a non-trivial-cycle exclusion.  It does not demote an
inherited claim.  Gate A, Gate B, non-trivial-cycle exclusion, and Collatz
remain open.

## 1. Ordinary cyclic numerator identity

Let `(a_0,...,a_(L-1))` be a cyclic word of positive integers, put

`A=sum a_j`, `D=2^A-3^L>0`,

and, with indices modulo `L`, define the full affine numerator at rotation
`j` by

`N_j=sum_(t=0)^(L-1) 3^(L-1-t) 2^(a_j+...+a_(j+t-1))`.       (1.1)

The empty exponent is zero.  Directly separating the first term in the two
cyclic sums gives

`2^(a_j) N_(j+1)=3N_j+D`.                                   (1.2)

This is the full-word counterpart of the overlapping-arc identity in RL164;
here the terminal discrepancy is exactly the full determinant `D`.

### Theorem RL167.1 — cyclic full-affine propagation

For every `j`,

`D | N_j  <=>  D | N_0`.                                    (1.3)

If these equivalent conditions hold, then

`y_j=N_j/D`

are positive integers and satisfy the ordinary accelerated Collatz equations

`3y_j+1=2^(a_j)y_(j+1)`                                     (1.4)

cyclically.  Conversely, any positive integral realization of the word
satisfies `D|N_0` and has `y_j=N_j/D`.

### Proof

The determinant `D` is odd.  Reducing (1.2) modulo `D`, both `2^(a_j)` and
`3` are units, so `D|N_(j+1)` if and only if `D|N_j`.  Cycling proves (1.3).
If `D|N_0`, all quotients `N_j/D` are positive integers because every term of
(1.1) is positive.  Dividing (1.2) by `D` gives (1.4).  Conversely, compose
the `L` ordinary equations from phase zero:

`2^A y_0=3^L y_0+N_0`,

so `N_0=Dy_0`.  This also identifies the rotated quotient.  ∎

### Consequence

The `L` apparent phase closing/integrality tests have rank one over the full
word.  Asking that all phase states be physical does not supply a further
phase-distribution or packing relation after the full affine closure has
already been imposed.  Least-state *ordering* still has content, but its
already inherited consequences must not be replaced by a fictitious family
of independent phase-closing congruences.

## 2. Exact relation to the coprime defect phase polynomial

Now retain only the inherited coprime `g=1` first-survivor least-root scope.
Thus `h_j=floor(Aj/L)-S_j>=0`, `h_0=0`, and `S_j=sum_(i<j)a_i`.
Let `p=A^(-1) mod L`, `u=(Ap-1)/L`, and

`rho=2^u 3^(-p) (mod D)`.

Then `rho^L=1/2 (mod D)`.  For every `j`, a direct Bezout reduction gives

`rho^(Aj-LS_j)=2^(S_j)3^(-j) (mod D)`.                     (2.1)

Indeed, use `2^A=3^L (mod D)` and `pA-uL=1` in the two factors of
`rho^(Aj-LS_j)`.  Therefore, with

`R_h(T)=sum_(j<L) T^(Aj-LS_j)`,

we have

`N_0 3^(-(L-1))=R_h(rho) (mod D)`.                         (2.2)

Since `Aj-LS_j=(Aj mod L)+Lh_j`, set `H=max h_j` and use
`rho^L=1/2` to obtain the corrected dense polynomial

`P_h(T)=sum_(j<L) 2^(H-h_j)T^(Aj mod L)`,

with

`P_h(rho)=2^H R_h(rho) (mod D)`.                            (2.3)

All displayed multiplier factors are units modulo `D`.  Consequently

`D|N_0  <=>  R_h(rho)=0 (mod D)  <=>  P_h(rho)=0 (mod D)`.  (2.4)

This recovers the correctly normalized RL157/RL159 ownership condition from
the actual full ordinary affine equality.  In particular, the physical
phase-by-phase conditions in Theorem RL167.1 do not yield an independent
constraint on the distribution of the heights `h_j`; they are all transport
of the same dense closure relation.

## 3. What this does and does not remove

RL166 had already shown that local nonnegative grammar, shallow population,
and the one-sided product mass cannot force a shallow inverse-phase pair.
RL167 now rules out the natural attempted supplement that treats the full
ordinary affine equality at many physical phases as many independent
distribution constraints.  The exact equations propagate around the cycle
from one closure condition.

This does **not** prove that a nonnegative defect path can satisfy (2.4), nor
construct a cycle.  Nor does it prove that no new phase-distribution theorem
can use the arithmetic of the single dense condition (2.4), a quantitative
ordering of the actual quotients `y_j`, or another genuinely global input.
It only rules out repeated all-phase affine closure/physicality as an
additional resource.

## 4. Exact audit and red teams

`RL167_CERTIFICATES/verify_full_affine_rank_one.py` uses only integer
arithmetic.  It checks (1.2), the all-rotation divisibility equivalence, and
the physical quotient equations over 5,332 bounded positive words with
positive determinant.  It separately checks the Bezout/defect normalization,
including `rho^L=1/2` and (2.2)--(2.4), on 432 bounded coprime
nonnegative-defect cases.

- **Ordinary increment:** PASS.  The `+D` term in (1.2) comes from the
  ordinary `+1` recurrence; no increment-scaling invariant is asserted.
- **Physical versus quotient:** PASS.  Theorem RL167.1 proves physical
  integrality conditional on one actual full divisibility; it does not call a
  bare residue an owned state.
- **Full closure versus product:** PASS.  The proof uses the entire affine
  numerator and its exact divisibility, not RL166's one-sided product bound.
- **Phase normalization:** PASS.  The retained relation is
  `rho^L=1/2`, with coefficient `2^(H-h_j)`; no demoted `3T^L-2` formula is
  used.
- **Multiplicity and scope:** PASS.  Section 1 is word-general; Section 2
  is explicitly restricted to the inherited coprime `g=1` least-root branch.
- **No false exclusion:** PASS.  The result is a rank-one method barrier and
  makes no claim of an RL or Collatz closure.

## 5. Next target

Seek an ordering-sensitive relation between the exact quotient values
`y_j=N_j/D` and the defect phases `h_j` that is not a restatement of their
cyclic affine recurrence, a fixed-radius condition, a count/product bound,
or the single congruence `P_h(rho)=0`.  Any such relation must consume actual
least-state order quantitatively and preserve the `g=1`, ordinary-`+1`,
physical-state, external-floor, and phase-order limits.
