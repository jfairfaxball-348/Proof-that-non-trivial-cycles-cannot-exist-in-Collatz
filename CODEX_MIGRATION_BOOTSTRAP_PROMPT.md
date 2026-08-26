# Codex Migration / Bootstrap Session Prompt

Use this prompt in a future ChatGPT session when I decide that this repository is ready to be prepared for Codex.

This prompt is deliberately independent of the current RL number, date, mathematical route, or current authoritative filenames.

---

I want to perform a **Codex migration/bootstrap session** for this RL research repository.

This is primarily an infrastructure/process session, not a new mathematical research attack.

## Core objective

Preserve the existing numbered RL “conveyor belt” research mechanism while making the repository safe and self-describing enough that future RL jobs can be executed interchangeably by ChatGPT or Codex.

The repository itself must become the authoritative state carrier. No future worker should require the conversational history of the worker that produced the previous session.

A long Codex macro-session may process several numbered RL jobs, but every RL job must remain an independent, auditable transaction with its own frozen handover and atomic repository transition.

## State independence

Do not assume any particular current RL number or filenames from this prompt.

Inspect the repository **as it exists when this prompt is run** and determine:

- the current authoritative RL generation;
- the existing `authoritative/`, `sessions/`, `Archive/`, and other repository conventions;
- the current proof-state / correction-demotion / verification-economy rules;
- current bundle/checksum/manifest/fresh-unpack conventions;
- current close-out conventions;
- existing scripts/verifiers that should be reused rather than duplicated.

Treat whatever is currently validly committed in `authoritative/` as the frozen current mathematical state.

Do not change mathematical claims merely as part of this migration.

## First protect the current research state

Before infrastructure work:

1. Confirm the repository working state and current HEAD.
2. Verify that the most recent RL research session has been properly closed according to its existing handover.
3. If the immediately preceding Chat session has already produced but not fully closed its RL handover, complete the normal RL close-out first.
4. Once a clean current authoritative state exists, freeze it as the migration baseline.
5. Do **not** start the next RL mathematical target during this bootstrap session.

## Install/audit the root AGENTS.md

There should be a root `AGENTS.md` defining the RL research conveyor protocol.

If one already exists, audit it rather than overwriting it blindly.

It must encode at minimum:

- repository state is authoritative, not chat/Codex memory;
- `authoritative/` is the single current incoming state;
- completed generations live in the repository's existing `sessions/` convention;
- historical archive conventions are preserved;
- proof-state classifications remain distinct;
- correction/demotion ledger is mandatory;
- verification economy;
- sustained attack;
- stop-and-repair triggers;
- branch/scope discipline;
- exact finite certificate / analytic theorem separation;
- support/red-team requirements inherited from the current handover;
- safe compute/chunking rules;
- cross-Chat/Codex portability;
- atomic promotion rule;
- no partial research-state commits.

Use the supplied/project version of `AGENTS.md` as the baseline if present.

## Create a non-authoritative working/checkpoint mechanism

I expect Codex runs to be long and they may end because of context, compute, or credit limits.

I want useful progress checkpointed without ever making a partial state authoritative.

Create a repository convention such as:

`.rl-work/`

and add it to `.gitignore`.

This directory is for:

- scratch calculations;
- resumable scan chunks;
- candidate certificates;
- candidate reports/handover files;
- command logs;
- checkpoint state;
- incomplete work.

It must never be treated as proof state merely because it exists.

Define a standard resumable checkpoint format, preferably including:

- `CHECKPOINT.md`;
- a machine-readable `STATE.json`;
- command/process log;
- artifact directory.

Each checkpoint must identify:

- base commit SHA;
- current RL number;
- current authoritative target;
- last fully verified result;
- exact completed certificate ranges;
- incomplete/unverified ranges;
- corrections/demotions discovered;
- verifier status;
- next intended step.

Checkpoints should be refreshed at sensible mathematical and computational milestones and before long expensive operations.

## Critical Git rule

This is the most important migration requirement.

**Codex must not create a research-state commit merely to save partial progress.**

During an unfinished RL job:

- do not move/delete/replace tracked `authoritative/`;
- do not move the current authoritative generation into `sessions/`;
- do not create a partial next authoritative state;
- do not commit half-complete certificates;
- do not push a partial RL state.

The currently committed authoritative generation must remain a safe recovery point throughout the entire in-progress job.

Only when the **complete next RL handover** has been frozen and independently verified may Codex perform the transition.

The final promotion should be one atomic transaction:

