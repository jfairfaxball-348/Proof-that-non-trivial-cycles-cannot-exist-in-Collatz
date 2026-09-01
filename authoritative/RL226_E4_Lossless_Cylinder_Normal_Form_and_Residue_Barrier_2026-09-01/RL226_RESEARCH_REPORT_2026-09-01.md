# RL226 research report — e=4 lossless cylinder compression

Date: 2026-09-01.

## Objective

Continue RL225's e=4 deterministic height attack without enumerating billions of k values. Seek an exact state merge or identify the datum preventing such a merge.

## Main advance

The rapidly growing RL225 state carried six entries `(phase,r,m,u,v,h)`. RL226 proves that after phase 36 the slope and height are not branch data at all:

- `u_i=3^(i-36)U_36`;
- `h_i=19+b(i)-b(36)-m`.

Exact valuation `a` consumes exactly `a` local k-bits. The lossless state is therefore reduced to `(phase,r,m,v)`.

This is a genuine quotient of the stored state, but not the hoped-for collapse to `(phase,m)`. The residue/intercept is mathematically load-bearing for the finite k-window. A phase-43 same-precision witness gives cylinder cardinalities 3 and 4, proving that exact finite counting changes when the residue translation changes.

## Exact contraction

The compressed verifier reproduces all RL225 failure counts and extends exact height replay through transition 43:

- transition 42: 1,299,949 new failures;
- transition 43: 3,429,092 new failures.

The combined survivor count after retaining terminal-Hensel coupling is **3,856,660,232**. The first terminal-Hensel candidate height failure occurs later than this certified depth, so overlap is zero through transition 43.

## Interpretation

The candidate family is contracting, but raw cylinder count grows from 361,277 states at phase 42 to 1,906,336 at phase 43. The new theorem explains both the available compression and why naive merging stalls: structural feasibility is controlled by phase/precision, while exact membership in the finite k-window remains translated by residue/intercept.

A future local consumer would need an endpoint-aware residue transducer, BDD, digit automaton, or another exact way to encode that translation without expanding every cylinder. RL226 does not assert which such consumer will succeed.

Per user directive, RL227 instead becomes a closure-roadmap session before further local implementation work.
