# RL202 — H21 root-anchor speed cone and height collision

Date: 2026-08-31. Incoming handover RL201; BASE_HEAD
`934f1289d655734d3ea8d78b3677ca200aab1d57`.
All physical implications remain conditional on the sole high branch
`(37,0,23,-1)`.

RL202 satisfies the incoming target's requested substantive absolute-anchor
restriction without claiming the still-open dyadic prefix selector.

## Result

Using exact `K_0=2^37`, lifted `K_L=lambda K_0`, the carry-free local K speed
bound, and `N=2^24`, every H21 terminal whose canonical phase is in
`[0,N) U [L-N,L)` must have rank in
`[38643145224,38659291956]`.

Exact modular counting removes 3,946,781 previously surviving necessary ranks
from those two windows. Independently, the forced positive 34-phase H21 tail
cannot hit inherited zero-height anchors `0,1,p,p+1`, adding four new exclusions:
`26058127775,28746802251,36398517186,39087191662`.

The inherited necessary count therefore falls from 16,192,674,019 to
**16,188,727,234**.

The four eta classes `0,8,9,17 mod18`, state e35, terminal sign/valuation and all
H21 charging/branch/Gate/global obligations remain open. The next target returns
to the exact dyadic joint-prefix moment after carrying forward this stronger
absolute-anchor rank set.

See `proofs/RL202_ABSOLUTE_ROOT_ANCHOR.md` and the canonical proof ledger for
full definitions, classifications and scope.
