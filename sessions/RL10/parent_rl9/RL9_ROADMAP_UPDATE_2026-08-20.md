# RL-9 Roadmap Update — 2026-08-20

## Rank 1 — radius 3, but split by `S` before touching `Q`

RL-L61 closes all non-cancelling two-edge self-rotation paths.

For three adjacent transpositions, the exact position-sum discrepancy is:

- `+/-3` if all three moves have the same direction;
- `+/-1` if two moves have one direction and one has the other.

Thus:

- mixed-direction radius-3 self-rotations force `gcd(A,L)=1`;
- same-direction radius-3 self-rotations force `gcd(A,L)|3`.

Derive the weighted three-unit `Q` shapes only after this split. Seek quadratic/Jacobi or cubic-character obstructions analogous to RL-L56.

## Rank 2 — root/return transposition radius

Use RL-L27/RL-L36 plus RL-L54 to target the distinguished rotations specifically. Try to prove the least-state root rotation cannot be within radius 3 of the final-return or first-post-neutral rotation.

## Rank 3 — exact-balanced factor descent

RL-L59 shows that a genuine zero-`S` self-rotation automatically forces an exact balanced cut and then a strict size contradiction. Revisit RL-L55 only if root/boundary grammar can force its weighted block cancellation onto such an exact-balanced cut.

## Rank 4 — positive-density displacement

Radius `>=3` is still only a constant lower bound. The global quantitative route needs `Omega(L)` weighted displacement from the Christoffel extremal class.

## Guardrails

- RL remains open.
- RL-L61 is analytic and infinite.
- The `A<=2000` plus-resonance scan is finite evidence only.
- Do not enumerate radius-2 paths again.
