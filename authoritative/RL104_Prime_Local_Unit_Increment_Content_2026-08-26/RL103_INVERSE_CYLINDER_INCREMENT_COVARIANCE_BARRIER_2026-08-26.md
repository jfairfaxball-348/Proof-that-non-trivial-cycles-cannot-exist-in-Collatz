# RL103 — inverse-cylinder increment covariance barrier

## Outcome

RL103 tested the remaining direct affine/lattice use of the exact
first-surplus cylinder.  It does not prove a raw-multiplicity exclusion, a
lower-content theorem, either Gate closure, nontrivial-cycle exclusion, or
Collatz.

It proves an exact covariance formula showing why this direct architecture
does not yet use ordinary ownership strongly enough.  The inverse-word
cylinder is present before normalization, but it transforms by the
generalized odd increment `s`.  Setting `s=1` for an owned Collatz cycle
selects a residue class but supplies no extra denominator relation or lower
bound on that residue.

## Exact inverse-cylinder formula

Consider a positive integer cycle of

`T_s(n)=n/2` for even `n`, and `(3n+s)/2` for odd `n`,

where `s` is odd.  Start at an even physical maximum `M` and read a backward
prefix of length `h`.  Let `o` be its number of odd predecessor steps.
Define an integer `N_h` recursively from `N_0=0` by

- an even predecessor: `N_(i+1)=2N_i`;
- an odd predecessor: `N_(i+1)=2N_i+3^(o_i)`.

Direct inverse composition gives the exact physical state

`x_h=(2^h M-sN_h)/3^o`.                                   (RL103.1)

Thus integrality is exactly

`2^hM == sN_h (mod 3^o)`.                                 (RL103.2)

Let `c_h` be the unique even lift modulo `2*3^o` of
`2^(-h)N_h (mod 3^o)`.  Since `M` is even and `s` is odd,

`boxed: M == s c_h (mod 2*3^o).`                          (RL103.3)

For `s=1`, this is the ordinary exact word cylinder.  The formula is
non-normalized and concerns actual physical states, but its content is still
increment-covariant.

For a full word with denominator `D=2^A-3^L`, RL79's canonical generalized
cycle has `s=D/gcd(D,Q(W))`; genuine ownership `D|Q(W)` is exactly `s=1`.
Substituting `s=1` into (RL103.3) removes `s` but introduces no new factor of
`D`.  It therefore cannot by itself turn the tiny least representative into
a lower bound or a trapped nonzero multiple of `D`.

Classification: **analytic theorem and direct-affine route barrier**.

## Finite audit

`verification/verify_rl103_cylinder_increment_covariance.py` exhaustively
checks (RL103.1)--(RL103.3) on 161,971 primitive generalized-cycle inverse
prefixes from all binary words through length 13 with positive denominator.
This is an exact finite audit of the symbolic formula, not a proof beyond the
displayed derivation.

## Red-team ledger

- **RL79 ordinary increment:** the formula explicitly retains `s`; it shows
  that the direct affine cylinder architecture is covariant, so it is not an
  `s=1` consumer.
- **RL20 fake/full ownership:** the same congruence exists for `s>1`; the
  full-owned case only replaces its multiplier by one.
- **RL81 physical-state:** `M` and `x_h` are physical generalized-cycle
  states; no quotient height is used as a physical bound.
- **Primitivity:** the finite audit restricts to primitive words.  No
  generalized witness is promoted to an ordinary cycle.
- **Raw multiplicity and slope scope:** the formula applies to every backward
  prefix; it does not identify raw `(gp,gq)` with a reduced pair or make a
  first-Farey universal claim.
- **External floor:** unused.

## Route decision

Freeze only direct *affine* cylinder/lattice consumers: inverse integrality,
the maximum cylinder residue, and their combinations with rotation transport
or full closure.  A next content attack must add a nonlinear, prime-local, or
other genuinely absolute `s=1` input; merely stating the ordinary residue
class is insufficient.
