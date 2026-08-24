# RL26 -> RL27 release verification

Date: 2026-08-21

Release checks performed against the copied handover tree itself:

1. All files needed for the RL21--RL26 continuation are present under `continuation/`.
2. All `continuation/verify_rl*.py` scripts were executed from the handover copy.
3. Exactly **19** verifier scripts ran.
4. Every verifier completed successfully; see `VERIFIER_LEDGER.txt`.
5. The handover retains the RL23 checkpoint documentation and the RL20 / RL22->RL23 prior ZIPs for provenance recovery.
6. `SHA256SUMS.txt` is generated only after the release files are finalized.
7. The final ZIP is tested with `unzip -t` after creation.

Proof-state reminder:

- RL remains open.
- The strongest RL24 packing theorem is analytic for `R>=161`.
- The numerical CF floor `57,397,300,723` additionally uses inherited external computational input `R>=2^71`.
- RL25 Section 7 and RL26 Section 6 are finite certificates, not global cycle theorems.
- RL23 saturation constructions are exact finite trajectory witnesses, not cycles.
