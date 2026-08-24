# Collatz R-sharp RL43 -> RL44 Audit/Review Handover

Date: 2026-08-22

This bundle is deliberately an **audit/review/road-map handover**, not a claim that RL has been closed.

The inherited RL42 bundle is included intact under `inherited/`. RL43 adds four theorem/certificate notes with companion verifiers, plus a separate exploratory/exact-computation directory.

## Current conservative status

- Inherited audited frontier entering RL43: `rho >= 49` in the surviving near-resonant order-2 / `g=2` balanced-return branch.
- RL43 exact certificate: `rho != 49`, hence **`rho >= 50`** in that branch.
- RL43 cutoff-free one-excursion theorem: a physical crossing entering with gap 9 has **excess `e >= 8`**.
- RL43 analytic bridge: defect complexity `K_def = E + N` controls sparse support; the proper-factor numerator has support at most `4 K_def` before collection.
- RL43 analytic full-denominator bridge: in the `G=4` one-excursion branch, full `D`-divisibility yields a defect-controlled phase polynomial modulo `X-Y`, against the short binomial `3 T^(a-ell) - 2` used in the inherited radius-3 work.
- Exact but audit-pending computation: all currently admissible one-excursion geometries with `26 <= e <= 40` at `(a,ell)=(65,41)` miss the required `X-Y` phase residue. If independently validated as exhaustive, this gives a one-excursion computational frontier `e >= 41`.
- Candidate uniform theorem, **not proved**: `e >= (a-ell)+2`, equivalently `rho_E >= a` in the one-excursion branch. A proposed `J_d/K` invariant is recorded for audit.

## Start here

1. `START_HERE_RL44_AUDIT.md`
2. `RL43_PROOF_STATUS_AND_AUDIT_ROADMAP.md`
3. `RL43_REPRODUCIBILITY_LEDGER.md`
4. `RL43_JK_INVARIANT_CANDIDATE.md`
5. `RL43_ONE_EXCURSION_E40_COMPUTATIONAL_LEDGER.md`
6. `NEXT_SESSION_KICKOFF_PROMPT_RL44_AUDIT.md`

Run `verification/run_all_rl43_verifiers.sh` before trusting any RL43 theorem/certificate statement.

The heavy `e<=40` scan is intentionally separate from the fast theorem verifier suite; see its ledger for commands and expected outputs.
