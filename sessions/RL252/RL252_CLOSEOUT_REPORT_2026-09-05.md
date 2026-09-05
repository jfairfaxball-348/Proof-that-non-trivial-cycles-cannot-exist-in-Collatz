# RL252 closeout report

Date: 2026-09-05
Incoming RL: RL252
Successor: RL253

## Classification

**R4_BRIDGE_REDUCED**

## Promoted RL252 result

At the first RL250 unexcluded scale
`(a,ell,z,q,r)=(783,494,289,317,200)`, RL252 turns the inherited
zero-run propagation lemma into an exact iterated endpoint statement and
combines its fifth iterate with the existing terminal-window packing
resource.

For a zero block `[s,s+L-1]` with `L>=10`, the forced q-shifted block is
exactly `[s+q+8,s+q+L-2]`, length `L-9`.

Starting from the terminal run `B_0=[783-t,782]` and iterating five
times gives, for `t>=46`,

`B_5=[59-t,13]`, length `t-45`.

For `t>=51`, this block, the fixed prefix zero at index 2, and the
terminal run fit inside a 149-site cyclic gap. The complementary two
317-windows each contain at least 116 zeros, forcing

`289 >= 232 + t + 1 + (t-45) = 2t+188`,

which is impossible for `t>=51`.

Therefore the first-frontier canonical selector contracts from
`31<=k<=59` to **`31<=k<=53`**. Equivalently `t<=50`; and
`m=291-k>=238`.

The exact packing mechanism is threshold-sharp at this boundary:
`t=50` gives the lower count 288, while `t=51` gives 290.

## Proof-state boundary

No Gate is closed. Radius 4 is not invoked. Radius 5 is inactive. No
non-trivial-cycle exclusion is claimed. No correction or demotion is
added in RL252. All RL249/RL250 demotions remain binding, and RL251's
Gabriel's-horn route remains frozen as equivalent to existing work.

## Successor

RL253 is prepared, not started. It continues the exact Branch-C
`beta(P)=6` event-versus-rigid terminal-ownership attack from

`(783,494,289,317,200), 31<=k<=53, m>=238`,

with the RL252 iterated zero-run packing contraction frozen.

Knowledge catalogues are stale/deferred under connector closeout policy.
