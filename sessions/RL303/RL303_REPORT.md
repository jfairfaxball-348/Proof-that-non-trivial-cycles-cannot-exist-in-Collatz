# RL303 — dyadic wall lattice, translation normal form, P-wall reduction, and P/Q commutation

Date: 2026-09-12
Base commit: `7a83d6fb5344acc4e477ae5d19fed9414534acda`

## 1. Classification and scope

Final classification:

`DYADIC_WALL_LATTICE_TRANSLATION_NORMAL_FORM_P_FIRST_WALL_REDUCTION_AND_GENERIC_LINEAR_DEBT_BARRIER_WITH_PQ_COMMUTATION_PROVED`

RL303 does **not** prove O1

`m_R3(E) >= m_8(E)`

for every positive even checkpoint `E`. Consequently O2, the all-depth P/8 checkpoint identity, `Bcal(P)<=1`, checkpoint-8 excess-one, and Gate A remain open.

Gate B remains open/frozen. The RL301 physical/resonance route remains frozen at the externally certified selector frontier `a=7354673373747273032`. Radius 6+ remains frozen. Lean formalisation is separate. No global non-trivial-cycle exclusion is claimed.

This session nevertheless succeeds under the incoming RL303 criterion: it proves several all-depth wall/refactorisation theorems, identifies a decisive barrier to generic linear wall-debt amortisation, and isolates a new fixed-cell P/Q commutation route for the remaining leading-P obstruction.

## 2. Notation

Use K-coordinate states and the canonical recurrence frozen in RL294/RL302. Let

- `P=(2,K=6)`;
- checkpoint `8=(1,K=9)`;
- `U=(1,K=6)`;
- `R2=(2,K=9)`;
- `Q=(2,K=18)`;
- tower `Rt(d)=(d,3^d)`.

For odd `D>=3`, write the tight wall families as

`L_D=(D,(5*3^D-3)/4)`,

`RW_D=(D,(9*3^D-3)/4)`.

The explicit name `RW` is used here to avoid the RL302 notation collision between the tower family and the right tight-wall family.

The RL302 credits remain

`B_L(D)=(D^2+D-6)/2`,

`B_R(D)=(D^2+3D-4)/2`.

Cascade composition is

`(a,A) o (b,B)=(a+b,3^b A+B)`.

## 3. Exact checkpoint-8 wall entries have uniform +3 debt

For every odd `D>=3`, checkpoint 8 reaches the tower state `Rt(D)` by

`001 0^(D+1)`

with exact cost

`(D^2-3D+6)/2`.

Appending `10` reaches `L_D` at cost

`(D^2+D)/2 = B_L(D)+3`.

Appending `011` reaches `RW_D` at cost

`(D^2+3D+2)/2 = B_R(D)+3`.

Thus direct checkpoint-8 wall entry misses the RL302 tight historical credits by a uniform three units, independent of wall depth. This is a useful normalization but does not prove the wall inequalities.

## 4. General dyadic wall lattice

For odd `D>=3` and `t>=0`, define

`C_(D,t)=(1,K=3(4t+1)2^(D-2)+3)`

and

`W_(D,t)=(D,((4t+5)3^D-3)/4)`.

Then the exact pure-zero lift is

`boxed: C_(D,t) 0^D = W_(D,t)`

with cost

`boxed: (D^2-D-2)/2`.

The first two cells are exactly

`W_(D,0)=L_D`,

`W_(D,1)=RW_D`.

Hence the tight L/R walls are the first two cells of one infinite dyadic wall lattice rather than unrelated exceptional states.

## 5. Fixed Q-cell factorisation of the right-wall family

The fixed cell

`Q=(2,18)`

and terminal cell

`U=(1,6)`

give, for `D=2n+1`,

`boxed: RW_D = Q^n o U`.

The inherited RL302 factorisation is, in collision-free notation,

`boxed: L_D = R2 o RW_(D-2)`.

This explains why genuine `D -> D-2` wall peeling can be represented by finite quotient/cascade transducers.

## 6. Translation-invariant adjacent-wall normal form

The RL302 L/R run-length identity is not special to `L_D/RW_D`.

Let `S=(d,K)` and

`S^+=(d,K+3^d)`.

For every `k>=0`, whenever the displayed paths are legal,

`boxed: S 0 1^k 01 = S^+ 1^(k+1) 00`,

with the `S^+` continuation cheaper by exactly `k+2`.

The complementary sibling is

`boxed: endpoint(S 0 1^k 00) = P o endpoint(S^+ 1^(k+1) 01)`,

again with continuation difference `k+2`.

Applying this to the dyadic lattice gives, for every `t>=0`,

`W_(D,t) 0 1^k 01 = W_(D,t+1) 1^(k+1)00`,

and the complementary leading-P sibling between adjacent lattice cells.

The quotient proof uses the formal unit translation state `(0,-1)`: one paired `0/1` column reaches the universal run gateway `(1,0)`, common `1/1` columns leave it fixed, and the final two columns either return to identity or produce the fixed factor `P`.

## 7. Four all-depth D -> D-2 merger families

The same quotient gateway yields four parameter families for every odd `D>=5` whenever the displayed prefixes are legal:

`boxed: L_D 10 1^k 00 = RW_(D-2) 0000 1^(k-2)01` for `k>=2`,

with source-minus-owner continuation cost `4-k`;

`boxed: L_D 010 1^k 00 = L_(D-2) 00000 1^(k-2)01` for `k>=2`,

with difference `6-k`;

