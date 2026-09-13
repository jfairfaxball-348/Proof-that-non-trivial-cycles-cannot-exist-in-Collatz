# RL307 red team

Date: 2026-09-13
Result: `RL307_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`

## Checks

1. **No shell-owner overclaim.**
   The proved R3 statement is only `M_R3>=M_8-3`, not `M_R3>=M_8`.

2. **Tight-wall recurrence coverage.**
   Every first R3 tower departure is classified by parity. Cross siblings are removed only by exact same-wall earlier R3 histories with strictly smaller cost. The shallow `d=3` branch is handled by the inherited boundary/checkpoint-2 recurrence.

3. **D0 scope.**
   Only the already-promoted F/S merger and odd leading-P families are contracted. The A-family and even trailing-P sectors remain open.

4. **A-family barrier.**
   The fixed `W_-4` factor is not assigned a generic positive penalty. The exact counterexample `M_A4(2)=M_S5(2)=8` explicitly blocks that shortcut.

5. **First-positive completeness.**
   The portable verifier reconstructs the complete minimum-cost nonpositive quotient for `(-28)` (19 states) and `(-17)` (27 states). Positivity is forward invariant, so no terminal positive checkpoint can bypass these front doors.

6. **History domination is physical-state valid.**
   Higher-cost revisits of a nonpositive state are discarded only because the future transition graph depends on the physical state, so the minimum-cost revisit can copy the same suffix.

7. **`Bcal(4,39)-6` provenance checked.**
   It comes from `(-28)->V=(5,104)` at cost 5, `V->(4,52)` at cost 4, and the cheaper `(4,39)->(4,52)` ingress at cost 3:
   `Bcal(4,52)<=Bcal(4,39)+3`, hence contribution `<=Bcal(4,39)-6`.
   It is not attributed to the U branch.

8. **Two fixed residues checked algebraically.**
   `X=(4,43)=(4,39)oW_4` and `Y=(6,504)=P o R_4`.

9. **No generic P-insertion theorem revived.**
   Inherited counterexamples remain binding. The exploratory fixed-context grammar is not promoted.

10. **`(-84)` remains partial.**
    The two safe six-column cylinders are supporting scratch only; wall-hit residues remain open.

11. **No finite evidence promoted to all-depth checkpoint-8 theorem.**
    RL306 shell certificates and affine-tree data retain their inherited evidence/certificate status.

12. **Gate A remains open.**
    No source ceiling required by Gate A is declared closed.

## Final red-team disposition

All promoted RL307 claims are either algebraic all-depth consequences of inherited exact identities or explicitly finite complete physical-state certificates replayed by the closeout verifier.
