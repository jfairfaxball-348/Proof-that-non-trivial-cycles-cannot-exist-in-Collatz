# RL287 proof-state and scope red team

Status: PASS
Date: 2026-09-09

## Audited primary classification

`STATE_RESERVE_PHASE_TRANSPORT_AND_GLOBAL_REACHABILITY_BARRIERS_PROVED`

## Checks

1. **Gate A remains open.** PASS. No RL287 theorem proves `nu_2(J)<=H`, `nu_2(K-1)<=H+d-1`, `k<=H_can`, or the fixed-seed high-divisibility sign theorem.

2. **Residual preserved exactly.** PASS. The authoritative residual remains `k>=25`, `k` odd, `H_can<k`.

3. **Local examples are not promoted to global reachability.** PASS. Direct-terminal predecessor families, arbitrary-hazard reset families, and `(110)^N` boundary families are explicitly local positive-phase/boundary constructions. No claim is made that their chosen inputs are reachable from the canonical seed at low height.

4. **Scalar dependency is explicit.** PASS. `Pcal=Q(2J+3)/5` is recorded as `(4/5)B+(1/5)Q`. The normalized global Ferrers reserve is recorded as exactly the inherited coupon defect `D`. Neither is counted as an independent terminal constraint.

5. **Cylinder-isometry scope.** PASS. The theorem says: if one input realizes a fixed legal segment, then all inputs in the same `2^L` lift family realize that segment and the output lift changes by an odd affine unit. It does not assert that arbitrary lifts are globally reachable from the fixed seed.

6. **Finite evidence separation.** PASS. The scratch `H<=22` odd-quotient phase inequality is explicitly `UNPROMOTED_FINITE_EVIDENCE_ONLY` and is not used to narrow the residual or justify a global theorem.

7. **Boundary-surplus theorem scope.** PASS. The linear lower bound applies only to a hypothetical residual Gate-A violator using inherited RL279 phase-box/residual facts. The `(110)^N` family is a separate local barrier and does not contradict that global necessary condition.

8. **No forbidden project drift.** PASS. Gate B remains separate/open/frozen; fifth selector unscanned; Radius 6+ frozen.

9. **No double-counting of inherited quantities.** PASS. The report explicitly identifies when new coordinates are algebraic repackagings of `B`, `D`, or inherited telescopes.

10. **Verifier role.** PASS. The portable verifier is regression support for exact identities/families. Analytic results are not reclassified as finite certificates.

## Corrections/demotions

None.

The exploratory finite phase inequality remains unpromoted and therefore requires no demotion.

## Remaining obligation

The missing theorem is genuinely global: restrict the high 2-adic cylinder lift selected by the complete canonical prefix from the fixed seed. Preferred target is RL285's all-depth `nu_2(K-1)<=H+d-1` or equivalent fixed-seed sign theorem.

RED TEAM: PASS
