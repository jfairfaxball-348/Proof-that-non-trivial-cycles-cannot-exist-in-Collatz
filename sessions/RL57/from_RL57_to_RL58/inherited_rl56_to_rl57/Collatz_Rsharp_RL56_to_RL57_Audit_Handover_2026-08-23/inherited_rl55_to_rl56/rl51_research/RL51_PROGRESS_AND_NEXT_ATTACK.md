# RL51 progress and next attack

Date: 2026-08-22

## Executive status

Gate A is still open globally. The RL branch is not closed.

RL51 has, however, completed the primary handover target for the sole stable continued-fraction survivor:

**the stable `z=27` case is eliminated.**

By parity (`q` odd, `t` even), that survivor now satisfies `z>=29`.

## New analytic/certificate result

The `z=27` proof couples three previously separate pieces:

1. `E<5/3` plus the exact zero identity forces `Zx>143/12`;
2. among 26 x-zeros, the safe sequential cap then forces one unique greedy x-zero schedule, with the final x-zero at column 70;
3. terminal `J=2^k` 3-adic predecessor arithmetic permits at most 56 all-x-one suffix columns, while the forced schedule requires `ell-48 = 77692117359936589355` such columns.

Contradiction.

The backward suffix bound is independently checked by both residue and symbolic-affine exact searches.

## z=29 probe

For `z=29`, exact terminal arithmetic bounds the final all-x-one suffix by 67 columns. Hence the last x-zero is terminal-negligible.

This alone is insufficient. Exact sequential-cap maxima show:

`M_26 = 11.9250209414... > 143/12`,

`M_25 = 11.5254046049... < 143/12`.

Thus the same phase-mass strategy becomes decisive exactly when the **last three** x-zeros are forced terminal-near.

## Immediate next finite target

Build the backward terminal automaton allowing at most two x-zero edges. Use exact maps in `Q_d=J+2^d-1`:

- `11` backward: `Q -> 2Q/3` (requires `3|Q`), height fixed;
- `10` backward: `Q -> 2Q+1`, height +1;
- `00` backward: `Q -> 2Q-(3^d-1)`, height fixed;
- `01` backward from current height `d>1`: `Q -> 2Q/3 - 3^(d-1)` (requires `3|Q`), height -1.

Track at most 28 y-zeros and at most two x-zero edges. A denominator-independent finite certificate bounding the resulting terminal suffix would eliminate `z=29`.

## Proof ledger

### Stable inherited inputs

- Barina peer-reviewed verification through `2^71`;
- RL50 safe continued-fraction gate and sole survivor below the Legendre range;
- full-phase survivor bounds `S>45/4`, `E<5/3`;
- exact zero identities and sequential prefix cap;
- terminal quotient `J=2^k` and parity constraints.

### New RL51 theorem/certificate

- stable sole-survivor `z=27` impossible;
- therefore sole stable survivor has `z>=29`.

### New exact barrier

- at `z=29`, last x-zero terminal-negligible is not enough;
- two terminal-negligible x-zeros are still not enough under the clean `E<5/3` threshold;
- three terminal-negligible x-zeros are sufficient for the zero-mass contradiction.

### Still open

- `z=29` itself;
- higher `z` on the sole safe survivor;
- denominators outside the safe Legendre gate;
- uniform Gate A `H>=t+3`;
- global RL closure.

## Prohibited overclaim

Do not state that Gate A, RL, or Collatz is solved. The new theorem removes one genuine surviving structural case and establishes a productive terminal-power mechanism, but the global branch remains open.
