# RL200 Provenance

Date: 2026-08-31.

- Repository: `jfairfaxball-348/Proof-that-non-trivial-cycles-cannot-exist-in-Collatz`.
- Branch: `main`.
- Incoming authoritative commit / BASE_HEAD:
  `d042bbd11529b7660c729a069a97d623c4a292de`.
- Incoming authoritative session: RL199.
- Incoming target: `RL200_H21_ORIENTED_LIFT_GLOBAL_SELECTOR_TARGET.md`.

## Verification economy

RL199 is accepted as frozen authority after direct readback of its current handover, target,
proof-state ledger/report, manifest, deterministic bundle-reconstruction record, and fresh-unpack
verification record.  No recursive historical audit is performed.

Targeted historical dependency expansion is limited to exact live facts needed by RL200:

- RL181: carry-completed `K/rho` normalization and global K corridor;
- RL190/RL193: H21 terminal core, terminal invariant, isolated rank deletions, and exact
  logarithmic defect bound;
- RL196: `pB=1 mod L` / rank convention;
- RL199: oriented lift, state/sign selectors and terminal normalized interface.

No external web mathematics or conversation-only mathematical premise is introduced.

## Promotion rule

Promotion is permitted only if `main` still equals BASE_HEAD.  The complete incoming RL199
authority is archived byte-for-byte under the RL200 session archive.  RL200 is then installed as
the sole successor `authoritative/` tree by one Git tree/commit/ref transition, followed by
readback.  Knowledge catalogues remain stale/deferred and are not part of the mathematical
promotion gate.
