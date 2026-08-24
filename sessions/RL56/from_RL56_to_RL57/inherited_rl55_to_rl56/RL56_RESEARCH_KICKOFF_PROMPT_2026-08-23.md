# RL56 Research Session Kickoff Prompt

Continue the Collatz RL/3n+1 research from the attached `Collatz_Rsharp_RL55_to_RL56_Handover_2026-08-23.zip` as a skeptical research mathematician.

The previous session was an audit/review/roadmap reset. Do not re-litigate already audited branches unless a verifier fails. The next session should actively attack the highest-leverage missing lemma.

## Mandatory integrity/reproducibility step

1. Verify the outer ZIP against its `.sha256` sidecar.
2. Extract it and run:

   `sha256sum -c SHA256SUMS_RL55_TO_RL56.txt`

3. Run:

   `bash verification/run_all_rl55_handover_verifiers.sh`

4. Treat any failure as a stop-and-repair event.
5. Read `RL55_AUDIT_FINDINGS_AND_PROOF_STATE_2026-08-23.md` and `RL56_AGGREGATE_LATE_MASS_ATTACK_PLAN.md` before extending claims.

## Current exact target

The legal first-26 x-zero optimization is independently certified:

`Zx_26^legal,max = 34057930625026471931596 / 2954312706550833698643`

`= 11.528207745072855...`.

The inherited survivor requires

`Zx > 143/12`.

Hence every survivor must satisfy

`Zx_late > Delta`,

where

`Delta = 4590516512150518575599 / 11817250826203334794572`

`= 0.3884589215938109...`.

Your primary goal is to prove the contradictory uniform bound

`Zx_late < Delta`

under the full inherited safe-CF survivor hypotheses for every remaining odd `z>=41`.

## Primary attack — terminal aggregate mass, not pointwise tiny weights

Let

`R=z-27`, `K=q-z+3`, so `K+R=q-24`.

Work with the genuine late x-zero weights and terminal grammar. Seek an exact aggregate inequality. In particular:

1. Derive the late-mass expression/envelope from the inherited g/J/d dynamics rather than assuming all late weights are individually tiny.
2. Use `P=2^rJ`, with `r` the remaining late-zero count, and independently rederive all backward updates before relying on them.
3. Search for a telescoping or monotone potential controlling `sum w_j`.
4. Preserve divisibility, parity and height constraints when they strengthen the argument.
5. Split large-K and small/intermediate-K regimes if useful. Large K may permit a geometric tail bound; small K should be attacked using the huge complementary R together with the fixed endpoint `P_end=2^(q-24)`, not by enumerating R events.
6. If a theorem covers all but a bounded K-window, turn only that genuinely bounded remainder into exact finite certificates.

A theorem giving **any exact upper bound below Delta** is enough; do not waste effort optimizing constants beyond the contradiction threshold.

## Secondary attack — legal cut-state compression

If the aggregate potential route needs a prefix cut, rebuild it from legal prefixes.

The old relaxed-greedy schedule is illegal and dies at column 20. Therefore do **not** reuse the old `-1318<J_cut<1379` interval as if it described live trajectories.

Instead extend the legal-prefix DP/certificate to record possible states at the 26th legal x-zero. Try to prove bounded ranges/residue classes for `(d,J,g)` or a normalized P/W coordinate. A finite classification is useful only if the prefix state set is genuinely exhaustive and the suffix theorem is rigorous.

## z=41 fallback

Only if the uniform routes need diagnostics or reduce to low-z exceptions, continue the exact terminal frontier from `L_terminal(9,17)` and subsequent z=41 targets.

Do not spend the whole session marching z=41 -> z=43 -> z=45 without extracting a uniform mechanism.

## Critical audit corrections that must remain in force

- The phrase “greedy first 26” refers only to a relaxed x-only sequential-cap extremizer, not a legal full Markov prefix.
- z=37 and z=39 still stand: once the relaxed extremizer is forced, its local illegality supplies the contradiction.
- The fixed all-R `2^-1000` target is impossible for small K and is retired.
- `P=2^rJ` has a fixed endpoint but is not yet a proven monotone potential.
- The old bounded-J cut is conditional on an illegal relaxed cut and is demoted.
- `z>=41` is only inside the sole safe continued-fraction survivor.
- Gate A remains open globally.
- Gate B / a valid RL -> radius-3 bridge remains open.
- Do not revive the invalid RL49 half-period radius-3 shortcut.

## Strategic checkpoint before closing the session

At the end, classify what was achieved as one of:

1. uniform safe-CF survivor elimination via aggregate late mass;
2. a rigorous K-regime theorem plus bounded remainder;
3. a genuine P-potential/divisibility theorem;
4. a legal cut-state finite theorem;
5. only survivor-local/z=41 progress.

Then state explicitly whether the new result plausibly advances global Gate A / a radius-3 bridge or remains confined to the safe-CF survivor.

If the first three approaches prove inherently nonuniform, pivot the roadmap back toward the global Gate-A/Gate-B lemma rather than accumulating more z thresholds.
