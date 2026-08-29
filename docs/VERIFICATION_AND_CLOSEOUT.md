# Verification and atomic closeout

`AGENTS.md` is binding. This document is the canonical verification and promotion procedure after `CLOSEOUT_LOCK` has been entered and `CLOSEOUT_STATE.md` has frozen the proposed result.

Do not use this procedure to start research or to create a partial transition.

## Bundle convention

Preserve the repository's established handover convention unless an explicit infrastructure task changes it:

- an authoritative ZIP, or documented lossless transport reconstructed only in temporary storage;
- an outer `.zip.sha256` sidecar;
- an unpacked internal `SHA256SUMS.txt`;
- portable fast verifier scripts;
- the current report, proof/correction ledgers, session state, target, certificates, and required provenance.

Follow the actual current naming/layout rather than inventing a parallel format.

## Candidate contents

Build the candidate entirely under `.rl-work/RL<incoming_rl>/candidate/`. It normally contains the established equivalents of:

- completed research report and proof-state update;
- session-state/completion review and successor kickoff;
- exact successor target;
- certified-facts/proof ledger and correction/demotion ledger;
- required verifier scripts and certificates;
- authoritative bundle or transport;
- outer SHA-256 sidecar;
- internal manifest;
- fresh-unpack verification report;
- required red-team report;
- README/start-here material used by the current convention;
- `PROMOTION_MANIFEST.json`.

The handover must be self-contained for a worker with no producing conversation.

## Structural promotion manifest

`tools/rl_conveyor.py check-promotion` requires `PROMOTION_MANIFEST.json` with format `rl-promotion-candidate-v1` and these fields:

- `current_rl` (the incoming RL) and `next_rl` (the successor RL);
- `completed_session` and `next_authoritative`;
- `bundle` and `sidecar`;
- `fresh_unpack_report` and `red_team_report`;
- a nonempty `verifier_commands` list.

This manifest is structural. Passing it does not decide theorem validity, exact-range completeness, or scope.

## Pre-promotion verification gate

Run this gate without interleaving research:

1. Freeze the exact proposed proof/research state.
2. Classify every promoted item under `docs/PROOF_STATE_CLASSIFICATIONS.md`.
3. Record successes, barriers/dead routes, corrections/demotions, dependencies, open obligations, exact scope, and verifier status.
4. Prove every promoted finite certificate is gap-free over its exact claimed range; aggregate chunk coverage independently.
5. Run every required current red team and target-specific verifier.
6. Recompute live minima, floors, support edges, constants, or other quantities explicitly required by the target.
7. Build the complete candidate handover and bundle.
8. Compute the outer sidecar and any lossless-transport part hashes.
9. Fresh-unpack or reconstruct into a new clean temporary directory.
10. Verify the internal manifest from that clean unpack.
11. Run the complete required portable fast verifier suite from the clean unpack.
12. Confirm the fresh unpack reproduces the frozen candidate state and expected file identities.
13. Run `check-promotion` on the candidate.
14. Run `check-snapshot` against the start snapshot and confirm tracked `authoritative/` still matches `BASE_HEAD`.
15. Confirm there are no unexplained tracked changes and no candidate artifact has leaked into `authoritative/` or `sessions/`.
16. Refresh `CLOSEOUT_STATE.md` with every result, command, hash, and status. At this point the only remaining work should be final-tree assembly, catalogue regeneration/validation, one atomic Git transition, push, and readback.

Prefer the combined structural check where appropriate:

```sh
python3 tools/rl_conveyor.py preflight PATH_TO_AUTHORITATIVE_SNAPSHOT .rl-work/RL<incoming_rl>/candidate
```

If any step fails, do not promote.

## Failure classification

Classify the first failing dependency before repair:

- checksum, manifest, transport, bundle, catalogue, path, and Git-tree defects are mechanical unless they expose a separate proof-state problem;
- theorem, scope, exact-range, certificate-content, mathematical verifier, and required-red-team failures are mathematical/proof-state failures.

Repair a mechanical defect without changing proof classification. For a mathematical failure, explicitly record the correction/demotion and remaining valid scope. In both cases, perform only the minimum repair, rebuild all affected downstream artifacts, rerun the necessary checks through the full gate, and remain in `CLOSEOUT_LOCK`.

## Atomic repository transaction

Only after the pre-promotion gate passes may tracked authority/session state change. Assemble one coherent final tree:

1. Confirm `HEAD` still equals `BASE_HEAD`.
2. Freeze the completed incoming generation under the repository's established `sessions/RL.../` location.
3. Replace `authoritative/` with **only** the verified successor generation; do not leave mixed generations.
4. Preserve historical paths and provenance. Do not rename or delete history merely to simplify layout.
5. Regenerate the deterministic knowledge catalogues from the assembled final tree:

   ```sh
   python3 tools/rl_conveyor.py index-build
   python3 tools/rl_conveyor.py index-validate
   ```

6. Confirm `startup --json` resolves the proposed successor authority; retain the passing `index-validate` result as the evidence that the catalogue is current.
7. Stage only the completed-session, successor-authority, generated-catalogue, and directly required session-generated files belonging to this transition.
8. Inspect `git diff --cached --stat`, the complete staged path list, and the full staged diff.
9. Run a lightweight staged/final-tree sanity check where tooling permits.
10. Create one atomic commit using the established RL-transition naming convention.
11. Push or advance the intended remote branch/ref to that commit.
12. Read back the remote ref and require its SHA to equal the new commit.
13. Read the committed frozen session path and successor `authoritative/START_HERE.md`.
14. Re-run compact startup/catalogue sanity checks against the committed tree.
15. Confirm no half-transition or unexplained tracked change remains.

The invariant is:

> The commit contains the complete verified transition from one incoming authority to its successor, or it does not exist.

Do not amend a published RL commit. A local commit that has not reached the intended remote ref is not a completed closeout.

## Post-commit result

After successful remote readback, record the commit SHA, remote ref, frozen session path, successor incoming RL/target, and sanity-check results in the final report. Only then may a macro-session consider the successor start gate.

If push/readback cannot be completed, follow the interruption section of `docs/CLOSEOUT_LOCK.md`; the last remotely committed authority remains truth.
