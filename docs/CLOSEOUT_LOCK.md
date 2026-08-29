# CLOSEOUT_LOCK and reserved completion budget

`AGENTS.md` is binding. This document is the canonical detailed procedure for entering and remaining in `CLOSEOUT_LOCK`. Load it when the lock is triggered; it is not ordinary startup material.

## Purpose

An incoming RL job is not complete when research stops. Classification, candidate freezing, packaging, checksums, fresh-unpack verification, atomic repository promotion, remote-ref advancement, and post-commit readback are part of the same transaction. A worker must retain enough context, compute, and tool capacity to finish them safely.

## Closeout reserve

When usable capacity can be estimated, reserve approximately the final 15–20% for closeout. When it cannot, act conservatively: after a meaningful result or verifier milestone, stop further exploration once continuing could endanger a clean transition.

Do not launch a marginal lemma, scan, audit, or long computation at the expense of a complete handover. As soon as the promoted result is stable, prepare the compact closeout state below.

## Lock triggers

Enter `CLOSEOUT_LOCK` immediately when either:

- the user says words to the effect of **finish**, **finish up**, **close out**, **close session**, **make the handover**, **handover**, **commit/push**, or otherwise explicitly asks to end or promote the incoming RL; or
- the worker judges that the closeout reserve has been reached and delaying closeout risks an incomplete transition.

Only an explicit user instruction to resume mathematical research may unlock the job before successful promotion. A verifier, packaging, catalogue, Git, or push problem does not unlock it.

## Compact closeout state

Create or refresh:

`.rl-work/RL<incoming_rl>/CLOSEOUT_STATE.md`

It must be sufficient to finish without conversational memory. Record at least:

- `BASE_HEAD`;
- authoritative snapshot path and hash/tree identity;
- incoming RL, handover generation, and intended successor RL;
- exact target being closed;
- promoted results with their recorded classifications and scope;
- corrections/demotions, or an explicit statement that there are none;
- barriers, failed routes, dependencies, and remaining open obligations;
- candidate root and every candidate path needed for promotion;
- candidate file hashes or Git blob identities;
- exact certificate ranges and coverage status;
- verifier and red-team commands already run, with results;
- bundle, sidecar, internal-manifest, and fresh-unpack status;
- catalogue build/validation status;
- any active repair issue, classified as mechanical or mathematical;
- exact remaining deterministic operations;
- intended completed-session path and successor-authority paths;
- expected commit message, target branch/ref, and remote;
- outstanding processes, if any.

Once this record and the candidate handover are complete, earlier scratch discussion is non-load-bearing.

## Behaviour while locked

While `CLOSEOUT_LOCK` is active:

1. Start no new mathematics, scans, historical audits, route exploration, or opportunistic improvements.
2. Do not recursively reread frozen history to regain context. Use `CLOSEOUT_STATE.md`, the candidate handover, the current authoritative snapshot, and exact catalogue-returned sources.
3. Do not alter `authoritative/` or `sessions/` until the pre-promotion verification gate has passed.
4. Execute only the deterministic path:
   candidate freeze/classification → required red teams/verifiers → bundle/sidecar → clean fresh unpack → manifest/fast suite → snapshot check → final-tree catalogue build/validation → atomic Git transition → push/ref update → post-commit readback.
5. Treat packaging, hash, transport, catalogue, and path mismatches as mechanical closeout defects, not invitations to reopen research or alter proof classification.
6. If a check exposes a genuine proof-state error, identify the first invalid dependency and make the smallest explicit correction/demotion necessary for a valid candidate.
7. After either kind of repair, rebuild and reverify, then return directly to the locked path.
8. Prefer one atomic Git transition. With ordinary Git, assemble and inspect the complete tree, stage it once, commit once, push, and read the ref back. Direct Git-object tooling is acceptable when it preserves the same atomic invariant.
9. Do not amend a published RL commit or combine multiple numbered transitions.
10. Do not call the job complete until the intended remote branch/ref points at the new commit and committed `sessions/` plus `authoritative/` have been read back.

## Verification handoff

After `CLOSEOUT_STATE.md` shows that the result is frozen and only deterministic work remains, follow `docs/VERIFICATION_AND_CLOSEOUT.md` in order. Do not interleave optional improvements or restart the sustained attack.

The candidate remains under `.rl-work/` until the complete pre-promotion gate passes. A local bundle, verifier success, staged tree, or local commit alone is not authority.

## Failure or interruption

If the transition cannot be completed safely:

- terminate or account for outstanding processes;
- preserve the candidate and refresh `CLOSEOUT_STATE.md`;
- leave the last committed authority as truth;
- make no partial research-state promotion;
- report the exact completed checks, first failing check, last valid checkpoint, and exact resume operation.

If a local commit exists but has not reached the intended remote ref, report it as an incomplete closeout, not an authoritative transition. Do not begin the successor RL.
