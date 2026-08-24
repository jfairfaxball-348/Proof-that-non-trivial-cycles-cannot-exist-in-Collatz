# Collatz R-sharp RL26 -> RL27 handover

Date: 2026-08-21

This bundle closes the RL24--RL26 session and is intended to be the starting point for the next research session.

## Current status

- **RL remains open.**
- Exact radius 3 remains closed under the inherited audited hypotheses/dependencies; do not reopen it unless a bundled verifier fails or an inherited dependency is invalidated.
- All **19** RL21--RL26 verifier scripts pass at handover creation.
- The strongest Track-A analytic packing coefficient is

  `457841/1843200 = 0.248394639756944...`

  from `continuation/RL24_TYPEI_HIGH_START_SUPPORTING_LINE.md`.
- Conditional on the inherited **EXTERNAL COMPUTATIONAL INPUT** `R>=2^71`, the exact continued-fraction certificate is

  `L/gcd(A,L) >= 57,397,300,723`.

  This numerical floor is not an unconditional analytic theorem.
- Track B now isolates a unique weak cubic sector. In the near-resonant order-3 branch, the old `4(3B+Y)` shortest vector survives only for

  `R == 1 (mod 3), G>H`.

  The five-bit least-state sieve sharpens this to the unique weak root class

  `R == 91 (mod 96)`.

  Within the inherited RL20 exceptional weak-close branch this refines further to

  `R == 91 (mod 288)`.
- Exact weak-vector equality forces

  `G=12, H=4`.

- The RL23 local packing saturation family survives the stronger five-bit root condition in infinite subfamilies (`t == 3 or 35 mod 48`). Therefore residue sieving alone does not close the surviving branch.

## Read first

1. `START_HERE.md`
2. `RL26_PROOF_STATUS_AND_NEXT_ATTACK.md`
3. `continuation/RL24_TYPEI_HIGH_START_SUPPORTING_LINE.md`
4. `continuation/RL25_CUBIC_RANGE_ORIENTATION_AND_HARD_SECTOR.md`
5. `continuation/RL26_FIVE_BIT_LOW_STATE_AND_CUBIC_HARD_SECTOR_SIEVE.md`
6. `VERIFIER_LEDGER.txt`

The earlier RL21--RL23 notes and verifiers are retained under `continuation/` for auditability. The superseded RL24 valuation notes are also retained deliberately.

## Verification rule

Before extending the mathematics, verify `SHA256SUMS.txt` and run all `continuation/verify_rl*.py` scripts. Any failure is a **stop-and-repair event**. Do not treat a failed verifier as computational noise.
