# RL328 — iterate the owned-bridge fixed-point contraction toward R1 closure

Date prepared: 2026-09-15
Status: PREPARED, NOT STARTED

## GLOBAL PROOF ROADMAP

`CURRENT_STAGE = R1`
`CURRENT_STAGE_NAME = Parent Bridge`
`CURRENT_STAGE_PROGRESS = 72%`
`GLOBAL_PROOF_STATUS = OPEN`

## Absolute objective

Close or materially contract the remaining genuine ordered `g=2`, `Z0>0`, `K<0` parent branch under

`1<=n<=32596612662`.

The preferred target is no longer another isolated forbidden block. Turn RL327's threshold-filtered owned-bridge automaton into a **self-propagating contraction/descent** over the remaining high-carry interval.

## Primary theorem target

For thresholds `H` in the live high-carry regime, define the exact parity-aware owned singleton/two-positive certificate at threshold `H`, derive its best finite potential density inequality, and consume that density with the residue-weighted telescope. Prove one of:

1. a uniform map `F(H)<H` on a nontrivial interval whose iteration is rigorously finite and drives the carry below the interval;
2. a finite partition of the remaining high-carry range into certified threshold layers whose contractions compose to a strict descent;
3. an ownership theorem showing that lowering the threshold necessarily introduces enough new bridge constraints to force contradiction or a strictly smaller genuinely owned balanced return.

A single small numerical cap improvement is useful only if it exposes such an iterative mechanism.

## Exact frontier inherited from RL327

- base high-carry automaton: 224 states, 21,805 edges, boundary 72, `Z<=24K+72`;
- residue-weighted intermediate cap: `n<=32603663706`;
- total-46 bootstrap at threshold `32596612663`: 2,414 endpoints, 187 pair types, 9 exact links, boundary 1347, `19Z<=449K+1347`;
- final cap: `n<=32596612662`;
- high-carry ownership theorem from RL326 remains available for `n>=20390252058`.

## Mandatory audit discipline

Every lower threshold/modulus layer must retain:

- explicit initial endpoint odd parity;
- all rational-mechanical factor cells in the stated length range;
- every endpoint lift in the finite physical band;
- exact shared-state ownership links for consecutive large singleton bridges;
- both exhaustive two-positive shapes;
- an independently checked potential on every admitted edge.

Do not trust or reuse the invalidated pre-parity scratch counts.

## Binding barriers and scope

Preserve RL324's local-propagation barrier, the linear-only telescope, the prohibition on late-row use of root-aligned `G<2^35`, and the externally conditional status of the `2^71` least-state floor.

Internal-only frontier: `ell>=190537`.
External-certificate-conditional frontier: `ell>=49547666544`.
Gate A OPEN. Gate B OPEN. R1 OPEN. `g=1` separate. Global positive non-trivial-cycle exclusion OPEN.
