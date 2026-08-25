# RL86 target — RL↑: finite genuine roof plus infinite external dyadic feeder ray

Date: 2026-08-25

## Authority and operating rule

Continue from the frozen RL85 state. Preserve all RL85 theorem labels, failures, barriers, corrections, verifier results, and the live fallback obligation. Do not replace RL85 with the RL↑ idea.

Apply the verification-economy rule: after this bundle's sidecar, internal manifest, and fast verifier pass, accept the frozen incoming ledger. Do not recursively rerun historical expensive certificates unless a dependency fails, a verifier fails, or an apparent contradiction triggers stop-and-repair.

No Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure may be claimed unless actually proved.

## 0. Terminology to freeze before new work

Use the ordinary shortcut map

- `T(n)=n/2` for even `n`;
- `T(n)=(3n+1)/2` for odd `n`.

Project terminology:

- **B**: blue, a state proved/known to lie in the basin of 1;
- **blue basin**: the full set of B states;
- **R**: red / hypothetical counterexample-associated state;
- **L**: nontrivial loop;
- **RL**: hypothetical nontrivial red loop;
- **cycle minimum**: genuine least repeated state of a chosen loop, denoted `R=min C` in RL82–RL85;
- **cycle interior**: repeated state strictly between the extrema;
- **RL♭**: genuine maximum/roof `M=max C`;
- **RL↑**: provisionally the external dyadic roof-feeder ray, not a greatest element;
- **F_k=2^k M`, `k>=1`; `F_1=2M` is the first upper feeder;
- **RO**: hypothetical genuinely nonperiodic/unbounded-orbit counterexample;
- historical **R#**: retain its original hypothesis exactly. RL85 verified that early R# meant the least positive red integer across the full red set, not automatically the chosen cycle minimum.

For the roof predecessor use

`P=(2M-1)/3`,

so

`F_1=3P+1=2M`.

This fraction is the authoritative formula; any typography resembling `32M-1` is only a formatting ambiguity.

## 1. Define the new object rigorously

Freeze exact distinctions among:

1. historical `R#`;
2. genuine cycle minimum `R`;
3. interior repeated states;
4. `RL♭=M`;
5. first upper feeder `F_1=2M`;
6. full ray `RL↑={F_k=2^kM:k>=1}`;
7. genuine `RO` objects.

For each state/class record whether it is:

- on-cycle;
- preperiodic;
- repeating;
- external to the loop;
- bounded as an individual trajectory;
- unbounded only as a set of starting values.

Do not conflate an unbounded set of initial values with an unbounded orbit.

## 2. Interrogate the apparent infinity against RL80

For every `k>=1`,

`T^k(F_k)=M`.

Red-team aggressively against RL80's dyadic/backward-saturation neutrality theorem.

Ask:

- Is the infinity of `RL↑` entirely tautological dyadic duplication?
- Does anchoring the base at the **true maximum** add ownership that generic dyadic saturation does not see?
- Does maximality of `M` impose a boundary condition at the base of the ray that survives normalization?
- Is there any invariant along `F_k` that is not dyadically neutral?
- Can the ordinary `+1` structure at `P` interact with the ray in a way RL80 did not consume?

If the answer is negative, freeze a theorem/barrier instead of forcing a route.

## 3. Exploit the canonical fork at the roof

Inherited exact roof structure:

`P=(2M-1)/3 -> M` from inside the cycle,

`F_1=2M -> M` from outside the cycle,

`F_1=3P+1`.

Investigate the internal/external sibling relation through:

- congruences;
- 2-adic valuations;
- inverse ownership;
- full backward cylinders/addresses;
- physical ordering;
- primitive-cycle restrictions;
- full-`D` ownership;
- historical entry/feeder lemmas that use ordinary `3x+1` non-homogeneously.

Mandatory inherited RL85 warning:

- `F_1` and `M` are even;
- `P==2 mod3` under the RL82 roof grammar;
- none of `F_1,M,P` is historical `R#`;
- `nu_2(3P+1)=1+nu_2(M)>=2`, so the old pure-`r=1` corridor does not attach directly.

The RL86 task is to determine whether the **off-cycle status itself** makes some historical feeder lemma useful even though historical minimality does not transfer.

## 4. Compare the two infinities: RL↑ versus RO

Make the distinction mathematically explicit.

### RL↑

- the set of starting values `2^kM` is unbounded in `k`;
- each individual orbit descends through finitely many halvings and then enters the same finite loop;
- unboundedness is transverse to time along any one trajectory.

### RO

- one trajectory remains nonperiodic/nonconvergent and becomes unbounded;
- unboundedness is longitudinal in trajectory time.

