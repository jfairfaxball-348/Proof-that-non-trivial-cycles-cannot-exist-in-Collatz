# RL82 target — RL♭ / cycle maximum and backward ownership

Date: 2026-08-24

## Purpose

The project originally grew from asking what must be true of the distinguished low/entry-side cycle state (`R#` / the first-number viewpoint). RL82 deliberately flips that perspective.

Define, as **new working notation for this attack**,

`RL♭ = M = max C`,

where `C` is a hypothetical nontrivial positive periodic orbit of the ordinary shortcut Collatz map

`T(n)=n/2` for even `n`,

`T(n)=(3n+1)/2` for odd `n`.

Do not cite `RL♭` as an inherited historical notation unless an older source is later found using it. In RL82 it simply means the maximum state of the cycle.

The central idea is that **maximality itself is an ownership condition**. When the orbit is reconstructed backwards from `M`, every candidate predecessor must both be a legal Collatz predecessor and remain `<=M`. That inequality can rule out whole inverse branches which are locally legal in the unrestricted inverse Collatz graph.

The first two backward steps already give more than parity.

---

## 1. Exact kickoff lemmas

These are elementary analytic deductions for a hypothetical **nontrivial positive** shortcut-Collatz cycle. They are included so the RL82 session starts from the sharpened top geometry rather than re-deriving only “the maximum is even”.

### Lemma 1 — the cycle maximum is even

Let `M=max C`.

If `M` were odd and `M>1`, then

`T(M)=(3M+1)/2 > M`,

contradicting maximality. Therefore

`boxed: M is even.`

The trivial positive cycle `{1,2}` has maximum `2`; RL82 is concerned with a hypothetical nontrivial positive cycle.

### Lemma 2 — the immediate predecessor of the maximum is odd

Let `P` be the state immediately before `M` on the cycle.

If `P` were even, then `M=P/2`, so `P=2M>M`, contradicting maximality.

Hence `P` is odd and

`M=(3P+1)/2`,

so

`boxed: P=(2M-1)/3}`

and necessarily

`boxed: M == 2 (mod 3).}`

### Lemma 3 — the second predecessor is also forced odd

Let `Q` be the state immediately before `P`.

If `Q` were even, then `Q=2P`. Since `Q<=M`, one would have

`2P <= (3P+1)/2`,

which forces `P<=1`.

But `P=1` gives `M=2` and hence the trivial `{1,2}` cycle. Therefore in a nontrivial positive cycle `Q` cannot be even.

Thus `Q` is odd and

`P=(3Q+1)/2`.

Consequently

`boxed: M == 8 (mod 18).}`

Writing

`boxed: M=18r+8,}`

one gets the exact top triple

`boxed: Q=8r+3 -> P=12r+5 -> M=18r+8.}`

In particular

- `M == 8 (mod18)`;
- `P == 5 (mod12)`;
- `Q == 3 (mod8)`.

The forward parity pattern immediately into the maximum is therefore necessarily

`11 0`

(two odd states followed by the even maximum).

### Lemma 4 — the next backward layer already splits by `r mod 3`

Let `R` be the predecessor of `Q` on the cycle.

There are only two local inverse possibilities:

- even predecessor: `R=2Q=16r+6`;
- odd predecessor: `R=(2Q-1)/3=(16r+5)/3`, which is integral exactly when `r==1 (mod3)`.

If the even predecessor is used, then `R>M/2`, so the predecessor of `R` cannot itself be even (that would exceed `M`). It must be odd, which requires

`R==2 (mod3)`,

and this is equivalent to

`r==2 (mod3)`.

Therefore

`boxed: r != 0 (mod3).}`

Equivalently the maximum of a hypothetical nontrivial cycle must satisfy the sharper necessary condition

`boxed: M == 26 or 44 (mod54).}`

The two surviving backward top grammars begin as follows.

**Branch A: `r==1 (mod3)`**

The actual predecessor of `Q` must be the odd inverse; the competing even inverse has no legal predecessor `<=M`.

**Branch B: `r==2 (mod3)`**

The predecessor of `Q` must be even, and its own predecessor is then forced odd.

This is the first example of the intended RL82 mechanism: **a locally valid inverse branch is rejected because it cannot be embedded in a cycle whose global maximum is `M`.**

Classification of Lemmas 1–4: **elementary analytic theorems**, independent of the RL machinery.

---

## 2. Exact backward-ownership operator

For a fixed candidate maximum `M`, define the bounded predecessor set

`Pred_M(x)`

for a cycle state `x<=M` by the two possible shortcut-Collatz inverse branches:

1. even predecessor `2x`, allowed only if `2x<=M`;
2. odd predecessor `(2x-1)/3`, allowed only if `x==2 (mod3)` and the resulting integer is positive odd.

For an actual periodic orbit with maximum `M`, the preceding cycle state must lie in `Pred_M(x)`.

This gives a deterministic pruning rule:

- if `Pred_M(x)` is empty, the proposed backward branch cannot belong to a cycle with maximum `M`;
- if `Pred_M(x)` has one element, that predecessor is forced;
- if it has two elements, both branches must be interrogated for further predecessor extendability under the same cap `M`.

The primary RL82 object should be the **backward ownership tree under the hard ceiling `M`**, not the unrestricted inverse Collatz tree.

---

## 3. Primary question

# How much exact arithmetic and parity structure is forced backwards from the fact that `M` is the maximum state of a nontrivial cycle?

The target is not merely to list a few residues. Seek a scalable theorem showing that maximality forces one of:

