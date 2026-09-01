# RL212 independent scope / red-team report

Date: 2026-09-01. Verdict: PASS for the scoped RL212 candidate.

Checks performed:

1. Re-derived `b_0..b_16`, the positive-acceleration height recurrence and the
   exact e=16 flat-K gap independently from the promoted RL210/RL211 interface.
2. Verified the finite recurrence contains exactly 108,950 arithmetic prefixes and
   that the eta map modulo 3^16 is injective on them.
3. Verified both inherited H21 states survive; no state or mod18-class exclusion
   is inferred from the 17 mod-2187 holes.
4. Verified the mod-2187 result with a compressed `(height,Q)` residue automaton,
   not a raw-prefix promotion. The exact forbidden list is `[0, 53, 431, 891, 917, 972, 1160, 1295, 1458, 1493, 1565, 1620, 1701, 1862, 2060, 2088, 2106]`.
5. Checked the root-unit refinement with exact Q values, not truncated Q mod2187.
   Every H21-compatible exact prefix has one unit-preserving lift modulo 3^17.
6. Checked that the ordinary terminal-valuation filter is independent modulo
   `2^22`; CRT compatibility is used only as a no-deletion boundary and not as an
   existence claim.
7. Confirmed the e=16 terminal rank and all global necessary counts are unchanged.
8. Confirmed the RL211 denominator-integrality shortcut remains rejected.

No correction or demotion is required. No rank deletion, physical incidence/charge,
branch contradiction, Gate closure or global nontrivial-cycle exclusion is promoted.
