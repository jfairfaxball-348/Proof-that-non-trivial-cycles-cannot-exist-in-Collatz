# RL277 closeout

Date: 2026-09-07

Classification:

`ONE_SIDED_COMMON_MODE_CONSUMER_PROVED`

Subordinate:

- `ABSOLUTE_ORDERED_RANK_MOMENT_BUDGET_PROVED`
- `GLOBAL_DANGEROUS_ZERO_BUDGET_Z_GE_K_PLUS_4`

## Promoted frontier

RL277 converts the inherited terminal rank identity into an absolute ordered-rank moment budget

`413/16 < sum_j 2^(a_j-(j-1)log_2 3) < 61`.

It then rewrites the same exact identity in zero-rank coordinates. If `m0=z-k+2` is the number of internal zeros, the global identity implies a weighted zero-rank sum greater than `17/2`.

This immediately gives `m0>=4`. The `m0=4` case reduces to ten exact canonical prefixes; only one terminal is phase-box compatible and it has `(k,H)=(3,6)`, hence is Gate-A safe.

The `m0=5` case reduces analytically to `u_5<=11`, then to 206 monotone zero-rank tuples, 72 legal canonical prefixes, 36 terminal closures, and 19 phase-box terminals. None has `H<k`.

Therefore every hypothetical Gate-A-violating full-phase object satisfies

`z>=k+4`.

## Scope

This is global Gate-A/full-phase scope and does not import Branch-C-only counterflow conclusions.

Gate A is not closed. Gate B is unchanged/open. Fifth selector not scanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

Exploratory six-zero replay found no counterexample but is not promoted.

## Verification

Portable verifier passes:

- zero-rank formula checks: 2,046
- four-zero relaxed patterns: 10
- five-zero admissible tuples: 206
- five-zero legal canonical prefixes: 72
- five-zero terminals: 36
- five-zero phase-box terminals: 19
- five-zero Gate-A violators: 0
- inherited bounded terminal paths replayed: 1,421
- inherited bounded phase-box paths: 250
- bounded phase-box Gate-A violators: 0

Successor RL278 should extend the exact zero-rank/canonical finite-reduction programme to six zeros and seek a scalable induction.
