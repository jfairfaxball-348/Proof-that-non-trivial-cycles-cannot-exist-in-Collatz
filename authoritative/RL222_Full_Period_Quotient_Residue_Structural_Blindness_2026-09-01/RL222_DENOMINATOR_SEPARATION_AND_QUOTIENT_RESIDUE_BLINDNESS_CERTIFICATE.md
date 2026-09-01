# RL222 denominator separation and quotient-residue structural-blindness certificate

Date: 2026-09-01.

Classification: **proved elementary/algebraic mathematics plus exact finite arithmetic support**.

## 1. Data

`A=217976794617`, `L=137528045312`, `D=2^A-3^L`.

Inherited from the corrected H21 interface:

`0 < ln(2^A/3^L)`,

so `D>0`.

Inherited exact root band after RL215:

`24913843845551577787381 <= y0 <= 31285589992934194300574`.

## 2. Exact modular lower bound for D

Use `M=2^76=75557863725914323419136`.  Exact modular exponentiation gives

`3^L mod M = 7653485309995355851777`.

Since `A>76`, `2^A=0 mod M`, hence

`D mod M = -3^L mod M = 67904378415918967567359`.

This residue lies in `(0,M)`.  Every positive integer congruent to it modulo `M` is
`67904378415918967567359 + tM` with `t>=0`.  Therefore

`D >= 67904378415918967567359`.

The exact gap over the current root cap is

`67904378415918967567359 - 31285589992934194300574 = 36618788422984773266785 > 0`.

Hence every live candidate root obeys `0<y0<D`.

This proof never approximates `2^A` or `3^L`.

## 3. What happens to Qfull modulo D^2

At the physical full-word scope RL214 proved

`Qfull(d)=D*y0`.

For any physical realization of a current live candidate,

`0 < D*y0 < D^2`.

Therefore the canonical residue modulo `D^2` is the integer itself:

`[Qfull(d)]_(D^2) = D*y0`.

Dividing the exact multiple by `D` gives

`[Qfull(d)/D]_D = y0`

because `0<y0<D`.

So the proposed `D^2` ownership residue contains zero extra `D`-adic information on this already bounded root family.  A candidate-wise intersection against that derived residue is the identity map on the existing candidate set.

## 4. The genuinely missing return datum

At phase 16,

`2^24 y16 = 3^16 y0 + Q16`.

For a remaining tail of length `N=A-24` and odd count `M=L-16`, define its independently generated affine numerator `Qtail(w)` by

`2^N y_end = 3^M y16 + Qtail(w)`.

The physical full return condition `y_end=y0` is therefore exactly

`Qtail(w) = 2^N y0 - 3^M y16 = T(c)`.

This equality is candidate-wise: `T(c)` is fixed by the existing tuple while `Qtail(w)` must be generated independently by a legal continuation.

A mere leading-prefix test modulo a power of two is insufficient.  If `m<=N` prefix bits contain `r` odd steps and have numerator `q_m`, then

`q_m = -3^r y16 (mod 2^m)`

and every completion has

`Qtail(w) = -3^M y16 (mod 2^m)`.

But `T(c)` has the same residue automatically because `2^N y0=0 mod 2^m`.
Thus the next attack must add a nonlocal endpoint/full-tail observable; an odd modulus coprime to 6 is a natural first exact test because it is not swallowed by the local binary denominator.

## 5. Explicit witness replay

For the RL221 witness,

`Q16=43079489`,
`k=28821`,
`eta=3722043165201`,
`y0=24921895945404894117887`,
`y16=63944214675001842327551`.

The verifier checks

`eta = 94527378 + 3^17*k`,
`y0 = 632932199441596415 + 3*2^58*k`,
and
`2^24*y16 = 3^16*y0 + Q16`.

The witness remains a live arithmetic necessary candidate, not a proved physical cycle.
