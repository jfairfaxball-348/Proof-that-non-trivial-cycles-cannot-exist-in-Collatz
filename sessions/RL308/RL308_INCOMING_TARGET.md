# RL308 — negative-front-door fixed-residue scalar Gate-A target

Date prepared: 2026-09-13
Status: PREPARED, NOT STARTED

## Incoming classification

RL307 closes as

`R3_SHELL_THREE_UNIT_BOUND_D0_ODD_COLLAPSE_AND_NEGATIVE_FRONTDOOR_DEPENDENCY_REDUCTION_PROVED`.

Gate A remains open. RL307 did not prove the checkpoint-8 shell-owner theorem, O1, O2, `Bcal(8)<=3`, or any complete non-P front-door ceiling. It did, however, materially contract the sourcewise shell/scalar problem.

## Absolute objective

Exploit the exact RL307 reduction of the `(3,-28)` Gate-A source.

Let

- `X=(4,J=43,K=58)=(4,39) o W_4`, where `W_4=(0,K=4)`;
- `Y=(6,J=504,K=567)=P o R_4`, where `P=(2,K=6)` and `R_4=(4,K=81)`.

RL307 proves

`Bcal(3,-28) <= max(`
` Bcal(2,-17)+2,`
` Bcal(4,39)-6,`
` Bcal(X)-8,`
` Bcal(Y)-9 )`.

Therefore, under the already-required Gate-A ceilings

`Bcal(2,-17)<=1`,
`Bcal(4,39)<=3`,

the entire `(3,-28)` obligation follows if

`Bcal(X)<=11`
and
`Bcal(Y)<=12`.

Primary mission: prove these two fixed scalar ceilings, or replace them by a strictly smaller exact dependency reduction.

If both close, record explicitly that `(3,-28)` is no longer an independent Gate-A node conditional on the existing `(-17)` and `(4,39)` obligations.

## Exact inherited shell results

For `k>=2`, RL307 proves the all-depth tight-wall shell recurrence

`M_R3(k)=min(`
` 3+M_8(k),`
` inf_D [B_L(D)+M_LD(k)],`
` inf_D [B_R(D)+M_RWD(k)] )`

over odd `D>=3`, and therefore

`M_R3(k)>=M_8(k)-3`.

Using the inherited checkpoint-2 recurrence,

`M_2(k)>=M_8(k)-2`.

These are available as scalar/shell sinks. They are not O1 and must not be silently strengthened to `M_R3>=M_8`.

## D0 status

RL307 removes, at shell level, the promoted F/S merger cylinders and all odd leading-P residuals from the independent D0 obstruction:

- odd F/S merger cylinders are at least `M_8+2`;
- even direct-merger cylinders are at least `M_8+4`;
- odd leading-P shared-state cylinders with `d>=5` are at least `M_8+16`;
- the `d=3` base has an equal-cost checkpoint-8 splice.

D0 is still open because the `A_d=F_d o Z` family and even trailing-P residuals remain.

The A-family has exact factorisations

`A_d=A_(d-1) o 8`,
`A_2=R_2`,
`A_d=R_2 o 8^(o(d-2))`,
`A_d=S_(d+1) o W_(-4)`.

Do not assume the fixed `-4` wall debt repays two units: RL307 gives an exact counterexample
`M_A4(2)=M_S5(2)=8`.

## Secondary negative-source lead

For `(2,-84)`, RL307 found an exact six-column affine/common-shadow fork:

- one cylinder becomes checkpoint 8 with six units of historical reserve;
- the complementary cylinder becomes the exact R3 relative problem with six units of reserve.

Both cylinders are safe using `M_R3>=M_8-3`; the remaining residues are exactly those where the synchronized checkpoint-8 shadow hits its wall.

This is preserved as a secondary lead, not a complete `(-84)` theorem.

## Route discipline

Do not default to:

- fixed-96 P/Q;
- universal P-insertion monotonicity;
- a large unweighted leading-P grammar;
- generic formal wall-debt amortisation;
- sequential checkpoint-8 cost-cap extension;
- same-endpoint O1/O2/P8.

For `X` and `Y`, use the very loose scalar allowances 11 and 12. A proof only needs a Bellman ceiling, not endpointwise checkpoint-8 ownership.

If an attempted fixed-context grammar proliferates without a decreasing weighted measure, stop it and instead build exact first-positive scalar reductions for `(-17)` and `(-84)` to shrink the Gate-A dependency graph.

## Scope

Gate A OPEN.
Gate B OPEN/frozen.
`Bcal(8)<=3` OPEN.
`Bcal(P)<=1` OPEN.
`Bcal(4,39)<=3` OPEN.
`Bcal(2,-17)<=1` OPEN.
`Bcal(2,-84)<=2` OPEN.
`Bcal(3,-28)<=3` OPEN, now reduced as above.
O1/O2/P8 OPEN.
Fixed-96 P/Q frozen.
Physical/resonance frozen at `a=7354673373747273032`.
Radius 6+ frozen.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.
