# RL56 attack plan — aggregate late-x-zero mass

Date: 2026-08-23

## Primary theorem target

Under the full inherited hypotheses defining the sole safe continued-fraction survivor, prove for every remaining odd `z>=41` that

`Zx_late < Delta`,

with

`Delta = 4590516512150518575599 / 11817250826203334794572`

`= 0.3884589215938109...`.

Because the exact legal first-26 contribution is at most

`11.528207745072855...`,

this would contradict the inherited total requirement

`Zx > 143/12`.

The goal is an **aggregate theorem**. Do not try to force each individual late weight below one universal microscopic constant.

## Variables to keep explicit

Use the inherited notation but keep these dependencies visible throughout:

- `z`: total x-zero parameter in the survivor;
- `R=z-27`: number of late x-zeros after the first 26;
- `K=q-z+3`: terminal exponent parameter;
- `K+R=q-24`: exact invariant;
- `w_j`: weight of the j-th late x-zero;
- `Zx_late=sum_j w_j`;
- `r`: remaining late x-zero budget in backward terminal coordinates;
- `P=2^r J`;
- `P_end=2^(q-24)`.

Every claimed “uniform in z” bound should be checked against the `K+R` coupling rather than treating K and R as independent.

## Track A — derive an aggregate terminal inequality

Start from terminal arithmetic and attempt to bound the **sum** of late zero weights directly.

Useful subgoals:

1. Express each late weight, or a controlled envelope for it, in terms of the terminal gap sequence / backward event grammar.
2. Search for a telescoping quantity whose decrement at a late x-zero controls that zero's weight.
3. Test whether inherited `W=gJ/3^d`, the new `P=2^rJ`, or a hybrid normalized quantity gives such a telescoping inequality.
4. Retain exact divisibility/parity constraints. A bound proved only in a relaxed grammar is acceptable as an upper bound only if the relaxation direction is explicitly checked.
5. Aim first for any exact constant `<Delta`; optimizing the constant is secondary.

A particularly valuable outcome would be a potential `Phi(state)` satisfying something like

`sum of future late weights <= Phi(current)-Phi(terminal)+controlled_error`

with a terminal expression independent of R or bounded uniformly through `K+R=q-24`.

## Track B — split the K regimes intelligently

The fixed `2^-1000` strategy failed because small K forces the final weight to be non-negligible. That failure suggests a natural split rather than a dead end.

### Large K

For large terminal exponent K, terminal weights are intrinsically small. Try to prove an aggregate geometric tail estimate strong enough to fall below `Delta`, without requiring every term to be `<2^-1000`.

The useful output is a rigorous threshold `K>=K0` for which the aggregate theorem holds.

### Small/intermediate K

Here `R=q-24-K` is correspondingly huge. Do not enumerate R events.

Exploit fixed endpoint `P_end=2^(q-24)`, divisibility, height and parity. Look for one of:

- an impossible divisibility chain;
- a monotone normalized potential;
- a finite quotient/state reduction independent of R;
- a forced positive amount of defect incompatible with the inherited defect budget;
- a way to compress repeated event macros before any finite computation.

If Track A proves the aggregate bound for all but a bounded K-window, only then use exact computation on that bounded remainder.

## Track C — rebuild the cut theorem legally

The old `-1318<J_cut<1379` cut was attached to an illegal relaxed prefix. The legal-prefix automaton already knows all states compatible with 26 x-zeros under the sequential cap.

A useful secondary project is therefore:

1. Extend the exact legal-prefix DP so it records reachable/dominating `(column,d,J,g,mass)` states when the 26th x-zero occurs.
2. Determine whether column 70 is maximal, merely the maximizing-mass endpoint, or irrelevant to other legal prefixes.
3. Search for rigorous bounds on `J`, `d`, `g`, or a normalized `P/W` at that legal cut.
4. If the state set can be reduced to a finite interval or finite residue classes, derive a true legal cut-state theorem.

This route becomes high leverage only if the terminal suffix can then be classified uniformly or with a bounded finite computation.

## Track D — z=41 terminal layers only as fallback

The inherited z=41 recurrence points next to `L_terminal(9,17)`, then `L(10,17)`, `L(11,17)`, and cleanup caps near `(12..14,18)`.

Do not default to this chain. Use it when:

- a terminal computation diagnoses which macro blocks defeat a proposed uniform bound;
- a uniform proof reduces to finitely many low-z exceptions;
- or the aggregate/P routes genuinely stall.

Closing z=41 alone is useful but substantially lower leverage than a uniform aggregate theorem.

## Track E — global Gate A / Gate B pivot criterion

After a serious attempt, explicitly ask whether every successful inequality still depends essentially on the single safe-CF denominator/survivor.

If yes, stop extending z thresholds and return to the global problem:

- Gate A `H>=t+3`, or
- a valid root-specific Gate B connecting full-phase RL data to the exact radius-3 theorem.

The radius-3 branch is already inherited/certified; the missing value is the bridge, not another re-proof of radius 3.

## Ranked roadmap

1. **Aggregate late-mass theorem** — highest immediate leverage; exact contradiction threshold already certified.
2. **P-based terminal potential/divisibility theorem** — best structural mechanism for making the aggregate bound uniform in R.
3. **Legal cut-state theorem** — promising finite compression if rebuilt from legal prefixes.
4. **z=41 exact terminal continuation** — fallback and diagnostic only.
5. **Global Gate-A/Gate-B pivot** — move here if the first three are inherently survivor-local/nonuniform.

## Success levels for RL56

### Strong success

Prove `Zx_late<Delta` uniformly for all remaining odd `z>=41` in the safe-CF survivor and thereby eliminate that survivor.

### Significant partial success

Prove the aggregate theorem for a full K-regime and reduce the complement to a bounded, explicitly stated structural/finite problem.

### Useful structural success

Prove a genuine monotone/telescoping P-potential or a legal finite cut-state theorem with exact quantifiers, even if the final contradiction remains open.

### Avoid false progress

Do not count as major progress:

- raising `z>=41` to `z>=43` by itself;
- another relaxed-greedy endpoint calculation;
- a large finite search with no theorem explaining why its range is exhaustive;
- assuming a pointwise tiny-weight statement contradicted by small K;
- presenting survivor-local elimination as global Gate A.
