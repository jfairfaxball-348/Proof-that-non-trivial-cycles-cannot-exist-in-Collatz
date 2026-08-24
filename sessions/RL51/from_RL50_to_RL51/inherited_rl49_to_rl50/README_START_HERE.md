# Collatz R# RL49 -> RL50 handover

Date: 2026-08-22

## Start here

This bundle continues the RL/3n+1 branch after the RL49 bridge audit. It is designed to be self-contained enough for a fresh session to verify the repaired RL48 baseline, inspect the recovered RL18-RL20 radius-3 provenance, reproduce all new RL49 calculations, and then attack the genuinely live bridge.

**Do not claim RL or Collatz is closed.** The session made important narrowing progress, but the decisive coupled structural lemma remains open.

First run:

```bash
bash verification/run_all_rl49_handover_verifiers.sh
```

Treat any failure as a stop-and-repair event.

Then read, in order:

1. `RL49_PROOF_STATE_AND_NEXT_ATTACK.md`
2. `RL49_REPRODUCIBILITY_LEDGER.md`
3. `rl49_research/RL49_RADIUS3_MATCH_AUDIT_AND_CORRECTION.md`
4. `rl49_research/RL49_PHASE_RESONANCE_AND_HEIGHT1_COUPLING.md`
5. `rl49_research/RL49_STRENGTHENED_EXTERNAL_FLOOR_AND_FAREY_GATE.md`
6. `RL50_COUPLED_NARROW_STRIP_KICKOFF_PROMPT_2026-08-22.md`

## Most important correction

The RL48 four-swap/full-phase pair `N <-> N+4` does **not** itself satisfy RL19's exact radius-3 hypothesis. RL19 radius means cyclic adjacent-transposition distance 3 between a full parity word and a rotation. For the actual half-period rotation `uv -> vu`, RL49 proves

`dist_cyc(uv,vu) = 2(a-t-3+H)`,

which is always even. The direct "third-bit split = radius 3" bridge is dead and must not be revived.

## Most important new positive results

Under hypothetical full phase, with `zeta=2^a/3^ell`, RL49 proves

`N(zeta-1) < 398/45`.

Using the external 2025 recursive-sufficiency prefix extension recorded in the research note, this gives a conditional denominator floor

`ell >= 205632218873398596256`,

with first presently live upper convergent

`(a,ell,q) = (325919355854421968365, 205632218873398596256, 120287136981023372109)`.

Separately, the height-one synchronized mass has an exact telescoping law. If `g=2^i/3^p`, then on a maximal height-one synchronized segment

`sum_(11) 2w = (gT)_exit - (gT)_entry`.

The normalized zero-position identities also compress the rank defect:

`X = 1-g_end+Zx`,

`S = 1-g_end+Zy`,

`E = Zx-Zy`,

and full phase gives

`27 N(zeta-1) = 127 + 8S`.

These are the coordinates in which the next proof attempt should be made.

## Live closure target

The recommended target is a **coupled narrow-strip / area incompatibility lemma**:

> No retained one-excursion path satisfying the exact prefix cap, the full-phase quotient condition, and `T+1=2^(t+3)` can have `H <= t+2`.

An even stronger success would prove full phase impossible directly.

Do not spend the next session on a larger blind continued-fraction scan or on generic bounded-radius reductions. Use the phase condition from the start and compress height-one synchronized blocks exactly.

## Provenance layout

- `baseline_rl48/`: repaired and passing RL48->RL49 baseline.
- `rl49_research/`: all new RL49 notes and exact verifiers.
- `provenance/`: selected immediately useful RL18-RL20 theorem/ledger extracts.
- `recovered_bundles/`: original RL18, RL19, RL20 and RL48->RL49 ZIPs.
- `verification/`: release verifier for this handover.
