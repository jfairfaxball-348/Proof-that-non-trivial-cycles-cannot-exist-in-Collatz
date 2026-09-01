# RL219 red-team report

Date: 2026-09-01. Verdict: **PASS within stated scope**.

1. **Incoming frontier lock.** The RL218 proof state remains numerically unchanged: 139,581,280 phase-51 candidates, 45,045 prefixes, frontier 13,415,865,871.
2. **Superset direction.** The finite verifier derives the `y_16` lower bound over the larger non-deleted pre-phase-51/Hensel family. Since phase-51 survivors form a subset, transporting a lower bound is valid and cannot omit a smaller phase-51 survivor.
3. **Deleted-prefix lock.** The already-deleted RL216 `Q=43,013,953` family is not reintroduced.
4. **Window/Hensel reconstruction.** The verifier reproduces 45,046 rows, 331,935,455 pre-Hensel lifts, 331,935,285 post-Hensel lifts, 170 Hensel deletions, and 331,927,916 lifts after the RL216 prefix deletion before applying the phase-51 subset fact.
5. **Height telescoping sign check.** Summing `a_i=b_(i+1)-b_i+h_i-h_(i+1)` gives `E_d=b_(16+d)-b_16+1-h_(16+d)`. Nonnegative physical height gives an upper, not lower, bound on E_d, hence a lower bound on the physical state. The inequality direction is correct.
6. **Lambda scope.** RL219 uses the inherited certified analytic statement `0<ln(lambda)<2^-40`; it does not recompute or strengthen it. `ln2>1/2>2^-40` implies `lambda<2` exactly.
7. **Even-state check.** Shortcut even states between accelerated odds are before the final halvings and are at least the following odd state, so the odd-state floor extends to the ordinary shortcut traversal.
8. **Physical versus arithmetic lock.** T1 assumes a full physical H21 realization. It does not delete phase-51 arithmetic candidates that have only passed necessary conditions through phase 51.
9. **External-result classification.** Barina's `2^71` result is recorded as externally inherited computation only. RL219 does not use the live 2026 project frontier as an authoritative constant.
10. **Dyadic recurrence check.** For fixed raw word `W(s)=(2^n s-C_w)/3^h`, replacing s by `2^t s` gives `Y_(t+1)=2Y_t+C_w/3^h>=2Y_t` because `C_w>=0`.
11. **Legal-subsequence check.** Restricting t to values for which the fixed word is integral/legal cannot create two values closer than the underlying factor-two spacing.
12. **Root-band check.** Exact `R_MAX<2R_MIN` is pinned by the verifier. Thus at most one dyadic parameter value per `(seed,word)` pair can land in the full root band.
13. **Quantifier lock.** T2 is only for finite seed sets and finite libraries of fixed raw words. It does not rule out an infinite parameterized family with varying non-dyadic word structure, an independently certified arithmetic progression, or another new basin theorem.
14. **No overpromotion.** Zero candidate/rank deletions; no physical incidence/charge, branch contradiction, Gate closure, global nontrivial-cycle exclusion, or Collatz proof is claimed.

No correction or demotion is required.
