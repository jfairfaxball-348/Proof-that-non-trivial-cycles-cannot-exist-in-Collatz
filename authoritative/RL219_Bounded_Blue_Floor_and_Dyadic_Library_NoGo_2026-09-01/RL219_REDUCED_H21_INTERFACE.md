# RL219 reduced H21 interface for RL220

Date: 2026-09-01.

## Global necessary state

- necessary terminal ranks: **13,415,865,871**
- above p: **7,091,831,284**
- below p: **6,324,034,587**
- Gate A: open globally
- Gate B: open globally
- global nontrivial-cycle exclusion: open

## Current e=16 arithmetic family

Unchanged from RL218:

- **45,045** live prefixes;
- **139,581,280** phase-51 arithmetic candidates;
- root progression `y(k)=y_*+3*2^58 k` on inherited exact finite windows with terminal-Hensel exclusions;
- **3,132,617** disjoint phase-51 2-adic survivor cylinders, max precision **25 bits**;
- state011 **90,749,885**, state111 **48,831,395**;
- mod18 `0:35,622,831`, `8:19,167,422`, `9:55,127,054`, `17:29,663,973`;
- all **469** reachable eta classes mod2187 survive;
- terminal rank **34,124,151,203** remains live.

Exact root band:

`R_MIN=24,913,843,845,551,577,787,381`,
`R_MAX=31,285,589,992,934,194,300,574`,
with `R_MAX<2 R_MIN`.

## RL218 recognition algebra retained

For a legal odd-only word,

`2^E s = 3^h y + Q_h`.

After `y=y_*+3*2^58 k`, the numerator is affine in k and high valuations give exact dyadic k classes. A fixed certified seed + fixed word gives at most one k.

## New RL219 physical floor

The exact pre-phase-51 superset already has

`y_16 >= 63,923,554,738,764,449,832,959`.

For any physical H21 realization, nonnegative height plus the inherited `0<ln(lambda)<2^-40` implies every shortcut state in a full L-odd-step period is strictly above

`B_H21=7,990,444,342,345,556,229,119`.

The stable externally verified Collatz interval `[1,2^71]` is strictly below this physical floor. This is a physical-state barrier, not a blanket phase-51 candidate deletion.

## New RL219 finite-library dyadic barrier

For one fixed seed s, fixed raw backward word w, and dyadic seed parameter t,

`Y_t=(2^(n+t)s-C_w)/3^h`,
`Y_(t+1)>=2Y_t`.

Because the entire current root band has multiplicative width <2, each fixed `(s,w)` pair contributes at most one endpoint value to the root band. Hence a finite set of seeds and finite library of fixed words, even with unbounded dyadic rays, remains only a finite singleton-probe architecture after affine pullback.

## Closed / nonproductive sources now on record

Do not repeat as open routes:

- RL80 LTE explicit comb versus the modern prefixes: zero intersections;
- seed-1 reverse tree through depth 86: zero matches;
- fixed seed + fixed word: singleton pullback;
- finite fixed-word library + finite seeds + arbitrary dyadic seed scaling: still finite singleton endpoint probes in the current root band;
- bounded verified interval as a physical endpoint set below `B_H21` without an exact candidate equality bridge.

## What RL220 must add

A useful next blue theorem must be **unbounded and non-dyadic in its essential parameterization**. Strong forms include:

- an independently proved arithmetic progression / finite union of progressions of blue integers extending above the current root band;
- a parameterized backward family whose non-dyadic word shape changes coherently and whose endpoint formula has additive/affine structure compatible with `y_*+3*2^58 k`;
- an exact theorem converting a family parameter directly into a non-singleton k congruence/class;
- or a proof that every such currently natural family reduces to sparse exponential/S-unit equality probes.

No large candidate enumeration should replace the missing compression theorem.
