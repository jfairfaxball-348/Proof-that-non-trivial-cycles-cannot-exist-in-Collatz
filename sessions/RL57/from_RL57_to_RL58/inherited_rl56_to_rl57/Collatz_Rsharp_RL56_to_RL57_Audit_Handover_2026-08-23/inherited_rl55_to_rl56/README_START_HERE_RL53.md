# RL52 -> RL53 handover — START HERE

Date: 2026-08-23

## First actions

1. Verify the outer ZIP against its `.zip.sha256` sidecar.
2. Extract the bundle.
3. Read `RL52_FINAL_PROOF_STATE_AND_RL53_ROADMAP.md`.
4. Run the current frontier checks:

   `bash rl51_research/run_rl51_latest_verifiers.sh`

   `bash rl52_research/run_rl52_gatea_verifiers.sh`

5. Use `RL53_RESEARCH_KICKOFF_PROMPT_2026-08-23.md` as the next-session kickoff.

Any verifier failure is a stop-and-repair event.

## Current certified frontier

For the sole stable continued-fraction survivor:

`z >= 37`.

The exact new RL52 closures are z=33 and z=35.

## Critical warnings

- RL and Collatz are not solved.
- Gate A is still open globally.
- Gate B is also open; the old direct full-phase -> radius-3 match is invalid.
- The inherited radius-3 theorem remains useful only if a valid global-to-local bridge is proved.
- The z-threshold applies only to the sole stable continued-fraction survivor, not all denominators.
- Do not revert to the old separable rank envelope as the main attack.

## Next target

z=37, beginning with the specialized one-x-zero terminal class `(1,36)`.

The recommended optimization is to decompose any such predecessor word into two x-zero-free `11/10` segments around the sole possible x-zero event. Use that specialized grammar to obtain the first terminal-nearness bound, then iterate the z=35 terminal/defect bootstrap.
