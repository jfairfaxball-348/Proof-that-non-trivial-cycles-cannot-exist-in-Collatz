# RL304 — fixed-96 P/Q stack contraction and finite six-column residual grammar

Date: 2026-09-12
Base commit: `c53086fb5a429e433ef4a7ceca5cdce13347e35b`
Base tree: `bc363cc5e756c080fe04eba89bc5980e90542403`

## 1. Classification and scope

Final classification:

`FIXED_96_PQ_STACK_CONTRACTION_AND_TWELVE_FACTOR_SIX_COLUMN_RESIDUAL_GRAMMAR_PROVED`

RL304 does **not** prove O1

`m_R3(E) >= m_8(E)`

for every positive even checkpoint `E`. It does not prove the universal P/8 identity, `Bcal(P)<=1`, checkpoint-8 excess-one, Gate A, Gate B, or global non-trivial-cycle exclusion.

The session does meet RL304's allowed structural-success outcome by replacing the arbitrary-height P-through-Q-stack problem with one fixed `+96` translation family and then proving a finite twelve-factor residual grammar after six physical columns. This is a strict contraction of the local P/Q problem, but it is not yet a clearly convergent all-depth closure mechanism.

Per explicit user instruction, the successor is therefore a whole-project Gate-A strategic audit rather than an automatic continuation of the P/Q route.

## 2. Inherited setting

Use the RL303 definitions

- `P=(2,6)`,
- `Q=(2,18)`,
- `U=(1,6)`,
- `RW_D=Q^n o U` for `D=2n+1`,

with cascade product

`(a,A) o (b,B) = (a+b, 3^b A+B)`.

RL303 proved the physical one-cell commutation

`(P o Q)01110 = Q o P`

at cost 14 and the Q-return family

`Q 0(10)^r110=Q`

at cost 2.

## 3. Exact fixed-96 stack contraction

For `n>=1` define

`C_n = Q^(n-1) o P o Q`

and

`T_n = Q^n o P`.

The exact power formula is

`Q^n = (2n, 9(9^n-1)/4)`.

Direct cascade algebra gives

`boxed: C_n = (2n+2, (3^(2n+4)-441)/4)`

and

`boxed: T_n = (2n+2, (3^(2n+4)-57)/4)`.

Hence for every `n>=1`,

`boxed: K(T_n)-K(C_n)=96`.

Equivalently, with formal wall translation `H_96=(0,96)`,

`boxed: T_n = C_n o H_96`.

This is the key all-depth contraction of RL304. The apparent problem of commuting P through arbitrarily many Q cells has a context-independent algebraic defect of exactly 96.

Important qualification: this does **not** revive generic integer-wall-debt amortisation. RL303 proved that generic linear-credit debt transport is false. The new theorem concerns one fixed defect on the rigid special family `C_n`.

## 4. Exact six-column finite residual grammar

Pair the physical states `C_n` and `T_n=C_n o H_96` and feed them the same external input columns.

As long as their K-difference is even, they have the same parity, hence the same canonical output bit and the same physical depth. If a common column has output bit `y`, the K-difference updates exactly by

`h' = 3^y h / 2`.

Starting from `h_0=96`, after five common columns with source outputs `y_1,...,y_5`,

`h_5 = 96*3^(y_1+...+y_5)/2^5 = 3^m`

where

`m = 1 + y_1+...+y_5 in {1,2,3,4,5,6}`.

Thus after five common columns the arbitrary stack context has collapsed to one of six odd defects

`3, 9, 27, 81, 243, 729`.

On the sixth common external input, the paired K-values have opposite parity, hence opposite canonical output bits.

If the source output is `0`, then

`boxed: T'_n = C'_n o F_m`

with

`F_m = (1, 3(3^m+1)/2)`.

If the source output is `1`, then

`boxed: C'_n = T'_n o G_m`

with

`G_m = (1, 3(1-3^m)/2)`.

Therefore the infinite family reduces after six physical columns to exactly twelve fixed depth-one factors:

`F_m` K-values:

`6, 15, 42, 123, 366, 1095`

and `G_m` K-values:

`-3, -12, -39, -120, -363, -1092`.

For `n>=3`, all six common columns are automatically physical because the initial depth is `2n+2>=8` and six columns cannot force either side through the physical wall before the cut. The portable verifier also checks every six-bit word for `n=1..100`; the low-n cases are retained as finite regression/base evidence rather than needed for the all-depth legality argument.

## 5. Exact relative historical accounting

During each of the six columns, both paired physical states have the same depth at the start of the edge. Therefore their historical edge costs are identical.

Hence

`boxed: relative historical cost through the six-column cut = 0`.

No formal depth-zero factor is evolved through fictitious negative-area edges. The factorization into `F_m` or `G_m` is performed after the sixth physical column, consistent with RL295 wall normalization.

## 6. Exact physical witnesses retained

