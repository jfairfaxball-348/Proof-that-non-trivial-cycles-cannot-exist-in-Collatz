# Verification and close-out

The incoming bundle convention is an outer `.zip.sha256` sidecar, an unpacked `SHA256SUMS.txt`, and portable fast verifier(s) in the bundle. Preserve that convention unless a future explicit infrastructure task changes it.

Before promotion, freeze the proposed state; classify results; record successes, barriers, corrections, dependencies, and obligations; prove every claimed finite range is gap-free; run the target's red teams; recompute live constants required by the target; build the bundle and sidecar; fresh-unpack it; check its manifest; run the complete required fast suite; and confirm the original authoritative snapshot still matches.

The candidate must remain under `.rl-work/` until all checks pass. Then, and only then, freeze the completed incoming generation under the existing `sessions/RL.../` convention, replace `authoritative/` with only the next generation, inspect the entire staged transition, and make one RL-transition commit. Do not stage partial research output, move a session early, or amend history.

The generic candidate manifest required by `tools/rl_conveyor.py check-promotion` is `PROMOTION_MANIFEST.json` with format `rl-promotion-candidate-v1`, current/next RL numbers, paths to the completed session, next authority, bundle, sidecar, fresh-unpack report, red-team report, and a nonempty verifier-command list. This structural check does not decide theorem validity.
