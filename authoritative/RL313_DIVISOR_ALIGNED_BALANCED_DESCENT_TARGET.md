# RL313 — divisor-aligned balanced descent / fully-active flow consumer target

Date prepared: 2026-09-13
Status: PREPARED, NOT STARTED
Session type: MATHEMATICAL EXECUTION CONTINUING RL312 GLOBAL BALANCED-RETURN ROUTE

## Absolute objective

Continue toward the actual theorem:

> Prove that a positive non-trivial Collatz cycle cannot exist.

RL313 starts from the strongest exact RL312 theorem. Do not reset automatically to an older local programme.

## Authoritative incoming state

Read in order:

1. `AGENTS.md`;
2. `docs/RL_RESEARCH_PROTOCOL.md`;
3. `docs/RL_STATE_MACHINE.md`;
4. `sessions/RL312/RL312_CLOSEOUT.md`;
5. `sessions/RL312/RL312_SHIFT_ORBIT_DICHOTOMY_AND_DIVISOR_DESCENT.md`;
6. `sessions/RL312/RL312_SINGLE_SHIFT_ORBIT_EXCLUSION.md`;
7. `sessions/RL312/RL312_BALANCED_RETURN_RADIUS2_EXCLUSION_AND_NORMALIZATION_REPAIR.md`;
8. exact historical sources named there only as needed.

Treat the repository as authoritative. Preserve every RL312 correction and scope qualification.

## Primary inherited object

RL311 gives, in the active `lambda<3` one-sided sector,

`g<=h+1`

or a proper genuine full-D owned balanced return with

`A=ga`, `L=g ell`, `s=ma`, `1<=m<=h+1`,

and original endpoint ratio

`1/lambda < (4x_k+1)/(4x_j+1) < lambda < 3`.

For that balanced shift define

`p=m ell`,
`G_i=p-W_i(s)`.

RL312 proves the following exact all-scale dichotomy. Let

`c=gcd(g,m)`, `d=ac`.

Then either:

### F — fully active shift-orbit branch

Every one of the `d=ac` shift-orbits is active. Each orbit has zero total canonical flow and therefore

`sum_i |G_i| >= 2ac`.

This is a bound for the canonical zero-sum flow. It is **not automatically** a bound for the optimally normalized cyclic transport distance.

### D — divisor-aligned descent branch

Some shift-orbit is inactive. Then, after a genuine cyclic rotation, the full word decomposes into

`A/(ac)=g/c`

consecutive blocks of exact counts

`(ca,c ell)`.

In particular there is a genuine full-D-owned balanced segment with those counts. If `c<m`, this is a strict descent from balanced gap `m` to gap `c`.

The descended endpoints retain global full-D ownership but do **not** automatically inherit the original RL311 physical endpoint ratio bound.

RL312 also proves independently:

- exact owned balanced Radius 2 is impossible;
- a full-D owned balanced flow cannot be supported on only one shift-orbit.

## Primary target

Consume the RL312 divisor/full-activity dichotomy without growing another fixed-radius grammar.

### A. Iterated divisor descent

Determine whether the descent alternative can be iterated in a genuinely monotone invariant until it reaches a terminal divisor configuration.

High-value terminal cases:

1. `gcd(g,m)=1`: either full activity across all `a` shift-orbits or an owned exact `(a,ell)` segment;
2. `c=gcd(g,m)<m`: strict descent; identify exactly what full-D quotient/row information survives descent;
3. `c=m` (so `m|g`): no gap reduction. Use the resulting exact equal-weight `ma` block partition as a direct global arithmetic object rather than calling it progress by itself.

A successful theorem should show that the descent cannot cycle or stall indefinitely without entering an already impossible ownership configuration.

### B. Fully-active consumer

Exploit the stronger orbitwise identity

`sum_(i in O) G_i=0`

for every shift-orbit `O`, together with full-D ownership and the weighted rotation identity.

The goal is an independent obstruction to the fully-active branch, not merely a lower bound on canonical mass.

Potential legitimate interfaces include:

- row/cyclotomic factorization that preserves full-D ownership;
- RL19 weighted exponential moment applied orbitwise or after a proved decomposition;
- proper sparse subfactors/results that survive the RL20 coboundary red team;
- quotient-layer integrality genuinely independent of the already-known full-phase quotient equality.

### C. Controlled-multiplicity branch

The complementary RL311 branch

`g<=h+1`

remains open. It may be attacked in parallel only if the divisor/full-activity route stalls or if a new theorem couples both branches.

Do not claim a packing contradiction from `g<=h+1` alone. RL312 tested the old strict-excursion/state-packing interfaces and did not close this branch.

## Required red teams

Every candidate must pass all of these.

1. **Canonical versus optimal flow.** The canonical balanced flow is zero-sum, but optimal cyclic transport may differ by an integer constant. Do not transfer canonical L1 bounds to optimal radius without proof.
2. **No local-denominator ownership leap.** Descended endpoints are genuine full-D rotations, but no local segment denominator owns them automatically.
3. **No inherited endpoint-ratio assumption after descent.** The original RL311 `<3` physical ratio belongs to the selected pair only unless separately reproved.
4. **No RL20 coboundary repackaging.** Whole-block telescoping is not an independent contradiction.
5. **No fixed-radius escalation.** Radius 6+ remains frozen absent an encounter theorem.
6. **No finite-depth substitute for an all-scale lift.** A search depending on `h`, `a`, `g`, or divisor depth needs a proved uniform reduction.
7. **Preserve RL312 single-orbit theorem scope.** It uses full-D ownership and rules out support on exactly one shift-orbit; it does not by itself rule out two or more active orbits.
8. **Preserve RL311 corrections.** Do not resurrect the demoted strip-width lower bound globally, `E_j<=floor(kappa_ext/A)`, or proper-prefix ownership.

## Frozen routes

Do not automatically resume:

- fixed-96 P/Q commutation;
- H21;
- Radius 6+;
- Gate-A `Y=(6,504)` / high-index A/F ancestry;
- raw finite Farey enumeration;
- selector scans;
- quotient gcd/content or fixed-prime residue programmes;
- recurrence-linear/coboundary forcing;
- local pattern grammars whose depth grows with `h`.

They remain frozen resources/barriers unless RL313 derives an exact new splice.

## Checkpoint discipline

At every meaningful checkpoint state

`PARENT_DIFFICULTY_DELTA = EASIER | LATERAL | HARDER`.

`EASIER` requires a real contraction of the parent global arrow: terminal divisor closure, an impossible fully-active configuration, a monotone descent theorem, closure of `g<=h+1`, or an equivalent exhaustive all-scale reduction.

If two consecutive meaningful RL313 checkpoints are LATERAL/HARDER, freeze this route and perform the strategic step-back/audit rather than growing a deeper local programme.

## Success ladder

Full success:
- contradiction for every hypothetical positive primitive non-trivial cycle, or a universal owned witness already excluded.

Strong partial success:
- close either the divisor/stall branch or fully-active branch with an independent theorem while strictly simplifying the remainder;
- prove a terminating descent to a bounded/terminal ownership configuration;
- close the controlled-multiplicity branch independently.

Insufficient success:
- another canonical mass lower bound;
- a divisor partition with no consumer;
- fixed-depth cases growing with the divisor structure;
- a repackaged coboundary identity.

## Scope

RL312 is closed and frozen.
Gate A remains open and frozen as fallback.
Gate B remains open.
Global non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains a separate project.
Knowledge catalogues remain stale/deferred.
