# RL160 Exact Synthesis Report

## 1. Scope
RL160 asked whether exact identities from earlier stages of the project become newly decisive when combined with the later valuation/reconstruction results and the RL158–RL159 algebraic elimination work.

The answer is a qualified **no for the major local/algebraic shortcut classes**, together with a sharp specification of what a successful crossover must contain.

No claim in this report proves the Collatz conjecture or excludes all non-trivial cycles.

---

## 2. The fixed-radius joint-factorization barrier

Let

\[
\pi_r:\{u\in\mathbb Z: u\text{ odd}\}\to \mathbb Z/2^r\mathbb Z,
\qquad \pi_r(u)=u\bmod 2^r.
\]

Suppose historical local observables `O_1,...,O_k` each factor through the same finite-radius state:

\[
O_i=f_i\circ\pi_r.
\]

Define

\[
F(y)=(f_1(y),\ldots,f_k(y)).
\]

Then the joint observable

\[
O(u)=(O_1(u),\ldots,O_k(u))
\]

satisfies

\[
O=F\circ\pi_r.
\]

### Theorem RL160-A — Joint local observables remain local
If every coordinate in a proposed fixed-radius crossover factors through `u mod 2^r`, then the whole crossover factors through `u mod 2^r`.

### Proof
For every odd `u`,

\[
O(u)=(f_1(\pi_r(u)),\ldots,f_k(\pi_r(u)))=F(\pi_r(u)).
\]

Hence `O=F∘π_r`. In particular, `π_r(u)=π_r(v)` implies `O(u)=O(v)`. ∎

### Consequence
Later valuation reconstruction may show that a collection of local measurements is **complete for the finite dyadic residue state**. That is useful local information, but it does not reverse the old finite-radius barrier. It cannot, by coordinate stacking alone, distinguish different physical integers in the same dyadic fibre or supply a whole-orbit contradiction.

This disposes of the purely local versions of the endpoint/suffix/branch-label/no-carry/valuation-reconstruction crossover.

---

## 3. The ordered-valuation barrier

For a prescribed accelerated odd-step exponent `a≥1`, write

\[
T_a(x)=\frac{3x+1}{2^a}.
\]

For two chronological steps with exponents `(a,b)`,

\[
T_b(T_a(x))
=\frac{3(3x+1)/2^a+1}{2^b}
=\frac{9x+3+2^a}{2^{a+b}}.
\]

Therefore

\[
T_2(T_1(x))=\frac{9x+5}{8},
\qquad
T_1(T_2(x))=\frac{9x+7}{8}.
\]

Both words have valuation multiset `{1,2}` and total valuation `3`, but their affine intercepts differ.

### Theorem RL160-B — Unordered valuation data do not determine affine closure data
The multiset of valuation exponents, and therefore any statistic depending only on their counts or total sum, does not determine the chronological affine numerator produced by composing accelerated Collatz steps.

### Proof
The explicit words `(1,2)` and `(2,1)` are a counterexample. They have identical multisets and sums, yet their composed maps are `(9x+5)/8` and `(9x+7)/8`. ∎

A deterministic replay is provided in `RL160_CERTIFICATES/order_sensitive_affine_composition.py`.

### Consequence
Historical population/count identities cannot be coupled to exact affine cycle closure merely by treating the valuation word as an unordered bag. A surviving bridge must retain chronology or introduce a different global invariant that genuinely depends only on the proposed aggregate.

---

## 4. RL158–RL159 same-root algebraic barrier
RL158 and RL159 already provide exact negative information about a second shortcut class. The one-binomial resultant route and then the joint distinguished-root Sylvester/SNF route remain capable of reconstructing a relation that vanishes because the physical root itself obeys its defining relation. In that setting, adding algebraic equations evaluated at the same distinguished root is not automatically adding independent cycle information.

RL160 therefore marks the following as a dead route **in its current form**:

> same-root polynomial/resultant/Sylvester/SNF stacking without a theorem proving independence from the physical-root algebra.

This is a method barrier, not a statement that all future elimination methods are impossible.

---

## 5. What genuinely independent information remains
The audit separates local completeness from global exclusion. The historical families that can still provide information outside a fixed dyadic residue fibre are:

1. **ownership:** a least-entry, singleton, full-phase, inverse-tree, or physical-representative condition that is not invariant under arbitrary local lifts;
2. **chronological order:** an exact constraint on the ordered valuation word or ordered phase transitions;
3. **population/packing:** simultaneous constraints on many orbit positions;
4. **global identities:** exact cycle product/divisibility, weighted-difference/perimeter, signed defect, or positive-lift relations quantified over a whole orbit.

The highest-value next theorem is therefore not another local coordinate identity. It is a bridge of the form

\[
\text{owned local phase}\Longrightarrow
\text{quantitative global burden}\Longrightarrow
\text{incompatibility with exact cycle closure}.
\]

---

## 6. Negative-audit closure
RL160 meets its target by the negative-audit promotion gate:

- the principal fixed-radius coordinate crossovers are formally collapsed to the same residue state;
- unordered valuation data are proved insufficient for ordered affine closure;
- the RL158–RL159 same-root algebraic route is retained as a certified method barrier;
- the surviving crossover search is reduced to ownership-sensitive/global or genuinely chronological information.

### Final mathematical status
**No finite-cycle contradiction has been obtained.** The global non-trivial-cycle exclusion theorem remains open. The exact advance is a narrower and more auditable search space for RL161+.
