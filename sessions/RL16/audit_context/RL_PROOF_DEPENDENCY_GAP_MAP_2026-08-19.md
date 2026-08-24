# Collatz R# RL — Proof Dependency and Gap Map

**Date:** 2026-08-19

## 1. Current shortest RL architecture

```text
Definition of red + least red R#
          |
          v
RL-F1/F2 minimality, oddness, R# != 2 mod3
          |
          +------------------------------+
          |                              |
          v                              v
RL-F3/F4 prefix pruning             RL-N1/N2 xi identity/barrier
b0=1, b1<=2                         xi(y) >= R#+1
          |                              |
          +---------------+--------------+
                          |
                          v
                exact odd preperiod b
                          |
                          v
RL-L1 eliminated LREC Diophantine system <---- exact cycle equation/rotations RL-C1/C2
          |                                      |
          |                                      v
          |                              cycle min + all states >= R#
          |                                      |
          +----------------+---------------------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
     RL-L3 suffix matching        RL-L5/L6 prefix/slack
     mod 3^h, all h              entry rotation budget
             |                           |
             +-------------+-------------+
                           |
                           v
               RL-L9 xi-weighted cycle
               parity/valuation/height coupling
                           |
                           v
              [OPEN RL-O1/O2/O3 CORE]
                           |
               exact infinite exclusion
               or finite automaton +
               proved extension theorem
                           |
                           v
                 CONTRADICTION TO RL
```

The inverse-tree route sits beside this mainline rather than inside it:

```text
cycle/preperiod physical inverse basin
        |
        v
RL-F8 collision-periodicity theorem
        |
        +-- k>0 root R#: path injectivity available
        |
        +-- cycle roots: quotient by physical endpoint required
                           |
                           v
                  [OPEN RL-O4 ownership]
```

## 2. Closed dependencies

| Edge | Status | Comment |
|---|---|---|
| red invariance -> least-red barrier | **CLOSED / PROVED** | no branch dependence |
| least-red barrier -> `b0=1`, `b1<=2` | **CLOSED / PROVED** | new RL prefix theorem |
| xi algebra -> red xi barrier | **CLOSED / PROVED** | transfer fully revalidated |
| odd iterate -> cycle equation/rotations | **CLOSED / PROVED** | exact integer algebra |
| preperiod + cycle -> eliminated LREC | **CLOSED / PROVED** | exact Diophantine coupling |
| LREC -> mod `3^h` suffix matching | **CLOSED / PROVED** | arbitrary h up to min(k,L) |
| least-red forward barrier -> prefix ceiling/slack | **CLOSED / PROVED** | exact analytic inequality |
| exponent parity -> cycle-state mod3 -> xi height | **CLOSED / PROVED** | exact cross-adic coupling |
| inverse collision -> periodic root | **CLOSED / PROVED** | correct RL collision semantics |

## 3. Critical gaps

### RL-O1 — Suffix matching needs an extension theorem

For every `h<=min(k,L)`, the terminal `h`-suffix of the preperiod and the terminal `h`-suffix of the entry rotation of the cycle must share the same exact `Phi_h` signature modulo `3^h`. This gives arbitrarily deep matching when `k` is large, but it is not yet known whether the signature system becomes injective enough, forces a forbidden cycle pattern, or admits a compact recurrent survivor automaton.

**Required closure object:** a theorem classifying all infinite-compatible suffix towers, or proving that every tower violates prefix/minimum/xi constraints.

### RL-O2 — Prefix slack versus all cycle rotations

The entry rotation obeys

`B + A_j <= (k+j) beta_R`.

All rotations also obey exact integrality and the common minimum barrier, but these facts have not yet been fused into a rotation-uniform exclusion. The strongest next move is to transport a finite amount of entry slack around a full rotation state, not to enumerate raw exponent words.

### RL-O3 — Xi profile around the cycle

At present only the coarse implication “odd preceding exponent => next state has `v3(c+1)>=1`” is used. The full profile

`m_j = v3(c_j+1)`

contains more information. Consecutive exponent-1 steps raise `m` exactly and preserve xi. A successful theorem may turn the cyclic `m`-profile into a constrained automaton coupled to the `a`-word.

### RL-O4 — periodic inverse-basin ownership

Any future inverse proliferation argument must deduplicate physical endpoints on the loop. The quotient relation is exact but no bounded multiplicity/ownership theorem has yet been proved for side branches attached to a periodic core.

### RL-O5 — branch split may be essential

`k=0` has a much sharper root: `R#=C_min`, `R#=1 mod3`, six mod144 residue classes, and a cycle word rotated to its minimum beginning with `1` and ending in an even exponent. `k>0` has strict `R#<C_min` and nonperiodic-root inverse injectivity. Treating these as one undifferentiated case may discard useful structure.

## 4. External dependencies

The published `2^71` computation and current cycle-length bounds may be used as explicit external inputs, but no theorem in the internal chain may silently upgrade a computation to a universal Collatz result. Hercher's 2023 `m>=92` theorem should be read with the corrigendum linked by the journal in 2026.

The 2026 Christoffel-word result is a promising preprint lead for rotation extremality, not a frozen dependency.

## 5. Distance-to-closure assessment

The first RL session has closed the **formulation gap**: there is now one exact coupled object instead of separate “tail” and “cycle” discussions. The remaining gap is not a missing algebra identity. It is an infinite-structure theorem showing that no exponent/valuation/collision state can satisfy all LREC constraints indefinitely.

Accordingly, the next session should attack the suffix/rotation/xi state system directly rather than expand the literature review or import RO XCORL machinery.
