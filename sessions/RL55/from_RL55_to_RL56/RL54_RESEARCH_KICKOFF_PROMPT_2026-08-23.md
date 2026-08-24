# RL54 research kickoff prompt

Continue the RL/3n+1 research from this handover as a skeptical research mathematician.

First verify the outer SHA-256 sidecar. Extract the bundle and read, in order:

1. `README_START_HERE_RL54.md`
2. `RL53_FINAL_PROOF_STATE_AND_RL54_ROADMAP.md`
3. `RL53_TERMINAL_BOOTSTRAP_Z37_Z39.md`
4. `rl53_research/RL53_EXACT_TERMINAL_RESULTS.txt`

Then run:

`bash rl53_research/run_rl53_frontier_verifiers.sh`

Also run the inherited RL51/RL52 frontier suites before changing any inherited dependency:

`bash rl51_research/run_rl51_latest_verifiers.sh`

`bash rl52_research/run_rl52_gatea_verifiers.sh`

Treat any verifier failure as a stop-and-repair event.

## Exact starting state

RL/Collatz is not closed. Gate A remains open globally. Gate B remains open because RL49 showed the old half-period rotation does not have radius 3.

For the sole stable continued-fraction survivor, exact terminal/defect arguments have eliminated

`z=27,29,31,33,35,37,39`,

hence odd parity gives the certified threshold

`z>=41`.

This is not a uniform denominator theorem.

## Primary RL54 target: z=41

Use the RL53 mechanism, not the old separable rank envelope.

Start with the exact one-x-zero terminal class

`(x<=1, y<=40)`.

The specialized x-zero-free `11/10` solver, the `Q == 2 mod 3` trap, exact-x decomposition, and deterministic chunking are all available in `rl53_research`.

If `(1,40)` is terminal-small enough to force the last two late x-zero weights below `2^-1000`, feed that directly into the exact scalar/defect inequalities. At the cap-forced minimum `p_26=45`, seventeen delayed first-26 matching y-zeros already push the defect above `5/3`; therefore the first feedback should give delayed first26 <=16 and the next terminal target `(3,30)`.

Continue with monotone later cuts rather than fixing every stage at u26.

## Parallel high-value target: uniformization

Do not let RL54 become only another finite z case.

Build a parameterized model for odd z:

- number of late x-zero weights after the first 26;
- terminal class required to force the last 2,4,6,... weights tiny;
- exact delayed-y upper bound produced at each cut u_n;
- growth of the terminal maximum as `(X,Y)` grows.

Seek a monotone recurrence or invariant proving the bootstrap eventually closes for every odd z in the stable survivor. If such a theorem fails, identify the first exact obstruction and state it sharply.

A uniform full-phase impossibility statement could bypass the failed direct Gate-B radius-3 shortcut and would be strategically much more important than merely advancing the finite threshold.

## Proof-state discipline

Keep separate:

- analytic theorem;
- exact finite certificate;
- inherited dependency;
- audit-pending computation;
- heuristic/conjecture.

Do not claim Gate A, Gate B, RL, or Collatz is closed without the full dependency chain. Do not generalize the stable-survivor z-threshold to denominators outside the safe continued-fraction gate.

At session end, update the proof-state ledger and package all new verifiers/results with checksums.
