Continue the Collatz R# RL branch from RL-8.

Canonical state:
- RL-7: one-edge self-rotations are exactly primitive Christoffel classes; those are internally excluded. Every primitive nontrivial cycle is non-Christoffel, but the one-defect quantitative gap is too small.
- RL-L53: every non-cancelling two-edge adjacent-transposition path collapses arithmetically. Overlap gives a unit or `5*unit`; disjoint edges force `D|2^u +/-3^v`. For `gcd(A,L)=1` self-rotations, opposite directions are impossible, so only `D|2^u+3^v` remains apart from `D=5`. With `k=uL-vA`, resonance also forces `D|2^|k|-sigma^L` and `D|3^|k|-sigma^A`.
- Finite diagnostic: proper binomial resonances through `A<=200` occur only for `(A,L,D)=(4,2,7),(5,3,5),(8,5,13)`. This is evidence only.
- RL-L54: at the least-state full parity rotation, every proper suffix is subcritical: `2^m>3^p`. Any undercritical proper prefix obeys `R# < 2^(m-p)(3^p-2^p)/(2^m-3^p)`. With inherited external `R#>=2^71`, every proper root prefix through length 183 is forced supercritical; `(184,116)` is the first generic rescue pair reaching the floor.
- RL-L55: for `g=gcd(A,L)>1`, reduction modulo `D0=2^(A/g)-3^(L/g)` gives a weighted block cancellation `sum 3^(-E_j)Q(B_j)==0 mod D0`.
- RL-G9: bare proper-factor descent is false. Primitive balanced word `100001` has `(A,L)=(6,2)`, `D=55`, `D0=5`, `Q=35`; so `D0|Q` does not force repetition or shorter closure.

Highest priority:
1. Encode the actual `(u,v)` of any two-edge distinguished-rotation path allowed by RL-L27 root departure and RL-L36 final return. Immediately pass to `k=uL-vA` and the determinant divisibilities. Seek an analytic exclusion of the plus resonance for RL-compatible coprime parameters.
2. Combine the exact suffix envelope with the externally forced first-183 prefix envelope and the physical root/closing parity blocks. Seek a mechanical-word distance theorem, not generic brute force.
3. Salvage residual-factor descent only by using the RL boundary/root grammar to prevent the weighted block cancellation in RL-L55. Any candidate lemma must reject the `100001` counterexample for a structural reason.
4. Continue the positive-density Christoffel-displacement target; the finite 183-step window alone is not asymptotic.
5. Keep `s=2` vs `s>=3` and `n_close=1` vs `n_close>=2` split explicit.

Do not broaden brute-force enumeration without tying it to the binomial determinant, the mechanical envelopes, or the weighted-block congruence. Maintain explicit PROVED / EXTERNAL / FINITE-EVIDENCE labels. RL remains open unless an actual infinite contradiction is proved.
