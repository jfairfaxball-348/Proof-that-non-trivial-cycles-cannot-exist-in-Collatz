# RL257 session state and RL258 kickoff

Date: 2026-09-05

## Frozen RL257 state

Classification: **R4_BRIDGE_REDUCED**.

The first halving selector remains

`(1100,694,406,317,200,14,4)`,

but `k=33` is now eliminated by exact full-phase internal-prefix legality.

The only remaining terminal exponent at this frontier is

`k=31`.

For `k=31`:

- `E_31<=27`;
- exact canonical right-flank floor `E_right>=11`;
- equality right prefixes:
  `110110111`, `110111010`;
- left weighted zero budget `E_left<=16`;
- at most five zeros among the final ten internal x-bits;
- 141 universal left x-patterns;
- 2719 right/left flank x-pattern pairs survive the exact E-budget plus
  complement-capacity certificate.

Historical endpoint correction is binding:
`J=2^k` is the internal terminal boundary before the omitted `(1,0)`.

Notation correction is binding:
`H_sel=14` is not canonical area `H_can`.

## Successor

RL258 is **PREPARED, NOT STARTED**.

Read `RL258_K31_TWO_FLANK_CANONICAL_COMPATIBILITY_TARGET.md`.

Gate A/B remain open. Radius 4 is not invoked. Radius 5 inactive.
