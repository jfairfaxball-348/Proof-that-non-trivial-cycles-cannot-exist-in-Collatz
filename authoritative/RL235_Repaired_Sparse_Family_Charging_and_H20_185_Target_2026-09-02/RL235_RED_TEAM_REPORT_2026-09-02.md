# RL235 mandatory red-team report

Status: **PASS**.

Checks performed:

1. **Necessary-state versus physical-state scope:** the 7,531 cells are treated as a retained necessary-state superset, not as claimed physical realizations.
2. **Exhaustive charging coverage:** every frozen atomic cell is checked. Generic local budget is used first; K-pricing is invoked only where generic safety fails.
3. **Invariant-specific occurrence caps:** the spacing-1001 penalty is applied only to the exact H21 `T=350220815692997949`, owners `{33,34,35}` invariant. No H20 or smaller-subset cell inherits that cap.
4. **K-pricing scope:** K-pricing is used only as a local physical defect budget. It is never used as an occurrence cap.
5. **Rank-endpoint monotonicity:** exact rational log bounds certify positive `s,d`, hence decreasing `K(r)`; the cell upper-rank endpoint therefore supplies a safe lower bound throughout the cell.
6. **Upper-tail monotonicity:** the repaired schedule is monotone (`a>b=c`) and uses inherited population differences in the same safe direction as the validated charging staircase.
7. **Variation versus excursion:** all signed/K consequences are explicitly total variation only.
8. **Historical demotions:** the invalid RL231 proof and old H17 `1,615` / `85,103,989` claims are not silently restored.
9. **Gate scope:** Gate A and Gate B remain independently open; no global Collatz exclusion is claimed.

No new stop-and-repair trigger was found.
