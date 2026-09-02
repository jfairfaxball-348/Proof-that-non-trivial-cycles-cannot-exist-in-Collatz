# RL234_Stop_and_Repair_RL231_Charging_Coverage_2026-09-02

Completed RL234 authoritative package.

Outcome: **STOP-AND-REPAIR** under the repository integrity protocol.

RL234 discovered a coverage defect in the promoted RL231 sparse-family charging theorem. An exact retained H20 necessary ownership cell with terminal invariant `T=5*3^35`, `H=20`, and simultaneous owners `{32,33,34,35}` is overcharged by the RL231 schedule but is not included in RL231's explicit exceptional-family penalty table.

The following dependent claims are therefore demoted pending repair:

- RL231 ordinary absolute corrected-flow bound `>665`;
- its derived signed-flow and directional-K bounds;
- the derived `N17<=1,615` threshold and spacing-only scale `85,103,989`;
- RL233's `b>=85,103,989` standalone-3-adic scale consequence, because it inherits that target scale.

Unaffected exact/analytic results are preserved, including RL232's combined H17 spacing `>=1001` and RL233's finite-modulus decomposition theorem.

Run the portable fast suite:

```sh
bash verification/run_fast_rl234_verifiers.sh
```

Unique successor:

`RL235_REPAIR_RL231_SPARSE_FAMILY_CHARGING_COVERAGE_AND_REBASE_H17_TARGET.md`

RL235 is prepared but **NOT STARTED**.
