# Connector worker workflow: bounded work, resumability, and atomic closeout

`AGENTS.md` is binding. This document is the connector-specific operational procedure for ChatGPT/GitHub sessions. It changes no mathematical authority and never substitutes for proof-state verification.

## Goals

A connector worker should preserve exactly the same integrity guarantees as a shell worker while minimizing failure-domain length, context volume, repeated reads, and GitHub operations.

The normal connector lifecycle is:

`pin authority -> validate exact current inputs -> cache compact resume state -> bounded continuation work units -> CLOSEOUT_LOCK -> idempotent atomic Git transition -> exact readback`

The connector should avoid repository-wide discovery when exact current paths are already declared by authority.

## Startup: exact paths, not tree discovery

Pin:

- live default-branch `BASE_HEAD`;
- the commit's root tree identity when available;
- the committed `authoritative/` tree identity;
- the unique incoming RL and target from `authoritative/START_HERE.md`.

Read `AGENTS.md`, `authoritative/START_HERE.md`, and only the exact current files that entry point names. Read the target after the gate. Use narrow line/range reads when only one section is needed.

Do not, during normal startup:

- fetch a recursive repository tree;
- enumerate every file under `authoritative/` merely to find current files;
- preload `sessions/` or `Archive/`;
- fetch `knowledge/result_catalog.jsonl` or `knowledge/session_catalog.jsonl` in full;
- reopen inherited proof ledgers already validated by the current handover unless a live dependency requires their exact statement;
- rerun expensive historical verification after current incoming verification is green.

For flat Git-tree authority, the current committed tree/blob identities are the transport identity. A connector does not need to recreate ZIP-era discovery work merely because shell compatibility tooling supports it.

## Compact resume state

After the startup gate passes, keep one compact non-authoritative `RESUME_STATE.json` (or equivalent structured sandbox record). It is a cache and resumability aid, never mathematical authority.

Recommended shape:

```json
{
  "format": "rl-connector-resume-v1",
  "base_head": "<commit>",
  "authoritative_tree_oid": "<tree>",
  "incoming_rl": 0,
  "target": "authoritative/<target>",
  "authority_gate": {
    "status": "PASS",
    "validated_paths": [],
    "verifiers": []
  },
  "live_attack": {
    "paths": [],
    "frontier": "",
    "classification": "",
    "unpromoted_remainder": ""
  },
  "completed_operations": [],
  "artifacts": [],
  "do_not_recompute": [],
  "next_exact_operation": "",
  "stop_and_repair_active": false,
  "closeout": null
}
```

Keep it small. Store large outputs separately and record only their exact sandbox path plus digest/identity. `validated_paths` should be exact current dependencies, not a dump of every historical file ever consulted.

Before a later bare `continue`, fetch only the live remote/default-branch HEAD. If it still equals `base_head` and the cached authoritative tree identity is unchanged, resume from `next_exact_operation`. Do not replay startup or reread validated authority merely because a new user turn began.

If the remote HEAD changed, stop ordinary continuation until the change is understood. Do not silently graft old scratch work onto a different authority generation.

## Bounded continuation work unit

A kickoff research turn and every bare `continue` should execute one coherent attack unit.

A good work unit:

- begins from one exact recorded frontier;
- pursues one coherent attack or computation far enough to produce meaningful information;
- checkpoints before a long computation or expensive branch fan-out;
- records completed subcomputations and their identities before opening another expensive branch;
- normally ends at a theorem-sized/material mathematical checkpoint;
- may instead end at a **durable frontier checkpoint** when substantial useful work is complete but the theorem-sized endpoint is still materially distant.

A durable frontier checkpoint is not a micro-checkpoint. It must materially narrow, structure, verify, or classify the live attack and must contain an exact next operation. Its purpose is to bound the loss caused by client/model interruption.

Do not continue one turn merely because more mathematics is possible. Once a coherent work unit has produced substantial durable information, starting another expensive independent branch belongs to the next `continue` unless the endpoint is clearly near and closeout/context headroom is ample.

## Tool-call economy

Prefer exact-path reads and already-returned identifiers.

- Reuse the repository full name, `BASE_HEAD`, tree IDs, blob SHAs, issue/PR IDs, and exact paths already established in the session.
- Do not rediscover connector schemas or repository metadata repeatedly.
- Do not use broad code search when the exact file is already known.
- Do not fetch a whole file when a narrow line range answers the live question.
- Do not fetch a recursive Git tree for concurrency checking; a live default-branch HEAD comparison is sufficient when the incoming authority snapshot/tree is already pinned.
- Do not reload generated catalogues on each `continue`.
- Do not rerun current verifiers on ordinary continuation unless the current candidate/input affecting them changed or the protocol requires a specific milestone check.

