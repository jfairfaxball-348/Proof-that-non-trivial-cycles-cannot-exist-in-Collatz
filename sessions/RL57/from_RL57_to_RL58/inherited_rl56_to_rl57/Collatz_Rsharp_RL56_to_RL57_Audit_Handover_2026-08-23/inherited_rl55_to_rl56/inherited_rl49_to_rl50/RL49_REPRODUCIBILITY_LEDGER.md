# RL49 reproducibility ledger

Date: 2026-08-22

## Release command

```bash
bash verification/run_all_rl49_handover_verifiers.sh
```

Expected last line:

`RL49->RL50 handover verifiers: PASS`

## Verifier map

| Result | File | Nature |
|---|---|---|
| repaired RL48 baseline | `baseline_rl48/verification/run_rl48_handover_verifiers.sh` | inherited exact checks + regressions |
| half-rotation metric correction | `rl49_research/verify_rl49_half_rotation_metric.py` | exact/regression + randomized equal-half metric tests |
| phase squeeze + first CF gate | `rl49_research/phase_squeeze/verify_rl49_phase_resonance_squeeze.py` | exact rational interval arithmetic |
| height-one mass telescoping | `rl49_research/phase_squeeze/verify_rl49_height1_mass_telescoping.py` | exact regression on audited witness |
| strengthened external-floor/Farey gate | `rl49_research/phase_squeeze/verify_rl49_ansari_floor_and_farey_extension.py` | exact arithmetic conditional on external `R_ext` input |
| zero-position telescoping | `rl49_research/phase_squeeze/verify_rl49_zero_position_telescoping.py` | exact identities/regression |

## Source notes

- `rl49_research/RL49_RADIUS3_MATCH_AUDIT_AND_CORRECTION.md`
- `rl49_research/RL49_PHASE_RESONANCE_AND_HEIGHT1_COUPLING.md`
- `rl49_research/RL49_STRENGTHENED_EXTERNAL_FLOOR_AND_FAREY_GATE.md`

## Provenance

The original recovered RL18, RL19 and RL20 ZIP handovers are preserved under `recovered_bundles/`. Selected high-value theorem/ledger files are extracted under `provenance/` for convenience. The original RL48->RL49 ZIP and sidecar are also preserved.

## Important reproducibility caveat

The numerical floor `R_ext=4*3^44+2` is entered as an external theorem input in the strengthened Farey verifier. The verifier proves the arithmetic consequence **if that external input is accepted**; it does not independently prove Ansari's recursive-sufficiency theorem.

## Release integrity

`SHA256SUMS.txt` contains hashes for every regular file in the handover except itself. The outer ZIP has a separate `.sha256` sidecar.
