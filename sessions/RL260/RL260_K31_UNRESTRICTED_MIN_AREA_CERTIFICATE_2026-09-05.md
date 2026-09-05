# RL260 — second-selector k=31 unrestricted minimum-area certificate

Date: 2026-09-05
Classification: **EXACT FINITE CERTIFICATE / TARGETED GATE-A THEOREM**

## Result

At the RL259 selector

`(a,ell,z,q,r,H_sel,n)=(1119,706,413,802,506,14,10)`,

the remaining `k=31` family is Gate-A safe:

`boxed: k=31 => H_can>=31`.

Together with RL259's promoted `k=33 => H_can>=33`, the whole second selector is
removed from the branch simultaneously unresolved by Gate A and Gate B.

## Exact contraction

Starting from the RL259-owned 8,976 flank pairs, the RL260 verifier reconstructs:

- 172,633 exact terminal-owned prefix/suffix chain realizations;
- 8,571 realizations after imposing hypothetical Gate-A danger `H_can<=30`
  through exact prefix/suffix area plus the unavoidable bridge lower bound;
- 2,778 distinct retained flank-pattern pairs;
- 28 distinct canonical prefix states `(d,J)`;
- 306 distinct `(middle_budget,d,J)` start cases;
- 1,064 distinct terminal predecessor states `(d,J)`;
- required terminal predecessor quotient range
  `3016492794 <= J <= 244335916693`.

The middle has the inherited fixed length 1068.

## Stronger unrestricted-time certificate

For a fixed canonical prefix state, propagate the exact quotient transition
`step_x` while labelling each reachable `(d,J)` by the minimum additional
canonical area required to reach it.  An edge leaving height `d` costs `d-1`.
Only states whose minimum area is within the relevant middle budget are retained.

This is a relaxation of the required 1068-step middle because time is discarded:
if a required terminal predecessor cannot be reached at *any* length within the
area budget, it cannot be reached at length 1068.

The portable C++ verifier exhausts the minimum-area reachable closure for all 28
canonical starts.  For every one of the 8,571 Gate-A-dangerous owned
realizations, its exact required terminal predecessor is absent at or below its
case-specific middle-area budget.  Total target hits: **zero**.

Therefore every hypothetical `H_can<=30` realization is impossible, proving
`k=31 => H_can>=31` at this selector.

## Successor arithmetic frontier

Using exactly the inherited RL259 selector predicate, the core verifier scans
`1120<=a<=1287` and finds exactly one retained selector:

`(1287,812,475,485,306,16,6)`.

Hence no retained selector exists for `1120<=a<1287`, and this tuple is the
next arithmetic frontier after removal of the second selector.

## Scope

This is targeted.  Gate A remains open uniformly and Gate B remains open.
Radius 4 is not invoked.  Radius 5 remains inactive.  `H_sel` is not identified
with `H_can`, and the corrected internal endpoint `J=2^k` before the omitted
terminal `10` is used throughout.
