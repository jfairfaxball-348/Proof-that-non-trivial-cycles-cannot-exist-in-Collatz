# Proof note — RL198 H21 global height selector

## Lemma 1: inherited zero-prefix valuation selector

For a physical clean shallow start whose first nonzero p-defect occurs after `tau`
zero-defect transitions, the inherited RL186 owned-numerator transition law gives

`v_2(C_0)=sum_(j<tau)d_j`

with every physical transition cost `d_j>=1`.  Hence `v_2(C_0)>=tau`.

RL197 gives, for the H21 co-owner starts,

`Delta34=21*2^33`, `Delta33=63*2^32`,
`C_j=2^e_j Delta_j`, and `e_j in {0,1}`.

Therefore

`33+e34=v_2(C34)>=34`,
`32+e33=v_2(C33)>=33`.

Thus `e34=e33=1`.

RL197's locally admissible states
`000,010,011,100,110,111`
therefore reduce exactly to `011,111`.

## Lemma 2: no owned zero edge in the co-owned zero prefix

The `tau=34` numerator is `C34=21*2^34`, so its valuation equals its prefix
length.  Since its 34 transition costs are positive integers summing to 34,
each is one.

For every zero-defect/common-height transition,

`d_j=c_j+M_j-M_(j+1)`,

so `d_j=1` implies

`M_(j+1)=M_j+c_j-1>=M_j`.

At the `tau=34` start the common height is one.  It never returns to zero through
the suffix.  The preceding `tau=35 -> tau=34` edge is `0->1` in state `011` and
`1->1` in state `111`.  Hence no chronological edge in the co-owned `tau=35`
zero-defect prefix is height-zero on both p-shifted trajectories.

## Lemma 3: exact remaining leading-cost bit

At `tau=33`,
`C33=63*2^33`, so the 33 suffix costs are all one.

At `tau=35`,

- `011`: `C35=7*2^35`, total cost 35; all 35 costs are one.
- `111`: `C35=7*2^36`, total cost 36; the common last 34 costs sum to 34,
  so the leading cost is two.

Thus `e35` is exactly the same unresolved bit as `d_lead-1`.

## Lemma 4: preterminal height and numerator

For H21 terminal rank
`r in [23369453298,41775866136]` minus inherited deletions,
the previous-source rank is `(r-B) mod L`, ranging over

`[80448749305,98855162143]`.

Since this is above `R=57079296007`, the final source mechanical bit is 2.

For the `tau=34` co-owner, the RL187 ownership identity is

`Dsum=tau+ell+h_start-H`.

With `Dsum=34`, `tau=34`, `h_start=1`, `H=21`, obtain `ell=20`.
The final bit contributes one of these 20 twos, so the first 33 zero-to-zero
transitions contain 19 twos.  With initial common height one and unit costs,

`M_pre=1+19=20`.

Starting from `C33=63*2^33`, after 32 unit-cost zero transitions,

`C_pre = 3^32*C33/2^32 = 14*3^34
       = 233480543795331966`.

Then `C_pre mod 8=6`, and

`3*C_pre/2 = 7*3^35 = 350220815692997949`.

This proves the exact final prehistory interface but not which endpoint receives
the terminal exponent-one transition.  That orientation/sign bit remains open.
