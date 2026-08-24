# Collatz R-sharp RL17 repair + strategy handover — 2026-08-20

## Mission

This is a **repair-and-advance** handover.  Do not treat the inherited RL16 status sheet as authoritative.  A skeptical audit found that the new RL16 arguments are mostly healthy, but the inherited exact-radius-3 closure ledger is incomplete and the global bridge from local radius exclusion to an RL contradiction is still missing.

The next session has two obligations:

1. **Repair the local proof chain**: restore missing proof provenance and close or sharply reduce the radius-3 branches that the prior roadmap silently dropped.
2. **Work strategically on RL itself**: attack the missing bridge that would make local transposition exclusions globally decisive.  Do not end the session after merely extending another finite radius calculation.

## Read in this order

1. `RL17_AUDIT_FINDINGS_FREEZE.md`
2. `RL17_PROOF_STATUS_AND_BRANCH_LEDGER.md`
3. `RL17_REPAIR_AND_STRATEGY_WORKPLAN.md`
4. `RL17_FULL_D_SPARSE_PROMOTION.md`
5. `RL17_FINITE_ARITHMETIC_EVIDENCE.md`
6. `RL17_GLOBAL_BRIDGE_TARGETS.md`
7. `NEXT_SESSION_KICKOFF_PROMPT.md`

Use `audit_sources/` for the directly surfaced RL16 audit material.  If the full inherited chain is needed, unpack:

`baseline/Collatz_Rsharp_RL16_Audit_Handover_2026-08-20.zip`

That bundle recursively contains the RL15/RL14/RL11 lineage.

## Fresh RL17 executable checks

Run:

```bash
python rl17/verify_rl17_full_D_sparse.py
python rl17/verify_rl17_sparse_uniqueness_a80.py
```

Expected results are frozen in:

- `rl17/RL17_FULL_D_VERIFICATION_LOG.txt`
- `rl17/RL17_A80_SCAN_LOG.txt`

These scripts promote two former conversation-only leads to **audit-reproduced artifacts**.  The finite scan remains computational evidence, not an infinite theorem.

## Current high-level verdict

- **Exact radius 3 is not yet closed.**
- **RL16's new coefficient-5 P3 boundary and j=2 P2 strict-interior closures survive audit.**
- **RL-L104 is a reduction, not a closure.**
- The sparse reduction strengthens analytically from the cubic cofactor `C` to the full discrepancy `D`; this is proved in this handover and structurally rechecked on the same 1,359 exact one-orbit cases.
- The `a<=80` / 2,785-parameter sparse uniqueness scan is reproduced exactly, but remains finite evidence.
- Two radius-3 families were omitted from the inherited roadmap: the coefficient-3 `P2 [2,1]` boundary and the `gcd(A,L)=3, gcd(A,m)=3` sector.
- RL12 and RL13 closures are not currently proof-auditable from the packaged lineage because their verifier scripts survive but their analytic proof reports do not.
- **Closing radius 3 would still not close RL** unless a separate global theorem forces an RL object into the forbidden local configuration (or supplies a different global contradiction).

## Guardrail

Prefer discovering a missing hypothesis, counterexample, or failed bridge over harmonizing the old notes.  Keep four statuses distinct: **analytic proof**, **external theorem dependency**, **exact finite certificate**, and **computational evidence**.
