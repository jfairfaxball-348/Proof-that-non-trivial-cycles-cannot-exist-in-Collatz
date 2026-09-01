# RL214 independent scope / red-team report

Date: 2026-09-01. Verdict: PASS for the scoped RL214 candidate.

Checks performed:

1. Re-derived the phase-aligned bridge from the RL206 complete binary recurrence rather than equating quotient notation with the H21 root by convention.
2. Confirmed that the full binary recurrence sampled at cumulative odd-step positions is exactly the accelerated odd recurrence, so `R_0=y_0=Q(d)/D`.
3. Checked that bare ownership still gives no quotient residue: `(Q/D) modD` depends on `Q modD^2`, matching the explicit RL206 exception.
4. Re-derived the p-arc identity `2^u K_0=(3^p-2^u)y_0+P` with the sign of every term checked and `P>0`.
5. Re-derived the rational cap from `Ap-uL=1`, `0<delta<2^-40`, `p<2^36`, and the positive atanh series bound `ln2>2/3`. No floating-point inequality is used.
6. Reconstructed all 108,950 RL212 e=16 prefixes and all 45,046 H21-compatible prefixes with exact integers.
7. Verified the unique mod-`3^17` root-unit lift for every H21 prefix and the canonical range `0<y_0^*<3*2^58`, so no negative-k lift can be positive.
8. Exhausted the exact k-range implied by the cap algebraically: 34,652 prefixes have kmax 36,180 and 10,394 have kmax 36,181, totaling 1,629,819,720 arithmetic candidates.
9. Solved the terminal `nu>=22` Hensel congruence exactly along every bounded progression. Exactly 789 candidates fail; no prefix fails. All four mod18 classes and all 469 RL212 reachable mod2187 classes remain.
10. Confirmed no bounded candidate is promoted as a complete physical word or cycle and no rank deletion is inferred.
11. Confirmed RL213 endpoint/G56 barriers, RL209 signed-successor scope, RL206 corrections, counts and all physical/charge/Gate/global locks remain intact.

No correction or demotion is required. The global frontier remains 13,415,865,871.
