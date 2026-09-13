# RL307 scratch freeze

Date: 2026-09-13
Status: FROZEN SUPPORTING SCRATCH. `RL307_REPORT.md` and `RL307_PROOF_AND_SCOPE.md` control theorem status.

## 1. R3 tower exploration and route barrier

RL307 initially pursued a uniform owner for first exits from the R3 all-zero tower.

At `T_d=(d,K=3^d)`:

- input 0 gives `T_(d+1)` at cost `d-1`;
- input 1 gives `S_d=(d-1,K=(3^d-1)/2)` at cost `d-1`.

For even `d=D+1`, one more bit lands on the two RL295 tight walls:

`T_d 10 = L_D`,
`T_d 11 = RW_D`.

For odd `d=D`, the two branches are

`T_d 10 = L_D`,
`T_d 11 = RW_(D-2)`,

with the `RW_(D-2)` sibling carrying D extra historical units over its earlier tight R3 ingress.

For even d, the L sibling carries D+1 extra units over its earlier tight ingress.

This showed that the attempted uniform tower-exit route simply reconstructs the old tight-wall obstruction. The useful outcome was the exact shell recurrence and the coarse `-3` bound, not a new endpointwise O1 proof.

## 2. Early local tower observations

Before the general zipper was recognized, exact checks included:

- d=4 tower exit to L3/RW3;
- d=5 exit to L5/RW3;
- d=6 exit to L5/RW5;
- several checkpoint-8 same-state owner words.

These are superseded by the all-depth recurrence and should not be used as separate proof obligations.

## 3. Common-right-shadow diagnostics

Directly translating a checkpoint-8 affine witness through the seed relation

`g_seed(u)=g_8(u+7)`

often breaks ballot positivity. Thus the naive same-length common-shadow exchange is not universal.

For R3 one has

`g_R3(u)=g_8(9u+2)`,

but the relative process hits exactly the tight-wall event. This is another expression of the same obstruction, not a separate convergence mechanism.

## 4. D0 A-family

The exact identities

`A_d=A_(d-1)o8`,
`A_d=R_2 o 8^(o(d-2))`,
`A_d=S_(d+1)oW_(-4)`

were found while trying to close the remaining D0 source.

The fixed `-4` wall shift looked promising, but exact shell computation gives

`M_A4(2)=M_S5(2)=8`.

Therefore the hoped-for automatic two-unit wall repayment is false. Do not revive it without an ancestry-sensitive theorem.

## 5. `(2,-84)` partial affine fork

In common-shadow coordinates, the source has a six-column fork with two exact safe cylinders:

- `000001` reduces to checkpoint 8 with six historical units of reserve;
- `000000` reduces to the R3 relative problem with six reserve.

Since `M_R3>=M_8-3`, both cylinders are safe for the `(-84)` shifted shell requirement.

The other legal residues are exactly those where the synchronized checkpoint-8 shadow reaches a component wall. No complete prefix cut was obtained.

## 6. `(3,-28)` first-positive frontier

Exact first-positive exits, preserved with witness words:

- `110000 -> (2,3)` cost 3;
- `110100 -> (2,1)` cost 4;
- `1110100 -> (3,2)` cost 5;
- `100 -> (4,21)` cost 5;
- `00 -> (5,104)` cost 5;
- `111000 -> (3,6)` cost 6;
- `010 -> (3,8)` cost 7;
- `10100 -> (3,11)` cost 7;
- `0110 -> (3,9)` cost 9.

The nonpositive minimum-cost quotient has exactly 19 states.

## 7. `(2,-17)` overlap used by the final reduction

Closeout verification reconstructs eight first-positive exits:

- `(2,3)` cost 2, word `01000`;
- `(3,2)` cost 2, word `00`;
- `(2,1)` cost 3, word `01100`;
- `(3,11)` cost 5, word `110000`;
- `(3,8)` cost 6, word `1000`;
- `(3,9)` cost 7, word `1101000`;
- `(3,6)` cost 8, word `11011101000`;
- `(4,25)` cost 9, word `10100`.

The first seven states except `(4,25)` overlap the `(-28)` frontier, and the largest source-cost disadvantage of `(-17)` relative to `(-28)` on them is exactly 2, at `(3,6)`.

## 8. Fixed leading-P grammar diagnosis

An intermediate reduction expressed `(-28)` through several fixed leading-P contexts such as `P o P`, `P o R2`, `P o B3`, and others.

Several contexts admitted early same-state simplifications, but the combined shallow grammar began proliferating. It was stopped under the RL305/RL306 convergence discipline.

The cross-front-door `(-17)` absorption and the final two fixed residues are strictly smaller and supersede this grammar as the recommended route.

## 9. Exact final residues

`X=(4,J=43,K=58)=(4,39)oW_4`, `W_4=(0,K=4)`.

`Y=(6,J=504,K=567)=P o R_4`, `R_4=(4,K=81)`.

Required loose scalar ceilings for RL308, conditional on existing `(-17)` and `(4,39)` Gate-A obligations:

`Bcal(X)<=11`,
`Bcal(Y)<=12`.
