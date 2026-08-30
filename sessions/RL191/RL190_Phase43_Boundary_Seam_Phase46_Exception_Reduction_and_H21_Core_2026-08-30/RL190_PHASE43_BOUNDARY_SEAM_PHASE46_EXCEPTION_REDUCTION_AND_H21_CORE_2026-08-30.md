# RL190 — phase-43 boundary seam, phase-46 exception reduction, and phase-resolved H21 core

Date: 2026-08-30

## 0. Outcome and classification

RL190 continues the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)` from RL189.

It does **not** eliminate the isolated `{35,36,37}` triple, close the high branch, close the preferred branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

RL190 proves four exact advances:

1. **RL190.1 — the first unresolved separation 43 is impossible.** The simultaneous terminal-rank overlap forces the six chronological mechanical bits `212122`. All six required pair transitions avoid the two common-mechanical exception sources, so RL183's physical affine transition law applies through the later triple's `tau=37` start at `t+6`. The resulting exact affine ball misses both permitted start gaps `2^37` and `2^38`.
2. **RL190.2 — extremal triple-terminal spacing strengthens to at least 46, and separation 46 reduces to two exact exceptional terminal ranks.** Separations 44 and 45 are rank-empty. At separation 46 every nonexceptional rank in the exact overlap is excluded by a nine-step affine mismatch; only `90789138715` and `101129528126` remain because one of the nine transitions hits a common-mechanical switch/carry exception there.
3. **RL190.3 — the global `N_35` density sharpens to `1/15`.** Consequently `N_35<=9168536354`, forcing at least `906638145` clean starts to have `tau<=34`.
4. **RL190.4 — the dangerous height-21 `{33,34,35}` charging family is phase-resolved.** Its common terminal invariant is `(T,H)=(350220815692997949,21)`. Full zero-prefix gap compatibility confines simultaneous co-ownership to the early mechanical terminal-rank core `[23369453298,41775866136]`, disjoint from the extremal triple core. Its `tau=35` starting numerator has odd part 7, so the predecessor defect is odd and nonzero; the dangerous block therefore has exact span 36.

The strengthened `N_35` crossover still does **not** improve the inherited ordinary absolute corrected-flow floor inside the same monotone two-level `tau<=34` / `tau=35` charging class. The height-21 `{33,34,35}` family remains the aggregate binder. Ordinary absolute corrected flow therefore remains the inherited

`>2787212689/6291456>443`.

No inherited mathematical claim requires correction or demotion.

## 1. Frozen inherited state

Use

`A=217976794617`,
`L=137528045312`,
`B=A-L=80448749305`,
`R=L-B=57079296007`,
`CLEAN=10075174499`.

Retain RL188/RL189:

- extremal `{35,36,37}` triple terminal necessary rank core
  `E=[72797034370,103818202602]`;
- terminal normalized gap
  `delta_t=3^37/2^21`;
- a `tau=37` triple-start normalized gap is exactly `2^37` or `2^38`;
- extremal triple block span is exactly 38;
- consecutive extremal triple terminals are separated by at least 43;
- nontriple blocks have `N_35` density at most `2/37`;
- `N_36<=7238318174` and `N_37<=7052720272`;
- ordinary absolute corrected-flow
  `>2787212689/6291456>443`.

Retain RL183's global ordinary/common-mechanical pair-gap law

`2^c delta' = 3 delta + epsilon`, with `|epsilon|<1`.

Here a p-pair transition is common-mechanical except when its source mechanical rank is exactly

- `R-1=57079296006` (ordinary mechanical-switch source), or
- `L-1=137528045311` (carry source).

This global law is the key boundary consumer in RL190: it is not restricted to the shallow corridor used by RL189.

Retain RL182's first ternary digit sensor

`3|C_i` iff `G_(i-1)` is even

for an ordinary physical p-edge, together with all necessary-versus-physical and corrected-flow scope locks.

## 2. RL190.1 — exact exclusion of separation 43

Let a first extremal triple terminal occur at chronological phase `t` with terminal mechanical rank `r in E`.

A second triple terminal at `t+43` requires

`r in E` and `(r+43B) mod L in E`.

Exactly,

`43B mod L = 21095087315`,

and the simultaneous overlap is

`72797034370 <= r <= 82723115287`.

The later terminal's `tau=37` start is at

`t+43-37=t+6`.

Thus six pair transitions, from `t` through `t+6`, are required.

Across the entire overlap the six chronological mechanical bits are constant:

`(c_t,...,c_(t+5)) = 212122`.

The source-rank intervals are exactly

