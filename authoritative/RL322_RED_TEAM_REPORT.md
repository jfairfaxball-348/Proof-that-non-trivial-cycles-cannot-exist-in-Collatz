# RL322 red-team report

Date: 2026-09-14
Status: PASS WITH EXPLICIT SCOPE LIMITS

## RT1 — prefix rigidity ownership

PASS. The `1^66` conclusion is applied only to the genuine ordinary-owned prefix `alpha` in the RL321 negative canonical branch. No affine surrogate is relabelled as a parity word.

## RT2 — 480-case certificate completeness

PASS. `2^71<=m<2^75` and `m==-1 (mod 2^66)` give exactly `33<=h<=512`, inclusive: 480 values. Every value is checked with exact rational outer bounds for `delta=D0/X`. There are no skipped ranges or floating-point proof steps.

## RT3 — logarithm/exponential enclosure

PASS. `log 2` and `log 3` are enclosed by finite rational atanh series with a rigorous rational tail. `1-exp(-Delta)` is enclosed by alternating Taylor inequalities on `0<Delta<2^-40`. The verifier uses `Fraction` throughout the certificate.

## RT4 — branch scope

PASS. The Branch-B contradiction is stated only at the conditional first external survivor and inherits the external least-state floor. It is uniform in the remaining support within that branch, but is not promoted as a global Gate-A/Gate-B theorem.

## RT5 — positive-branch relabelling

PASS. The session explicitly rejects the inference `Z0>0 => Z0 is an ordinary balanced-row numerator`. The exact `u,v,W` countermodel satisfies the listed geometry and canonical-tail properties while producing `0<Zgeom<Y-2^ell`, below the universal balanced numerator minimum.

## RT6 — countermodel physical status

PASS. The Branch-A construction is labelled a combinatorial/method countermodel, not a physical cycle and not a counterexample to Collatz.

## RT7 — strategic overclaim

PASS. The closeout uses `PARENT_DIFFICULTY_DELTA = LATERAL`. One sign branch is genuinely removed, but the project-level all-scale ordinary/full-`D` ownership consumer remains absent.

## RT8 — frozen barriers

PASS. No fixed-depth generic scan, support-by-support grammar, bare modulus escalation, recurrence-only reformulation, RL147 independent-layer ownership assumption, demoted RL321 height-38 claim, or root-aligned `G<2^35` scope transfer is revived.

## Final red-team result

PASS for promotion with the scope and strategic classification recorded above.
