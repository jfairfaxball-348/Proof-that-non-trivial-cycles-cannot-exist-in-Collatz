# RL217 certified facts and proof ledger

Date: 2026-09-01.

## Inherited frozen state

All RL216 certified mathematics, corrections and scope locks remain authoritative. In particular:

- global necessary terminal frontier: **13,415,865,871**;
- above-p count: **7,091,831,284**; below-p count: **6,324,034,587**;
- e=16 family after RL216: **45,045 prefixes** and **331,927,916 arithmetic candidates**;
- the unique minimum-Q prefix `Q=43,013,953` remains deleted and is never reintroduced;
- both H21 states, all four necessary mod18 classes and all 469 reachable eta classes modulo2187 survive;
- e=16 terminal rank `34,124,151,203` remains live;
- arithmetic candidates are not physical H21 populations;
- `Q mod D=0` is not the quotient residue `(Q/D) mod D`;
- RL209 signed-successor scope and all physical/charge/Gate locks remain binding.

## RL217-T1 — universal phase-16 coordinate factorisation

**Classification: proved exact recurrence mathematics.**

For every inherited e=16 prefix, write

`eta = eta_* + 3^17 k`,
`x = eta_* + 3^17 k` (equivalently the lifted eta itself),
`y_16 = 2^34 x - 1 - 3^16*2^13`, `h_16=1`.

The deterministic forward odd recurrence from phase 16 is therefore independent of the prefix label `Q`: once `x` is fixed, the subsequent odd state and mechanical height are fixed. Prefix identity only supplies the finite admissible `k` interval and its affine offset.

Consequently a single 2-adic automaton in `x` can be intersected exactly with every prefix family. This is the shared-state compression required by RL217; it is not candidate-by-candidate replay.

## RL217-CERT1 — prefix-wide phase-51 modular height consumer

**Classification: exact finite modular arithmetic certificate.**

The universal automaton is propagated from phase 16 through phase 51 using the exact recurrence

`a_i=v2(3y_i+1)`,
`y_(i+1)=(3y_i+1)/2^a_i`,
`h_(i+1)=b_(i+1)-b_i+h_i-a_i`,

splitting a 2-adic branch only when the next valuation bit is genuinely unresolved. A branch is deleted exactly when every integer in it forces negative height.

At phase 51 the automaton has:

- **14,514,513** processed modular states;
- **1,705,547** certified failure cylinders;
- **3,132,617** disjoint live cylinders;
- maximum required 2-adic precision **25 bits**;
- survivor-cylinder digest `abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05`.

For a live cylinder `x=r mod2^m`, multiplication by `(3^17)^(-1) mod2^m` turns membership into an exact congruence on the prefix parameter `k`. Each finite prefix interval is counted by cyclic interval arithmetic. No enumeration of the 331,927,916 incoming candidates is used by the promoted projection.

After preserving the inherited terminal-Hensel exclusions and the already-deleted RL216 prefix, the exact phase-51 consumer leaves:

- **139,581,280** arithmetic candidates;
- **192,346,636** newly removed relative to RL216;
- **45,045** prefixes, with between **2,995** and **3,235** phase-51 survivors in every prefix;
- state011: **90,749,885** survivors;
- state111: **48,831,395** survivors;
- mod18 counts: `0:35,622,831`, `8:19,167,422`, `9:55,127,054`, `17:29,663,973`;
- all **469** reachable eta classes modulo2187 still represented.

No new prefix, state, mod18 class, eta class or terminal rank is deleted.

## RL217-B1 — finite-horizon state-growth boundary

**Classification: certified finite-horizon computation plus method barrier; not a theorem of intrinsic impossibility.**

The shared automaton succeeds as a large exact consumer, but by phase 51 the unresolved set already requires 3,132,617 disjoint cylinders and 25 bits of 2-adic precision while every prefix still has thousands of survivors. Continuing only by raw cylinder depth would rapidly increase state count and risks becoming disguised exhaustive enumeration.

RL217 therefore freezes the exact phase-51 selector as the smallest promoted unresolved interface. This does **not** prove that deeper height information cannot delete more candidates; it only records the present compression boundary and prevents an unjustified extrapolation beyond phase 51.

## Global scope

No necessary terminal rank is deleted. The e=16 terminal rank `34,124,151,203` remains represented and the global frontier remains **13,415,865,871**.

No physical H21 incidence/charge, branch contradiction, Gate A closure, Gate B closure or global nontrivial-cycle exclusion is proved.
