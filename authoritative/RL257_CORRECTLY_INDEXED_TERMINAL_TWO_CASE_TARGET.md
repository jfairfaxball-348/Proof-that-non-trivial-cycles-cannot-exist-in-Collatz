# RL257 — correctly indexed terminal two-case target

Date prepared: 2026-09-05
Status: **PREPARED, NOT STARTED**

## Incoming exact state

At the unique first halving selector

`(a,ell,z,q,r,H,n)=(1100,694,406,317,200,14,4)`

RL256 proves

`k in {31,33}`.

For the two cases:

- `k=31`: `E_31<=27`;
- `k=33`: `beta(P)>=281`, `E_33<=5`, and a physical `1^7` run is forced
  adjacent to the terminal structure.

## Mandatory indexing repair

Do not reuse RL256's demoted provisional four-state tree.

Use the exact historical convention:

- physical half-word `u=110 x 1 0^(k-3)`;
- the internal canonical path ends before the omitted terminal `(1,0)`;
- the terminal state `J=2^k` occurs after that final canonical `10`.

Every backward terminal calculation must restore this omitted final column
before tracing any forced internal one-run.

## Primary target

1. Correctly index the `k=33` forced physical flank pattern in the canonical
   `(d,J)` / full-phase ledger.
2. Combine it with exact ownership, terminal `J=2^33`, `H=14`, and any safe
   inherited valuation/rank identities.
3. Either eliminate `k=33` analytically or reduce it to a finite explicit
   owned state family with a complete verifier.
4. If `k=33` is eliminated, attack the remaining `k=31` branch using
   `E_31<=27` and the same correctly indexed terminal machinery.

Do not claim Gate A or Gate B closure from a local physical pattern alone.
Do not promote MILP infeasibility without an exact reproducible certificate.

Gate A open. Gate B open. Radius 4 not invoked. Radius 5 inactive.
