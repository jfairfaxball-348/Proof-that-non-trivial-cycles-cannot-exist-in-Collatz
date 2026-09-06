# RL262 — fourth-selector arithmetic frontier and exact full-phase elimination

Date: 2026-09-06
Classification: **EXACT FINITE CERTIFICATE**
Scope: the inherited selector predicate beyond `a=1287`, and the single next selector `(1417,894,523,317,200,18,4)`.

## Arithmetic frontier

Using exactly the selector predicate frozen in the promoted RL260 verifier, there is no retained selector for

`1288 <= a < 1417`.

The unique first retained selector is

`(a,ell,z,q,r,H_sel,n)=(1417,894,523,317,200,18,4)`.

The exact identities are

- `1417*200 - 317*894 = 2`;
- `19*523 - 7*1417 = 18`;
- with `B=317-200=117`, `19*117 - 7*317 = 4`.

This is an even-halving selector with `K=9`, `t=2`:

- `9*317 = 2*1417 + 19`;
- `9*117 = 2*523 + 7`.

The nine exact length-33 physical blocks are

`[129,161] [278,310] [446,478] [595,627] [763,795] [912,944] [1080,1112] [1229,1261] [1378,1410]`.

Their cyclic complementary gap lengths are

`[116,135,116,135,116,135,116,116,135]`,

total complement size `1120`, with exact isolated-root capacity `375`.

These geometry data are verified but are not needed for the stronger full-phase elimination below.

## Stronger exact full-phase elimination

Use the promoted RL65 ordered rank-defect/full-phase quotient theorem.
For this selector

- `rho=ell-3=891`;
- `M=2^1417-3^894`;
- internal length `m=1417-k-1`;
- a full internal word must have common x/y weight `rho`.

Therefore full-phase feasibility itself forces `m>=rho`, hence

`k <= 1417-891-1 = 525`.

Inherited terminal ownership gives odd `k>=31`, so the complete possible terminal range is exactly

`k=31,33,...,525` (248 values).

The canonical nine-bit right-prefix family from `(d,J)=(1,-13)` contains exactly 199 legal words. Its minimum weighted-zero cost remains 11, attained only by `110110111` and `110111010`.

For every feasible `k`, nonnegative rank defect gives the same exact quotient bound `N_phase<=288`. The full-phase theorem gives `N_phase == 3 (mod 8)`, while exact integrality with odd `k` forces `N_phase == 1 (mod 3)`, hence

`N_phase == 19 (mod 24)`.

After the canonical nine-bit ordered-rank congruence, every one of the 248 terminal exponents has exactly 9 surviving `(prefix,N_phase)` classes. Thus the complete exact extension problem contains

`248 * 9 = 2232`

classes.

The verifier follows the actual canonical `step_x` transition, updates the ordered x/y ranks and exposed rank-defect partial sum, enforces the exact quotient-implied rank defect at every dyadic prefix, and prunes when either internal word can no longer finish with weight 891.

All 2,232 classes die. The maximum death depth is 988, attained by

`k=31`, prefix `101000111`, `N_phase=43`.

Hence there is no genuine full-phase object at the selector `(1417,894,523,317,200,18,4)`.

## Consequence and limits

The fourth retained selector in the current arithmetic-frontier process is completely removed from the branch simultaneously unresolved by Gate A and Gate B.

This does **not** prove uniform Gate A, Gate B, global non-trivial-cycle exclusion, or the Collatz conjecture. Radius 4 is not invoked and Radius 5 remains inactive.
