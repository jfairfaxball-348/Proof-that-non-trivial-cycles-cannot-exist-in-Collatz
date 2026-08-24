Continue the Collatz R# RL branch from RL-9.

Canonical state:
- RL-L53 (RL-8): any disjoint two-edge path between `D`-divisible rotations reduces to `D|2^u +/-3^v`.
- RL-L56: Jacobi signature of `D=2^A-3^L` kills coprime plus resonance for even `L` and forces even determinant `k` for odd `L`.
- RL-L57: every coprime disjoint same-direction two-swap self-rotation has odd `k`; hence the coprime two-edge route is closed.
- RL-L58: the overlap `D=5` exception is also closed.
- RL-L59: opposite-direction two-swap self-rotations force `u/A=v/L`, making the required proper difference strictly smaller than `D`; this closes all opposite-direction cases for every gcd.
- RL-L60: when `gcd(A,L)=2`, the half determinant `k0=u(L/2)-v(A/2)` satisfies `|k0|<A/2`, while modulo `2^(A/2)+3^(L/2)` a plus resonance requires the opposite inequality unless `k0=0`; `k0=0` forces exact half repetition.
- RL-L61: therefore no primitive `D`-divisible word has a distinct rotation at non-cancelling transposition distance 2. Distance 1 was already excluded in RL-7, so every distinct primitive cycle rotation is at distance at least 3.
- Finite support only: plus resonances through `A<=2000` occur only at `(4,2,7)` and `(8,5,13)`.

Highest priority:
1. Start radius 3 from the exact `S` discrepancy, not from brute-force `Q`: mixed directions give `+/-1` and force `gcd(A,L)=1`; all-same directions give `+/-3` and force `gcd(A,L)|3`.
2. Derive the distinct three-edge weighted-change geometries after quotienting overlaps/cancellations. Seek a Jacobi/cubic-character obstruction or determinant system.
3. In parallel, use RL-L27/RL-L36/RL-L54 to prove a radius-3 exclusion only for the distinguished least-root/final-return rotations.
4. Revisit RL-L55 factor descent only through exact-balanced cuts suggested by RL-L59; bare `D0` descent remains refuted.
5. Keep the positive-density Christoffel displacement route alive; constant radius exclusions do not by themselves yield the needed `Omega(L)` gap.

Do not re-enumerate radius-2 paths. Maintain PROVED / EXTERNAL / FINITE-EVIDENCE labels. RL remains open unless an actual infinite contradiction is proved.
