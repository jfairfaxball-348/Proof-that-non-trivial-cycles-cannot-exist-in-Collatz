# RL312 — full-D exclusion of a single active balanced shift-orbit

Date: 2026-09-13
Status: LIVE RL312 CHECKPOINT
Classification: EXACT ANALYTIC ALL-SCALE CONSUMER

`PARENT_DIFFICULTY_DELTA = EASIER`

This checkpoint strengthens the preceding Radius-2 exclusion.  It proves an all-scale support-multiplicity theorem for every proper balanced self-rotation of a primitive positive full-`D` cycle.  It does not close the whole RL311 balanced-return branch, and it does not touch the complementary `g<=h+1` branch.

## 1. Setup

Let `w` be a genuine primitive positive full-`D` Collatz cycle word of length `A`, weight `L`, with

`D=2^A-3^L>1`.

Let `s`, `1<=s<A`, be a **balanced** rotation length, so

`p=sL/A`

is an integer.  Define the cyclic length-`s` window count

`W_i=sum_(t=0)^(s-1) w_(i+t)`

and the canonical balanced flow

`f_i=p-W_i`.

Then

`sum_i f_i=0`,

`f_(i+1)-f_i=w_i-w_(i+s)`.                    (R312S.1)

Put

`d0=gcd(A,s)`, `n=A/d0`.

The permutation `i -> i+s (mod A)` has exactly `d0` orbits, the residue classes modulo `d0`, each of length `n`.

Because the shift is proper, `n>1`.

Also `d0>=2`.  Indeed, writing `A=ga`, `L=g ell` in lowest terms gives `s=ma`, hence

`d0=a gcd(g,m)`.

Since `D>0` and `ell>=1`, one has `a>=2`.

## 2. The support-one hypothesis

Assume for contradiction that `f` is nonzero but is supported on exactly one shift-orbit.

Thus, for some residue `r (mod d0)`,

`f_i=0` whenever `i != r (mod d0)`.

Rotate the genuine cycle so that residue `r-1` is the start of every consecutive row of length `d0`.  Full-`D` ownership is preserved under genuine cyclic rotation.

In these coordinates the only residue on which `f` may be nonzero is column `1`.

Write the word as `n` consecutive rows

`B_0 B_1 ... B_(n-1)`,

where every `B_k` has length `d0`.

Since `s=d0 m0` with `gcd(m0,n)=1`, the shift by `s` acts transitively on the row indices.

## 3. Exact row rigidity

For every column `c>=2`, both `f_i` and `f_(i+1)` vanish at positions in column `c`.  Equation (R312S.1) gives

`w_(i+s)=w_i`.

By transitivity of the row shift, every column `c>=2` is therefore constant across all rows.

At column `0`, (R312S.1) gives

`w_(i+s)-w_i=-f_(i+1)`.

At column `1`, it gives

`w_(i+s)-w_i= f_i`.

Hence the sum of the two special bits is invariant under the row shift.  Because `f` is nonzero somewhere, the invariant sum cannot be `0` or `2`; it is exactly `1`.

Therefore every row has the form

`10 C`

or

`01 C`,                                               (R312S.2)

for one fixed binary suffix `C` of length `d0-2`.

Both row types occur: if all rows had the same type then the word would be invariant under the transitive row shift and (R312S.1) would give `f=0`.

In particular every row has the same weight.  Let it be `l0`.  Since there are `n` rows,

`L=n l0`.

Put

`X0=2^d0`, `Y0=3^l0`, `D0=X0-Y0`.

Then

`D=X0^n-Y0^n=D0 H`,

where

`H=sum_(k=0)^(n-1) X0^k Y0^(n-1-k)`.          (R312S.3)

Since `D>0`, also `D0>0` and `H>0`.

## 4. Exact two-row numerator difference

Let `Q10` be the standard affine numerator of the row `10C`, and `Q01` that of `01C`.

The two rows have the same weight and differ only by moving the first `1` one step to the right.  All later prefix-one counts agree.  Hence exactly

`Q01-Q10=3^(l0-1)=:C0`.                       (R312S.4)

In particular `C0` is a power of `3`.

Encode row `B_k` by `eps_k in {0,1}`, with `eps_k=1` for `01C` and `0` for `10C`.

