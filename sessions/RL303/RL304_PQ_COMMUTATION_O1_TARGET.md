# RL304 — P/Q commutation grammar for Bellman O1

Date prepared: 2026-09-12
Status: PREPARED, NOT STARTED

## Incoming classification

RL303 closes as

`DYADIC_WALL_LATTICE_TRANSLATION_NORMAL_FORM_P_FIRST_WALL_REDUCTION_AND_GENERIC_LINEAR_DEBT_BARRIER_WITH_PQ_COMMUTATION_PROVED`.

O1 remains open:

`m_R3(E)>=m_8(E)`

for every positive even checkpoint `E`.

## Primary target — close the leading-P sibling on the actual Q stack

Use the collision-free right-wall factorisation

`RW_D=Q^n o U`,

where

`D=2n+1`, `Q=(2,18)`, `U=(1,6)`.

RL303 proved the exact physical one-cell commutation

`(P o Q)01110=Q o P`

at cost 14, and the all-r Q return family

`Q 0(10)^r110=Q`

at cost 2 with propagated output `00(01)^r11`.

Construct a **complete finite commutation/refactorisation grammar** for a P factor moving through the stack `Q^n o U`.

The desired outcome is one of:

1. every legal wall-derived leading-P sibling is rewritten to an exact smaller-wall owner with enough inherited credit;
2. P is pushed through the complete Q stack into a finite base family that checkpoint 8 owns directly;
3. a finite exact residual grammar is isolated, strictly smaller than the current leading-P problem;
4. an exact counterexample/barrier shows that the P/Q route itself cannot close O1.

## Required accounting

All macros must be physical/canonical after RL295 wall normalization. Do not charge fictitious negative-depth factor area.

Track total physical historical cost against the RL302 wall credits

`B_L(D)=(D^2+D-6)/2`,

`B_R(D)=(D^2+3D-4)/2`.

The important peel increment is

`B_R(D)-B_R(D-2)=2D+1`.

A fixed per-Q-cell commutation cost is potentially affordable for large D, but this must be proved with the full propagated-context grammar rather than inferred from the single 14-cost swap.

## Inherited exact tools

1. General dyadic lattice
   `W_(D,t)=((D),((4t+5)3^D-3)/4)`.
2. Translation-invariant adjacent-wall normal form
   `S 0 1^k01=S^+1^(k+1)00`
   plus leading-P sibling.
3. Four exact `D -> D-2` merger families from RL303.
4. Leading-P first-wall reduction to positive reserve plus normalized integer wall debt.
5. Direct root splice `R3 011 -> RW_3`, already checkpoint-8 owned one unit cheaper.

## Hard barriers to respect

1. Do not return to generic linear-credit integer wall-debt amortisation. RL303 proved a legal quadratic counterfamily:
   for `D=6n+3`, `W_(D,4)1^(3n)` versus `W_(D,0)(110)^n` has relative cost `-3n(n-1)/2`.
2. Do not use generic P insertion monotonicity; RL302 has exact counterexamples.
3. Do not rebuild an unrestricted relative wall grammar; RL302 identified it as circular with checkpoint-2 futures.
4. Do not claim higher lattice cells are cheaply checkpoint-8 accessible without an explicit all-depth owner construction.
5. Bounded search may discover macros but cannot substitute for the all-depth grammar.

## Secondary target — complete wall prefix coverage

If the P/Q grammar closes the leading-P sibling, combine it with RL303's four `D -> D-2` merger families and the adjacent-wall theorem to build a complete well-founded prefix cut for both `L_D` and `RW_D` wall inequalities.

If O1 closes, immediately return to RL302's contracted O2 residual (even trailing-P siblings and `A_d=F_d o Z`) before claiming the P/8 identity.

## Scope

Gate A OPEN.
Gate B OPEN.
Physical/resonance branch frozen at external selector frontier `a=7354673373747273032`.
Radius 6+ frozen.
RO/divergent-orbit work out of scope.
Lean formalisation separate.
No global non-trivial-cycle exclusion is claimed.
