# RL147 target — layerwise carry order or negative-defect pivot

## Primary objective

Exploit RL146's exact contact-carry order mechanism beyond binary height one.  Determine whether a nonnegative mixed-height owner can be decomposed into binary layers carrying enough compatible arithmetic structure to inherit an order, monotonicity, or cyclic-lock contradiction.

## Frozen inputs

- RL145 exact ordinary-owned cyclic contact-carry recurrence and subset-weight injectivity.
- RL145 local height-one CRT/population coefficient saturation barrier.
- RL146 theorem: no primitive height-one owner exists for any `g>1`.
- RL146 residue ladder
  `3 y_{t,r}+h_{t+1,r}=2^{a_r}y_{t,r+1}+h_{t,r}`
  and its binary strict-order proof.

## Phase A — layer decomposition

For nonnegative heights, write each height as a sum of binary superlevel indicators.  Derive exactly which owner/contact polynomial and carry identities are linear across these layers and which are not.  Do not assume ownership factorization or independent divisibility.

Seek a rigorous layerwise carry state whose cyclic endpoint is inherited and whose comparison error remains dominated by the factor `3`.

## Phase B — mixed-height order alternatives

If simple binary layering is insufficient, test:

- lexicographic order across height layers;
- weighted carry vectors;
- bounded-difference comparisons using the mechanical `2^{a_r}` transition;
- telescoping identities that force a maximal layer to behave like an owned height-one subsystem.

Any promoted theorem must state exactly what height range/sign assumptions it uses.

## Phase C — mandatory pivot condition

If mixed-height nonnegative layers do not inherit enough ownership/carry structure for a genuine coefficient-independent gain, freeze the exact obstruction.  Then pivot the next target to true negative-defect structure.  Do not return to the saturated `162/13` local population route merely by adding more congruence labels.

## Deliverables

Produce a proof-state report, fast verifier for exact algebra/sanity checks, updated correction/demotion ledger and open frontier, completion review, session state, next target, checksum manifest, reconstructable bundle transport, and fresh-unpack verification.

## Scope discipline

RL146 closes only primitive height-one owners with `g>1`.  RL147 must not silently promote that to `g=1`, mixed heights, negative defect, all non-trivial cycles, Gate A/B globally, or Collatz closure.
