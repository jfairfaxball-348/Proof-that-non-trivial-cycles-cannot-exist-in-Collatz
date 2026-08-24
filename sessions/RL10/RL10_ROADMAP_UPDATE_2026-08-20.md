# RL-10 Roadmap Update — 2026-08-20

## Rank 1 — kill the mixed sparse three-jump forms

For `gcd(A,L)=1`, mixed radius-3 self-rotations have `e=+/-1`, hence a single rotation orbit. RL-L67 reduces `D|Q` exactly to one of three sparse congruences in `rho=theta^-1`:

- `rho^a + 3 rho^b - 3 rho^c = 0`;
- `rho^a - rho^b + rho^c = 0`;
- `-rho^a + rho^b + 3 rho^c = 0`.

Exploit the fact that natural adjacent edges correspond to a fixed jump in rotation coordinate because `mL == -1 (mod A)` in the `e=+1` orientation. Seek a resultant/Jacobi contradiction or reduce to an already-closed radius-2 resonance.

## Rank 2 — same-direction coprime one-orbit cubic form

RL-L67 gives

`sigma^a + 3 sigma^b + 9 sigma^c = 0`,

with `sigma=theta^-3` and `1-sigma` a unit. Seek a cubic-character or norm obstruction. Do not return to generic three-unit sums.

## Rank 3 — the `gcd(A,L)=3` cubic cofactor

Write

`D=(2^a-3^ell)(2^(2a)+2^a3^ell+3^(2ell))`.

The only exact finite radius-3 survivor through `A<=40` is `(10)^3`, where the three isolated edge weights sum exactly to the cubic cofactor `37=16+12+9` and the shorter denominator is `1`.

Target theorem: cubic-cofactor divisibility plus the three-jump rotation geometry forces an exact third-repeat; then RL-L48 reduces the only possible integer case to the trivial cycle.

## Rank 4 — coprime `gcd(A,m)=3` three-orbit branch

Same-direction `e=+/-3` permits `gcd(A,m)=3`. Derive the three-orbit analogue of RL-L67 and see whether each orbit contributes one jump, producing a factorizable cubic norm.

## Guardrails

- RL remains open.
- Radius 3 is not yet analytically closed.
- The connected `[3]` branch is closed analytically; never enumerate it again.
- The `A<=40` survivor statement is finite evidence only.
- Exact repetitions remain nonprimitive and are already excluded by RL-L48.
