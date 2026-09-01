# RL223 reduced H21 interface

Date: 2026-09-01. Compact successor interface for RL224.

## Frozen constants and live family

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`, `z=72057431991`,
`K0=2^37`, `Ap-uL=1`.

Necessary terminal frontier: **13,415,865,871**.
The e=16 terminal rank **34,124,151,203** remains live.

Exact RL217/RL221 phase-51 family:

- **139,581,280** arithmetic candidates;
- **45,045** prefixes;
- **3,132,617** phase-51 2-adic cylinders, max precision 25 bits;
- state011 **90,749,885**; state111 **48,831,395**;
- all **469** reachable eta classes modulo 2187.

For each live prefix,

`eta=eta_*+3^17 k`,

`y0=y0_*+3*2^58 k`

inside the inherited finite `k`-window and terminal-Hensel/phase51 filters.
At phase16,

`y16=2^34 eta-1-3^16*2^13`,

`2^24 y16=3^16 y0+Q16`.

Root band:

`24913843845551577787381 <= y0 <= 31285589992934194300574`.

## Denominator and return-defect locks

With `D=2^A-3^L>0`,

`D mod 2^76=67904378415918967567359`,

so `D>y0` on the entire current family.  For a physical realization,
ownership-derived `Qfull mod D^2=D*y0` contains no independent digit.

After phase16 set

`N=A-24=217976794593`,

`M=L-16=137528045296`,

`N-M=80448749297`,

`T(c)=2^N y0-3^M y16`.

A legal remaining word closes the full return exactly when its independently
generated numerator satisfies `Qtail=T(c)`.  Leading-prefix comparisons modulo
powers of two are automatic and must not be used as selectors.

## RL223 odd-modulus lock

For ordinary length-`N`, weight-`M` binary words and every
`2<=q<=283635` with `gcd(q,6)=1`,

`{Qtail mod q}=Z/qZ`.

This remains true after any fixed finite prefix whose residual one/zero
capacities satisfy the Euler-block bound.  An exact DP independently checks all
340 eligible moduli from 5 through 1023.

For a legal tail ending at `y_end`,

`Qtail=T(c) (mod q)` iff `y_end=y0 (mod q)`.

On each inherited `k`-lift,

`T(k+1)-T(k)=3*2^34*D`.

The count-only theorem is a relaxation blindness lock.  It does not determine
the actual endpoint residue of the fixed exact candidate.

## Required successor state

Any successor endpoint automaton must preserve an independently certified
candidate-to-tail continuation relation.  Retaining only remaining length,
remaining odd count, and `Q mod q` is insufficient in the proved range.

No candidate, prefix, state, eta class, rank, physical H21 incidence/charge,
Gate, branch contradiction, or global exclusion is added by RL223.

Knowledge catalogues remain stale/deferred.
