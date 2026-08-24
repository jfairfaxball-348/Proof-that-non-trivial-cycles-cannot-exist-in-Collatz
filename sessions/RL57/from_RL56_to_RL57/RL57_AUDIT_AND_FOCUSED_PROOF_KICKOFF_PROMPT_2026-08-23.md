# RL57 Audit + Focused Proof Session Kickoff Prompt

Continue the Collatz RL/3n+1 research from the attached `Collatz_Rsharp_RL56_to_RL57_Audit_Handover_2026-08-23.zip` as a skeptical research mathematician.

This session has two phases: **audit first, then a focused terminal-divisibility proof attack**. Do not extend the newest RL56 claims until they survive audit.

## Mandatory integrity/reproducibility step

1. Verify the outer ZIP against its `.sha256` sidecar.
2. Extract it.
3. Run:

   `sha256sum -c SHA256SUMS_RL56_TO_RL57_AUDIT.txt`

4. Run:

   `bash verification/run_all_rl56_to_rl57_audit_verifiers.sh`

5. Treat any failure as a stop-and-repair event.
6. Read:
   - `RL56_FINAL_PROOF_STATE_AND_RL57_AUDIT_ROADMAP.md`
   - `RL56_SESSION_INCREMENT_AND_AUDIT_TARGETS_2026-08-23.md`
   - `RL56_AGGREGATE_POTENTIAL_AND_TERMINAL_COMPATIBLE_PREFIX.md`
   - inherited `inherited_rl55_to_rl56/RL55_AUDIT_FINDINGS_AND_PROOF_STATE_2026-08-23.md`.

## Phase I — skeptical audit

### 1. Re-derive the aggregate potentials

From the exact four legal forward maps, independently recompute the increments of

`Xi = g[(T-1)/3^(d-1)+1/2^(d-1)]`

and

`Psi = g+Xi/2`.

Verify:

- `Xi` is monotone;
- `Psi` is monotone;
- every x-zero of weight `w=g` satisfies `Delta Psi>=w`;
- therefore `Zx(segment)<=Psi(end)-Psi(start)`;
- all start/terminal formulas and strict inequalities are correct.

Do not accept the companion verifier as a substitute for the algebra.

### 2. Audit the `K>=25` deduction

Rerun and inspect the inherited RL45 `H<=23` quotient certificate. Then explicitly reconcile the notation:

- current terminal exponent `K` in `J_end=2^K`;
- terminal height-one `H`;
- RL45's internal quantity also named `K` away from terminal height.

Verify that under the retained counterexample hypothesis `H<K`, every odd current `K<=23` is excluded, hence the live branch really has `K>=25`.

### 3. Independently audit the finite prefix results

The same-code reruns bundled here report:

- with `K>=25`, a terminal-compatible prefix bound `Zx_26<=103/10`;
- with the coupled same-`K` viability test, `Zx_26<=33/4`;
- a viable witness exists above `8`.

Create an independent implementation or otherwise independently reconstruct every pruning inequality. In particular verify that the `33/4` search cannot prune a genuine survivor.

If the `33/4` result survives, promote the consequences

`Zx_late>11/3`

and

`Psi_cut<3.084`.

### 4. Audit the defect localization

Using only the inherited exact identity

`E=sum_j w_j[1-(2/3)^r_j]`, `E<5/3`,

verify that

`M_{r>=2}<3`

and hence, if `Zx_late>11/3`,

`M_{r<=1}>2/3`.

Check the strictness carefully. Since every `w_j<17/30`, at least two late x-zeros must have displacement at most one.

## Phase II — focused proof attack

### Primary theorem target

Prove

`M_{r<=1} <= 2/3`

under the full remaining survivor hypotheses.

This alone contradicts the audited strict lower bound `M_{r<=1}>2/3` and eliminates the sole safe-CF survivor.

### Step A — reconstruct the exact near-aligned grammar

Do not trust the session shorthand. Starting from the inherited rank-matching/displacement definition, classify all late x-zero configurations with displacement `r_j=0` and `r_j=1`.

Determine exactly:

- allowed starting heights;
- edge macro (`00`, `01`, neighboring `10/11` structure);
- weight update through the macro;
- effect on `Q_d=J+2^d-1`;
- y-zero consumption;
- whether the macro returns to height one or two.

The working expectation is that the entire grammar is confined to `d<=2`, but prove or correct this.

### Step B — use the terminal `Q` divisibility

Use the inherited exact backward maps:

- `11: Q -> 2Q/3`, iff `3|Q`;
- `10: Q -> 2Q+1`;
- `00: Q -> 2Q-(3^d-1)`;
- `01: Q -> 2Q/3-3^(d-1)`, with `d>1` and `3|Q`.

Backward `11` pumping is exactly limited by `v3(Q)`. Combine this with terminal

`J_end=2^K`, odd `K>=25`,

and the exact suffix count relation. If the legal cut has height `d_c` and the suffix event counts are `a,b,c,e` for `11,10,00,01`, verify and use

`b=e+d_c-1`.

Look for a quotient/residue invariant that prevents accumulating more than `2/3` weight in the audited displacement-0/1 macros.

### Step C — compress neutral height-one pumping

Do not try to prove arbitrary settling of the unrestricted height-one Collatz-conjugate subsystem. Instead quotient repeated `11` runs by `v3(Q)` and treat the near-aligned x-zero events as the charged events. A successful theorem should bound mass per compressed charged event or show that too many charged events force an impossible terminal residue.

### Step D — bounded remainder only if genuinely bounded

If the divisibility argument covers all but a finite `K` window or finite residue set, then and only then use exact computation to close that remainder. Do not enumerate the enormous late suffix length.

## Strategic stop condition

If the audit invalidates `33/4`, repair that first.

If the audit survives but every near-aligned bound still reduces to unrestricted height-one Collatz dynamics with no terminal arithmetic gain, explicitly stop the survivor-local escalation and recommend a pivot back to global Gate A / a valid Gate B connecting full-phase RL data to the already-certified radius-3 theorem.

## End-of-session report

Separate clearly:

- analytic theorems;
- inherited exact certificates;
- new independently audited finite certificates;
- same-code reproducibility only;
- conjectures/open lemmas.

State whether the safe-CF survivor was actually eliminated and whether any result advances global Gate A/Gate B rather than only the survivor-local branch.
