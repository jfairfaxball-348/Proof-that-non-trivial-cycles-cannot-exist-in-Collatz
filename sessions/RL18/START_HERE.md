# RL18 START HERE — repaired radius-3 ledger + global orbit identity

Date: 2026-08-20

This bundle supersedes RL17 as the working handover.  Its purpose is **repair first, then strategic progress**.  It does not claim a proof of RL or of the Collatz conjecture.

## What changed from RL17

RL17 correctly identified four defects in the inherited radius-3 story:

1. RL12's analytic proof provenance was missing.
2. RL13's analytic proof provenance was missing.
3. Two coefficient-3 P2 boundary leaves had been silently omitted.
4. The sector `gcd(A,L)=gcd(A,m)=3` had also been silently omitted.

RL18 repairs all four:

- RL12's three-orbit denominator envelope is reconstructed analytically and tied back to the inherited LMN + continued-fraction + finite certificate.
- RL13's near/far density proof is reconstructed analytically and tied back to its inherited certificate.
- the `j=1` coefficient-3 P2 boundary is closed by an elementary binomial resultant contradiction;
- the `j=2` coefficient-3 P2 boundary is closed by a binomial resultant barrier + the published Laurent–Mignotte–Nesterenko two-log theorem + continued fractions + a 456-test exact tail;
- the omitted `gcd(A,L)=gcd(A,m)=3` sector reduces exactly to the same P2 three-orbit mechanism, with the only arithmetic zero producing `(10)^3`, hence no primitive survivor.

After these repairs, **one radius-3 leaf remains open**:

> `gcd(A,L)=3`, `gcd(A,m)=1`, full-`D` cubic sparse uniqueness.

The exact target is stated in `RL18_PROOF_STATUS_AND_BRANCH_LEDGER.md`.

## New strategic result beyond repair

RL18 also derives an exact **unbounded-radius orbit-sum identity**.  For any binary word and any rotation shift, `D|Q` is equivalent to vanishing of a weighted orbit sum `Z`, and each shift orbit is represented by an explicit polynomial/Laurent polynomial in the rotation multiplier `rho`.  Radius 3 is a sparse specialization of this identity rather than an isolated calculation.

This is the main global object the next session should try to connect to the RL least-root/final-return grammar.

## New reduction on the last cubic leaf

Modulo the cubic cofactor `C=X^2+XY+Y^2`, center the three gaps at `a`.  A sparse zero implies

`A + epsilon B = 0`, with `epsilon^2+epsilon+1=0`,

and therefore

`A^2 - A B + B^2 = 0 (mod C)`.

For the positive rational lift `q=2^m/3^p`, the corresponding Eisenstein norm is strictly positive for every skew triple.  Thus a skew zero forces `C` to divide a **nonzero positive norm numerator**.  This turns the open uniqueness problem into a concrete size/resultant problem.

## External dependency warning

There is **no Jacobian Conjecture dependency** in this project.  RL17's phrase was **Jacobi/order arguments**, i.e. the Jacobi symbol/quadratic reciprocity.  The Jacobian Conjecture is a different problem and, as of this handover, is known to be false in dimensions at least 3.  See `RL18_EXTERNAL_DEPENDENCY_AUDIT.md`.

The only named external deep theorem active in the repaired finite reductions is the published Laurent–Mignotte–Nesterenko two-logarithm theorem, in its rational specialization.  Every place it enters is explicitly labelled `EXTERNAL: LMN`.

## Run first

From this directory:

```bash
python verify_rl18_repairs.py
python verify_rl18_global_orbit_identity.py
python verify_rl18_cubic_norm_reduction.py
python inherited/verify_rl12_same_direction_canonical.py
python inherited/verify_rl13_p3_j0_interior.py
```

All five are expected to print `PASS`.

## Reading order

1. `RL18_PROOF_STATUS_AND_BRANCH_LEDGER.md`
2. `RL18_REPAIRED_RADIUS3_PROOF_REPORT.md`
3. `RL18_CUBIC_NORM_REDUCTION.md`
4. `RL18_GLOBAL_ORBIT_SUM_IDENTITY.md`
5. `RL18_EXTERNAL_DEPENDENCY_AUDIT.md`
6. `RL18_STRATEGIC_WORKPLAN.md`
7. `NEXT_SESSION_KICKOFF_PROMPT.md`

Do not promote computational evidence to theorem status.  In particular, the old `a<=80` cubic scan remains evidence only; the new norm reduction is analytic, but the needed infinite norm-size obstruction is still open.
