# RL329 finite positive-run enumeration barrier

Date: 2026-09-15
Status: FROZEN PROVED ANALYTIC METHOD BARRIER
Incoming authoritative HEAD: `828db8a17863a676e35df61168741e31fd721c63`

## Purpose

RL329 showed by exact physical reconstruction that the specific RL328 unrestricted three-positive `N(49)->N(49)` edge has no high-carry physical realization. That reopens long-positive-run ownership, but it also raises an immediate strategic question: should one now enumerate run lengths `p=4,5,6,...` one at a time?

The answer is no as a default closure programme.

## Barrier theorem

Suppose a successor bridge graph has exact ownership information for every positive-excess run of lengths at most `P`, but — as a conservative fallback — still admits every positive run of length at least `P+1` between zero plateaux of lengths at most 49.

Then the unchanged fallback contains the self-cycle

`N(49) -> N(49)`

using a positive run of length exactly `P+1`.

For one traversal this cycle has

`Z=49`,
`K=P+1`,

so repetition forces every fixed-boundary density inequality

`Z <= R K + B`

on that conservative graph to have

`R >= 49/(P+1)`.

This is the same max-plus obstruction mechanism used by RL328, with `3` replaced by the first run length left unrestricted.

Classification: **proved analytic method barrier for finite run-length truncation**.

## Quantitative consequences at the inherited consumer

RL328 proved that the residue-min linear telescope requires asymptotically

`Z/K < 0.21777433003982435...`

to reach the high-carry ownership floor `n=20390252058`.

Since `49/225 = 0.217777...` is still too large while `49/226 = 0.216814159292...` is below the diagnostic threshold, one would have to certify every positive-run length through at least 225 merely to remove this particular fallback-cycle obstruction for that consumer.

RL328 also proved that even the impossible optimistic factor-two height gain in the same linear coefficient family still requires

`Z/K < 1.1357780287610304...`.

Here `49/43 = 1.139534...` is too large whereas `49/44 = 1.113636...` is below the diagnostic threshold. Thus even under the factor-two ceiling, a run-by-run programme would need exact control through at least length 43 before this one fallback cycle ceased to be a certified obstruction.

These are necessary thresholds for that architecture, not sufficient conditions for closure.

## Strategic conclusion

The exact p=3 certificate is useful because it proves that RL328's displayed `49/3` cycle is not physically realized. But p=4, p=5, ... enumeration must remain diagnostic/subordinate.

The next theorem must compress infinitely many positive-run lengths at once, or strengthen the consumer so that long-run geometry is charged by more than raw positive-rank count. Suitable targets remain an all-length owned-state drift/descent theorem, a global run/residue coupling theorem, or a height/displacement-sensitive nonlinear telescope.

R1 OPEN. Gate A OPEN. Gate B OPEN. `g=1` separate. Global positive non-trivial-cycle exclusion OPEN.