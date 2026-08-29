# Repository knowledge index

This directory is a deterministic lookup acceleration layer between current `authoritative/` and historical evidence. It contains no mathematics and does not replace the RL conveyor.

## Authority status

The catalogue is **non-authoritative cache data**.

- `authoritative/` remains the sole incoming mathematical state.
- A missing or stale catalogue does not block startup, research, or a numbered RL promotion.
- Catalogue absence is never evidence that a mathematical result, correction, session, or certificate does not exist.
- Do not hand-edit generated catalogue files.

This rule exists so both shell-based Codex and cloud ChatGPT workers can run the complete RL conveyor without environment handoffs.

## Generated files

- `session_catalog.jsonl` — historical generation/session locators.
- `result_catalog.jsonl` — conservative locators extracted from designated proof/status and correction sources.
- `index_metadata.json` — schema/count/hash metadata.

The catalogue does not infer truth, falsity, supersession, scope, or claim-specific verifier coverage. Open the canonical source for full provenance.

## Maintenance

When a repository shell is available, regenerate deterministically with:

```sh
python3 tools/rl_conveyor.py index-build
python3 tools/rl_conveyor.py index-validate
```

A shell worker should normally refresh after a closeout when practical. A connector/cloud worker may defer regeneration and leave the tracked catalogue at its previous known generation. Such a transition must report catalogue status as `stale/deferred`, but the RL closeout remains complete if all mathematical, packaging, atomic Git, push, and readback gates pass.

A later dedicated infrastructure commit or shell-capable session may refresh the index without consuming an RL number.

## Historical convention and search policy

Historical container names are not universal completed-RL identifiers; preserve existing paths and explicit provenance.

Prefer exact catalogue-returned paths when the catalogue is current enough. If it is stale for the needed generation, use a narrowly targeted repository lookup. Do not recursively search all `sessions/`, `Archive/`, bundle contents, transports, or certificate payloads unless an explicit dependency or audit requires it.

The index is an optimisation for speed, never a safety barrier that can strand an otherwise verified RL.
