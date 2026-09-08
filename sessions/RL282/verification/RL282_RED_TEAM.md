# RL282 closeout red-team note

Date: 2026-09-08

Result: **PASS**

This is a closeout proof-state/scope red team, not new research.

Checks:

1. **Gate scope.** RL282 does not claim Gate A globally. The authoritative residual remains `k>=5`, `k` odd, `H_can<k`.
2. **Local-versus-global scope.** The pure-zero final-tail family is explicitly local. It proves exact legal positive blocks beginning at a constructed checkpoint `J_in`; it does not prove that `J_in` is globally reachable from the original `J=-13` trajectory at insufficient accumulated height.
3. **One-zero shell, `h=1`.** The proof of `nu_3(J_out)=1` for height one uses the inherited reachable-state condition `J_in mod 3 in {0,2}` at `d=1`. The statement is not silently extended to arbitrary non-reachable integer inputs.
4. **Boundary suffix scope.** The affine suffix identity is algebraically valid for compositions of the boundary affine maps; its dynamical use is stated only for legal zero-height `d=1` suffixes.
5. **Height-digit inequality.** `nu_3(N_w(k))-r` is an upper bound on the actual preceding one-zero height. RL282 does not claim equality in general because the odd quotient in the one-zero identity may carry additional factors of `3`.
6. **Primitive-root step.** The unique exponent class modulo `3^n` is supported analytically by the exact order `ord_(3^n)(2)=2*3^(n-1)`, derived by LTE from `nu_3(4^(3^m)-1)=1+m`.
7. **Pure-zero construction.** The defining congruence makes `nu_3(2J_0+3)=h` exactly, not merely at least `h`; the normalized quotient is odd and nonzero modulo `3`, giving `J_in` even, `J_in==0 (mod 3)`, and `nu_2(J_in+4)=h`. Choosing a sufficiently large representative of the unique `q` residue class ensures `J_in>0`.
8. **Boundary legality of the family.** During the `0^q` tail,
   `T_0^t(J_0)=2^(q-t)(2^k-1)+1`; every state before the terminal is positive odd, so the entire boundary tail is legal.
9. **Scale/mass/F scope.** The zero-mass and `F` formulas are exact conditional identities for the local block at a given terminal scale `Q_T`. They show insufficiency of the inherited scalar budgets; they do not assert existence of a retained global path with arbitrary chosen `Q_T`.
10. **Neutral-loop barrier.** The positive `J=3` loop demonstrates that zero count is not uniformly priced by total mass. This is a route barrier, not a new terminal or cycle classification.
11. **Local 2-adic monotonicity.** The example `30 -> 24` is used only to reject a blockwise proof of `nu_2(J)<=H`. The global checkpoint inequality remains unproved and is not promoted.
12. **Finite-vs-analytic status.** The large `H<=26` scratch search and observed safety through odd `k=27` are recorded as unpromoted evidence. No authoritative residual contraction depends on that computation.
13. **Inherited scope.** Gate B remains open/frozen; the fifth selector and Radius 6+ are untouched. No global non-trivial-cycle exclusion is claimed.
14. **Successor isolation.** RL283 is exactly one generation ahead and targets the upstream reachability/state-height obstruction identified by RL282, without treating conjectural `nu_2(J)<=H` or `J<=2^H` as established.

No mathematical correction or demotion of the inherited authoritative state is required.

No promoted RL282 claim requires demotion.
