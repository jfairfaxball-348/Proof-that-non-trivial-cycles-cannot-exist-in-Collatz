# RL-6 Canonical Register Delta — 2026-08-19

This delta supplements RL-5.

| ID | Claim | Status |
|---|---|---|
| RL-L42 | For every admissible cyclic compressed word, the height word `h_j=n_j-mu_(j+1)` has positive total `L`, so a cycle-lemma rotation exists with every nonempty suffix height sum positive. At that rotation the final numerator term is the unique 3-adic minimum, hence `v3(C_good)=M` automatically even with exact-boundary exits and arbitrary declared cancellation depths. | **PROVED ANALYTIC THEOREM** |
| RL-L43 | If `v3(C_j)=M`, every non-boundary edge preserves `v3(C_(j+1))=M` automatically. At an exact boundary `r=n`, `mu'=n+c`, the next signature is exact iff `kappa=c`, where `kappa=v3(C_hat_j+2^(M+n)D((2^t-1)/3^n))`; this requires only a residue modulo `3^(c+1)`. | **PROVED ANALYTIC THEOREM** |
| RL-L44 | For an arbitrary admissible cyclic word, choose a good rotation. A positive periodic integer anchor orbit exists iff `D|C_good` and every exact-boundary cancellation gate passes. Generic RL-L41 is the zero-boundary special case. | **PROVED ANALYTIC THEOREM** |
| RL-L45 | For the minimum rational anchor candidate `W_*`, with `E_mu=sum (2/3)^mu_next(1-2^-t)`, `e_close/W_* < D/2^A < E_mu/W_* < P/W_*` for `P>1`. For k=0, `W_*=R#+1` and `e_close=1-2^-t_close`; with external `R#>=2^71`, `D/2^A<E_mu/(2^71+1)`. | **PROVED ANALYTIC THEOREM + EXTERNAL COROLLARY** |
| RL-X10 | New verifier audits 6,370 symbolic good rotations, 6,370 boundary-gate equivalences, 4,062 denominator-defect instances, and exhaustively checks the generalized criterion on the declared `P<=3,n,t<=6,c<=2` domain. Only three trivial `W=2` repetitions survive. | **EXACT FINITE CERTIFICATE** |

## Reformulated obligations

- **RL-O3 / k=0 global:** both generic and exact-boundary words now reduce to `D|C_good`, with boundary words carrying only a finite list of explicit 3-adic gates. The global numerator/denominator obstruction is unified.
- **RL-O5 / boundary:** the structural boundary-cancellation exception is closed; it is no longer an open all-rotation valuation problem.
- **RL-O7 / extension theorem:** still critical. The next infinite theorem must obstruct `D|C_good` using the root departure/return gates or a denominator descent/lift mechanism.
- **RL-O2 / k>0:** unchanged from RL-5; extend repeated-order rigidity beyond the `2R#` horizon using cumulative reciprocal-height control.
