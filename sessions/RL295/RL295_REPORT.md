# RL295 report — exact wall normalization, `(4,39)` all-depth sector cut, and Q17 owner-tail splice

Date: 2026-09-11

## 1. Authority and scope

Incoming `main` / `BASE_HEAD`:

`e59bccbc0091b9a118fb63bc8677895ae02ab03b`

Incoming authority:

`authoritative/RL295_CANONICAL_CASCADE_WALL_DEBT_AND_P_OWNER_GATE_A_TARGET.md`

Incoming authority blob:

`52200054aca6c9e4df1f6c2d866831ca0c6d2e06`

Incoming `authoritative/START_HERE.md` blob:

`96415f8407e5a148faf778b8a7e811a98ed42922`

This session remained on the research front. No Lean-formalisation work was performed.

Gate A remains OPEN with exact residual

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector remains unscanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.

## 2. Frozen classification

`ZERO_DEPTH_WALL_NORMALIZATION_4_39_CUT_AND_Q17_OWNER_TAIL_PROVED`

The session made strong progress on RL295 Primary Targets A and B:

1. the formal depth-zero wall debt now has an exact normalization rule with no fictitious negative area;
2. the frozen RL294 `(4,39)=P o Z o Z` candidate is proved all-depth outside one exact early prefix;
3. the formerly infinite coefficient-tail obstruction is cut by an explicit P-owner certificate at `Q17`, leaving a finite pre-Q17 sector list.

The complete `(4,39)` Bellman obligation is **not** yet closed, because the surviving finite wall sectors still require authoritative owner/Bellman certificates.

## 3. Exact zero-depth wall normalization

Use K-coordinate cascade states `(d,K)` and RL294's product

`(a,A) o (b,B) = (a+b, 3^b A + B)`.

For a formal depth-zero wall component

`W_u=(0,u)`,

the following are exact algebraic identities:

`W_u o (b,B) = (b, B + 3^b u)`

and

`(a,A) o W_u = (a, A+u)`.

In particular `W_0=I` is the true identity and is quotiented immediately. Adjacent wall debts merge additively:

`W_u o W_v = W_(u+v)`.

### Area accounting

Suppose a synchronized column begins with factor depths `d_1,...,d_m`. The physical composite edge cost is

`(sum_i d_i)-1 = sum_i(d_i-1) + (m-1)`.

Wall normalization is performed **after** that edge. It preserves total depth and the exact composite K-coordinate and therefore costs zero additional historical area. A factor reaching depth zero is never subsequently charged with a fictitious `-1` edge.

Thus the nonzero rejected-tube debt is retained exactly as an integer K-shift in an adjacent positive-depth factor, while the formal identity disappears.

This meets RL295 Target-A requirements at the algebraic/min-plus level: exact physical state, exact area ledger, immediate identity quotient, nonzero debt retention, and no dependence on a chosen history gauge.

## 4. Double-E wall refactorization

RL294's formal transducer has

`E --0--> P` with propagated output `1`

and

`E --1--> I` with propagated output `0`.

Consider a synchronized state `A o E o E`. On the next column, regardless of the propagated bit produced by `A`, exactly one E becomes P and the other becomes I. Quotienting I gives the same normalized form

`A' o P`.

This is an exact physical-state identity, not a residue correction and not an extension that evolves a depth-zero factor through a rejected tube.

## 5. All-depth `(4,39)` sector cut

The hard RL292 front-door state is

`S=(4,39)=P o Z o Z`.

As long as the leading P factor emits propagated output `1`, both Z factors stay Z. At the first leading-P output `0`, both Z factors become E. A checkpoint-ending future cannot stop at that instant, so one further column applies the double-E refactorization.

The leading-P output-1 ray is

`P --1--> R_2`

and

`R_d --0--> R_(d+1)`

with `R_d=(d,K=3^d)`.

If the first leading-P output zero occurs from `R_d` (`d>=2`), the source prefix is

`1 0^(d-2) 1 epsilon`

and has exact source cost

`C_s(d)=(d^2+5d+2)/2`.

After the wall refactorization every non-immediate sector is one of two families, for odd `D>=3`:

`L_D=(D, K=(5*3^D-3)/4)`

or

`R_D=(D, K=(9*3^D-3)/4)`.

Explicit P-owner routes are:

`P -- 1 0^(D-2) 1 0 --> L_D`

with cost

`C_L(D)=(D^2+D-2)/2`,

and

`P -- 1 0^(D-1) 1 1 --> R_D`

with cost

`C_R(D)=(D^2+3D)/2`.

Comparing exact costs gives, in all four parity/epsilon cases,

`owner cost <= source cost + 1`.

The RL292 allowance for `(4,39)` is `source cost +2`, so every non-immediate sector closes by exact same-state P splicing.

The immediate two-bit cut is:

- `01 -> L_3=(3,K=33)` at source cost 6, with P-owner cost 5;
- `00 -> (5,191)` at source cost 6.

Therefore the unique residual sector of the all-depth `(4,39)` cut is exactly

`00 -> (5,191)`.

Equivalently,

