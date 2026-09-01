# RL209 reduced H21 interface for RL210

All constants, definitions, ownership locks and physical qualifications in
`RL206_INHERITED_H21_INTERFACE.md` remain in force.  RL206-C1/C2 override older
text.  The complete RL208 reduced predicate in `RL208_REDUCED_H21_INTERFACE.md`
is the starting predicate for this interface.

## Current necessary-terminal predicate

Start with the RL208 predicate of cardinality 13,423,606,911.  On the canonical
above-p side, terminal phases lie in `[0,34) U [p+35,L)` for source
`a=i-34 modL`.  RL209 changes only the backward root-side portion
`i in [L-2^35,L)`.

1. In `[L-2^24,L)`, retain only ranks satisfying the exact pointwise inequality

`K_0+1/9-(L-i)/3 < K_H21(r) < K_0+1/8+(L-i)/3`.

This deletes 983 of the 1,969 RL208 survivors there.

2. For each `k=24,...,34`, subdivide the backward distance band
`(2^k,2^(k+1)]` into 4,096 equal sublayers.  If a sublayer has outer distance N,
retain the RL208-surviving ranks only inside the RL209 safe band defined by

`K_0+1/9-N/3 < K_H21(r) < K_0+1/8+N/3`.

The sublayers are disjoint and delete 7,740,057 additional ranks.  There are no
hits on preexisting isolated/anchor deletions.

Total RL209 deletion: **7,741,040**, all from canonical `a>p`.
The current exact counts are therefore

- total: **13,415,865,871**;
- `a>p`: **7,091,831,284**;
- `a<p`: **6,324,034,587**.

Do not materialize the multi-billion-element survivor set.  Apply the inherited
RL208 predicate followed by the exact RL209 predicate above; the portable
verifier implements the required modular counts.

## Above-p endpoint information boundary

For `a=p+e>p`, put `R_(p,a)=sum_(p<=j<a)q_j`.  The exact endpoint moment is

`E_a=3*2^(u+37)-2^u P_p+(3^p-2^u)R_(p,a)`,

and source height one gives

`S_a=u+floor((Ae+1)/L)-1>=u`.

Consequently the `2^u P_p` term is not a 56-bit-vanishing root contribution.
Any useful eta/Hensel consumer must independently control the required global
cancellation/prefix datum; merely rewriting the endpoint identity is not new
information.

For the p-shift use lifted phases.  The actual epsilon carry is unique at phase
`L-p`; a canonical wrap of `a+p` is not itself a reflected below-p tau34 source.

## Eta and physical locks

Eta classes remain `0,8,9,17 mod18`.  No eta/state/sign/valuation selector is
proved.  On the 986 exact pointwise survivors in the old backward root window,
all 42 inherited sign/valuation pairs pass the immediate signed-successor root
corridor, so that scoped consumer is exhausted without a selector.

The sole high branch remains `(37,0,23,-1)`.  Necessary ranks are not physical
H21 occurrences, incidence, or charges.  Gate A and Gate B remain globally open;
global nontrivial-cycle exclusion remains open.
