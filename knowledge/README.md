# Repository knowledge index

This directory is the deterministic locator layer between the current
`authoritative/` generation and immutable historical evidence. It contains no
new mathematics and does not replace the RL conveyor.

Use the single public command surface:

```sh
python3 tools/rl_conveyor.py startup
python3 tools/rl_conveyor.py session RL174
python3 tools/rl_conveyor.py result 'RL175.4'
python3 tools/rl_conveyor.py index-validate
```

Open an exact returned source for full provenance. Do not recursively search
all of `sessions/`, `Archive/`, bundles, transports, or certificate payloads
during ordinary startup.

## Historical convention

`sessions/RL<n>/` is a stable container label, not a universal completed-RL
identifier. Layouts vary: a container may hold a same-labelled completed
generation, the preceding completed generation that launched incoming
`RL<n>`, several explicit `from_RLx_to_RLy` transitions, or cumulative
inherited material. Historical paths must not be renamed to make the layout
look uniform.

The catalogue therefore keeps these concepts separate:

- physical container path and label;
- one or more generation roots;
- completed and incoming RL identifiers only when explicit metadata records
  them;
- embedded-only locators when an old RL label exists only inside a cumulative
  package;
- all role paths as arrays;
- predecessor/successor relationships derived only from explicit transition
  pairs;
- deterministic SHA-256 identities of the indexed source generation and its
  container.

Null fields and `ambiguities` are deliberate. They are safer than guessing.

## Generated files

- `session_catalog.jsonl` contains one record per mechanically identified
  transition plus unresolved or embedded locators. It records entry points,
  reports, handovers, targets, proof/correction ledgers, verifier and
  certificate locations, bundles, sidecars, manifests, archive provenance,
  relationships, and source identities.
- `result_catalog.jsonl` contains conservative locators extracted only from
  designated proof/status, correction/demotion, and session-state sources.
  It stores exact source lines, aliases, and verbatim classifications where
  the source explicitly encodes one.
- `index_metadata.json` records schemas, counts, coverage, and content hashes.

The result catalogue does not infer truth, falsity, supersession, scope, or
claim-specific verifier coverage. A verifier or certificate root returned
with a result is a session-level candidate unless the canonical source itself
links it. Conflicting records are returned together and are never
adjudicated. Absence of a dedicated correction ledger means only that no such
ledger was indexed, not that no correction exists.

These three files are generated. Do not edit them by hand.

## Maintenance

After a future verified RL closeout has assembled the final frozen session and
replacement authority, but before the atomic commit, run:

```sh
python3 tools/rl_conveyor.py index-build
python3 tools/rl_conveyor.py index-validate
```

Run `index-validate` again after the commit/read-back. Generation is sorted,
timestamp-free, and requires no semantic summary, so identical repository
state produces byte-identical indexes. Validation rebuilds the expected bytes
in memory and fails closed on a missing or stale generated file. It also
checks that root `START_HERE.md` remains a timeless pointer to the startup
command and current authoritative entry point rather than duplicating an RL
number.

## Search policy

The tracked `.rgignore` keeps normal `rg` searches on the live and operational
surface. After an index query, open or search the exact returned path. Use
`rg --no-ignore` only for a named dependency, verifier failure, apparent
conflict, stop-and-repair reconstruction, or an explicitly requested
historical/global audit.

ZIP contents, inherited trees, bundle transports, logs, and certificate
payloads are packaging or deep provenance surfaces. Search them only when the
exact indexed source is insufficient. Historical duplicate files and OS
metadata are preserved because removal offers negligible lookup benefit and
stable paths retain provenance.
