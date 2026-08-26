# RL116 target — two-base finite transducer with synchronizing defect

## Objective

Work only on the next retained RL113 route. Construct a sound finite-state
transducer for one selected closest-pair transport step that carries binary
position, ternary rank, and the ordinary full-numerator ownership condition,
rather than parity grammar alone. The intended success is a proved
synchronizing defect that excludes an owned selected support with `R>=4` or
forces the already-closed `R<=3` branch.

## First mandatory lemma

Specify the state set, transition map, input/output data, and an invariant
mapping every actual ordinary owned zero-flow-cut swap to a transition.
Prove the state set is finite **uniformly in the variable denominator**
`D=2^A-3^L`, or give a proved finite quotient that preserves exactly the
ownership information it uses. The RL20 word must enter a non-owned reject
state because its numerator is not divisible by `D`, not merely because it
has a radius-four local pattern.

## Mandatory red teams

1. RL20 rejection must occur at the full ordinary ownership input.
2. Preserve `D|Q` and `D|S` without cancelling the generalized increment
   factor (RL79).
3. Treat `Q/D` as physical only after actual ownership is established
   (RL81).
4. Locate precisely the use of primitivity/distinct rotations and `S!=0`.
5. Mark any Raw/Farey subcase as branch-specific.
6. Label finite-state exploration and scans with exact complete bounds;
   they do not prove a uniform transducer theorem.

## Stop and handoff

Record a barrier and stop this route if retaining exact `D|Q` needs an
unbounded modulus, residue, counter, or state space; if the state machine is
only a parity/local-grammar machine; or if synchronisation is empirical.
On that outcome begin the legal S-unit gap route, retaining the binding
fallback order.
