# RL-8 Canonical Register Delta — 2026-08-19

This delta supplements RL-7.

| ID | Claim | Status |
|---|---|---|
| RL-L53 | Every non-cancelling two-adjacent-transposition path has an exact arithmetic collapse. Overlapping edges give either a `2^a3^b` unit change or `5*2^a3^b`; disjoint edges give `2^a3^b(3^v +/- 2^u)`. Hence two `D`-divisible endpoints force `D=5` in the exceptional overlap case or `D|2^u +/-3^v` in the disjoint case. For a coprime nontrivial self-rotation, opposite directions are impossible, so only the plus resonance remains (apart from `D=5`). Writing `k=uL-vA`, any resonance also forces `D|2^|k|-sigma^L` and `D|3^|k|-sigma^A`. | **PROVED ANALYTIC THEOREM** |
| RL-L54 | At the full-parity rotation based at the least cycle state, every proper suffix with `p` ones and length `m` satisfies `2^m>3^p`. Any undercritical proper root prefix satisfies `R# < 2^(m-p)(3^p-2^p)/(2^m-3^p)`. With inherited external `R#>=2^71`, every proper root prefix through `m<=183` is forced supercritical; `(184,116)` is the first generic rescue pair reaching that floor. | **PROVED ANALYTIC THEOREM + EXTERNAL/FINITE COROLLARY** |
| RL-L55 | For `g=gcd(A,L)>1`, `a=A/g`, `ell=L/g`, `D0=2^a-3^ell`, partitioning into length-`a` blocks gives `Q(d) == 3^(L-ell) sum_j 3^(-E_(j+1))Q(B_j) (mod D0)`, where `E` is cumulative block-count imbalance. Proper-factor divisibility is therefore a weighted block cancellation law, not individual shorter-word divisibility. | **PROVED ANALYTIC THEOREM** |
| RL-G9 | Bare proper-factor descent is false: `d=100001`, `(A,L)=(6,2)`, has `D=55`, `D0=5`, balanced primitive blocks `100,001`, and `Q=35`, so `D0|Q` without repetition or full `D`-divisibility. | **FAILED / REFUTED ROUTE (BARE DESCENT)** |
| RL-X12 | New exact verifier audits two-edge path reduction, cyclic distance-two self-rotations, proper binomial resonances through `A<=200`, least-state suffix/prefix inequalities, the exact `183/184` external-floor threshold, and the proper-factor block congruence/counterexample. | **EXACT FINITE CERTIFICATE** |

## Reformulated obligations

- **RL-O3 / k=0 global:** unchanged: exclude `D|C_good` / force `D_res>1` for every nontrivial admissible primitive word.
- **RL-O7 / transposition:** length one is closed; length two is now reduced to `D=5` or a proper binomial resonance. Highest priority is to combine the determinant `k=uL-vA` with RL-L27/RL-L36 endpoint grammar.
- **RL-O7 / quantitative:** still requires a positive-density or total-weight Christoffel displacement theorem. RL-L54 supplies a new minimum-word mechanical envelope but not yet `Omega(L)` defects.
- **Residual-factor descent:** bare `D0` reduction is refuted. Any future descent must use root/return/boundary constraints to prevent the weighted cancellations in RL-L55.
- **RL-O2 / k>0:** unchanged and separate.
