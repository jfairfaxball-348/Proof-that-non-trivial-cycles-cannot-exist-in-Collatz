# RL318 external finite computational certificate dependency — Barina 2^71

Date frozen: 2026-09-14
Classification: EXTERNAL FINITE COMPUTATIONAL CERTIFICATE DEPENDENCY

## Exact external statement consumed

RL318 consumes only the following finite statement:

> Every positive starting value `n < 2^71` converges to `1` under the shortcut Collatz map
> `n -> n/2` for even `n`, `(3n+1)/2` for odd `n`.

This is the exact map used by the ordinary half-step model in the research repository.

The external exhaustive computation is not reproduced by this repository.  It is consumed in the same proof-engineering sense as the earlier RL300 external finite computational dependency: exact provenance is frozen, while all load-bearing consumer arithmetic is replayed locally.

## Frozen provenance

Publication:

- David Barina, "Improved verification limit for the convergence of the Collatz conjecture"
- Journal of Supercomputing 81 (2025), article 810
- published 2025-05-02
- DOI: `10.1007/s11227-025-07337-0`

The publication reports verification through `2^71` and points to the open-source implementation.

Source repository / cited source revision:

- repository: `xbarin02/collatz`
- commit: `53c2a0608075d6fe3f10cc6eeeaf50e400c86338`

A mutable project status page currently advertises a slightly larger verified range.  RL318 deliberately does **not** consume that moving extension.  Only the static peer-reviewed `2^71` statement is authoritative for this dependency.

## Exact local consequences

Let

`R0 = 2^71 = 2,361,183,241,434,822,606,848`.

1. RL317's exact first-internal-fibre state ceiling is

   `1,311,372,708,449 < R0`.

   Hence that entire fibre is incompatible with the external convergence certificate.

2. Replaying the inherited RL131 rational-log denominator argument with `R0` gives

   `qmax = 49,547,666,543`,

   and therefore the conditional reduced odd-count frontier

   `ell >= 49,547,666,544`.

3. RL315 already proved that the least-state/product consumer transfers to the positive reduced shadow, so this conditional frontier applies to the reduced pair of every `g>1` survivor.  No external floor is internalized into the internal-only proof state.

4. The first above-resonance continued-fraction survivor beyond that wall is

   `(a,ell) = (217,976,794,617, 137,528,045,312)`.

   This pair was already identified and studied in RL132--RL143.

The exact consumer arithmetic is replayed by

`sessions/RL318/verification/verify_rl318_external_floor_consumer.py`.

## Scope

This dependency does not prove the Collatz conjecture, Gate A, Gate B, or global non-trivial-cycle exclusion.  It is a finite external certificate used to move the conditional reduced frontier and to eliminate candidate cycles whose least state would lie below `2^71`.

The internal-only reduced frontier remains `ell >= 190,537`.
