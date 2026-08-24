# Collatz R-sharp RL14 handover — 2026-08-20

## Baseline
Start from `baseline/Collatz_Rsharp_RL11_Handover_2026-08-20.zip` for the full inherited project state.
The `rl12/`, `rl13/`, and `rl14/` directories contain the delta results produced after RL11.

## Closed after RL11
1. `gcd(A,m)=3` same-direction radius-3 branch: closed (RL12).
2. `j=0, P3, [1,1,1]` same-direction one-orbit interior: closed (RL13).
3. `j=1, P2, [1,1,1]` coprime one-orbit interior: closed analytically (RL14).
4. `j=1, P3` interiors with any two equal simplex gaps: closed (RL14).

## Structural normal form
The canonical P2/P3 one-orbit equations can be expressed coefficient-free as
`1 + theta^a + theta^(a+b) = 0` with `a+b+c=0`, equivalently an S-unit 3-cycle under `T(u)=-1-u^{-1}`.

## Strongest live target
Attack the **scalene `j=1, P3, [1,1,1]` interior**, where the simplex gaps `x,y,z` are pairwise distinct.
Use the RL14 facts:
- `B=A-L`.
- `D > 4^B` for every coprime `j=1,P3` parameter pair (LMN-dependent finite certificate included).
- For `H(X)=4X^(x+y)+6X^y+9`, the resultant `Res(8X^B-27,H)` is nonzero unless `x=y=z=B/3`; coprimality excludes that singularity.
- Any two-equal-gap case is impossible via the primitive-cube-root descent.

A natural next objective is to obtain a **quantitative lower bound on gap imbalance** or an **upper bound on the nonzero side-B resultant** strong enough to contradict `D>4^B`. Try difference variables such as `p=y-x`, `q=z-y` (after cyclic/order normalization), and exploit subtraction of conjugate/cyclic forms to factor terms like `tau^p-1` and `tau^q-1`.

## Other live branches
- coefficient-5 P3 `[2,1]` boundary;
- the `j=2` P2 lift;
- separate `gcd(A,L)=3` cubic-cofactor branch.

Do not revisit the mixed radius-3 branch, the `gcd(A,m)=3` branch, `j=0 P3` interior, `j=1 P2` interior, or the two-equal-gap `j=1 P3` cases except to reuse their lemmas.

## Verification
Run the Python verifiers in each delta directory. Logs from the successful runs are included beside them.
