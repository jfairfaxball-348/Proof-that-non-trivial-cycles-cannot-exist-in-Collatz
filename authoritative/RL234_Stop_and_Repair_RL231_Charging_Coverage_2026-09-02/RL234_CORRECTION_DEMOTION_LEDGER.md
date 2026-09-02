# RL234 correction / demotion ledger

Date: 2026-09-02

## Correction event

RL234 triggers the repository **stop-and-repair** rule.

The RL231 sparse-family charging proof is incomplete over its retained necessary state space. The exact witness is the retained H20 cell `(T,H)=(250157725494998535,20)` with simultaneous offsets `{32,33,34,35}` and K-compatible terminal ranks `[96351434735,98855162143]`.

RL231's assigned charge is `(1180/21)U`; its generic H20 budget is `16U`; the cell is not one of the six exact terminal families receiving an explicit occurrence penalty.

## Demotions

Pending RL235 repair, demote:

1. RL231 `ordinary |f|>665`.
2. RL231 signed-flow and directional-K consequences of that bound.
3. RL231 `N17<=1,615` charge-improvement requirement.
4. RL231 spacing-only requirement `>=85,103,989`.
5. RL232/RL233 wording that treats `1,615` as a currently proved/binding required H17 incidence cap.
6. RL233 `standalone_3adic_required_b_ge=85,103,989` as a proof-state scale consequence.

The RL233 finite 3-adic memory theorem itself is **not** demoted.

## Preserved results

RL232's exact H17 spacing `>=1001`, K cores, local owned-prefix certificates and method barriers remain valid at their stated scopes. RL233's finite-modulus decomposition remains valid at its stated scope.

## Scratch withdrawals

All RL234 exploratory strengthened flow floors are not promoted.

No frontier, e=4, Gate, branch, or global status changes.
