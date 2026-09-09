# RL286 startup-repair red team

Date: 2026-09-09
Result: PASS

Scope: proof-state classification, exact RL286 identities, regression scope, successor constraints, and forbidden overclaims.

This audit was rerun during the RL287 start gate after the frozen RL286 closeout was found to reference a red-team file that had not actually been committed. The audit restores the missing verification artefact; it does not change RL286's mathematical classification.

## Checks

1. **Carry/coupon bridge is algebraically scoped correctly.** RL286 claims only for genuine positive first-return excursions that `C_E=W_x-W_y=3^r D_E/Q_in`, equivalently `C_E/2^L=D_E/Q_out`. The zero-rank expansion in the report gives the same Ferrers-cell sum termwise after multiplying the inherited coupon-defect formula by `3^r`.

2. **Height cell count/support is consistent.** The component has exactly `sum_j h_j=h` cells. With exponents `p=j-1+u_j+q`, the mandatory entry zero gives the unique exponent-zero cell, and the inherited first-return nesting inequality bounds every exponent by `h-1`.

3. **One-zero barrier is exact.** For `x=0 1^h`, `y=1^h 0`, the identity `C_E=3^h-2^h` gives `C_E/2^h=(3/2)^h-1`, so a uniform state-free height-only normalized-carry cap is genuinely impossible.

4. **No local valuation induction is revived.** RL286 explicitly preserves the earlier counterexamples to blockwise `nu_2(J)` growth bounded by excursion height and states that a state-dependent reserve is still required.

5. **Portable regression rerun passes.** The committed verifier was rerun independently during this startup repair. It reproduces exactly `13,909` first-return excursions and `199` one-zero excursions, with all bridge, cell-count/support, uniqueness, and one-zero assertions passing.

6. **Finite regression is not promoted to theorem.** The bounded verifier is used only as regression support for the analytic identities and does not claim Gate A or the global post-column valuation inequality.

7. **Successor scope is correct.** RL287 is directed to a return-normalized, state-dependent reserve closed under arbitrary positive zero-height boundary retention, coupling the RL286 defect identity with one-zero rigidity and RL281 multi-zero pricing.

8. **Residual is unchanged.** Gate A remains open exactly at odd `k>=25` with `H_can<k`; no global `nu_2(K-1)<=H+d-1` theorem is claimed.

9. **Frozen fronts remain frozen.** Gate B stays separate/open, the fifth selector is unscanned, and Radius 6+ remains frozen.

10. **No global Collatz conclusion.** RL286 does not claim exclusion of non-trivial Collatz cycles.
