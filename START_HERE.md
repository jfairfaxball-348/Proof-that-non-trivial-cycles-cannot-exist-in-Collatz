# RL research repository — start here

The repository is the research-state carrier; worker conversations are disposable. `authoritative/` is the sole current incoming mathematical state.

For a compact, mechanically derived shell-worker startup view, run:

```sh
python3 tools/rl_conveyor.py startup
```

Then read [authoritative/START_HERE.md](authoritative/START_HERE.md), the current status/red-team paths emitted by `startup`, and the current files that entry point names. Before beginning mathematics, follow the binding start gate in [AGENTS.md](AGENTS.md).

## Connector fast path

A connector worker should not emulate a shell startup by recursively browsing the repository. Pin the live default-branch `BASE_HEAD` and its committed `authoritative/` tree identity, then read only:

1. `AGENTS.md`;
2. `authoritative/START_HERE.md`;
3. the exact current files named there;
4. the unique current target.

Use inherited/frozen material only by exact path when a live dependency requires it. Do not preload `sessions/`, `Archive/`, the generated catalogue JSONL files, bundle copies, certificate payloads, or a recursive Git tree.

After the incoming gate is validated, keep a compact connector resume state keyed by `BASE_HEAD` + authoritative tree identity. On a later bare `continue`, if that identity is unchanged, resume from the recorded frontier without rerunning startup or rereading already validated inherited authority. See [docs/CONNECTOR_WORKFLOW.md](docs/CONNECTOR_WORKFLOW.md).

Historical material in `sessions/` and `Archive/`, bundle copies, ZIP contents, and certificate payloads are not part of normal startup. Query the repository catalogue through the commands in [docs/CODEX_OPERATIONS.md](docs/CODEX_OPERATIONS.md), and open only the exact source returned when inherited provenance is needed.

Detailed process documents are phase-loaded through `AGENTS.md`; do not preload them during ordinary startup. Local work belongs under ignored `.rl-work/RL<incoming_rl>/` or the connector's equivalent sandbox state and is never authoritative.
