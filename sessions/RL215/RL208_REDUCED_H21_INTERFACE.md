# RL208 reduced H21 interface for RL209

All inherited constants, definitions, ownership rules and physical locks in
`RL206_INHERITED_H21_INTERFACE.md` remain in force, with RL206-C1/C2 taking
precedence over older text.

## Reduced terminal predicate

Start with the inherited RL207 necessary-terminal predicate of cardinality
16,188,727,234.  Put `N0=2^24`, `M=2^35`, and for each
`k=24,...,34`, `j=1,...,64` let `N=2^k+j*2^(k-6)` and let `N_prev` be the
immediately preceding radius (starting at N0).

For each N define exact safe band `[s_lo(N),s_hi(N)]` by the crossings of the
strictly decreasing `K_H21(r)` with

`K_0+1+N/3` and `K_0-N/3`

exactly as in `RL208_LAYERED_ROOT_CONE_CERTIFICATE.md`.  Delete a previously
surviving rank r when terminal phase `i=pr modL` lies in either

`[N_prev,N)` or `[L-N,L-N_prev)`

and r lies outside that layer's safe band.  This disjoint predicate deletes
exactly 2,765,120,323 ranks, leaving **13,423,606,911**.

No successor worker should materialize or approximate the 13-billion-element
set merely to use it; apply the inherited predicate plus the exact 704-layer
exclusion predicate.

## Source-side split

For tau34 source `a=i-34 modL`, canonical `a>p` corresponds exactly to terminal
phase `i in [0,34) U [p+35,L)`.  After RL208-CERT1:

- `a>p`: **7,099,572,324** necessary ranks;
- `a<p`: **6,324,034,587** necessary ranks.

The above-p range remains the preferred independent-information target.  No
reflection of the corrected below-p 37 / 60 / 97 theorem is available.

## Unchanged eta and physical locks

Eta classes remain `0,8,9,17 mod18`; terminal Hensel and first-rank restrictions
retain their inherited exact scope.  RL208 selects no eta/state/sign/valuation.
The sole high branch remains `(37,0,23,-1)`.  Rank survival is not physical H21
occurrence, incidence, or charge.  Gate A and Gate B remain globally open and
nontrivial-cycle exclusion remains open.

The conservative common-radius root-cone method is saturated at `M=2^35` because
its safe band there is the complete inherited core `[25583192106,41775866136]`.
Any further root-cone work must use a genuinely sharper pointwise/global input
and must subtract only disjoint new exclusions from this reduced predicate.
