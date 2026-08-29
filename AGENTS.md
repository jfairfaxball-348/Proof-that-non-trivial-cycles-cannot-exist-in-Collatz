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
6. conversation or memory.

`authoritative/` is the sole incoming mathematical state. `sessions/` and `Archive/` are history, not startup material. Scratch belongs only under ignored `.rl-work/RL<incoming_rl>/`. If inherited sources conflict, enter stop-and-repair and preserve the pointers.

## Mathematical integrity and verification economy

Preserve the recorded distinction between analytic proof, exact finite certificate, inherited certificate, evidence, conjecture, barrier/dead route, correction/demotion, and open obligation. Definitions are in `docs/PROOF_STATE_CLASSIFICATIONS.md`.

Never promote evidence or incomplete coverage to theorem/certificate, a branch result to a global result, or silently strengthen scope, repair, demote, or reinterpret a claim. A finite elimination or successful branch cannot by itself close a global Gate, all nontrivial cycles, or the Collatz conjecture. Preserve every handover scope qualification and named red team.

After the current checksum, internal manifest, clean fresh unpack, and fast suite pass, accept the frozen incoming ledgers under **verification economy**. Rerun expensive history only for an unresolved live dependency, current failure, genuine contradiction, required repair, or explicit handover instruction.

## Mandatory start gate

Before mathematics, run from the repository root:

```sh
python3 tools/rl_conveyor.py startup
python3 tools/rl_conveyor.py verify-incoming
```

After `verify-incoming` passes, run `python3 tools/rl_conveyor.py init-checkpoint`.

Together these identify the target/ledgers/red teams, record `BASE_HEAD` and the authoritative snapshot, check tracked state, and verify sidecar, manifest, fresh unpack, and fast suite. Read root `START_HERE.md`, then the current read set emitted by `startup`. Query history only for needed provenance.

If the gate fails, do not start ordinary research or mutate authority to make it pass. Follow stop-and-repair. Command details: `docs/CODEX_OPERATIONS.md`.

## Research, Git, and interruption

Keep all work under `.rl-work/RL<incoming_rl>/`. Checkpoint material results and long-work boundaries. Mark partial computation **NOT PROMOTED** with its exact uncovered range; it is never gap-free coverage.

Continue adjacent productive work only while verification and a complete closeout remain safe. Preserve closeout capacity. During research, do not stage outputs, create a research-state commit, move authority into sessions, replace authority, push partial state, amend published history, or mix unrelated cleanup into the transition.

If interrupted, account for processes, refresh the ignored checkpoint, leave authority/sessions unchanged, make no research-state commit, and report the last verified checkpoint plus unpromoted remainder.

Research/checkpoint/compute/reporting procedure: `docs/RL_RESEARCH_PROTOCOL.md`. State transitions: `docs/RL_STATE_MACHINE.md`.

## Stop-and-repair

Stop on any integrity/verifier failure, inherited contradiction, scope error, failed required red team, certificate range gap, invalidated live bound, incomplete work used as complete, or unexplained `BASE_HEAD` mismatch.

Freeze the last valid frontier and identify the first invalid dependency. A mathematical correction/demotion is only for invalid proof state; checksum, packaging, transport, catalogue, or path defects are mechanical and do not alone change classification. Do not promote until the complete gate passes.

## CLOSEOUT_LOCK and promotion

Reserve enough capacity for classification, packaging, clean verification, atomic promotion, push, and readback—approximately the final 15–20% when estimable. Enter **`CLOSEOUT_LOCK` immediately** when the user asks to finish, close, hand over, commit/push, end/promote the RL, or when delay risks incomplete closeout.

Once locked, stop mathematics, scans, historical audits, route exploration, and optional improvements. Use refreshed `CLOSEOUT_STATE.md`, the candidate, and the snapshot. Only explicit user instruction to resume mathematics may unlock the job.

Read `docs/CLOSEOUT_LOCK.md`, then execute `docs/VERIFICATION_AND_CLOSEOUT.md` without interleaved research. Failure permits only the minimum repair and a direct return to closeout.

Promotion is one coherent transaction: freeze the completed incoming generation under the established sessions convention, replace authority with only the verified successor, inspect the full tree, create one RL commit, advance the intended remote ref, and read back both frozen session and new authority. A partial/local-only commit is not completion. Never combine numbered transitions; start another only after readback and a fresh start gate.

## Portability and infrastructure

Every handover must carry all load-bearing definitions, constants, scope, obligations, corrections, provenance, verifiers, and target for a worker with no conversation history.

Do not alter this protocol, repository architecture, verifier framework, or authority/session lifecycle during mathematical research. Infrastructure changes require an explicit dedicated task, consume no RL number, and must not mix with a mathematical promotion.

Linked phase documents elaborate this binding contract and are required when their phase begins; they may not weaken it.
