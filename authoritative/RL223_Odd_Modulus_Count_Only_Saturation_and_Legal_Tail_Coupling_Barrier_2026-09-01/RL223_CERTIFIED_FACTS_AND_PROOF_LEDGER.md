# RL223 certified facts and proof ledger

Date: 2026-09-01.

## Inherited frozen state

All RL222 and earlier certified claims, corrections, demotions, scope locks, and
verification-economy rules remain binding.

- necessary terminal-rank frontier: **13,415,865,871**;
- e=16 phase-51 family: **139,581,280** arithmetic candidates across
  **45,045** prefixes;
- e=16 terminal rank **34,124,151,203** remains live;
- phase-51 live cylinders: **3,132,617**, maximum precision 25 bits;
- state011 **90,749,885**; state111 **48,831,395**;
- all **469** reachable eta classes modulo 2187 remain represented;
- physical H21 incidence/charge is not proved;
- Gate A, Gate B, branch contradiction, and global nontrivial-cycle exclusion
  remain open.

The RL222 denominator and return-defect locks remain:

`D=2^A-3^L>0`,

`D mod 2^76=67904378415918967567359>31285589992934194300574>=y0`,

and for any physical realization `Qfull=D*y0<D^2`.  Ownership-derived
`Qfull mod D^2` is therefore the already-known root coordinate.  After phase16,

`N=A-24`, `M=L-16`,

`T(c)=2^N y0-3^M y16`,

and a physical return requires an independently generated legal-tail numerator
`Qtail=T(c)`.  Leading-prefix comparisons modulo powers of two are automatic.

## RL223-T1 — exact count-only recurrence and ordinary legality

**Classification: proved affine/parity algebra.**

For ordinary length-`N`, weight-`M` binary parity words, the numerator residue
set `S_(N,M)(q)` is exactly characterized by either recurrence recorded in
`RL223_ODD_MODULUS_COUNT_ONLY_SATURATION_THEOREM.md`.  Every binary word is
realized by infinitely many positive starts in one residue class modulo `2^N`.
This ordinary legality varies the start and does not imply continuation from a
fixed current `y16`.

## RL223-T2 — Euler-block count-only saturation

**Classification: proved analytic theorem.**

If `gcd(q,6)=1`, `H=phi(q)`, and `min(M,N-M)>=qH`, then

`S_(N,M)(q)=Z/qZ`.

For the frozen RL223 dimensions this holds, without factoring individual
moduli, for every `2<=q<=283635` coprime to 6.  There are exactly **94,544**
such admissible moduli in this range.  The proof uses `q` switchable Euler blocks of equal length and weight whose switches all add one common unit
modulo `q`.

This is precisely a theorem-quality blindness result under RL223 success
criterion 4: an odd-modulus automaton retaining only remaining length, remaining
odd count, and numerator residue cannot be a candidate selector in this range.

## RL223-T3 — fixed-prefix saturation and endpoint equivalence

**Classification: proved algebraic corollary with an exact phase-51-prefix type guard.**

Any fixed finite prefix retains count-only saturation if the remaining one and
zero capacities meet the same Euler-block bound.  The exact inherited common
witness prefix through phase51 was replayed, and a formal exact-count completion
modulo 5 meets its return target.  The selectable suffix is explicitly not
claimed to be the actual continuation of the exact phase-51 endpoint.

For a genuinely legal tail,

`Qtail=T(c) (mod q)` if and only if `y_end=y0 (mod q)`.

The missing datum is therefore a certified candidate-to-legal-tail
language/automaton coupling that determines attainable endpoint residues for the
actual continuation constraints.

## RL223-T4 — target affine-lift slope

**Classification: proved exact affine algebra.**

On every inherited `k`-lift,

`T(k+1)-T(k)=3*2^34*D`.

Modulo `q`, the target image on complete `k` residue classes has exactly
`q/gcd(D,q)` residues.  This does not overcome the full count-only word-side
image.

## RL223-C1 — bounded exact residue certificate

**Classification: exact finite certificate at explicitly limited scope.**

The independent forward DP exhausts every eligible modulus `5<=q<=1023`:

- **340 / 340** eligible moduli checked gap-free;
- **340 / 340** saturated for unconstrained fixed-count words;
- largest minimal saturating prefix length: **16**;
- the inherited witness target intersects the relaxed word-side set for all
  **340** moduli.

Original scratch-certificate SHA256:
`0d795e2809dd46180e7c42077f03090c0938dcd2645a218d384d31cb54a52990`.

The frozen copy changes only its two promotion-status labels to the exact scope
`PROMOTED_BY_RL223_AT_UNCONSTRAINED_COUNT_ONLY_SCOPE`; its SHA256 is
`778e725b169250181b78b0ea35f7318679d475a22b9d1d86505d59d5add25161`.
No legal-H21 claim is promoted.

## Consequence and open obligation

RL223 deletes **0 candidates, 0 prefixes, 0 ranks, 0 states, and 0 eta classes**.
The necessary frontier remains **13,415,865,871** and both global Gates remain
open.

The unique successor obligation is to couple an endpoint modulus to the actual
candidate-specific legal tail.  A state system containing only counts and
`Q mod q` is already certified structurally blind in the stated range.
