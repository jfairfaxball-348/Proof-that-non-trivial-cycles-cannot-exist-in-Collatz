# RL234 — stop-and-repair: RL231 sparse-family charging coverage

Date: 2026-09-02

## 0. Outcome

RL234 entered the owned macro-reset target from the verified RL233 state. During mandatory red-team work, it found a first-invalid dependency in the inherited RL231 charging theorem.

**Outcome: STOP-AND-REPAIR.**

No branch contradiction, terminal-rank deletion, Gate closure, or global exclusion is claimed.

Frozen live state remains:

- sole high branch `(37,0,23,-1)`;
- K corridor `128081997553 < K < 146795909391`;
- frontier `13415865870`;
- e=4 rank `31435476727` live with `3856660232` combined arithmetic survivors through transition 43;
- RL232 combined H17 chronological spacing `>=1001`;
- Gate A open;
- Gate B open;
- global non-trivial-cycle exclusion open.

## 1. Valid analytic lemma retained from RL234

For a physical owned first-defect terminal with terminal numerator `T`, endpoint maximum `H`, residue factor `rho`, and unequal endpoint heights, the physical corrected flow obeys

`|f| = rho |2^-b - 2^-a| >= rho 2^-H`.

The terminal K identity is

`K = (T/2^H) rho`.

Therefore

`|f| >= K/T > 128081997553/T`.

This **K-priced defect lemma** is analytic and independent of the RL231 charging coverage defect. It is not used here to promote a stronger flow floor.

## 2. Exact retained H20 counter-state

Replay the RL186/RL187 first-defect arithmetic and the RL231 full-prefix physical-gap filtering for

`T = 5*3^35 = 250157725494998535`, `H=20`.

The exact retained rows include simultaneous offsets `32,33,34,35`. Their full-prefix cores intersect on

`[96166487668, 98855162143]`.

Applying the inherited physical K corridor gives a nonempty K-compatible subinterval

`[96351434735, 98855162143]`.

This is a **necessary-state countermodel to the charging proof**, not a claimed physical Collatz realization.

## 3. The RL231 charging gap

RL231 uses `U=2^-25` and the schedule

- `tau<=34`: `x=(128/7)U`;
- `tau=35,36`: `y=(4/3)U`;
- `tau>=37`: `U`.

The retained H20 cell `{32,33,34,35}` receives

`3x+y = (1180/21)U`.

The generic H20 budget used by RL231 is

`2^-21 = 16U`.

Hence the cell exceeds that budget by

`(844/21)U`.

Even replacing the generic budget by the maximum possible physical K-priced budget over the inherited corridor gives at most

`(146795909391/250157725494998535) = 19.690190857755 U`,

still far below `(1180/21)U`.

RL231 subtracts explicit high-family penalties only for six named H18-H21 terminal families. Its H20 penalty is attached to the distinct six-owner family `{31,32,33,34,35,36}` with terminal invariant `3^36`; it does not price the retained `T=5*3^35`, `{32,33,34,35}` cell.

Therefore the promoted RL231 lower-bound calculation does not cover the complete retained necessary state space.

## 4. Correction/demotion consequences

The first invalid dependency is the RL231 sparse-family charging coverage step.

Demote pending repair:

1. RL231 ordinary absolute corrected-flow theorem `>665`.
2. RL231 signed-flow and directional-K bounds derived from that theorem.
3. RL231's quantitative assertion that further uniform early-charge improvement requires combined H17 incidence `<=1,615`.
4. The spacing-only scale `85,103,989` derived from that incidence threshold.
5. RL232/RL233 references that treat `1,615` as a binding inherited required incidence target.
6. RL233's standalone 3-adic scale consequence `b>=85,103,989`.

Preserve:

- RL231 exact ownership enumeration and exact H17 two-family classification, except where a statement depends on the flawed charging lower bound;
- RL231 individual recurrence certificates for H18-H21;
- RL232 exact four-class H17 return exclusion through separation 1000, hence combined H17 spacing `>=1001`;
- RL232 exact H17 K-compatible cores, H17-A K floor, local owned-prefix results, and method-barrier constructions;
- RL233 exact owned-return telescope, dyadic rebasing, finite 3-adic source-memory theorem, unit-modulus fixed-label reversibility, and complete finite-modulus decomposition;
- frontier/e=4/Gate/global status.

## 5. RL234 scratch withdrawals

The uncommitted RL234 exploratory flow figures `>842`, `>872`, and `>921` are **withdrawn / not promoted**. They were built while probing the inherited charging layer and are not authoritative.

One additional scratch issue was found before closeout: a nonmonotone trial charge that set `tau=35,36` to zero and restored positive charge for `tau>=37` cannot use inherited upper-tail `N_n` bounds as a lower-bound staircase in that form.

Neither scratch issue changes the preserved analytic K-priced defect lemma.

## 6. Successor

RL235 must repair RL231's charging coverage before the macro-reset/H17-incidence route is resumed.

The repair must enumerate **every retained simultaneous-owner terminal cell actually exposed to charge**, prove each is either locally budget-safe or assigned a rigorously applicable global occurrence penalty/cap, and only then recompute a corrected flow floor and any resulting H17 target.
