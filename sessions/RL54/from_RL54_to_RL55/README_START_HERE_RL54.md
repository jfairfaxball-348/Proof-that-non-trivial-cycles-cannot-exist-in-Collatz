# RL53 -> RL54 handover — START HERE

Date: 2026-08-23

## First actions

1. Verify the outer ZIP against its `.zip.sha256` sidecar.
2. Extract the bundle.
3. Read `RL53_FINAL_PROOF_STATE_AND_RL54_ROADMAP.md`.
4. Read `RL53_TERMINAL_BOOTSTRAP_Z37_Z39.md`.
5. Run:

   `bash rl53_research/run_rl53_frontier_verifiers.sh`

6. Then rerun the inherited frontier suites if extending dependencies:

   `bash rl51_research/run_rl51_latest_verifiers.sh`

   `bash rl52_research/run_rl52_gatea_verifiers.sh`

7. Use `RL54_RESEARCH_KICKOFF_PROMPT_2026-08-23.md` as the next-session kickoff.

Any verifier failure is a stop-and-repair event.

## Current certified frontier

For the sole stable continued-fraction survivor:

`z >= 41`.

RL53 newly eliminates z=37 and z=39.

## Critical warnings

- RL and Collatz are not solved.
- Gate A remains open globally.
- Gate B remains open; RL49 killed the old direct full-phase -> radius-3 match.
- The inherited radius-3 theorem remains local and requires a valid bridge before it can close the global branch.
- The z-threshold applies only inside the inherited safe continued-fraction gate.

## Next target

Start z=41 with `(1,40)`, then use the terminal-near/defect bootstrap. In parallel, prioritize a parametric recurrence or monotone invariant that could eliminate all remaining odd z at once.
