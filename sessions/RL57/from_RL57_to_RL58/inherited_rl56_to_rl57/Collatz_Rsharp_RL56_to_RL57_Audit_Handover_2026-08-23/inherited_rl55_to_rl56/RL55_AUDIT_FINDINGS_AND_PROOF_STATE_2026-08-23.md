# RL55 audit findings and proof-state reset

Date: 2026-08-23

## Executive verdict

The RL53/RL54 progress survives skeptical review, but several statements require sharper quantifiers and terminology.

The most important positive result is that the exact legal first-26 optimization is independently reproducible and yields a robust aggregate target. The most important correction is that the previously named “greedy first-26 schedule” is not a legal full Markov trajectory.

RL, Gate A, Gate B and Collatz remain open.

## Proof ledger

| Item | RL55 audit verdict | Classification |
|---|---|---|
| Outer RL54->RL55 ZIP and internal manifests | passed | verified integrity |
| RL54 lightweight audit suite | all PASS | reproducible exact checks |
| z=37 elimination | survives terminology repair | certified inside inherited safe-CF survivor |
| z=39 elimination | survives terminology repair | certified inside inherited safe-CF survivor |
| `z>=41` | valid only for sole safe-CF survivor | survivor-local theorem, not global denominator theorem |
| z=41 self-seeding recurrence | formulas/budgets check | analytic/exact-rational reduction |
| uniform `(R,R+4)` reduction | conditional reduction checks | analytic reduction, not terminal theorem |
| legal 26-zero maximum | independently reproduced | strong exact exhaustive finite certificate |
| late-mass gap `Delta` | exact | exact rational consequence |
| relaxed greedy prefix death at column 20 | verified | exact local contradiction |
| fixed `2^-1000` all-R target | impossible for small terminal exponent K | correction confirmed |
| `P=2^r J` maps and fixed endpoint | algebraically valid | structural identity; theorem still missing |
| `L_terminal(8,17)=70` | bundled deterministic source/run coherent; fresh audit did not complete a full independent end-to-end recomputation | exact certificate with residual independent-rerun task |
| `-1318<J_cut<1379` | algebra correct under relaxed-greedy cut assumptions | conditional regression fact; demoted for live-prefix use |
| exact radius-3 branch | inherited | certified inherited branch |
| Gate A `H>=t+3` | open globally | open |
| valid RL -> radius-3 Gate B | open | open |

## Legal-prefix certificate

A separate RL55 implementation of the exact branch-and-bound reproduces

`Zx_26^legal,max = 34057930625026471931596 / 2954312706550833698643`

with decimal value

`11.528207745072855...`.

The maximizing legal x-zero positions are

`[2, 5, 7, 10, 14, 15, 18, 21, 25, 26, 29, 32, 34, 37, 40, 44, 45, 48, 51, 53, 56, 59, 62, 64, 67, 70]`.

The inherited required mass is

`143/12 = 11.916666666666666...`.

Hence the exact gap is

`Delta = 143/12 - Zx_26^legal,max`

`= 4590516512150518575599 / 11817250826203334794572`

`= 0.3884589215938109...`.

The independent verifier is `rl55_audit/verify_rl55_legal26_independent.py`; its stored run is `rl55_audit/RL55_LEGAL26_INDEPENDENT_RUN.txt`.

### Why the pruning is safe

At a fixed future state `(column i, power-count p, remaining zero count, d, J)`, a path with larger accumulated mass dominates a path with smaller accumulated mass because all future legal transitions and future weights are identical functions of that state.

The upper bound

`future mass <= min(rem * 17/30, (2^rem - 1) * g)`

is a relaxation: each future zero individually obeys the sequential cap, and even if no intervening x=1 columns occur the largest possible geometric sequence of zero weights is `g,2g,...,2^(rem-1)g`.

Therefore pruning cannot remove a maximizing legal path.

## Greedy terminology repair

The schedule previously called the “greedy first-26 x-zero schedule” is the unique extremizer of a **relaxed x-only sequential-cap** problem. It is not a legal full x/y/J Markov prefix.

Replaying that prescribed x-word from the inherited initial Markov state reaches `(d,J)=(1,-6)` after column 19. At column 20 the prescribed `x=1` has no legal y choice: parity forces `y=0`, which would leave the allowed half-plane at height zero, while `y=1` is nonintegral.

Thus the relaxed schedule dies locally at column 20.

### Effect on z=37 and z=39

This does not invalidate the z=37/z=39 eliminations. Their terminal/defect cascades first force the late weights tiny using relaxed x-only mass upper bounds. Those upper bounds remain valid relaxations. The remaining mass requirement then forces the relaxed greedy x-schedule. Since that x-schedule cannot be extended to a legal full Markov prefix, contradiction is obtained already at column 20.

Accordingly the later terminal contradictions `(10,14)` and `(12,16)` may be retained as redundant checks, but are no longer needed for the cleanest logical presentation.

## Fixed tiny-weight target correction

With

`K=q-z+3`, `R=z-27`,

one has

`K+R=q-24`.

At terminal,

`g_end = 27*zeta / 2^(K+1)` with `zeta>1`.

For the final x-zero, if `c>=0` x-one columns follow it,

`w_last = (g_end/2)*(3/2)^c >= g_end/2 > 27/2^(K+2)`.

Therefore odd `K<=1001` already makes `w_last > 2^-1000`. A fixed all-R theorem saying every late weight is below `2^-1000` is impossible.

The useful replacement is an **aggregate** bound on the sum of late x-zero weights.

## Normalized terminal coordinate

Let `r` be remaining late x-zero budget and define

`P = 2^r J`.

The inherited backward grammar transforms exactly as follows:

- `11`: `P -> (2P - 2^r(2^d-1))/3`
- `10`: `P -> 2P`
- `00`: `P -> P - 2^(r-1)(3^d-2^d)`
- `01`: `P -> P/3 - 2^(r-1)(3^d-2^(d-1)-1)/3`

with the inherited integrality, divisibility and height restrictions still required.

Because `K+R=q-24`, terminal satisfies

`P_end = 2^(q-24)`,

independent of `R`.

This is strategically promising because it removes the direct R-dependence from the endpoint, but no monotone potential, finite-state quotient, or divisibility obstruction has yet been proved from it.

## Bounded-cut demotion

The positive `<1379` and lower `>-1318` calculations are algebraically correct under the old cut assumptions. However those assumptions place the cut after the relaxed greedy first-26 schedule, which is not a legal trajectory.

Do not use this interval as a live-prefix finite theorem.

A repaired version would need to enumerate or analytically bound states at the 26th x-zero over **legal** prefixes, preferably reusing the exact legal-prefix automaton rather than fixing column 70.

## Bridge status

The exact radius-3 branch remains valuable but is not presently connected to the RL full-phase branch by a valid global bridge.

RL49 ruled out the old half-period shortcut. Gate A `H>=t+3` remains unproved globally. A root-specific Gate B matching genuine RL full-phase data to radius-3 hypotheses also remains unproved.

Eliminating the sole safe-CF survivor would be a major full-phase result but would not automatically establish Gate A for all denominator regimes.

## Highest-leverage missing lemma after audit

The clean survivor-local target is

`Zx_late < Delta`

where

`Delta = 0.3884589215938109...` exactly as above.

Combined with the legal first-26 maximum, this contradicts the inherited requirement `Zx>143/12`.
