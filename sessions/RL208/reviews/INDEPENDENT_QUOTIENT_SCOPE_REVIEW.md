# RL206 independent red team: quotient-residual family and scope

Status: **Completed bounded candidate review.** No tracked files changed.
The root revalidated that incoming RL206 authority is unchanged before this review.
This review uses the repaired `../interfaces/RL206_FROZEN_INTERFACE.md` and does not explore a
new route.

## 1. Verdict and scope of the proposed pivot

The finite-arc parameterization and bounded integer rational-function theorem
in `FINITE_ARC_SCALE_THEOREM.md` are **analytically sound as stated**. The two
minor corollary wording qualifications identified below have been applied and
the corrected artifact was reread. They classify a genuinely
specified family: rational residuals whose integrality and fixed absolute size
bound hold on every sufficiently large compatible integer realization of one
fixed finite arc, without closure or extra global inequalities.

The actual `QUOTIENT_MODULE_THEOREM.md` was subsequently read in full during
CLOSEOUT_LOCK. Its cyclic kernel, explicit unimodular reduction, additive
character classification, and recurrence-zero identity classification all
**PASS** under the exact fixed-word, universal-formal-forcing hypotheses. Its
prominent solution-residue/modulo-`D^2` exception correctly preserves the
limitation identified in section 2 below.

Together these results can support RL206 target option (3) **for these expressly
specified families only**. They provide a precise reason for the prescribed H21
pivot: recurrence compatibility and a bound obtained solely from free finite-arc
transport do not supply the missing independent full-cycle information.

They do not establish an impossibility theorem for all quotient-sensitive
residuals, all phase-linear inequalities using global hypotheses, or arithmetic
after division by `D`. They do not close Gate B and do not supply its absent
exhaustive witness-selection theorem. The pivot is the target-authorized next
research choice after this scoped method barrier, not a theorem that H21 is the
only possible route.

## 2. Independent check of the proposed cyclic module theorem

Fix a word of length `A>=2`, weight `0<L<A`, and `D=2^A−3^L>0`. Put
`a_j=3^(d_j)`. Let the integer matrix `B` encode

`(Bx)_j=2x_(j+1)−a_j x_j`,

with cyclic indices. The ordinary cycle system is `Bx=d`, while general integer
right-hand sides are written `b` to expose the entire additive compatibility
module.

The determinant is `det B=(−1)^(A−1)D`. Deleting the last row and the first
column gives an `(A−1)`-minor of absolute value `2^(A−1)`; deleting the last row
and the last column gives one of absolute value `3^(sum_(j<A−1)d_j)`.
These minors are coprime. Thus the `(A−1)`st determinantal divisor is `1`, and
the Smith invariants are

`1,...,1,D`.

There is also an explicit complete compatibility map. Set

`v_j=2^j 3^(sum_(k>j)d_k)` and
`Phi(b)=sum_j v_j b_j mod D`.

Direct column cancellation gives

`v^T B=D e_0^T`.

Hence `BZ^A` is contained in `ker Phi`. The last coefficient
`v_(A−1)=2^(A−1)` is a unit modulo the odd integer `D`, so `Phi` is surjective.
Both `BZ^A` and `ker Phi` have index `D`, proving equality. Therefore

`b in BZ^A  iff  sum_j v_j b_j=0 modD`.

For `b=d`, the sum is exactly the standard word numerator `Q(w)`. Thus ordinary
integer compatibility is exactly `D|Q(w)`.

Every additive obstruction `chi:Z^A -> G` which vanishes on `BZ^A` factors
through this single cyclic quotient. In particular a claimed independent
additive RHS solvability modulus cannot emerge from integer elimination of the
same equations alone.

### Necessary limitation: solution information is not a cokernel obstruction

The classification above concerns homomorphisms which **vanish on the image**
`BZ^A`. It does not classify all observables defined **on** that image. Once
`b=Bx`, the exact integer quotient

`(sum_j v_j b_j)/D=x_0`

can have nontrivial residues modulo `D` or another modulus. For example, take
`b(k)=B(k e_0)` for varying integers `k`. Every `b(k)` is compatible, while

`(sum_j v_j b_j(k))/D=k`.

Its residue modulo `D` varies. Thus modulo-`D^2` content of the numerator,
or quotient-state residues after exact division, is not erased by the Smith
normal form. This example is a scope check in the general RHS module, not a
family of ordinary Collatz cycles with fixed right-hand side `d`.

Likewise the theorem is per fixed word. It does not rule out a theorem coupling
word coefficients, physical ordering, primitive closure, or independently
proved least-state inequalities across a class of words. A global geometry
consumer added to a recurrence-derived identity is outside the bare additive
solvability classification.

**Safe result name:** “Cyclic recurrence additive compatibility has one full-`D`
obstruction.”

**Unsafe enlargement:** “All linear quotient residuals, integer-state residues,
or quotient-layer modulus arguments reduce to `D|Q` and are useless.”

### Actual module artifact review — PASS

