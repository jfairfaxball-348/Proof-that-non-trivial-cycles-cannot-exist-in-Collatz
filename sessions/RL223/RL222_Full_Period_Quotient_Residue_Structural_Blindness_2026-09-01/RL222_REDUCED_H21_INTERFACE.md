# RL222 reduced H21 interface

Date: 2026-09-01. Compact successor interface for RL223.

## Frozen constants and live family

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`, `z=72057431991`,
`K0=2^37`, `Ap-uL=1`.

Necessary terminal frontier: **13,415,865,871**.
The e=16 terminal rank **34,124,151,203** remains live.

Exact RL217/RL221 phase-51 family:

- **139,581,280** candidates;
- **45,045** prefixes;
- **3,132,617** phase-51 2-adic cylinders, max precision 25 bits;
- state011 **90,749,885**; state111 **48,831,395**;
- all **469** reachable eta classes modulo2187.

For each live prefix:

`eta = eta_* + 3^17 k`,
`y0 = y0_* + 3*2^58 k`

inside the inherited finite k-window and terminal-Hensel/phase51 filters.

At phase16:

`y16 = 2^34 eta - 1 - 3^16*2^13`,
`2^24 y16 = 3^16 y0 + Q16`.

Root band:

`24913843845551577787381 <= y0 <= 31285589992934194300574`.

## RL222 denominator lock

With `D=2^A-3^L>0`,

`D mod 2^76 = 67904378415918967567359`,

hence

`D >= 67904378415918967567359 > 31285589992934194300574 >= y0`.

Therefore, for any physical realization of a current candidate,

`Qfull mod D^2 = D*y0`
and
`(Qfull/D) mod D = y0`.

An ownership-derived `D^2` residue is not a new selector.

## Return-defect interface

After phase16 set

`N=A-24`, `M=L-16`,
`T(c)=2^N y0 - 3^M y16`.

A legal remaining word `w` closes the full return exactly when its independently
generated tail numerator satisfies

`Qtail(w)=T(c)`.

Do **not** use a leading-tail comparison modulo `2^m` as a selector: for every
locally generated prefix it is automatically equal to `T(c) mod 2^m`.

## Frozen scope

No candidate, prefix, state, eta class, terminal rank, physical H21 incidence/charge,
Gate, branch contradiction, or global exclusion is added by RL222.

Knowledge catalogues remain stale/deferred.
