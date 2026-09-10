# RL294 scratch freeze

Date frozen: 2026-09-10
Status: `UNPROMOTED_EXPLORATORY_PROVENANCE`

This file preserves the mathematically relevant unfinished RL294 work. Nothing in this file is authoritative theorem/certificate unless it is also stated as promoted in `RL294_REPORT.md`.

## A. T-coordinate tower and `(4,39)` zero spine

Use

`T=K+1-3^d`.

For P=`(2,3)` one has T=-2. At any state with T=-2:

- `x=0` gives T=-1 at the same depth;
- another `x=0` gives T=-2 at depth one higher.

Thus the macro `00` raises depth by one and returns T to -2. The constructed P cost to the depth-d T=-2 tower is

`C_P(d)=(d-2)(d-1)`.

Explicit tower members:

- d=2, J=3, cost 0;
- d=3, J=17, cost 2;
- d=4, J=63, cost 6;
- d=5, J=209, cost 12;
- d=6, J=663, cost 20.

For `(4,39)`, T=-26. Repeated x=0 gives the exact spine

`-26 -> -13 -> -20 -> -10 -> -5 -> -8 -> -4 -> -2`

with cumulative source costs

`0,3,6,10,14,18,23,28`.

The endpoint is `(6,663)`, the P T=-2 tower member, which P reaches at cost 20.

The exact first-x1 exit cut from the seven premerge states is:

1. `(4,66,T=1)` at source cost 3;
2. `(3,26,T=7)` at cost 6;
3. `(5,302,T=91)` at cost 10;
4. `(5,317,T=106)` at cost 14;
5. `(4,103,T=38)` at cost 18;
6. `(6,1017,T=352)` at cost 23;
7. `(6,1023,T=358)` at cost 28.

Known exploratory P costs included

`m_P(4,66)=4`,
`m_P(3,26)=4`,
`m_P(5,302)=17`,
`m_P(5,317)=21`.

The first two exits are immediately owned under the `(4,39)` allowance; the later exits motivated the cascade reformulation.

## B. Early local continuation from difficult exits

Recorded exploratory children:

- `(5,302)`:
  - x1 -> `(4,151)`, source cumulative cost 14, P cost 16;
  - x0 -> `(6,801,T=136)`, cumulative cost 14, P cost observed 21.

- `(5,317)`:
  - x1 -> `(5,491,T=280)`, cumulative cost 18, P cost observed 21;
  - x0 -> `(5,264,T=53)`, cumulative cost 18.

- `(4,151)`:
  - x0 -> `(4,108,T=43)`, cumulative cost 17, P cost observed 19;
  - x1 -> `(4,234)`, cumulative cost 17, P cost observed 14.

- `(5,491)`:
  - x1 -> `(5,752)`, cumulative cost 22, P cost observed 20;
  - x0 -> `(5,351)`, cumulative cost 22.

These values were used as route diagnostics, not certificates.

## C. P-avoidance-tree evidence

A source branch was pruned whenever P had already reached the identical physical state with the required one-unit owner advantage.

Exploratory results:

- through source cost 60, only 343 undominated states remained and there was no undominated positive first-d=1 arrival;
- through source cost 120, 20,267 retained competitor states and 1,080 P-dominated cut states were observed, again with no undominated positive first-d=1 arrival;
- the first apparent escapes moved sharply outward when the P-owner oracle cap was raised.

These computations were exploratory and were not packaged as exact promoted certificates.

## D. Corrected `J=76611` example

A long competing history produced a first positive boundary state

`(d,J)=(1,76611)`

at historical cost about 163 in the exploratory search.

This is not an owner counterexample. A P route was found with exact added cost 25, using a low-area positive route followed by a long zero-height boundary phase. An earlier scratch figure 26 is superseded.

The lesson was structural: raw positive physical-state cones overprice P if they do not efficiently quotient arbitrary zero-height positive boundary motion.

## E. Dual autonomous endpoint picture

Promoted in the report:

