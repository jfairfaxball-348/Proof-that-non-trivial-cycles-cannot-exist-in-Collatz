# Kickoff Prompt — Collatz R# RL-4 Phase-Aware Crossing / Cycle-Xi Coupling

Continue the dedicated RL/nontrivial-loop branch from RL-3. Do not restart raw `Phi_h` scans and do not deepen the k=0 root-only xi sieve.

Read:

1. `RL3_ROOT_XI_SPARSITY_AND_RELATIVE_HEIGHT_2026-08-19.md`
2. `RL3_CANONICAL_REGISTER_DELTA_2026-08-19.md`
3. `RL3_ROADMAP_UPDATE_2026-08-19.md`
4. `parent_rl2/RL2_SUFFIX_CODE_OBSTRUCTION_AND_XI_PROBE_ATTACK_2026-08-19.md`

Run:

```bash
python3 tools/verify_rl3_rootxi_relative.py
```

## Frozen RL-3 facts

- k=0 root xi ceiling violation sets are single 3-adic cylinders with an exact `d mod6 -> bad mod9` map.
- The full infinite root xi sieve leaves positive 3-adic measure in both inherited root branches.
- Each of the six inherited k=0 mod144 classes contains an explicit arbitrarily large integer family satisfying every root xi ceiling.
- In k>0, an entry exponent gap `2m` separates the two predecessors by an exact `4^m` affine amplification.
- Relative branch order obeys an exact recurrence; strict preperiods require at least one reverse phase with tail exponent below cycle exponent.
- If the tail is the larger entry branch, gap `2m` forces a quantitative exponent-1 contraction debt; gap 2 forces at least four later contractions.

## Primary mission

### k>0

Build the smallest exact phase-aware state that fuses entry orientation/amplification, relative ratio crossing, contraction debt, and inherited prefix slack. Test whether one orientation can be excluded analytically.

### k=0

Move xi from the root to actual cycle states. Fuse cycle-state probe valuations with minimum rotation and common-denominator integrality. Root-only xi is no longer a candidate closure route.

A successful session should produce a genuine exclusion, a proved recurrent survivor grammar/lift theorem, or a precise proof that the next proposed finite state still loses indispensable information.
