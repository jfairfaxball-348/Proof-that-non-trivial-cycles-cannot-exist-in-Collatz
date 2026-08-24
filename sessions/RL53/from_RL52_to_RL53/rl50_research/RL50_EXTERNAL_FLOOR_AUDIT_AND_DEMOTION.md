# RL50 — external floor audit and demotion

Date: 2026-08-22

## Status

**EXTERNAL-DEPENDENCY AUDIT + EXACT ELEMENTARY COUNTERCHECK.**

This note changes the admissible dependency ledger. It does **not** disprove Ansari's broader ideas, and it does not prove or disprove the Collatz conjecture. It records a concrete failure in the printed induction that RL49 had conditionally used to raise the verified prefix beyond `2^71`.

## 1. What RL49 had used conditionally

RL49 treated the following as conditional pending audit:

- Barina's computational verification through `2^71`;
- Ansari 2025, Proposition 3.2 / Remark 3.1, as a recursive-sufficiency argument upgrading this to
  `R_ext = 4*3^44+2`;
- the resulting strengthened phase/Farey denominator floor
  `ell >= 205632218873398596256`.

The arithmetic in the final bullet is correct **if** `R_ext` is a valid certified prefix. The issue is the external theorem used to justify `R_ext`.

## 2. Direct check of the printed sieve definition

Ansari defines

`F_n = union_{a_0,...,a_{n-1} in {0,1}} (4*3^n N_0 + 4 sum_i a_i 3^i + 3)`.

Reducing this exact definition modulo 36 gives

`F_1 mod 36 = {3,7,15,19,27,31}`,

`F_2 mod 36 = {3,7,15,19}`,

so

`F_1 \ F_2 mod 36 = {27,31}`.

This is an exact finite residue computation, independently reproduced by `verify_rl50_external_floor_audit.py`.

## 3. The printed induction identity fails already at n=1

In Lemma 3.1 the paper introduces an auxiliary `F'_n` in which the final two ternary digits range over `{0,1,2}`, then an `A'` obtained by fixing both of those digits to `2`, and states

`F_{n+1} = F'_n \ A'`.

At `n=1`, directly from the printed formulas,

`F'_1 mod 36 = {3,7,11,15,19,23,27,31,35}`,

`A'_1 mod 36 = {35}`,

therefore

`F'_1 \ A'_1 mod 36 = {3,7,11,15,19,23,27,31}`,

which is not

`F_2 mod 36 = {3,7,15,19}`.

Thus the displayed induction identity used to prove every `F_n` recursively sufficient is false in the first induction step.

This is more than a missing explanatory sentence: four entire residue classes (`11,23,27,31 mod 36`) remain in `F'_1\A'_1` but are absent from `F_2`.

## 4. The 31-class is not the whole obstruction

The residue class `36k+31` itself has an elementary merge to a smaller integer:

`36k+31 <- 72k+62 <- 48k+41 <- 32k+27`,

where every arrow is an undirected edge in the shortcut Collatz graph and

`32k+27 < 36k+31`.

Equivalently, for `x=36k+31`,

`x <-> 2x <-> (4x-1)/3 <-> (8x-5)/9 = 32k+27 < x`.

The verifier checks this on 1000 symbolic instances after proving the formulas algebraically. This shows that one of the two classes in `F_1\F_2` is individually recursive, but it does not repair the printed `F'_n\A'` identity or prove the needed recursive-sufficiency chain.

## 5. Dependency decision

For this RL project, until a corrected proof or authoritative corrigendum is independently verified:

- **ACCEPTED EXTERNAL COMPUTATIONAL FLOOR:** `2^71` (Barina 2025).
- **NOT ADMISSIBLE AS AN AUDITED FLOOR:** `4*3^44+2` from the printed Ansari argument.
- **DEMOTED:** RL49's strengthened denominator floor `ell >= 205632218873398596256`.
- **STILL VALID CONDITIONALLY:** the arithmetic/Farey verifier showing what would follow *if* the stronger floor were supplied by a valid theorem.

A search of the official journal article page during RL50 did not expose an erratum/corrigendum. This is not a claim that no correction exists anywhere; it is only the present audit state.

## 6. Safe phase gate after demotion

Re-running the RL49 phase verifier using only `N >= 2^71` gives the accepted gate

`ell <= 92524042457747860050`  (Legendre region),

with exactly one above-`log_2(3)` convergent surviving the phase inequality below that gate:

`a   = 123139092617126647266`,

`ell = 77692117359936589403`,

`q   = 45446975257190057863`.

This is now the correct explicit stress point below the safe gate. It is not itself a candidate proved to satisfy the structural/full-phase constraints; it is merely the only continued-fraction spine point not eliminated by this particular phase inequality in the stated denominator range.

## Verification

Run:

`python rl50_research/verify_rl50_external_floor_audit.py`

and

`python rl49_research/phase_squeeze/verify_rl49_phase_resonance_squeeze.py`.
