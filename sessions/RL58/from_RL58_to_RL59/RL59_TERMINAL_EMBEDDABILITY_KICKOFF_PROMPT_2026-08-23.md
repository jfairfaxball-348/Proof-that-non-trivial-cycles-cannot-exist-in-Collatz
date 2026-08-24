# RL59 terminal-embeddability kickoff prompt

Continue the Collatz R-sharp/RL research from the attached `Collatz_Rsharp_RL58_to_RL59_Terminal_Embeddability_Handover_2026-08-23.zip` as a skeptical research mathematician.

RL58 completed the independent audits of the two RL57 discovery certificates. The first task in RL59 is therefore **not** another broad audit and **not** further prefix squeezing. The central task is to decide whether the exact synchronized positive pump

`J=3 --11--> 5 --00--> 3`

can be repeated enough times inside a genuine safe-CF late suffix while remaining compatible with the exact terminal endpoint and phase/exponent arithmetic.

## 1. Integrity gate

Verify the outer `.sha256` file, then run

```bash
bash verification/run_all_rl58_to_rl59_verifiers.sh
```

Treat any failure as stop-and-repair. The previous RL57->RL58 outer handover is preserved under `inherited_rl57_to_rl58/`.

## 2. Proof ledger to inherit

Unless a verifier fails, retain/promote:

- `Zx>143/12`;
- `E<5/3`;
- every x-zero weight `w<17/30`;
- exact defect identity;
- safe-CF survivor with odd `z>=41`;
- odd terminal `K>=25`;
- `J_end=2^K`, `Q_end=2^K+1`;
- `v3(Q_end)=1+v3(K)`;
- independently audited `M0_26<=17/3`;
- independently audited `Zx_26<=77/10`;
- strict `M0_late>5/4`;
- strict `Zx_late>253/60`;
- sharpened `Psi_cut<2.533333534500`.

Gate A, Gate B, RL, and Collatz remain open.

## 3. Start from the exact obstruction

RL58 showed defect + cap + Psi cannot by themselves force `M0_late<=5/4`.

For the exact pump,

`g_out=(4/3)g_in`,

and after `m` repeats,

`A_m=2g_in((4/3)^m-1)`.

Four repeats from `g_in=7/20` produce `245/162>5/4` aligned mass while satisfying the local cap and staying below the sharpened Psi ceiling.

This is a local proof-method obstruction, **not** a proof that such a block embeds in a genuine terminal suffix. That embeddability question is the target.

## 4. Derive a maximal pump block symbolically

Before broad search, derive the exact block-level transformation through `m` pumps. Track:

- `J,Q`;
- scalar `g`;
- `(i,p)` and any terminal exponent counters;
- aligned zero count and mass;
- Xi/Psi;
- all phase variables entering terminal relations.

Classify every legal entry to `J=3` and every legal exit from `J=3` or `J=5`. The aim is a compressed block transition that can be spliced into the exact backward terminal grammar.

## 5. Attack terminal compatibility

Work backward from

`Q_end=2^K+1`, odd `K>=25`,

with

`11: Q->2Q/3`,

`10: Q->2Q+1`,

`00: Q->2Q-(3^d-1)`,

`01: Q->2Q/3-3^(d-1)`.

Track the first backward hit of `Q=4` or `Q=6` and use:

- `v3(2^K+1)=1+v3(K)`;
- `Q mod 3^n`;
- `v3(Q)`;
- `v2(Q-2)`;
- exact event-count changes from an `m`-pump block;
- scalar/weight constraints at entry and exit.

Try to prove

`m>=m0 => K belongs to a finite exceptional set`

or a stronger direct impossibility.

## 6. Computation policy

Use exact computation to discover congruence patterns and certify bounded remainders, but keep roles separate:

- symbolic block derivation first;
- analytic divisibility/congruence lemma second;
- finite exact verifier only after the analytic step bounds the remainder;
- exploratory searches explicitly labelled non-proof.

## 7. Avoid already-defeated routes

Do not spend the beginning of RL59 on:

- tightening `17/3` toward `557/100`;
- arguing separated aligned runs must consume defect;
- trying to close from Psi slack alone;
- assuming a positive lower bound on `Psi_cut`.

RL58 already showed these are insufficient or not yet justified.

## 8. Pivot condition

If, and only if, a rigorous analysis shows arbitrarily many pumps can be embedded while preserving **all** exact terminal endpoint, phase, exponent, and survivor constraints, record that an unrestricted Collatz-conjugate subsystem survives and pivot the next roadmap back to global Gate A / Gate B.

The mere existence of the local `3<->5` cycle is not enough to justify the pivot.

## 9. Desired end state

Best case: prove terminal compatibility bounds synchronized pumping strongly enough to contradict `M0_late>5/4` and eliminate the safe-CF survivor.

Otherwise isolate the strongest exact terminal-divisibility lemma, any finite exceptional remainder, and a clean proof ledger distinguishing theorem, exact finite certificate, exploratory computation, and conjecture.
