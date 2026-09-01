# RL215 independent scope / red-team report

Date: 2026-09-01. Verdict: PASS for the scoped RL215 candidate.

Checks performed:

1. Re-derived the complementary arc from the exact accelerated recurrence: the
   remaining `z=L-p` odd steps carry `y_p=y_0+K0` back to `y_L=y_0` with exponent
   `A-u`, giving `2^(A-u)y_0=3^z(y_0+K0)+P_z`.
2. Checked the sign: `P_z` is the ordinary affine numerator of a nonempty positive
   arc, so `P_z>0`; this yields a lower, not upper, bound on `y_0`.
3. Confirmed independence from RL214 at the claimed scope: RL214 used the first
   p-arc numerator; RL215 uses the distinct complementary return arc and full-cycle
   return. No `Q modD=0` quotient-residue mistake is made.
4. Re-derived `L ln(gamma)=ln2+z delta` from `Ap-uL=1`.
5. Verified the rational upper bound
   `ln2<13274467117/19151007876` from the positive atanh series through n=6 plus
   a geometric tail, and used only exact rational inequalities thereafter.
6. Reconstructed all 108,950 e=16 prefixes and all 45,046 H21-compatible prefixes.
7. Projected the strict lower root bound and inherited RL214 upper cap exactly onto
   every progression; kmin is only 28,812 or 28,813.
8. Re-solved the terminal Hensel congruence inside the two-sided ranges. Exactly
   170 candidates fail; no prefix fails.
9. Confirmed both H21 states, all four mod18 classes and all 469 reachable mod2187
   classes remain represented.
10. Checked the shifted e=16 p-arc roof estimate independently; it is weaker by
    1,251 or 1,252 k-steps and adds no deletion.
11. Confirmed no arithmetic-candidate deletion is promoted as a necessary-rank,
    physical incidence/charge, branch, Gate or global-cycle conclusion.

No correction or demotion is required. The global frontier remains 13,415,865,871.
