# RL189 — N35 crossover early-defect charging and boundary consumer

Date: 2026-08-30

## 0. Outcome and classification

RL189 continues the sole surviving high branch `(v,H,J,d)=(37,0,23,-1)` from RL188.

It does **not** eliminate the isolated `{35,36,37}` triple, close the high branch, close the preferred branch, close Gate A or Gate B, exclude all non-trivial cycles, or prove Collatz.

RL189 proves two new exact results:

1. **RL189.1 — extremal triple-terminal spacing improves from 41 to 43.**
   Separation 41 is excluded by four exact post-terminal common-mechanical transitions supplied by the co-owned `tau=35` clean corridor; separation 42 is excluded by the terminal-rank core.
2. **RL189.2 — the strengthened `N_35` crossover cannot improve the inherited RL187 corrected-flow floor inside the natural two-level `tau<=34` / `tau=35` reweighting class.**
   The binding height-21 co-ownership family `{33,34,35}` forces the optimum back to the old flat `tau<=35` weight.

Consequently the clean-start survival cap sharpens to

`N_35 <= floor(3L/43) = 9594979905`,

so at least

`480194594`

clean starts have first nonzero defect at offset `tau<=34`.

The ordinary absolute corrected-flow bound remains the inherited RL187 value

`> 2787212689/6291456 > 443`.

No correction or demotion of inherited mathematics is required.

## 1. Frozen inherited state

Use

`A=217976794617`,
`L=137528045312`,
`B=A-L=80448749305`,
`R=L-B=57079296007`,
`CLEAN=10075174499`.

Retain RL188:

- every extremal `{35,36,37}` terminal has necessary mechanical rank
  `r in E=[72797034370,103818202602]`;
- the exact terminal normalized gap is `delta_t=3^37/2^21`;
- every `tau=37` triple-start normalized gap is exactly `2^37` or `2^38`;
- consecutive triple terminals are separated by at least 41 phases;
- an extremal triple block has exact span 38;
- every nontriple block contributing to `N_35` has density at most `2/37`;
- the clean family supplies a physical 40-edge corridor for each counted shallow start.

Retain RL183's common-mechanical ordinary transition law

`2^c delta' = 3 delta + epsilon`, with `|epsilon|<1`,

and the mechanical bit rule `c=1` for residue `<R`, `c=2` otherwise.

Retain RL187's safe charging schedule

- `w_short=1/(3*2^22)` for `tau<=35`,
- `w_36=1/(3*2^23)` for `tau=36`,
- `w_long=1/2^25` for `tau>=37`,

together with `N_36<=7238318174`, `N_37<=7052720272` and ordinary absolute corrected-flow `>2787212689/6291456>443`.

## 2. RL189.1 — separation 41 is impossible

Let the first triple terminal occur at phase `t` with mechanical residue `r in E`.

A second triple terminal 41 phases later requires

`r in E` and `(r+41B) mod L in E`.

Exactly,

`41B mod L = 135253679329 = L-2274365983`,

and the simultaneous rank overlap is

`75071400353 <= r <= 103818202602`.

The extremal terminal is co-owned by the clean `tau=35` start at phase `t-35`. Its inherited 40-edge clean corridor therefore contains at least the four post-terminal transitions

`t -> t+1 -> t+2 -> t+3 -> t+4`.

No `tau<=34` extension is used here.

Across the exact overlap above, the four mechanical bits `(c_t,c_(t+1),c_(t+2),c_(t+3))` have only two possibilities:

- `75071400353 <= r <= 90789138715`: word `2121`;
- `90789138716 <= r <= 103818202602`: word `2122`.

Iterating the affine law for four transitions gives the following centers and strict error radii.

### Word `2121`

`delta_(t+4)` lies strictly within `119/64` of

`3^41/2^27`.

If a second triple terminal occurred at `t+41`, its `tau=37` start would be exactly `t+4`, hence its gap would be `2^37` or `2^38`.

The nearest permitted target is `2^38`, and

`|3^41/2^27 - 2^38|
 = (2^65-3^41)/2^27
 = 420491770248316829/134217728
 > 119/64`.

Contradiction.

### Word `2122`

`delta_(t+4)` lies strictly within `119/128` of

`3^41/2^28`.

The nearest permitted target is `2^37`, and

`|2^37 - 3^41/2^28|
 = (2^65-3^41)/2^28
 = 420491770248316829/268435456
 > 119/128`.

Contradiction.

Thus separation 41 is impossible.

## 3. Separation 42 is rank-forbidden

Exactly,

`42B mod L = 78174383322`.

The cyclic distance of this displacement from zero is

