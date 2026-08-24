# RL53 research kickoff prompt

Continue the RL/3n+1 research from this handover as a skeptical research mathematician.

First verify the outer SHA-256 sidecar. Extract the bundle and read:

1. `README_START_HERE_RL53.md`
2. `RL52_FINAL_PROOF_STATE_AND_RL53_ROADMAP.md`
3. `rl52_research/RL52_GATEA_Z33_Z35_TERMINAL_BOOTSTRAP.md`

Then run:

`bash rl51_research/run_rl51_latest_verifiers.sh`

`bash rl52_research/run_rl52_gatea_verifiers.sh`

Treat any verifier failure as a stop-and-repair event. Do not extend a failed certificate.

## Exact starting state

RL/Collatz is not closed.

The inherited radius-3 branch remains certified, but Gate B is open: RL49 proved the old half-period rotation has cyclic transposition distance `2(a-t-3+H)`, not radius 3. Therefore do not claim that Gate A alone automatically closes RL via radius 3.

Gate A `H>=t+3` remains the main global structural target, but the strongest strategic goal is a full-phase impossibility theorem that would bypass the failed direct Gate-B shortcut.

For the sole stable continued-fraction survivor, exact coupled terminal-power arguments have eliminated

`z=27,29,31,33,35`,

so parity gives the certified threshold

`z>=37`.

This threshold is not uniform over all denominators.

## Primary RL53 problem: z=37 one-x-zero terminal grammar

Do not return to the old independent/separable rank envelope. The productive mechanism is terminal-power + defect coupling.

At z=35 the bootstrap succeeded by repeatedly proving late x-zero weights terminal-near/negligible, feeding that back into `Zx>143/12` and `E<5/3`, shrinking the delayed-y budget, and rerunning a smaller exact terminal automaton.

For z=37, the first brute terminal class `(x<=1,y<=36)` is too large for the generic event recursion to be the right first move.

Exploit the special grammar of at most one x-zero:

- before and after the sole x-zero event, the backward word contains only `11` and `10`;
- therefore it is the composition of at most two x-zero-free predecessor segments plus one `00` or `01` event;
- solve or memoize the x-zero-free segment parametrically in the terminal 3-adic residue and remaining y-zero budget;
- compose the two segments exactly and seek a sharp finite maximum for `(1,36)`.

Use exact modular/3-adic arithmetic. Any finite-precision implementation must certify that no `v3` decision is ambiguous. Prefer a conservative grammar over heuristic positivity pruning.

## Required validation

Before trusting a specialized solver, reproduce known exact maxima from the generic event automaton, especially

`L_terminal(1,34)=85`.

Also regression-check one or more of

- `(6,16)=54` for z=33;
- `(3,18)=52`, `(5,16)=54`, `(7,14)=51`, `(8,12)=48` for z=35.

## If the first z=37 bootstrap closes

Immediately feed the terminal-near weight bound into the exact scalar/defect inequalities. Mirror the z=35 stages:

1. bound `p_26`;
2. bound the number of first-26 matching y-zeros delayed beyond `u_26`;
3. obtain a smaller total suffix `(x-zero,y-zero)` budget;
4. prove another exact terminal maximum;
5. iterate until all late x-zero weights are negligible or the mechanism genuinely stops.

If all ten late x-zero weights for z=37 become negligible, test whether the first-26 greedy schedule is forced and whether `u_26=70` again follows. Then use the five-delayed defect cost `2.059051471...>5/3` to localize the remaining y-zeros and run the final terminal class.

## High-value generalization

While attacking z=37, look for a parameterized theorem rather than merely another isolated case. In particular ask whether the bootstrap has a monotone invariant in z: terminal zero budgets, negligibility thresholds, or defect lower bounds that improve sufficiently to eliminate all odd `z>=27` in the retained survivor.

A genuine uniform statement would be much more valuable than continuing indefinitely case-by-case and could become the missing full-phase impossibility mechanism.

## Proof-state discipline

Separate in every note:

- analytic theorem;
- exact finite certificate;
- inherited dependency;
- computational exploration;
- conjecture/open target.

Do not promote exploratory z=37 computations to a theorem without a verifier. Do not state that Gate A, Gate B, RL, or Collatz is closed unless the full dependency chain is actually proved.

At the end of the session, update the proof-state ledger and package all new notes/verifiers with checksums for the next handover.
