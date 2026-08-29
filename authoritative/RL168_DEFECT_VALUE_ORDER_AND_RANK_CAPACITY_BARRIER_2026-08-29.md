# RL168 — defect-value order and rank-capacity barrier

Date: 2026-08-29

## Outcome and classification

RL168 obtains a genuinely global, ordering-sensitive coupling between the
least-root defect path and the actual physical phase values.  It then proves
that the most direct odd-state rank-packing use of that coupling has no
distributional force under the inherited external minimum floor.

New results:

1. **RL168.1 — lifted-defect state-order theorem** (analytic, ordinary `+1`,
   coprime `g=1` first-survivor least-root scope): the physical state values
   are strictly ordered by `E_j=Aj-LS_j`.
2. **RL168.2 — single-phase rank-capacity barrier** (analytic, conditional on
   inherited external `m>=2^71`): the state-packing lower bound implied by
   RL168.1 is strictly below the inherited physical upper envelope at every
   nonminimal phase.  Thus this direct order-plus-individual-packing route
   cannot restrict the defect-height distribution.

No cycle is constructed or excluded.  The result does not reopen local,
count/product, bare-residue, phase-order, or same-root-elimination routes.
Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.

## 1. Scope and notation

Retain the coprime first-survivor branch

`A=217,976,794,617`, `L=137,528,045,312`, `gcd(A,L)=1`,

with an assumed ordinary accelerated cycle rooted at its least odd state
`m=y_0`.  Put

`S_j=sum_(i<j)a_i`, `q_j=2^(S_j)/3^j`,
`h_j=floor(Aj/L)-S_j>=0`, and

`E_j=Aj-LS_j=(Aj mod L)+Lh_j`.                             (1.1)

For `0<=j<L`, the `E_j` are nonnegative.  They are also distinct: equality
`E_j=E_k` would give `A(j-k)=L(S_j-S_k)`, and coprimality forces
`L | (j-k)`, hence `j=k` in this range.  In particular, `E_0=0` is the unique
minimum.

Write `Delta=A log(2)-L log(3)`,
`theta=L Delta/log(2)`, and `lambda=2^A/3^L`.  The inherited exact
RL134 certificate gives `5 theta<1`; in particular `theta<1/2`.

The prefix and complementary suffix affine identities from RL133 give, for
every phase needed below,

`m < q_j y_j < lambda m`,                                  (1.2)

with the left equality only at the distinguished initial phase.  The strict
upper inequality remains valid at that phase because `lambda>1`.

## 2. RL168.1 — lifted-defect state order

The exact identity

`log_2(q_j)=j theta/L^2-E_j/L`                              (2.1)

follows by substituting `S_j=(Aj-E_j)/L`.  If `E_j<E_k`, then

`log_2(q_j/(lambda q_k))`

`= [E_k-E_j-theta+(j-k)theta/L]/L`.                         (2.2)

Since `E_k-E_j>=1`, `-(L-1)<=j-k<=L-1`, and `theta<1/2`, the
numerator in (2.2) is strictly larger than

`1-theta-(L-1)theta/L > 1-2theta > 0`.

Thus `q_j>lambda q_k`.  Applying (1.2) gives

`y_j < lambda m/q_j < m/q_k < y_k`.                        (2.3)

### Theorem RL168.1

For all `0<=j,k<L`,

`E_j<E_k  <=>  y_j<y_k`.                                    (2.4)

The reverse implication follows because the `E_j` are distinct and the
forward implication applies after swapping indices.  This is a full
phase-to-value order theorem: it is not a count or local-residue statement.

For adjacent chronological phases,

`E_(j+1)-E_j=A-La_j`.

Since `L<A<2L`, this is positive exactly when `a_j=1`; the corresponding
ordinary state increment is positive exactly then as well.  This is a useful
consistency check, but the theorem controls every pair of phases, not only
one-step comparisons.

## 3. RL168.2 — direct rank packing is slack

Let

`r_j=#{k:E_k<E_j}`.

By RL168.1, there are `r_j` distinct odd states below `y_j`, all at least
`m`.  Hence

`y_j>=m+2r_j`.                                              (3.1)

On the other hand, (1.2) and (2.1) give the exact upper envelope

`y_j < lambda m/q_j`
`    =m 2^((E_j+theta(1-j/L))/L)`.                          (3.2)

The distinct nonnegative integers `E_k` give the purely combinatorial bound
`r_j<=E_j`.  Now impose only the inherited external qualification
`m>=2^71`.  Since `L<2^38` and `log(2)>1/2`, for every `E_j>0`,

`m(2^((E_j+theta(1-j/L))/L)-1)`
` >m(2^(E_j/L)-1)`
` >(m log(2)/L)E_j`
` >2E_j`.                                                    (3.3)

The last inequality already follows from `2^70>2L`.  Combining
`r_j<=E_j` with (3.3) yields

`m+2r_j < lambda m/q_j`.                                    (3.4)

### Theorem RL168.2

Conditional on the inherited external floor, every individual lower bound
obtained by ordering and packing the earlier odd states, namely (3.1), lies
strictly below the already available phase upper envelope (3.2).  Therefore
this single-phase rank comparison cannot produce a contradiction or a new
restriction on which residues can carry a given height.

This is a sharp scope statement.  It does not assert a jointly realizable
physical cycle or a countermodel.  It only proves that this proposed
order-plus-*individual*-capacity comparison is numerically incapable of
excluding a defect distribution.  A successor would need a simultaneous
multi-phase integer-gap theorem, not merely the rank lower bound (3.1).

## 4. Exact audit and red teams

`RL168_CERTIFICATES/verify_defect_value_order.py` uses exact integer and
rational arithmetic.  It reconstructs the inherited logarithm interval far
enough to certify `5 theta<1`, checks the exact survivor arithmetic
`L<2^38` and `2^70>2L`, and checks distinct lifted defects and rank bounds on
2,404 bounded coprime nonnegative-defect paths.

- **Ordinary increment:** PASS.  The two-sided affine squeeze is from the
  actual ordinary `+1` prefix and suffix numerators.
- **Physical versus quotient:** PASS.  `y_j` are assumed physical phase
  states; no residue is promoted to an owned state.
- **Global versus local:** PASS.  The result compares arbitrary phase pairs
  through the full least-root squeeze.  It is not a fixed-radius argument.
- **External input:** PASS.  Only RL168.2 uses the inherited external
  `m>=2^71`; RL168.1 is internal to the assumed `g=1` physical branch.
- **Phase normalization and order:** PASS.  It uses the established
  `E_j=(Aj mod L)+Lh_j` lift and does not confuse modular phase adjacency
  with chronological adjacency.
- **No false closure:** PASS.  No full-cycle divisibility, state construction,
  or non-trivial-cycle exclusion is claimed.

## 5. Next target

Seek a genuinely simultaneous integer-gap relation among several ordered
phases that uses the exact increments of `q_j y_j`, not merely their
individual envelopes or the rank count.  It must remain in the `g=1`,
ordinary-`+1`, physical least-root branch and must not collapse back to the
single full closure condition, a count/product bound, or a local cylinder.
