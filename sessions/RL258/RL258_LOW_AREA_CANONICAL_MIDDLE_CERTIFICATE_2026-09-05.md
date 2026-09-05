# RL258 — k=31 exact low-area canonical middle certificate

Date: 2026-09-05
Classification: **TARGETED_GATE_A_CERTIFICATE**

## Incoming exact frontier

The unique first halving selector is

`(a,ell,z,q,r,H_sel,n)=(1100,694,406,317,200,14,4)`.

RL257 eliminates `k=33`.  The only remaining terminal exponent at this first
frontier is `k=31`, with 2719 right/left flank x-pattern pairs surviving the
exact E-budget and complement-capacity certificate.

Binding conventions retained:

- the internal terminal boundary is `(d,J)=(1,2^31)` before the omitted
  terminal `(1,0)`;
- `H_sel=14` is not identified with canonical accumulated area `H_can`.

## 1. Exact terminal inversion

For every ten-bit left suffix, invert the exact RL45/RL64 x-driven transition
from `(d,J)=(1,2^31)`.

All 141 suffix words with universal left weighted zero cost at most 16 have
at least one legal inverse chain.  Together they have exactly 2706 inverse
chains.

After coupling these inverse chains to the 2719 RL257 flank pairs, there are
exactly 53335 owned prefix/suffix canonical-state realizations.

Thus terminal inversion alone does not eliminate the first frontier.

## 2. Gate-A-dangerous area contraction

At `k=31`, a completion still unresolved by Gate A must satisfy

`H_can <= 30`.

The internal path length is `m=1068`.  RL257 fixes the first nine x-bits and
RL258 fixes the final ten x-bits/inverse chains, leaving a middle of length

`1068-9-10 = 1049`.

For any positive height path whose middle begins at height `s` and ends at
height `e`, the unavoidable middle-area contribution is

`s(s-1)/2 + (e-1)(e-2)/2`.

This is attained by descending to height one as early as possible, remaining
there, and making the required ascent as late as possible.

Combining this exact lower bound with the exact prefix and suffix area leaves:

- 667 low-area owned realizations;
- 348 distinct flank x-pattern pairs;
- total prefix+unavoidable-middle+suffix area lower bound between 21 and 30;
- only 71 distinct `(remaining middle-area budget, starting d, starting J)`
  middle automata;
- each remaining middle-area budget is between 1 and 10.

## 3. Exact sparse-excursion automata

For each of the 71 cases, run the exact canonical transition while retaining
every legal x-choice whose accumulated middle area remains within its budget.

This is a safe superset of genuine completions: the automata do not impose
the exact remaining x/y weights, so failure here is stronger than failure
after adding those constraints.

Exact exhaustive result:

- 16 automata become empty;
- 55 repeat their complete state set exactly;
- latest empty/repeat depth: 154;
- repeat periods: 1, 2, 3, 11, 33;
- maximum J reached anywhere in every full preperiod/cycle: 212.

By contrast, among all 667 required terminal-side predecessor states,

`min J_required = 9049478310`.

Therefore no low-area automaton can ever reach any required terminal-side
predecessor.  Once an automaton repeats its full state set, all future depths
repeat exactly; empty cases remain empty.

Hence no genuine completion at this first frontier can have `H_can<=30`.

## 4. Promoted conclusion

At the unique first halving selector,

`(a,ell,z,q,r,H_sel,n)=(1100,694,406,317,200,14,4)`,

the remaining case `k=31` satisfies

`boxed: H_can >= 31`.

Together with RL257's analytic elimination of `k=33`, the complete first
halving frontier is removed from the branch simultaneously unresolved by
Gate A and Gate B.

## Scope

Promoted:

- exact backward terminal ownership count;
- exact low-area contraction from 53335 owned realizations to 667;
- exact 71-automaton finite certificate;
- targeted Gate-A safety `k=31 => H_can>=31` at the first halving selector.

Not promoted:

- no uniform Gate-A theorem;
- no Gate-B closure;
- no Radius-4 application;
- no global cycle exclusion;
- no claim that the arithmetic selector itself is impossible;
- no claim about the next arithmetic selector/frontier.

The successor must recompute the next simultaneous unresolved frontier using
the already-promoted arithmetic machinery, with this first selector removed.
