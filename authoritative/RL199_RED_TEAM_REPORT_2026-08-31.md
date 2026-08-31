# RL199 Red-Team Report

Date: 2026-08-31. Verdict: PASS for the scoped candidate.

1. Checked the indexing distinction: RL198 has 34 unit pair-costs, while exactly the first 33
   transitions are zero-defect individual exponent-one steps before the terminal split.
2. Re-derived `2^34 | (Y_0+1)` and the unique oriented lift index `eta`.
3. Replayed all 33 affine tail transitions and the exact preterminal difference `14*3^34`.
4. Independently derived the `tau=35` inverse formulas for states `011` and `111`.
5. Proved rather than assumed that every odd cycle state is nonzero mod 3.
6. Exhausted residues mod 18: exactly `0,8,9,17` satisfy the state/prehistory conditions, with
   the claimed state and terminal orientation.
7. Re-derived the final individual exponent law and signed terminal defect; checked the terminal
   numerator is `7*3^35` in either orientation.
8. Recomputed `3^(-34) mod 2^22=1893305` and all four CRT forbidden lift residues modulo
   `37748736`.
9. Confirmed the Hensel filter removes one of `2097152` lift residues inside each mod-18 class,
   not an entire state/sign class.
10. Confirmed `eta` cancels from every displayed common suffix difference. The resulting barrier
    is limited to the named unoriented interface.
11. Re-derived the signed K increment and retained the no-excursion guardrail.
12. Confirmed no H21 realization/exclusion, budget release, branch/Gate/global closure is claimed.

No correction/demotion event is required.
