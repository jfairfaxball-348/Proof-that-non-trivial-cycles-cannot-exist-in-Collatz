# RL301 target-specific red team

Status: PASS for promoted scope.

Checks performed during closeout:

1. **Strict finite range.** The external certificate is used only for starts strictly below `46500000000000000000`. The controlling B-ancestor maximum is `38578560366951810319`, strictly below it. The next-record B-ancestor maximum `216988486345374634367` is strictly above it and is not claimed covered.
2. **External semantics.** The quantitative bound is derived from completed class-record coverage and the definition of class record as the least element of a delay class, not from convergence-only checks.
3. **Delay replay.** `D(28019077177231758495)=2456` is independently recomputed by the portable verifier.
4. **Ancestry sign.** Four removed half-steps are all odd, so `J_B=J_Y-4`, not `J_Y+4`.
5. **Single-trajectory sufficiency.** A genuine full phase requires both physical internal words to attain the same required weight; proving the B word cannot attain it is sufficient to exclude the candidate.
6. **Frontier off-by-one.** The first uncovered resonance is exactly `a=7354673373747273033`; the promoted frontier is exactly one less.
7. **No global overclaim.** Gate A and Gate B remain open. No global stopping or non-trivial-cycle theorem is inferred from the finite external certificate.
8. **Finite-ladder diagnosis.** Later resonance-envelope values are classified as exact route diagnostics, not as eliminated frontiers.

Result:

`RL301_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`.
