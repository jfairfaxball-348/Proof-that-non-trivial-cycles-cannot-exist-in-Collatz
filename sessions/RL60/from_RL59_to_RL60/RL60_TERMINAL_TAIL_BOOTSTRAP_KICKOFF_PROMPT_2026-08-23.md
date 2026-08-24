# RL60 terminal-tail bootstrap kickoff prompt

Continue the Collatz R-sharp / RL research from the attached `Collatz_Rsharp_RL59_to_RL60_Terminal_Tail_Bootstrap_Handover_2026-08-23.zip` as a skeptical research mathematician.

RL59 did not prove Gate A, Gate B, RL, or Collatz, and did not eliminate the sole safe-CF survivor. It did remove the RL58 synchronized-pump obstruction and reduce the remaining late-mass problem to the final positive height-one synchronized terminal tail.

## 1. Integrity and audit gate

Verify the outer SHA-256 sidecar and run

```bash
bash verification/run_all_rl59_to_rl60_verifiers.sh
```

Treat any assertion failure, changed finite boundary, or source/expected-output mismatch as stop-and-repair.

Then independently audit the two most important new ingredients:

1. the general normalized terminal potential

   `J*g <= zeta*3^(4-d)/2`;

2. the exact finite shortcut ancestor boundary showing no positive `n<11,184,810` reaches an admissible odd `K>=25` terminal predecessor.

Do not merely trust the bundled implementation.

## 2. Proof state to inherit

Unless the audit fails, retain:

- all RL58 inherited safe-CF constraints;
- `M0_late>5/4`, `Zx_late>253/60`;
- terminal `K` odd, `K>=25`;
- normalized terminal potential `Jg<=zeta*3^(4-d)/2`;
- both exits of the exact `J=3<->5` pump are terminally harmless;
- a defect-compatible four-pump local entry exists, so the obstruction is genuinely terminal;
- the final synchronized tail has aligned mass `M_final>23/4`;
- exact K25 shortcut boundary `n_min=11,184,810`, yielding `z>=9,457,747` after the analytic weight bound.

Classify K27/K29 boundaries as exact finite computational results pending independent implementation audit:

- K>=27: `n_min=13,256,071`, forced final `00>=11,209,179`;
- K>=29: `n_min=125,687,199`, forced final `00>=106,279,618`.

Note the corrected K27 count; do not repeat the earlier erroneous `11,209,546` figure.

## 3. Main target — make the K/z bootstrap close

Define, for odd `K0`,

`N(K0)=min n>0 whose shortcut orbit reaches either 2^K-1 or (2^K-2)/3 for some odd K>=K0`.

From a certified `N(K0)`, set

`Jmin=2N(K0)+1`.

The terminal potential and `M_final>23/4` force

`#00_final > 115*Jmin/272`.

Therefore obtain a lower bound on `z` under the hypothesis `K>=K0`.

Combine this with the exact inherited relation

`K+z=q+3`.

The goal is a contradiction, a finite interval remainder, or a self-improving exponent interval—not merely a larger numerical lower bound on `z`.

## 4. Before extending K0, search the inherited ledger for an upper restriction on z

This is the highest-leverage housekeeping task.

Reconstruct all exact relations involving

- total x-zero count;
- total y-zero count;
- word length;
- `ell`, `q`, `K`, `z`, `R`;
- denominator/exponent budgets;
- defect support;
- any positivity or phase inequalities.

Ask whether the new bound `z>=9,457,747` already collides with an inherited upper bound or makes another finite regime theorem applicable.

Do not assume there is such an upper bound; find and verify it.

## 5. Build an interval reverse-tree method

If no immediate upper-bound contradiction exists, do not rely on brute-force forward scans alone.

Work backward from the terminal alternatives

`2^K-1`, `(2^K-2)/3`

under the shortcut map. Seek an exact branch-and-bound or modular theorem that certifies lower bounds on all ancestors over ranges of odd `K`.

Promising handles include:

- exact parity strings;
- reverse transformations `n->2n` and, when divisible, `n->(2n-1)/3`;
- residue classes modulo powers of 2 and 3;
- lower bounds on reverse-tree values as a function of depth / odd-step count;
- exponent interval certificates;
- pruning using `K+z=q+3`.

The objective is to replace isolated K25/K27/K29 searches by a scalable theorem or finite certificate family.

## 6. Guard against circularity

The final synchronized subsystem is conjugate to shortcut Collatz. Do not assume global convergence, monotone growth, or an unproved lower bound for all shortcut ancestors.

Any use of the subsystem must be one of:

- an exact finite computation;
- a proven modular/reverse-tree lemma;
- an inherited exponent restriction that makes the relevant range finite.

## 7. Verification policy

Keep separate labels for:

- analytic theorem;
- exact finite certificate;
- exact computation pending independent audit;
- exploratory search;
- conjecture.

Before promoting new K-threshold numbers, reproduce both the below-boundary and at-boundary runs and preferably add an independent implementation.

## 8. Desired RL60 end state

Best case: eliminate the sole safe-CF survivor by combining the new terminal-tail bootstrap with an inherited upper/exponent restriction.

Otherwise: produce a rigorous interval theorem for terminal shortcut ancestors, a finite unresolved exponent range, and a clear statement of whether this route is genuinely reducing the branch or has hit an unrestricted Collatz-conjugate barrier.
