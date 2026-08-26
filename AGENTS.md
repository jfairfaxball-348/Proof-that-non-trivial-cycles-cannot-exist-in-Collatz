# AGENTS.md — RL Research Conveyor Protocol

## Purpose

This repository is a long-running mathematical research project organised as a sequence of numbered RL research jobs.

The repository, not any ChatGPT or Codex conversation, is the authoritative carrier of project state.

A model session is only a worker. It may be ChatGPT, Codex, or another compatible environment. No important proof state may depend on conversational memory.

The core operating model is a conveyor belt:

`authoritative/` → work one RL job → verify/freeze → `sessions/RL.../` + new `authoritative/` → next RL job

A single long Codex run may complete several RL jobs, but every RL job remains an independent, auditable transaction with its own handover and commit.

---

## 1. Repository state model

Use the repository's existing path names and conventions. In particular:

- `authoritative/` contains the **single current incoming RL state** from which new research is allowed to proceed.
- `sessions/` contains frozen completed RL session states using the repository's established numbering/layout.
- `Archive/` contains older historical material according to the repository's existing archival convention.
- `.rl-work/` is the preferred **local, non-authoritative working/checkpoint area** for Codex research. It must be gitignored.
- Existing repository documentation, verifier scripts, manifests, ledgers, naming conventions, and handover conventions take precedence over invented replacements unless a user explicitly requests a migration.

Do not treat an old session file, old chat, old Codex transcript, or unverified scratch result as current proof state merely because it exists.

---

## 2. Authority hierarchy

For mathematical/research work, use this priority order:

1. direct user instruction for the current task;
2. this `AGENTS.md` and any more specific nested `AGENTS.md`;
3. current files in `authoritative/`;
4. current proof-state / correction-demotion / verification ledgers carried by the authoritative handover;
5. frozen completed material in `sessions/` and `Archive/`, consulted only when needed;
6. model memory or conversational history.

If two inherited claims conflict, do not choose silently. Trigger stop-and-repair and record the conflict.

---

## 3. Non-negotiable proof-state classifications

Preserve explicit distinctions between at least:

- proved analytic mathematics;
- exact finite certificates;
- externally inherited certificates;
- computational evidence;
- conjectures;
- method barriers / dead routes;
- repaired or demoted claims;
- open obligations.

Do not promote evidence to theorem.

Do not promote a branch-specific exclusion to a global theorem.

Do not silently strengthen scope.

Do not silently repair an inherited statement. Record repairs/demotions explicitly.

Any claim of global Gate closure, RL/nontrivial-cycle exclusion, or Collatz closure requires the actual inherited proof obligations to be discharged. Never infer such closure merely from a large finite elimination or a successful branch computation.

---

## 4. Verification economy

Apply the repository's verification-economy rule.

After the current authoritative bundle checksum, internal manifest, supplied fresh-unpack verification, and current fast verifier suite pass, accept the frozen incoming proof-state ledger as the authoritative inherited state.

Do **not** recursively rerun historical expensive certificates unless at least one of these occurs:

- a new argument depends on an unresolved historical definition or certificate;
- a current verifier fails;
- a genuine apparent contradiction appears;
- a stop-and-repair event requires historical reconstruction;
- the authoritative handover explicitly requires the rerun.

Spend compute primarily on the live mathematical obstruction.

---

## 5. Sustained attack rule

An RL job should be manageable and auditable, but a successful theorem, scan chunk, endpoint elimination, support change, or local milestone is a **checkpoint**, not automatically a close trigger.

Continue the live attack through adjacent productive steps while:

- the route remains mathematically useful;
- verification remains reliable;
- compute/context/credit pressure is not threatening correctness;
- no stop-and-repair event has occurred.

For a long Codex macro-session, additional capacity should normally increase **the number of complete RL jobs processed**, not destroy RL granularity by turning many jobs into one huge indivisible session.

---