1. complete/freeze the current RL result;
2. build the complete next numbered handover in local staging;
3. create bundle, manifest and sidecar;
4. fresh-unpack it;
5. run the complete required fast verifier suite;
6. confirm all promoted exact ranges are gap-free;
7. confirm all required red teams pass;
8. confirm the original tracked `authoritative/` still matches the start-of-job snapshot;
9. move/freeze the completed current authoritative generation into the repository's existing `sessions/RL.../` convention;
10. replace `authoritative/` with **only** the fully verified next generation;
11. inspect the complete staged diff;
12. create one atomic RL transition commit using the existing naming convention.

If anything fails before step 12, no research-state commit should be made and the old authoritative state should remain intact.

## Credit/interruption behaviour

Design the workflow so that if Codex ends mid-job:

- the last committed `authoritative/` state is still valid;
- `sessions/` has not been half-updated;
- unfinished results are clearly non-authoritative;
- any locally surviving checkpoint gives an exact resume point.

Be explicit in the documentation that an ignored/uncommitted local checkpoint can only survive as long as the execution environment preserves it. Do **not** pretend otherwise.

If guaranteed persistence of unfinished work across disposable machines is desired later, document an **optional** user-approved mechanism (for example a dedicated non-authoritative checkpoint branch or external artifact/issue store), but do not enable partial-main-branch commits by default.

## Multiple RL jobs in one Codex macro-session

Document the desired loop:

`RLn research → verify → atomic promotion commit → RLn+1 research → verify → atomic promotion commit → ...`

A larger Codex context/compute budget should normally increase conveyor throughput rather than eliminate RL boundaries.

Each numbered RL transition gets its own independent close-out and commit.

If Codex stops between jobs, the repo is in a perfect handoff state.

If it stops inside a job, the previous committed authoritative generation remains the recovery state.

## Bootstrap documentation

Create or rationalise a small durable documentation set rather than one enormous manual.

At minimum create clear equivalents of:

- `docs/RL_RESEARCH_PROTOCOL.md`
- `docs/RL_STATE_MACHINE.md`
- `docs/CODEX_OPERATIONS.md`
- `docs/PROOF_STATE_CLASSIFICATIONS.md`
- `docs/VERIFICATION_AND_CLOSEOUT.md`
- `START_HERE.md` or another obvious repository entry point

Prefer `AGENTS.md` as a concise operational contract/table of contents, with detailed explanations in `docs/`.

Do not duplicate large quantities of historical mathematics into these process docs.

## Automation/tooling

Inspect existing tools first.

Where useful and safe, add small deterministic scripts for actions such as:

- reporting current authoritative RL generation;
- snapshotting/checking `authoritative/`;
- verifying incoming sidecar/manifest;
- creating/updating local checkpoints;
- validating gap-free scan ranges;
- building a candidate handover;
- fresh-unpack verification;
- checking that a promotion candidate is complete;
- preflight-checking the staged atomic transition.

Do **not** automate mathematical promotion criteria that genuinely require theorem-level judgement.

Any promotion script should fail closed: uncertainty or missing required files must prevent promotion.

## Preserve current repository conventions

Do not perform a broad cosmetic repository rewrite.

Preserve current path names, capitalization, RL numbering, historical folders, bundle conventions, and commit naming unless there is a concrete reason to change them.

If current repository structure differs from examples in this prompt, follow the actual repository and document the resolved convention.

Do not renumber old sessions.

Do not rewrite published history.

## Test the migration

Before declaring bootstrap complete:

1. run the new process checks against the **current** authoritative generation without altering its mathematical content;
2. simulate beginning a next RL job into the local checkpoint/staging area;
3. prove that an interrupted simulated job leaves tracked `authoritative/` and `sessions/` unchanged;
4. simulate/build a promotion candidate without actually promoting the mathematical state;
5. confirm the preflight correctly refuses incomplete candidates;
6. confirm all documentation paths/commands are valid;
7. inspect `git status` and repository diff carefully.

## Bootstrap commit

This infrastructure migration is not itself an RL mathematical transition.

Once the process/documentation/tooling changes are tested and the current mathematical authoritative state is confirmed unchanged, place the bootstrap infrastructure in one clearly named infrastructure commit, for example:

`Codex bootstrap: RL conveyor protocol and atomic promotion tooling`

Do not mix new Collatz/RL mathematical claims into that infrastructure commit.

If repository permissions/tooling in this Chat environment cannot safely make that commit, prepare the exact files and provide the exact commit instruction for me instead.

## Final bootstrap handover

At the end, give me:

- a concise description of the installed workflow;
- exact files added/changed;
- confirmation that current mathematical `authoritative/` state was not advanced;
- confirmation that no completed session was spuriously moved;
- checkpoint/resume behaviour;
- exact atomic promotion rule;
- bootstrap verifier/test results;
- bootstrap commit SHA if committed;
- the minimal prompt I should use to start the **first Codex research macro-session** from whatever RL generation is then authoritative.

Do not start that first Codex research attack during this bootstrap session.
