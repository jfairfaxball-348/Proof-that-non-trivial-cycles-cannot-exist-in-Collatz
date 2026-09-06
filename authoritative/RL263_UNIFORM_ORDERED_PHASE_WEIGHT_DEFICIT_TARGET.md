# RL263 — uniform ordered-phase weight-deficit target

Date prepared: 2026-09-06
Status: **PREPARED, NOT STARTED**

## Incoming promoted state

RL262 proves two results.

First, the inherited selector scan has no retained selector for `1288<=a<1417`; its unique first survivor is `(1417,894,523,317,200,18,4)`, and an exact RL65 ordered full-phase replay eliminates all 2,232 possible `(k,prefix,N_phase)` classes for every feasible odd `31<=k<=525`. Thus the fourth retained selector is removed completely.

Second, RL262 isolates the selector-independent ordered-phase identity. For every inherited odd-terminal full-phase datum, with `rho=ell-3` and `m=a-k-1`,

`N_phase == 19 (mod24)`

and

`Dcal = 3^rho*(9*N_phase+61)/4 - 2^(m-2)*(4+(N_phase-2)*2^(k+1))/3`.

Hence through depth `m-2`,

`Dcal == 3^rho*(9*N_phase+61)/4 (mod 2^(m-2))`.

The stronger modulus `2^m` version seen in RL262 scratch was explicitly corrected before promotion and is not authoritative.

## Unique RL263 objective

Do **not** begin by scanning for a fifth selector.

Attack the global ordered-phase mechanism exposed by RL261--RL262. Prove, or decisively falsify with an exact counterexample/barrier, a uniform theorem showing that a legal canonical ordered extension satisfying the corrected dyadic defect target cannot reach the required common internal weight `rho` at length `m` throughout the currently surviving resonance branch.

The preferred theorem shape is an eventual-corridor / weight-deficit statement: after a controlled transient, every indefinitely extendable ordered state is forced into a finite family of low-one-density regimes (the live RL262 scratch suggests an alternating density-1/2 corridor), while the resonance hypotheses require a uniformly larger final one-density. The exact theorem need not use this wording if a stronger equivalent ordered-prefix obstruction is found.

Requirements:

1. Work from the exact RL65/RL262 identities and the actual canonical `step_x` path; do not relax away ordered rank or prefix coupling.
2. Treat arbitrary admissible positive `N_phase`; do not globalize the selector-specific bounds `288` or `1209`.
3. Preserve the explicit last-two-bit carry term involving `k`; do not restore the corrected-away modulus-`2^m` claim.
4. A finite-state or automaton theorem is acceptable only if its state space and coverage are proved uniform over the claimed parameter range.
5. If the global route is decisively blocked, freeze the exact barrier and only then prepare a justified return target. Do not silently resume selector-by-selector enumeration in this RL.
6. Radius 4 may be invoked only if every audited primitive/full-D/exact-distance hypothesis is explicitly manufactured. Radius 5 remains inactive.

Gate A and Gate B remain open unless independently closed by a promoted theorem.
