# RL216 independent scope / red-team report

Date: 2026-09-01. Verdict: PASS for the scoped RL216 candidate.

Checks performed:

1. Reconstructed all 108,950 e=16 root prefixes and all 45,046 H21-compatible exact prefixes from the inherited recurrence.
2. Confirmed the canonical target is uniquely selected by minimum `Q=43,013,953`; no data-dependent arbitrary prefix label is used.
3. Re-derived `y_16=2^34 eta-1-3^16*2^13` from the RL212 matched-source gap and `eta=eta_*+3^17 k` from the inherited lift.
4. Re-derived the forward height equation `h_(i+1)=c_i+h_i-v2(3y_i+1)` from the inherited mechanical relation.
5. Confirmed that a negative reconstructed height is a necessary-word contradiction, not a heuristic trajectory score.
6. Re-derived the exact RL215 interval `k=28,812..36,180` for the canonical prefix and checked that the inherited terminal Hensel congruence deletes zero candidates there.
7. Audited the modular branch rule: on `k=r+2^m t`, the current state remains affine in t; parity splitting is exact whenever the valuation is not fixed.
8. Counted each failure residue class against the finite k interval algebraically. The 6,219 disjoint failure branches cover exactly 7,369 integers and leave no survivor through phase 174.
9. Independently replayed all 7,369 deterministic candidates as a red-team check only; the failure-phase population agrees exactly with the modular sieve, including the unique latest failure at phase 174.
10. Confirmed the deleted prefix contributes 3,684 class-8 and 3,685 class-17 candidates; both H21 states and all four mod18 classes remain nonempty.
11. Confirmed eta residue 1709 modulo2187 occurs in eleven other exact prefixes, so the count of reachable residues remains 469.
12. Confirmed no deletion is promoted to terminal rank `34,124,151,203`, physical incidence/charge, branch contradiction, Gate closure or global-cycle conclusion.

No correction or demotion is required. The global frontier remains 13,415,865,871.