## 6. Start-of-RL gate

Before new mathematics for an RL job:

1. Read the current `authoritative/` state and identify:
   - current RL number;
   - next target;
   - frozen proof-state ledger;
   - correction/demotion ledger;
   - required red teams;
   - required verifier suite;
   - inherited constants and exact certificates.
2. Record the current Git `HEAD` as `BASE_HEAD`.
3. Record a machine-checkable snapshot of the current `authoritative/` tree, preferably:
   - paths;
   - sizes;
   - hashes or Git blob/tree identities.
4. Confirm the working tree is clean apart from permitted ignored local work.
5. Verify the incoming sidecar/checksum.
6. Verify the incoming internal manifest.
7. Run the supplied fresh-unpack/fast verifier gate.
8. If the gate passes, apply verification economy.
9. If the gate fails, do **not** begin ordinary new research. Enter stop-and-repair.

Do not mutate `authoritative/` merely to make the start gate pass.

---

## 7. Working area and checkpoint discipline

### 7.1 Default working area

During research, write scratch work, scan outputs, temporary certificates, candidate reports, logs, and resumable checkpoints under:

`.rl-work/<current-RL>/`

This area is **not authoritative** and must be excluded by `.gitignore`.

Do not use `authoritative/` as a scratch directory.

Do not use `sessions/` as a scratch directory.

### 7.2 Sensible checkpoint moments

Create or refresh a checkpoint after any materially useful event, including:

- completion of a meaningful exact scan batch;
- establishment of a new lemma/theorem candidate;
- exact interval propagation;
- support-edge or geometric crossover;
- discovery of a new global minimum/floor;
- any correction or demotion;
- successful verifier milestone;
- before launching a long or expensive computation;
- after a long computation completes;
- before a likely context/credit boundary;
- before switching mathematical routes.

### 7.3 Checkpoint contents

A checkpoint should make resumption possible without conversational memory. At minimum record:

- `BASE_HEAD`;
- current RL number;
- authoritative incoming target;
- timestamp;
- last fully verified mathematical checkpoint;
- new proved results, clearly classified;
- completed exact finite certificates and their exact ranges;
- incomplete/partial computations, explicitly labelled **NOT PROMOTED**;
- current constants/minima/floors/endpoints where relevant;
- verifier commands already run and results;
- failed commands or abandoned routes;
- files produced in `.rl-work/`;
- next intended command or mathematical step;
- whether a stop-and-repair condition is active.

Recommended files:

- `.rl-work/<RL>/CHECKPOINT.md`
- `.rl-work/<RL>/STATE.json`
- `.rl-work/<RL>/commands.log`
- `.rl-work/<RL>/artifacts/`

A partial scan is never equivalent to a gap-free certificate. Preserve partial output if useful, but mark it unverified and never promote it as exact coverage.

### 7.4 Credit/interruption rule

If the run is ending before a complete RL promotion is ready:

- update the local checkpoint;
- terminate or account for outstanding processes;
- leave `authoritative/` unchanged;
- leave `sessions/` unchanged;
- make **no research-state commit**;
- report the exact last fully verified checkpoint and the exact unverified remainder.

This protects the authoritative repository even if a long Codex run ends unexpectedly.

Important limitation: uncommitted local checkpoint files are only as persistent as the execution environment that stores them. If guaranteed cross-machine survival of unfinished work is later required, configure a separate explicit persistent checkpoint channel (for example a dedicated non-authoritative branch, issue/artifact store, or other user-approved mechanism). Do **not** silently weaken the no-partial-commit rule.

---

## 8. Git safety rule — no commit until atomic promotion

This rule is strict.

During an in-progress RL job, do **not**:

- `git add` research outputs for commit;
- create a research-state commit;
- move current `authoritative/` material into `sessions/`;
- replace current `authoritative/` with candidate next-session material;
- push a partial RL state;
- amend or rewrite published history;
- mix unrelated repository cleanup into the RL promotion.

