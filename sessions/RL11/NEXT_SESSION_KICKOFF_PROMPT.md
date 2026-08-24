Continue the Collatz R# RL research from the attached RL-11 handover bundle.

Do not restart the mixed radius-3 branch. RL-11 closes it completely.

Inherited high-value facts:

1. primitive `D`-divisible cycle rotations have transposition distance at least 3 (RL-9);
2. exact radius 3 has support `[3]`, `[2,1]`, or `[1,1,1]` (RL-L62);
3. connected `[3]` is analytically impossible (RL-L63);
4. mixed radius 3 has the canonical form `1-rho^x+rho^s=0` with `0<x<s<=min(L,A-L)` (RL-L68/RL-L69);
5. the full mixed radius-3 branch is impossible (RL-L73), using a published Laurent–Mignotte–Nesterenko two-logarithm estimate plus an exact finite certificate;
6. in the coprime one-orbit same-direction branch, three negative events generate three equal cyclic `r`-arcs and the source bits satisfy `b_t=u_t-j`, `3r=L+jA` (RL-L74);
7. RL-L67 still gives the same-direction sparse form `sigma^a+3sigma^b+9sigma^c=0`.

Highest priority: combine RL-L74 with the `1,3,9` sparse form to obtain a canonical same-direction gap geometry and seek a resultant/linear-forms contradiction.

Second priority: derive the `gcd(A,m)=3` three-orbit analogue.

Third priority: close the `gcd(A,L)=3` cubic-cofactor branch and prove any survivor is an exact third-repeat, leaving only the already-excluded trivial `(10)^3` repetition.

Guardrails: RL remains open; radius 3 remains open in same-direction branches; preserve the external LMN dependency explicitly rather than calling RL-L73 self-contained.
