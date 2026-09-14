# RL317 fresh-unpack verification

Date: 2026-09-14
Status: PASS

Canonical bundle:
`RL317_to_RL318_Handover.zip`

Transport for connector promotion:
`RL317_to_RL318_Handover_BUNDLE_TRANSPORT/` (checksummed Base64 parts,
losslessly reconstructing the canonical ZIP).

Outer SHA-256:
`c0d34dd9aaea94163c591351609ede1f05f3438d4191c2fb0a75ec45c2d0d6fd`

Checks performed on the frozen candidate and repeated from a clean local
reconstruction before promotion:

1. outer `.zip.sha256` sidecar: PASS;
2. ZIP extraction: PASS;
3. unique internal `SHA256SUMS.txt`: PASS;
4. every listed internal file hash: PASS;
5. `verify_rl317_dual_shadow_composition.py`: PASS;
6. `verify_rl317_cofactor_mismatch.py`: PASS;
7. `verify_rl317_generalized_increment_reduction.py`: PASS;
8. `verify_rl317_first_reduced_fibre.py`: PASS;
9. saved certificate JSON and its sidecar: PASS.

Exact regression counts:

- 111,350 ordered row pairs;
- 221 `D0`-owned nonzero-remainder pairs;
- 1,024,422 factor/content cases;
- 1,017,228 two-clock cases;
- 190,497 contiguous `ell` values in `41..190537`.

The first-fibre verifier regenerated the certificate object exactly and
reported certificate SHA-256
`dfdb70f67b657410e2219ed3aca79d2116bb5c9c3e8fa434a837bc5d948e0edb`.

No incoming-authority file was changed during candidate or fresh-unpack
verification. The packaging adaptation from physical ZIP to checksummed Base64
transport changes no canonical bundle byte or mathematical claim.
