# RL221 reduced H21 interface

Date: 2026-09-01. Compact successor interface for RL222.

## Frozen constants and live family

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`, `z=72057431991`,
`K0=2^37`, `Ap-uL=1`.

Necessary terminal frontier: **13,415,865,871**.
The e=16 terminal rank **34,124,151,203** remains live.

The exact RL217 phase-51 arithmetic family remains:

- **139,581,280** candidates;
- **45,045** prefixes;
- **3,132,617** disjoint phase-51 2-adic cylinders, max precision **25 bits**;
- state011 **90,749,885**, state111 **48,831,395**;
- mod18 `0:35,622,831`, `8:19,167,422`, `9:55,127,054`, `17:29,663,973`;
- all **469** reachable eta classes modulo2187.

For each live prefix:

`eta = eta_* + 3^17 k`,
`y0 = y0_* + 3*2^58 k`

inside its exact finite two-sided k-window and terminal-Hensel exclusions.

At phase16:

`y16 = 2^34 eta - 1 - 3^16*2^13`, `h16=1`.

The root band is exactly bounded by

`24,913,843,845,551,577,787,381
 <= y0 <=
31,285,589,992,934,194,300,574`.

## RL221 exact consistency witness

One certified live tuple is:

`Q16=43079489`,
`eta_*=94527378`,
`y0_*=632932199441596415`,
`k=28821` in `[28812,36180]`,
`eta=3722043165201`,
`y0=24921895945404894117887`.

It has state011, `eta=9 mod18`, `eta=864 mod2187`,
terminal `nu=v2(3^34 eta-1)=3`,
`v2(3y0+1)=1`, and all mechanical heights through phase51 are nonnegative.

Therefore the inherited prefix/state + root-window + terminal-Hensel + phase51-height + first-root-v2 constraints have nonempty intersection.

## Type lock

RL219/RL220 blue-family and pump no-go results are not extra candidate predicates unless a new theorem proves every physical candidate belongs to the corresponding construction family.  Do not count route barriers as candidate deletions.

## RL222 live target datum

Let `D=2^A-3^L` and `Qfull(d)` be the phase-aligned complete-word numerator:

`y0 = Qfull(d)/D`.

`Qfull(d)=0 modD` alone does not determine the quotient residue.
The live missing discriminator is

`(Qfull(d)/D) modD`,

equivalently `Qfull(d) modD^2`, or an equally strong independent full-period p/z-arc return numerator congruence.

Because `gcd(3*2^58,D)=1`, any such root residue is an exact congruence on k and can be intersected with the finite RL217 windows/cylinders.

No physical H21 incidence/charge, branch contradiction, Gate closure, or global nontrivial-cycle exclusion is proved.
