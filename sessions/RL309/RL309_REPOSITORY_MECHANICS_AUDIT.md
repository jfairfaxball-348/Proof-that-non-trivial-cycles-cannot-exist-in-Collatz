# RL309 practical repository-mechanics audit

## What works well

The following lifecycle is retained:

- `authoritative/` as the sole incoming research state;
- immutable frozen `sessions/RL.../` history;
- portable verifiers and correction/demotion ledgers;
- explicit `continue` meaningful-checkpoint convention;
- explicit `finish up` -> `CLOSEOUT_LOCK` transition;
- verified atomic promotion and post-commit readback;
- separation of the research repository from the Lean formalisation project.

These mechanics strongly protect against conversational drift and partial promotion.

## Identified practical weakness

The generated lookup acceleration layer exists but is severely stale for the current programme.

The repository defines:

- `knowledge/session_catalog.jsonl`;
- `knowledge/result_catalog.jsonl`;
- `knowledge/index_metadata.json`.

They are designed as deterministic historical locators and are explicitly preferred to broad archive searching when current.

At RL309 closeout, the tracked metadata is still from the early-RL200s era and does not cover the modern RL309 frontier. This forces connector workers to perform targeted historical GitHub lookups for recent theorem provenance.

The staleness is permitted by protocol because connector closeout must not be blocked by lack of a repository shell. That safety rule is correct; the operational failure is allowing deferred maintenance to accumulate for many generations.

## Second weakness: locator versus live proof ledger

Even a fresh generated result catalogue is intentionally only a conservative locator. It does not adjudicate:

- truth/current validity;
- supersession/corrections;
- exact current scope;
- dependency role;
- whether a result is parent-near or merely downstream.

Therefore the project also benefits from a compact current proof/dependency ledger.

RL309_DEPENDENCY_MAP.md is the immediate hand-authored current-state version for RL310.

## Recommended separate non-RL infrastructure task

Do not mix these changes into a numbered mathematical transition.

In a dedicated infrastructure pass, preferably before substantial RL310 execution:

1. regenerate the `knowledge/` catalogues through the current session;
2. run `index-validate` and staged validation in a shell-capable environment;
3. create a compact maintained live proof/dependency ledger mechanism;
4. make startup prefer: current authority -> live proof ledger -> exact canonical source -> generated catalogue -> exceptional repository search;
5. make closeout update the live ledger with theorem ID, statement, scope, status, provenance, corrections/audits, current role, and downstream consumers;
6. add a catalogue freshness policy so deferred status cannot silently accumulate for dozens of RL generations;
7. include the session's parent/global-distance delta in the maintained current state.

This task consumes no RL number under `AGENTS.md`.

## Interim RL310 lookup discipline

Until that infrastructure task is completed:

1. read `sessions/RL309/RL309_DEPENDENCY_MAP.md` first;
2. follow its exact canonical provenance paths;
3. use generated catalogues only for generations they actually cover;
4. use narrow GitHub lookup only when the dependency map/catalogue is insufficient;
5. never infer absence of a theorem from a stale catalogue.