- `t`: `[72797034370,82723115287]`;
- `t+1`: `[15717738363,25643819280]`;
- `t+2`: `[96166487668,106092568585]`;
- `t+3`: `[39087191661,49013272578]`;
- `t+4`: `[119535940966,129462021883]`;
- `t+5`: `[62456644959,72382725876]`.

None contains `R-1` or `L-1`. Therefore every one of the six p-pair transitions is ordinary/common-mechanical, and the global RL183 affine law applies. No `tau<=34` companion corridor and no unproved extension of the RL189 `tau=35` corridor is used.

Starting from

`delta_t=3^37/2^21`

and iterating the word `212122`, the homogeneous center at `t+6` is

`3^43/2^31`

and the strict accumulated error radius is

`1519/1024`.

If a second extremal triple terminal occurred at `t+43`, its `tau=37` start at `t+6` would have normalized gap exactly `2^37` or `2^38`.

For `2^37` the exact center distance is

`33109062215184251771 / 2147483648`,

and for `2^38` it is

`262038842964168574085 / 2147483648`.

Both are vastly larger than `1519/1024`. Contradiction.

Therefore separation 43 is impossible.

## 3. Separations 44 and 45 are rank-forbidden

Exactly,

`44B mod L=101543836620`

and

`45B mod L=44464540613`.

For each displacement the exact cyclic translate of `E` has empty intersection with `E`.

Together with the inherited spacing `>=43` and Section 2:

**consecutive extremal `{35,36,37}` triple terminals are separated by at least 46 chronological phases.**

## 4. RL190.2 — separation 46 reduces to two exceptional ranks

At separation 46,

`46B mod L=124913289918`

and the exact simultaneous terminal-rank overlap is

`85411789764 <= r <= 103818202602`.

The later `tau=37` start is at `t+9`, so nine p-pair transitions are required.

The only first-terminal ranks in this overlap for which one of those nine source ranks hits a common-mechanical exception are exactly

`r=90789138715`

and

`r=101129528126`.

More precisely:

- at `r=90789138715`, the source at offset 3 is the mechanical-switch source and the source at offset 4 is the carry source;
- at `r=101129528126`, the source at offset 8 is the mechanical-switch source.

Remove those two ranks. The remaining overlap splits into three exact common-mechanical intervals:

1. `[85411789764,90789138714]` with word `212122121`;
2. `[90789138716,101129528125]` with word `212212121`;
3. `[101129528127,103818202602]` with word `212212122`.

For each interval, exact affine propagation of `delta_t=3^37/2^21` through the nine bits produces a strict error ball disjoint from both permitted next triple-start gaps `2^37` and `2^38`.

Hence any hypothetical pair of extremal triple terminals exactly 46 phases apart must have the first terminal rank in the two-point set

`{90789138715,101129528126}`.

This is a finite exceptional seam reduction, **not** an exclusion of separation 46 and not a physical realization claim for either rank.

The missing datum is now explicit: one needs the exact physical transition law or an independent ownership/rank obstruction at the switch/carry exceptions themselves.

## 5. RL190.3 — exact `N_35` density `1/15`

Group each extremal triple block with the following nontriple blocks up to the next extremal triple, as in RL188/RL189.

An extremal triple block has exact span 38 and owns three `N_35` starts.

Let the following nontriple span be `S` and let it own `K` additional `N_35` starts.

If `K=0`, spacing at least 46 gives `S>=8`, so the group density is at most

`3/(38+S) <= 3/46 < 1/15`.

If `K>0`, inherited nontriple capacity gives

`S>=36`, `K<=floor(2S/37)`.

Write

`S=37q+r`, `0<=r<=36`.

Then

`floor(2S/37)=2q` for `r<=18`,
and
`floor(2S/37)=2q+1` for `r>=19`.

The desired bound

`(3+K)/(38+S) <= 1/15`

follows from

`15 floor(2S/37) <= S-7`.

For `r<=18` the difference is `7q+r-7`, nonnegative at the least admissible `q`; for `r>=19` it is `7q+r-22`, again nonnegative at the least admissible `q`. Equality is attained at

`S=37`, `K=2`,

where the density is

`5/75=1/15`.

Therefore the exact global ceiling is

`N_35/L <= 1/15`.

Since `L=137528045312`,

`N_35 <= floor(L/15)=9168536354`.

Thus at least

`CLEAN-N_35 >= 10075174499-9168536354 = 906638145`

clean starts have first nonzero defect at offset `tau<=34`.

This almost doubles RL189's forced early population.

## 6. The aggregate two-level charging plateau still binds

Let

- `x` be the charge for `tau<=34`;
- `y` be the charge for `tau=35`;

with the same monotone condition `x>=y` and the inherited later charges.

The dangerous height-21 family `{33,34,35}` still enforces

