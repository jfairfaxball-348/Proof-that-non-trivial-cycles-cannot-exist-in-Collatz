# RL60 residue-threshold replay notes

Date: 2026-08-23

## Preserved source

`verification/residue_interval_cert.cpp`

This is the source recovered from the RL60 session for the residue/minimal-counterexample interval certificate.

## Claimed role

For a start interval `[L,U]` and odd threshold `KMIN`, the program attempts to certify that no starting value in the interval reaches an admissible terminal predecessor with odd `K>=KMIN` before dropping below its own start.

It groups starts by shortcut-parity residues and prunes a residue class once the affine image is forced below the minimal start in that class. Small/unresolved leaves are checked by exact trajectory iteration.

This is intended as a finite minimal-counterexample proof: if a hypothetical smallest bad start existed in a pruned class, its trajectory would first reach a smaller positive start, contradicting minimality.

## Session claims to replay

- K35 was independently re-covered by the residue certificate after an earlier chunked strong-induction proof.
- K37: no hit below `45,812,984,490`; the boundary is `(2^37-2)/3` and hits immediately.
- K39: no hit below `122,167,958,641`; the boundary reaches `(2^39-2)/3` after one shortcut step.

The original K39 replay interval list recovered from the session is preserved as

`verification/k39_replay_intervals_original_session.txt`.

## Reproducibility caveat

The session's raw output logs for every chunk are not present in the active workspace. The source is preserved, but the RL61 audit should regenerate and archive the logs.

## Audit checklist for the C++ implementation

Inspect at least:

1. `hit()` correctly represents both terminal alternatives;
2. only odd `K>=KMIN` are admitted;
3. the affine residue representation `(A*n+C)/2^j` remains exact;
4. residue interval endpoints returned by `range()` are correct;
5. the `den>A` drop test really proves the image is strictly below the start throughout the class;
6. the branching update for odd/even shortcut parity is correct;
7. the direct target-preimage test does not miss an admissible state;
8. leaf fallback `exact()` is non-circular under the minimal-counterexample interpretation;
9. integer widths cannot overflow on the replayed ranges;
10. interval endpoints are contiguous with no gaps or double-counting that matters.

The next audit should preferably implement a structurally different second checker for at least K37 and K39.
