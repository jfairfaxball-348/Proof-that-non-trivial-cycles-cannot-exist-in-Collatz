# RL337 closeout verification

Date: 2026-09-16
Status: GREEN FOR THE CLAIMS LISTED BELOW

Incoming base: `a456ff4d27624d015e06f92456b08b6665946e0e`.

Portable command:

`python3 -I sessions/RL337/verification/verify_rl337_affine_profile_and_identity.py`

Observed output:

```text
RL337_AFFINE_PROFILE_GREEN
fixed_terminal_sign positive_profile_source_is_smaller
suffix_height_bound_green p<=8_exhaustive
p5_shared_identity 30437321051399780895133 31208280367336569715567 (2, 1, 2, 1, 1) [(24, 27), (24, 28), (24, 29)]
p5_reverse_rows 0
```

The checker independently verifies:

1. the affine carry recurrence and its closed form on exact integer examples;
2. preservation of total exponent under profile deformation;
3. the explicit nonnegative carry-drop formula;
4. the corrected fixed-terminal source ordering;
5. the concatenation identity;
6. the right-suffix height bound on the complete admissible profile sets through p=8 as a finite sanity check of the analytic induction;
7. exact mechanical-factor, residue, state, and ownership reconstruction for the targeted p=5 shared-state diagnostic and its reverse orientations.

The all-length affine theorem and suffix-height theorem are analytic; the finite checks are verification support, not the logical reason they hold at arbitrary length.

No checker output is interpreted as R1 closure. No q=33 theorem is asserted. The p=5 identity result is a finite diagnostic only.
