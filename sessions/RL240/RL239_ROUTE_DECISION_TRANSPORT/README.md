# RL239 route-decision transport

Completed generation: **RL239 — DECISION SESSION / VERIFIED ROUTE SELECTION**.

Promoted outcomes:

- `R4_AUDIT_PASS`;
- `R5_VIABILITY = MODERATE_NEW_PROJECT` (assessment only; no Radius-5 theorem);
- `ROUTE_DECISION = R4_GLOBAL_BRIDGE`.

The canonical RL239 ZIP is carried losslessly as base64 text in `RL239_Radius4_Audit_Radius5_Viability_and_Route_Decision_2026-09-03.zip.b64.part01` through `.part04`.
Reconstruct it with `reconstruct_rl239_bundle.py`, verify
`PART_SHA256SUMS.txt`, then verify the reconstructed ZIP against the outer
authoritative `.zip.sha256` sidecar.

Canonical ZIP SHA256:
`28fd81440e44ac888f21e25da9cdad8fef5e5603aea9c8036c9084c27828893f`.

The bundle contains the proof-state ledger, correction/demotion ledger,
independent Radius-4 audit record, Radius-5 structural/finite evidence,
same-root Radius-3 bridge provenance, portable fast verifier suite, fresh
unpack record, and the RL240 target.

Gate A, Gate B, and global non-trivial-cycle exclusion remain open.
Knowledge catalogues remain stale/deferred.