## Research scratch and candidate preparation

Remote authority remains untouched during research. Connector scratch may contain:

- computation outputs;
- candidate theorem/proof text;
- prospective closeout files;
- hashes/digests;
- exact intended successor path list.

Preparing candidate file contents in scratch after a material result is encouraged when it reduces later closeout work. This is not promotion and must be clearly marked non-authoritative. Do not create partial RL commits or mutate `authoritative/`/`sessions/` before the candidate gate.

## CLOSEOUT_STATE

On `finish up`, enter `CLOSEOUT_LOCK` immediately. Convert the resume state into a compact, idempotent closeout record. Recommended phases are:

- `LOCKED`
- `CANDIDATE_READY`
- `VERIFIED`
- `BLOBS_READY`
- `TREE_READY`
- `COMMIT_READY`
- `REF_ADVANCED`
- `READBACK_DONE`

Record at least:

```json
{
  "format": "rl-connector-closeout-v1",
  "base_head": "<incoming commit>",
  "base_tree_oid": "<incoming root tree>",
  "authoritative_tree_oid": "<incoming authoritative tree>",
  "incoming_rl": 0,
  "successor_rl": 0,
  "phase": "LOCKED",
  "candidate_paths": {},
  "verifier_results": [],
  "red_team_results": [],
  "blob_oids": {},
  "candidate_tree_oid": null,
  "candidate_commit_oid": null,
  "ref_advanced": false,
  "readback": {},
  "remaining_operations": []
}
```

Persist immutable Git object IDs as soon as they exist. If a turn stops, reuse them rather than recreating equivalent blobs/trees/commits.

## Efficient connector Git-object closeout

For a connector Git-object transition, prefer this deterministic sequence:

1. Freeze the exact candidate in scratch and run all required verifier/red-team/candidate checks.
2. Record the exact changed/new/deleted path set. Do not enumerate unrelated repository paths.
3. Create blobs only for files whose content changes or is newly added. Reuse known blob IDs for identical content.
4. Create one candidate tree using the recorded incoming **base tree** plus only the changed path entries. There is no need to recreate unchanged blobs one-by-one.
5. Create one candidate commit with `BASE_HEAD` as parent.
6. Record the candidate tree and commit IDs in `CLOSEOUT_STATE` before any ref mutation.
7. At the latest safe point, fetch the live default-branch HEAD. Require it to equal `BASE_HEAD`.
8. Advance the intended branch ref once to the candidate commit.
9. Read back the branch ref and the exact critical paths: frozen session entry point/closeout record and successor `authoritative/START_HERE.md` plus the unique target identity.
10. Mark `READBACK_DONE` only after all required readback checks pass.

The final concurrency check is an identity comparison, not a reason to retrieve the full repository tree again.

## Idempotent closeout resume

After interruption, inspect `CLOSEOUT_STATE` before doing work.

- If `phase < BLOBS_READY`, continue only missing candidate/verification work.
- If blob IDs exist, reuse them.
- If a candidate tree exists, do not rebuild it unless candidate paths changed.
- If a candidate commit exists and the live ref still equals `BASE_HEAD`, reuse that commit after rechecking the candidate gate identities that could have changed outside Git.
- If the live ref already equals the recorded candidate commit, do not create another commit or move the ref again; perform only missing readback.
- If the live ref equals neither `BASE_HEAD` nor the candidate commit, stop on concurrency mismatch and inspect the intervening change.

This makes `finish up` safely restartable without weakening the atomic-transition invariant.

## Catalogue policy for connectors

The generated catalogues are historical lookup caches, not hot state. Current repository size makes full connector loading counterproductive. Treat them as cold storage:

- never load the full JSONL files during startup or ordinary continuation;
- use exact paths from current authority first;
- if inherited provenance is needed and the catalogue is known current enough, use the narrowest matching query/result;
- if it is stale for the needed generation, use a targeted exact repository lookup;
- do not regenerate the catalogues as part of a connector RL closeout.

Catalogue maintenance belongs to a shell-capable or dedicated infrastructure pass and must not block a valid numbered transition.

## User-facing checkpoint

At the end of each bounded work unit, report the mathematical result/classification, what remains open or unpromoted, and the exact durable resume frontier. The resume state itself stays non-authoritative and need not be pasted in full.

The purpose of this procedure is reliability: less repeated loading, smaller failure domains, exact resumption, and deterministic closeout with the same proof-state guarantees.
