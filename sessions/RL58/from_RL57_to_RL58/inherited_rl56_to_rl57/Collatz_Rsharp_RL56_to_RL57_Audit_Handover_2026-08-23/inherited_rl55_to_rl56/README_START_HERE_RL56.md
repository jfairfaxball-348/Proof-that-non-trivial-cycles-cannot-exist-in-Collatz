# START HERE — RL56 extension handover

Date: 2026-08-23

This bundle follows the RL55 skeptical audit/review/roadmap session. The audit did **not** close RL, Gate A, Gate B, or Collatz. It did leave a cleaner and better-focused next target.

## Recommended next-session mission

Attack the **aggregate late-x-zero mass theorem** rather than continuing the abandoned fixed `2^-1000` pointwise target or doing z-by-z terminal enumeration by default.

The exact legal-prefix certificate gives

`Zx_26^legal,max = 34057930625026471931596 / 2954312706550833698643`

`= 11.528207745072855...`

while every inherited survivor requires

`Zx > 143/12 = 11.916666666666666...`.

Therefore a surviving trajectory must have late mass

`Zx_late > Delta`, where

`Delta = 4590516512150518575599 / 11817250826203334794572`

`= 0.3884589215938109...`.

So the main theorem target is the strict opposite inequality

`Zx_late < Delta`.

If that can be proved under the full inherited safe-CF survivor hypotheses uniformly for all odd `z>=41`, the sole safe-CF survivor is eliminated. That would be a major local/full-phase result, but **not yet a global proof of Gate A** and not by itself a valid RL -> radius-3 bridge.

## Mandatory first actions

1. Verify the outer `.sha256` sidecar supplied with this ZIP.
2. Extract the bundle.
3. Run:

   `sha256sum -c SHA256SUMS_RL55_TO_RL56.txt`

4. Run:

   `bash verification/run_all_rl55_handover_verifiers.sh`

5. Read, in this order:
   - `RL55_AUDIT_FINDINGS_AND_PROOF_STATE_2026-08-23.md`
   - `RL56_AGGREGATE_LATE_MASS_ATTACK_PLAN.md`
   - `RL56_RESEARCH_KICKOFF_PROMPT_2026-08-23.md`
   - inherited `RL53_FINAL_PROOF_STATE_AND_RL54_ROADMAP.md`
   - inherited `RL55_AUDIT_REVIEW_KICKOFF_PROMPT_2026-08-23.md` if audit provenance is needed.

Treat any checksum or verifier failure as a **stop-and-repair event**.

## Do-not-regress warnings from RL55 audit

- “Greedy first 26” means a **relaxed x-only sequential-cap extremizer**, not a legal full Markov prefix. That relaxed schedule dies at column 20.
- z=37 and z=39 remain intact after repairing this terminology: once their cascades force the relaxed extremizer, its local illegality already gives the contradiction.
- The old fixed `2^-1000` late-weight target cannot hold uniformly in `R`; do not revive it.
- `P=2^r J` is an exact and promising normalization with fixed terminal endpoint, but no monotone-potential theorem has yet been proved from it.
- The inherited `-1318 < J_cut < 1379` calculation depends on the illegal relaxed-greedy cut and is **not** presently a live-prefix finite classification theorem. Rebuild any cut theorem using legal prefixes.
- `z>=41` applies only to the one inherited safe continued-fraction survivor, not globally over denominators.
- Gate A remains open globally. Gate B / a valid global-to-radius-3 bridge remains open.
