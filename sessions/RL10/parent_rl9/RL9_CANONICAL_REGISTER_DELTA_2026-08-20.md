# RL-9 Canonical Register Delta — 2026-08-20

| ID | Statement | Status |
|---|---|---|
| RL-L56 | For `D=2^A-3^L>1`, `(2/D)=(-1)^L`, `(-1/D)=(-1)^(L+1)`, `(3/D)=(-1)^(A+L+1)`. A coprime plus resonance is impossible for even `L`; for odd `L` it forces `k=uL-vA` even. | **PROVED ANALYTIC THEOREM** |
| RL-L57 | A coprime disjoint same-direction two-swap self-rotation has odd determinant `k`. For odd `A,L`, after orienting right moves, `k=A-2U` with `U=((A-L)/2)u mod A`. | **PROVED ANALYTIC THEOREM** |
| RL-L58 | The exceptional overlap factor `5` cannot occur in a coprime self-rotation: `D=5` forces odd `A,L`, and the orbit equation forces the local factor to be `100`, not `110`. | **PROVED ANALYTIC THEOREM** |
| RL-L59 | Every opposite-direction two-swap self-rotation forces an exact balanced cut `u/A=v/L`; the resulting proper difference `2^u-3^v` lies strictly between `0` and `D`. | **PROVED ANALYTIC THEOREM** |
| RL-L60 | For `gcd(A,L)=2`, write `(A,L)=(2a,2ell)`. A same-direction self-rotation has half determinant `k0=u ell-v a` with `|k0|<a`. But divisibility modulo `D+=2^a+3^ell` requires `|k0|>=a` unless `k0=0`; the zero case is an exact half-repeat. | **PROVED ANALYTIC THEOREM** |
| RL-L61 | No primitive `D`-divisible full parity word has a distinct rotation reachable by two non-cancelling adjacent cyclic transpositions. Thus primitive cycle rotations have transposition distance at least 3. | **PROVED ANALYTIC THEOREM** |
| RL-F9 | Exact plus-resonance scan through `A<=2000` finds only `(4,2,7)` and `(8,5,13)`. | **EXACT FINITE EVIDENCE** |

## Canonical strategic change

The one-edge route was closed in RL-7; the two-edge route is now closed completely. Do not spend further computation on radius-2 paths.

The next transposition target begins at radius 3, where the `S` discrepancy is automatically in `{+/-1,+/-3}` and hence immediately restricts `gcd(A,L)` to `1` or `3` depending on direction signature.
