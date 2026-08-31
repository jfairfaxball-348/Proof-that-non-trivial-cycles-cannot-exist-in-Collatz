# RL203 certified facts and proof ledger

Date: 2026-08-31. Canonical status-bearing ledger. All physical implications
remain conditional on the sole high branch `(37,0,23,-1)` and every inherited
H21 ownership/Gate/global scope lock.

## Proved analytic mathematics

- Put `d=3^p-2^u` and
  `E_a=3*2^u*K_0-3^p P_p+d P_a`. At an H21 tau34 source of height one, the
  inherited exact endpoint moment is equivalent to
  `E_a=d*2^(b_a-1)*3^(1-a)*(2^34 eta-1)`. Hence the normalized 2-adic unit
  `U_a=E_a/2^(b_a-1)` is exactly
  `U_a=d*3^(1-a)*(2^34 eta-1)`.
- Every truncation of `U_a` modulo `2^m`, `m<=34`, is eta-independent. Modulo
  `2^35`, the first eta-sensitive bit is exactly `eta mod 2`, which is already
  the inherited terminal-orientation/sign bit. This is an information-boundary
  theorem, not a new sign selection.
- The forced tau34 unit-cost tail reproduces the same bit exactly. Its first 34
  normalized terms sum to `3-2^34 (mod 2^35)`. If eta is even the lower terminal
  exponent is one and the terminal term changes this to `3`; if eta is odd that
  terminal term vanishes modulo `2^35`. These are exactly the two residues of
  `3(1-2^34 eta)`. Thus the shallow dyadic consumer is tautological with the
  inherited terminal-orientation law.
- To combine a newly determined dyadic eta residue with the inherited terminal
  Hensel exclusion modulo `2^22`, eta must be known modulo `2^22`, equivalently
  the normalized endpoint unit must be known through modulus `2^56`.
- On the `a<p` side, offsets `1..33` before the zero anchor `p` are impossible
  for a tau34 source because the inherited 34 positive H21 heights would hit
  `h_p=0`. Offsets 34..38 have exact canonical ranks
  `15303429871,72382725878,129462021885,49013272580,106092568587`, all outside
  the inherited rank core. Offset 39 has rank `25643819282`, the first rank in
  that core.
- Therefore every surviving necessary H21 source with canonical phase `a<p`
  satisfies `p-a>=39`. The Bezout identity gives
  `b_(p-e)=u-ceil((Ae-1)/L)`. At `e=39`, height one gives
  `u-(b_a-1)=63`, and the depth is nondecreasing as `e` grows.
- In the exact `a<p` prefix representation
  `E_a=3*2^(u+37)-2^u P_a-3^p sum_(j=a)^(p-1)q_j`, the finite prefix `P_a` is an
  odd 2-adic unit (`q_0=1`, while every `q_j`, `j>=1`, is 2-adically even).
  Consequently the root-prefix contribution begins exactly at depth at least
  63 for every below-p necessary source, while the first root-normalization term
  begins still deeper. Both vanish modulo `2^56`.
- Hence the existing root anchor cannot independently determine the Hensel-level
  eta bits for any below-p necessary source at this truncation depth. A
  continuation on this side must use genuinely deeper post-terminal completion
  data or a different independently global coupling.

## Exact finite certificate

`verification/verify_rl203_dyadic_prefix_boundary.py` checks the actual constants,
Bezout/rank identities, exact offset ranks 34..39, the depth-63 inequality, the
`2^35` geometric-prefix parity identities, and the `2^56` Hensel-resolution
comparison.

## Inherited state retained

The exact RL202 necessary-rank predicate and count **16,188,727,234** are
unchanged. All four eta classes `0,8,9,17 mod18`, RL201's first-rank lift cut,
all inherited Hensel exclusions, exact terminal K law, endpoint moment,
denominator equivalence, and the RL202 root/anchor exclusions remain binding.

## Method barriers and open obligations

RL203 removes no rank and selects no eta class, e35 state, terminal sign or
valuation. The below-p depth statement is one-sided and must not be reflected
across the p-shift carry without proof. It is a precise barrier to the named
shallow dyadic-prefix route, not a proof that complete-word 2-adic or other
global coupling cannot succeed. No physical H21 occurrence, H21 charge,
sole-branch closure, Gate A/B closure, nontrivial-cycle exclusion or global
Collatz conclusion follows.
