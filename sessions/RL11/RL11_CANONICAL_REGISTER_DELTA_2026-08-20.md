# RL-11 Canonical Register Delta — 2026-08-20

| ID | Statement | Status |
|---|---|---|
| RL-L68 | In mixed radius 3 (`e=+1`), writing the three flow events cyclically as `-1,+1,-1` at `0<x<s`, the source bits satisfy the exact sliding-window identity `b_t=-sum_(r=1)^L g_(t-r)`. Binary solvability is equivalent to `0<x<s<=min(L,A-L)`. | **PROVED ANALYTIC THEOREM** |
| RL-L69 | The three RL-L67 mixed sparse trinomials are cyclic presentations of the single canonical congruence `1-rho^x+rho^s=0 (mod D)` in the RL-L68 triangle. | **PROVED ANALYTIC REDUCTION** |
| RL-L70 | Mixed `[2,1]` geometry forces `s=min(L,A-L)`. If `L<A/2`, the length-two move is `100->001`; if `L>A/2`, it is `110->011`. | **PROVED ANALYTIC THEOREM** |
| RL-L71 | The `L<A/2`, `s=L` boundary is impossible: canonical divisibility forces `D|2^(A-L+x)-1`, but the positive integer is strictly smaller than `D`. | **PROVED ANALYTIC THEOREM** |
| RL-L72 | Every remaining mixed canonical case has a nonzero resultant with `2X^L-1`; root-of-unity orthogonality + AM-GM gives `D<2^(A-L)3^(L/2)`, hence `D/2^A<(sqrt(3)/2)^L`. | **PROVED ANALYTIC THEOREM** |
| RL-L73 | The entire mixed radius-3 branch is impossible. LMN gives `L<52000` under RL-L72; exact scan leaves only five `(A,L)` barrier candidates and zero canonical congruence solutions. | **PROVED USING EXTERNAL LMN THEOREM + EXACT FINITE CERTIFICATE** |
| RL-L74 | In the coprime one-orbit same-direction branch, let `r=-m^-1 mod A`, so `3r=L+jA`. The source bit is `b_t=u_t-j`, where `u_t` is the multiplicity of three equal cyclic `r`-arcs from the three negative events. Binary solvability is exactly `u_t in {j,j+1}`. | **PROVED ANALYTIC STRUCTURAL THEOREM** |
| RL-F11 | Exact finite denominator-barrier scan for `L<52000` leaves only `(5,3)`, `(7,4)`, `(8,5)`, `(13,8)`, `(27,17)` in the coprime mixed branch; all 62 canonical triples on these pairs fail. | **FINITE CERTIFICATE USED WITH RL-L73** |
