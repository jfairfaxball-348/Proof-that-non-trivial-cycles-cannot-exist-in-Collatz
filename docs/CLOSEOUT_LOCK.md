# CLOSEOUT_LOCK and reserved completion budget

`AGENTS.md` is binding. This document is the canonical detailed procedure for closing an RL in either a shell worker or connector worker.

## Purpose

An incoming RL job is not complete when research stops. Classification, candidate freeze, packaging, clean verification, atomic repository promotion, remote-ref advancement, and post-commit readback are part of one transaction.

The worker must not require the user to migrate the job between Codex/local and ChatGPT/cloud merely to finish routine closeout.

## Lock triggers

Enter `CLOSEOUT_LOCK` when the user asks to finish/close/hand over/commit/push/promote, or when continued research threatens a complete closeout.

Only an explicit instruction to resume mathematics unlocks the job before successful promotion.

## Compact closeout state

Maintain a compact non-authoritative closeout record sufficient to finish without conversation memory. Shell workers normally use:

`.rl-work/RL<incoming_rl>/CLOSEOUT_STATE.md`

Connector workers should keep the equivalent structured state in sandbox artifacts and follow `docs/CONNECTOR_WORKFLOW.md`.

Record at least:

- `BASE_HEAD`, incoming root tree identity, and authoritative snapshot/tree identity;
- incoming and successor RL;
- exact target;
- promoted results and classifications;
- corrections/demotions;
- barriers/dependencies/open obligations;
- candidate paths/hashes;
- verifier/red-team results;
- bundle/sidecar/manifest/fresh-unpack status;
- intended session and successor-authority paths;
- intended commit/ref;
- connector Git object IDs already created (blob/tree/commit) and current closeout phase;
- whether the ref has advanced and which readback checks are complete;
- catalogue freshness status (`current`, `stale/deferred`, or `not checked`);
- exact remaining deterministic operations.

Treat created Git blobs, trees, and commits as immutable reusable closeout artifacts. Do not recreate them after interruption unless their intended content/path set changed.

## Behaviour while locked

1. Start no new mathematics, scans, historical audits, route exploration, or opportunistic improvements.
2. Do not alter remote `authoritative/` or `sessions/` until the candidate verification gate passes.
3. Execute only: candidate freeze/classification → required red teams/verifiers → bundle/sidecar or flat-tree candidate → clean verification → authority snapshot check → atomic Git transition → push/ref update → post-commit readback.
4. Treat packaging, hash, transport, path, catalogue, and execution-environment limitations as mechanical matters unless they expose a proof-state problem.
5. If a genuine proof-state error appears, make the smallest explicit correction/demotion necessary, rebuild/reverify, and return directly to closeout.
6. Prefer one atomic Git transition. Ordinary Git and direct Git-object tooling are both valid.
7. Do not amend a published RL commit or combine numbered transitions.
8. Do not call the job complete until the intended remote ref points at the new commit and committed `sessions/` plus `authoritative/` have been read back.

## Connector-efficient closeout

For connector Git-object tooling:

1. finish and hash the candidate files in scratch before any branch/ref mutation;
2. determine the exact changed/new/deleted path set only;
3. create blobs only for changed/new content and record each returned object ID in `CLOSEOUT_STATE`;
4. build one candidate tree from the recorded incoming base tree plus those changed/deleted entries, rather than enumerating/recreating unchanged repository blobs;
5. create one candidate commit with `BASE_HEAD` as parent and record its ID;
6. fetch the live default-branch HEAD immediately before the ref move and require it to equal `BASE_HEAD`;
7. advance the ref once;
8. read back the ref and exact critical frozen-session/successor-authority paths.

Do not fetch a full recursive repository tree merely for the final concurrency check. If closeout is interrupted, resume from the first incomplete phase recorded in `CLOSEOUT_STATE`. If the ref already equals the recorded candidate commit, skip object creation/ref movement and complete only missing readback.

## Catalogue handling

Knowledge catalogues are optional optimisation caches. They are not part of the mathematical promotion gate.

If a shell is available, refresh/validate them when practical. If no repository shell is available, or catalogue regeneration would otherwise force an environment handoff, leave them unchanged and explicitly report them as stale/deferred. This does not block the RL commit.

Never hand-edit generated catalogue files to simulate a successful build. Connector workers should not load the full catalogue JSONL files during closeout merely to report freshness.

## Failure or interruption

If safe atomic promotion cannot be completed:

- preserve the candidate/closeout record, including immutable Git object IDs already created;
- leave the last remotely committed authority as truth unless the recorded candidate commit is already the live ref;
- make no partial research-state promotion;
- report the first failing gate and exact resume operation.

A stale catalogue alone is not such a failure.
