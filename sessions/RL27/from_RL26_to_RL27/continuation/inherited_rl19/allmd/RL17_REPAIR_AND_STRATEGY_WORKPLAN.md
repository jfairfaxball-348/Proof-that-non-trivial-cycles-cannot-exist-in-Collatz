# RL17 next-session workplan

## Objective

Repair the exact-radius-3 proof chain **and** extract a route that can matter globally for RL.  The session should end with a new handover that is stricter than this one: every claimed closure must have a proof note, every finite computation must have an executable verifier, and the global bridge status must be explicit.

## Phase 0 — establish the working ledger

1. Read the RL17 audit freeze and branch ledger.
2. Rerun all four directly relevant verifiers:
   - RL16 main closure verifier;
   - RL16 cubic-cofactor verifier;
   - RL17 full-D sparse verifier;
   - RL17 `a<=80` scan.
3. Unpack the RL15/RL14/RL11 lineage only as needed.
4. Reconstruct the exact radius-3 case tree on one page, with each leaf carrying one of: `CLOSED`, `OPEN`, `PROOF NOTE MISSING`, `EXTERNAL`, `FINITE ONLY`.

**Exit condition:** no branch is removed merely by a roadmap sentence or unnamed symmetry.

## Phase 1 — repair proof provenance before extending conclusions

### 1A. RL12

Reconstruct the analytic derivation behind the verifier, especially the infinite envelope(s) that reduce the three-orbit branch to a finite check.  Freeze a proper theorem/proof note and explicitly state any external logarithmic-form input.

### 1B. RL13

Reconstruct the `j=0,P3` strict-interior proof, including the near-density bound `D^6<569^L`, far-density resultant regime, monotonicity, cutoff, and exact finite tail.

If either derivation cannot be justified, downgrade that leaf to OPEN and work on the missing inequality rather than retaining the old status.

**Exit condition:** scripts are certificates for a written reduction, not substitutes for it.

## Phase 2 — fix the two branches silently dropped by the old roadmap

### 2A. Coefficient-3 P2 boundary — first priority

Attack simultaneously the `j=1` and `j=2` P2 boundaries:

\[
3+4\sigma^t\equiv0\pmod D.
\]

Preferred route:

1. recover the RL12 root reformulation `theta^k=-1` exactly;
2. split parity/order cases cleanly;
3. use Jacobi/order arguments where possible;
4. if a residual family remains, seek a binomial resultant against the relevant short-defect polynomial and derive an LMN-compatible exponential barrier;
5. freeze a verifier only after the infinite reduction is written.

**Target:** one theorem covering both P2 boundary leaves.

### 2B. Cubic three-orbit sector

Analyze

\[
\gcd(A,L)=3,\qquad \gcd(A,m)=3.
\]

First normalize `A=3a`, `L=3ell`, `m=3n` and determine whether the rotation action descends to length `a` or to three coupled `a`-orbits.  Test whether primitivity forces a repetition, or whether an RL12-type three-orbit sparse polynomial appears with a modified modulus.

Use `(10)^3` as a sanity check: any theorem that purports to rule out the sector without invoking primitivity or an equivalent condition is false.

## Phase 3 — exploit the stronger full-D cubic lemma

The full-D promotion is now available.  Do not retreat to the weaker cofactor statement unless a proof step specifically needs factorization in `C`.

Attack

\[
1+3\rho^u+9\rho^{u+v}\equiv0\pmod D,
\qquad u+v+w=3a.
\]

Promising routes, in order:

1. **Conjugate/factor route:** compare the equation after multiplication by the cubic phase `omega`; eliminate `rho` or one gap and look for a factor divisible by `X-Y`.
2. **Resultant route:** treat one normalized gap variable as an exponent/root and combine with `rho^a=(1/3)omega^m`; seek a nonzero integer resultant whose size is `<D` away from equal spacing.
3. **Order/norm route:** exploit `D=(X-Y)C`, Chinese-remainder behavior when the factors are not coprime, and the fact that the equation must vanish simultaneously on the residual factor and cubic factor.
4. **Geometry route:** use actual binary jump realizability to eliminate arithmetic sparse zeros before trying to classify all modular zeros.

The finite `a<=80` scan is a pattern detector only.

**Target:** prove sparse uniqueness, or derive a strong reduction that leaves one explicitly parameterized infinite subfamily.

## Phase 4 — protected global strategy work

After making a serious repair attempt, switch to the global bridge even if radius 3 is not fully closed.

### 4A. Test the distinguished root/return bridge

Formulate the strongest precise statement actually suggested by RL-L27/RL-L36/RL-L54.  Attempt both proof and falsification.  Compute only to find counterexamples or conjecture the correct bound; do not substitute a scan for a theorem.

### 4B. In parallel derive a weighted transposition identity

Abstract the radius-3 `Q` difference into a path formula valid for arbitrary support.  Ask whether RL return paths impose coefficient signs/order that make divisibility impossible independently of radius.

### 4C. Only then revisit suffix/xi or residual descent

Use the dependency-gap map to identify whether either route now has a sharper induction invariant supplied by the rotation work.

**Strategic exit condition:** the session must leave behind at least one concrete global theorem attempt, counterexample, or unbounded-radius invariant.  “Radius 3 is closer” is not enough.

## Phase 5 — closeout discipline

Before handing to another agent:

1. rerun every verifier touched;
2. create a SHA-256 manifest;
3. update the proof-status table and branch tree;
4. separate analytic proof, external theorem, exact finite certificate, and experiment;
5. state two distances separately:
   - distance to exact-radius-3 closure;
   - distance to RL closure;
6. include a `NEXT_SESSION_KICKOFF_PROMPT.md` that starts from the new frontier rather than repeating this work;
7. if a bridge candidate failed, preserve the counterexample and remove the false route from the roadmap.