`2x+y <= 2^-22`.

At the new `N_35` cap,

`a=CLEAN-N_35=906638145`

is the guaranteed `tau<=34` population and

`b=N_35-N_36=1930218180`

is the cap-boundary `tau=35` population.

Along the saturated height-21 budget the objective slope in `y` is

`b-a/2 = 2953798215/2 >0`.

Therefore the guaranteed lower bound is still maximized by making `y` as large as monotonicity allows, which forces

`x=y=1/(3*2^22)`,

the inherited flat short charge.

So the stronger `N_35` theorem alone still does not improve the ordinary corrected-flow floor inside this two-level monotone class.

## 7. RL190.4 — phase-resolved dangerous H21 `{33,34,35}` core

The exact RL187 joint-terminal enumeration shows that the binding `{33,34,35}` family shares the unique terminal invariant

`T=350220815692997949`, `H=21`.

The relevant exact shallow starts are:

- `tau=33`: `h0=1`, `C0=541165879296=63*2^33`, raw terminal rank `[0,41775866136]`;
- `tau=34`: `h0=1`, `C0=360777252864=21*2^34`, raw terminal rank `[0,122224615441]`;
- `tau=35`: `h0=0`, `C0=240518168576=7*2^35`, raw terminal rank `[0,65145319434]`;
- `tau=35`: `h0=1`, `C0=481036337152=7*2^36`, with the same raw terminal-rank interval.

Now apply the RL188 full-prefix physical gap test separately to each offset: rotate backward from the terminal rank through the exact mechanical word, propagate the zero-defect normalized gap backward, and require every physical p-gap to remain strictly in

`(128081997553,293591818782)`.

The surviving necessary terminal-rank cores are:

- `tau=33`: `[23369453298,41775866136]`;
- `tau=34`: `[23369453298,59767970482]`;
- `tau=35`: `[23369453298,59767970482]`.

Therefore simultaneous `{33,34,35}` co-ownership is confined to the exact joint core

`D=[23369453298,41775866136]`.

This lies entirely below the mechanical threshold `R=57079296007` and is disjoint from the extremal `{35,36,37}` triple core `E`.

The `tau=35` starting numerator has odd part 7 and is not divisible by 3. By RL182's first-ternary-digit sensor, its immediately preceding defect is odd and nonzero. Thus the dangerous `{33,34,35}` block has exact span 36.

This phase resolution is genuine new structure, but it does not yet bound how many physical dangerous terminals occur in `D`, nor their corrected-flow sign. Consequently it is not sufficient by itself to relax the binding `2x+y` budget.

## 8. What is not promoted

RL190 does not promote:

- physical realization of any rank in `E` or `D`;
- exclusion of separation 46;
- exclusion of the isolated `{35,36,37}` triple;
- a corrected-flow floor larger than RL187's `>443`;
- a universal no-go theorem for phase/sign-sensitive charging;
- a chronological K excursion from total variation;
- branch, Gate A/B, non-trivial-cycle, or Collatz closure.

The two exact unresolved phase-46 ranks and the dangerous early H21 core are now the smallest live boundary objects.

## 9. Exact verification

`verification/verify_rl190_phase43_46_and_h21_core.py` certifies with integer/Fraction arithmetic:

- the separation-43 rank overlap and forced six-bit word;
- avoidance of both common-mechanical exception sources on all six transitions;
- the exact six-step affine center/radius and exclusion of both triple-start gaps;
- empty rank overlaps at separations 44 and 45;
- the separation-46 overlap, the exact two exceptional terminal ranks, the three safe word intervals, and affine exclusion of every nonexceptional rank;
- the exact `1/15` `N_35` group-density theorem, `N_35<=9168536354`, and `906638145` forced `tau<=34` starts;
- persistence of the monotone two-level charging plateau;
- reconstruction and full-prefix refinement of the dangerous H21 `{33,34,35}` family to `D=[23369453298,41775866136]`;
- its exact predecessor reset/span-36 consequence;
- preservation of the inherited `>443` ordinary corrected-flow floor.

## 10. Next authoritative target

RL191 should attack the now finite **phase-46 exceptional seam** first:

`r=90789138715` and `r=101129528126`.

Derive the exact switch/carry transition behavior at those ranks, or exclude them by an independent terminal-prefix, numerator, parity, or ownership constraint.

In parallel, use the phase-resolved dangerous H21 core

`D=[23369453298,41775866136]`

and exact block span 36 to seek a quantitative incidence/sign/spacing theorem strong enough to relax the binding `{33,34,35}` charge budget.

Do not replace either physical problem by arbitrary word enumeration or a necessary-rank existence claim.
