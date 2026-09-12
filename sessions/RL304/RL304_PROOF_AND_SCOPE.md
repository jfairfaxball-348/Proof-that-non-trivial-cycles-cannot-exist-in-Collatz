# RL304 proof and scope ledger

Date: 2026-09-12

## Promoted analytic mathematics

1. For `Q=(2,18)`,
   `Q^n=(2n,9(9^n-1)/4)`.

2. For
   `C_n=Q^(n-1) o P o Q`
   and
   `T_n=Q^n o P`,
   one has exactly
   `C_n=(2n+2,(3^(2n+4)-441)/4)` and
   `T_n=(2n+2,(3^(2n+4)-57)/4)`.

3. Therefore
   `T_n=C_n o H_96`
   with fixed formal translation
   `H_96=(0,96)`
   for every `n>=1`.

4. Under common physical input columns while the defect is even, the paired states have equal depth and output and the defect updates by
   `h'=3^y h/2`.

5. Starting from `h=96`, after five common columns the defect is exactly
   `3^m`, where `m=1+sum(y_1,...,y_5)` and `1<=m<=6`.

6. On the sixth common input, opposite parity gives the exact finite factor grammar:
   - if the source output is 0,
     `T'=C' o F_m`,
     `F_m=(1,3(3^m+1)/2)`;
   - if the source output is 1,
     `C'=T' o G_m`,
     `G_m=(1,3(1-3^m)/2)`.

7. The twelve fixed K-values are
   `F: 6,15,42,123,366,1095`
   and
   `G: -3,-12,-39,-120,-363,-1092`.

8. Relative historical cost through this six-column cut is exactly zero because the paired physical depths agree at the start of all six edges.

9. The exact physical witness words listed in `RL304_REPORT.md` replay from `C_n` to `T_n` over their stated finite ranges.

## Important non-claims

- O1 is not proved or refuted.
- Gate A is not proved.
- The twelve-factor grammar is not proved to terminate under iteration.
- No theorem states that all twelve factors are checkpoint-8 owned.
- No generic integer-wall-debt theorem is revived.
- No recurrence is promoted from the finite witness-word data.
- No shortest-path finite search is used as an all-depth theorem.
- The P/Q route has not met the user's criterion for a clearly convergent all-depth mechanism.

## Strategic disposition

The P/Q route is frozen at this exact frontier and loses automatic priority for the next RL only because the user explicitly requested a whole-project strategic audit unless a major obligation had closed or the route had become clearly convergent. Neither condition occurred.

## Still open

O1, O2, P/8, `Bcal(P)<=1`, checkpoint-8 excess-one, RL296 non-P residuals, Gate A, Gate B, and global non-trivial-cycle exclusion.

## Frozen branches

The physical/resonance branch remains frozen at external selector frontier `a=7354673373747273032`. Radius 6+ and the separate Lean formalisation remain out of scope for RL305 except as audit inputs where relevant.
