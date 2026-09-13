# RL307 proof and scope ledger

Date: 2026-09-13
Classification: `R3_SHELL_THREE_UNIT_BOUND_D0_ODD_COLLAPSE_AND_NEGATIVE_FRONTDOOR_DEPENDENCY_REDUCTION_PROVED`

## Promoted analytic results

### P1. Tight-wall shell recurrence for R3

For every relevant `k>=2`,

`M_R3(k)=min(`
` 3+M_8(k),`
` inf_(D odd>=3)[B_L(D)+M_LD(k)],`
` inf_(D odd>=3)[B_R(D)+M_RWD(k)] )`.

Reason: first tower departure is unique; RL302's zipper gives tight and cross wall branches; every cross branch reaches exactly the same wall state as an earlier tight R3 history with positive extra cost and is Bellman dominated. The shallow d=3 branch enters the inherited 2/3/5/8 renewal component.

### P2. Coarse R3 shell ownership

RL303 gives

`8 -> L_D` at `B_L(D)+3`,
`8 -> RW_D` at `B_R(D)+3`.

Therefore

`M_R3(k)>=M_8(k)-3`.

No stronger pointwise inequality is claimed.

### P3. Checkpoint-2 shell bound

From the inherited exact recurrence

`M_2=1+min(M_R3,M_8)`,

P2 gives

`M_2(k)>=M_8(k)-2`.

### P4. D0 promoted-family shell contractions

On every legal odd F/S merger cylinder the D0 route exceeds the checkpoint-2 route by

`d(d-1)/2+j+1>=4`,

so its shell cost is at least `M_8+2`.

On every promoted even direct-merger cylinder the history difference is

`d(d-1)/2>=6`,

so its shell cost is at least `M_8+4`.

For odd leading-P residuals with `d=D+2>=5`, the exact D0/R3 shared-state splice has historical gap

`(D^2+7D+8)/2>=19`,

hence shell cost at least `M_8+16`. The d=3 base has an equal-cost checkpoint-8 splice.

These are branch-family contractions, not a proof of `M_D0>=M_8`.

### P5. A-family factorisations

`A_2=R_2`,
`A_d=A_(d-1) o 8`,
`A_d=R_2 o 8^(o(d-2))`,
`A_d=S_(d+1) o W_(-4)`.

### P6. Fixed wall-repayment counterexample

Exact minimum-shell computation:

`M_A4(2)=M_S5(2)=8`.

Therefore the candidate universal inequality
`M_Ad(k)>=M_S(d+1)(k)+2`
is false.

### P7. `(3,-28)` finite first-positive front door

The minimum-cost nonpositive physical quotient contains 19 states and has exactly the nine first-positive exits listed in `RL307_REPORT.md`.

This is a complete Bellman front door because positivity is forward invariant and a higher-cost revisit of the same physical state has the same future and is dominated by the minimum-cost revisit.

### P8. Seven-exit absorption by `(2,-17)`

The `(-17)` minimum-cost nonpositive quotient has 27 states and eight first-positive exits. Seven coincide with `(-28)` exits with ingress-cost difference at most +2 on the `(-17)` side.

Therefore those seven `(-28)` contributions are bounded by

`Bcal(2,-17)+2`.

### P9. Final `(3,-28)` scalar dependency reduction

Let

`X=(4,43)=(4,39) o W_4`,
`Y=(6,504)=P o R_4`.

Then

`Bcal(3,-28) <= max(`
` Bcal(2,-17)+2,`
` Bcal(4,39)-6,`
` Bcal(X)-8,`
` Bcal(Y)-9 )`.

Consequently, conditional on the existing Gate-A obligations
`Bcal(2,-17)<=1` and `Bcal(4,39)<=3`, the `(-28)` obligation follows from only

`Bcal(X)<=11`,
`Bcal(Y)<=12`.

## Exact finite certificates

The portable verifier independently reconstructs:

- 19 nonpositive quotient states and nine first-positive exits for `(-28)`;
- 27 nonpositive quotient states and eight first-positive exits for `(-17)`;
- all seven shared exits and cost differences;
- `M_A4(2)=M_S5(2)=8`.

These are exact finite certificates used only at their stated scope.

## Supporting but unpromoted leads

- `(2,-84)` six-column affine fork: two cylinders are safe via checkpoint 8 / R3 with six reserve, but the wall-hit remainder is unresolved.
- Direct common-right-shadow translation `u -> u+7` is not globally ballot legal.
- Finite shell data continue to suggest `M_R3=M_8+3` on visible shells, but no all-depth equality is promoted.
- Fixed leading-P context cleanup around `(-28)` was exploratory and stopped when the grammar proliferated.

## Corrections / non-claims

No inherited theorem is demoted.

Do not infer any of:

- `M_R3>=M_8`;
- O1;
- full checkpoint-8 shell ownership;
- `M_D0>=M_8`;
- `Bcal(D0)<=3`;
- `Bcal(3,-28)<=3`;
- `Bcal(2,-17)<=1`;
- `Bcal(2,-84)<=2`;
- `Bcal(4,39)<=3`;
- `Bcal(8)<=3`;
- Gate A.

## Scope unchanged

Gate A OPEN.
Gate B OPEN/frozen.
Physical/resonance frozen at `a=7354673373747273032`.
Radius 6+ frozen.
Lean formalisation separate.
