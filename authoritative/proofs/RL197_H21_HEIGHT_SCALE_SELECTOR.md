# RL197 proof note — H21 height-scale selector

For terminal rank `r in [23369453298,41775866136]`, exact modular arithmetic gives the
offset-rank intervals

`k=36: [15303429870,33709842708]`,
`k=35: [95752179175,114158592013]`,
`k=34: [38672883168,57079296006]`,
`k=33: [119121632473,137528045311]`.

Relative to `R=57079296007` the digits are `1,2,1,2`. The seam ranks `R-1,L-1`
at the last two sources occur only for terminal `r=41775866136`, an inherited deletion.

For binary common heights `(x,y,z)` at `tau=35,34,33`, positive exponents are
`d0=2+x-y` and `d1=1+y-z`. The first is always positive; the second is positive iff `z<=y`.
Therefore the exact survivors are `000,010,011,100,110,111`.

The middle source and target are duplicated under p-shift because their p-defects are zero.
The two chronological edges are both zero-zero iff `y=z=0`, which among the survivors is
exactly `000,100`, equivalently `y=0`.

Finally
`Delta35=7*2^35`,
`Delta34=(3/4)Delta35=21*2^33`,
`Delta33=(3/2)Delta34=63*2^32`.
For common height `e`, `C=2^e Delta`; raising the height by one doubles C, preserves Delta,
and preserves whether `3|C`. Hence the inherited normalized-gap and mod-3 predecessor data
cannot choose the middle height.
