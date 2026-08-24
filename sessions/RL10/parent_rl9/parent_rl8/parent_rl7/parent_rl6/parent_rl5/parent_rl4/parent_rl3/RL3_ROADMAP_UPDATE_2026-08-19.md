# RL-3 Roadmap Update — 2026-08-19

## Rank 1 — k>0 phase-aware crossing/debt automaton

Use the exact entry split from RL-L20.

### Orientation A: `b_(k-1) < a_(L-1)`

The tail predecessor begins below the cycle predecessor by a factor exceeding `4^m`. Track whether it can remain below the periodic branch while the tail height lands exactly at `R#`.

### Orientation B: `b_(k-1) > a_(L-1)`

The tail predecessor begins above the cycle predecessor by a factor exceeding `4^m`, incurs RL-L22 contraction debt, and must later cross below. The first crossing must occur at a cycle phase with tail exponent smaller than cycle exponent and must satisfy the exact ratio threshold from RL-L21.

State candidates:

- cycle phase modulo `L`;
- sign/order of `x_h-y_h`;
- a bounded interval code for `x_h/y_h` or normalized tail height;
- accumulated contraction debt / count of exponent-1 moves;
- prefix slack `beta_R*h-S_h`;
- selected cycle-state xi valuations.

Primary target: prove that one of the two entry orientations is impossible, or reduce both to a recurrent grammar with an extension theorem.

## Rank 2 — k=0 cycle-coupled xi, not root-only xi

RL-L18/L19/G7 show that all root xi ceilings plus the six inherited mod144 classes admit arbitrarily large ordinary integers. Do not deepen the root-only sieve.

Next useful xi object must involve actual cycle states and rotations, for example:

- `q_d(c_j)` tied to the local exponent/rotation;
- the common cycle denominator `D=2^A-3^L` and all rotated numerators;
- minimum-state inequalities at the rotation where `c_j=C_min=R#`;
- exact neutral-run length only where it constrains the adjacent cycle word.

## Rank 3 — test whether contraction debt is already encoded by prefix slack

Determine whether RL-L22 is genuinely sharper than RL-L5/L6 in some entry-gap/phase regimes. If it is redundant, record the equivalence and avoid a larger state. If it is sharper, quantify the surviving orientation classes.

## Rank 4 — cycle-wide valuation-frequency theorem

Seek a theorem forcing enough high `q_d(c_j)` events around a periodic word to violate the least-red barrier or the cycle product slope. Root-side probes are too sparse; periodic recurrence is the missing coupling.
