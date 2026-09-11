# RL301 — B-ancestry external class-record bridge and route-decision report

Date: 2026-09-11
Base authority: `056aaa4132ba5bccf11e3c8678f500e6ecfd7797`
Base tree: `342d852af648746aba850007fe0fbe42c213b7cc`

## Classification

`EXTERNAL_CLASS_RECORD_CERTIFICATE_PLUS_B_ANCESTRY_FRONTIER_TO_A7354673373747273032_WITH_FINITE_LADDER_BARRIER_AND_BELLMAN_P_RETURN`

Gate A remains open. Gate B remains open. Radius 6+ remains frozen. RO/divergent-orbit work remains out of scope. Lean formalisation is separate. No global Collatz stopping theorem and no global non-trivial-cycle exclusion is claimed.

## 1. Incoming state

RL301 inherited:

- internally self-contained selector frontier `a=630138896` from RL299;
- promoted external-delay selector frontier `a=206745572560704146` from RL300;
- the exact B-family ancestry for `N=19+24h`:
  `16h+15 -> 24h+23 -> 36h+35 -> 54h+53 -> 81h+80=B0`, four odd half-steps;
- the weight lemma: if a half-Collatz trajectory reaches 1 with imbalance `J=O-E`, then `2rho-m >= J+2` excludes weight `rho`;
- the sparse one-sided resonance-record reduction for the relaxed quotient ceiling.

## 2. Existing RL300 certificate crosses the first direct-start boundary

The first incoming unresolved resonance record was

`(206745572560704147,130441933147714940)`

with exact

`Nhat=4894841535700125438`.

For every admissible `N=19+24h` in this block, the B-ancestor

`Y=16h+15`

has exact maximum

`Ymax=3263227690466750287`,

which is below the RL300 external threshold

`4761963248413673697`.

Thus the inherited RL300 bound `D(Y)<=2334` applies to every B-ancestor in this block. Since the first four half-steps from Y to B0 are all odd,

`J_B = J_Y - 4 <= 2330`.

Therefore the B trajectory alone cannot attain the required common weight, and every retained selector through the next resonance minus one is eliminated.

The next record is

`(630118245525664765,397560349370386783)`.

This gives the first RL301 checkpoint frontier

`a=630118245525664764`.

## 3. New external class-record certificate

RL301 freezes a stronger provenance-backed external finite computational dependency:

`D(n)<=2456 for every positive n<46500000000000000000`.

The source is Eric Roosendaal's class-record project. Its current status states that all numbers up to `46.5*10^18` have been checked for class records, and the class-record table states that all 2425 class records up to that bound are listed. A class record is the least element of a delay class.

The largest delay class represented below this bound is 2456, with class record

`28019077177231758495`.

The portable RL301 verifier independently replays its ordinary Collatz delay as exactly 2456.

Therefore if any positive `n<46500000000000000000` had delay greater than 2456, the least element of its delay class would be a class record below the completed bound, contradicting the complete class-record table.

This is an external finite computational dependency: RL301 does not rerun the historical exhaustive class-record search.

## 4. Second B-ancestry block and promoted frontier

At the next controlling resonance

`(630118245525664765,397560349370386783)`

the exact relaxed ceiling is

`Nhat=57867840550427715479`.

For `N=19+24h`, the maximum B-ancestor is

`Ymax=38578560366951810319`,

and

`38578560366951810319 < 46500000000000000000`.

Hence every B-ancestor in this block satisfies `D(Y)<=2456`. Ordinary delay bounds half-Collatz stopping time, so `J_Y<=2456`; removing the four initial odd half-steps gives

`J_B<=2452`.

Thus the inherited weight theorem needs only

`2rho-m >= 2454`.

For the longest inherited horizon `m=a-32`, with `rho=ell-3`, the left side is

`2ell-a+26`.

The retained selector floor `ell>=ceil(147a/233)` gives

`2ell-a+26 >= 61a/233+26`,

which already vastly exceeds 2454 at the first newly exposed `a` and increases thereafter.

Therefore the B physical word alone excludes every retained selector in both new record blocks, yielding

`boxed: every retained selector through a=7354673373747273032 is eliminated.`

This frontier depends on the promoted external class-record certificate above.

## 5. Exact next boundary

The next one-sided resonance record is

`(7354673373747273033,4640282259296926456)`.

Its exact relaxed ceiling is

`Nhat=325482729518061951549`,

with

`Ymax=216988486345374634367`.

This exceeds the external class-record threshold, so the present certificate + four-step B-ancestry mechanism stops exactly before this record.

This is a method boundary, not a counterexample.

## 6. Finite-ladder diagnosis

Exact continued-fraction continuation gives further controlling records whose B-ancestor maxima are:

- at `a=43497921996957973433`: `578000081092056995967`;
- at `a=123139092617126647266`: `1718888687177252770687`;
- at `a=325919355854421968365`: `65745565451581383653839`.

The required quantitative external ranges therefore escalate sharply. Deeper reverse ancestry does not uniformly improve the coefficient 16 because RL299 already proved the `h==0 mod3` optimality barrier. A forward residue/transducer exploration did not produce theorem-sized contraction and is not promoted.

RL301 therefore classifies the external physical route as a strong finite accelerator but not, in its present form, a structural Gate-A closure route.

## 7. Strategic comparison with Bellman/P

The parked RL297 route remains weak-green rather than proved, but it is scale-free and structural:

- no Bellman score >=2 was found in the exact P-cone audit through added area 27;
- the unique tight score-1 endpoint is checkpoint 8;
- the shared dual endpoint `N(P)=T(8)=7` gives a concrete mechanism behind the observed checkpoint distance identity;
- RL294 already contains all-depth endpoint/cascade algebra and checkpoint-2 domination;
- RL296 reduced the difficult `(4,39)` front-door branch to four explicit residual states.

In contrast, the external physical route now demonstrably asks for successively larger finite delay certificates.

RL301 therefore closes with the strategic decision

`RETURN_TO_BELLMAN_P_ROUTE_STRATEGICALLY_SUPERIOR`.

The physical/resonance route is frozen, not discarded, and may be resumed if a qualitatively stronger structural or quantitative certificate becomes available.

## 8. Proof-state distinctions

Promoted internal exact mathematics/computation:

- exact B-ancestry use at the first RL301 boundary;
- 44-term certified continued-fraction prefix used by the portable verifier;
- exact consecutive resonance records through the new boundary and several diagnostic records beyond it;
- exact `Nhat` and B-ancestor maxima;
- exact conversion `D(Y) -> J_B` through four odd half-steps;
- exact selector-margin comparison;
- exact finite-ladder diagnostic values.

Promoted external finite computational dependency:

- completeness of the class-record computation below `46.5*10^18`, yielding `D(n)<=2456` throughout that finite interval.

Not promoted:

- independent exhaustive verification of all starts below `46.5*10^18`;
- any claim that convergence checks alone imply a stopping/delay/J bound;
- any extension at or beyond `a=7354673373747273033`;
- any global Collatz theorem;
- Gate A, Gate B, or global non-trivial-cycle exclusion.
