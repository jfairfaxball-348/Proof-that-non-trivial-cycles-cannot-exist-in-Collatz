# RL47 Radius-3 Bridge and RL-Closure Roadmap

Date: 2026-08-22

## 1. What is already closed and what is not

The inherited program treats the exact radius-3 theorem as already closed/audited. The unresolved problem is not to re-prove radius 3. It is to prove that a surviving RL phase configuration is forced into the arithmetic situation to which that radius-3 closure applies.

RL45 identified the relevant one-excursion objects:

- short binomial `f(T)=3T^q-2`, with `q=a-ell`;
- comparator `L(T)=2T^ell-1`, satisfying the exact resultant identity `Res(f,L)=2^a-3^ell=X-Y`;
- phase polynomial `P(T)` coming from the full-denominator phase condition.

The naive plan `|Res(f,P)|_(3') < X-Y` is false, by an exact `(65,41)` countermodel. Therefore the bridge must be **same-root arithmetic**, not an absolute resultant-size estimate.

## 2. The two remaining closure gates

A credible RL closure currently requires two logically distinct gates.

### Gate A — uniform one-excursion area theorem

Prove, for every genuine retained terminal geometry,

`H >= t+3 = v2(T+1)`.

This gives the required excess/rank inequality `e>=q+2` in the live one-excursion branch.

RL47 materially narrows this gate:

- neutral `11` motion is quotiented exactly by `Phi`;
- `H` is exactly total rank displacement;
- q=79 is now certified;
- the rank-transport relaxation eliminates entire high-t tails analytically.

The main analytic target is now to turn the finite-pair rank envelope into a **uniform geometric-series inequality** using only near resonance, prefix cap, and the total displacement budget.

### Gate B — same-root radius-3 bridge

Use the full phase condition, not merely the proper-factor geometry, to show that a prime divisor of `X-Y` cannot support the required **same root** of `f`, `L`, and `P` unless the radius-3 forbidden/unique configuration occurs.

A plain gcd of `Res(f,P)` and `Res(f,L)` is insufficient because the two resultants can acquire the same prime from different roots of `f`. The missing object should therefore be a three-polynomial subresultant/Bezout certificate, or an equivalent root-specific congruence.

The proof-ready bridge lemma should have a form similar to:

> For every prime power dividing `X-Y` in the retained branch, if `rho` is the root selected by the full denominator so that `f(rho)=L(rho)=0`, then the phase condition `P(rho)=0` forces a radius-3 configuration already excluded by the audited radius-3 theorem.

This wording is a **target**, not a theorem. The next session must reconstruct the exact inherited radius-3 hypotheses before finalizing the statement.

## 3. Why the new rank-transport identity may connect the gates

RL45 proved that after reduction modulo `f`, distinct one-runs occupy distinct residue classes and the reduced run coefficients are positive. RL47 now adds

`H = sum_j delta_j`, with `delta_j=a_j-b_j>=0`,

and

`14 + (27/2) zeta (1-2^-k)`

`= sum_j (2^a_j/3^j) (3-2^-delta_j)`.

Under a hypothetical low-area counterexample, the total displacement `sum delta_j` is small. Therefore the full phase data is a low-total-displacement perturbation of the synchronized (`delta_j=0`) rank arrangement.

This suggests a concrete bridge program:

1. express the reduced phase polynomial `P mod f` directly in terms of rank positions and displacements `delta_j`;
2. isolate the synchronized baseline and a defect polynomial supported only where `delta_j>0`;
3. use the prefix-cap envelope to show the high-weight ranks have extremely limited displacement;
4. derive a root-specific congruence for the defect at the common root of `f` and `L`;
5. compare that congruence with the exact short-binomial/radius-3 uniqueness mechanism.

The key point is that RL47 has changed “phase complexity” from an opaque run polynomial into a transport budget. If the bridge exists in this branch, this is currently the most promising common language for the combinatorial and algebraic sides.

## 4. Recommended RL48 attack order

### Priority 1: prove a uniform rank-transport inequality

Start from the exact relaxed verifier and replace each finite coordinate bound by a symbolic bound. In particular:

- derive an explicit upper bound for `2^a_j/3^j` from the prefix cap;
- sum the synchronized baseline as a geometric series;
- optimize the displacement enhancement with total budget `t+2` analytically;
- compare with `14+(27/2)zeta(1-2^-(t+3))` uniformly over the retained zeta window.

If successful, this closes Gate A without further q-by-q computation.

### Priority 2: reconstruct the radius-3 same-root hypotheses exactly

Do not rely on memory or analogy. Pull the exact radius-3 theorem and the RL43/RL44 phase polynomial definitions from inherited provenance if available; otherwise state precisely what additional historical handover is required. Identify the exact root, modulus, coefficient ring, and prime-power multiplicity statements.

### Priority 3: derive the defect polynomial in rank-displacement variables

Translate the one-run reduction modulo `f` into `(a_j,b_j)` / `delta_j` notation. Check whether low total displacement forces:

- small support;
- bounded subresultant degree;
- a restricted Bezout coefficient;
- or a congruence with the short radius-3 polynomial.

Do not assume that low `H` means radius <=3; prove any support compression quantitatively.

### Priority 4: attack a root-specific subresultant lemma

The intended output should be one exact lemma, with hypotheses matching the live RL branch, whose proof plus the already-audited radius-3 theorem yields a contradiction.

A useful success criterion for the session is not necessarily full closure; it is acceptable to end with a theorem of the form:

> RL closure now reduces to Lemma X, an explicit inequality/subresultant divisibility statement involving only `f,L,P` and the rank-displacement budget.

That would be much closer to closure than extending q=134 by brute force.

### Priority 5: use q=134 only as a falsification laboratory

The unresolved q=134 strip is valuable for testing proposed invariants. Do not make finishing q=134 the main goal unless the new invariant makes it cheap. A uniform theorem is worth far more than a larger finite certificate.

## 5. How close is the program now?

The radius-3 theorem itself is not the present bottleneck. The program has progressed from a vague need for a bridge to two sharply identified missing statements.

A next session can realistically get **very close to a proof-ready radius-3 bridge** if it succeeds in writing the phase remainder in rank-displacement variables and derives a same-root subresultant/Bezout condition. That would reduce the bridge to one explicit quantitative lemma rather than an open-ended idea.

A complete RL closure in one further session is **possible but should not be expected**. It would require a genuine uniform argument for Gate A and a valid same-root theorem for Gate B, with all inherited radius-3 hypotheses checked. Neither is currently proved. The q=79 closure and the new transport identity are strong evidence that Gate A is becoming tractable, but they do not by themselves imply the global theorem.

The most plausible one-session high-water mark is therefore:

- close Gate A analytically, or reduce it to a single clean scalar inequality; and
- formulate/prove most of Gate B up to one precise root-specific arithmetic lemma.

If both unexpectedly collapse under the new transport formulation, RL could close; otherwise the correct outcome is a much smaller, auditable final lemma rather than another long chain of computational evidence.