The current authoritative state must remain recoverable and unchanged until the replacement state is proven ready.

If tracked files outside the intended final promotion are modified accidentally, inspect and repair those changes before continuing. Never discard user changes blindly.

---

## 9. Stop-and-repair conditions

Stop ordinary promotion logic and enter repair mode if any of these occurs:

- checksum/manifest failure;
- verifier failure;
- a newly discovered floor/minimum invalidates a promoted bound;
- an apparent contradiction between inherited results;
- a proof uses a scope stronger than its premises;
- physical/quotient representative separation is violated;
- a required red-team check fails;
- a supposedly exact certificate has a range gap;
- a supporting-edge or optimization claim was inherited without required revalidation;
- an incomplete computation was accidentally used as complete evidence;
- repository state no longer matches `BASE_HEAD` in an unexplained way.

In repair mode:

1. freeze the last unquestionably valid state;
2. identify the first invalid dependency;
3. demote/repair explicitly;
4. rerun only the verification necessary to restore a trustworthy frontier;
5. do not promote until the corrected state passes the complete close-out gate.

---

## 10. Preparing a candidate next RL state

Build the candidate next session under `.rl-work/`, not in `authoritative/`.

Follow the repository's current file naming and bundle conventions rather than inventing a parallel format.

A candidate next RL state normally includes the repository's established equivalents of:

- complete research report / proof-state update;
- session-state and next-RL kickoff;
- next authoritative target;
- authoritative bundle/archive;
- SHA-256 sidecar;
- internal manifest;
- fresh-unpack verification report;
- verifier scripts/certificates needed by the next session;
- README/start-here material if that is part of the current convention.

The candidate handover must be self-contained enough that **either ChatGPT or Codex** can continue from GitHub without access to the producing conversation.

---

## 11. Close-out verification gate

Before changing tracked authoritative/session state:

1. Freeze the exact proposed proof/research state.
2. Classify every new result.
3. Record:
   - successes;
   - failures/dead routes;
   - corrections/demotions;
   - dependencies;
   - open obligations;
   - verifier status.
4. Ensure every promoted exact certificate is gap-free over its claimed range.
5. Rerun all required current red teams.
6. Recompute any live minima/floors/support edges/constants that the authoritative target requires.
7. Build the next numbered bundle.
8. Build its sidecar/checksum.
9. Fresh-unpack the bundle into a clean temporary directory.
10. Verify its internal manifest.
11. Run the complete fast verifier suite from the fresh unpack.
12. Confirm the fresh unpack reproduces the proposed frozen state.
13. Confirm the current tracked `authoritative/` still matches the snapshot taken at `BASE_HEAD`.
14. Confirm there are no unexplained tracked changes.

If any step fails, do not promote.

---

## 12. Atomic promotion transaction

Only after Section 11 passes may the repository transition to the next RL job.

The promotion must be one coherent Git transaction.

Using the repository's existing convention:

1. Freeze the completed current authoritative session under the appropriate `sessions/RL.../` location.
2. Replace `authoritative/` with **only** the fully verified next-session authoritative files.
3. Do not leave a mixture of old and new authoritative generations.
4. Preserve historical material; do not delete history merely to simplify the tree.
5. Stage only the intended completed-session + new-authoritative transition and any directly required session-generated files.
6. Inspect `git diff --cached --stat`.
7. Inspect the complete staged diff or equivalent file list.
8. Re-run a lightweight state sanity check against the staged tree if tooling permits.
9. Create **one atomic commit for that RL transition**, using the repository's established RL commit naming convention.
10. Do not amend an earlier published RL commit.

The essential invariant is:

> The commit either contains the complete verified transition from current authoritative RL state to next authoritative RL state, or it does not exist.

No half-promoted authoritative state is acceptable.

---

## 13. Multiple RL jobs in one Codex macro-session

