# RL302 closeout

Date: 2026-09-12
Base commit: `daf7739976b914b4fa62e70446d0f1da90e5fb91`
Base tree: `fde3018f880bdaa0266f49240ceb1a2910250e8f`
Successor: RL303

## Final classification

`P8_TWO_OBLIGATION_REDUCTION_TIGHT_WALL_CASCADE_NORMAL_FORMS_AND_CONDITIONAL_SECOND_OBLIGATION_COLLAPSE_PROVED`

## Promoted state

1. The all-depth P/8 checkpoint identity is reduced exactly to two fixed-source obligations O1 and O2.
2. O1 is reduced to two tight one-parameter wall families after exact R-tower zippering.
3. Paired shared-endpoint transport is identified exactly with the RL294 cascade left factor.
4. Tight walls admit exact run-length merger / leading-P normal forms.
5. O2 admits an exact two-state zero spine and odd/even F/S normal forms.
6. Generic left/right P-insertion monotonicity is disproved by exact counterexamples.
7. Conditional on O1, O2 becomes direct D0-vs-8 domination.
8. An exact `D -> D+2` index-shift splice identifies O1 and odd-O2 leading-P residual states, with a growing quadratic entry-cost margin.
9. Hence all odd-d leading-P residuals of O2 conditionally close into O1; only even trailing-P and `A_d=F_d o Z` sectors remain new after O1.

## Proof-state qualification

O1 remains unproved. Therefore O2, the universal P/8 identity, `Bcal(P)<=1`, checkpoint-8 excess-one, and Gate A all remain open.

The physical/resonance route from RL301 remains frozen, not superseded.

## Corrections / demotions

- checkpoint-3 auxiliary `(1,K=6)` is renamed `U`; do not call it `R1`;
- unrestricted relative wall grammar is marked circular, not a proof route;
- generic P-insertion monotonicity is explicitly false on both sides.

## Verification

The self-contained closeout verifier `sessions/RL302/verification/verify_rl302_structural.py` is green. See `RL302_FRESH_VERIFICATION.txt` and `SHA256SUMS.txt`.

## Successor

`RL303_BELLMAN_O1_TIGHT_WALL_TARGET.md`

RL303 should prioritize O1 `m_R3(E)>=m_8(E)`, using the exact tight-wall/run-length machinery. If O1 closes, it should immediately finish the already-contracted O2 residual before returning to checkpoint-8 excess-one and the RL296 front door.

## Catalogue status

`stale/deferred` — generated knowledge catalogues are unchanged and outside the promotion gate.
