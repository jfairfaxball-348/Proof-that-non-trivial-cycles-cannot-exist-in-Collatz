# RL224 provenance

Date: 2026-09-01.

Repository: `jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`.

Incoming authoritative identity:

- `BASE_HEAD`: `7eacfbe28d424f747e4f1dbd81f3821b69a038eb`;
- root tree: `82d605fee47282e2e72bd48db50205f371bdaab7`;
- incoming `authoritative/` tree: `db779d8d868f6a1f9656b3270b661fdfb0dbf74c`;
- incoming RL223 bundle outer SHA256: `19e9339f31b733fc7b0d3ca2585f7e0066a519a73274d156c5bae70b171433a9`.

Primary inherited exact sources used under verification economy:

- RL223 certified facts, correction ledger, reduced H21 interface and RL224 target;
- RL217 portable prefix-wide height verifier for the exact reconstruction/recurrence;
- RL216 reduced H21 interface for the mandatory nonnegative-height condition and exhaustive e=16 family bridge;
- inherited small-offset rank transport identifying e=16 with terminal rank 34,124,151,203.

The RL217 exact verifier was independently reproduced at its phase-51 aggregate counts before extension. The source RL224 phase-200 scan was run in nine contiguous chunks and independently aggregated; hashes of the source-closeout aggregates remain in `certificates/rl224_reconstructive_summary.json` as provenance. For promotion, bulky TSV payloads are replaced by a deterministic reconstructive certificate: it regenerates the exact inherited record table (pinned SHA256), reruns every one of the 331,927,916 targeted candidates through phase 200, and replays every resulting survivor through transition 346. This changes no mathematics or scope and is independently gap-free.

All computation is deterministic integer arithmetic. Portable reconstruction/scanner/replay sources are included under `support/`; the optimized full reconstructive certificate wrapper and fast proof-state guard are included under `verification/`.

Knowledge catalogues are `stale/deferred` and were not used as proof-state authority.
