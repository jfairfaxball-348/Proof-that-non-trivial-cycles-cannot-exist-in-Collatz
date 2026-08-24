# RL29 audit handover release verification

Date: 2026-08-21

## Original handover integrity

The user-supplied RL27->RL28 archive was checked against its supplied SHA256 file before unpacking: PASS.

## Inherited verifier rerun

The inherited 20-verifier stack was rerun from the supplied archive.

An aggregate shell invocation reached its execution cap during `verify_rl24_typeI_high_start_supporting_line.py` after the preceding 15 verifiers had already printed PASS. The unfinished tail was then rerun individually with per-script limits:

- `verify_rl24_typeI_high_start_supporting_line.py`: PASS
- `verify_rl24_valuation_coupled_packing.py`: PASS
- `verify_rl25_cubic_range_orientation.py`: PASS
- `verify_rl26_cubic_mod32_hard_sector.py`: PASS
- `verify_rl27_full_spread_adjacent_ownership.py`: PASS

Therefore the mathematical verifier status is:

> inherited verifiers: **20/20 PASS**.

Raw outputs are retained as `INHERITED_VERIFIER_RERUN_PART1.txt` and `INHERITED_VERIFIER_RERUN_TAIL.txt`.

## New RL29 checks

- `rl29_additions/verify_rl29_exact_ownership_and_lifts.py`: PASS
- `rl29_additions/verify_rl29_transport_scaling.py`: PASS

These scripts are exact/sanity certificates for algebra and finite arithmetic. They do not replace the analytic audit requested in `RL29_AUDIT_LEDGER.md`.

## Exploratory reproduction

`rl29_experiments/reproduce_rl29_lift_density_to35.py` reproduced:

- depth 20: 109 survivors, min unsynchronized 13;
- depth 25: 794 survivors, min unsynchronized 14;
- depth 30: 6458 survivors, min unsynchronized 18;
- depth 35: 43996 survivors, min unsynchronized 20.

This is session evidence only.

## Release status

Inherited proof verifiers: 20 PASS.
New RL29 sanity verifiers: 2 PASS.
Total scripts checked for release: 22 PASS.

**RL status: OPEN.**
