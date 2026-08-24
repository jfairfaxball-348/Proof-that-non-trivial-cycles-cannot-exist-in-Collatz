# RL18 strategic workplan for the next session

## Primary objective

Do not spend the next session re-auditing already repaired branches unless a verifier fails.  Attack the **single remaining radius-3 leaf** and, in parallel, try to turn the new orbit-sum identity into a global RL obstruction.

## Track A — close the one remaining radius-3 leaf

Target:

`1+3rho^u+9rho^(u+v)=0 (mod D)`, `u+v+w=3a`,

in the `gcd(A,L)=3,gcd(A,m)=1` sector.

### A1. Start from the RL18 Eisenstein norm, not the old finite scan

Center the gaps and use

`C | Num[(q^d-1)^2-(q^d-1)(q^t-1)+(q^t-1)^2]`

for every hypothetical skew zero.

Try to prove a size obstruction by separating sign patterns of `(d,t)`:

- `d,t>=0`;
- `d,t<=0`;
- opposite signs.

Clear denominators minimally in each region rather than with one crude global factor.  Compare the resulting numerator directly with `C=X^2+XY+Y^2`.

### A2. Exploit `ap-mell=1`

Do not treat `q=2^m/3^p` as a free positive rational.  Use the exact Bezout relation to convert powers such as `q^a` into expressions involving `X/Y` and the cubic phase.  Search for a second norm/resultant that drops the exponent size from `O(a)` to centered deviations.

### A3. Use actual rotation geometry

If the arithmetic statement is false for arbitrary positive gaps, classify arithmetic counterexamples and ask whether they satisfy the event/jump realizability conditions.  A geometry-assisted theorem is sufficient; proving uniqueness for every formal triple is stronger than necessary.

### A4. Required exit

Either:

- prove full skew uniqueness; or
- leave one sharply parameterized infinite subfamily with a stated missing inequality; or
- produce an exact arithmetic counterexample showing that a geometry hypothesis is indispensable.

A larger `a` scan alone does not count.

## Track B — use the unbounded-radius orbit identity on RL grammar

### B1. Reconstruct the RL-specific hypotheses exactly

Return to the least-root/final-return lemmas (especially the RL-L27/RL-L36/RL-L54 line in the older lineage).  Write down only what is actually proved about the distinguished rotations, return chain, prefix-flow signs, and ownership.

### B2. Substitute them into the orbit polynomial

For each distinguished return shift, compute the symbolic shape

`sum rho^k 3^(-S_k)`

implied by the proved prefix-flow constraints.

Look for one of four radius-independent obstructions:

1. a positive/one-sided coefficient pattern giving a size contradiction;
2. an Eisenstein/cyclotomic norm structure analogous to the cubic leaf;
3. an order/Jacobi obstruction after grouping equal levels of `S_k`;
4. a resultant whose degree/height depends on flow variation rather than raw radius.

### B3. Falsify the bounded-radius bridge early

If older notes suggest that two distinguished RL rotations must lie within transposition radius 3, test that exact theorem against the proved grammar.  If it is false, preserve the smallest countermodel and remove the route.  Do not assume radius-3 closure automatically matters globally.

## Track C — theorem-dependency hygiene

Before invoking any named theorem:

- check `RL18_EXTERNAL_DEPENDENCY_AUDIT.md`;
- add a bibliographic source and exact specialization if new;
- distinguish conjecture from theorem;
- never refer to “Jacobian” when “Jacobi symbol” is meant.

## Verification discipline

At session start run all five bundled verifiers.  At closeout rerun every changed verifier and regenerate the SHA-256 manifest.

## Desired next handover

The next bundle should state separately:

1. **radius-3 status** — whether cubic skew uniqueness is closed;
2. **global RL status** — what theorem actually connects arbitrary RL return structure to a contradiction;
3. **external dependencies** — exactly which published theorems are used;
4. **finite evidence** — clearly separated from proof.
