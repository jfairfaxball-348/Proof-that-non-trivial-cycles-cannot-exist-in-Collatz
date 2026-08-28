# RL143 — height-one run-fibre exclusion

For the inherited first survivor, let a hypothetical full-count cycle have
`h_j in {0,1}` and multiplicity `g` in the certified one-defect range. Then
the exponent recurrence gives `a_j in {1,2,3}`. Put
`Z=g(A-L)` and let `t` be the number of ordinary zero runs. If `r` is the
number of length-two zero runs, then `Z=t+r`, so `t<=Z`.

Every odd run of length at least two followed by its zero run supplies an
RL123 CRT boundary state in the one class modulo `2*3^2=18`. The number of
such boundaries is exactly `O_2=gL-t`, hence at least `g(2L-A)`. Thus

`W >= 18(g(2L-A)-1)`.                                    (1)

For `h in {0,1}`, inherited `rho_j>(1/2)exp(j Delta/L)` and the physical
prefix inequality give every accelerated odd state `y<4exp(gDelta)m`.
Every ordinary state is either such an odd state or its first even successor;
using the odd minimum gives

`W < 6exp(gDelta)2^75`.                                  (2)

RL137 gives `m<2^75`. The rigorous inherited log enclosure gives
`exp(gDelta)<=1/(1-g Delta_hi)`. Exact rational comparison of (1) and (2)
proves a contradiction for

`303,279,262,681 <= g <= 771,316,334,039`.

Therefore no actual height-one full-count cycle occurs in that interval.
This excludes only the stated height-one branch; mixed-height, negative,
lower multiplicities, frontier/global closure, and Collatz remain open.