`QUOTIENT_MODULE_THEOREM.md` proves the kernel directly: the exact cyclic
numerators satisfy `2N_(i+1)−a_iN_i=D f_i`, so `D|N_0` propagates to all
coordinates because `2` is invertible modulo `D`. The displayed `N_i/D`
solution and uniqueness proof are correct.

The explicit change of basis was checked algebraically. With
`alpha=c_0`, `beta=c_(A−1)`, `alpha*u+beta*v=1`, its first and last columns
form a determinant-one transformation; each middle column is the stated
elementary subtraction. The displayed inverse rows multiply those columns to
the identity. Thus `det U=1`, and `W=S^(−1)U^(−1)B` is integer with determinant
`(−1)^(A−1)`. Consequently `U^(−1)BW^(−1)=S` is a valid unimodular reduction,
including the admitted `D=1` case. The index/minor proof above is an independent
verification of the same conclusion, not a replacement for checking this text.

Theorem 2's unique character parameter `t` satisfies `Dt=0 modM`; its effective
factor is correctly `m=M/gcd(M,t)`, which divides `gcd(M,D)`. The `t=0` and
multiple-proper-factor cases are handled explicitly. No unsupported condition
`M|D` is assumed.

Theorem 3 defines exactly the annihilator congruences and rational affine zero
identities valid for every formal solution. Substitution `f=Bx` proves its
zero-identity classification directly. The theorem does not silently classify
all expressions that merely look linear on owned states.

Section 5 explicitly proves that `(T(f)/D) modD` is a nonzero map on the image
lattice at `f=B e_0`, and hence outside the annihilator family. Its statement
that the formal-forcing example is not a family of ordinary cycles is correct.
Sections 6–7 retain the globality and finite-verification scope locks.

No required edit to the module proof remains after this independent review.

## 3. Review of the actual finite-arc theorem

Artifact reviewed: `FINITE_ARC_SCALE_THEOREM.md`, sections 1–4.

### Theorem 1 — PASS

For a fixed arc of length `m`, final integrality imposes exactly one residue
`a_0 mod2^m`, since `3^P_m` is odd. The supplied word-composition identity proves
that this final congruence also gives integrality of every earlier prefix.
The exact parameterization

`x_j(t)=a_j+3^(P_j)2^(m−j)t`, `t in Z`,

therefore includes all and only integral trajectories for the prescribed arc.
Reducing each recurrence modulo `2` enforces the stated input parity, so this
is not merely an affine path with incorrect branches. Every slope is positive,
which gives simultaneous positivity for all sufficiently large integer `t`.
No periodic completion is asserted or needed.

### Theorem 2 — PASS

With fixed rational coefficients, substitution gives a one-variable rational
function `f=U/V`, with nonzero polynomial denominator. Integer values under a
uniform two-sided bound occupy a finite set. An infinitely repeated value `c`
makes `U−cV` vanish at infinitely many distinct integers and hence identically.
Thus `f` is the integer constant `c` wherever defined.

The proof establishes constancy on this affine arc, not constancy over different
words, external parameter choices, or arbitrary points in state space.

### Corollary 2a — PASS; conditional fake wording applied

The rational identity extends to every rational point of the same affine arc
where the residual is defined. To instantiate it on the RL20 fake, the arc must
actually be a matching segment of the fake, the fixed external coefficients
must be retained, and the evaluation must be defined. Arbitrary fixed arcs
need not occur in that one prescribed fake.

The requested exact qualification has been applied in the candidate:

> Whenever the fixed arc is a segment of the RL20 fake and the same fixed
> coefficients define the residual at its rational states, the residual has
> that same constant value there. This does not remove an independently imposed
> integer-ownership premise.

The constant can depend on the word or on allowed fixed external parameters.
Constancy therefore does not mean that the constant is automatically zero,
word-independent, or incapable of participating in a separate global theorem.
For example, prefix elimination gives the constant
`2^m x_m−3^P_m x_0=Q(arc)` on every realization. Full closure can then consume
such a constant; that extra step is outside the free-arc theorem.

### Corollary 2b — PASS; same modulus on both statements applied

The corrected candidate names the same positive integer `M` in `M|F` and
`|F|<M`. Their simultaneous
validity on every sufficiently large compatible integer realization forces
zero, because such realizations exist. The corollary supplies no new theorem
that a proposed `M` divides a residual; that implication is an explicit premise
which still has to be proved.

This small-multiple observation is compatible with, and does not replace, the
more informative rational-function constancy theorem.

## 4. Why each arc hypothesis must remain visible

These are qualification checks, not newly proposed routes:

- **Integrality:** `1/(1+x_0)` is a bounded nonconstant rational residual on
  positive arcs, so bounded rational functions need not be constant without
  integer-valuedness.
- **Uniform two-sided scale:** a growing state is integer and nonconstant but
  has a growing bound, e.g. `|x_0|<x_0+1` on positive arcs. A one-sided bound
  alone also fails, as `−x_0<1` illustrates. The fixed `M` must be independent
  of `t`.
