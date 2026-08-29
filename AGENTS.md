# AGENTS.md — binding RL conveyor contract

## Purpose and authority

The repository, not conversation or model memory, carries this numbered mathematical research state:

`authoritative/` → one RL job → verified freeze in `sessions/RL.../` + successor `authoritative/`

**Incoming RL** is the job worked now; **handover generation** produced current authority; **successor RL** exists only after promotion. Each transition is a separate auditable commit.

Authority order is:

1. direct user instruction;
2. this file and nested `AGENTS.md`;
3. current `authoritative/`;
4. its proof-state, correction/demotion, and verification ledgers;
5. frozen `sessions/` and `Archive/`, only when needed;
6. generated knowledge catalogues;
7. conversation or memory.

`authoritative/` is the sole incoming mathematical state. `sessions/` and `Archive/` are history. Generated `knowledge/` catalogues are lookup caches only: they may be stale or absent without changing mathematical authority.

## Mathematical integrity and verification economy

Preserve the recorded distinction between analytic proof, exact finite certificate, inherited certificate, evidence, conjecture, barrier/dead route, correction/demotion, and open obligation. Definitions are in `docs/PROOF_STATE_CLASSIFICATIONS.md`.

Never promote evidence or incomplete coverage to theorem/certificate, a branch result to a global result, or silently strengthen scope, repair, demote, or reinterpret a claim. Preserve every handover scope qualification and named red team.

After the current checksum, internal manifest, clean fresh unpack, and fast suite pass, accept the frozen incoming ledgers under **verification economy**. Rerun expensive history only for an unresolved live dependency, current failure, genuine contradiction, required repair, or explicit handover instruction.

## Execution environments are peers

Both of these are first-class supported workers:

- **shell worker** — e.g. Codex/local clone, with Git and Python execution;
- **connector worker** — e.g. ChatGPT cloud with GitHub read/write/Git-object tools and a local sandbox, but no repository shell.

No RL rule may require a user to move a session from one environment to the other merely to complete routine startup or closeout.

Where this repository documents a shell command, a shell worker runs it. A connector worker performs the same underlying checks using available repository reads, local artifact verification, hashes, Git tree/blob identities, and atomic Git-object operations. It must report which checks were performed equivalently rather than falsely claiming a command ran.

Lack of a repository shell is not an integrity failure and is not a reason to leave a verified RL unpromoted.

## Start gate

Before mathematics, establish:

- current remote/default-branch HEAD (`BASE_HEAD`);
- the unique incoming RL and target from `authoritative/`;
- current proof/correction ledgers and required red teams/verifiers;
- incoming bundle/transport and outer sidecar;
- clean fresh unpack, internal manifest, and portable fast verifier result;
- a snapshot/identity of the incoming `authoritative/` state sufficient to detect concurrent change before promotion.

Shell workers should use:

```sh
python3 tools/rl_conveyor.py startup
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
```

Connector workers may establish the same gate through GitHub reads plus local/sandbox verification. Their scratch/checkpoint state may live in the current sandbox/conversation artifacts and need not be committed.

If the mathematical/incoming-integrity gate fails, do not begin ordinary research or mutate authority merely to make it pass. Follow stop-and-repair.

## Research, Git, and interruption

Keep scratch work non-authoritative. Shell workers use ignored `.rl-work/RL<incoming_rl>/`; connector workers may use local sandbox artifacts. Checkpoint material results and long-work boundaries. Mark partial computation **NOT PROMOTED** with its exact uncovered range.

During research, do not create a partial research-state commit, move authority into sessions, replace authority, push partial state, amend published history, or mix unrelated cleanup into the RL transition.

If interrupted, leave the last remote authority as truth and report the last verified checkpoint plus unpromoted remainder.

Research procedure: `docs/RL_RESEARCH_PROTOCOL.md`. State transitions: `docs/RL_STATE_MACHINE.md`.

## Stop-and-repair

Stop on any integrity/verifier failure, inherited contradiction, scope error, failed required red team, certificate range gap, invalidated live bound, incomplete work used as complete, or unexplained `BASE_HEAD` mismatch.

Freeze the last valid frontier and identify the first invalid dependency. A mathematical correction/demotion is only for invalid proof state. Checksum, packaging, transport, catalogue, path, or tooling-capability defects are mechanical and do not alone change mathematical classification.

A stale/missing knowledge catalogue is never by itself a stop-and-repair event for a numbered RL transition.

## CLOSEOUT_LOCK and promotion

Enter **`CLOSEOUT_LOCK` immediately** when the user asks to finish, close, hand over, commit/push, end/promote the RL, or when delay risks incomplete closeout.

Once locked, stop mathematics, scans, historical audits, route exploration, and optional improvements. Freeze/classify the candidate, run required red teams/verifiers, build/check the bundle and sidecar, fresh-unpack it, verify the manifest and fast suite, and confirm the incoming authority has not changed.

Promotion is one coherent transaction:

1. freeze the completed incoming generation under the established `sessions/` convention;
2. replace `authoritative/` with only the verified successor;
3. inspect the intended final path set/tree;
4. create one atomic RL commit;
5. advance the intended remote ref once;
6. read back the remote ref, frozen session, and successor authority.

With ordinary Git, stage/inspect/commit/push. With connector Git-object tooling, build blobs/tree/commit and move the ref once. Both are equally valid when the same atomic invariant is preserved.

A partial/local-only commit is not completion. Never combine numbered transitions; start another only after readback and a fresh start gate.

Read `docs/CLOSEOUT_LOCK.md`, then `docs/VERIFICATION_AND_CLOSEOUT.md`.

## Knowledge catalogue policy

`knowledge/session_catalog.jsonl`, `knowledge/result_catalog.jsonl`, and `knowledge/index_metadata.json` are deterministic performance aids, not authority and not part of the proof-state safety boundary.

- Shell workers should refresh and validate them during closeout when practical.
- Connector workers are **not required** to regenerate them.
- A numbered RL transition may be promoted with stale catalogues if all mathematical, packaging, authority-snapshot, atomic-commit, push, and readback gates pass.
- A worker must not claim a stale catalogue is current.
- Catalogue freshness may be restored in any later shell-capable session or dedicated infrastructure pass without consuming an RL number.
- When a catalogue is known or suspected stale, do not use its absence as evidence about mathematics; use exact authoritative sources or targeted repository lookup.

Catalogue maintenance is an optimisation, never a blocker that forces environment switching.

## Portability and infrastructure

Every handover must carry all load-bearing definitions, constants, scope, obligations, corrections, provenance, verifiers, and target for a worker with no conversation history.

Do not alter this protocol, repository architecture, verifier framework, or authority/session lifecycle during mathematical research. Infrastructure changes require an explicit dedicated task, consume no RL number, and must not mix into the same commit as a numbered mathematical promotion.

Linked phase documents elaborate this contract and may not weaken it.
