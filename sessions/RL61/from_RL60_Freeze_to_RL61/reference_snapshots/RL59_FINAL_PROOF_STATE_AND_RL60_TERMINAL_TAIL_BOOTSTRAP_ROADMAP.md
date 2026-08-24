# RL59 final proof state and RL60 terminal-tail bootstrap roadmap

Date: 2026-08-23

## Executive status

RL59 does **not** prove Gate A, Gate B, RL, or Collatz.

The sole safe-CF survivor is still open.

However, RL59 has removed the RL58 synchronized-pump obstruction and reduced the live branch to a deterministic final height-one shortcut-Collatz tail with extremely strong terminal mass and size requirements.

The strongest current survivor reduction is

`z >= 9,457,747`.

The intended RL60 task is to exploit the exact coupling between `K` and `z` and the terminal shortcut ancestor thresholds, not to restart generic prefix squeezing.

## A. Inherited audited baseline

Retain unless a verifier fails:

- `Zx>143/12` strictly;
- `E<5/3` strictly;
- each x-zero weight `w<17/30`;
- exact defect identity;
- sole safe-CF survivor, odd `z>=41` before RL59 strengthening;
- terminal `J_end=2^K`, `Q_end=2^K+1`;
- terminal `K` odd and `K>=25`;
- `M0_26<=17/3` exact finite certificate;
- `Zx_26<=77/10` exact finite certificate;
- therefore `M0_late>5/4` and `Zx_late>253/60`;
- inherited phase squeeze for `zeta`;
- radius-3 closure/certification status inherited from earlier handovers;
- Gate A remains open;
- no global Gate-B/RL-to-radius-3 bridge is proved.

The complete RL58->RL59 handover is bundled under `inherited_rl58_to_rl59/`.

## B. RL59 promoted analytic results

### B1. Positive terminal potential

For every positive post-cut state that can embed in the safe-CF terminal endpoint,

`J*g <= zeta*3^(4-d)/2`.

At `d=1`, `Jg<=27zeta/2`; at `d=2`, `Jg<=9zeta/2`.

This is the key new analytic interface.

### B2. RL58 pump neutralized

All maximal `J=3<->5` synchronized pump blocks are harmless terminally.

- Type-A exit gives total pump mass `<17/30`.
- Type-B exit plus terminal potential gives total pump mass `<17/25`.

Thus the repeatable RL58 pump cannot meet `M0_late>5/4` in a genuine survivor.

### B3. Local entry remains genuinely viable

There is an exact defect-compatible prefix to `(73,47,1,3)` with matched defect `~0.847046<5/3`, and four local pumps supply `~1.53488>5/4` before the terminal obstruction kills them.

This demonstrates that the new obstruction is truly terminal, not a disguised prefix-cap argument.

### B4. Final synchronized-tail forcing

After the last `10` return, the remaining positive height-one tail is synchronized and deterministic.

The strengthened bound is

`M_final > 23/4`.

The earlier independent rational regression gives the weaker but useful event consequences

- `M_final>45/8`;
- synchronized `11` mass `>17/3`;
- at least 10 final `00` events;
- at least 16 final `11` events;
- at least five maximal final `00` runs.

## C. RL59 exact finite terminal-ancestor result

Under the final-tail shortcut map

`n even -> n/2`,

`n odd -> (3n+1)/2`,

with `n=(J-1)/2`, the first positive starting state whose trajectory encounters any admissible odd `K>=25` terminal predecessor is exactly

`n=11,184,810`.

No smaller start hits one.

Consequently

`J>=22,369,621`

throughout a genuine final terminal tail, so each final aligned zero is `<68/111,848,105`.

With `M_final>23/4`, this forces

`#00_final >= 9,457,745`

and hence

`z >= 9,457,747`.

Classification: exact finite computation plus analytic consequence. The C++ result is reproduced and internally consistent; an independent implementation audit is still desirable before treating the boundary as publication-grade.

## D. Reproduced higher-K finite boundaries

For threshold `K>=27`:

`n_min=13,256,071`, `J_min=26,512,143`, forced `#00>=11,209,179`.

For threshold `K>=29`:

`n_min=125,687,199`, `J_min=251,374,399`, forced `#00>=106,279,618`.

