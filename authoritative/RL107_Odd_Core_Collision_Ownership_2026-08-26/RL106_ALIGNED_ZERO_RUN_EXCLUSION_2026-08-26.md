# RL106 — aligned all-even-run exclusion at raw first-Farey multiplicity

## Outcome

RL106 establishes one new structural theorem for the frozen first-Farey raw-
multiplicity branch.  It does not exclude a raw multiplicity, close either
global Gate, exclude nontrivial cycles, or prove Collatz.

Let the first-surplus raw pair be `(gp,gq)` at the fixed reduced first-Farey
pair, with `g>=2`, and divide the maximum-rooted prefix into `g` aligned
blocks of length `p`.  No run of `ceil(g/2)` consecutive blocks may contain
zero odd inputs.

Classification: **proved analytic theorem conditional on the inherited
external computational input `R>=2^71` and the inherited ordinary RL101
maximum envelope**.

## Proof

Put `d_h=o_(hp)-hq`.  For a run of `r` zero-odd blocks beginning after the
boundary `hp`, the identity `d_(h+r)=d_h-rq`, together with `d_g=0` and
positivity of internal `d`, gives `d_h>=rq`.  The first block cannot be zero
because `b_1>=q+1`.

The actual state at that boundary satisfies

`x_(hp)/M < rho^h/3^(d_h) < 2/3^(rq)`,

because `h<g` and `rho^g<2`.  Hence

`M > R 3^(rq)/2 >= 2^70 3^(rq)`.                           (106.1)

RL101 supplies

`M < [400,000,000,000/g](3/2)^(gq)`.                       (106.2)

Together these require

`2^70 < [400,000,000,000/g]((3/2)^g/3^r)^q`.               (106.3)

For `r>=ceil(g/2)`, the base is at most `3/4`; for even `g=2m` it is at most
`(3/4)^m`, and for odd `g=2m+1` it is at most
`(1/2)(3/4)^m`.  Since the fixed `q=72,057,431,991>=100`,
`(3/4)^5<1/4`, and `200,000,000,000<2^38`, the right side of
(106.3) is less than `1`, a contradiction.

For `g=2`, this in particular says the final aligned block contains at least
one odd input.

## Red teams and scope

- **RL79:** this is not generalized-increment invariant: the ordinary
  maximum envelope and inherited ordinary-cycle minimum floor do not survive
  scaling `(states,1)->(c states,c)`.
- **RL20:** the external floor applies only to an actual positive integer
  ordinary cycle; no rotation or CRT condition is claimed.
- **RL81:** all values in the proof are physical cycle states.
- **Primitivity:** no periodic-word conclusion is used.
- **Raw scope:** `g` remains raw multiplicity; no reduced/raw identification
  is made.
- **External status:** `R>=2^71` remains external and load-bearing.

## Related barriers retained

RL106 also verifies, without promotion as a closing result, that (i) the
two-step roof state has no uniform finite-time basin certificate, and (ii)
the bare population of internal low boundary states is generalized-increment
invariant and does not inject into odd product phases.  These remain route
barriers, not exclusions.

## Verification

`python3 verification/verify_zero_run_barrier.py` passes 299 exact threshold
checks.  The finite check audits the numerical domination; the proof above is
uniform in `g`.
