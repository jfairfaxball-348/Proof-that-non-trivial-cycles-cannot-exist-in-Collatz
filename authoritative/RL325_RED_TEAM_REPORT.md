# RL325 red-team report

Date: 2026-09-15
Status: PASS FOR CLOSEOUT CANDIDATE

## RT1 — live-branch scope transfer

Question: does any promoted RL325 theorem use the RL319 root-aligned cap `G<2^35` in the late-row-root branch?

Result: **PASS**.

The attempted scratch transfer is explicitly demoted in `RL325_CORRECTION_AND_DEMOTION_LEDGER.md`. The promoted contraction uses only `n-5/6<lambda G`, `G<2^z`, and the global zero budget.

## RT2 — RL324 local-counterfamily compatibility

Question: does RL325 claim an absolute displacement bound by iterating the local matched-defect recurrence?

Result: **PASS**.

No. The key new bound

`(L-h)+z<=floor(d rho/ell)`

uses the global least-root mechanical inequality across the whole crossing-to-canonical interval. That ingredient is absent from the RL324 local counterfamily. The local propagation barrier remains frozen and binding.

## RT3 — cyclic-wrap contamination

Question: is the exact ownership telescope used across the cyclic endpoint?

Result: **PASS**.

No. Every promoted telescope statement is explicitly linear. The withdrawn cyclic-wrap mode is not used.

## RT4 — strict/integer boundary handling

Question: are the integer carry caps obtained from strict inequalities with correct rounding?

Result: **PASS**.

The exact rational verifier checks:

- the initial Beatty upper bound is `<33068504828`, hence `n<=33068504827`;
- the `rho=60` Beatty upper is `<33068504813`;
- the `rho=63` Beatty upper is `<33068504812`;
- the `rho<=59` carry upper is `<33068504812`.

These are sufficient for the promoted integer conclusions.

## RT5 — maximal-carry endgame scope

Question: is `rho in {60,61,62}`, `L<=62`, or the at-most-one-zero suffix asserted for every surviving carry?

Result: **PASS**.

No. Those conclusions are stated only under the hypothesis

`n=33068504812`.

Lower carries remain open.

## RT6 — external-certificate conditioning

Question: are the external least-state floor and first-survivor constants silently promoted to unconditional statements?

Result: **PASS**.

No. The external scope remains explicitly conditional. Internal-only and external-certificate-conditional frontiers remain distinct.

## RT7 — stage-closure discipline

Question: does RL325 claim the parent bridge, Gate A, Gate B, or global cycle exclusion is closed?

Result: **PASS**.

No. R1 remains OPEN. The successor remains on the parent bridge.

## RT8 — certificate reproducibility

Question: can the numerical thresholds be checked without floating point or external dependencies?

Result: **PASS**.

`verification/verify_rl325_global_ownership.py` uses only Python's exact `Fraction` arithmetic and the 280-term rational atanh enclosure. Floating output, where printed, is informational only.

Overall red-team result: **GREEN**.