`N=K+1`, `T=K+1-3^d`,
`x=1 => N'=G(N)`,
`x=0 => T'=G(T)`,

where G is the half-step `(z/2)` / `((3z-1)/2)` map.

The interval `[T,N]` has exact length `3^d`.

This picture produced the cascade search but should not be treated as a standalone local potential.

## F. `(4,39)=P o R3` cascade route

Promoted identity:

`(4,39)=P o R3=P o Z o Z`.

Unpromoted stronger route:

Track the propagated output of the P factor. While the output remains 1, the Z factors remain in their neutral state. The first propagated 0 converts each Z to E; one further propagated bit sends E formally to either P or identity I.

This creates exact same-state mergers into P-derived cascades.

A candidate all-depth cut emerged:

- all nonexceptional first-output sectors appear P-owned with the needed `(4,39)` two-unit threshold;
- the unique unresolved early prefix is external `00`, reaching `(5,191)` at source cost 6.

The argument was not independently packaged/proved in full before CLOSEOUT_LOCK, so it is explicitly not promoted.

## G. `(5,191)` and P×P preperiod

Exact factorisation used in scratch:

`(5,191)=(3,K=24) o P`.

An output-controlled exploratory decomposition isolated a finite preperiod with first departures at approximately:

- `(5,201)` after added source cost 4 from `(5,191)`;
- `(4,151)` after 8;
- `(6,733)` after 13;
- `(6,949)` after 18;
- `(6,1273)` after 23.

The `(4,151)` branch was already same-state P-owned at its available allowance. A no-departure branch reached `(6,2853)` at cost 23 from `(5,191)` and was observed P-reachable at cost 24.

The coefficient dynamics in states `K=q 3^d` entered the small pattern

`4 -> 6 -> 9 -> 5 -> 3 -> 2 -> 3 -> 2 -> ...`.

This suggests an eventual parametric tail whose source/P cost difference is constant after a finite preperiod.

The exact finite preperiod proof and the tail domination proof remain RL295 work.

## H. Base-9 carry

Promoted barrier:

For `K=9A+r` with even r in 0..16, the residual/carry transition is finite but cannot be absorbed into a scalar correction `g(r)`.

This should be used positively in RL295: the missing object is a min-plus ordered factor/carry or wall-debt state, not another endpoint scalar.

## I. Formal wall / rejected-tube correspondence

When a cascade factor at depth one would take the rejected descent, it enters formal depth zero. At positive even checkpoint J, RL289's rejected-tube theorem says the number of formal binary levels available is exactly `nu_2(J)`.

Cascade composition can keep the total physical depth positive while one factor is formal depth zero. This is the exact place where the static danger-tree phase must be priced/refactored.

The simple hope that the composition cross-term `+L` pays all formal negative area is false: the cross-term can cancel the negative signed area of the formal depth-zero factor.

Therefore RL295 needs an explicit wall-refactorisation theorem.

## J. Exploratory P×P finite closure

A large exploratory shortest-path closure from

`P o P=(4,45)`

through added cost 30 produced approximately 11.37 million physical states. No threatening high Bellman value was observed; the largest recorded finite-window value was negative.

This computation is evidence only. It must not be cited as a proof or finite certificate unless independently reconstructed, range-checked, and frozen by a future session.

## K. Exact open successor questions

1. Is the candidate `(4,39)` cut to `(5,191)` fully correct at all depths?
2. Can the `(5,191)` finite preperiod and `2<->3` coefficient tail be proved as a finite-state min-plus quotient?
3. What is the exact refactorisation rule when one ordered factor reaches formal `d=0` with nonzero K?
4. Can every such wall debt be transferred into checkpoint 2/P, or into a finite list of residual wall states?
5. Once `(4,39)` is closed, do the exact negative-front-door cascade factorizations close by the same transducer?
6. Does the resulting finite augmentation prove the all-depth first-d=1 owner theorem, or only the five front-door owner hypotheses?
7. Only after that: can the tight P-source static principal-cylinder danger tree prove `Bcal(P)<=1`?
