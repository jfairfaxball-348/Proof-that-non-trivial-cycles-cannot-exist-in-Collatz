# RL16 audit status, distance to RL, and candidate route

Date: 2026-08-20

## 1. Executive assessment

The project has made a real structural advance: the generic exact-radius-3 arithmetic has been narrowed very heavily.  According to the inherited RL11--RL16 case decomposition, all coprime same-direction radius-3 pieces and the mixed / three-orbit pieces are now closed, leaving the `gcd(A,L)=3` cubic-cofactor branch as the main radius-3 obstruction.

However, there are **two distinct distances** that must not be conflated:

- **Distance to closing exact radius 3:** apparently one major analytic branch, namely the cubic-cofactor converse, assuming the case decomposition is exhaustive and all previous closures survive audit.
- **Distance to closing RL:** larger.  Even a complete exact-radius-3 exclusion does not yet supply the global RL contradiction.  The inherited RL9 theorem says primitive `D`-divisible rotations cannot occur at transposition distance 1 or 2; radius-3 exclusion would push that obstruction further.  What is still missing is a bridge from the RL-specific least-root/final-return grammar (or another global mechanism) to a forbidden short rotation / bounded path, or an alternative infinite extension theorem.

So the project may be **close to a clean radius-3 theorem**, but it is **not justified to say RL is one lemma away**.

## 2. Frozen radius-3 chain

| Stage | Frozen status | What it contributes |
|---|---|---|
| RL7--RL9 | Analytic | Distances 1 and 2 between distinct primitive `D`-divisible rotations are excluded; exact radius 3 becomes the next transposition target. |
| RL10 | Analytic classification + finite audit | Exact radius-3 flow is classified into support `[3]`, `[2,1]`, `[1,1,1]`; connected `[3]` is excluded; sparse/common-base forms are derived. |
| RL11 | Analytic + external LMN + exact finite certificate | Entire mixed-direction radius-3 branch excluded; same-direction equal-arc cover normal form derived. |
| RL12 | Analytic/certificate in inherited baseline | `gcd(A,m)=3` same-direction three-orbit branch closed. |
| RL13 | Analytic/certificate in inherited baseline | coprime `j=0, P3, [1,1,1]` strict interior closed. |
| RL14 | Analytic + LMN/certificate where stated | coprime `j=1, P2` strict interior closed; all two-equal-gap `j=1,P3` interiors closed; useful descent/resultant lemmas. |
| RL15 | Analytic + external LMN + exact finite certificate | complete coprime `j=1,P3,[1,1,1]` strict interior closed, including scalene cases. |
| RL16 main | Analytic + external LMN + exact finite certificate | coefficient-5 `P3 [2,1]` boundary closed for `j=0,1`; coprime `j=2,P2,[1,1,1]` strict interior closed. |
| RL16 cofactor | Analytic reduction + structural audit | `gcd(A,L)=3`, one-orbit same-direction branch implies sparse `1,3,9` congruence modulo cubic cofactor `C`; exact `a,a,a` spacing is singular. Converse remains open. |

### Audit requirement

The table above records the inherited claim structure; it is not a substitute for an exhaustiveness proof.  The review session should explicitly reconstruct the radius-3 case tree and check that after RL16 there is no omitted coprime boundary/orientation/support case hidden by reciprocal or cyclic identifications.

## 3. What RL16 actually proves

### RL16 main closure

The verifier freshly reruns to PASS.  Important exact outputs include:

- `j=0, P3 [2,1]`: LMN cutoff `L<189000`; only two continued-fraction candidates in the large finite band and both fail; eight small barrier pairs lead to 73 exact boundary tests and zero zeros.
- `j=1, P3 [2,1]`: LMN cutoff `L<25000`; 3,800 exact parameter pairs; zero barrier survivors.
- `j=2, P2 [1,1,1]`: LMN cutoff `L<78000`; 11,852 exact parameter pairs; only `(8,5)` and `(65,41)` survive the coarse barrier; 786 exact strict simplices produce zero zeros.

These closures depend on the same published Laurent--Mignotte--Nesterenko two-logarithm estimate inherited from RL11.  An audit should verify the exact theorem statement/constants and every monotonicity/cutoff step rather than treating the Python assertions as a proof of the external theorem.

### RL-L104 cubic-cofactor reduction

For `A=3a`, `L=3ell`, `gcd(a,ell)=1`, with cubic cofactor

\[
C=2^{2a}+2^a3^\ell+3^{2\ell},
\]

RL-L104 derives, in the one-orbit same-direction branch,

\[
\rho^\alpha+3\rho^\beta+9\rho^\gamma\equiv0\pmod C.
\]

The phase cancellation is analytic.  The included finite audit checks the structural identities on 1,359 exact one-orbit structural solutions through `A<25`.  Exact spacing by `a` makes the sparse form vanish because it reduces to a cubic-root identity.

The missing theorem is the converse:

\[
\rho^\alpha+3\rho^\beta+9\rho^\gamma\equiv0\pmod C
\quad + \quad \text{actual rotation geometry}
\quad\Longrightarrow\quad
\beta-\alpha=\gamma-\beta=a.
\]

If proved in the primitive setting, the inherited repetition/descent theorem RL-L48 is expected to eliminate the branch.

