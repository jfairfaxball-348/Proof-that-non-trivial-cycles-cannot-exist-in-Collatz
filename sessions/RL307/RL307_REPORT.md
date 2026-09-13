# RL307 report — shell contraction, D0 residual collapse, and negative-front-door dependency reduction

Date: 2026-09-13
Base commit: `de25370eb0c81d29b6f82a8ef1133d72c6096f0d`

Primary classification:

`R3_SHELL_THREE_UNIT_BOUND_D0_ODD_COLLAPSE_AND_NEGATIVE_FRONTDOOR_DEPENDENCY_REDUCTION_PROVED`

Gate A remains open. Gate B remains separate/open/frozen. Fixed-96 P/Q remains frozen. Lean formalisation is separate. No global non-trivial-cycle exclusion is claimed.

## 1. Incoming mission and outcome

RL307 inherited the shell identity

`M_seed(k)=3+min(M_R3,M_8,M_D0,M_439,M_-17-2,M_-84-1,M_-28)`

for `k>=2` and was asked to prove or falsify checkpoint-8 shell ownership.

The full shell-owner theorem was not proved. Instead RL307 obtained three exact structural contractions:

1. the R3 shell problem reduces exactly to checkpoint 8 plus the two tight-wall families and yields the unconditional all-depth coarse bound `M_R3>=M_8-3`;
2. that coarse bound is already strong enough to remove large promoted portions of the D0 residual without O1;
3. the negative source `(3,-28)` has a finite exact first-positive front door and its Gate-A scalar obligation reduces to the existing `(-17)` and `(4,39)` obligations plus two fixed scalar residues.

These are genuine contractions. They do not prove Gate A.

## 2. Exact R3 shell recurrence

Let

`L_D=(D,K=(5*3^D-3)/4)`,
`RW_D=(D,K=(9*3^D-3)/4)`

for odd `D>=3`, with historical credits

`B_L(D)=(D^2+D-6)/2`,
`B_R(D)=(D^2+3D-4)/2`.

RL302's tower zipper classifies every nonempty R3 checkpoint future by its first tower departure. RL307 observes that every non-tight sibling reaches the same wall state as an earlier R3 tight prefix but with strictly larger cost, so it can be removed min-plus globally.

Using the shallow boundary/checkpoint-2 renewal for the `d=3` sibling, for every relevant `k>=2`:

`boxed:`
`M_R3(k)=min(`
` 3+M_8(k),`
` inf_(D odd>=3) [B_L(D)+M_LD(k)],`
` inf_(D odd>=3) [B_R(D)+M_RWD(k)] )`.

RL303 already gives exact checkpoint-8 wall entries at costs

`B_L(D)+3`, `B_R(D)+3`.

Therefore each wall term is at least `M_8(k)-3`, and hence

`boxed: M_R3(k)>=M_8(k)-3`.

This is weaker than O1 and does not imply `M_R3>=M_8`.

## 3. Checkpoint-2 shell consequence

The inherited exact recurrence

`M_2(k)=1+min(M_R3(k),M_8(k))`

immediately gives

`boxed: M_2(k)>=M_8(k)-2`.

This two-unit coarse bound is enough for several D0 families.

## 4. D0 promoted-family contraction without O1

Use RL302 notation

`F_d=(d-1,K=(3^d-3)/2)`,
`S_d=(d-1,K=(3^d-1)/2)`.

D0 reaches `F_d` at exact cost

`C_F(d)=d^2-d-2`,

while checkpoint 2 reaches `S_d` at

`C_2(d)=d(d-1)/2`.

### Odd direct-merger cylinders

On every legal promoted odd normal-form cylinder

`F_d 00 1^j 01 = S_d 1^(j+2)00`

the S continuation is cheaper by `j+3`. Therefore the D0 history to the common state exceeds the checkpoint-2 history by

`d(d-1)/2+j+1 >=4`.

Thus every such shell continuation costs at least

`M_2(k)+4 >= M_8(k)+2`.

### Even direct-merger cylinders

The promoted even F/S merger has the S continuation cheaper by exactly two. The full D0/checkpoint-2 history difference is

`d(d-1)/2 >=6`

for reachable even `d>=4`, hence these cylinders cost at least

`M_8(k)+4`.

### Odd leading-P residuals

For `d=D+2>=5`, RL302 proves the odd F/S leading-P residual and the R3 tight-wall residual are literally the same physical state, while the D0 history is more expensive by

`(D^2+7D+8)/2 >=19`.

Therefore RL307's `M_R3>=M_8-3` gives a shell margin at least 16. The `d=3` base is directly reached from D0 and checkpoint 8 at equal cost 4.

Consequently these promoted D0 families are no longer independent shell-owner obstructions.

Important non-claim: D0 itself is not closed. The A-family and even trailing-P residuals remain.

## 5. A-family exact factorisation and barrier

For

`A_d=(d,K=(3^(d+1)-9)/2)`

RL307 proves algebraically

`A_2=R_2`,
`A_d=A_(d-1) o 8`,
`A_d=R_2 o 8^(o(d-2))`.

Also

`boxed: A_d=S_(d+1) o W_(-4)`

with formal wall shift `W_(-4)=(0,K=-4)`.

This reduces the parameterised family to one fixed wall debt, but the tempting two-unit repayment theorem is false. Exact shell search gives

`M_A4(2)=8`,
`M_S5(2)=8`.

