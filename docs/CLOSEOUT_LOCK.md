# Closeout lock and reserved completion budget

This document defines the compact closeout discipline used by both ChatGPT and Codex workers. `AGENTS.md` remains the binding operational contract.

## Why this exists

An RL session is not complete merely because the mathematics is complete. Packaging, checksum creation, fresh-unpack verification, atomic repository promotion, branch/ref advancement, and post-commit sanity checking are part of the job. A worker must therefore preserve enough remaining context, compute, and tool budget to finish those deterministic steps.

## Closeout reserve

Treat the final roughly 15–20% of a session's usable context/compute/tool capacity as a **closeout reserve** when that capacity can be estimated. If it cannot be estimated reliably, use judgement conservatively: after a meaningful promoted result or verifier milestone, stop further exploration once continuing could put a clean closeout at risk. A marginal extra lemma is lower priority than a complete, auditable repository transition.

As soon as the promoted result is stable, create or refresh `.rl-work/RL<current>/CLOSEOUT_STATE.md`. It should be a compact context-compression checkpoint containing at least:

- `BASE_HEAD` and authoritative snapshot identity;
- current RL and next RL numbers;
- promoted results and any correction/demotion;
- candidate file paths and hashes/blob identities;
- verifier/red-team/fresh-unpack status;
- any active stop-and-repair issue;
- the exact remaining closeout operations;
- the expected commit message and target branch/ref.

Once this file is sufficient, earlier conversational or scratch context is non-load-bearing for closeout.

## CLOSEOUT_LOCK triggers

Enter `CLOSEOUT_LOCK` immediately when either:

- the user says words to the effect of **finish**, **finish up**, **close out**, **close session**, **make the handover**, **commit/push**, or otherwise explicitly asks to end/promote the RL job; or
- the worker judges that the closeout reserve has been reached and delaying closeout risks an incomplete transition.

Only an explicit user instruction to resume mathematical research should unlock a session before successful promotion.

## Behaviour while locked

While `CLOSEOUT_LOCK` is active:

1. **Do not begin new mathematics, scans, historical audits, route exploration, or opportunistic improvements.**
2. Do not recursively reread frozen history merely to regain context. Use `CLOSEOUT_STATE.md`, the candidate handover, and the current authoritative snapshot.
3. Execute only the deterministic closeout sequence: freeze/classify → red teams/verifiers → bundle/sidecar → clean fresh unpack → manifest/fast suite → snapshot check → atomic Git transition → push/ref update → post-commit sanity check.
4. If a closeout check exposes a genuine error, enter the smallest necessary stop-and-repair, fix only the invalid dependency, rebuild/reverify the candidate, then return directly to `CLOSEOUT_LOCK`. Do not reopen the sustained attack.
5. Packaging or hash mismatches are closeout defects, not invitations to resume research.
6. Prefer one atomic Git transition. Where direct Git-object tooling exists, constructing the final tree/commit and moving the branch ref once is preferred to a chain of per-file commits. With ordinary local Git, stage the complete transition, inspect it, create one commit, and push it.
7. Closeout is not complete until the target remote branch/ref points at the new commit and a post-commit read confirms both the frozen `sessions/RL.../` generation and the new `authoritative/` generation.

If the transition cannot be completed safely, follow the interruption rule: make no partial research-state promotion, leave the last committed authority as truth, and record the exact resume point.
