# RL217 exact prefix-wide e=16 height-automaton certificate

Date: 2026-09-01. Classification: **exact finite modular arithmetic certificate** supporting the scoped RL217 theorem.

The verifier independently reconstructs the inherited 45,046 RL215-compatible e=16 prefixes, their exact two-sided `k` windows and the terminal-Hensel filter, reproducing 331,935,285 post-Hensel RL215 candidates. It then removes the already-certified RL216 minimum-Q family of 7,369 candidates, recovering the exact RL217 incoming population **331,927,916** across **45,045** prefixes.

For every prefix the phase-16 state factors through one lifted coordinate

`x = eta_* + 3^17 k`,
`y_16 = 2^34 x - 1 - 3^16*2^13`, `h_16=1`.

Thus the post-phase-16 height test is represented by one universal 2-adic automaton. For a branch `x=r+2^m t`, the odd state stays affine in `t`; ambiguous valuations are split exactly by parity and branches forcing `h<0` are rejected.

Through phase 51 the universal automaton produces **1,705,547** failure cylinders and **3,132,617** disjoint survivor cylinders, using at most 25 bits of 2-adic precision. The exact survivor-cylinder digest is

`abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05`.

For each live cylinder, multiplication by `(3^17)^(-1) mod2^m` converts the cylinder to a congruence on the prefix parameter `k`. Intersections with each finite prefix interval are counted algebraically by cyclic range arithmetic. The promoted calculation never enumerates the 331,927,916 incoming arithmetic candidates.

Exact phase-51 consequence:

- newly removed vs RL216: **192,346,636** arithmetic candidates;
- survivors through phase 51: **139,581,280**;
- additional complete prefixes deleted: **0**;
- each of the 45,045 prefixes retains 2,995..3,235 candidates;
- both H21 states, all four mod18 classes and all 469 eta classes mod2187 remain represented;
- no terminal rank deletion; global frontier remains **13,415,865,871**.

A small deterministic direct-replay cross-section, including prefixes hit by the inherited terminal-Hensel filter, is used only as an independent red-team check and agrees exactly with the modular projection.

The certificate is finite-horizon: no claim is made for phases beyond 51.
