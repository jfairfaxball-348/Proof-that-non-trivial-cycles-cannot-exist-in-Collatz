# RL178 red-team report — 2026-08-29

## Scope

Red-team the new second-transition law, the `v=37,d=+1` exclusion, the surviving `d=-1` return window, and all proof-state classifications.

## Checks

- **Indexing:** PASS.  `J=23` is the mismatch exponent index; `k=24` is the first nonzero-defect state phase.  The next mechanical digit used for continuation is correctly `c_24=1`.
- **Extremal gap:** PASS.  `v2(g_p)=37` together with inherited `0<g_p<2^38` forces `g_p=2^37`; no external least-state minimum is used.
- **Positive-sign pair relation:** PASS.  `2y_(p+24)-y_24=3^24` follows from the common-prefix gap and mismatch exponents `(1,2)`.
- **Positive-sign contradiction:** PASS.  Height caps give `a_(p+24)=1`, `a_24 in {1,2}`.  Exact `v2(3^25+1)=2` is incompatible with both valuation patterns.
- **Negative-sign pair relation:** PASS.  `y_(p+24)-2y_24=3^24` follows from mismatch exponents `(2,1)`.
- **Negative next pair:** PASS.  `v2(3^25-1)=1` excludes the equal-valuation `a_(p+24)=2` option and forces `(1,1)`.
- **Transition recursion:** PASS.  The formulas compare the exact valuations of the two transformed odd numerators.  Equality cases correctly require one extra factor of two because the normalized zero-defect difference is even.
- **Finite coverage:** PASS.  The certificate enumerates every exponent pair allowed by the mechanical height caps at each propagated necessary state through phase 30.  No range is sampled or truncated.
- **Existence overclaim:** PASS.  Surviving necessary states are explicitly not treated as realizable cycles.
- **Residue-deficit identity:** PASS.  It is a summation-by-parts representation of the corrected physical flow with the unique final carry separated; it does not use the demoted RL173 functional or revive the RL175 sparse resultant as a gap obstruction.
- **External provenance:** PASS.  No new core result uses `m>=2^71`.
- **No false closure:** PASS.  Only one signed high zero-height type is excluded.  The preferred branch and global problem remain open.

## Conclusion

PASS for promotion as a genuine narrowing/second-transition result.  RL179 should attack the surviving `v=37,d=-1` branch from the forced negative window and quantized phase-29 return interface before broadening to the remaining zero-height odd-part classes.
