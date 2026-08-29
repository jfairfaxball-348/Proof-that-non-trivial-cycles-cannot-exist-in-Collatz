# RL174 certified facts and proof ledger

## Correction / demotion

- **RL173 physical-functional identification — DEMOTED.**  With accelerated
  weights `q_i=2^(S_i)/3^i` and exponent-prefix flow `G_i`, the rotated weight
  is `q_i 2^(G_i)`, not `q_i 3^(-G_i)`.
- RL173's exact values `-52/81` and `176/27` remain certified only for the
  auxiliary `F3=sum q_i(3^(-G_i)-1)` functional.
- The old two-witness argument is superseded as a proof about physical
  weighted-difference sign.

## New proved analytic mathematics

- **RL174.1:** `F2=sum q_i(2^(G_i)-1)=3(lambda-1)(y_p-y_0)` for the accelerated
  ordinary `+1` p-rotation.
- **RL174.3:** in the physical coprime `g=1` first-survivor least-root branch,
  `y_p-y_0>(lambda-1)m` and `F2>3m(lambda-1)^2`.
- Distinct odd physical states give the internal floor `F2>6Delta`.
- **RL174.5:** if `h_p=0`, then `F2<2/3` using the inherited internal
  `m<2^75` and below-neighbour discrepancy strip.

## Exact rational certificates

- Correct local sign-nonforcing witnesses for `F2`:
  - `(1,4)` gives `14/3`;
  - `(2,5,4)` gives `-28/9`.
- Exact logarithm enclosures certify
  `6Delta>1/186000000000`.
- Conditional on inherited external `m>=2^71`, they certify
  `y_p-y_0>=2,120,000,002` and `F2>1/176`.
- The height-zero upper estimate is certified strictly below `2/3`.

## Inherited facts used

- RL133 nonnegative defect for the coprime `g=1` first survivor.
- RL134 `5theta<1`, `-6Delta<d_-<-5Delta`, and internal `m<2^75`.
- RL168 lifted-defect/state-order framework and physical squeeze.
- RL169 chronological pair-gap theorem.
- RL163 p-arc/Bezout constants.
- The external computational least-state floor `m>=2^71` only where explicitly
  labelled conditional.

## Global status

No cycle construction or exclusion. Gate A and Gate B remain open. Global
non-trivial-cycle exclusion and the Collatz conjecture remain open.
