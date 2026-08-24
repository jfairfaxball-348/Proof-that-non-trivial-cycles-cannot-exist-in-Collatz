# RL42 next-session kickoff

Continue the Collatz R-sharp / RL bridge research from the attached RL41->RL42 handover as a skeptical research mathematician.

## First actions

Read, in this order:

1. `RL41_PROOF_STATUS_AND_RL42_ATTACK.md`
2. `RL41_REPRODUCIBILITY_LEDGER.md`
3. `START_HERE_RL42.md`
4. the inherited RL40 handover and its proof-status note.

Verify checksums and rerun the retained arithmetic/RL40 verifiers. Treat every verifier discrepancy as a stop-and-repair event.

## Current mathematical checkpoint

The completed RL41 session reaches the working branch floor

`rho >= 28`

in the surviving near-resonant order-2 / `g=2` branch.

The low-area search now sees exactly two Diophantine near-resonances:

`(a,l)=(46,29)` and `(65,41)`.

Absolute Collatz numerator congruences eliminate all abstract survivors through total area 27 in the completed session.

Small useful modulus facts:

`2^46-3^29 = 39409 * 44110909`,

and `44110909` kills the encountered `(46,29)` candidates;

`2^65-3^41 = 19*29*17021*44835377399`,

and `323399=19*17021` kills the encountered area-27 `(65,41)` candidates.

Single-excursion configurations through area 28 are analytically impossible: a one-excursion return at the first near resonance requires `D >= 2^46+3^29`, while area<=28 gives `D<3^h<=3^29`.

## Important audit caveat

The area-26/27 search completed in RL41, but not all huge transient search sources/tables were retained. Reconstruct/rerun those two certificates before treating `rho>=28` as fully artifact-audited. The inherited `rho>=18` theorem is fully verifier-backed, and area<=25 enumeration/source fragments are retained.

Do not silently downgrade the session findings, but do not overstate reproducibility either.

## Primary research target — distortion versus concentration

Do **not** make `rho>=29` the primary goal.

RL39 proves the fixed-multiplicity correction

`C_l(q)=-R log(1-(z/R)2^(-(l-1)/2)3^(-q/l))`

is decreasing and convex in charge `q`, so raw transport can concentrate in one sacrificial high state. Therefore no linear product saving in total `rho` follows from RL39 alone.

Attack the missing bridge: prove that such concentration is incompatible with RL38 excursion geometry / exact distortion telescoping.

Try to derive a quantitative inequality connecting one state's large charge

`q=lH-log_3(2) l(l-1)/2`

to its excursion distortion `J_E`, scaled gap, valuation multiplicity, or compensating-excursion requirements.

Use the exact global identity

`prod_E J_E = z`,

with

`1 < z < sqrt(16/15)`.

A successful mechanism would be:

`one state absorbs large charge`
`=> its J_E is forced away from 1`
`=> other excursions must compensate`
`=> those excursions force additional owned charged states`
`=> RL39 correction saving becomes distributed rather than concentrated`.

Also investigate the complementary two-regime route:

- use RL36's sparse S-unit relation to eliminate `rho=o(L)`;
- use the distortion/charge-spread theorem for `rho` linear in `L`.

## Secondary target — finite falsification

After the bridge work is underway, use area 28 as a diagnostic:

- reconstruct the certified area-26 crossing table first;
- exploit the single-excursion analytic exclusion;
- search only genuinely new multi-excursion configurations;
- record the next resonance if one appears;
- test every candidate bridge inequality against exact survivors.

Do not keep increasing a constant floor without extracting a scalable theorem.

## Success criterion

Best case: prove a scalable charge-spread/direct-distortion theorem strong enough to combine with RL39 and close the `g=2` branch.

Otherwise: fully reconstruct the `rho>=28` certificate, make measurable progress on the bridge inequality, and freeze the sharpest falsification/counterexample information for the next session.

Maintain strict evidence discipline. RL remains open unless every dependency is actually closed and audited.
