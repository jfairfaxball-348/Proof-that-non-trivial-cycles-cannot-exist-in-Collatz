# RL195 Correction / Demotion Ledger

Date: 2026-08-31.

## Inherited mathematical corrections or demotions

**None new.** No inherited theorem, certificate range or live bound failed.
All prior correction/guardrail state remains in force. RL194's explicit
spacing>=1001 wording clarification is preserved; no stronger spacing is
claimed here.

## Explicit unpromoted verifier repair

The new owned-local seed helper advertised arbitrary compatible odd-modulus
classes but initially asserted that both starting states were nonzero
modulo3. Local uncoupled starting states may instead both be divisible by3;
their odd successors are automatically nonzero modulo3.

The reviewer reported the mismatch, new research paused, and the helper was
repaired to normalize odd residues and permit the valid initial classes.
All336 targeted helper regressions passed, including126 initially mod3-zero
cases. The original t=1 modulo3^5 full-path certificate and digest were
unchanged. Independent reread/replay and an alternative t=0 modulo3 replay
over all34039 final paths passed. The finding is closed.

This is a bounded verifier-interface repair before promotion, not an
inherited mathematical demotion or an unreported finite coverage change.

## Research hypothesis refinement

An early suggestion that odd integrality would always remain an additional
test after window reconstruction was rejected before final classification.
The proved denominator equivalence shows it is already forced by a complete
admissible word plus exact dyadic K0. It can remain missing in interval or
local relaxations. No opposite inherited claim was changed.

## Root-summary clarifications during closeout

The integration reviewer requested two precise wording repairs. The two
doublet d-weights have the same eta/theta coefficient, not the same weight;
their ratio remains4/3. The common reduced odd denominator belongs to y_i,
not to its integer numerator R_i. Both summary sentences were corrected to
match the already-reviewed proofs. No proof, numerical constant, certificate
range or inherited mathematical classification changed.

## Scope guardrails retained and extended

- Physical conclusions remain conditional on(37,0,23,-1).
- J00 counts chronological height-zero edges; it is neither the branch
  parameter J=23 nor a p-shifted zero pair, H21/clean-start or terminal count.
- N0, J00, q mass, necessary ranks, graph states, graph edges and graph paths
  are distinct statistics. No ownership multiplicity is inferred from them.
- Canonical floors and early signatures are not transported to arbitrary
  relabelings. K/rho/q have lambda-quasiperiodic lifts. The one-step physical
  height law is universal; the p-gap carry remains exceptional as recorded.
- Rank order is not chronological order; variation is not actual excursion.
- Height-only countermodels and local odd trajectories are not physical
  high-branch witnesses. In particular, they do not satisfy a complete exact
  fixed-K0 moment merely because they pass a few necessary constraints.
- One dyadic-gap integrality equivalence requires a complete globally
  admissible word. An interval, partial range or local CRT family cannot
  be substituted for that hypothesis.
- The terminal rank set/floors, prior sign tables, H21 budget, inherited
  flow/variation/spacing and all branch/global obligations remain unchanged.
