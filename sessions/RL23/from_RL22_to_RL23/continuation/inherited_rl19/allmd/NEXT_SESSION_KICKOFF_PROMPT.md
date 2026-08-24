# Next-session kickoff prompt — RL20

Continue the RL/3n+1 research from the attached **RL19 Radius3 Closure And Global Packing handover** as a skeptical research mathematician.

First run the bundled verifiers and read `RL19_PROOF_STATUS_AND_BRANCH_LEDGER.md`, `RL19_SESSION_CLOSEOUT.md`, and `RL18_EXTERNAL_DEPENDENCY_AUDIT.md`. Treat any verifier assertion failure as a stop-and-repair event. Do not redo the radius-3 case tree unless a verifier or proof audit exposes a defect.

## Track A — audit/freeze exact radius-3 closure

The final `gcd(A,L)=3, gcd(A,m)=1` one-orbit cubic leaf is claimed closed analytically in `RL19_CUBIC_SKEW_ANALYTIC_CLOSURE.md`.

Audit especially:

1. the exact weak-interlacing equivalence under RL10 conventions, including coincident `[2,1]` events;
2. the cyclic normalization used in the interior skew sector;
3. the Eisenstein coefficient/norm inequalities, including equality boundaries;
4. nonvanishing and `<C` estimates in the `k=1` and `k=3` extreme resultant sectors;
5. equal-gap => nonprimitivity.

Do not use the old `a<=80` scan as proof. If the audit holds, leave radius 3 closed and move on.

## Track B — attack RL globally

Start from the exact arbitrary-radius identities, not a radius-4/5 cutoff ladder.

Use together:

- RL18 arbitrary-radius orbit polynomial;
- RL19 weighted-difference identity;
- RL19 exact weighted populations/state packing;
- RL19 exact odd-step product identity
  `lambda=prod_(odd phases)(1+1/(3x_i))`;
- the bound
  `log lambda <= 1/(3R#)+(1/6)log(1+2(L-1)/R#)`;
- the proved least-root/final-return lineage (RL-L27/RL-L36/RL-L54).

Priority targets:

1. **Near-resonant branch.** Combine the new `R#`-dependent upper bound for `A log2-L log3` with a rigorously stated two-logarithm lower bound or continued-fraction structure. Any Laurent–Mignotte–Nesterenko use must remain `EXTERNAL: LMN`; do not turn it into an unexplained finite-cutoff engine.
2. **Huge-length branch.** Try to make `L ~ R#` incompatible with root/final-return ownership, residue classes, state populations, or a proper-factor/resultant obstruction.
3. **Weighted-difference obstruction.** Seek a proper factor or conjugate/resultant estimate for
   `sum_i q_i(3^(-G_i)-1)=4(lambda-1)(R_m-R#)`
   rather than positivity of the raw orbit sum.
4. **Higher-block hierarchy.** The exact block identities are potentially useful only if they remove the free correlation parameters; prove a new restriction before investing in scans.

## Bounded-radius bridge caution

RL19 found an in-session length-184 countermodel suggesting RL-L27/RL-L36/RL-L54 local grammar alone does not force radius <=3, but its exact word/certificate was not frozen. Reconstruct and save the smallest countermodel before citing the bridge as formally falsified. Do not confuse such a local-grammar model with an RL object satisfying global `D|Q`.

## Dependency discipline

Maintain labels: `ANALYTIC`, `EXTERNAL: LMN`, `EXACT FINITE CERTIFICATE`, `EXTERNAL COMPUTATIONAL INPUT`, `COMPUTATIONAL EVIDENCE`, `OPEN`.

Jacobi means the classical Jacobi symbol/quadratic reciprocity. The Jacobian Conjecture is not used in this proof chain.

Before handing over, rerun every affected verifier, preserve exact certificates, regenerate `SHA256_CONTENTS.txt`, and state separately:

- distance to exact radius-3 closure;
- distance to an actual RL contradiction.

Do not claim RL or Collatz solved unless every required global bridge is itself proved.
