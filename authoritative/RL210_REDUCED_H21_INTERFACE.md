# RL210 reduced H21 interface for RL211

All definitions, constants, corrections, ownership locks and physical
qualifications in `RL206_INHERITED_H21_INTERFACE.md` remain in force. Apply the
complete RL208 reduced predicate and then the exact RL209 pointwise predicate.

## Current necessary-terminal predicate

RL210 makes no rank deletion. The exact current counts remain:

- total: **13,415,865,871**;
- canonical `a>p`: **7,091,831,284**;
- canonical `a<p`: **6,324,034,587**.

Eta classes remain `0,8,9,17 mod18`; corrected below-p constants remain
37 / 60 / 97.

## New above-p global-prefix condition

For an above-p source `a=p+e`, `1<=e<z=L-p`, define

`S_t=b_t-h_t`, `S'_t=S_(p+t)-u=b_t-h_(p+t)` for `0<=t<z`.

The equality for S' is exact because the unique lifted p-shift carry occurs only
at t=z. Both sequences are strictly increasing and start `0,1`.

For every current necessary source with `e>=56`, a physical H21 word must obey

`sum_(t=0)^55 (2^(S'_t)-2^(S_t))3^(-t) = -3*2^37 mod2^56`.

Consequently, at their first mismatch m,

`24<=m<=37`, `min(S_m,S'_m)=37`,

and `h_t=h_(p+t)` for every t<m. If m=24, only

`S'_24=37<S_24=38`

survives the exact modulo-2^40 orientation certificate, so
`h_(p+24)=1`, `h_24=0`.

Exactly **7,091,831,278** current above-p necessary ranks have `e>=56` and hence
carry this necessary global selector.

## Small-offset boundary

Exactly six current above-p necessary sources have `1<=e<56`:

`e = 4,16,28,33,40,45`.

At e=4 and e=16, a physical word must satisfy

`h_t=h_(p+t)` for `0<=t<=e`, and therefore
`K_0=K_1=...=K_(e+1)=2^37`.

No additional selector is proved for e=28,33,40,45 in RL210.

## Scope locks

RL210 selects no eta class, 011/111 state, terminal sign or valuation. A necessary
rank is not a physical occurrence or charge. The sole high branch remains
`(37,0,23,-1)`. Gate A and Gate B remain globally open; global nontrivial-cycle
exclusion remains open. Do not turn abstract compatibility of a prefix shape into
physical realization.
