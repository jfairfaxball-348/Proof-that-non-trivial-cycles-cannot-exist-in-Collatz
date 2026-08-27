# Open obligation frontier after RL129

## Promoted

- RL128 frontier `L>=13` is inherited.
- RL129 excludes every primitive positive ordinary shortcut-cycle candidate with `13<=L<=40`.
- New frozen primitive ordinary low-odd-count frontier: `L>=41`.
- Quotient rotation follows the exact halved Collatz map whenever `D|Q`.
- Universal transition-root numerator bound: `Q <= 2^(Z-1)(3^L-2^L)`.
- Exact global quotient ceiling for `L=13..40`: `30,400,121`.
- Exact descent certificate: all `15,200,061` odd starts through that ceiling descend to the trivial orbit.

## Corrections/demotions

- No new inherited theorem demoted.
- RL126 empty-depth-fibre repair remains in force.
- No exploratory RL129 capacity count is promoted; the quotient route supersedes it.

## Still open

- `L>=41` primitive ordinary candidates.
- Gate A.
- Gate B.
- Global nontrivial-cycle exclusion.
- Collatz conjecture.

## Next live target

RL130: extend quotient descent from `L=41`, starting with the exact quotient ceiling `727,618,641`, and investigate the small-positive-denominator spikes controlling scalability.
