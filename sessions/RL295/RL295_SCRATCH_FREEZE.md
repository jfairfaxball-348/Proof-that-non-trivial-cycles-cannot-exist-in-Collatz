# RL295 scratch freeze

Date: 2026-09-11

This file preserves useful RL295 work that is **not part of the promoted theorem set unless explicitly repeated in RL295_REPORT.md**.

## 1. Finite reductions found during the session but not fully certificate-frozen

The session obtained the following exact-looking Bellman reductions by finite owner search and same-state splicing. The search results were repeatedly replayed in-session, but not every individual owner word was retained before closeout. Therefore these are successor leads, not authority.

### From `(5,191)`

The unique `(4,39)` residual is `(5,191)` after source cost 6.

A distinguished finite preperiod produced:

`(5,201)` at +4,
`(4,151)` at +8,
`(6,733)` at +13,
`(6,949)` at +18,
`(6,1273)` at +23.

The session reduced the branch to three principal residuals

`(5,201)`, `(6,733)`, `(6,949)`

with target allowances relative to P:

`Bcal(5,201) <= Bcal(P)+12`

`Bcal(6,733) <= Bcal(P)+21`

`Bcal(6,949) <= Bcal(P)+26`.

These inequalities are NOT promoted here.

### From `(5,201)`

A finite cut left the early states

`(5,206)`, `(5,264)`, `(5,351)`

as the unresolved sectors in the session search.

### From `(6,733)`

A finite cut left

`(6,699)`, `(6,898)`.

### From `(6,949)`

A finite cut left

`(6,807)`.

Combining the in-session search claims gave the candidate frontier

`Bcal(4,39) <= max(`
` Bcal(P)+2,`
` Bcal(5,206)-14,`
` Bcal(5,264)-18,`
` Bcal(5,351)-22,`
` Bcal(6,699)-24,`
` Bcal(6,898)-29,`
` Bcal(6,807)-29 )`.

This frontier is a high-priority RL296 reconstruction target. Do not use it as authority until the missing owner witnesses are frozen.

## 2. Exact coefficient spine observed from `(5,191)`

The tower coefficient recurrence was identified exactly.

For a state `K=q*3^d`, the unique external bit preserving tower form is:

- q even: `x=1`, q -> 3q/2;
- q odd: `x=0`, q -> (q+1)/2 while depth increases by one.

The frozen coefficient pattern was therefore structural:

`4 -> 6 -> 9 -> 5 -> 3 -> 2 -> 3 -> 2 -> ...`.

This helped discover the Q-tower splice but is not needed in the final promoted proof.

## 3. Repunit E_d family and wall/P normal form

Define

`E_d=(d-1, K=(3^(d+1)-1)/2)`.

Direct canonical algebra gives:

`E_d --0--> W_2 o P^floor(d/2)`

`E_d --1--> W_6 o P^floor((d-1)/2)`.

For

`C_m^(u)=W_u o P^m`

one has

`C_m^(u)=(2m, K=((4u+3)9^m-3)/4)`.

This was the route that exposed two dyadic boundary ladders.

## 4. Dyadic boundary ladders

For `a=4u-1`, with `u in {2,6}`, define

`O_D^(a)=(1, J=a*2^(D-1)+1)`

and complementary checkpoint

`B_D^(a)=(1, J=3a*2^(D-2)+2)`.

A zero-cost boundary exit from O gives B. From B a pure-zero lift reaches the corresponding wall/P cascade. In T-coordinates the lift was derived explicitly and has historical cost

`(D^2-D-2)/2`.

Base searches found very cheap P entries to several ladder states, including the a=7 O17 state ultimately used in the Q17 certificate.

A hoped-for universal short raw-word `D -> D+2` macro did not emerge. Raw boundary words are gauge-heavy and should not be the successor's principal representation.

## 5. Superseded constant-gap analysis

Before the Q17 base certificate was found, an explicit P construction for one tail family missed the needed owner allowance by a constant four units, and a later Q-tower construction exposed a constant 42-unit deficit.

These were not genuine obstructions. The cheap P -> Q17 certificate removes them with 17 units of margin against the `(6,807)` credit.

Do not restart by optimizing the obsolete 4-unit or 42-unit paths unless the Q17 certificate is invalidated.

## 6. Failed / nonprincipal routes

- Bounded P-owner cones cannot certify an all-depth future by themselves.
- Raw long boundary words are dominated by zero-height gauge freedom.
- A fixed recent suffix cannot control arbitrary boundary phase (inherited RL289 barrier).
- Residue-only scalar corrections to cascade debt remain impossible (RL294).
- The cascade cross-term alone does not pay rejected-tube depth.
- No Gate-B, fifth-selector, Radius-6+, or generic Collatz-termination route was used.

## 7. Recommended reconstruction order for RL296

1. Re-run `verify_rl295_wall_owner.py`.
2. Accept the promoted `(4,39)->(5,191)` unique-residual cut and Q17 all-depth tail splice.
3. Reconstruct the candidate finite `(5,191)` frontier above one residual at a time.
4. Every owner claim must carry an explicit replayable word or a parametric analytic formula.
5. Close `(6,807)` first if the candidate `(6,949)->(6,807)` reduction is reproduced, because its post-Q17 future is already solved.
6. Once `(4,39)` closes, move to `(2,-17)`, `(2,-84)`, `(3,-28)`.
7. Only after all non-P front-door states close should `Bcal(P)<=1` become the primary target.
