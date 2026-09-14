# RL323 correction and demotion ledger

Date: 2026-09-14
Status: FROZEN WITH RL323 CLOSEOUT

## C1 — invalid cyclic wrap in unpromoted matched-rank scratch

An early RL323 scratch construction defined a normalized odd-rank defect and derived a correct interior recurrence. It then asserted a cyclic wrap recurrence that treated the final odd-rank transition as returning within the same row.

That is invalid: the physical wrap swaps the two balanced rows. Therefore the proposed cyclic one-crossing theorem built from that wrap is withdrawn.

This claim was never promoted and changes no prior authoritative theorem.

## C2 — post-crossing tail was not yet a matched-rank displacement

A later checkpoint obtained a bound on a genuine post-crossing tail and described it too strongly as a matched-rank displacement.

The tail bound itself was a physical ordinary-tail statement, but the matched-rank label was not yet justified at that checkpoint.

RL323.3 repairs this by cutting immediately before the actual first `H`-carry sign transition and identifying

`beta=v[v_j:u_j]`,
`r=u_j-v_j`,
`wt(beta)=h`.

The final promoted displacement bound is therefore the genuine matched-rank bound

`r<=77265916075`

in the inherited externally conditional first-survivor scope.

## C3 — no promotion of the unfinished residual-class refinement

Immediately before closeout, a possible refinement separating the two parity types of the first crossing was only identified as a next calculation. No theorem from that unfinished refinement is promoted.

The frozen frontier ends at RL323.5 in `RL323_PROOF_LEDGER.md`.
