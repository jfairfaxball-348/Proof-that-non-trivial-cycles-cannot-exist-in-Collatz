# Collatz R-sharp RL16 audit/review handover — 2026-08-20

## Purpose

This bundle is for an **audit/review session**, not for immediately extending the proof.  The first job is to establish exactly what is frozen, what remains open, how close the radius-3 program is to completion, and whether completing radius 3 would actually close RL.

## Baseline lineage

- `baseline/Collatz_Rsharp_RL15_Handover_2026-08-20.zip` contains the inherited RL15 state and, recursively, the earlier RL14/RL11 lineage.
- `rl16/` contains the current RL16 delta, its two verifiers, original logs, and a fresh recheck log produced while packaging this audit handover.
- `audit_context/` surfaces a small set of older roadmap/dependency files directly so an auditor does not have to unpack the whole lineage before challenging the global proof architecture.

## Current frozen verdict

The packaged/verifiable RL16 state supports the following:

1. The remaining coprime same-direction radius-3 targets listed at RL15 are closed by RL16: the coefficient-5 `P3 [2,1]` boundary (`j=0` and `j=1`) and the coprime `j=2, P2, [1,1,1]` strict interior.
2. The `gcd(A,L)=3` one-orbit branch has a new **analytic reduction** (RL-L104) to a sparse `1,3,9` congruence modulo the cubic cofactor `C`.
3. RL-L104 is **not** a closure.  The converse “sparse zero forces exact `a,a,a` spacing / third repetition” remains unproved.
4. The later conversational lead claiming a sparse relation modulo the **full discrepancy `D`**, and the reported pure-arithmetic uniqueness scan through `a<=80` / 2,785 admissible parameter choices, are **not frozen in the files in this bundle**.  They must be treated as leads to reproduce, not as established results.
5. Closing the cubic-cofactor branch would plausibly complete the inherited **exact radius-3 classification**, subject to re-auditing the case decomposition.  It would **not by itself prove RL**.  The older global RL architecture still lacks a theorem forcing the relevant distinguished rotations into radius <=3 (or another infinite contradiction).  Radius-3 closure would strengthen a rotation-distance obstruction; it is not yet the final bridge to RL.

Read `AUDIT_STATUS_AND_DISTANCE_TO_RL.md` before doing new mathematics.

## Verification

Run from the bundle root:

```bash
python rl16/verify_rl16_p3_boundary_j2p2.py
python rl16/verify_rl16_cubic_cofactor_sparse.py
```

Both were rerun successfully during packaging; see `rl16/RL16_FRESH_RECHECK_2026-08-20.txt`.

## Audit posture

Do not accept branch completeness, LMN usage, resultant nonvanishing, finite cutoff logic, or the sufficiency of radius-3 closure merely because the previous sessions say so.  Re-derive those dependencies and label each item **PROVED**, **EXTERNAL**, **FINITE CERTIFICATE**, **COMPUTATIONAL EVIDENCE**, or **OPEN**.