- **Rational operations:** remainder or floor operations can give bounded,
  nonconstant integer functions of `t`, e.g. `t mod2`. They are expressly
  outside the family. Valuations are also not rational functions.
- **Enough compatible states:** full closure fixes `D x_0=Q` and hence at
  most one rational value of `t`. The finite-image argument cannot be applied
  to a singleton or empty family of owned cycle states.
- **No unproved global replacement:** least-state inequalities, canonical
  witness selection, and global coupling can restrict the free parameter.
  A bound using such an independently proved restriction is not a bound from
  the local recurrence and positivity alone.
- **Fixed coefficients:** if the formula or its coefficients are permitted
  to vary with `t`, substitution need not produce a single rational function.
- **Defined evaluation:** the pulled-back denominator must not be identically
  zero; statements about points where an expression is undefined are excluded.

## 5. Seven required RL206 red teams

1. **RL20 fake:** integer quotient ownership fails on the fake. The arc theorem
   does not pretend otherwise; its rational constant-value conclusion uses
   only a matching arc and defined evaluation. Rejecting the fake alone does
   not close Gate B.
2. **RL79 rank one:** additive compatibility is consistent with the inherited
   same-modulus rank-one barrier. It does not overreach to quotient residues
   after exact division or modulo-`D^2` data.
3. **Coboundary:** the proposed barrier identifies redundancy from recurrence
   elimination; it does not manufacture a nonzero residual from a telescoping
   identity. The corrected block-lift coefficient is retained.
4. **Proper factor:** the cyclic module uses the full `D`; its cyclic quotient
   is not replaced by a smaller factor. The separate half-word `M` remains
   branch-specific, as in the frozen interface.
5. **Generalized increment:** the review does not equate homogeneous rational
   identities with integer-lattice predicates. Full ownership and solution
   residues remain valid extra information.
6. **Scale:** free local arc scale is parameterized exactly; the constancy
   theorem requires a genuinely uniform bound. No bound is silently extended
   from actual closed cycles to arbitrary arc completions.
7. **Globality:** no global Gate-B witness class, contradiction, rank exclusion,
   or bounded exhaustive reduction is inferred. All global proof-state locks
   remain unchanged.

## 6. Recommended closeout wording

“RL206 proves a scoped recurrence barrier: additive solvability of the cyclic
integer recurrence has the single full-`D` ownership obstruction, and a rational
residual uniformly bounded and integer-valued on every compatible finite arc
must be constant on that arc. These retire transport-only variants in the
specified families. They do not exclude quotient residues, nonrational lattice
operations, or residual bounds using additional global information. Following
the incoming target's option (3), RL207 pivots to H21 independent-information
completion. Gate B and global nontrivial-cycle exclusion remain open.”

## 7. Required correction closeout review

Both root correction notes were read again during CLOSEOUT_LOCK. The required
independent checks pass:

- **RL206-C1:** `RL20_INCREMENT_TARGETED_REPAIR.md` carries the missing factor
  `3^(−E_(j+1))`, conditions strictness on a positive block numerator, and
  explicitly preserves the independently proved height/strip statements. The
  six-bit example and the RL20 fake are correctly identified as all-word
  rational algebra checks, not examples in the near-resonant owned branch.
  This agrees with the exact independent fake check in
  `RL20_BLOCK_LIFT_CORRECTION_CHECK.json` and section 9 of
  `OWNERSHIP_BARRIER_RECOVERY.md`.
- **RL206-C2:** `RL203_SOURCE_TERMINAL_INDEX_REPAIR.md` locates the first
  invalid source/terminal interval comparison and corrects the below-`p`
  necessary offset/depth constants from `39/63/100` to `37/60/97`. Both
  normalized root contributions still vanish modulo `2^56`. The candidate
  distinguishes necessary-rank survival from physical realization and leaves
  the certified necessary-rank set/count unchanged. This agrees with
  `RL203_COORDINATE_REPAIR_INDEPENDENT_REVIEW.md` and its exact six-offset JSON.

These repairs must remain explicit in the promoted correction/proof ledgers;
historical frozen files must not be silently rewritten. They introduce no
additional Gate, rank, eta, or physical-incidence conclusion.

## 8. Final required-review verdict

**PASS — no remaining required mathematical or scope edit in the reviewed
candidate proof/correction artifacts.**

The actual module proof, corrected finite-arc proof, RL206-C1 correction, and
RL206-C2 correction have all been read and independently checked at their
specified scopes. The two arc corollary qualifications are applied. The seven
named RL206 red teams pass for the bounded method-barrier claims, with the
exceptions above expressly retained.

RL206's option-(3) outcome is family-scoped; the H21 pivot follows the incoming
fallback instruction as a strategic choice. Neither a broader all-quotient
impossibility nor a Gate-B success may replace that wording at promotion.
This review does not claim to have performed the root's bundle/manifest/fresh
unpack/remote-promotion gates; those remain separate required closeout steps.