`Bcal(4,39) <= max(Bcal(P)+2, Bcal(5,191)-6)`.

This proves the first bullet of RL295 Target B all-depth.

## 6. Exact Q17 P-owner certificate

Define the tower states

`Q_d=(d,K=2*3^d)`.

A fully replayable certificate now reaches `Q_17` from P.

### Stage 1: P to the odd boundary ladder

The frozen 262-column word in the portable verifier takes

`P=(2,3)`

to

`O_17^(7)=(1,J=458753)`

at exact historical cost 29.

Its complementary zero-height boundary exit (`x=1`) reaches

`B_17^(7)=(1,J=688130)`

at no additional cost.

### Stage 2: one positive excursion to Q17

From `B_17^(7)`, the 40-column word

`0010110010010111011101010000000100000000`

reaches `Q_17` at exact cost 154.

After the forced launch, this excursion never returns to depth one before its endpoint.

Thus the concatenated 303-column exact certificate gives

`m_P(Q_17) <= 183`.

The portable verifier freezes the complete 262-column first-stage word and the 40-column excursion word, so the result does not depend on conversational scratch.

## 7. All-depth Q-tail splice

There is an exact tower recurrence

`Q_d --10--> Q_(d+1)`

with cost `2(d-1)`.

Appending `(10)^(d-17)` to the Q17 owner certificate proves for every `d>=17`

`m_P(Q_d) <= d^2 - 3d - 55`.

The distinguished `(6,807)` spine reaches Q17 via

`1000000101000101`

at exact cost 169, then follows the same tower recurrence. Hence its source cost to Q_d is

`c_807(Q_d)=d^2-3d-69`.

Therefore for every `d>=17`

`m_P(Q_d)-c_807(Q_d) <= 14`.

The `(6,807)` branch has 31 units of owner credit in the inherited reduction, so this splice has 17 units of spare margin. Once the source reaches Q17, **every arbitrary future suffix** is P-owned by exact same-state splicing.

Thus the formerly infinite post-Q17 tail is completely eliminated.

## 8. Finite pre-Q17 cut for `(6,807)`

Before the source word

`1000000101000101`

reaches Q17, the sixteen complementary first-deviation sectors are exactly:

| state `(d,J)` | source cost |
|---|---:|
| `(6,736)` | 5 |
| `(5,621)` | 10 |
| `(6,1462)` | 16 |
| `(7,3801)` | 23 |
| `(8,10558)` | 31 |
| `(9,30471)` | 40 |
| `(10,89737)` | 50 |
| `(12,530626)` | 61 |
| `(11,401454)` | 72 |
| `(13,1792803)` | 84 |
| `(12,1501654)` | 96 |
| `(13,3446175)` | 109 |
| `(14,8752393)` | 123 |
| `(16,45372670)` | 138 |
| `(15,35839500)` | 153 |
| `(17,150532452)` | 169 |

These states are a finite authoritative cut. No claim is made in this closeout that all sixteen are already P-owned.

## 9. Verification

Portable verifier:

`sessions/RL295/verification/verify_rl295_wall_owner.py`

Frozen output:

`sessions/RL295/verification/RL295_FAST_VERIFIER_OUTPUT.txt`

The verifier checks:

- 1,331,352 zero-depth wall-normalization identities;
- 118 `(4,39)` parametric sector instances through leading-ray depth 60;
- the complete 262-column P -> O17 certificate, cost 29;
- the exact O17 -> B17 zero-height complementary exit;
- the 40-column B17 -> Q17 positive excursion, cost 154;
- the complete 303-column P -> Q17 certificate, cost 183;
- the `(6,807)` spine to Q17 at source cost 169;
- all sixteen pre-Q17 side sectors;
- Q_d propagation and constant owner lag 14 through d=80.

The analytic formulas prove the parameter ranges all-depth; finite loops are regressions against the formulas, not substitutes for them.

## 10. Important work preserved but not promoted

During RL295 several useful finite owner searches further contracted `(5,191)`, `(5,201)`, `(6,733)`, `(6,949)`, and `(6,807)`. Some individual witness words were not retained before closeout. Those numerical contractions are therefore frozen in `RL295_SCRATCH_FREEZE.md` as **unpromoted leads**, not used in the authoritative proof state.

Likewise, the repunit family `E_d`, its two wall/P normal forms, the dyadic boundary ladders, and several candidate ladder-propagation routes are preserved as secondary exact/exploratory material. They became unnecessary for the all-depth post-Q17 closure and should not displace the shorter Q17 splice unless needed again.

## 11. Consequences and exact remaining target

RL295 strongly succeeds on Target A and partially on Target B:

- the wall-refactorization calculus exists and is exact;
- the complete nonexceptional `(4,39)` sector family is closed;
- `(4,39)` has one exact early residual `(5,191)`;
- a major infinite tail arising in the frozen continuation is converted into a finite cut.

But the complete `(4,39)` inequality is not yet proved. The next session must produce replayable certificates for the remaining finite wall sectors, beginning from `(5,191)`, and only then propagate to the other RL292 front-door states.

`Bcal(P)<=1` remains open.

Gate A remains open.
