# RL51 research kickoff prompt

Continue the Collatz R-sharp / RL branch research from the attached `Collatz_Rsharp_RL50_to_RL51_Handover_2026-08-22.zip` as a skeptical research mathematician.

First verify the outer SHA-256 sidecar after extraction, then run:

`bash verification/run_all_rl50_handover_verifiers.sh`

Treat any failure as a stop-and-repair event. The original inherited RL49 half-rotation verifier has a known stale absolute path; use the bundled portable verifier from the RL50->RL51 verification script. Do not silently rewrite inherited provenance files.

Then read `RL50_FINAL_PROOF_STATE_AND_RL51_ROADMAP.md` and the five RL50 research notes/verifiers.

## Proof-state discipline

The RL branch is NOT closed. The live target is Gate A:

`H >= t+3`, equivalently the inherited terminal height-one valuation inequality.

Do NOT resurrect the old direct full-phase -> radius-3 shortcut. Do NOT use the Ansari-based `4*3^44+2` external floor as an accepted theorem: RL50 found an explicit failure in the printed induction identity at `n=1`. The stable external floor is Barina's peer-reviewed `2^71` verification. Keep any current live project status separate and explicitly conditional.

## What RL50 has established

Use as audited starting facts after the verifiers pass:

- safe CF gate leaves one explicit above-`log_2(3)` survivor:
  `(a,ell,q)=(123139092617126647266, 77692117359936589403, 45446975257190057863)`;
- uniform genuine full phase has `z>=20`;
- the sole safe survivor has `z>=27`, `S>45/4`, `E<5/3`;
- `W=gJ/3^d` is monotone and `sum epsilon=2E` exactly;
- zero displacement satisfies `H=sum r_j` and `E=sum w_j[1-(2/3)^r_j]` exactly;
- complete height-one excursions satisfy `Delta L=S_exc+3E_exc/2`, `S_exc<=E_exc`;
- all genuine excursions of the sole safe survivor have total `Delta L<25/6`, and its first positive height-one return obeys `L<25/6`, `W<142/45`;
- after its first genuine excursion departure the sole safe survivor must return to height one and execute at least 7 height-one `11` plus 2 height-one `00` columns;
- the height-one odd-preserving synchronized grammar is exactly conjugate to shortcut Collatz, so do not try to solve that subsystem in isolation;
- RL47 rank transport now has exact enhancement `Lambda=2X+E`.

## Primary RL51 target: eliminate stable z=27

The current safe `z=27` rank-transport exclusion misses by only about `0.0134` in the needed E-bound:

required approximately `E<1.6499581...`,

available stably `E<1.6633648...`.

Attack this tiny sliver with a genuinely coupled constraint, preferably one of:

1. simultaneous x/y sequential prefix caps rather than an x-only cap;
2. exact compatibility of zero-displacement weights with the terminal power `J_end=2^k`;
3. a denominator-independent finite state/certificate that carries `(g_x,g_y, displacement/height, E-budget)` without enumerating the huge denominator;
4. backward divisibility through the final height-one synchronized block.

If `z=27` is excluded, exploit parity for the sole candidate (`q` odd, `t` even) to jump to `z>=29`.

## Secondary target: do NOT polish the separable rank envelope

For `z>=28`, RL50 found the inherited separable rank envelope is already too weak even with `E=0`. Therefore after the `z=27` case, switch to a new coupled terminal/macro argument.

Start from the first positive height-one return with

`L<25/6`, `W<142/45`,

compress later genuine excursions by `(E_exc,S_exc,Delta L_exc)`, and propagate the terminal condition `J=2^k` backward through maximal synchronized `00/11` blocks. Investigate exact dyadic divisibility invariants of `g(J-1)` / `g(J+1)` and macro endpoints.

## Deliverables for RL51

1. A verifier-backed attempt on the stable `z=27` sliver, with exact arithmetic and explicit statement of success/failure.
2. If it fails, isolate the precise extremal configuration that achieves the remaining gap; do not merely report another scalar upper bound.
3. A terminal-power/backward-macro lemma strong enough to address `z>=29`, or a rigorous countermodel/barrier showing exactly why the proposed invariant is insufficient.
4. Updated proof ledger clearly separating analytic theorems, exact finite certificates, stable external inputs, live conditional inputs, conjectures, and failed approaches.
5. Bundle every new verifier and its run output for the next handover.

The objective is not cosmetic progress: either close Gate A, eliminate a genuine surviving structural case, or produce a sharp obstruction that materially narrows the next attack.
