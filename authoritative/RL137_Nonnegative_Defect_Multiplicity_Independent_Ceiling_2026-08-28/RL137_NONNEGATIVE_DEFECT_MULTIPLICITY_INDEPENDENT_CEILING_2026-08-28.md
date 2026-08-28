# RL137 — nonnegative-defect multiplicity-independent least-state ceiling

Date: 2026-08-28

## Outcome and classification

At the verified first reduced survivor
`(A,L)=(217,976,794,617,137,528,045,312)`, RL137 resolves one
quantitative part of the no-negative side of the RL136 dichotomy.

**RL137.1 — no-negative geometric cancellation.** Suppose a hypothetical
primitive ordinary cycle with full counts `(gA,gL)` has `h_j>=0` at every
proper phase. Then, independently of `g`, `m<2^75`.

Thus, throughout the inherited one-defect range
`1<=g<=771,316,334,039`, the explicit no-negative branch has `m<2^75`.
Conditional on inherited external `R#>=2^71`, it has
`2^71<=m<2^75`.

This is an analytic ordinary-owned consequence plus an exact rational
constant certificate. It does not force a negative excursion, exclude a
multiplicity, advance a frontier, or close Gate A, Gate B, nontrivial-cycle
exclusion, or Collatz.

## Exact multiplicity cancellation

Use the inherited notation
`q_j=2^(S_j)/3^j`, `rho_j=2^(floor(Aj/L))/3^j`, and
`h_j=floor(Aj/L)-S_j`. The no-negative hypothesis gives

`q_j=rho_j 2^(-h_j) <= rho_j`.                              (1)

Let `R=sum_(r=0)^(L-1) rho_r`. Exact block repetition gives

`sum_(j=0)^(gL-1) rho_j = ((exp(g Delta)-1)/(exp(Delta)-1)) R`. (2)

For the actual assumed ordinary cycle, the physical cycle-closing identity is

`(exp(g Delta)-1)m = (1/3) sum_(j=0)^(gL-1) q_j`.           (3)

Combining (1)--(3) cancels the full multiplicity factor:

`m <= R/[3(exp(Delta)-1)] < R/(3 Delta)`.                   (4)

RL134's exact rational logarithm enclosure gives `R<99,205,514,478`, and
the carried verifier certifies `R/(3 Delta)<2^75`.

### Theorem RL137.1

Whenever the all-nonnegative hypothesis holds, the first survivor has
`m<2^75`. The stated RL135 one-defect range identifies the live branch but is
not needed for the algebraic implication itself.

## Scope and red teams

RL20 passes because (3) is the actual ordinary affine cycle identity at the
least state, not a fixed-content condition. RL79 passes because the ordinary
increment is load-bearing in that identity. RL81 passes because all quantities
refer to an assumed physical ordinary cycle. Primitivity is retained in the
hypothetical setting but does not manufacture an excursion.

The result is a branch ceiling only. It supplies no population lower bound,
no realised shell, and no global sliding-window dispersion required by
RL123.5. No inherited theorem is corrected or demoted.

## Next target

Consume either the RL136 isolated-excursion fibres or this all-range
no-negative state band in a new physical packing, terminal-return, CRT, or
global-window theorem. Do not restart bare shell enumeration.