- an impossible infinite backward continuation;
- rapidly shrinking residue cylinders for `M`;
- a forced parity grammar incompatible with cycle closure;
- a quantitative contradiction between the top block and global cycle counts/product identities;
- a bridge from the top block to the existing RL/full-phase geometry.

---

## 4. Required investigations

### 4.1 Build the symbolic backward automaton

Starting from `M`, derive predecessor states symbolically as affine/rational functions of `M` or of the natural parameter `r=(M-8)/18`.

At every node impose simultaneously:

- exact inverse Collatz integrality;
- required parity;
- positivity;
- the ceiling condition `state<=M`;
- existence of at least one further predecessor `<=M` unless cycle closure has already been established.

Prefer symbolic congruence classes over brute-force scans of numerical maxima.

### 4.2 Determine the longest universally forced top word

The first two predecessors are universally odd for a nontrivial cycle.

Determine whether further predecessors become forced after splitting by residue classes of `M`, and whether repeated pruning yields a finite-state residue automaton modulo powers of `2` and `3`.

Track exact parity words immediately before the maximum. Do not assume the branch must remain all odd.

### 4.3 Exploit “state > M/2” as a forced-odd-predecessor region

For any current state `x>M/2`, an even predecessor `2x` would exceed the maximum and is impossible. Therefore any predecessor must be the odd inverse, which additionally requires `x==2 (mod3)`.

This creates a simple but potentially powerful top-zone rule:

`boxed: x>M/2 => predecessor is forced odd, hence x==2 (mod3).}`

Investigate excursions of the backward chain in and out of this top half and whether return to the top half forces a residue contradiction.

### 4.4 Search for monotone ratios or top-zone barriers

Normalize backward states by `M` and study the two inverse branches:

- even inverse roughly doubles the ratio;
- odd inverse roughly multiplies it by `2/3`.

The additive `-1/3` term is essential and must not be discarded if the argument is intended to be ordinary-Collatz specific.

Look for exact intervals in which only one inverse branch is compatible with maximality, then propagate those intervals symbolically.

### 4.5 Derive top-specific congruence ladders

The forced top triple already gives `M==8 mod18`; one additional predecessor layer strengthens this to `M==26 or44 mod54`.

Investigate whether deeper backward ownership yields a nested family

`M in R_j (mod 2*3^j)`

or related mixed `2`/`3` residue cylinders whose density shrinks fast enough to interact with another global cycle condition.

A residue ladder alone is not closure. Identify its intended global consumer.

### 4.6 Connect top geometry to global cycle identities

Only after the top automaton is exact, test it against established global facts such as:

- counts of odd/even shortcut steps in a cycle;
- the standard cycle product/denominator relation `2^a-3^ell`;
- minimum-state or verified-floor bounds;
- the RL48 full-phase physical states if a genuine ownership correspondence can be proved;
- existing Gate-A terminal structure if the top block can be located within that geometry.

Do not guess that `RL♭` equals the RL48 midpoint `N`, `N+4`, or any auxiliary `J` coordinate. Any such identification must be proved.

### 4.7 Compare top and bottom viewpoints

The strategic reason for this route is the asymmetry:

- at a minimum/entry state, forward growth is constrained from below;
- at the maximum, **backward preimages are constrained from above**.

Seek a theorem that uses both extremal ends of the same hypothetical cycle, rather than treating the top analysis as an isolated modular exercise.

### 4.8 Ordinary `+1` red-team

The top formulas are genuinely non-homogeneous. For the generalized odd rule

`T_s(n)=(3n+s)/2`,

the odd predecessor of a maximum becomes

`(2M-s)/3`,

so the exact residue ladder changes with `s`.

Any successful RL82 theorem should retain this absolute increment dependence rather than collapsing to a homogeneous scaling statement.

---

## 5. Computational role

A small exact program is encouraged for:

- generating the symbolic/residue backward automaton;
- discovering forced residue classes;
- falsifying proposed induction rules;
- checking branch-exhaustiveness at bounded depth.

But bounded search is evidence/certificate only. An infinite exclusion requires an analytic induction, finite-state closure theorem, or another exact global argument.

Do not enumerate candidate cycle maxima up to a large numerical bound as the main attack.

---

## 6. Fast stop / pivot conditions

Freeze or demote a sub-route if:

- it produces only thinner congruence classes with no global consumer;
- the number of backward residue states grows without a compressible invariant;
- a proposed top-to-RL identification is only an analogy between coordinates;
- the argument becomes equivalent to solving unrestricted inverse Collatz dynamics without using maximality.

The unit-lattice/content route proposed in the first RL81 close-out is **deferred, not disproved**, and remains available if the RL♭ architecture reaches a clean barrier.

---

## 7. Desired outcome

Prefer, in order:

1. an analytic top-of-cycle theorem excluding a genuine class of hypothetical nontrivial cycles;
2. a finite-state backward-ownership theorem giving a strong necessary residue/parity grammar for every cycle maximum;
3. an exact bridge between `RL♭` top geometry and an existing RL/full-phase global invariant;
4. a rigorous no-go theorem showing why maximum-only backward ownership cannot close the branch, together with the strongest reusable extremal lemmas.

Do not claim RL or Collatz closure without a complete chain.

---

## 8. Close-out requirements for RL82

Freeze separately:

- proved analytic maximum-state mathematics;
- exact finite certificates;
- externally inherited certificates;
- computational evidence;
- conjectures;
- method barriers/dead routes;
- any new connection to the historical RL framework.

Create the next numbered authoritative bundle and sidecar and verify its internal manifest and fresh-unpack fast suite.
