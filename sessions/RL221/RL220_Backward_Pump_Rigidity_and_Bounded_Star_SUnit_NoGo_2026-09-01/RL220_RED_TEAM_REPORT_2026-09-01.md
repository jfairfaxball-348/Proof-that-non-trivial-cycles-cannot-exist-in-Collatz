# RL220 red-team report

Date: 2026-09-01

## RT1 — does fixed-block integrality get confused with full legality?

PASS. RL220-T1 assumes only that every repeated block endpoint is integral.
Full backward legality implies endpoint integrality, so using the weaker
hypothesis is safe. The theorem does not infer legality from integrality.

## RT2 — can the proof divide by a zero `2^n-3^h`?

PASS. For a nonempty block containing an odd inverse, `2^n` and `3^h` are
distinct positive powers of different primes, so `2^n!=3^h`.

## RT3 — does the theorem silently prove there are no nontrivial cycles?

PASS. It does not. A positive integral fixed point of a repeated block is left
as a possible periodic point unless it is independently certified blue. The
global nontrivial-cycle claim remains open.

## RT4 — is every parameterized word family now excluded?

PASS. No. The bounded-star theorem requires a finite expression with
independent parameters ranging over the full rectangular domain `N^r`.
Correlated/nonrectangular domains, growing numbers of odd inverses, and
aperiodic/recursive families remain outside scope.

## RT5 — is the S-unit reduction being overstated as finiteness?

PASS. No finiteness or solution-count theorem is promoted. The exact statement
is only that after bounded-star collapse the endpoint/pullback is a finite
signed exponential equation and each parameter tuple yields at most one `k`.

## RT6 — external `[1,2^71]` interval

PASS. RL220 does not promote the external computation to analytic mathematics.
The exact prefix scan proves all current root progressions have
`v2(3y+1)=1`, so the first accelerated successor is far above the interval.
Candidate deletions: zero.

## RT7 — tempting family `b_n=(4^n-1)/3`

PASS. Although `b_38=25185954575304774473045` lies inside the root band, exact equality scanning
gives zero inherited root-window matches. More importantly,
`b_n=O(2^(2n-1))`, so the family is already a fixed-word/dyadic-ray
architecture under RL219-T2 and is not advertised as a new non-dyadic route.

## RT8 — numerical inheritance

PASS. RL220 changes no candidate, prefix, eta, state, mod18, or rank counts.
All numerical frontier statements remain exactly inherited.
