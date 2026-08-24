# RL59 terminal-embeddability session — start here

Date: 2026-08-23

RL58 successfully independently audited the two new RL57 prefix certificates:

- `M0_26 <= 17/3`, hence `M0_late > 5/4`;
- `Zx_26 <= 77/10`, hence `Zx_late > 253/60`.

It also audited/repaired the local `r=0/r=1` grammar and sharpened the potential interface to

`Psi_cut < 2.533333534500`.

The strategy changes because RL58 found the exact synchronized positive cycle

`J=3 --11--> 5 --00--> 3`.

Repeated locally, it can exceed `5/4` aligned mass with zero defect and without violating the cap or Psi ceiling. Thus the next theorem must use **terminal endpoint arithmetic**.

## Run first

```bash
bash verification/run_all_rl58_to_rl59_verifiers.sh
```

Then read:

1. `RL58_FINAL_PROOF_STATE_AND_RL59_TERMINAL_EMBEDDABILITY_ROADMAP.md`
2. `RL58_AUDIT_FINDINGS_AND_OBSTRUCTION_NOTES_2026-08-23.md`
3. `RL59_TERMINAL_EMBEDDABILITY_KICKOFF_PROMPT_2026-08-23.md`

## RL59 primary objective

Classify a maximal repeated `J=3<->5` pump block, its legal entry/exit grammar, and whether it can embed in a suffix ending at

`Q_end=2^K+1`, odd `K>=25`.

The preferred proof object is a congruence/divisibility theorem that bounds pump multiplicity or reduces large multiplicity to finitely many terminal cases.

## Status warning

Gate A, Gate B, RL, and Collatz remain open. Radius-3 remains inherited/certified, but no global RL-to-radius-3 bridge is proved. The exploratory `557/100` aligned target is not promoted.