Thus one cannot infer `M_A4(2)>=M_S5(2)+2`. The fixed wall debt is a real residual, consistent with RL294's rejected-tube pricing barrier.

## 6. Exact first-positive front door for `(3,-28)`

Positivity is forward invariant. Exhausting the nonpositive physical graph from `(3,-28)` gives exactly 19 minimum-cost nonpositive states and nine minimum-cost first-positive exits:

| word | state `(d,J)` | cost |
|---|---|---:|
| `110000` | `(2,3)=P` | 3 |
| `110100` | `(2,1)` | 4 |
| `1110100` | `(3,2)` | 5 |
| `100` | `(4,21)` | 5 |
| `00` | `(5,104)` | 5 |
| `111000` | `(3,6)` | 6 |
| `010` | `(3,8)` | 7 |
| `10100` | `(3,11)` | 7 |
| `0110` | `(3,9)` | 9 |

Every higher-cost revisit of a nonpositive physical state is Bellman dominated by its minimum-cost history, so this is a complete scalar front door.

## 7. Seven exits are absorbed by `(2,-17)`

The corresponding nonpositive graph from `(2,-17)` has 27 minimum-cost nonpositive states and eight first-positive exits. Seven are shared with the `(-28)` front door:

| state | `c_-28` | `c_-17` | difference |
|---|---:|---:|---:|
| `(2,3)` | 3 | 2 | -1 |
| `(2,1)` | 4 | 3 | -1 |
| `(3,2)` | 5 | 2 | -3 |
| `(3,6)` | 6 | 8 | 2 |
| `(3,8)` | 7 | 6 | -1 |
| `(3,11)` | 7 | 5 | -2 |
| `(3,9)` | 9 | 7 | -2 |

Hence every shared exit contributes at most

`Bcal(2,-17)+2`

to `Bcal(3,-28)`.

Only

`U=(4,21)` and `V=(5,104)`

remain.

## 8. Final exact scalar reduction for `(3,-28)`

The U children are

`U --0,cost3--> X=(4,43)`,
`U --1,cost3--> (4,39)`.

The V children are

`V --0,cost4--> Y=(6,504)`,
`V --1,cost4--> (4,52)`,

and

`(4,39) --0,cost3--> (4,52)`.

Therefore

`boxed:`
`Bcal(3,-28) <= max(`
` Bcal(2,-17)+2,`
` Bcal(4,39)-6,`
` Bcal(X)-8,`
` Bcal(Y)-9 )`.

The `Bcal(4,39)-6` term comes specifically from the V->(4,52) branch combined with the cheaper `(4,39)->(4,52)` ingress.

The two fixed residues factor exactly as

`X=(4,39) o W_4`, `W_4=(0,K=4)`,

and

`Y=P o R_4`, with `P=(2,K=6)`, `R_4=(4,K=81)`.

Thus, under the already-required Gate-A ceilings

`Bcal(2,-17)<=1`,
`Bcal(4,39)<=3`,

it suffices for the entire `(-28)` obligation to prove only

`Bcal(X)<=11`,
`Bcal(Y)<=12`.

This is the preferred RL308 target.

## 9. Preserved partial `(-84)` lead

RL307's affine/common-shadow analysis found an exact six-column fork for `(2,-84)`:

- one cylinder reduces to checkpoint 8 with six units of historical reserve;
- the complementary cylinder reduces to the exact R3 relative problem with six units of reserve.

Both cylinders are safe using `M_R3>=M_8-3`.

The remaining residues are exactly those where the synchronized checkpoint-8 shadow encounters its component wall. No complete `(-84)` theorem is claimed.

## 10. Route barriers and rejected shortcuts

- Uniform tower-exit domination is not a new route: the first exits reproduce the inherited tight-wall obstruction.
- Direct translated seed/8 common-shadow paths can fail ballot legality.
- Generic P-insertion monotonicity remains false.
- The A-family fixed `-4` wall debt does not automatically repay two area units.
- A simultaneous shallow grammar for the fixed leading-P contexts arising from `(-28)` proliferated and was stopped rather than expanded without a decreasing measure.
- No checkpoint-8 shell-owner theorem was proved.
- No `Bcal` Gate-A source ceiling was closed.

## 11. Verification

Portable verifier:

`sessions/RL307/verification/verify_rl307_closeout.py`.

Fresh output:

`sessions/RL307/RL307_FRESH_VERIFICATION.txt`.

It checks the R3 zipper/tight-credit identities, checkpoint-8 +3 wall entries, D0 F/S margins, A-family factorisations and the A4/S5 counterexample, both finite first-positive front doors, their seven shared exits, and the final two-residue `(3,-28)` reduction.

## 12. Exact remaining proof state

OPEN:

- Gate A and Gate B;
- `Bcal(8)<=3`;
- `Bcal(P)<=1`;
- all seven RL305 scalar obligations in the literal dependency graph;
- full checkpoint-8 shell ownership;
- full D0;
- `(4,39)`, `(-17)`, `(-84)`, `(-28)`;
- O1/O2/P8 and checkpoint-8 excess-one.

CONTRACTED:

- R3 has the unconditional shell lower bound `M_R3>=M_8-3`;
- large D0 F/S families are shell-safe as above;
- `(-28)` conditionally reduces to two fixed scalar residues once the existing `(-17)` and `(4,39)` obligations are supplied.
