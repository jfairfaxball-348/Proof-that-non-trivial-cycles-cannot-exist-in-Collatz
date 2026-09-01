# RL225 red-team report

Date: 2026-09-01.

## Checks performed

1. **Authority check.** Re-read live `main` and the current `authoritative/` package/transport. Binding counts are the RL224 values 13,415,865,870 total and 7,091,831,283 above-p. No stale historical count is used.
2. **No e=16 transplant.** Re-derived the e=4 root progression only from RL211's exact e=4 equations and selector.
3. **Coordinate check.** Verified that RL214/RL215's two-sided bound is on the same absolute H21 root `y_0` used by RL211.
4. **Gap-free window.** Used exact floor/ceiling arithmetic to derive kmin/kmax and the complete candidate count.
5. **Terminal parity check.** Treated odd/even eta branches separately before solving the forbidden mod-2^22 residue.
6. **Candidate coupling.** Height propagation uses each cylinder's exact affine candidate trajectory; there is no free word completion.
7. **Partition check.** At every certified transition, surviving dyadic cylinders plus new failures reproduce the previous exact candidate count.
8. **Overlap check.** Directly replayed all 1,842 terminal-Hensel-forbidden k values through transition 41; none fails height by then.
9. **Scope check.** No e=4 rank deletion is claimed. e=28,33,40,45 are untouched.

## Result

No promoted RL225 claim failed red-team review. The correct conclusion is a strict exact finite e=4 candidate contraction, not terminal-rank exclusion.
