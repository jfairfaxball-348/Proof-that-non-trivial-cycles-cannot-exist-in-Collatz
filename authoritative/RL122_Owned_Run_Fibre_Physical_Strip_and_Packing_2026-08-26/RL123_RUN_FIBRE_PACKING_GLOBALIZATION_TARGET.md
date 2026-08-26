# RL123 target — run-fibre packing globalization

RL122 has supplied the first new global ordinary-owned physical-width resource after the RL110/RL121 barrier:

`W >= P(w)`

and therefore

`D P(w) <= B(A,L) := (2^Z-1)(3^L-2^L)`

for every hypothetical primitive nontrivial positive ordinary shortcut cycle.

RL123 must test whether this new resource can be strengthened into a global producer/contradiction.

Work in this order.

## Priority A — exact combinatorial lower envelope for `P(w)`

Write the cyclic word as alternating zero-runs and one-runs.  Express

`Z_k = sum_j max(z_j-k+1,0)`,
`O_k = sum_j max(o_j-k+1,0)`.

Determine, analytically, the smallest possible

`P(w)=max_k{(Z_k-1)2^k+1,(O_k-1)3^k}`

compatible with fixed `(L,Z)` and primitivity.

The target is a theorem, not a bulk scan.  A finite verifier may falsify candidate lower envelopes but cannot replace the proof.

## Priority B — multi-fibre packing

If the max-of-one-fibre bound is insufficient, exploit simultaneous occupancy of several physical residue fibres.

In particular, states at an odd-to-even boundary can satisfy both

`x == 0 (mod 2^k)` and `x == -1 (mod 3^j)`

for suitable adjacent zero/one run depths, hence lie in a CRT class modulo `2^k3^j`.

Seek a rigorous union/interlacing/CRT packing lower bound on `W` stronger than the simple maximum of individual fibre spacings.

A valid theorem must use actual physical states and must preserve the RL79 generalized-increment discriminator.

## Priority C — couple packing to closest-rotation radius

On the live complement `R_*>=4`, seek a theorem forcing enough run diversity, run depth, transition count, or CRT fibre occupancy that the RL122 packing inequality fails.

Do **not** assume `R_*>=4` directly implies long runs without proof.  RL20 remains the local-geometry falsification model.

## Success conditions

Any one of the following is useful:

1. prove `D P(w)>B(A,L)` for all remaining nontrivial primitive ordinary words;
2. reduce the remaining `(L,Z)` or run-profile family to a finite explicitly parameterized set by an analytic theorem;
3. force `R_*<=3`, handing the word to the closed local engine;
4. prove a stronger multi-fibre physical-strip theorem with a demonstrable new excluded parameter range.

## Mandatory red teams

Every promoted statement must record:

- RL20 ownership discriminator;
- RL79 generalized-increment scaling;
- RL81 physical-state ownership;
- exact use of primitivity;
- Raw/Farey scope;
- finite-certificate scope.

No Gate closure may be claimed unless the actual global obligation is discharged.
