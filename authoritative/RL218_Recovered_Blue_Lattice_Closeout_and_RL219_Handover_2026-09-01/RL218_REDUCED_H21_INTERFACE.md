# RL218 reduced H21 interface for RL219

Date: 2026-09-01.

This is the compact load-bearing incoming interface. Historical generations are in `sessions/`; normal RL219 startup does not need to recursively read them.

## Global necessary-rank state

- necessary terminal ranks: **13,415,865,871**
- above p: **7,091,831,284**
- below p: **6,324,034,587**
- Gate A: open globally
- Gate B: open globally
- global nontrivial-cycle exclusion: open

## e=16 modern arithmetic family

- **45,045** live prefixes
- **139,581,280** phase-51 arithmetic candidates
- each prefix root is `y(k)=y_*+3*2^58 k` on its exact short finite k-window with inherited terminal-Hensel exclusions
- phase-51 selector: **3,132,617** live disjoint 2-adic cylinders, maximum precision **25 bits**
- survivor digest: `abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05`
- state011: **90,749,885**; state111: **48,831,395**
- mod18 counts: `0:35,622,831`, `8:19,167,422`, `9:55,127,054`, `17:29,663,973`
- all **469** reachable eta classes mod2187 remain represented
- terminal rank **34,124,151,203** remains live

## RL218 backward-recognition interface

For a legal odd-only backward word with h odd inverses and exponent word `(e_1,...,e_h)`,
`Q_0=0`, `Q_j=2^e_j Q_(j-1)+3^(j-1)`. For odd root y and odd endpoint seed s:
`2^E s = 3^h y + Q_h`, with canonical exact branch condition
`E=v2(3^h y+Q_h)`.

After `y=y_*+3*2^58 k`, write
`A=3^h y_*+Q_h`, `C=3^(h+1)`, so
`N(k)=A+C*2^58*k`.

- If `v2(A)<58`, exact valuation is constant in k.
- If `v2(A)>=58`, `E=58+d` gives one exact class
  `k=kappa_d mod 2^(d+1)`.
- A fixed certified-blue seed plus a fixed word gives at most one exact k.
- A phase-51 cylinder and a high-valuation word class intersect by the usual compatible dyadic congruence test.

## Closed/negative subroutes from RL218

Do not repeat these as if open:
- explicit RL80 LTE analytic blue comb: zero possible intersections across all 45,046 inherited bases;
- seed-1 legal reverse tree depths 0..86: zero RL217 lattice matches;
- fixed seed + fixed word cannot certify a non-singleton k-class.

The unfinished forward-floor experiment is not a result and must not be inherited as one.

## What would now count as progress

A useful blue-basin attack needs a **compressed certified endpoint set**, not more singleton reverse-tree growth. Examples: an independently certified blue interval/progression/finite union that pulls back through the affine endpoint lattices, or an exact equality theorem that eliminates whole k-classes/prefixes. Any such result must still identify the same physical integers.
