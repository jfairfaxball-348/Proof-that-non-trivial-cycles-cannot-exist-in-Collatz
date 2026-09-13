# RL311 — canonical extremal one-sided transport closure target

Date prepared: 2026-09-13
Status: PREPARED, NOT STARTED
Session type: MATHEMATICAL EXECUTION CONTINUING THE RL310 GLOBAL ROUTE

## Absolute objective

Continue toward the actual theorem:

> Prove that a positive non-trivial Collatz cycle cannot exist.

RL311 starts from the new RL310 global extremal architecture. Do not reset to an older local programme merely because it is mature.

## Authoritative incoming state

Read in order:

1. `AGENTS.md`;
2. `docs/RL_RESEARCH_PROTOCOL.md`;
3. `docs/RL_STATE_MACHINE.md`;
4. `sessions/RL310/RL310_CLOSEOUT.md`;
5. `sessions/RL310/verify_rl310_extremal_and_farey.py`;
6. exact historical sources named by RL310 only as needed.

Treat the repository as authoritative. Do not rely on chat memory when it conflicts with the files above.

## New universal RL310 structure

For every hypothetical primitive positive cycle, let

- `R=min C`;
- `M=max C`;
- `A` be full shortcut length;
- `L` be full odd count;
- `lambda=2^A/3^L`;
- the physical forward arc `R -> ... -> M` have length `d` and odd count `o`;
- the complementary arc `M -> ... -> R` have length `A-d` and odd count `L-o`.

RL310 proves analytically:

`lambda < M/R`.

Together with RL84's complementary-arc inequality, this forces

`2^d < 3^o`,

hence the canonical slope bracket

`d/o < log_2 3 < A/L < (A-d)/(L-o)`.

Define

`kappa_ext = A o-dL > 0`.

This is the canonical extremal cross-determinant.

RL310 also proves the exact weighted extremal identity

`[sum_i q_i 3^(-G_i)]/[sum_i q_i] = (4M+1)/(4R+1)`

for the self-rotation by `d`, where

`G_i = W_i(d)-o`.

Therefore the canonical extremal self-rotation has transport/discrepancy height at least

`h = ceil(log_3((4M+1)/(4R+1)))`.

In the sufficient near-resonant branch

`lambda<3`,

RL310 proves the much stronger one-sided statement

`W_i(d)<=o` for every cyclic start `i`.

Thus

`P_i := o-W_i(d) >= 0`,

`P_0=0`,

`P_{i+1}-P_i in {-1,0,1}`,

and

`sum_i P_i = A o-dL = kappa_ext`.

The same weighted identity forces `max P_i>=h`, hence

`kappa_ext >= h^2`.

This is the live frontier.

## Primary target

Convert the canonical extremal structure into closure by proving at least one of the following.

### A. Exhaustive one-sidedness

The proof of one-sidedness actually uses only the segment condition

`S_RM < ln 3`,

where `S_RM` is the ordinary `+1` logarithmic mass on the actual `R->M` arc.

Prove this universally, or derive a contradiction from the complementary branch

`S_RM >= ln 3`.

Do not treat `lambda<3` as logically necessary if the sharper segment condition can be reached directly.

### B. Extremal determinant upper budget

Find a genuinely independent global/physical/full-D resource that forces an upper bound on

`kappa_ext = Ao-dL`

incompatible with the RL310 lower bound

`kappa_ext >= ceil(log_3((4M+1)/(4R+1)))^2`

or with a stronger bound derivable from the one-sided profile.

The upper resource must be independent; a restatement of the same window identity or a recurrence coboundary does not count.

### C. Owned compression

Use the nonnegative profile

`P_i>=0`, `P_0=0`, `sum P=kappa_ext`

plus genuine full-D ownership and primitivity to force another primitive/full-D self-rotation in a bounded transport class already eliminated by Radius 3, Radius 4, or Radius 5.

Any such compression must be proved, not assumed from largeness or pigeonhole intuition.

### D. Owned replication

Prove that the extremal one-sided profile forces repeated independently owned zero-rich/phase-rich structures whose cumulative cost exceeds an established global budget.

The replication count must grow with scale.

## Required attack order

1. Re-derive the exact entrance to `P_i>=0` from the physical segment comparison and isolate the weakest sufficient hypothesis (`S_RM<ln3`).
2. Attack the complementary branch before doing any long finite enumeration.
3. If one-sidedness becomes universal, treat `P` as the primary global owned object and look for an independent upper resource or compression theorem.
4. Test RL274 determinant/discrepancy machinery only with exact quantifier matching. `kappa_ext` is not automatically the historical determinant-2 selector.
5. Use full-D ownership only where genuine divisibility survives. Preserve RL310's explicit rejection of proper-prefix ownership from `D_g|D_G`.
6. Prefer a theorem uniform in `A,L,R,M,d,o` over another Farey cutoff.
7. If a candidate merely shows counterflow grows, ask immediately what independent budget it exceeds. Large discrepancy alone is not closure.
8. If this route hits two consecutive meaningful `LATERAL/HARDER` checkpoints, freeze it and fall back to the parent-nearest Gate A/B obligation rather than drifting into Radius 6+ or fixed-depth grammar.

## High-value possible splices

The following are legitimate to test, with hypotheses audited exactly:

- RL19 weighted population/state packing;
- RL274 determinant-discrepancy identities;
- full-D cyclic numerator ownership and quotient-layer physicality;
- canonical minimum/maximum ownership;
- established Radius-3/4/5 obstruction theorems as consumers of a proved bounded-radius extraction;
- Gate A/B only if the extremal determinant/profile supplies the missing scale-growing ownership input.

## Frozen negative controls

Do not rediscover or silently reactivate:

- RL206 recurrence-linear/coboundary compatibility as an independent obstruction;
- quotient gcd/content as a scale-growing theorem;
- direct prime/order/cylinder-residue sparse-prefix variants killed by RL104;
- variable p-adic prime-power families without a new global mechanism;
- finite Farey cascade as though it covers the infinite tail;
- proper-prefix ownership inferred from factor divisibility;
- fixed local pattern escalation without scale-growing ownership;
- Radius 6+ without an encounter/extractor theorem;
- the claim that a large extremal radius is itself contradictory.

## Checkpoint discipline

At every meaningful checkpoint state:

1. exact theorem/lemma proved or exact barrier found;
2. proof-state classification;
3. parent global arrow affected;
4. `PARENT_DIFFICULTY_DELTA = EASIER | LATERAL | HARDER`;
5. precise reason for the classification.

`EASIER` requires a real global improvement: exhaustive branch closure, an independent upper budget, bounded owned extraction, removal of an unbounded parameter, or another parent-near theorem of comparable force.

## Success ladder

### Full success

A direct contradiction for every hypothetical positive primitive non-trivial cycle, or a universal bounded owned witness whose exclusion is already established.

### Strong partial success

Make one-sided extremal transport exhaustive, or prove an independent upper/compression theorem for `kappa_ext` that strictly narrows the master obstruction.

### Insufficient success

Another numerical Farey cutoff, fixed-depth grammar, selected determinant case, or larger counterflow lower bound with no consumer.

Preserve such results but do not let them seize automatic priority.

## Scope

Gate A remains open.
Gate B remains open.
Global non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains a separate project.
