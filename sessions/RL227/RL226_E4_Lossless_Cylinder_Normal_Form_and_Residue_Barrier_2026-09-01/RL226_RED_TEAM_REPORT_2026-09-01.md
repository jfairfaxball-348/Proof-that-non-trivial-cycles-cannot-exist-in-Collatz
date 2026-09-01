# RL226 red-team report

Date: 2026-09-01.

## Checks performed

1. Reproduced RL225 transition failures 36 through 41 exactly before accepting any new count.
2. Verified on every traversed state that `v2(u_i)=1`, the intercept is odd, `u_i=3^(i-36)U_36`, and `h_i=19+b(i)-b(36)-m`.
3. Verified that exact valuation `a` raises residue precision by exactly `a` and has one exact local residue class modulo `2^a`.
4. Extended exact gap-free counting through transitions 42 and 43.
5. Replayed all 1,842 terminal-Hensel-forbidden candidates independently through transition 43; overlap with height failure remains zero.
6. Constructed a same-phase/same-precision witness with different finite-window cylinder counts to prevent an invalid `(phase,m)` merge.

## Failure modes explicitly rejected

- Treating the valuation word as free rather than candidate-coupled.
- Replacing the finite k-window by a uniform 2-adic density argument.
- Dropping the residue/intercept merely because slope and height merge.
- Assuming terminal-Hensel disjointness beyond the replayed depth.
- Calling substantial contraction an e=4 rank deletion.
- Copying the e=4 normal form to other offsets without their own affine bridge.

## Verdict

The normal form and transition-43 counts are internally exact and verifier-backed. The e=4 family remains nonempty, so no rank/Gate/global promotion is permitted.
