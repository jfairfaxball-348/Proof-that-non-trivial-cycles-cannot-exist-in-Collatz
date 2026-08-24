# Session provenance — RL-7

Date: 2026-08-19

Input seed:
- `/mnt/data/rl6/Collatz_Rsharp_RL6_Handover_2026-08-19.zip`
- expanded RL-6 work tree already present under `/mnt/data/rl6/Collatz_Rsharp_RL6_Handover_2026-08-19/rl6_work/`

New work:
- exact analytic derivation of least-anchor prefix/suffix sandwich and reciprocal defect refinement;
- exact rotation-invariance of `gcd(C,D)` and residual denominator formulation;
- exact repeated compressed-word fixed-point descent;
- exact adjacent parity-transposition unit-edge obstruction modulo `D`;
- explicit quantitative Christoffel gap `>3^(L-1)/4` and resulting minimum-cycle bound;
- exact finite verifier for all preceding algebraic identities in declared finite domains.

External literature checked during this continuation:
- Fernández & Ibáñez, arXiv:2607.24844v1 (2026), Christoffel extremality and relation to Knight high cycles;
- Knight, Discrete Mathematics 349 (2026), 114812, nonexistence of positive-integer high cycles;
- Hercher, JIS 26 (2023; corrigendum listed by journal in 2026), `m>=92`;
- Barina, Journal of Supercomputing (2025), verification through `2^71`.

No external theorem is silently promoted to an internal proof. RL remains open.

Late RL-7 strengthening:
- proved RL-L51: one cyclic adjacent self-rotation iff primitive Christoffel rotation class;
- proved RL-L52: Christoffel parity words are internally excluded from primitive nontrivial integer cycles using rotation-invariant D-divisibility plus RL-L49; this removes Knight as a dependency of the RL-L50 cycle bound.
