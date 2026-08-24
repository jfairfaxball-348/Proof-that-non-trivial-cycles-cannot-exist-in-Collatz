# RL17 strategic targets: turning local obstructions into an RL contradiction

## Problem

Radius exclusions matter only if the RL-specific grammar forces a hypothetical RL object to encounter them, or if the local arithmetic can be upgraded into a radius-independent obstruction.

The next session should not assume either fact.  It should attempt to prove or falsify concrete bridge statements.

## Rank 1 — distinguished root/return rotation-distance theorem

### Candidate theorem

Find a natural pair (or bounded-size family) of `D`-divisible rotations canonically owned by the RL least-root/final-return structure and prove that two distinct members have transposition distance at most 3.

A useful strong form would be:

> Every primitive RL object has two distinct distinguished `D`-divisible rotations, selected from the least-root/final-return grammar, whose binary words differ by at most three adjacent `01<->10` transpositions.

Do not assume this is true.  First reconstruct the exact ownership/return lemmas (especially the RL-L27/RL-L36/RL-L54 line) and test whether they imply any bounded-distance statement at all.

### If the strong form fails

Produce the smallest explicit combinatorial countermodel satisfying the currently proved root/return constraints while keeping all distinguished rotation distances `>=4`.  A counterexample is progress: it prevents further investment in the wrong bridge and identifies the missing structural hypothesis.

### Weaker targets worth proving

- a distance bound depending on the number of root/return blocks;
- a forced short edge somewhere along the distinguished return chain;
- a bounded **weighted** transposition path even when raw distance is large;
- a pigeonhole theorem forcing two return rotations to share a long suffix/prefix and hence a short sparse difference.

## Rank 2 — weighted multi-edge obstruction

Radius 1--3 calculations may be shadows of a more global identity.  Derive the exact change in `Q` along a path of adjacent transpositions and keep the edge weights instead of collapsing to the path length.

Target a theorem of the form:

> For two distinct primitive `D`-divisible rotations linked by an RL-compatible return path, the weighted transposition identity has a definite sign / size / prime-adic obstruction, irrespective of the number of edges.

Concrete tasks:

1. Write `Q(w')-Q(w)` as a sum over swap edges with exact powers of 2 and 3.
2. Group edges by return/root ownership and look for monotone coefficients or telescoping.
3. Check whether the radius-3 sparse polynomials are the three-edge specializations of a general weighted polynomial.
4. Search for a resultant or lower-bound mechanism depending on total weight rather than support size.

A successful weighted theorem could make exact radius 3 strategically unnecessary even while the local repair is being completed.

## Rank 3 — suffix/xi extension theorem

The older dependency-gap map identifies suffix towers, prefix slack, and `xi` valuation profiles as a separate route to an infinite contradiction.

The useful target is not another finite suffix scan.  It is an extension theorem such as:

> Any admissible RL root/return prefix with the required divisibility/xi profile extends to a strictly stronger suffix constraint; iterating the extension eventually violates a valuation, density, or primitivity bound.

Re-read the older suffix/xi notes only after identifying the exact missing induction invariant.  Prefer a theorem with a monotone quantity over additional computational depth.

## Rank 4 — residual-denominator descent

Try to turn a `D`-divisible rotation identity into a smaller admissible denominator/object.  The challenge is preservation: a formal factorization is useless unless the descendant retains enough RL/root-return structure to iterate.

Target:

> A nontrivial primitive RL solution yields a strictly smaller primitive/admissible RL-type solution with the same essential divisibility grammar.

If preservation fails, document exactly which axiom is lost.

## Required strategic output before the next handover

Before closing the next session, produce at least one of:

- a proved nontrivial bridge lemma;
- a rigorous counterexample to one of the proposed bridge statements;
- a new invariant/identity that genuinely applies at unbounded transposition radius;
- a sharply formulated global theorem with all currently known hypotheses verified and only one explicit missing step.

Do not count a larger finite radius scan or a higher numerical cutoff as fulfilling the strategic requirement.
