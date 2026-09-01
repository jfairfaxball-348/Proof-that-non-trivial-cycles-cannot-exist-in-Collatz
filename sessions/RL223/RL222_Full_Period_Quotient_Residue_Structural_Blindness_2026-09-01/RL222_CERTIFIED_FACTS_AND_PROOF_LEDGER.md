# RL222 certified facts and proof ledger

Date: 2026-09-01.

## Inherited frozen state

All RL221 and earlier certified claims, corrections, demotions, scope locks, and verification-economy rules remain binding.

- necessary terminal-rank frontier: **13,415,865,871**;
- e=16 phase-51 family: **139,581,280** arithmetic candidates across **45,045** prefixes;
- e=16 terminal rank **34,124,151,203** remains live;
- state011 **90,749,885**; state111 **48,831,395**;
- all **469** reachable eta classes modulo 2187 remain represented;
- physical H21 incidence/charge is not proved;
- Gate A, Gate B, branch contradiction, and global nontrivial-cycle exclusion remain open.

## RL222-T1 — exact denominator separation

**Classification: proved elementary modular arithmetic, supported by exact finite arithmetic certificate.**

Let `D=2^A-3^L` with
`A=217976794617` and `L=137528045312`.  The inherited `0<ln(2^A/3^L)` gives `D>0`.

Modulo `2^76`,

`3^L = 7653485309995355851777 (mod 2^76)`

and, because `A>76`,

`D = 67904378415918967567359 (mod 2^76)`.

The least positive residue is already larger than the inherited exact root cap:

`67904378415918967567359 > 31285589992934194300574`.

Since `D>0`, it follows that `D >= 67904378415918967567359`.  Therefore every current live root candidate satisfies

`0 < y0 <= 31285589992934194300574 < D`.

The certified separation gap between the residue lower bound and the root cap is
**36618788422984773266785**.

## RL222-T2 — bounded-family quotient-residue collapse

**Classification: proved algebraic consequence at the physical-realization scope.**

RL214 proved the phase-aligned full-word bridge `Qfull(d)=D*y0` for a physical word.
For any physical realization of a current live candidate, RL222-T1 gives `0<y0<D`.
Hence

`0 < Qfull(d)=D*y0 < D^2`.

Consequently there is no wrap modulo `D^2`:

`Qfull(d) mod D^2 = Qfull(d) = D*y0`

and

`(Qfull(d)/D) mod D = y0`.

Thus an ownership-derived computation of the requested `Qfull mod D^2` digit is not a new candidate predicate on the current bounded family: it merely re-encodes the already exact root coordinate.  This is the RL222 structural-blindness outcome.  It does **not** forbid an independently computed word-side return observable from being informative.

## RL222-T3 — exact full-tail target and local 2-adic blindness

**Classification: proved exact recurrence/concatenation algebra.**

For an e=16 prefix,

`2^24 y16 = 3^16 y0 + Q16`.

Let the remaining full-word tail have binary length `N=A-24`, odd count `M=L-16`, and affine numerator `Qtail`.  A full return to `y0` is equivalent to

`Qtail = T(c) := 2^(A-24) y0 - 3^(L-16) y16`.

Equivalently,

`Qfull = 3^(L-16) Q16 + 2^24 Qtail = D*y0`.

This gives an exact candidate-wise target `T(c)`, because the current tuple fixes `y0`, `eta`, `y16`, and `Q16`.

However a prefix-only 2-adic test of this target is automatically satisfied.  For any first `m` tail bits with `r` odd steps and local numerator `q_m`,

`2^m x_m = 3^r x + q_m`.

Therefore `q_m = -3^r x (mod 2^m)`.  Any complete tail numerator has

`Qtail = 3^(M-r) q_m + 2^m Qrest`,

so

`Qtail = -3^M x (mod 2^m)`.

The target itself has
`T(c)=2^N y0-3^M x = -3^M x (mod 2^m)` for `m<=N`.
Thus extending only local 2-adic prefix precision and comparing `Qtail mod 2^m` to the return target cannot discriminate a full return.

## RL222-C1 — exact support replay

**Classification: exact finite arithmetic certificate.**

The portable verifier recomputes the `2^76` denominator residue and replays the RL221 common witness:
`Q16=43079489`, `k=28821`, `eta=3722043165201`, `y0=24921895945404894117887`.
It checks the affine lift identities, the inherited root band, and

`2^24*y16 = 3^16*y0 + Q16`.

## Consequence and open obligation

RL222 deletes **0 candidates, 0 prefixes, 0 ranks**.  No state or eta class is deleted.
The frontier remains **13,415,865,871** and both global Gates remain open.

The next candidate-wise datum must be computed independently from the legal remaining word/endpoint, not recovered from `Qfull=D*y0` and not reduced to an automatic local 2-adic prefix congruence.
