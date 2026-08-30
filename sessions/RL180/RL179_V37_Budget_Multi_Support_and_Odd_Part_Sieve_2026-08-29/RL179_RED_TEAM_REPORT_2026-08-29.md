# RL179 red-team report — 2026-08-29

## Result

PASS for promotion as a narrowing / support-multiplicity / congruence-sieve result.

## Checks

1. **No high-branch overclaim.** `(37,0,23,-1)` remains open.  The report promotes mandatory later support, not a contradiction.
2. **Budget coverage.** The exact verifier propagates every RL178 necessary phase-24 state through phase 29 and obtains 10 path histories.  The promoted best cumulative value is the exact maximum over those histories, not a sample.
3. **Pre-phase-24 omission.** Legitimate because inherited `G_i=0` through phase 23, so those flow terms vanish.
4. **Positive-term cap.** The inference `T_i<1` uses RL178's proved residue ordering `rho_i<1` for every nonzero phase, together with `T_i=rho_i(2^-hp-2^-h)` when `G_i>0`.
5. **`F2>1/3` rigor.** No floating-point logarithm is used.  The verifier uses exact `Fraction` arithmetic, a finite atanh-series lower/upper bound for `ln 2` and `ln 3`, and a rational tail bound.
6. **Multiplicity inference.** Later *net* flow `>1` implies the sum of later positive terms is `>1`; because each positive term is `<1`, at least two distinct positive phases are required.  The analogous `>2` inference gives at least three.
7. **Pair-state scope.** Phase-30 images are necessary arithmetic states only.  No survivor is called physically realizable.
8. **Odd-part theorem scope.** The mod-8 exclusion is asserted only when `c_(J+1)=1`; the four `c_(J+1)=2` indices are explicitly left open.
9. **Residue calculation.** The forbidden `v2=2` condition is checked over all four odd residues modulo 8 for both signs and both parities of `J+2`.
10. **Historical locks.** RL173 auxiliary-functional demotion, RL175 resultant restriction, corrected physical p-shift, and no-use of `m>=2^71` are retained.

## Open obligations

- Convert the multi-support requirement into a quantitative residue-deficit contradiction or further support-location restriction.
- Continue exact phase-29 pair states without uncontrolled necessary-state explosion.
- Lift the odd-part sieve to higher 2-adic modulus, especially the four `c_(J+1)=2` indices.

No correction/demotion event was triggered.