Ask whether this transverse-versus-longitudinal distinction supports a real invariant, compactness principle, scaling contradiction, ownership theorem, or boundary principle.

Do not claim an RL/RO bridge unless one is actually proved.

## 5. Search for a finite-roof / infinite-ray contradiction

Test whether a finite primitive loop with rigid maximum `M` can coexist with the automatically attached infinite tower `2^kM` in any nontrivial sense.

Directions worth testing:

- normalization by `M`;
- scale invariance versus the inhomogeneous `+1`;
- residue/address stabilization along `F_k`;
- interaction with the cycle minimum `R`;
- entry-time versus size tradeoffs;
- density/packing of feeder cylinders;
- primitive/full-`D` ownership;
- collisions between different inverse representations;
- finite-state residue descriptions combined with arbitrarily large dyadic scale.

Every proposed contradiction must survive the obvious objection that

`2^kM -> 2^(k-1)M -> ... -> M`

contains no new non-dyadic dynamics before the roof is reached.

## 6. Connect directly back to RL85

RL86 is not a notation-only session.

Use the completed RL85 results:

### Historical mismatch

The immediate roof fork does not satisfy historical least-red hypotheses. Test whether a lemma that failed because its object was not on-cycle becomes useful when applied deliberately to a canonical **off-cycle** feeder instead.

Conversely, mark every lemma that still requires true cyclic ownership and therefore remains restricted to `R`, `M`, or another repeated state.

### First-Farey physical scale

On the exact first-Farey branch RL85 proved

`M<3^27,021,536,997`

and `M` is the least positive even maximum-cylinder representative, with at least `45,035,894,994` leading zero ternary digits in the zero-padded `q`-digit representation.

Ask whether the feeder ray turns this finite-base information into anything new. In particular, pure doubling preserves normalized cylinder height, so any useful theorem must see the base `M`, the fork `F_1=3P+1`, or true ownership.

### RL75/RL76 splice fallback

RL85 proved that, in the first-Farey/full-phase intersection, every proper synchronized quotient return has span

`<=43,234,459,194`.

The giant RL73 macro then has at least `930,959` spaced-distinct quotient states on the intersection branch.

If RL↑ proves neutral, return to this exact obligation rather than restarting generic residue or CF work.

## 7. Revisit the blue-funnel analogy only structurally

Compare:

- blue `x` implies `2^kx` is blue;
- red-loop roof `M` implies `2^kM` feeds the same red loop.

Do **not** repeat RL80's generic dyadic-saturation work.

The only live question is whether anchoring the red ray at the **true maximum plus forced odd predecessor** creates a separation, boundary, residue, density, or ownership condition absent in the generic blue/red dyadic statement.

## 8. Seek an invariant that sees the base

Purely dyadic quantities are unlikely to help. Prefer invariants consuming one or more of:

- exact residue class of `M`;
- `P=(2M-1)/3` and `F_1=3P+1`;
- opposite extremal structure at cycle minimum `R`;
- full backward word cylinders;
- RL84/RL85 first-Farey cylinder-height/physical-size bounds;
- cycle length / odd-count bounds;
- primitive/full-`D` restrictions;
- exact physical size relations.

Preferred theorem shape:

> an infinite roof-feeder ray can exist only if its finite base `M` satisfies property X,

where X is genuinely stronger than the already-frozen maximum conditions.

## 9. Mandatory red teams

Any proposed RL↑ theorem must be checked against:

1. RL80 dyadic saturation neutrality;
2. RL81 auxiliary-to-physical lift failure;
3. RL20 address/continued-fraction decoupling;
4. RL83 count-only first-surplus insufficiency;
5. RL84/RL85 cylinder-height without an independent lower consumer;
6. generic infinitely-many-preimages facts;
7. RL79 generalized-increment/homogeneity barrier where relevant.

If the ray is only a restatement of one of these, freeze that negative result explicitly.

## Desired outcomes, in priority order

1. a new analytic constraint on `M=RL♭` caused by existence of `RL↑`;
2. an exact bridge from `RL↑` to a surviving historical R# / entry-side theorem;
3. a useful base-sensitive invariant distinguishing roof feeders from generic dyadic saturation;
4. a theorem explaining exactly why the ray is mathematically neutral;
5. a clean route barrier ruling out RL↑ as a closure architecture.

A rigorous negative result is fully acceptable.

## Close-out requirements for RL86

At the end of RL86:

- freeze the exact theorem/evidence/barrier ledger;
- preserve all still-live RL85 obligations;
- create the next numbered authoritative bundle and `.sha256` sidecar;
- perform fresh-unpack/internal-manifest/fast-verifier checks;
- do not claim Gate A, Gate B, RL/nontrivial-cycle, or Collatz closure unless actually proved.
