# RL-4 Roadmap Update — 2026-08-19

## Rank 1 — iterate the k=0 plateau/exit grammar

RL-L28 already compresses every exponent-1 plateau exactly: `n=v2(y+1)+v3(y+1)` and the xi level stay fixed across the run, and one exit parameter `t=v2(3^n q-1)` determines the next state. RL-L29 says the low root exit must eventually be balanced by a high/deep xi-descent.

Primary target: quantify the cost/frequency of **deep exits** `t>=n` and **regular-high exits** `2^(n+t-r)>3^(n-r)`. Fuse that density with the common denominator and rotation constraints. RL-L30 shows that merely summing plateau xi ratios reproduces the existing scalar cycle-product slope exactly, so do not count that scalar telescoping as new progress. The desired endpoint is a recurrent grammar with no periodic word, or a finite exceptional family with an extension theorem.

Split off the boundary `s=L` one-plateau equation `(2^(s+t)-3^s)q=2^t-1`; either close it directly or keep it as an explicit exceptional state.

Do not deepen the root-only xi sieve; RL-G7 already rules that out.

## Rank 2 — k>0 first-crossing automaton without a continuous ratio state

For the tail-larger entry orientation:

- initialize cumulative exponent difference at `+2m`;
- require it to be `<=0` by the first down-crossing (RL-L23);
- require the phase/slack threshold in RL-L25;
- retain RL-L22 plus the length-sensitive one-density debt in RL-L24.

Next target: determine whether a second crossing can be ruled out, or whether every additional crossing consumes a monotone slack/variation budget.

## Rank 3 — tail-smaller orientation

If the tail starts below the cycle and never up-crosses, seek a direct endpoint inequality at `x_k=R#<y_k` using the relative product identity.

If it does up-cross, RL-L23 forces cumulative tail exponent catch-up at that first up-cross; any later return below then forces a second sign change in cumulative exponent order. Search for a bounded-variation theorem on these sign changes.

## Rank 4 — cycle product with exact xi levels

RL-L26 upgrades the scalar xi barrier to a strict off-spine gap. Use

`c_j+1 >= (3/2)^(m_j) * xi(c_j)`

with `xi(c_j)=R#+1` only on the neutral spine and `xi(c_j)>=R#+3` elsewhere.

Fuse the resulting cycle-wide height profile with `2^A=prod(3+1/c_j)` and the plateau/exit grammar. The goal is a density theorem, not another isolated local exclusion.