`min(78174383322,59353661990)=59353661990`,

which exceeds the diameter

`diam(E)=31021168232`.

Equivalently, the exact overlap

`E intersect (E-42B mod L)`

is empty.

Together with RL188's spacing-at-least-41 theorem and the exclusion of 41 above:

**consecutive extremal triple terminals are separated by at least 43 chronological phases.**

## 4. Strengthened `N_35` density and crossover

Group every extremal triple block with the following nontriple blocks up to the next extremal triple, as in RL188.

A triple owns three `N_35` starts and has exact span 38.

If the intervening span is `S`:

- with no intervening `N_35` start, spacing at least 43 gives `S>=5`, hence group density at most `3/(38+S)<=3/43`;
- with at least one intervening `N_35` start, inherited nontriple capacity gives `S>=36` and `K<=2S/37`, so

`(3+K)/(38+S)
 <= (3+2S/37)/(38+S)
 <= 3/43`.

The last inequality is equivalent to

`25S-555 >= 0`,

true for `S>=36`.

Therefore

`N_35/L <= 3/43`

and hence

`N_35 <= floor(3L/43)=9594979905`.

Since `CLEAN=10075174499`,

`CLEAN-N_35 >= 480194594`.

So at least **480,194,594** clean starts have `tau<=34`.

This is a much stronger distribution theorem than RL188's `12,146,794` lower bound, but it is still not by itself a branch contradiction.

## 5. RL189.2 — exact two-level charging obstruction

The natural consumer is to split the old short weight into

- `x` for `tau<=34`,
- `y` for `tau=35`,

while retaining RL187's later weights. A safe offset-sensitive strengthening must preserve monotonicity `x>=y`.

The inherited exact height-21 co-ownership family `{33,34,35}` has physical charge budget `2^-22`. Therefore every such schedule must obey

`2x+y <= 2^-22`.

Let `U=2^-25`. Then the budget is

`2x+y <= 8U`.

For the guaranteed lower-bound calculation use the strengthened caps

`N_35<=9594979905`,
`N_36<=7238318174`.

The guaranteed populations at the cap boundary are

`a=CLEAN-N_35=480194594` for `tau<=34`,

`b=N_35-N_36=2356661731` for `tau=35`.

At saturation of the binding height-21 budget,

`x=(8U-y)/2`.

The `x,y` part of the guaranteed charge is

`a x + b y`,

whose slope in `y` is

`b-a/2 = 2116564434 > 0`.

Thus the lower bound is maximized by taking `y` as large as permitted. Monotonicity `x>=y`, together with `2x+y<=8U`, forces

`y <= 8U/3`.

The maximum therefore occurs at

`x=y=8U/3 = 1/(3*2^22)`,

which is exactly the inherited RL187 flat short weight.

Because that flat schedule is already certified feasible against every other height/co-ownership family, no schedule in this two-level monotone split class can improve the RL187 ordinary corrected-flow floor.

This is an exact obstruction, not a statement that **all** possible offset-sensitive consumers fail. Any genuine gain must use information that breaks this aggregate height-21 bottleneck, for example phase/sign localization, a finer terminal-height split, or a stronger physical co-ownership exclusion.

## 6. What was not promoted

RL189 does not promote:

- physical realization of every rank in `E`;
- impossibility of an isolated `{35,36,37}` triple;
- a corrected-flow floor larger than RL187's `>443`;
- a chronological K excursion from total variation alone;
- a Gate A/B or global Collatz closure.

The rigorous spacing-41 argument uses the existing clean `tau=35` corridor. No `tau=34` companion corridor is assumed.

## 7. Exact verification

`verification/verify_rl189_phase41_42_and_n35_charging.py` certifies:

- the exact separation-41 terminal-rank overlap;
- the exact `2121` / `2122` four-bit partition;
- the four-step affine centers and error radii;
- exclusion of both permitted next triple-start gaps;
- empty separation-42 rank overlap;
- spacing `>=43`;
- density `<=3/43`, `N_35<=9594979905`, and `480194594` forced `tau<=34` starts;
- the height-21 two-level charging obstruction and recovery of the RL187 flat optimum.

## 8. Next authoritative target

RL190 should attack the **first unresolved spacing 43 seam** and the **phase-resolved charging bottleneck** together.

A separation-43 recurrence would place the next `tau=37` start at `t+6`; the co-owned `tau=35` 40-edge corridor reaches only through the available post-terminal boundary and no longer supplies the same closure automatically. This is the natural next seam to investigate.

In parallel, any charging improvement must break the aggregate `{33,34,35}` height-21 budget rather than merely split `tau<=34` from `tau=35`.
