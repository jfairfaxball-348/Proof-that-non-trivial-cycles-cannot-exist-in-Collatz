# RL178 Negative Compensation and Height-Return Target

## Main objective

Exploit the global negative-flow requirement created by RL177.  In the
preferred physical `h_p=0` branch, retain

`1<=J<=36`, `d=G_{J+1}!=0`, `v=v2(g_p)<=37`,

and

`T_first=sgn(d)*(2^|d|-1)*2^v/3^(J+1)`.

RL177 proves total negative corrected-flow magnitude `N>3/10^7`; in the
zero-common-height branch it proves `N>1/3` and leaves only 28 signed local
types.

The target is to convert that required negative budget into either:

1. a second quantized transition/return law that is incompatible with the
   physical height/order constraints; or
2. a stronger global bound that closes one first-mismatch branch or one of
   the high-valuation cases.

## Frozen input

Preserve all RL176/RL177 facts, in particular:

- corrected `G_i=S_{p+i}-S_p-S_i` and
  `F2=sum q_i(2^G_i-1)=3(lambda-1)g_p`;
- `4|g_p`, `4<=g_p<=185999999996`;
- `E_{p+i}=E_i+1` through the common prefix;
- first-order crossing: `d>0` reverses pair order, `d<0` preserves it;
- exact first-flow quantum;
- mandatory positive carry `T_t>1/2`;
- zero-height 28-type list and `N>1/3`;
- positive-height three-support loss and
  `F2<1/2-11Delta/16`;
- local-automaton barrier: every `v=2,...,37` and both signs remain feasible
  under the local rules alone;
- `|d|<=21`;
- high cases: `v=36 => H>=1`; `v=37,H=0 => J=23,d=+/-1` only.

The inherited external `m>=2^71` bound remains optional and must be explicitly
qualified if used.

## Primary attack A: earliest negative defect / height-order reversal

Define the earliest phase after `J+1` at which `G_i<0`, or, if the first
defect is negative, the earliest later phase at which `G_i>=0` or the height
difference returns to zero.

Derive an exact transition law for this first return/crossing.  Use the
mechanical increments and nonnegative heights, but also use the global
lifted-defect/value order and the required negative-flow magnitude.  The goal
is a second quantized flow contribution, not another unconstrained local
path count.

## Primary attack B: zero-height 28-type interface

Treat the 28 signed types as the preferred finite attack surface.

- For `d>0`, the first term is positive `>1/3`, the mandatory carry is
  `>1/2`, and therefore negative compensation `>1/3` is compulsory.
  Quantify the earliest possible negative return.
- For `d<0`, the first negative term already has magnitude `>1/3`; quantify
  the positive return needed to end at the small positive exact `F2`.

Prioritize the `v=37,J=23` pair, where
`|T_first|=2^37/3^24` is close to `1/2`.

## Primary attack C: positive-height branch

Use

`R-Q>3/2-2^-H-2^(-|d|-1)`

rather than only the uniform `3/4` floor.  Couple this height-sensitive loss
with any second transition found in A.  The `v=36` branch is entirely here.

## Avoid

- Do not rerun or merely enlarge the RL177 local automaton using the same
  rules; it is certified to leave every valuation and sign locally feasible.
- Do not infer that a locally feasible tuple extends to a physical cycle.
- Do not revive the old RL173 defect or use the RL175 sparse resultant as an
  independent gap obstruction.
- Do not silently import the external least-state minimum.
- Do not move to `h_p>=1` until this compensation/return attack is worked as
  far as productive.

## Success condition

Preferred: close one or both first-mismatch sign branches in `h_p=0`.

Strong partial success: prove an exact second-transition/return theorem that
materially narrows the 28 zero-height types or the `v=36/37` branches and is
not implied by the already-certified local automaton.
