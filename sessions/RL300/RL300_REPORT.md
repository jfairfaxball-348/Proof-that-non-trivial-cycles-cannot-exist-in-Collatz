# RL300 — external delay-record bridge and exact resonance frontier report

Date: 2026-09-11
Base authority: `d1564092e4f43fb2ab2347398455ccb7c4f1a211`
Base tree: `4758d988ce85327975d68a724bc17ee86d86c851`

## Classification

`EXTERNAL_DELAY_RECORD_CERTIFICATE_PLUS_EXACT_RESONANCE_FRONTIER_TO_A206745572560704146_WITH_DIRECT_START_BOUNDARY`

This promotion uses a **provenance-backed external finite computational certificate** for an ordinary-Collatz delay interval. The resonance arithmetic, conversion to the half-Collatz consumer, and frontier calculation are exact and independently replayable in-repository.

Gate A remains open. Gate B remains open. RL297 P-bottleneck work remains parked weak-green background. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed. The Lean project is separate.

## 1. Incoming state

RL300 inherited from RL299:

- every retained selector through `a=630138896` eliminated by internally frozen exact/finite certificates;
- first unresolved resonance `U5=(630138897,397573379)`;
- relaxed quotient ceiling
  `Nhat=floor((79/9)/(exp(Delta)-1))+2`, where `Delta=a ln2-ell ln3>0`;
- new worst quotient envelopes occur only at one-sided continued-fraction record pairs;
- physical starts for `N=19+24h` are
  `A0=27h+22`, `B0=81h+80`;
- if a half-Collatz trajectory reaches 1 after `O` odd and `E` even half-steps, with `J=O-E`, then
  `2W(m)<=m+J+1`;
- therefore the exact sufficient obstruction is
  `2rho-m >= J+2`;
- for the selector/full-phase geometry,
  `2rho-mmax = 2ell-a+26`.

No RL299 theorem is demoted.

## 2. Frozen external finite-delay certificate

RL300 freezes the exact external provenance in
`RL300_EXTERNAL_DELAY_CERTIFICATE.md`.

The relevant source sequence is OEIS A006877, whose definition is that its starting values set new records for the number of ordinary `3x+1` steps to reach 1; OEIS explicitly states that both the `3x+1` step and halving steps are counted. Its linked b-file is sourced from Eric Roosendaal's delay-record table.

The two consecutive source values used here are

- `R = 3571472436310255273`;
- `Rnext = 4761963248413673697`.

Roosendaal's delay-record definition is the strict record property:
a confirmed delay record `N` has larger delay than every positive `M<N`.

The portable RL300 verifier independently replays

- `D(R)=2334`;
- `D(Rnext)=2337`.

Therefore the external record-table completeness assertion yields the finite quantitative certificate

`for every positive n < 4761963248413673697, D(n) <= 2334`.

This is an external finite computational dependency. RL300 does **not** claim to have independently rerun the exhaustive search over that entire interval.

## 3. Conversion to the physical J bound

For the ordinary Collatz map, an odd step `n -> 3n+1` is necessarily followed by a halving step before it reaches the RL299 half-Collatz state `(3n+1)/2`.

Thus every odd half-Collatz step compresses two ordinary steps, while every even half-step is one ordinary halving step. Hence for any start in the certified interval,

`half_stopping_time <= ordinary_delay <= 2334`.

Since `J=O-E <= O+E = half_stopping_time`,

`boxed: J <= 2334`

for every relevant physical start below `Rnext`.

Combining with the inherited RL299 weight lemma, it is sufficient that

`2ell-a+26 >= 2336`.

## 4. Exact resonance extension

The exact rational logarithm verifier extends the certified common continued-fraction prefix for `log_2(3)` to

`[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8,1,11,1,20]`.

Enumerating the corresponding upper convergents/intermediate convergents and comparing the positive linear forms with exact rational bounds gives exactly 51 one-sided record pairs from `U5` through the first direct-start boundary.

The complete machine-readable list, exact `Nhat`, and exact physical maxima are frozen in
`RL300_RESONANCE_RECORD_CERTIFICATE.txt`.

The final safe controlling record is

`(a,ell)=(196864044717151823,124207383220472977)`,

with

`Nhat=1250146787826445598`.

For all `N=19+24h <= Nhat`, the largest B-family start is

`Bmax=4219245408914253845`,

and

`4219245408914253845 < 4761963248413673697`.

Therefore every physical A/B start in every record block from `U5` through the block controlled by this record lies inside the external `D<=2334` certificate.

## 5. Selector margin

The inherited selector floor is

`ell >= ceil(147a/233)`.

Therefore

`2ell-a+26 >= 61a/233 + 26`.

For every `a>=630138897`, this lower bound is already greater than `164972011`, hence enormously exceeds the required `2336`.

Thus every retained selector in the externally certified record blocks is eliminated.

The promoted external-certificate frontier is

`boxed: every retained selector through a=206745572560704146 is eliminated.`

This statement carries the external finite-delay certificate dependency described above.

## 6. Exact direct-start boundary

The next one-sided resonance record is

`(206745572560704147,130441933147714940)`.

Its exact relaxed ceiling is

`Nhat=4894841535700125438`,

and the resulting B-family maximum is

`Bmax=16520090182987923332`.

This exceeds the frozen external threshold `4761963248413673697`.

Therefore the **direct physical-start use of this one delay-record interval** stops exactly before this record. This is a method boundary, not a counterexample and not evidence that the selector survives.

The inherited RL299 B-family ancestry theorem remains available to RL301, but RL300 performed no post-lock extension using it.

## 7. Proof-state distinctions

Promoted internal exact mathematics / computation:

- 34-term certified continued-fraction prefix;
- exact enumeration of the 51 upper resonance records from U5 to the direct-start boundary;
- exact `Nhat` values and A/B physical maxima;
- independent ordinary-delay replay of the two load-bearing external record values;
- exact consumer conversion `D -> half stopping -> J`;
- exact selector-margin comparison.

Promoted external finite computational dependency:

- the completeness of the consecutive delay-record pair, implying
  `D(n)<=2334` for all positive `n<Rnext`.

Not promoted:

- any claim that RL300 independently exhaustively verified all `n<Rnext`;
- any use of later delay-record values;
- any extension past `a=206745572560704146`;
- any global Collatz stopping theorem;
- Gate A, Gate B, or global non-trivial-cycle exclusion.

## 8. Strategic consequence

The selector/physical route has moved from an internally self-contained frontier of `630138896` to a promoted external-certificate frontier above `2.067e17` without bulk trajectory enumeration.

The first direct-start boundary is now explicit rather than a vague scaling wall. RL301 should first test whether the inherited B-family ancestry or a similarly compact consumer bridge lets the same/adjacent finite delay certificate cross that boundary. If this again yields only a finite ladder, compare its cost against the parked RL297 Bellman/P shared-endpoint route.
