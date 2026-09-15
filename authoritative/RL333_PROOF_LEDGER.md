# RL333 proof ledger — defect-stable low-slack anchor contraction

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL333 CLOSEOUT
Incoming authoritative HEAD: `6536ce65c343f7e063869fc0cbf4a2935c0153d8`

## Scope
Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` parent branch at `(a,ell)=(217976794617,137528045312)`. RL332's exact ownership graph, density theorem `2Z<=43K+129`, normalized phase identity, residue consumer and all-rho architecture are retained. Gate A, Gate B, R1, `g=1`, and global positive non-trivial-cycle exclusion remain open. The external `2^71` least-state floor remains conditional.

## RL333.1 — finite-block phase amplification
For `alpha=(45a mod ell)/ell=44464540613/137528045312`, exact rational evaluation for blocks through length 8 proves the all-length theorem: with `c=0.25120009946627`, every nonempty zero-slack recurrent block containing `h` recurrent low anchors has phase excess at least `c(h-1)`. Classification: **proved analytic theorem with exact finite certificate**.

## RL333.2 — low-slack first-return geometry
Exact audit of the unchanged 323-state / 26514-edge graph proves that retaining all edges with `sigma<=2` gives 614 edges, 269 SCCs, exactly one cyclic SCC of size 55 containing all 21 recurrent low anchors; deleting the low anchors leaves an acyclic graph. Every recurrent first return is exactly one of `(0,2,45)`, `(1,1,22)`, `(2,2,44)` in `(sigma,K,Delta R)`. Classification: **proved exact finite-state geometry**.

## RL333.3 — defect-stable anchor theorem
An exact integer potential on the `sigma<=2` graph has range `0..4` and proves `K_good<=2H_good+4`. Every edge with `sigma>=3` satisfies `4k+16<=7sigma`, with equality on exactly nine edges, all `(sigma,k)=(4,3)`. Therefore

`2H >= K - (7/4)S - 4`.

This strictly supersedes RL332's `2H>=K-8S-5` in the live consumer. Classification: **proved exact finite-state theorem**.

## RL333.4 — support-uniform phase envelope
The all-length block theorem and the new anchor theorem give

`W_struct >= K + (c/2)K - (15c/8)S - 3c`.

Classification: **proved support-uniform analytic envelope**.

## RL333.5 — all-rho contraction
At `rho=60`, exact structural/residue intersection gives weighted loss `31922482`, hence `n<32548554424.769184...` and `n<=32548554424`. Exact evaluation covers `rho=61..845`. From `rho=846`, monotonicity plus worst endpoint slack gives gain at least `31920245` to the ordinary-consumer handoff. At `rho=11242132`, directed rounding gives `32548554424.69233845469604681476649494444... < 32548554425`; inherited monotonicity then applies. The companion inequality covers `rho<=59`. Classification: **proved all-rho contraction**.

## RL333.6 — lower-bootstrap self-consistency
At bootstrap `H=32548554425`, three new physical realizations enter relative to RL332: two total-44 rows, pairs `(4,40)` and `(5,39)`, and one total-45 row, pair `(5,40)`. Thus total-44 rows become `13558` and large-singleton rows `7189`.

All load-bearing projections remain unchanged: 14 total-44 links, 14 large links, 7/6 cross-links, short supports 282/166, two-positive counts `{45:2030,46:707,47:270,48:93,49:34,50:11,51:2}`, conservative graph 323/26514, potential range `0..53`, boundary 129, and `2Z<=43K+129`. Classification: **proved exact finite reconstruction**.

## Final RL333 result
Authoritative carry cap: `1<=n<=32548554424`, improving RL332 by `1806897`.

R1 remains OPEN. The exact next bottleneck is the high-defect charge, especially the nine slack-4 / `k=3` equality edges. `PARENT_DIFFICULTY_DELTA = EASIER`.
