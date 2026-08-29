# Verification and close-out

The incoming bundle convention is an outer `.zip.sha256` sidecar, an unpacked `SHA256SUMS.txt`, and portable fast verifier(s) in the bundle. Preserve that convention unless a future explicit infrastructure task changes it.

## Closeout reserve and CLOSEOUT_LOCK

An RL job is not complete when the mathematics stops; packaging, fresh-unpack verification, repository promotion, remote ref advancement, and post-commit checks are part of the same job. Preserve enough remaining context/compute/tool budget to finish them. When capacity can be estimated, reserve roughly the final 15–20%; otherwise stop exploration conservatively once continuing could put a clean closeout at risk.

A user instruction such as **finish**, **finish up**, **close out**, **close session**, **handover**, or **commit/push** activates `CLOSEOUT_LOCK` immediately. Reaching the reserved closeout budget activates it proactively. Once locked, do not perform new mathematics, scans, historical audits, or optional improvements. Build or refresh `.rl-work/RL<current>/CLOSEOUT_STATE.md` and use it as a compact context-compression carrier for the remainder of the transaction. See `docs/CLOSEOUT_LOCK.md`.

Before promotion, freeze the proposed state; classify results; record successes, barriers, corrections, dependencies, and obligations; prove every claimed finite range is gap-free; run the target's red teams; recompute live constants required by the target; build the bundle and sidecar; fresh-unpack it; check its manifest; run the complete required fast suite; and confirm the original authoritative snapshot still matches. Do not interleave further research while this gate is running.

If a closeout check fails, enter only the minimum stop-and-repair necessary to correct the invalid dependency or packaging defect. Rebuild and reverify the candidate, then return directly to `CLOSEOUT_LOCK`; do not reopen the sustained mathematical attack unless the user explicitly instructs that.

The candidate must remain under `.rl-work/` until all checks pass. Then, and only then, freeze the completed incoming generation under the existing `sessions/RL.../` convention, replace `authoritative/` with only the next generation, inspect the entire staged/final-tree transition, and make one RL-transition commit. Do not stage partial research output, move a session early, or amend history.

Where direct Git-object tooling exists, prefer constructing the complete tree and commit and advancing the target branch/ref once. With ordinary local Git, stage the complete transition, inspect it, create one commit, and push it. **Closeout is not complete until the intended remote branch/ref points at the new commit and a post-commit read confirms both the frozen session generation and the new `authoritative/` generation.**

The generic candidate manifest required by `tools/rl_conveyor.py check-promotion` is `PROMOTION_MANIFEST.json` with format `rl-promotion-candidate-v1`, current/next RL numbers, paths to the completed session, next authority, bundle, sidecar, fresh-unpack report, red-team report, and a nonempty verifier-command list. This structural check does not decide theorem validity.