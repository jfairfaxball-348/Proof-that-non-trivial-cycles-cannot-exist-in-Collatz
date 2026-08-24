# START HERE — RL44 skeptical audit/review and road-map session

Do **not** begin by extending `rho` or `e` numerically.

The purpose of RL44 is to decide exactly what RL43 bought us, whether the new bridge is sound, and which next theorem could plausibly close the remaining RL branch rather than merely move a finite frontier.

## Mandatory first pass

1. Verify the outer bundle checksum and `SHA256SUMS.txt`.
2. Verify the inherited RL42 zip checksum.
3. Run `verification/run_all_rl43_verifiers.sh`.
4. Read the four RL43 theorem/certificate notes in this order:
   - `RL43_RHO49_ELIMINATION_AND_EXCESS_GAP_LEMMA.md`
   - `RL43_DEFECT_SUPPORT_RADIUS3_BRIDGE.md`
   - `RL43_GAP9_CUTOFF_FREE_AUTOMATON.md`
   - `RL43_FULL_DENOMINATOR_PHASE_BRIDGE.md`
5. Read `RL43_PROOF_STATUS_AND_AUDIT_ROADMAP.md` and reconstruct every dependency from RL19/RL21/RL38/RL42 that RL43 imports.
6. Treat any verifier failure, missing inherited lemma, hidden cutoff, or unjustified exhaustion claim as a stop-and-repair event.

## Audit targets

### A. `rho=49` elimination

Recheck the low-excess crossing catalogue, safe synchronized-run over-approximation, near-resonant endpoint filtering, and exact effective-mass comparisons. Confirm that `rho >= 50` really follows in precisely the retained branch and nowhere broader.

### B. Defect-support compression

Audit `z <= e+1`, run compression, global support accounting, shifts between local and global `Q` conventions, and the resultant gateway. Confirm that `4(E+N)` is a valid pre-collection bound and identify whether a sharper support bound is available.

### C. Cutoff-free gap-9 automaton

Derive the `T` transition from first principles and prove the quotient graph is genuinely finite at fixed excess after quotienting the neutral `(d,T)=(1,-2)` pump. Confirm `e>=8` without a hidden length or odd-weight cutoff.

### D. Full denominator phase bridge

Audit the inherited two-factor decomposition and the new phase compression. Reprove:

`X-Y | V+YG`,

`3 rho^(a-ell) = 2 (mod X-Y)`,

`X-Y | Res(3T^(a-ell)-2, P(T))`,

and nonvanishing of the resultant.

Then compare line-by-line with the inherited RL19 radius-3 `k=1` extreme-sector argument. Identify exactly what quantitative lemma is missing before the RL19 machinery can be transplanted.

### E. `e<=40` exact phase computation

This is **audit-pending**, not theorem-grade. Reconstruct the quotient-state geometry filter independently, especially the neutral-pump parameterization, near-resonance enumeration, `rho>=50`, gcd/primitivity conditions, effective-mass upper bound, and terminal synchronization.

The normalized admissible geometries through `e=40` should be only `(a,ell)=(65,41)` with:

- `t=0, z=24` for `e=26..40`;
- `t=2, z=22` for `e=30..40`;
- `t=4, z=20` for `e=34..40`;
- `t=6, z=18` for `e=35..40`.

Then independently verify that no phase residue equals `-4*3^41 mod (2^65-3^41)`.

**Narrative correction:** one earlier conversational summary said the `t=6` geometry first appeared at `e=37`; the actual quotient-state filter admits it at `e=35`. The included exact DP eliminates `e=35,36` as well. Trust the scripts/ledger, not the earlier wording.

### F. `J_d/K` candidate invariant

This is the highest-value proof target, but it is a **conjecture**, not a retained lemma. Try hard to disprove it before proving it. If it survives, seek a transition-by-transition induction or a monotone potential proof. Do not use finite testing as proof.

## Deliverable for RL44

Produce an audit report with four columns/status classes:

1. analytically proved;
2. exact finite certificate / reproducible computation;
3. inherited dependency requiring explicit citation/check;
4. conjectural / heuristic.

Then set a ranked road map for closing the bridge. Prefer a uniform theorem over extending `e=40` to `e=41,42,...` unless the finite computation directly reveals the invariant needed for the theorem.
