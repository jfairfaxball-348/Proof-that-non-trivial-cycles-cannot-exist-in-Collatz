# RL105 — ordinary roof factor-5 bridge: exact barrier

## Outcome and classification

RL105 tested one specifically non-homogeneous ordinary-Collatz input at the
physical roof of a hypothetical positive nontrivial cycle.  It produces an
exact physical relation and a strict maximum/minimum ratio, but proves that
the candidate factor-5 denominator use is only the already-frozen rotation
transport after full-word ownership is inserted.

Classification: **analytic candidate-route barrier**.  No Gate closure,
raw-multiplicity exclusion, nontrivial-cycle exclusion, or Collatz conclusion
is claimed.  No inherited claim is demoted.

## Candidate, scope, and proof

For a nontrivial positive cycle of the ordinary shortcut map, let `M` be its
physical maximum and `R` its physical minimum.  The candidate was to use the
two cycle states immediately preceding `M` to obtain a factor-5 condition
which remains nonzero before denominator division.

An odd maximum greater than one maps above itself, so `M` is even.  Its cycle
predecessor cannot be `2M`, hence is the odd state

`P=(2M-1)/3`.

Since `M>2`, `P>M/2`; therefore `2P>M` cannot be the predecessor of `P` in a
cycle whose maximum is `M`.  Its predecessor is the odd physical state

`Q=(2P-1)/3=(4M-5)/9`.

Thus

`4M-9Q=5`, `Q<M/2`, `R<=Q`, and `M/R>=9M/(4M-5)>9/4`.       (105.1)

The same equation gives `9 | M+1` and

`gcd(M,Q)=gcd(M,5)`.                                        (105.2)

The two-step roof chain itself was already recorded in RL86 as a consequence
of the inherited leading-`OO` roof grammar.  RL105 does not promote it as a
new theorem; it tests the new proposed *factor-5 consumer*.

## Why this is an ordinary-`+1` input

For `T_s(n)=n/2` when even and `(3n+s)/2` when odd, the corresponding affine
constant is `5s`, not `5`.  The generalized primitive word `10` gives, for
every odd `s>1`, the positive cycle `s -> 2s -> s`, with maximum/minimum ratio
exactly `2`.  Therefore the strict `>9/4` consequence is not invariant under
generalized increment scaling.

## Required red teams

- **RL79:** passes as a discriminator by the exact generalized word-`10`
  counterfamily above.
- **RL20 / full ownership:** fails as a new consumer.  Root a full parity word
  at `M` and rotate it two positions to root it at `Q`.  With its denominator
  `D`, ownership says `Q(W)=DM` and `Q(rot_2 W)=DQ`.  Equation (105.1) becomes
  `4Q(W)-9Q(rot_2 W)=5D`, which after exact division by `D` is only (105.1).
  Hence it is precisely the frozen two-step rotation-transport architecture.
- **RL81:** all three named values are actual physical cycle states; no
  quotient height is treated as physical.
- **Primitivity:** the ordinary implication needs no primitivity.  The
  generalized word `10` is primitive and is a red-team model only.
- **Raw multiplicity / scope:** the relation is valid for every nontrivial
  positive ordinary cycle and does not equate raw and reduced count pairs.
- **External input:** none.  The external `R>=2^71` floor, if imported, stays
  external and yields only `M>9*2^69`.

## No raw-multiplicity contradiction

For the inherited first-Farey pair with
`q=72,057,431,991`, the existing raw-`g` envelope satisfies

`U_g > (3/2)^(gq)-1 >= (3/2)^q-1`.

As `3^8>2^12` and `q>=150`, this is greater than `2^75-1`, hence greater
than `9*2^69`, for every `g>=1`.  The new roof lower bound is consequently
compatible with every inherited raw-multiplicity maximum envelope.  It gives
neither a bounded physical state for a finite basin certificate nor a
nonzero denominator multiple trapped in a bounded interval.

## Verification

`python3 verification/verify_roof_factor5_barrier.py` passes:

- 10,000 exact ordinary roof-chain path checks;
- 9,999 exact primitive generalized word-`10` cycle checks;
- the small-exponent comparison used in the raw-envelope compatibility proof.

The finite checks are audits of the displayed algebra, not evidence for a
nontrivial ordinary cycle.

## Route decision

Freeze only the factor-5/gcd attempt which substitutes the roof-chain
identity into a rotated full-word numerator.  It is transport in disguise.
Do not retry it through CRT, a maximum-cylinder residue, or generalized-map
homogeneous geometry.  The first-Farey raw-multiplicity obstruction remains
open.
