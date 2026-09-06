# RL268 correction / demotion ledger

Date: 2026-09-06

## Corrections before promotion

1. **Do not reuse the RL267 three-component bound.**
   The first four-component attempt confirmed that blindly replacing the three-component support cut by `U4=floor((3A+1)/4)` in the old estimate is too weak near half-period shifts. That route is not promoted.

2. **Superseded coarse scratch certificate.**
   An intermediate conservative bound with an extra factor two produced 1,115 size pairs, 256,431,048 gap configurations, 13,512,787 structural candidates and maximum structural `A=190`, with zero full-`D` hits. It was safe but non-final. The determinant-window bookkeeping was then tightened to the promoted `5*3^(7+r)*2^(U4-r)` bound, yielding the final 967-pair / 9,510,691-candidate certificate. The earlier larger counts are superseded, not contradictory.

3. **Edge-identity red-team cut.**
   A scratch direct-Q comparison initially applied the zero-flow-cut edge identity before actually rotating to a zero-flow cut and therefore reported mismatches. After enforcing the inherited cut hypothesis, the independent replay gives exactly zero edge-identity mismatches.

## Demotions

No inherited RL238/RL239/RL265/RL266/RL267 theorem or certificate is demoted.

No claim beyond the `[2,1,1,1]`, `|kappa|=1`, positive-domain full-`D` leaf is promoted in RL268.
