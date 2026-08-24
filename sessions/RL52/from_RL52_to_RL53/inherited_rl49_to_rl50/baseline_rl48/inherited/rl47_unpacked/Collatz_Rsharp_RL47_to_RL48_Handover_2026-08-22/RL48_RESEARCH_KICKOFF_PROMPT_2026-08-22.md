# RL48 Research Session Kickoff

Continue the Collatz R-sharp / RL research from `Collatz_Rsharp_RL47_to_RL48_Handover_2026-08-22.zip` as a skeptical research mathematician. The objective of this pass is to turn RL47's transport/phase identities into a proof-level route to the radius-3 bridge and, if possible, close the surviving RL branch.

## 0. Mandatory verification

First run:

```bash
sha256sum -c SHA256SUMS.txt
bash verification/run_rl47_core_verifiers.sh
bash verification/run_rl47_q134_stress_verifier.sh
```

Treat any failure as a stop-and-repair event. Do not extend a failed certificate.

Read:

1. `README_START_HERE.md`
2. `RL47_PROOF_STATE_AND_PROGRESS.md`
3. `RL47_RADIUS3_BRIDGE_AND_CLOSURE_ROADMAP.md`
4. `RL47_REPRODUCIBILITY_LEDGER.md`

Use `inherited/Collatz_Rsharp_RL46_to_RL47_Handover_2026-08-22.zip` only when an inherited definition or proof needs reconstruction.

## 1. First priority — uniformize the rank-transport bound

The main theorem remains

`H >= t+3 = v2(T+1)`.

RL47 proved

`H = sum_j (a_j-b_j)`

and

`14 + (27/2) zeta (1-2^-k)`

`= sum_j (2^a_j/3^j)(3-2^-(a_j-b_j))`, `k=t+3`.

It also implemented a rigorous finite-pair relaxation using the prefix-cap coordinate envelope and the total displacement budget.

Your first goal is to replace that finite-pair optimization by a symbolic inequality uniform in `(a,ell,q,t)` over the retained near-resonant window. Derive the strongest clean bound you can on `2^a_j/3^j`, sum the baseline geometrically, and optimize the displacement enhancement analytically.

If a full proof fails, isolate the exact scalar inequality or monotonicity statement still missing. Do not substitute more q-by-q computation for this step.

## 2. Second priority — produce the genuine radius-3 bridge

The radius-3 theorem itself is inherited as closed/audited. The missing step is to connect the RL phase condition to that theorem.

Work with the exact one-excursion objects:

`f(T)=3T^q-2`,
`L(T)=2T^ell-1`,
`P(T)=phase polynomial`.

Inherited RL45 gives `Res(f,L)=X-Y` and disproves the naive universal bound on `|Res(f,P)|_(3')`.

Reconstruct the exact inherited radius-3 theorem and the RL43/RL44 full-denominator phase condition before making a bridge claim. Then formulate a **same-root** statement: the relevant prime divisor of `X-Y` must see the same root of `f` in both `L` and `P`. A gcd of separate resultants is not enough unless you rule out different-root contamination.

Promising proof objects:

- a three-polynomial subresultant;
- a Bezout identity evaluated at the selected common root;
- a restricted phase congruence before taking a global norm;
- a defect polynomial obtained by expressing `P mod f` in rank-displacement variables.

The session should explicitly identify the quantitative lemma whose truth would let the audited radius-3 theorem close the branch.

## 3. Connect the two gates through rank displacement

RL45 showed reduced one-run terms occupy distinct residue classes modulo `q`. RL47 shows hypothetical low area means small total displacement `sum delta_j`.

Try to express `P mod f` as

`synchronized baseline + displacement defect`.

Then ask whether the low-displacement defect has sufficiently restricted support/degree/subresultant structure to trigger the radius-3 mechanism.

Do not assume “small area” means “radius 3”. Prove any support compression quantitatively.

## 4. q134 is a laboratory, not the objective

Known:

- exact no-violation for even `t<=16`;
- analytic exclusion for even `t>=116`;
- unresolved even `18<=t<=114`.

Use q134 to falsify candidate invariants. Extend the finite frontier only if a new proof-level compression makes it cheap. Do not spend the session merely pushing the cutoff.

## 5. Closure discipline

A claim that RL is closed must separately verify:

1. the uniform terminal area theorem or an equivalent result sufficient for the live branch;
2. the exact full-denominator/same-root bridge into the already-closed radius-3 theorem;
3. every inherited hypothesis used by the radius-3 theorem is actually satisfied by the RL configuration;
4. no proper-factor countermodel is being mistaken for a full RL solution;
5. finite certificates are not being promoted to uniform theorems.

If closure is not reached, end by reducing the remaining problem to the smallest explicit lemma(s) possible, with a proof-status ledger and reproducible counterexample tests.

Before ending the session, package source, verifier outputs, proof notes, checksums, and the next kickoff in one handover bundle.
