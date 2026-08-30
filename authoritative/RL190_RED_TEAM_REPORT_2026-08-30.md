# RL190 red-team report

Date: 2026-08-30

## Scope

Adversarial review of the phase-43 exclusion, phase-46 exceptional reduction, `N_35` density update, and phase-resolved H21 charging core.

## Checks passed

1. **Boundary indexing.** A terminal at `t+43` has its `tau=37` start exactly at `t+6`, so six transitions are necessary and sufficient for the affine comparison.

2. **No borrowed corridor.** The six-step proof does not extend RL189's clean `tau=35` corridor by assumption. RL183's transition law is global for ordinary/common-mechanical p-pairs. Exact source-rank propagation shows all six transitions avoid `R-1` and `L-1`.

3. **Phase-43 word and error.** The full separation-43 overlap has one word, `212122`. Exact Fraction propagation gives center `3^43/2^31`, radius `1519/1024`, and strict separation from both `2^37` and `2^38`.

4. **Rank-only exclusions.** Separations 44 and 45 have genuinely empty intersections of the inherited terminal core with its cyclic translates.

5. **Phase-46 scope.** The nine-step affine argument is used only on source ranks avoiding the two common-mechanical exceptions. The two exact exception ranks are deliberately retained, not silently passed through the ordinary law.

6. **Density integrality.** The new global ceiling is not the naive `3/46`. For intervening nontriple blocks with starts, the integer floor `K<=floor(2S/37)` is retained. Residue-class arithmetic proves the true worst grouped density is `1/15`, attained at `S=37,K=2`.

7. **Charging direction.** At the new cap, the guaranteed `tau=35` coefficient still dominates half the `tau<=34` coefficient, so the two-level objective again increases toward the largest permitted `y`. The old flat point remains the exact optimum under `2x+y<=2^-22`, `x>=y`.

8. **H21 reconstruction.** The common `(T,H)` rows for offsets 33, 34, and 35 are reconstructed from the inherited integer conditions. Full-prefix backward gap propagation is then applied to actual mechanical factors, not arbitrary words.

9. **H21 joint core versus individual cores.** The promoted `D=[23369453298,41775866136]` is the intersection required for simultaneous `{33,34,35}` ownership. Individual `tau=34/35` compatibility extends farther; no stronger individual exclusion is claimed.

10. **Predecessor reset.** The `tau=35` starting numerator has odd part 7 and is nonzero modulo 3. Using the inherited RL182 iff sensor, the immediately preceding defect is odd/nonzero, proving span 36 without a backward-height assumption.

## Claims deliberately rejected

- No physical realization of either phase-46 candidate rank.
- No exclusion of separation 46.
- No elimination of the isolated extremal triple.
- No improvement of the ordinary corrected-flow floor beyond `>443`.
- No claim that all phase-resolved charging schemes fail.
- No branch or global closure.

## Verdict

PASS for promotion with the scope locks above.
