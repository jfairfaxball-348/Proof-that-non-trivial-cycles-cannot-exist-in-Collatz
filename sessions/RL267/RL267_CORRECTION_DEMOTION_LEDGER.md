# RL267 correction / demotion ledger

Date: 2026-09-06

## Corrections made before promotion

1. **Determinant-pair bookkeeping label.**
   A scratch checkpoint called 2,673 the complete determinant-pair count. Exact reconstruction shows 2,683 size-surviving determinant pairs in total; 2,673 is the subset with `A>=8`, which is exactly the subset capable of supporting the three-component nonempty-gap structural parametrizations. The gap-configuration and structural-candidate counts were already computed over the correct structural range. No certificate candidate was omitted.

2. **`[2,2,1]` cyclic order coverage.**
   The first scratch pass anchored the positive length-two component but enumerated only the order `++ ... -- ... + ...`. A separate small-range brute-force reconstruction exposed the second order `++ ... + ... -- ...`. The final promoted certificate enumerates both orders independently. Each has 2,530,566 structural candidates and zero full-`D` hits.

3. **Scope of the three-component bound.**
   The uniform `U=floor((2A+2)/3)` support argument is promoted only for the two three-component leaves treated here (and may be reused only after proof of matching hypotheses). It is not silently transferred to `[2,1,1,1]` or `[1,1,1,1,1]`.

## Demotions

No inherited RL238/RL239/RL265/RL266 theorem or certificate is demoted.

No claim beyond the `[3,1,1]` and `[2,2,1]`, `|kappa|=1`, positive-domain full-`D` leaves is promoted in RL267.
