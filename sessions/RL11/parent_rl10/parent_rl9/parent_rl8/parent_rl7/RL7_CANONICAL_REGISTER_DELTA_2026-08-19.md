# RL-7 Canonical Register Delta — 2026-08-19

This delta supplements RL-6.

| ID | Claim | Status |
|---|---|---|
| RL-L46 | At the least rational anchor, every proper compressed prefix obeys `rho W_j/W_0 < A_j < W_j/W_0`; the denominator defect satisfies the sharpened reciprocal bound `D/2^A < e_close/W_0 + sum e_i/W_(i+1) < sum 1/W_j`. For physical plateau starts this becomes a reciprocal-state sum; closing odd `t` gives `D/2^A>1/[2(R#+1)]`, strengthened to `>7/[8(R#+1)]` when `n_close>=2`. | **PROVED ANALYTIC THEOREM** |
| RL-L47 | `gcd(C_r,D)` is invariant under rotation. Once all RL-6 boundary gates pass, every rational anchor has the same reduced odd denominator `D_res=D/gcd(C_r,D)`, and realization is equivalent to `D_res=1`. | **PROVED ANALYTIC THEOREM** |
| RL-L48 | If a cyclic compressed word is `V^m`, `m>=2`, its affine fixed point is already the fixed point of `V`; a primitive orbit cannot have an exact repeated compressed word. | **PROVED ANALYTIC THEOREM** |
| RL-L49 | For full parity words with fixed `(A,L)`, one adjacent `10<->01` transposition changes the numerator by `2^a3^b`, a unit modulo `D=2^A-3^L`. For every nontrivial `D>1`, two `D`-divisible words cannot be adjacent in the transposition graph. | **PROVED ANALYTIC THEOREM** |
| RL-L50 | Every non-Christoffel rotation class satisfies `Q_min < Q_Chr - 3^(L-1)/4`. Hence a cycle minimum obeys `R# < 1/(2^(A/L)-3) - 3^(L-1)/(4D) = 1/[3(e^(Lambda/L)-1)] - 1/[12(e^Lambda-1)]`. RL-L52 makes this internal for every primitive nontrivial positive integer cycle. | **PROVED ANALYTIC THEOREM** |
| RL-L51 | A nonconstant binary word has a nontrivial rotation differing by one cyclic adjacent transposition iff its rotation class is primitive Christoffel. Such a shift `m` forces `gcd(A,m)=gcd(A,L)=1` and `Lm=+/-1 (mod A)`. | **PROVED ANALYTIC THEOREM** |
| RL-L52 | Primitive Christoffel parity words cannot satisfy `D|Q` for `D>1`: D-divisibility propagates to all rotations, RL-L51 supplies an adjacent self-rotation, and RL-L49 forbids both endpoints from being D-divisible. Nonprimitive Christoffel words are exact repetitions and cannot encode a primitive cycle. Thus every primitive nontrivial integer cycle is internally non-Christoffel. | **PROVED ANALYTIC THEOREM** |
| RL-X11 | New exact verifier audits the prefix/suffix sandwich, reciprocal defect, rotation gcd, adjacent-transposition unit edge, quantitative Christoffel gap through `A<=14` in the cycle-slope strip, repeated-word descent, and the one-edge/primitive-Christoffel classification. | **EXACT FINITE CERTIFICATE** |

## Reformulated obligations

- **RL-O3 / k=0 global:** still `D|C_good`, now equivalently `D_res=1` with a rotation-invariant residual denominator.
- **RL-O7 / extension theorem:** the one-edge distinguished-rotation attack is exhausted—it is exactly the primitive Christoffel case. Highest priority moves to **weighted transposition paths of length >=2**, or a positive-density Christoffel displacement forced by root/return grammar.
- **RL-O5 / boundary:** remains closed structurally by RL-6; boundary gates are finite local conditions, not the global obstruction.
- **RL-O2 / k>0:** unchanged and separate.