Define

`S=sum_(k=0)^(n-1) eps_k X0^k Y0^(n-1-k)`.     (R312S.5)

Because both row types occur and every summand in `H` is positive,

`0<S<H`.                                               (R312S.6)

Grouping the full word numerator by equal-length/equal-weight rows gives the exact identity

`Q(w)=Q10 H + C0 S`.                                  (R312S.7)

## 5. Full-D contradiction

Because `w` is a genuine full-`D` cycle rotation,

`D | Q(w)`.

Multiply (R312S.7) by `D0`.  Using `D=D0 H`,

`D0 Q(w)=D Q10 + C0 D0 S`.

Therefore

`D | C0 D0 S`,

hence

`H | C0 S`.                                             (R312S.8)

But `H` is coprime to `3`: modulo `3`, every term in (R312S.3) except the last vanishes, while the last is `X0^(n-1)`, nonzero modulo `3`.

Since `C0` is a power of `3`,

`gcd(H,C0)=1`.

Thus (R312S.8) implies

`H | S`,

contradicting `0<S<H`.

Therefore the support-one hypothesis is impossible.

## 6. Theorem

**Single-active-shift-orbit exclusion.**

For every proper balanced self-rotation of a primitive positive full-`D` Collatz cycle, the canonical balanced flow is either identically zero or is nonzero on at least two distinct `i -> i+s` shift-orbits.

The identically-zero case would make the word invariant under the proper rotation and is excluded by primitivity.  Hence every genuine proper balanced self-rotation activates at least two shift-orbits.

This theorem is independent of the `lambda<3` restriction.  The `lambda<3` hypothesis is needed only upstream, to obtain the RL311 short equal-level balanced return.

## 7. Relation to the preceding Radius-2 theorem

A zero-sum exact Radius-2 flow has one `+1` and one `-1`.  Since the sum of `f` on each shift-orbit telescopes to zero, those two defects must lie on the same shift-orbit.  The theorem above therefore excludes Radius 2 as an immediate corollary.

The earlier RL312 Radius-2 proof remains a valid independent derivation; this checkpoint strictly strengthens its support conclusion.

Combining with the audited Radius-4 local theorem, a proper balanced full-`D` self-rotation cannot lie in Radius `0`, `2`, or `4` (with the usual low-radius normalization `R<A`).  No Radius-6 theorem is activated or claimed.

## 8. Why this escapes the RL20 coboundary barrier

RL20 shows that the **whole** canonical block polynomial is a state coboundary and that raw proper-factor cancellation is tautological.

Here the extra input is not the raw block cancellation.  The independently assumed sparse physical support forces an exact two-row alphabet `10C/01C`, and hence a rank-one numerator decomposition

`Q=Q10 H+C0 S`

with the strict positivity bound `0<S<H`.

Full-`D` ownership then forces the impossible proper-cofactor divisibility `H|S`.

This is precisely a sparse coefficient-pattern consumer of the kind RL20 left open; no proper-prefix denominator ownership is used.

## 9. RL311 consequence

For the RL311 equal-level return with shift `s=ma`, the canonical flow satisfies at block cuts

`f_(ra)=E_r-E_(r+m)`.

The new theorem says that this flow cannot concentrate all of its discrepancy on one shift-orbit.  Any surviving RL311 balanced return must carry genuinely multi-orbit discrepancy.

This is an all-scale structural contraction: it is not a fixed-depth grammar and has no dependence on `h`.

## 10. Scope and checkpoint rating

Promoted:

- exact row rigidity under one active shift-orbit;
- exact rank-one full-numerator factorization;
- full-`D` exclusion of every nonzero single-orbit balanced flow;
- Radius-2 exclusion as a corollary.

Still open:

- exclusion of balanced flows on two or more shift-orbits at arbitrary radius;
- an upper bound on the RL311 balanced-return radius/support;
- the complementary `g<=h+1` branch;
- Gate A, Gate B, and global non-trivial-cycle exclusion.

`PARENT_DIFFICULTY_DELTA = EASIER` is justified because this is a genuinely independent, all-scale ownership-sensitive consumer that removes an entire support class rather than adding another discrepancy lower bound.
