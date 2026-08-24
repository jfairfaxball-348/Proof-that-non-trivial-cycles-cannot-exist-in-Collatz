# RL-3 Canonical Register Delta — 2026-08-19

This delta supplements the RL-2 register.

| ID | Claim | Status |
|---|---|---|
| RL-L18 | In `k=0`, a violation of the root xi ceiling at even `d` is exactly one cylinder `R#=-2^(1-d) mod 3^(Q_d+1)`; its bad mod-9 class is determined by `d mod6`. | **PROVED ANALYTIC THEOREM** |
| RL-G7 | The full infinite root xi-ceiling sieve leaves positive 3-adic measure in both inherited mod-9 branches; root xi + inherited root residues cannot close `k=0`. | **FAILED / REFUTED ROUTE** |
| RL-L19 | Six explicit arbitrarily large integer families, one in each inherited `k=0` class mod144, satisfy every root xi ceiling. | **PROVED ANALYTIC THEOREM** |
| RL-L20 | For `k>0`, entry predecessor exponent gap `2m` gives exact branch amplification: larger predecessor = `4^m` smaller + `(4^m-1)/3`. | **PROVED ANALYTIC THEOREM** |
| RL-L21 | Relative branch difference obeys an exact recurrence; sign reversal requires the corresponding exponent order reversal. Every strict preperiod has at least one reverse phase with tail exponent below cycle exponent. | **PROVED ANALYTIC THEOREM** |
| RL-L22 | If the tail is the larger entry predecessor by exponent gap `2m`, it incurs contraction debt `N1 > m log(4)/log(3/2)`; gap 2 forces at least four later exponent-1 moves. | **PROVED ANALYTIC THEOREM** |
| RL-X5 | New verifier audits root bad cylinders, measure bounds, explicit root families, entry amplification, relative-order recurrence and normalized height behavior. | **EXACT FINITE CERTIFICATE** |

## Reformulated obligations

- **RL-O3 / k=0:** root-only xi probing is now structurally exhausted as an exclusion route. Move xi to cycle states/rotations or combine it with common-denominator integrality.
- **RL-O2 / k>0:** use entry amplification + crossing phase + contraction debt as the initial state for a phase-aware relative-height automaton.
- **RL-O7:** still critical. Finite diagnostics remain nonproof unless backed by an infinite extension theorem.
