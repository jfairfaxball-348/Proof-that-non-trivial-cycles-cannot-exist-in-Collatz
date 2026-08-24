# RL66 handover — start here

1. Read `RL66_SESSION_STATE_AND_KICKOFF_2026-08-24.md` for the authoritative outgoing proof/research state and the self-contained RL67 kickoff.
2. Read `RL66_LAST_ACTIVE_RANK_AND_PHASE_DIGIT_LADDER.md` for the new analytic mathematics.
3. Run `bash verification/run_fast_rl66_verifiers.sh` after verifying the outer ZIP sidecar and internal `SHA256SUMS.txt`.
4. Apply the **verification economy rule** after those RL66 checks pass: accept the frozen RL66 ledger as the inherited state; do not recursively rerun RL65/RL64 historical suites unless a new argument genuinely requires an unresolved definition, a verifier fails, or a contradiction triggers stop-and-repair.
5. `inherited/RL65_Rank_Tail_Phase_Selector_2026-08-24.zip` and its sidecar are the frozen incoming RL65 binary authority.

RL66 proves that canonical terminal `k` must be odd and derives an exact rank-tail phase-digit ladder. It does **not** prove odd-`k` Gate A, Gate B, RL closure, nontrivial-cycle exclusion, or the Collatz conjecture.