Besides the inherited one-cell witness, RL304 found exact physical whole-stack witnesses:

- `n=1`: `01110`, length 5, cost 14;
- `n=2`: `00101110001`, length 11, cost 53;
- `n=3`: `010011111001001001`, length 18, cost 127;
- `n=4`: `100011101110111000001`, length 21, cost 187;
- `n=5`: `100001110101010000001110`, length 24, cost 260;
- `n=6`: `0110100000111110110010001`, length 25, cost 339;
- `n=7`: `1001111100110001100001010110`, length 28, cost 413.

These are exact replayable witnesses from `C_n` to `T_n`. They are finite evidence only; RL304 does not promote a recurrence or all-n witness language from them.

A separate Q-return-compositional construction, stronger structurally but more expensive, was found through `n=6`:

- `n=1`: `01110`, length 5, cost 14;
- `n=2`: `00101110001`, length 11, cost 53;
- `n=3`: `001011000111101010001`, length 21, cost 143;
- `n=4`: `000011010100100011111100100`, length 27, cost 249;
- `n=5`: `011010001000110110000111110001001`, length 33, cost 373;
- `n=6`: `101110000011001110010101101100100101011100`, length 42, cost 582.

For `n=2` the outer Q returns physically to Q and emits `01001101001`, after which `P o Q` reaches `Q o P`. For `n=3` the outer Q likewise returns physically before the residual stack commute. These compositional witnesses motivated the fixed-defect theorem but are not themselves an all-depth proof.

## 7. Failed recurrence / barrier evidence

The compositional data at `n=3,4,5` suggested the tempting pattern

`length = 6n+3`

and

`cost = 9n^2+43n-67`.

That extrapolation predicts length 39 and cost 515 at `n=6`. The exact compositional witness found at `n=6` has length 42 and cost 582.

Therefore no such recurrence is promoted. This is an explicit warning against reading a global grammar from three local samples.

Likewise, bounded shortest-path work through `n=7` shows short exact translations but does not by itself give a well-founded all-depth mechanism.

## 8. Immediate finite residual leads

Two of the twelve `F_m` factors touch distinguished Bellman states immediately:

- `F_1=(1,6)=U`, and `F_1 --1--> (1,9)=8` at zero edge area;
- `F_2=(1,15)`, and `F_2 --0--> (2,27)=R3`.

The complete one-column formal/physical scratch table is frozen in `RL304_SCRATCH_FREEZE.md`.

These observations make the twelve-state grammar promising, but RL304 does not prove that all twelve factors are checkpoint-8 owned with the required credit. Therefore O1 remains open.

## 9. Strategic interpretation

RL304 has objectively reduced the local P/Q obstruction:

`arbitrary Q-stack commutation`

becomes

`fixed +96 translation on C_n`

and then

`twelve fixed depth-one residual factors after six equal-cost physical columns`.

However, this remains another finite normal form rather than a proof that the residual complexity decreases under iteration. There is not yet a demonstrated well-founded parameter that forces termination at checkpoint 8 or a smaller-wall owner.

Under the user's explicit material-change criterion, this is not sufficient to give the P/Q route automatic priority in the next session.

## 10. Verification

Portable verifier:

`sessions/RL304/verification/verify_rl304_fixed96.py`.

It checks:

- the closed form for `Q^n`, `C_n`, and `T_n` through `n=1..100`;
- the exact fixed `+96` defect;
- every one of the 64 six-bit common prefixes for every `n=1..100`;
- the twelve `F_m/G_m` factor formulas whenever the six-column paths are physical;
- zero relative six-column historical cost;
- all seven exact whole-stack witness words;
- all six exact compositional witness words;
- the `F_1 -> 8` and `F_2 -> R3` immediate transitions.

The finite loops are regression/certificate checks against the analytic algebra, not substitutes for an O1 proof.

## 11. Exact remaining proof state

Still open:

- O1: `m_R3(E)>=m_8(E)` all depth;
- the remaining O2 sectors;
- universal `m_P(E)=m_8(E)+2`;
- `Bcal(P)<=1` / checkpoint-8 excess-one;
- RL296 non-P front-door residuals;
- Gate A;
- Gate B;
- global non-trivial-cycle exclusion.

Frozen:

- P/Q route at the exact fixed-96 / twelve-factor frontier above;
- RL301 physical/resonance route at external selector frontier `a=7354673373747273032`;
- Radius 6+;
- separate Lean formalisation.

## 12. Successor

The successor is **RL305 — whole-project Gate-A strategic convergence audit**.

RL305 must not simply continue the P/Q calculation. It must reconstruct the project by eras, compare the logical burden before and after each major programme, identify repeated obstructions under coordinate changes, test whether O1/P8 is stronger than Gate A actually needs, search cross-era combinations and shortcuts, define falsifiable convergence/pivot criteria, and rank the highest-probability routes to an actual Gate-A proof.

The P/Q route remains fully frozen and resumable after that audit.
