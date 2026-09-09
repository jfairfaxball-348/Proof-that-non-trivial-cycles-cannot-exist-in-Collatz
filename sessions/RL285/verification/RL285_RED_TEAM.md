# RL285 closeout red team

Result: PASS

Scope: proof-state classification, exact identities, finite-certificate scope, and forbidden overclaims.

## Checks

1. **False scratch invariant isolated.** The discarded claim `nu_2(J)<=H-d+1` fails at genuine reachable `(2,4,2)`. It is explicitly unpromoted and no inherited theorem depends on it.

2. **Global Gate-A theorem not claimed.** The statement `nu_2(K-1)<=H+d-1` is kept conjectural globally. Only the exhaustive `H<=22` raw closure is classified as an exact finite certificate.

3. **Finite certificate is gap-free over its stated range.** The portable verifier performs exhaustive BFS from `(1,-13,0)` using only the normalized exact recurrence and the sole cutoff `H<=22`; no `J`, word-length, or depth cutoff is imposed. It reproduces 3,837,389 total states and 584,154 positive states, with zero positive violations and exactly three equality states.

4. **Candidate specializes correctly.** At `d=1`, `K-1=J` and `H+d-1=H`, so the all-depth candidate specializes exactly to the authoritative Gate-A checkpoint target.

5. **No local-induction overclaim.** Explicit locally legal/residue-admissible fake first entrances are recorded for all four branch types. Therefore the candidate is not presented as a reachability-blind local invariant.

6. **Shadow scalar independence rejected.** `C_w(-7)+1=(S_w-6)/q_w` is recorded, so shifted shadows are recognized as zero-mass coordinates rather than a new independent scalar. The relaxed `k=25,H=3` scalar construction is kept as a barrier only.

7. **High-divisibility reconstruction scope checked.** The proof uses prefix dominance plus backward integrality of odd-coefficient affine half-steps. It is not stated for arbitrary unrelated endpoint polynomials.

8. **Ferrers rigidity checked.** The portable verifier exhaustively regresses equal-weight prefix-dominant pairs through length 8 and confirms the shifted-shadow rank identity and `nu_2(W_x-W_y)=b_*` whenever displacement is nonzero.

9. **Carry peeling not overstated.** First-carry reconstruction is promoted as a bridge to the first genuine excursion entry. Iteration is explicitly classified as reconstructing the existing excursion structure, not as a proof of Gate A.

10. **Terminal extension scope checked.** Signed area `H-k` is an exact reformulation of the RL283 forced extension. No cyclic-minimality or selector extremality theorem is assumed.

11. **Residual unchanged.** Gate A remains open at `k>=25`, odd, with `H_can<k`. Gate B, fifth selector, and Radius 6+ remain frozen.

12. **No global Collatz conclusion.** RL285 does not claim non-trivial-cycle exclusion.