A long Codex run may continue after a successful atomic promotion.

But every transition remains independent:

`RLn → commit → RLn+1 → commit → RLn+2`

Never combine several numbered RL transitions into one giant commit merely because Codex has more context or compute.

After each successful promotion:

1. verify the new commit/worktree state;
2. treat the newly written `authoritative/` as a fresh incoming session;
3. reset `BASE_HEAD`;
4. rerun the ordinary start-of-RL gate;
5. continue only if compute/context/reliability are healthy.

If the macro-session ends between RL jobs, the repository is already in a valid handoff state.

If it ends during an RL job, Section 7.4 applies and the last committed authoritative state remains valid.

---

## 14. Branch/scope discipline

Preserve all scope limitations carried by the authoritative state, including first-Farey/full-phase or other branch qualifications.

Do not restart previously rejected/dead methods unless:

- the live target explicitly reopens them; or
- genuinely new structure invalidates the old barrier.

When the current target requires support-edge re-optimization, population accounting, physical representative separation, primitivity, reset-family checks, or other named red teams, perform them exactly as required by the authoritative handover.

---

## 15. Compute discipline

Use available compute aggressively but reproducibly.

Prefer:

- bounded parallelism over uncontrolled oversubscription;
- deterministic exact arithmetic where the proof state requires exactness;
- chunked scans with explicit ranges;
- resumable outputs;
- machine-readable summaries;
- checksums/manifests;
- independent aggregation/verifier passes.

If a large parallel run partially fails or times out:

- do not infer completion;
- retain completed chunks only if individually trustworthy;
- identify the exact uncovered range;
- rerun the missing range with safer resource bounds;
- promote only once coverage is demonstrably gap-free.

---

## 16. Portability between ChatGPT and Codex

Every close-out must assume the next worker may be a different system with no conversational memory.

Therefore:

- never write “as discussed above” as a load-bearing instruction;
- put required constants, definitions, scope, obligations, and verifier commands into repository files;
- make the next target explicit;
- carry forward correction/demotion state;
- carry forward verification-economy and sustained-attack rules;
- keep exact provenance for externally inherited certificates;
- ensure the next worker can discover the authoritative entry point from the repository alone.

Conversation transcripts are optional context, never the state machine.

---

## 17. Final response requirements for an RL job

When an RL job is fully promoted, report succinctly:

- completed RL number;
- main mathematical advances;
- any correction/demotion;
- exact new frontier/endpoint where relevant;
- verifier/fresh-unpack status;
- resulting next RL number/target;
- promotion commit SHA if available.

When an RL job is **not** fully promoted, report instead:

- no authoritative transition was committed;
- last committed authoritative RL state remains unchanged;
- last fully verified local checkpoint;
- incomplete work that remains unpromoted;
- exact resume instruction if available.

Never describe an uncommitted partial result as authoritative.

---

## 18. Infrastructure changes

Do not casually modify this protocol, repository architecture, verifier framework, or authoritative/session lifecycle during mathematical research.

If process improvements are useful, record them as proposals in local work and defer them to a dedicated infrastructure/bootstrap task unless the current user explicitly authorises the change.

Mathematical promotion commits should remain focused on one RL state transition.

---

## 19. Short operational checklist

Before research:

- verify current authoritative package;
- capture `BASE_HEAD` and authoritative snapshot;
- keep tracked authoritative/session state untouched.

During research:

- work under `.rl-work/`;
- checkpoint often;
- classify results;
- preserve exact coverage;
- repair immediately when a floor/minimum/verifier changes.

Before commit:

- complete close-out;
- build next package locally;
- fresh-unpack verify;
- confirm incoming authoritative state is unchanged.

Commit:

- move completed current session to `sessions/`;
- replace `authoritative/` with verified next state;
- inspect staged transition;
- one atomic RL commit.

If interrupted:

- no partial commit;
- no half-promotion;
- last committed authoritative state remains the truth.
