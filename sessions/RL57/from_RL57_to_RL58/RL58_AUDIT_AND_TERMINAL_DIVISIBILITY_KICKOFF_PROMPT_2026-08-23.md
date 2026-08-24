# RL58 audit and terminal-divisibility kickoff prompt

Continue the Collatz R-sharp/RL research from the attached `Collatz_Rsharp_RL57_to_RL58_Audit_Handover_2026-08-23.zip` as a skeptical research mathematician.

Do not assume that the two new RL57 discovery certificates are correct merely because they were exact computations. Begin with integrity and independent audit.

## 1. Integrity gate

Verify the outer handover checksum and run

`verification/run_all_rl57_to_rl58_verifiers.sh`.

Treat any failure as a stop-and-repair event. The inherited RL56->RL57 handover and its verifier suite are preserved under `inherited_rl56_to_rl57/`.

## 2. Fix the proof ledger before extension

Keep the following statuses distinct:

- inherited/audited baseline: `Zx>143/12`, `E<5/3`, `w_j<17/30`, exact defect identity, safe-CF survivor, radius-3 certification, open Gate A;
- promoted RL57 computation: `Zx_26<=33/4`, independently reproduced in exact C++;
- audit-pending RL57 computations: `Zx_26<=77/10` and aligned `M0_26<=17/3`;
- audit-pending local formulas: the exact `r=1` macro characterization and its entry valuation formula.

Do not state that Gate A, Gate B, RL, or Collatz is closed unless a new complete argument genuinely proves it.

## 3. Primary audit target — `M0_26<=17/3`

Reimplement the aligned-prefix decision structurally independently. Do not merely rerun `aligned_prefix_search.cpp`.

Audit every survivor-favouring condition:

- legal forward transition and forced-y rule;
- sequential x-zero cap and its strict endpoint;
- same odd `K>=25` selector for Xi/Psi terminal compatibility;
- W interval;
- Xi/Psi cut pruning;
- total-mass viability prune;
- new defect lower-bound prune
  `D_raw-(d-1)*17/45 <5/3`;
- aligned-objective future upper bounds;
- dominance/memo rule;
- strictness at the target `17/3`.

If independently verified, promote

`M0_late>5/4`.

Then also record the immediate consequences: at least three late aligned zeros and at least two separated late height-one `00` runs.

## 4. Secondary audit target — `Zx_26<=77/10`

Independently reimplement the defect-aware total-prefix search. If it survives, promote

`Zx_late>253/60`.

This is secondary to the aligned route unless it supplies a stronger terminal contradiction.

## 5. Reconstruct the local grammar exactly

Independently rederive, from the rank-matching definition and exact forward/backward maps:

- `r=0` iff the relevant x-zero is a height-one `00` edge;
- maximal aligned run length from `v2(Q-2)`;
- the exact displacement-one macro, expected to be `01(00)^(n-1)10`;
- whether `v2(3Q-7)=n` is exactly correct, including endpoint conventions;
- the exact potential increment/mass ratio for that macro.

If any of these differ from RL57 notes, repair the notes before using them.

## 6. Main proof attack if `17/3` survives

Use the exact backward grammar

`11: Q->2Q/3`,

`10: Q->2Q+1`,

`00: Q->2Q-(3^d-1)`,

`01: Q->2Q/3-3^(d-1)`

with

- terminal `Q_end=2^K+1`;
- odd `K>=25`;
- `v3(Q_end)=1+v3(K)`;
- strict late aligned requirement `M0_late>5/4`;
- per-zero cap `w<17/30`;
- at least two separated height-one `00` runs.

Try to prove the weak upper bound

`M0_late<=5/4`.

A weak upper bound suffices because the inherited/new lower bound is strict.

Focus on the arithmetic of the excursion between two aligned runs. Track `Q mod 3^n`, `v3(Q)`, `v2(Q-2)`, exact event counts, and weight scaling. The terminal `11` budget is controlled exactly by `1+v3(K)`.

Do not waste time trying to exclude a single final `00`: that configuration is not arithmetically impossible by itself.

## 7. Fallback

If the aligned certificate fails audit, retain the promoted `33/4` result and return to the RL56 mixed displacement target:

`M_{r<=1}>2/3`.

If the aligned certificate survives but a repeatable separated-`00` macro defeats `M0_late<=5/4`, identify that macro exactly, derive its Q-transform and weight evolution, and test terminal compatibility. If it reduces to an unrestricted Collatz-conjugate subsystem rather than a bounded arithmetic remainder, pivot back to the global Gate-A/Gate-B bridge problem rather than extending z-threshold computations indefinitely.

## 8. Desired end state for RL58

Best case: independently certify `17/3` and prove `M0_late<=5/4`, eliminating the safe-CF survivor.

Otherwise leave a clean audited ledger, an exact classification of the separated aligned-run grammar, and a sharply stated next missing lemma. Create the next handover only after separating proved theorems, independent finite certificates, audit-pending computations, and conjectural mechanisms.
