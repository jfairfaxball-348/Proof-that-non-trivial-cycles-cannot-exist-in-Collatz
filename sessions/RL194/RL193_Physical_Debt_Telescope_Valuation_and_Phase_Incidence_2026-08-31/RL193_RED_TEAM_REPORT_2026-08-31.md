# RL193 final bounded closeout red team

Audited the frozen candidate report and `verify_rl193_physical_debt.py` under
`CLOSEOUT_LOCK`.  No new mathematics, range extension, or exploratory scan was
performed.  The required verifier was executed and returned **PASS**, exit 0.

## Passed checks

- **Telescope/indexing:** the tail is `[u,a+L)` with `u=a+37`, length `L-37`.
  The exponent-normalized sum is exactly `(2^A-3^L)/2^21`, and each weighted
  summand is the stated constant multiple of a physical `K` increment.
- **Canonical versus lifted phases:** `a` is canonical, while `u` may initially
  be lifted.  The bound on `K_u` is valid because the zero prefix gives
  `K_u=K_a`, to which the canonical corridor applies.  A lifted carry has its
  base positive flow multiplied by `lambda>1`, so the `>1/2` carry floor
  remains valid.  The newly proved terminal floor in fact excludes wrapped
  extremal terminals, without being needed for these earlier arguments.
- **Valuation through carry:** both physical endpoint heights rise by at most
  one per chronological step, including periodic wraps.  At the carry,
  `v_2(epsilon)=-h_source>=-H_j`; thus the argument does not incorrectly apply
  an ordinary-pair identity across the seam.  The first term is uniquely of
  valuation `-21`, all later terms have valuation at least `-20`.
- **Deletion coverage:** 15 early-window plus 9 carry exclusions are distinct
  in `E`; 9 early-window plus 5 carry exclusions are distinct in the H21 core.
  The totals 24/14 and remaining certificate-rank cardinalities are correct.
- **Canonical terminal floors:** the exceptional phase 24 is outside both
  cores; the tested endpoint ranges establish floors 71 and 67 without
  asserting realization at those phases.
- **Strict prefix signs:** Q is excluded, canonical `a!=0` on the upper atom,
  and the exact formula for `rho_a` rules out equality with 1 there.  Lower
  atom prefix flow is positive; upper atom prefix flow is negative.
- **Cancellation constants:** both displayed exact fractions follow from
  `lambda-1<1/(2^40-1)`, the appropriate canonical `K_a` bound, and the carry
  floor.  Height at least one improves each floor by `1/4` as stated.
- **Realization/H21:** no rank, terminal, or cycle is constructed; the 24/14
  deletions remain finite necessary-state refinements.  No physical count,
  ownership multiplicity, branch closure, or H21 budget release is claimed.

## One required candidate wording correction

Report Section 7 (line 286 in the audited version) calls the result a method
barrier for "unsigned aggregate-flow consumers" without qualification.  This
is broader than the proof: it shows that the displayed *total weighted-debt
equation and total valuation alone* cannot exclude a physical triple, but it
does not exclude every possible future aggregate-flow argument.

Narrow that classification to the displayed total weighted-debt and
total-valuation identities alone.  The separate inherited rule that unsigned
variation cannot be converted directly to excursion without an ordering
theorem may remain.  This is candidate scope wording, not an inherited
mathematical contradiction or correction/demotion event.

Final status for the audited bytes: **all mathematical/numerical checks PASS;
one overbroad scope phrase requires narrowing before unqualified PASS**.

## Resolution and final sign-off

The revised Section 7 was read back directly.  It now limits the method
barrier to "the displayed total weighted-debt and total-valuation identities
alone" and states the missing ordering theorem for unsigned variation
separately.  This resolves the sole scope finding.  No numerical or
mathematical change was required, and no inherited correction/demotion was
introduced.

Resolved final status: **PASS** for the report and verifier under this bounded
audit.  No outstanding defect was found in the requested closeout checks.