These are exact computational discoveries/reproductions, not yet independent two-code certificates.

Important correction: `11,209,179` is the correct `K>=27` count; an earlier prose value `11,209,546` was an arithmetic slip.

## E. What is not proved

Do **not** infer any of the following:

- that the safe-CF survivor is eliminated;
- that large `z` alone is contradictory;
- that the shortcut-Collatz terminal subsystem has a global lower-envelope theorem for arbitrary `K`;
- that the finite `K>=27` or `K>=29` searches generalize monotonically in a simple closed form;
- that Gate A, Gate B, RL, or Collatz is solved.

The final tail is a real Collatz-conjugate subsystem. Any claim that effectively assumes all shortcut trajectories behave globally is circular unless reduced to a finite exact range or proved independently.

## F. RL60 attack sequence

### Gate 1 — verify / independently audit

Run `verification/run_all_rl59_to_rl60_verifiers.sh`.

Then independently inspect:

- the general normalized-`P` derivation;
- the shortcut terminal-hit predicate;
- the dynamic `done` caching logic in the finite ancestor search;
- exact conversion from an `n_min` threshold to the `z` lower bound.

If the K25 boundary fails independent audit, stop and repair before extension.

### Gate 2 — formalize the bootstrap operator

For odd threshold `K0`, define

`N(K0) = min positive n whose shortcut orbit encounters an admissible terminal predecessor with odd K>=K0`.

When `N(K0)` is certified, define

`Jmin(K0)=2N(K0)+1`

and

`Amin(K0)=floor(115*Jmin(K0)/272)+1`.

Then terminal mass gives

`z >= next_odd(Amin(K0)+1)`

under the hypothesis `K>=K0`.

Combine this with

`K+z=q+3`.

The goal is to find a finite dichotomy or self-improving interval map on `K` / `z`.

### Gate 3 — avoid naive huge scans

Do not simply scan larger and larger `n` for `K>=31,33,...` without a structural plan.

Instead investigate exact reverse preimage trees of the terminal alternatives

`2^K-1`, `(2^K-2)/3`,

under the shortcut map, and seek a certified lower envelope for starting values as a function of `K` over an interval of odd exponents.

Useful possibilities:

- reverse-tree branch-and-bound with exact lower bounds;
- modular pruning by powers of 2 and 3;
- certificates that cover exponent intervals rather than one `K0` at a time;
- use `K+z=q+3` to rule out large chunks of exponent space before searching them.

### Gate 4 — split exponent regimes

A productive proof structure may be:

1. if `K` is below some large threshold, `z=q+3-K` is already extremely large;
2. if `K` is above that threshold, a certified `N(K0)` lower envelope forces `z` large by tiny terminal weights;
3. combine either lower bound with any inherited upper restriction on `z`, zero count, length, denominator exponent, or defect budget.

The next session should explicitly search the inherited ledger for a usable **upper** bound or affine restriction involving `z`; without one, the bootstrap only grows lower bounds.

### Gate 5 — check for a potential global-count contradiction

Revisit inherited exact identities involving total word length, x/y zero counts, `ell`, `q`, denominator exponents, and defect. Determine whether `z>=9,457,747` already violates any previously dormant inequality.

This is higher priority than pushing `K0=31` blindly.

### Gate 6 — only then extend the finite ancestor frontier

If no inherited upper restriction closes the branch, extend the exact terminal ancestor analysis, preferably with an independent second implementation.

## G. Success classifications for RL60

**Strong:** combine the terminal-tail bootstrap with an inherited upper restriction to eliminate the safe-CF survivor.

**Significant:** prove a rigorous interval lower envelope `N(K0)` / reverse-tree theorem that turns `K+z=q+3` into a finite remainder.

**Useful:** independently certify the K25/K27/K29 ancestor boundaries and derive a robust bootstrap iteration with explicitly bounded unresolved exponent intervals.

**Pivot:** demonstrate that the remaining terminal tail embeds an unrestricted global shortcut-Collatz problem with no usable inherited upper restriction, making further local mass squeezing strategically unproductive.

**Repair:** invalidate any normalized-P, final-tail, or finite ancestor claim; repair before extending.
