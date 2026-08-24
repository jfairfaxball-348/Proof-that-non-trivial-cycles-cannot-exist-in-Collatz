# Proof-chain audit checklist

Use this as a red-team checklist.  The goal is not to preserve the current narrative; it is to find the first unsupported implication if one exists.

- [ ] Reconstruct the global RL target and the role of `D|Q` from the earliest baseline definitions.
- [ ] Recheck RL-L48 repetition/descent and exactly what “primitive” excludes.
- [ ] Recheck RL7--RL9 distance-1/distance-2 exclusions, including cancellation conventions for transposition paths.
- [ ] Recheck RL10 exact-radius-3 flow classification and support partition exhaustiveness.
- [ ] Recheck RL11 mixed-branch closure, including the LMN theorem statement/constants and finite certificate coverage.
- [ ] Recheck RL12 `gcd(A,m)=3` closure from its verifier/baseline derivation.
- [ ] Recheck RL13 `j=0,P3` interior closure.
- [ ] Recheck RL14 `j=1,P2` and equal-gap `j=1,P3` closures.
- [ ] Recheck RL15 short-defect identity, nonzero resultant theorem, LMN cutoff, and exact parameter certificate.
- [ ] Recheck RL16 `j=0` coefficient-5 minimax resultant and continued-fraction reduction.
- [ ] Recheck RL16 `j=1` coefficient-5 short-defect boundary resultant and its uniform margin.
- [ ] Recheck RL16 `j=2,P2` short relation, cyclic largest-gap omission, uniform margin, and the two direct survivors.
- [ ] Reconstruct the complete post-RL16 radius-3 case tree; explicitly list every branch and its closing lemma.
- [ ] Re-derive RL-L104 symbolically from first principles; verify the phase cancellation and the use of the cubic cofactor.
- [ ] Determine whether `C|Q` is the strongest justified modulus or whether the sparse relation can be promoted to full `D`.
- [ ] Independently reproduce any claimed skew-zero/uniqueness scan before citing it.
- [ ] Search for counterexamples to the pure arithmetic converse without imposing binary rotation geometry.
- [ ] Search separately for counterexamples satisfying the actual binary equal-arc geometry.
- [ ] Prove or refute: sparse zero + actual geometry implies `a,a,a` spacing.
- [ ] Verify that equal spacing really yields a repeated compressed word to which RL-L48 applies in every primitive case.
- [ ] After radius-3 closure, identify the exact missing global bridge to RL; do not infer it from a distance lower bound.
- [ ] Test whether RL-L27/RL-L36/RL-L54 force a distinguished rotation pair to transposition distance <=3.
- [ ] If not, decide whether to pursue a bounded larger-radius bridge or return to suffix/xi/extension-theorem routes.
