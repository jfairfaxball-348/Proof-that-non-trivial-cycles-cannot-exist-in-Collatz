# RL130 concurrent-line reconciliation

## Trigger

Two independent successor lines were created from RL129 commit
`2d34a4e7b4746eaa3e32688c3d24bf6cdea7c4d5` while research was in progress.

- Local line: `59750d2`, `692ef0f`, and `c2f3892`, with exact quotient-descent
  certificates advancing the primitive ordinary frontier to `L>=58`.
- Remote line: `03c1e05`, with the RL130 minimum-element product-coupling
  package claiming frontier `L>=190,537`.

## Independent reconciliation checks

The remote package's outer SHA-256 sidecar, fresh extraction, internal
`SHA256SUMS.txt`, and supplied fast verifier all passed independently. Its
certificate explicitly covers every `41<=L<=190,536`, hence strictly subsumes
the local line's `41<=L<=57` frontier extension. The remote package remains
scope-limited: Gate A/B, global nontrivial-cycle exclusion, and Collatz closure
are all open.

## Resolution

The verified stronger remote package is the single new authoritative incoming
state. The local authoritative RL131 package is frozen intact under
`sessions/RL131/`; prior local RL130 and RL129 materials remain preserved under
their session directories. The local RL129 repair, correcting its stale outer
archive sidecar after verification, is retained in `sessions/RL129/`.

This is an explicit lineage reconciliation, not a claim that the two proof
methods are identical or that either closes a global gate.
