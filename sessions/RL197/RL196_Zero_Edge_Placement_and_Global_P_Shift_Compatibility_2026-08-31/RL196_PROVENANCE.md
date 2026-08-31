# RL196 provenance

Date: 2026-08-31.
BASE_HEAD: `a6d0c0b0821723b0d8338f4ffab83b841e79c038`.

RL196 uses the frozen RL195 authority without recursively re-auditing historical bundles. Direct live dependencies are the RL195 height recurrence, rank map, p-shift convention, `G_0=...=G_23=0`, N0/J00 floors, and H21 ledger.

The new theorem is exact arithmetic plus one finite residue-count barrier, checked by `verification/verify_rl196_p_shift_compatibility.py`.

Bundle: `RL196_Zero_Edge_Placement_and_Global_P_Shift_Compatibility_2026-08-31.zip`
SHA256: `a2e3b1109db69ad53c0efb8e522e44633193719978b9ae617543ba54b5e6a1c0`.
The bundle contains only the new RL196 proof/session payload and verifier; inherited RL195 files remain authoritative by verification economy.
