# RL217 red-team report

Date: 2026-09-01. Verdict: **PASS within stated finite-horizon scope**.

## Checks

1. **Inherited population reconstruction.** Independent formulas reproduce 45,046 RL215-compatible prefixes, 331,935,455 candidates before terminal Hensel, 331,935,285 after the 170 narrowed-window Hensel exclusions, and the exact RL216 incoming remainder 331,927,916 after removing the already-certified 7,369-candidate minimum-Q prefix.
2. **No prefix leakage.** The deleted `Q=43,013,953` family is excluded from every RL217 population update. It is used only to verify inherited arithmetic reconstruction.
3. **Universal-coordinate check.** Substitution into `y_16=2^34 eta-1-3^16*2^13` confirms that the post-phase-16 recurrence depends on the lifted coordinate alone. No ownership claim is transported from this factorisation.
4. **Cylinder exactness.** The automaton splits only on unresolved parity bits; all children are disjoint and exhaustive. Fixed-valuation branches use exact divisibility before recurrence propagation.
5. **Range-counting check.** Live `x` cylinders are converted to `k` congruences using the inverse of `3^17 mod2^m`; finite interval counts are exact and do not enumerate the incoming population.
6. **Direct replay cross-check.** Thirteen deterministic prefixes, including prefixes with inherited terminal-Hensel hits, are replayed candidate-by-candidate only as a small independent red-team sample. Their direct phase-51 survivor counts agree exactly with the modular projection.
7. **Population consistency.** State counts and mod18 counts sum to 139,581,280; all 469 eta classes mod2187 remain represented; every prefix has positive population.
8. **Finite-horizon lock.** No result through phase 51 is extrapolated to later phases. The state-growth observation is classified as a method barrier, not an intrinsic no-go theorem.
9. **Physical-scope lock.** Arithmetic survivors are not physical H21 occurrences or charges. No Gate or branch contradiction is inferred.

No correction or demotion is required.
