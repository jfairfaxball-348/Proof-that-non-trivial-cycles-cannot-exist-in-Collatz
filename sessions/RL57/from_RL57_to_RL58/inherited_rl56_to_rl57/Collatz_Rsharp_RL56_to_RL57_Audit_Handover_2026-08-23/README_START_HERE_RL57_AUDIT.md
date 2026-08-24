# START HERE — RL57 audit + focused proof handover

Date: 2026-08-23

This bundle hands the RL/3n+1 project from the RL56 aggregate-late-mass session into a deliberately skeptical RL57 audit/review session.

The new RL56 work is promising but **must not be promoted wholesale without audit**. The correct next move is to verify the inherited baseline, independently audit the new `Xi/Psi` potential and finite prefix certificates, and only then attack the now sharply localized `d<=2`, displacement-`<=1` terminal grammar.

## Mandatory first actions

1. Verify the outer ZIP against its `.sha256` sidecar.
2. Extract the bundle.
3. Run:

   `sha256sum -c SHA256SUMS_RL56_TO_RL57_AUDIT.txt`

4. Run:

   `bash verification/run_all_rl56_to_rl57_audit_verifiers.sh`

5. Read, in order:
   - `RL56_FINAL_PROOF_STATE_AND_RL57_AUDIT_ROADMAP.md`
   - `RL56_SESSION_INCREMENT_AND_AUDIT_TARGETS_2026-08-23.md`
   - `RL57_AUDIT_AND_FOCUSED_PROOF_KICKOFF_PROMPT_2026-08-23.md`
   - `RL56_AGGREGATE_POTENTIAL_AND_TERMINAL_COMPATIBLE_PREFIX.md`
   - `RL56_AGGREGATE_LATE_MASS_ATTACK_PLAN.md`
   - inherited `inherited_rl55_to_rl56/RL55_AUDIT_FINDINGS_AND_PROOF_STATE_2026-08-23.md`

Treat any checksum or verifier failure as a **stop-and-repair event**.

## Current live target after RL56

The strongest session-generated viable-prefix certificate says that every still-viable first-26 prefix satisfies

`Zx_26 <= 33/4`.

Combined with the inherited survivor requirement

`Zx > 143/12`,

this gives

`Zx_late > 11/3`.

The inherited exact defect identity and `E<5/3` then imply that more than `2/3` of late x-zero mass must have matching displacement at most one.

This is the key new localization. If RL57 can prove that terminal power/divisibility permits at most `2/3` total late x-zero weight in those near-aligned `d<=2` macros, the sole safe-CF survivor is eliminated.

## Important status distinction

The bundle deliberately distinguishes:

- inherited/audited results;
- RL56 analytic results with a reproducible verifier;
- fresh exact finite certificates that have been rerun but are still **independent-audit pending**;
- session deductions that should be reconstructed line-by-line before use;
- open conjectural closure steps.

Do not relabel a fresh script result as an analytic theorem.

## Global warning

Even elimination of the safe-CF survivor would not by itself prove global Gate A, construct a valid Gate B to the exact radius-3 theorem, close RL, or prove Collatz. Keep survivor-local and global claims separate.
