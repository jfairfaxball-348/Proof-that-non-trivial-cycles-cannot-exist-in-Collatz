# RL196 Certified Facts and Proof Ledger

Date: 2026-08-31. Conditional physical branch remains `(37,0,23,-1)`.

## Newly proved analytic mathematics

- `pB=1 (mod L)`, hence p-shift is exactly rank `+1`.
- With `t=L-p=72057431991`, `c_(i+p)=c_i` for every phase except: `i=t-1` difference `+1`; `i=t` difference `-1`.
- `G_(i+1)-G_i=c_i-c_(i+p)+a_(i+p)-a_i`.
- Frozen `G_0=...=G_23=0` therefore gives, for `0<=i<=22`, exact p-shift copying of edge heights and exponents.
- `h_0=h_1=h_p=h_(p+1)=0`; the zero edge `0->1` has exact p-shifted copy `p->p+1`, with source ranks 0 and 1.
- A rank-set relaxation satisfies the inherited N0/J00 floors and retains exactly that one rank adjacency. Thus those bulk floors plus the anchor do not force a second p-shift zero pair.

## Exact certificate

`verification/verify_rl196_p_shift_compatibility.py` checks Bezout/rank-shift arithmetic, exact seam inverse-rank phases, p-shift digit equality on the frozen prefix, the baseline seam carry, and exact counts 55,011,218,125 and 38,921,468,263 in the placement barrier.

## Inherited state retained

RL195's `J00>=9719139553`, `N0>=43742681439`, necessary-rank cardinality 27057465824, canonical terminal floors 190574/1826072, spacing>=1001, N35<=7559400754, ordinary flow>480, directional K variation>80, complete-word denominator equivalence, local depth3 barrier, and all prior correction guardrails are unchanged.

H21 remains core `[23369453298,41775866136]` minus 14 deletions, canonical floor 67, binding `{33,34,35}` budget and ownership obligations.

## Open obligations

No second p-shift zero pair, H21 ownership multiplicity, H21 budget release, atom realization/exclusion, branch closure or global Collatz closure is proved. RL197 must introduce genuinely additional physical/global coupling.