## 4. Important audit correction: session leads that are not frozen

Two stronger claims appeared in conversation after the packaged RL16 note:

1. that the sparse congruence can be promoted from modulo `C` to modulo the full discrepancy `D`;
2. that a pure arithmetic scan through `a<=80`, covering 2,785 admissible parameter choices, found exactly one normalized sparse zero, always equal-gap.

Neither claim is represented by a note/verifier/log in the supplied RL16 files.  Therefore the audit bundle deliberately labels them **UNVERIFIED SESSION LEADS**.  A review session may try to reconstruct them, but they must not be used as premises before reproduction.

## 5. Distance to closing exact radius 3

Subject to audit of the case partition, the remaining route is unusually narrow:

1. Re-derive RL-L104 independently and decide whether the modulus can be strengthened from `C` to `D`.
2. Normalize jump times, for example by setting `u=beta-alpha`, `v=gamma-beta`, `w=3a-u-v` (with the actual cyclic/geometric constraints).
3. Prove uniqueness of the sparse zero at `(u,v,w)=(a,a,a)`, or derive a proper-factor/resultant inequality that excludes every skew triple.
4. Convert equal spacing to exact third repetition and apply RL-L48 / primitive descent.
5. Re-audit the radius-3 case tree to certify that this closes the final exact-radius-3 branch.

Promising proof mechanisms for step 3 include cubic norm factorization, conjugating by `omega`, subtracting the two conjugate sparse equations, resultants in a normalized gap variable, or a size/divisibility comparison that uses the full `D` if the stronger modulus is valid.

## 6. Why radius-3 closure is not yet RL closure

The global RL project predates the radius-3 subprogram.  Its older dependency map identifies open infinite-structure problems involving suffix towers, prefix slack across cycle rotations, xi valuation profiles, and the need for a genuine extension theorem.

The transposition program changed the landscape by proving:

- distance 1 impossible (except the already-excluded Christoffel mechanism),
- distance 2 impossible,
- many/all radius-3 branches now impossible.

But the missing global statement is not “all primitive rotations have distance at least 4.”  To contradict RL, one still needs to show that **the specific rotations forced by an RL candidate** must be connected by a path in the forbidden range, or obtain an independent global contradiction.

The inherited roadmaps repeatedly name the natural bridge:

> prove a distinguished-rotation theorem for the least-state/root-departure and final-return rotations using RL-L27/RL-L36/RL-L54, or prove a weighted multi-edge obstruction whose exact numerator change lies strictly between `0` and `D`.

No such global bridge is frozen in RL16.

## 7. Candidate route from here

### Route A — finish radius 3 first

This is the cleanest local research objective:

- prove the cubic-cofactor sparse-zero converse;
- certify full radius-3 exhaustiveness;
- promote “primitive cycle rotations have distance >=3” to “no exact radius-3 self-rotation”, hence a stronger distance lower bound.

This is valuable even if it does not close RL because it sharply constrains any future distinguished-rotation theorem.

### Route B — immediately audit the global bridge

In parallel, check whether the accumulated RL root/return grammar now forces a distinguished pair into radius <=3.  If yes, then radius-3 closure plus that bridge could become a near-complete RL route.  If no, quantify the smallest radius/path length actually forced.  This prevents spending months proving radius-4, radius-5, ... generic classifications without evidence that RL needs them.

### Route C — abandon generic radius escalation if no bridge appears

Return to the older global mechanisms: suffix-tower extension, prefix/slack transport across all rotations, xi-profile cycle automata, or residual-denominator descent.  These attack RL directly and may use the radius-3 theorems as local constraints rather than as an endless hierarchy.

## 8. Audit questions that should be answered before new claims

1. Is the RL10--RL16 radius-3 case decomposition genuinely exhaustive after all symmetry/gcd/orientation identifications?
2. Are every one of the resultant nonvanishing claims valid over the exact rings/moduli used, with no hidden unit/gcd assumption?
3. Is the inherited LMN theorem quoted with correct hypotheses and constants, and do all cutoff/Legendre steps follow rigorously?
4. Are the finite certificates complete supersets of every analytic survivor and based only on exact integer arithmetic where claimed?
5. Does RL-L104 really follow from `C|Q`, and is any converse possible from `C` alone?  Are there arithmetic skew zeros not realized by binary geometry?
6. Can the sparse congruence be strengthened to modulo `D`?  If so, write and verify the exact derivation.
7. Exactly what theorem would turn “radius 3 closed” into “RL closed”?  Is that bridge already implicit in RL-L27/RL-L36/RL-L54, or is it still a major independent theorem?
8. If the bridge is not radius <=3, what is the smallest structurally forced path radius, and is generic radius classification still a sensible strategy?

## 9. Recommended audit verdict vocabulary

Use only these labels in the review:

- **PROVED ANALYTIC** — infinite argument self-contained in the project notes;
- **PROVED + EXTERNAL** — depends on a named external theorem such as LMN;
- **EXACT FINITE CERTIFICATE** — exhaustive finite check after a proved cutoff;
- **COMPUTATIONAL EVIDENCE** — finite scan without an infinite theorem;
- **UNVERIFIED SESSION LEAD** — claimed in conversation but not frozen/reproduced;
- **OPEN** — required theorem not yet established.
