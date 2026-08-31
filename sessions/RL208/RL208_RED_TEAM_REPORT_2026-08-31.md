# RL208 independent red-team report

Date: 2026-08-31.

Result: **PASS at the stated RL208 scope.**

1. **Terminal/source coordinates:** all exclusion counts use terminal phase
   `i=pr modL`; the source split alone uses `a=i-34 modL`.  No source rank is
   tested against a terminal predicate.
2. **Carry convention:** the maximum selected radius is `2^35`, and the exact
   inequalities `2^35<p-1<z+1` keep both selected root paths away from the
   unique carry.  No quasiperiodic carry is silently crossed.
3. **Boundary signs:** safe-band crossings are certified by exact rational
   logarithm enclosures.  Floating-point arithmetic is not used for promoted
   signs.
4. **Gap-free/disjoint count:** 704 consecutive half-open layers partition the
   new phase domains `[2^24,2^35)` and `[L-2^35,L-2^24)`.  Exact floor sums and
   an independent inverse-coordinate rectangle count agree for every layer.
5. **Prior-deletion overlap:** the new phase layers are outside the old root
   windows, forward/backward layers are disjoint, and the verifier finds zero
   hits among all twelve isolated and four anchor deletions.  The subtraction
   16,188,727,234 - 2,765,120,323 is therefore disjoint and exact.
6. **No recycled eta information:** the result uses only root K geometry and
   monotone terminal rank.  It does not relabel parity, state, sign, valuation,
   Hensel residue, endpoint moment or denominator equivalence as new data.
7. **Physical and Gate scope:** a necessary-rank exclusion is not a physical H21
   occurrence or charge.  No branch contradiction, Gate A/B closure or global
   nontrivial-cycle conclusion follows.
8. **Method saturation:** at `N=2^35` the conservative common-radius safe band is
   the full inherited core.  The report does not overstate this as a no-go for a
   sharper pointwise root argument.

No correction or demotion is triggered.
