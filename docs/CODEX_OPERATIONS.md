# Codex / cloud operations and repository lookup

`AGENTS.md` is binding. The repository supports both shell workers and connector workers. The shell tooling requires Python 3.9 or later and has no third-party runtime dependencies. Run `python3 tools/rl_conveyor.py --help` or append `--help` to a subcommand for its current interface.

## Shell-worker startup

From the repository root, run the start gate in this order:

```sh
python3 tools/rl_conveyor.py startup
python3 tools/rl_conveyor.py verify-incoming
python3 tools/rl_conveyor.py init-checkpoint
```

`startup` identifies the live remote/default-branch base, local HEAD, unique incoming RL and target, current ledgers and red-team material, and the required command sequence. `verify-incoming` validates the outer checksum, reconstructs the configured transport when necessary, fresh-unpacks the bundle, validates its internal manifest, and runs its portable fast verifiers. `init-checkpoint` creates ignored, non-authoritative resumability state only after the gate passes and refuses to overwrite an existing checkpoint.

Do not begin mathematics if a command fails. A remote identity or incoming-integrity mismatch is a fail-closed condition, not a reason to modify authority.

## Candidate and closeout checks

At closeout, use the snapshot created by `init-checkpoint` and a complete promotion-candidate directory. For example, an RL232 checkpoint and candidate are checked with:

```sh
python3 tools/rl_conveyor.py check-snapshot .rl-work/RL232/authoritative-snapshot.json
python3 tools/rl_conveyor.py check-promotion .rl-work/RL232/promotion-candidate
python3 tools/rl_conveyor.py preflight .rl-work/RL232/authoritative-snapshot.json .rl-work/RL232/promotion-candidate
```

These structural helpers do not stage, commit, promote, or adjudicate mathematical claims. Continue with the candidate, atomic Git, push, and readback gates in [CLOSEOUT_LOCK.md](CLOSEOUT_LOCK.md) and [VERIFICATION_AND_CLOSEOUT.md](VERIFICATION_AND_CLOSEOUT.md).

### Promotion manifest

The candidate root must contain `PROMOTION_MANIFEST.json` with format `rl-promotion-candidate-v1`. All artifact fields are safe relative paths below the candidate root; absolute paths and traversal are rejected. `next_rl` must be exactly one greater than `current_rl`, and `verifier_commands` must be a non-empty list of commands that were used to verify the candidate.

This is a concrete structural example, not a live authority declaration:

```json
{
  "format": "rl-promotion-candidate-v1",
  "current_rl": 231,
  "next_rl": 232,
  "completed_session": "sessions/RL232",
  "next_authoritative": "authoritative",
  "bundle": "authoritative/RL231_HANDOVER_BUNDLE.zip",
  "sidecar": "authoritative/RL231_HANDOVER_BUNDLE.zip.sha256",
  "fresh_unpack_report": "authoritative/FRESH_UNPACK_VERIFICATION.md",
  "verifier_commands": [
    "python3 verification/verify_fast.py"
  ],
  "red_team_report": "sessions/RL232/RL231_RED_TEAM_REPORT.md"
}
```

The referenced paths must exist in that candidate layout. The `bundle` field may point to the physical bundle or the supported reconstructible transport artifact used by that handover. Passing `check-promotion` establishes structural completeness only; every mathematical, packaging, snapshot, and readback gate remains required.

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
python3 tools/rl_conveyor.py session RL231
python3 tools/rl_conveyor.py result H17
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

After staging the complete intended source tree and regenerated catalogue files, validate exactly what the commit will contain:

```sh
python3 tools/rl_conveyor.py index-validate --staged
```

The ordinary form validates the working tree; `--staged` validates the Git index and fails if an indexed input is missing from or differs in that staged tree. Normal cloud RL promotion does not require either form and may leave catalogues stale. Never hand-edit them to imitate generation. A later infrastructure refresh is sufficient.

A catalogue status written inside a frozen handover is an as-of-freeze historical statement. It does not determine the status of the present checkout. For live status, run `index-validate` against the working tree or `index-validate --staged` against an intended commit; do not infer freshness from prose or metadata alone.

## Continuous integration

Infrastructure changes run the complete unit suite and live catalogue validation on Python 3.9 and a current Python release. Changes to incoming authority run `verify-incoming` in a separate read-only workflow. That authority workflow intentionally does not validate catalogue freshness, because stale/deferred catalogues are permitted for an otherwise complete numbered transition.

## Default search exclusions

Ordinary startup/provenance lookup should not recursively search all of:

- `sessions/` or `Archive/`;
- ZIP contents or transports;
- duplicated bundle payloads;
- generated certificate payloads;
- unrelated legacy material.

Use the smallest exact source population necessary.

For research procedure see `docs/RL_RESEARCH_PROTOCOL.md`. On closeout read `docs/CLOSEOUT_LOCK.md` and `docs/VERIFICATION_AND_CLOSEOUT.md`.
