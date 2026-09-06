# RL261 correction / demotion ledger

Date: 2026-09-06

## Mathematical corrections or demotions

None to promoted mathematics.

The RL260 handover explicitly marked its new-selector scratch as unpromoted.
One such scratch hint suggested a possible `k=39` phase value `N=859`.  RL261
recomputed the phase selector independently and did **not** reproduce that
value.  The exact surviving `k=39` phase classes instead have
`N_phase=235,235,763`.  Because the old value was never promoted, no theorem or
certificate is demoted.

An unrestricted minimum-area experiment attempted early in RL261 was exploratory
and is not evidence for the promoted result.  The final certificate uses the
ordered full-phase/rank-defect congruence instead.

## Mechanical verifier correction during closeout

The first frozen verifier draft enumerated integral defect quotients but omitted
an explicit filter for the inherited theorem condition `N_phase == 3 (mod 8)`
in one summary assertion.  Closeout added the condition explicitly.  All exact
RL261 pair counts, phase classes, and death depths were unchanged.  This was a
verifier-completeness repair, not a mathematical change.

## Naming discipline

The selector parameter `n=6` is denoted `NSEL` in the verifier.  The full-phase
quotient is denoted `N_phase`/`N` and must not be confused with the selector
parameter.  Likewise selector determinant parameter `r=306` is distinct from
the internal rank/weight `rho=809`.
