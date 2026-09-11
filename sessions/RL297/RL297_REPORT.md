# RL297 — P-bottleneck risk-first Gate-A audit report

Date: 2026-09-11

## Classification

`P_BOTTLENECK_RISK_AUDIT_WEAK_GREEN_SHARED_ENDPOINT_STRUCTURE_IDENTIFIED`

This is an audit result, **not** a proof of `Bcal(P)<=1`, Gate A, or global non-trivial-cycle exclusion.

Gate A remains open with inherited residual

`k>=31`, `k` odd, `H_can<k`.

The fifth selector / branch programme remains unscanned and was not worked in RL297.

## Audit question

RL297 was instructed to attack

`Bcal(P)<=1`, `P=(2,3)`

adversarially, first seeking an exact legal future of Bellman score at least 2.

No such witness was found in the exact finite audit performed.

## Exact finite P-cone audit

Using the authoritative canonical recurrence, the positive P cone was exhaustively scanned through added area 27.

Reproduced counts:

- positive physical states: `23,652,724`;
- positive even checkpoints through area 23: `320,762`;
- through area 26: `2,865,881`;
- through area 27: `5,962,876`.

For every positive even `d=1` checkpoint reached through area 27, the Bellman endpoint score

`nu_2(J)-A`

was evaluated.

Result:

- maximum score: `1`;
- unique score-1 endpoint: `J=8` at added area `A=2`, with `nu_2(8)=3`;
- no score-0 endpoint;
- no score >=2 endpoint.

The unique tight witness is the exact P word `1111`:

`(2,3) -> (2,6) -> (1,3) -> (1,5) -> (1,8)`

with total added area `2`, hence score `3-2=1`.

This is an exact finite certificate only. Bounded search failure is not an all-depth theorem.

## P versus checkpoint 8 shortest-path evidence

Let `m_P(E)` and `m_8(E)` denote minimum added-area cost to a positive even checkpoint `E` from P and checkpoint 8 respectively.

Exact comparison found:

- through P-cost 15 / 8-cost 13: all 1,088 common non-2 checkpoints satisfy `m_P(E)=m_8(E)+2`;
- through P-cost 20 / 8-cost 18: all 36,207 common non-2 checkpoints satisfy `m_P(E)=m_8(E)+2`;
- the sole exceptional checkpoint is `E=2`, where P has the cheaper direct history.

No all-depth proof of this identity was obtained in RL297.

If the universal checkpoint identity

`m_P(E)=m_8(E)+2` for every positive even `E != 2`

is proved, then endpoint minimisation gives the exact reduction

`Bcal(P)=Bcal(8)-2`,

so `Bcal(P)<=1` becomes exactly `Bcal(8)<=3`.

For nonempty futures from checkpoint 8 this is the inherited excess-one inequality

`nu_2(J_end)<=A+1`.

RL293 already proved the checkpoint-8 low-area version through `A<=7`, with equality rigidity.

## Structural mechanism isolated

In RL294 dual coordinates, P has interval

`[T,N]=[-2,7]`

while checkpoint 8 has interval

`[7,10]`.

Thus

`N(P)=T(8)=7`.

This shared endpoint is a concrete algebraic mechanism behind the observed P/8 checkpoint-distance relation and is the main structural lead left by the audit.

A direct finite physical-state ownership attempt does **not** yield a global statewise theorem: there are non-checkpoint interior exceptions even while the checkpoint-minimum relation persists. Therefore any future proof should target checkpoint-ending paths / shared-endpoint transport, not blanket physical-state ownership.

## Additional shared-endpoint scratch lead

A complementary paired-state rewrite was isolated while probing the same mechanism. For odd departure depths in the tested family, a source `L_D` continuation `101100` and the preceding tight owner state `R_{D-2}` continuation `000001` merge to the same physical state, with the owner continuation two area units cheaper.

The associated dual intervals share the endpoint

`q_D=(3^D+1)/4`,

with

`R_{D-2}=[q_D-3^(D-2),q_D]`,

`L_D=[q_D,q_D+3^D]`.

A normalized paired-coordinate description `(delta,r)` also emerged, suggesting a finite shared-endpoint transducer. In particular, for an owner `m` levels below a source while sharing the source left endpoint,

`(delta,r)=(-m,-1)`,

pairing source `0` with owner `1` preserves the shared endpoint and sends

`(-m,-1)->(-(m+1),-1)`.

These observations are deliberately frozen as **scratch structural leads**, not promoted as the missing all-depth theorem in this closeout.

## Red-team outcome

The audit did not find evidence that turns the current Gate-A route red.

Equally, it did not upgrade weak-green to proved/strong-green because:

1. the P scan is bounded;
2. the P/8 shortest-path identity remains unproved all-depth;
3. the checkpoint-8 excess-one theorem remains unproved all-depth;
4. remaining non-P front-door engineering is still not fully closed and was only provisionally bypassed for RL297 prioritisation.

Therefore the correct status is **weak green**: the presumed final bottleneck survived a serious finite and structural attack, with a plausible exact mechanism identified, but the theorem remains open.

## Scope discipline

No fifth-selector mathematics was performed in RL297. Historical authority was only recovered far enough to identify the frozen continuation point: RL258 removed the first selector, RL260 the second, RL261 the third, and RL262 the fourth; RL262 then deliberately pivoted before scanning the fifth selector.

Per user direction, RL297 closes here as an audit session. The next session returns to that selector/branch programme unless later evidence turns the Gate-A weak-green assessment red.
