# Codex operations and repository lookup

Run commands from the repository root with:

`python3 tools/rl_conveyor.py COMMAND`

`AGENTS.md` is the binding contract. This document is the command reference and default search policy.

## Minimal startup

For human-readable startup output:

```sh
python3 tools/rl_conveyor.py startup
```

For machine-readable output:

```sh
python3 tools/rl_conveyor.py startup --json
```

`startup` derives the incoming RL, handover generation, exact target, minimal current read set, bundle/transport paths, and catalogue state from the repository. It must fail closed on ambiguous current authority. Prefer it to filename grepping or a manually maintained RL pointer.

Normal startup order is:

1. read the concise `AGENTS.md`;
2. run `startup`;
3. read root `START_HERE.md`;
4. read `authoritative/START_HERE.md`, the emitted status/red-team paths, and current sources named there;
5. run the incoming integrity gate before mathematics;
6. query history only when an inherited dependency needs provenance.

## Historical session lookup

Locate a frozen session without recursively searching `sessions/` or `Archive/`:

```sh
python3 tools/rl_conveyor.py session RL<N>
python3 tools/rl_conveyor.py session RL<N> --json
```

The command returns compact locator metadata from `knowledge/session_catalog.jsonl`, including the historical container, completed/incoming identifiers, canonical report/handover/target paths, bundle/checksum paths, relationship metadata, and source-generation identity when available. Historical format variation is reported explicitly; a surprising container name is not silently normalized or renamed.

Open only the exact canonical source needed after the lookup.

## Result and claim lookup

Locate a recorded result, alias, correction, verifier, or certificate:

```sh
python3 tools/rl_conveyor.py result QUERY
python3 tools/rl_conveyor.py result QUERY --limit N
python3 tools/rl_conveyor.py result QUERY --json
```

The result catalogue is a conservative locator sourced only from designated proof-state, correction/demotion, and session-state records. Output classifications are copied from their source; the tool does not infer theorem status from ordinary prose or adjudicate conflicts. When sources conflict, it returns the relevant pointers for future mathematical review.

Use the returned canonical source for full provenance. Do not treat catalogue text as a replacement for the source.

## Catalogue maintenance

The generated files are:

- `knowledge/session_catalog.jsonl`;
- `knowledge/result_catalog.jsonl`;
- `knowledge/index_metadata.json`.

Their schema, extraction policy, and limitations are documented in `knowledge/README.md`.

Regenerate deterministically with:

```sh
python3 tools/rl_conveyor.py index-build
```

Validate coverage, hashes, ordering, source identities, and current-generation metadata with:

```sh
python3 tools/rl_conveyor.py index-validate
```

Run both when assembling the final tree of a normal RL promotion and after an authorized infrastructure change that affects indexed sources. Validation must identify missing/stale entries and fail closed; it must not alter mathematical status.

`index-build` writes only the generated `knowledge/` catalogue files. `index-validate` is read-only.

## Incoming integrity gate

Before mathematics run:

```sh
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
```

`verify-incoming` verifies the outer SHA-256 sidecar, reconstructs any documented lossless transport only in a temporary directory, cleanly unpacks the bundle, verifies its internal SHA-256 manifest, and runs portable `verification/verify_*.py` checks. It fails closed if the convention is ambiguous, incomplete, or inconsistent.

`init-checkpoint` creates ignored `.rl-work/RL<incoming_rl>/CHECKPOINT.md`, `STATE.json`, `commands.log`, `artifacts/`, and `authoritative-snapshot.json`. It records `BASE_HEAD` and refuses unexplained tracked state.

The lower-level `status` command remains useful for a compact repository diagnostic, including the physical bundle/outer-sidecar match when it can be checked without transport reconstruction. `startup` is the normal entry point because it also includes the minimal read set and catalogue status.

## Snapshot and candidate checks

Before promotion:

```sh
python3 tools/rl_conveyor.py check-snapshot PATH_TO_AUTHORITATIVE_SNAPSHOT
python3 tools/rl_conveyor.py check-promotion .rl-work/RL<incoming_rl>/candidate
python3 tools/rl_conveyor.py preflight PATH_TO_AUTHORITATIVE_SNAPSHOT .rl-work/RL<incoming_rl>/candidate
```

`check-snapshot` proves that current tracked authority still matches the start snapshot. `check-promotion` validates the structural promotion manifest and required candidate artifacts. `preflight` performs both.

These utilities never decide theorem validity and do not replace target-specific proofs, exact-range checks, red teams, or independent verifier judgement. Except for `init-checkpoint` and `index-build`, the commands documented here are read-only with respect to tracked repository state; none stages, moves, deletes, commits, or pushes a mathematical transition.

## Default search exclusions

Ordinary startup and provenance lookup must not recursively search:

- all of `sessions/` or `Archive/`;
- ZIP contents or lossless transport parts;
- duplicated bundle payloads;
- generated certificate payloads;
- legacy material unrelated to a returned source.

Deeper search is justified only when a canonical source is missing, an index validation fails, a live dependency requires a definition absent from its recorded source, a genuine conflict triggers stop-and-repair, or an explicit historical reconstruction is required. Record the reason and narrow the search to the smallest relevant population.

For research procedure see `docs/RL_RESEARCH_PROTOCOL.md`. On entering closeout, read `docs/CLOSEOUT_LOCK.md`, then `docs/VERIFICATION_AND_CLOSEOUT.md`.
