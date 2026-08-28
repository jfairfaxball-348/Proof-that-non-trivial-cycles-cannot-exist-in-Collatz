# Correction / demotion ledger through RL159

- RL156: notation-only repair: least state `M`, Bezout coefficient `u`.
- RL157: demote the incorrect `3T^L-2` phase normalization and `2^h_j 3^(H-h_j)` coefficient; replace by `2T^L-1` and `2^(H-h_j)`.
- RL158: retain `D | Res(2T^L-1,P_h)` as a necessary condition but demote it as a standalone ownership discriminator. Exact valid-grammar counterexample: `(A,L)=(13,8)`, `D=1631`, resultant `=D`, physical evaluation `=17`.
- RL158: introduce `3T^(A-L)-2` only as the correctly derived distinguished-root companion. This does not revive the demoted `3T^L-2` formula.
- RL159: the joint distinguished-root Sylvester/SNF/minor route is **demoted as an exclusion mechanism**. It exactly recovers physical evaluation: `SNF=diag(1,...,1,|D|)` and augmented maximal-minor divisor `gcd(|D|,P_h(rho))`. This is useful structural mathematics but supplies no independent contradiction leverage beyond `P_h(rho)=0 mod |D|`.
