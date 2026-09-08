# RL281 closeout red-team note

Date: 2026-09-08

Result: **PASS**

This is a closeout scope/proof-state red team, not new research.

Checks:

1. **Gate scope.** RL281 does not claim Gate A globally. It closes only the `k=3` case and proves even terminal exponents unreachable. The residual is explicitly `k>=5`, `k` odd, `H_can<k`.
2. **Gate B / radius scope.** Gate B remains open/frozen; the fifth selector and Radius 6+ are untouched.
3. **Endpoint dependency.** The `B=Q(J+1)/2` and `C=Q(J-1)` phase decompositions are derived from the inherited endpoint-potential/endpoint identity structure. They are not counted as new independent global scalar equations.
4. **Finite-vs-analytic status.** The 13,909 excursion and 45,170 checkpoint regressions support the analytic proofs but are not used to promote a finite sample as a global theorem. The `H<=2` reachable closure is separately exact and gap-free because it exhausts the full state graph under the explicit height cap.
5. **Equality scope.** The 2-adic equality-entry suppression theorem is stated only for positive depth-two equality excursions with `z>=5`, where positivity forces the odd parameter `w>=1`.
6. **One-zero scope.** The identity `h=nu_2(J+4)` is stated with the explicit exception `J=-4`; the sign-change conclusions handle that exceptional value by the exact sign equation.
7. **No hidden boundary classification.** Positive and negative zero-height boundary cycles are quotiented only through inherited monotonicity/telescope laws; no Collatz-cycle classification is claimed.
8. **No forbidden repetition.** RL281 does not promote flat eight-zero enumeration, selector enumeration, Gate-B coupling, or Radius 6+ work.
9. **Successor isolation.** RL282 is exactly one generation ahead and targets only the residual odd-`k` height-escalation problem.

No correction or demotion is required.
