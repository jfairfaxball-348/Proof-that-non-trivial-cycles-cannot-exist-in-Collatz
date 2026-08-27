# RL125 — `H`-floor tail cut for `L=11`

## Outcome and classification

RL125 gives an analytic tail improvement for the RL124 `L=11` target:

> Every hypothetical primitive nontrivial positive ordinary shortcut cycle with `L=11` has `7<=Z<=33`.

Together with the inherited `L>=11` frontier, this is an **analytic necessary-condition reduction** only.  It does not exclude the remaining strip and does not close Gate A, Gate B, the nontrivial-cycle problem, or Collatz.  No inherited result is repaired or demoted.

## Proof

RL123 supplies the parameter floor

`W >= H(11,Z)=min_t max(E_0(Z,t),E_1(11,t),6(t-1))`.

Direct finite evaluation over `t=1,...,11` gives `H(11,34)=89`.  For `Z>=11`, the minimization index set is fixed at `t=1,...,11`; each `E_0(Z,t)` is nondecreasing in `Z`, hence so is each fixed-`t` maximum and their pointwise minimum `H(11,Z)`.  Therefore `H(11,Z)>=89` for every `Z>=34`.

On the other hand, the inherited numerator diameter ceiling gives `D W<=B`, where

`D=2^(11+Z)-3^11`, `B=(2^Z-1)(3^11-2^11)`.

Exact simplification yields

`86D-B = 1029*2^Z-15,059,543 > 0` for every `Z>=14`.

Thus `W<B/D<86` for `Z>=34`, contradicting `W>=89`.  RL124 already supplies positivity from `Z=7`; consequently only `7<=Z<=33` remains.

Classification: **proved analytic mathematics**, relying on the inherited ordinary physical-ownership framework for `H` and the width ceiling.

## Verification and scope

The verifier checks `H(11,34)=89`, its monotonicity over a finite diagnostic range, and the exact displayed width identity.  The monotonicity proof above, not the finite diagnostic range, supplies the unbounded conclusion.

RL20 ownership, RL79 scaling, RL81 physical-state ownership, primitivity separation, and Raw/Farey scope carry forward unchanged.  The local corrected profile-capacity enumeration for `Z=7,...,20` remains **NOT PROMOTED**: it is an incomplete partial scan, retained only under `.rl-work/RL125/`.

## RL126 kickoff

Continue the depth-sensitive capacity attack on the remaining `L=11`, `7<=Z<=33` strip.  Develop a constrained profile generator before an ownership scan; raw ordered-profile counts are too large near the upper endpoint.