`boxed: RW_D 1100 1^k 00 = L_(D-2) 00000 1^(k-1)01` for `k>=1`,

with difference `2-k`;

and

`boxed: RW_D 0100 1^k 00 = RW_(D-2) 000000 1^(k-2)01` for `k>=2`,

with difference `7-k`.

Combining these continuation differences with the RL302 historical credit increments gives large positive induction windows. They close substantial wall cylinders recursively but do not form a complete prefix cut, so O1 remains open.

## 8. Leading-P siblings reduce to positive reserve plus integer wall debt

Consider a leading-P sibling

`X=P o Y`.

Propagate a physical future of `X` through the left P factor until the **first** column at which that factor reaches formal depth zero. Before that first wall hit the factor depths are all positive. By the exact cascade area ledger, the source side therefore accumulates a strictly positive relative historical reserve before any rejected-depth debt appears.

Immediately before the rejected descent the P factor is at a genuine depth-one positive-even checkpoint of the form

`(1,K=2a+1)`, equivalently `J=2a`, `a>=1`.

The rejected descent produces the formal integer wall debt

`H_a=(0,a)`.

RL295 wall normalization then absorbs this depth-zero component into the adjacent positive factor at zero additional historical cost. Therefore every leading-P sibling has the exact structural reduction

`boxed: leading P -> positive accumulated reserve + normalized integer wall debt H_a`.

This is a structural localization theorem, not generic P-insertion monotonicity.

## 9. Generic linear-credit wall-debt amortisation is false

A generic theorem asserting that a linear-in-D historical reserve can absorb arbitrary integer wall debt is impossible.

For every `n>=1`, set

`D=6n+3`.

The fully legal physical pair

`W_(D,4) 1^(3n)`

and

`W_(D,0) (110)^n`

satisfies, at their endpoints,

`d_owner-d_source=n`,

`K_source=K_owner+4*3^(d_owner)`,

while the exact source-minus-owner historical cost is

`boxed: -3n(n-1)/2`.

Thus a fixed four-cell wall separation admits arbitrarily large **quadratic** adverse paired cost even though `D` grows only linearly in `n`.

This does not refute O1, because Bellman ownership may use a different route. It does decisively refute the proposed generic proof strategy “integer wall debt + linear D-credit always suffices.” Any successful proof must exploit the special tight-wall/Q-stack ancestry before that generic debt cycle develops.

## 10. Exact P/Q commutation route

The new fixed-cell route is the exact physical identity

`P o Q = (4,72)`,

`Q o P = (4,168)`,

and

`boxed: (P o Q) 01110 = Q o P`

at exact historical cost `14`.

This moves the troublesome P factor through one Q cell without releasing it into a generic rejected-tube debt problem.

The Q cell also has an all-r return family. For every `r>=0`,

`boxed: Q 0(10)^r110 = Q`

at exact cost `2`, with propagated output word

`boxed: 00(01)^r11`.

This is the principal successor lead. Since

`RW_D=Q^((D-1)/2) o U`,

a finite commutation-and-return grammar that repeatedly pushes P through the Q stack could replace the false generic wall-debt amortisation strategy. The historical wall-credit increment

`B_R(D)-B_R(D-2)=2D+1`

also eventually exceeds the fixed single-cell physical commutation cost 14.

No all-depth repeated-stack theorem is claimed in RL303.

## 11. Corrections and rejected shortcuts

1. The frozen RL302 notation `L_D=R2 o R_(D-2)` is correct only when `R_(D-2)` denotes the **right tight wall**, not the tower. RL303 uses `RW` to remove this collision.
2. The simple dyadic-checkpoint sufficient condition for the L wall is false already at the first nontrivial tested case and is not promoted as a proof route.
3. A root-level P-renewal analysis is unnecessary on the source prefix `R3 011`, because checkpoint 8 already reaches the identical `RW_3` wall one unit more cheaply: `R3 011` costs 7 while `8 01001` costs 6.
4. Generic integer-wall-debt linear amortisation is refuted by Section 9.
5. A six-cell lattice rebase of P was algebraically attractive but no universal cheap owner access to the required higher cells was proved; it is not promoted.

## 12. Verification

The portable structural verifier

`sessions/RL303/verification/verify_rl303_structural.py`

checks:

- 49 odd-depth instances of the exact checkpoint-8 +3 wall-entry formulas through `D=99`;
- 980 generalized dyadic wall lifts (`D=3..99` odd, `t=0..19`);
- 49 fixed-Q / inherited wall factorisations;
- 14,816 adjacent-wall merger instances and 14,756 leading-P siblings;
- 2,703 legal instances of the four `D -> D-2` merger families;
- the physical quadratic debt counterfamily for `n=1..100`;
- the exact P/Q commutation identity;
- 101 Q-return instances (`r=0..100`);
- the direct `R3 011` / checkpoint-8 `01001` splice at `RW_3`.

These finite loops are regressions against the analytic formulas, not substitutes for their all-depth algebraic derivations.

## 13. Exact remaining target

O1 remains the primary target.

The recommended next route is **not** unrestricted debt normalization. It is a finite transducer problem on the actual right-wall factorisation

`RW_D=Q^n o U`:

1. derive all legal P/Q swap and Q-return/refactorisation macros needed after the first swap;
2. prove that their language moves a leading P factor through the full `Q^n` stack, or isolate the smallest exact residual;
3. track physical historical cost against the RL302 wall credits at each peel;
4. only if this closes, return to the remaining L-wall cylinders and then finish O1;
5. if O1 closes, immediately resume the already-contracted O2 obligations before claiming the P/8 identity.
