# RL44 Audit/Review Session Kickoff Prompt

Audit the attached `Collatz_Rsharp_RL43_to_RL44_Audit_Handover_2026-08-22.zip` as a skeptical research mathematician before extending the Collatz RL/3n+1 research.

First verify the bundle checksums and run `verification/run_all_rl43_verifiers.sh`. Treat any failure as a stop-and-repair event.

Your main goals are:

1. Establish the exact proof state after RL43. Separate analytic theorems, exact finite certificates, inherited dependencies, exact but audit-pending computations, and conjectures. In particular independently audit the new `rho>=50` certificate, the cutoff-free gap-9 `e>=8` theorem, defect-support compression, and the full-denominator phase bridge.

2. Audit the claimed radius-3 connection rather than merely restating it. Reconstruct the inherited RL19 short-binomial `3T^q-2` argument and compare it line-by-line with RL43's phase polynomial `P(T)`. Identify the precise quantitative lemma still missing to turn the shared binomial anchor into a genuine closure theorem.

3. Independently audit the one-excursion `e<=40` exact phase computation. Verify the quotient-state/pump exhaustion, all coarse filters, the normalized geometry families, and the residue DP. Do not promote `e>=41` beyond “exact computational frontier” unless the certificate is independently validated. Note the correction that the `t=6` geometry is admissible already at `e=35`, not `e=37`.

4. Red-team the unproved candidate theorem

`e >= (a-ell)+2`, equivalently `rho_E >= a`.

Start from `RL43_JK_INVARIANT_CANDIDATE.md`. Derive all `J_d,K` transition laws and try to find a counterexample. If it survives, seek a rigorous transition-by-transition or minimal-counterexample proof. Finite testing is evidence only.

5. Set a strategic road map for closing RL. Rank at least these routes:
   - prove a uniform transport/valuation theorem such as `rho_E>=a`;
   - transplant the RL19 resultant-size/uniqueness argument to the defect-controlled phase polynomial;
   - generalize the full-denominator sparse phase bridge from one excursion to multiple excursions with complexity controlled by `E+N`.

Do not spend the session simply extending `e=40` to larger finite cutoffs unless that computation is directly used to test or discover a uniform theorem.

At the end, produce an audit report stating: what is definitely proved, what is computationally certified, what remains conjectural, how close the radius-3 bridge really is, the highest-leverage next theorem, and any repaired/invalidated claims. If the audit is clean, propose the RL45 research attack rather than immediately grinding another cutoff.
