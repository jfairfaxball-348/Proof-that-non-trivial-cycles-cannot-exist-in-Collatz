# Collatz R# RL-6 Handover

RL-6 closes the **structural** exception left by RL-5 for exact saturation-boundary exits. It does **not** prove that nontrivial Collatz cycles are absent.

The key new object is the cyclic height word

`h_j = n_j - mu_(j+1)`, with `sum h_j = L > 0`.

A cycle-lemma rotation can always be chosen so that every nonempty suffix sum of the rotated height word is positive. At that rotation, the final composed-numerator term is the unique 3-adic minimum, so

`v3(C_good)=M`

holds for **every admissible word**, including words with exact boundaries. Starting from this good rotation, non-boundary edges propagate the `v3(C)=M` signature automatically. An exact boundary `r=n`, `mu'=n+c` preserves it iff one explicit 3-adic cancellation gate has depth exactly `c`.

Consequently the RL-L41 scalar criterion extends to all admissible words:

- choose a good rotation;
- require `D | C_good`;
- check only the finitely many exact-boundary cancellation gates.

If these pass, the full positive periodic integer anchor orbit is realized, with all declared local exit valuations exact.

RL-6 also derives a denominator-defect budget from the least-anchor ceiling orbit. If `W_*` is the minimum rational anchor candidate and `E_mu=sum (2/3)^mu_next (1-2^-t)`, then for `P>1`

`e_close/W_* < D/2^A < E_mu/W_* < P/W_*`.

For the k=0 RL root, `W_*=R#+1` and the closing error is `1-2^-t_close`, so the common denominator must be extremely near-resonant whenever `R#` is large.

The verifier passes. In the exhaustive diagnostic domain `P<=3`, `n,t<=6`, cancellation depth `<=2`, there are 11,278 admissible positive-slope words containing exact boundaries; 3,593 pass all boundary 3-adic gates, but only the three trivial repetitions of `W=2` satisfy the full generalized criterion.

RL remains open. The next target is now cleanly concentrated on `D | C_good`, especially with the low root-departure and high/discrete-log root-return gates inserted.
