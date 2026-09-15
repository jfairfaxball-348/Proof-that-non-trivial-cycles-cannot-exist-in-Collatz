# RL327 red-team report

Date: 2026-09-15
Status: GREEN FOR CLOSEOUT

The independent red team was rerun from the corrected portable package. It does not merely compare headline constants. It cross-checks the structural assumptions used by the finite certificates.

## Checks

1. **Mechanical factor cells.** Independent cut-cell enumeration at lengths 47, 48, 49, 54, 73, and 99 agrees exactly with the verifier's `mechanical_factors` output, including discontinuity-adjacent cells.
2. **Endpoint band and parity.** Every retained singleton endpoint lies in the finite physical band, has the declared left/right lengths, and is odd. The promoted singleton range contains 1,528 high-carry endpoints.
3. **Two-positive shapes.** Exhaustive baseline-gap/height logic independently proves that the only positive length-two returns are `(1,1)` and `(2,1)`.
4. **Max-plus potential.** Every one of the 21,805 base automaton edges satisfies the stored potential inequality, and the semantic boundary recomputes to 72.
5. **Residue weighting.** `gcd(a,ell)=1` is rechecked. Closed power sums through degree four are tested against direct summation, and the weighted cap independently rederives as `32603663706`.
6. **Bootstrap automaton.** The corrected threshold layer independently checks 2,414 endpoints, 187 pair types, 9 links, boundary 1347, and rederives the final cap `32596612662`.
7. **Spot reconstruction.** Low, middle, and high retained endpoints are checked for oddness and admissible run lengths.

## Closeout rerun

Main verifier first line:

`RL327_OWNED_EXCESS_DENSITY_VERIFIER_GREEN`

Red team first line after the sibling-path packaging repair:

`RL327_OWNED_EXCESS_RED_TEAM_GREEN`

Result: **GREEN**.

The only defect found in the session was the scratch-only missing parity filter already frozen in `RL327_CORRECTION_AND_DEMOTION_LEDGER.md`; all affected counts were discarded and rerun before promotion.
