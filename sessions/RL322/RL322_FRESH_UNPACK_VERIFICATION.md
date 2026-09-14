# RL322 connector reconstruction verification

Date: 2026-09-14
Status: PASS AFTER MECHANICAL PATH-MAPPING REPAIR

The RL322 mathematical candidate was frozen before publication. Post-commit readback of the first Git-object publication exposed a mechanical packaging defect: several already-verified text blobs were assigned to the wrong filenames and the binary ZIP was not actually present. No theorem, certificate, scope statement, barrier, or successor target changed.

Under the connector-worker provision in `AGENTS.md` and `docs/VERIFICATION_AND_CLOSEOUT.md`, RL322 therefore uses documented lossless Git-tree transport rather than a ZIP bundle.

Verified after repair:

1. the frozen RL322 proof ledger, closeout, red-team report, strategic assessment, Branch-A barrier, incoming target, session handover, successor target, and START_HERE are mapped to their intended filenames by exact Git blob identity;
2. the portable verifier is stored as `verification/verify_rl322_negative_branch_and_positive_barrier.py`;
3. the verifier was independently reconstructed and rerun with Python `-I` during repair and returned PASS with exactly 480 Branch-B cases, forced prefix length 66, worst `h=430`, unit-interval index `28512881031`, minimum certified margin `>0.000775775058363`, and Branch-A geometry barrier PASS;
4. the frozen verifier output matches those values;
5. `RL322_TRANSPORT_MANIFEST.md` records the path-to-blob map used for both `sessions/RL322/` and successor `authoritative/`;
6. the repaired remote branch is read back after the repair commit.

This repair is mechanical only. `PARENT_DIFFICULTY_DELTA = LATERAL`; Gate A, Gate B, global positive non-trivial-cycle exclusion, and `g=1` remain exactly as stated in the proof ledger and closeout.
