# RL261 — third-selector exact terminal/capacity contraction target

Date prepared: 2026-09-05
Status: **PREPARED, NOT STARTED**

## Incoming promoted state

RL260 removes the second selector `(1119,706,413,802,506,14,10)` from the
simultaneously unresolved branch by proving `k=31 => H_can>=31`; RL259 had
already proved the corresponding `k=33` result.

Using the inherited selector predicate, RL260 proves that there is no retained
selector for `1120<=a<1287` and that the next exact selector is uniquely

`(a,ell,z,q,r,H_sel,n)=(1287,812,475,485,306,16,6)`.

## Unique target

Work only at this selector until the next theorem-sized contraction.

1. Reconstruct its exact halving/physical-block geometry and complement capacity.
2. Derive the exact surviving odd terminal-exponent range using only promoted
   capacity, terminal-zero, parity, and canonical-flank constraints.
3. Enumerate the surviving flank families exactly and attack from the cheapest
   terminal exponent downward.
4. Use the RL260 minimum-area closure certificate when it is computationally
   finite and exact; where it is not, preserve the ordered active-rank/full-phase
   information rather than weakening to an untargeted state relaxation.
5. Radius 4 may be used only if every audited primitive/full-D/exact-distance
   hypothesis is explicitly manufactured.  Radius 5 remains inactive.

## Unpromoted leads from RL260 scratch

The previous worker saw indications of a much smaller high-`k` family and a
possible `k=39` active-rank/phase contraction.  None of those counts or claims
is inherited.  Recompute them independently before using them.

Gate A remains open uniformly.  Gate B remains open.
