Continue the Collatz R# RL branch from RL-7.

Canonical state:
- RL-6: arbitrary admissible compressed k=0 words reduce to `D|C_good` plus finite exact-boundary 3-adic gates.
- RL-L46: least-anchor all-prefix sandwich and reciprocal defect; always `D/2^A>1/[2(R#+1)]`, and `>7/[8(R#+1)]` if final `n_close>=2`.
- RL-L47: `gcd(C_r,D)` is rotation-invariant; define residual odd denominator `D_res=D/gcd(C,D)`. Realization iff `D_res=1` after boundary gates.
- RL-L48: exact repeated compressed words descend to their primitive block.
- RL-L49: adjacent parity `10<->01` transposition changes `Q` by a unit `2^a3^b mod D`; for nontrivial `D>1`, two D-divisible words cannot be adjacent.
- RL-L51: a binary word has a nontrivial rotation one cyclic adjacent transposition away iff it is a primitive Christoffel rotation class.
- RL-L52: combine RL-L51 + RL-L49 + rotation-invariance of `D|Q` to exclude primitive Christoffel parity words internally; nonprimitive Christoffel words are repetitions. Knight is no longer needed for this step.
- RL-L50: therefore every hypothetical primitive nontrivial integer cycle loses more than `3^(L-1)/4` from the Christoffel numerator, yielding
  `R# < 1/[3(e^(Lambda/L)-1)] - 1/[12(e^Lambda-1)]`.
  The one-move penalty is only ~`1/(4L)` relative, so it does not close the branch.

Highest priority:
1. Encode the full parity words of the root rotation, the first post-neutral rotation, the last-anchor rotation, and the root return using inherited RL-L27/RL-L36.
2. Compute/derive weighted adjacent-transposition paths between distinguished rotations, now explicitly starting at path length >=2. The one-edge case is exactly Christoffel and already exhausted. Seek a monotone/sign-controlled path whose exact weighted sum lies strictly between 0 and D.
3. In parallel, prove a lower bound on the **number/weight** of Christoffel corrections forced by root grammar. A positive-density displacement is needed; one correction is asymptotically too small.
4. Split `s=v2(R#+1)=2` from `s>=3`, and final `n_close=1` from `n_close>=2`.
5. Test residual-denominator descent for `gcd(A,L)>1` through `D_0=2^(A/g)-3^(L/g)`.

Do not broaden brute-force enumeration without tying it to one of these theorem targets. Maintain explicit PROVED / EXTERNAL / FINITE-EVIDENCE labels. RL remains open unless an actual infinite contradiction is proved.
