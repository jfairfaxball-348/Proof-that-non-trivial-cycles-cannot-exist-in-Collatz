# RL217 research report — prefix-wide universal height automaton

Date: 2026-09-01.

## Target worked

RL217 was tasked with generalising RL216's successful single-prefix height cone across the remaining 45,045 e=16 prefixes without enumerating 331,927,916 arithmetic lifts.

## Main advance

The critical compression is stronger than prefix memoisation: after phase 16 all prefixes share the same physical formula in the lifted coordinate `x=eta_*+3^17 k`. The height consumer is therefore one universal 2-adic automaton. Prefixes differ only in the affine offset and finite `k` interval used to sample that automaton.

A universal cylinder `x=r mod2^m` converts exactly to one congruence on `k`. Whole prefix intervals can then be intersected with the survivor set by cyclic range arithmetic.

## Exact finite-horizon result

At horizon 51:

- processed universal states: 14,514,513;
- failure cylinders: 1,705,547;
- live cylinders: 3,132,617;
- maximum 2-adic precision: 25 bits;
- incoming RL216 candidates: 331,927,916;
- removed through phase 51: 192,346,636;
- surviving arithmetic candidates: **139,581,280**.

The consumer is substantial, removing about 58% of the incoming arithmetic family, but it does not empty a full surviving prefix. Every one of the 45,045 prefixes retains between 2,995 and 3,235 candidates. Both states, every necessary mod18 class and all 469 eta classes modulo2187 remain live.

## Boundary / why the height route is frozen here

The universal construction avoids candidate enumeration, but its live cylinder count grows rapidly. By phase 51 it already contains 3.13 million disjoint classes at up to 25-bit precision while no prefix is close to empty. A raw extension by depth alone is therefore not a good next authoritative job. This is recorded as a method barrier, not as a theorem that deeper height information is useless.

The smallest exact unresolved interface is the phase-51 survivor selector itself: for each prefix, retain the inherited root progression and `k` interval, terminal-Hensel exclusions, and the requirement that `x` lie in one of the certified live 2-adic cylinders.

## Successor direction

Per direct user instruction, RL218 is not a blind continuation of height depth. It is a deliberately scoped revival of the certified-blue-basin idea, now asking whether exact finite legal backward Collatz words act as arithmetic selectors on this much thinner RL217 lattice. RL80/RL81 no-go locks are inherited explicitly: density, proximity and arbitrary backward saturation are not cycle traps, and the old auxiliary-transfer route stays closed absent a new exact ownership bridge.

No Gate, rank, physical-word, charge, ownership or correction/demotion lock changes in RL217.
