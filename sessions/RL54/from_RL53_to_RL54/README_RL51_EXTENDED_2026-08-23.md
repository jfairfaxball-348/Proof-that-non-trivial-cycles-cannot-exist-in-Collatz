# RL51 extended checkpoint — 2026-08-23

Start with:

`rl51_research/RL51_EXTENDED_PROGRESS_AND_NEXT_ATTACK.md`

Then read:

- `rl51_research/RL51_Z29_COUPLED_ELIMINATION.md`
- `rl51_research/RL51_Z31_COUPLED_ELIMINATION.md`
- `rl51_research/RL51_Z33_REDUCED_TERMINAL_FRONTIER.md`

Latest verification:

`bash rl51_research/run_rl51_latest_verifiers.sh`

The inherited RL50 handover verifier remains:

`bash verification/run_all_rl50_handover_verifiers.sh`

Current stable result for the sole safe continued-fraction survivor:

`z >= 33`.

This does not prove Gate A, RL, or Collatz. The first open odd case is z=33, reduced exactly to a terminal suffix with at most 6 x-zero and 16 y-zero edges after u_26, with u_26<=81.
