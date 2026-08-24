# START HERE — RL55 audit/review/roadmap handover

Date: 2026-08-23

This is an **audit/review/roadmap-setting session**, not a routine extension session.

RL and Collatz are **not solved**. Gate A remains open globally. Gate B / a valid global-to-radius-3 bridge remains open. The inherited exact radius-3 branch remains useful but must not be conflated with a global RL closure.

## First actions

1. Verify the outer `.sha256` sidecar supplied with this ZIP.
2. Inside the extracted bundle run:

   `sha256sum -c SHA256SUMS_RL54_TO_RL55_AUDIT.txt`

3. Run the lightweight audit suite:

   `bash verification/run_all_rl54_audit_verifiers.sh`

4. Read, in this order:
   - `RL54_FINAL_PROOF_STATE_AND_RL55_AUDIT_ROADMAP.md`
   - `RL53_FINAL_PROOF_STATE_AND_RL54_ROADMAP.md`
   - `RL54_UNIFORM_DEFECT_REDUCTION.md`
   - `rl54_research/RL54_LEGAL_PREFIX_UNIFORM_OBSTRUCTION_RUN.txt`
   - `RL55_AUDIT_REVIEW_KICKOFF_PROMPT_2026-08-23.md`

Treat any checksum or verifier failure as a **stop-and-repair event**.

## Main audit questions

The most important new RL54 claims to red-team are:

1. the exact z=41 self-seeding defect recurrence and the terminal caps it produces;
2. the exact finite certificate `L_terminal(8,17)=70`;
3. the claimed all-z uniform defect reduction to the relaxed family `(R,R+4)`;
4. the correction that a fixed `2^-1000` late-weight target cannot hold uniformly for all `R` because `K+R=q-24`;
5. the exact legal-prefix optimization giving
   `Zx_26^legal,max = 11.528207745...`;
6. the resulting replacement target
   `Zx_late < 0.3884589215938109...`;
7. the claim that the old greedy first-26 x-zero schedule is not a legal Markov prefix and dies at column 20;
8. the normalized terminal coordinate `P=2^r J` and the claimed fixed-endpoint / bounded-cut consequences.

Do not extend the research until these are classified as proved, exact finite certificate, inherited dependency, audit-pending computation, or conjectural/heuristic.
