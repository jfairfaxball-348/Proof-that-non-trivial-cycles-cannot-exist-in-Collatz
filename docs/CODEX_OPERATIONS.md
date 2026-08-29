# Codex / cloud operations and repository lookup

`AGENTS.md` is binding. The repository supports both shell workers and connector workers.

## Shell worker

From the repository root, the normal command surface is:

```sh
python3 tools/rl_conveyor.py startup
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
python3 tools/rl_conveyor.py session RL<N>
python3 tools/rl_conveyor.py result QUERY
python3 tools/rl_conveyor.py index-build
python3 tools/rl_conveyor.py index-validate
```

Use `check-snapshot`, `check-promotion`, and `preflight` before promotion where applicable.

## Connector/cloud worker

A cloud ChatGPT worker with GitHub access may complete the same numbered RL lifecycle without a checked-out repository shell.

It should:

- read `AGENTS.md`, root `START_HERE.md`, `authoritative/START_HERE.md`, and the exact current authority files;
- record remote HEAD and authoritative file/blob identities;
- verify incoming/candidate bundles and portable verifiers in local sandbox storage;
- use targeted GitHub reads for provenance;
- construct one atomic final Git tree/commit through Git-object tooling;
- advance the branch ref only after the complete tree is ready;
- read the ref/session/authority back after promotion.

It must not claim shell commands ran when they did not. Equivalent direct checks are acceptable.

## Historical lookup

The generated `knowledge/` catalogues are conservative locator caches. When known current, shell workers may use:

```sh
python3 tools/rl_conveyor.py session RL<N>
python3 tools/rl_conveyor.py result QUERY
```

A connector worker may read these files directly if their generation is sufficient for the requested history, but must treat them as possibly stale after a cloud promotion. If a needed record is newer than the catalogue, use a narrow exact GitHub lookup rather than a recursive archive search.

Never infer that a mathematical result is absent merely because a catalogue has no entry.

## Catalogue maintenance

Generated files:

- `knowledge/session_catalog.jsonl`
- `knowledge/result_catalog.jsonl`
- `knowledge/index_metadata.json`

They are deterministic optimisation caches, not authority.

Shell-capable workers should periodically run:

```sh
python3 tools/rl_conveyor.py index-build
python3 tools/rl_conveyor.py index-validate
```

Normal cloud RL promotion does not require these commands and may leave catalogues stale. Never hand-edit them to imitate generation. A later infrastructure refresh is sufficient.

## Default search exclusions

Ordinary startup/provenance lookup should not recursively search all of:

- `sessions/` or `Archive/`;
- ZIP contents or transports;
- duplicated bundle payloads;
- generated certificate payloads;
- unrelated legacy material.

Use the smallest exact source population necessary.

For research procedure see `docs/RL_RESEARCH_PROTOCOL.md`. On closeout read `docs/CLOSEOUT_LOCK.md` and `docs/VERIFICATION_AND_CLOSEOUT.md`.
