# RL307 closeout

Date: 2026-09-13
Base commit: `de25370eb0c81d29b6f82a8ef1133d72c6096f0d`
Base tree: `12350f36b2a1d1b1e70b094143aa67582494b668`
Successor: RL308

## Final classification

`R3_SHELL_THREE_UNIT_BOUND_D0_ODD_COLLAPSE_AND_NEGATIVE_FRONTDOOR_DEPENDENCY_REDUCTION_PROVED`

## Outcome

RL307 does not prove the full checkpoint-8 shell-owner theorem. It does produce objective Gate-A dependency contraction.

The session proves an exact all-depth shell recurrence for R3 and the unconditional coarse bound

`M_R3(k)>=M_8(k)-3`.

Together with the inherited checkpoint-2 recurrence this gives

`M_2(k)>=M_8(k)-2`.

Those coarse inequalities are already sufficient to remove the promoted D0 direct-merger families and odd leading-P families from the independent shell obstruction, without assuming O1.

The unresolved D0 A-family is reorganized as a repeated checkpoint-8 cascade with one fixed `-4` wall debt; a direct two-unit repayment theorem is explicitly falsified by `M_A4(2)=M_S5(2)=8`.

The strongest new front-door result is the exact `(3,-28)` scalar reduction

`Bcal(3,-28) <= max(`
` Bcal(2,-17)+2,`
` Bcal(4,39)-6,`
` Bcal((4,43))-8,`
` Bcal((6,504))-9 )`,

where

`(4,43)=(4,39)oW_4`,
`(6,504)=P o R_4`.

Thus the `(-28)` Gate-A node will become redundant, conditional on the already-existing `(-17)` and `(4,39)` obligations, if the two fixed loose ceilings

`Bcal(4,43)<=11`,
`Bcal(6,504)<=12`

are proved.

## Successor priority

RL308 should attack those two fixed scalar residues first. This is a strictly smaller task than the abandoned fixed leading-P grammar and much weaker than universal P-insertion or O1/P8.

If both close, eliminate the `(-28)` node from the active Gate-A dependency graph conditional on the existing `(-17)` and `(4,39)` nodes, then move to direct scalar reduction of `(-17)` / `(-84)`.

Do not resume fixed-96 P/Q or a large unweighted leading-P grammar by default.

## Verification

Fresh portable verifier:

`sessions/RL307/verification/verify_rl307_closeout.py`

Fresh output:

`sessions/RL307/RL307_FRESH_VERIFICATION.txt`

Result:

`RL307_CLOSEOUT_VERIFIER_GREEN`.

The verifier replays all load-bearing finite front-door certificates and broad parametric regressions for the analytic identities.

## Transport and catalogue

The session uses the repository's documented lossless-text transport convention. `SHA256SUMS.txt` is the internal manifest.

Knowledge catalogues are unchanged and therefore `stale/deferred`; they are not proof-state authority and do not block promotion.

## Scope

Gate A OPEN.
Gate B OPEN/frozen.
`Bcal(P)<=1` OPEN.
`Bcal(8)<=3` OPEN.
`Bcal(4,39)<=3` OPEN.
`Bcal(2,-17)<=1` OPEN.
`Bcal(2,-84)<=2` OPEN.
`Bcal(3,-28)<=3` OPEN, contracted as above.
O1/O2/P8 OPEN.
Physical/resonance frozen at `a=7354673373747273032`.
Radius 6+ frozen.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.
