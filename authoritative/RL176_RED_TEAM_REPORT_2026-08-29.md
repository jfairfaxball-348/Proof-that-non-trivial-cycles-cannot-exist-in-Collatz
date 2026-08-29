# RL176 red-team report — 2026-08-29

## Scope

This review stress-tests only the new RL176 p-gap and first-mismatch
claims.  It does not re-audit inherited RL175 certificates under the
verification-economy rule.

## Checks

- **Endpoint exponent lemma:** `a_0=1` follows from minimality of `m`.
  `a_p=1` uses the inherited RL175 fact that `y_p` is the unique
  second-smallest physical state and the genuine period length `L`; if
  `a_p>=2`, the next state would be below `y_p` and therefore equal `m`,
  producing an earlier return.  No ownership resultant is used.
- **Mod-4 lattice:** exact exponent one at an odd state is equivalent to
  residue `3 mod 4`, so `4 | (y_p-m)` is exact.
- **Gap upper bound:** the proof uses only
  `exp(Delta)-1>Delta`, the RL175 half-barrier, and the inherited
  certified `Delta>1/1,116,000,000,000`.  No decimal logarithm is needed.
- **Mismatch existence:** it is proved *before* the valuation identity.
  If 37 shifted exponents agreed, the difference after 37 identical
  affine maps would be even and force `2^38 | g_p`, contradicting
  `0<g_p<186,000,000,000<2^38`.
- **Index safety:** `p+37<L`, so the 37-step comparison does not wrap
  around the cycle.
- **Valuation identity:** at the first mismatch, unequal valuations of
  `3X+1` and `3Z+1` force the valuation of their difference to be the
  smaller one.  This yields
  `v2(g_p)=S_J+min(a_J,a_{p+J})` exactly.
- **External boundary:** the lower band
  `g_p>=10,608,333,336` is explicitly conditional on the inherited
  computational minimum `m>=2^71` and is not used in the internal core.
- **Corrected defect:** all p-shift statements use
  `G_i=S_{p+i}-S_p-S_i`; the old RL173 defect is not revived.

## Red-team conclusion

PASS for promotion as a narrowing result.  No contradiction is claimed.
The preferred `h_p=0` branch remains open; RL177 must still control the
sign and compensation of the forced early corrected p-shift defect.
