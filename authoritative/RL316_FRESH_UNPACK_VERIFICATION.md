# RL316 to RL317 fresh-unpack verification

Date: 2026-09-14
Status: PASS

Bundle:
`RL316_to_RL317_Handover.zip`

Outer SHA-256:
`33d4a5f555d8b6456abec28e3e64f8f7cb64831eb103663645a2997775fb53d8`

Checks performed in a newly created temporary directory:

1. outer `.zip.sha256` sidecar: PASS;
2. safe clean extraction: PASS;
3. unique internal `SHA256SUMS.txt`: PASS;
4. every internal manifest member hash: PASS;
5. `python3 -I verification/verify_rl316_row_energy.py`: PASS;
6. `python3 -I verification/verify_rl316_g2_dual_shadow.py`: PASS.

Verifier totals:

- 2,645 general canonical words;
- 224,325 balanced `g=2` row pairs;
- 111,350 ordered bounded dual-shadow pairs;
- frozen RL21 `H`-factor saturation replay: PASS;
- frozen RL38 area-seven saturation replay: PASS.

The unpack contained exactly the closeout, proof ledger, red-team report,
session state, incoming target archive, successor target, verifier output,
two portable verifiers, and one internal manifest listed by the bundle build.
