# RL332 proof ledger — defect-stable pairwise phase contraction

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL332 CLOSEOUT
Incoming authoritative HEAD: `8869d3e9d38fb0d32db96b85aa5968f7252433e9`

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch at `(a,ell)=(217976794617,137528045312)`. RL331's exact physical ownership graph, true edge slack, arbitrary-support residue consumer, and incoming cap `1<=n<=32551214208` are retained. Gate A, Gate B, R1, `g=1`, and global positive non-trivial-cycle exclusion remain open. The external `2^71` least-state floor remains conditional.

## RL332.1 — exact normalized phase potential

For an automaton edge `(s,t,z,k)`, with RL331 potential `Phi` and true slack

`sigma = Phi(t)-Phi(s)-(2z-43k) >= 0`,

the physical rank coordinate advances by `Delta R=z+k`. Define

`Q(R,s)=2R-Phi(s)`.

Then identically

`Delta Q = 45k-sigma`.

Hence along every path `P`,

`Q_end-Q_start = 45K(P)-Sigma(P)`.

In particular zero-slack transitions do not arbitrarily reset the normalized phase. This is an exact algebraic identity on every edge of the conservative graph.

Classification: **proved exact graph identity**.

## RL332.2 — exact zero-slack recurrent geometry

Every recurrent low anchor is a state `N(z)` with `z<=21`, and `Phi=0` there. Therefore any two recurrent low anchors in one zero-slack block have actual rank difference divisible by 45.

The full zero-slack condensation was audited over all 26,514 edges. It still has 288 SCCs, 16 cyclic. There are exactly 195 zero-slack transitions between distinct cyclic SCCs. Each such transition leaves a recurrent low anchor, enters the complementary state of the destination cyclic SCC, and the transition plus the next internal edge advances exactly 45 physical ranks. There is no noncyclic-to-cyclic zero-slack entry and no recurrent-to-transient-to-recurrent return. A block that never becomes recurrent has at most three positive ranks; after the final recurrent SCC at most four positive ranks remain.

Combining these facts with true-slack charging gives, for total positive multiplicity `K`, total true slack `S`, and number `H` of recurrent low anchors,

`2H >= K-8S-5`.

Classification: **proved finite-state zero-slack splicing and sharpened anchor theorem**.

## RL332.3 — phase-uniform two-anchor theorem

Let

`alpha=(45a mod ell)/ell=44464540613/137528045312`.

Since `alpha<1/2`, for every phase `x in [0,1)`, direct split into the no-wrap and wrap cases proves

`2^x + 2^{ {x+alpha} } >= 1+2^alpha`.

A rational lower certificate obtained from a lower enclosure for `ln 2` and the first eight positive exponential-series terms proves

`c := 2^alpha-1 > 0.25120009946627`.

Delete positive-slack edges. There are at most `B<=S+1` zero-slack blocks. Pair consecutive recurrent anchors separately within each block. The pair count `P` satisfies

`P >= (H-B)/2 >= (K-10S-7)/4`.

Every unpaired positive rank retains unit weight, while every paired anchor pair gains at least `c` above its two-unit baseline. Hence

`W_struct >= K + c*(K-10S-7)/4`.

This bound has no Denjoy--Koksma discrepancy penalty and remains uniform in all starting phases and all allowed defect patterns.

Classification: **proved analytic phase-uniform pair theorem and support-weight lower bound**.

## RL332.4 — all-rho support-uniform contraction

At `rho=60`, write `K=K0+h`, with `K0=6112357564` and endpoint slack `s0=3`, so `S<=45h+3`. Intersecting the pairwise structural envelope with the inherited arbitrary-support envelope has its exact integer minimum at

`h=10239722`.

Thus the weighted loss improves by at least `10239722`, and the enhanced telescope gives

`n < 32550361321.43585...`.

For `rho=61..199`, exact rational evaluation using each actual rounded density floor and endpoint slack stays below bootstrap `32550361322`; the minimum certified gain over that finite interval is `10239721`.

For `rho=200..3606999`, monotonicity of structural-minus-residue in `Kbase` and worst endpoint slack `44` give a uniform certified gain `>=10239542`. At `rho=200` even this worst-case gain gives `32550361303.1871... < 32550361322`, and inherited monotonicity covers the remainder of the bridge.

At `rho=3607000`, a directed-rounding 80-digit ordinary-consumer evaluation gives the rigorous upper bound

`32550361123.514934403130650090851253575529046655733284226974114149230715060826564`,

already below bootstrap; inherited monotonicity covers all larger rho. The companion inequality covers `rho<=59`.

Therefore every rho is covered.

Classification: **proved all-rho support-uniform consumer contraction**.

## RL332.5 — lower-bootstrap physical self-consistency

The complete physical ownership reconstruction was rerun at bootstrap

`H=32550361322`.

It reproduces exactly:

- total-44 rows: `13556`, physical links: `14`;
- large-singleton rows: `7188`, with totals `{45:4759,46:1634,47:556,48:173,49:46,50:14,51:6}`, physical links: `14`;
- large-to-total44 / total44-to-large physical links: `7 / 6`;
- owned singleton DAG: `274` nodes, `21` edges, longest path one edge;
- exact short supports: `282 / 166`;
- two-positive counts: `{45:2030,46:707,47:270,48:93,49:34,50:11,51:2}`;
- conservative graph: `323` states, `26514` edges;
- potential relaxation: two iterations, range `0..53`, boundary `129`;
- density theorem: `2Z<=43K+129`.

Lowering the bootstrap can only add physical realizations, so equality of these complete reconstructed layers certifies that no load-bearing ownership set changed.

Hence the self-consistent authoritative carry cap is

`1<=n<=32550361321`.

Classification: **proved exact finite reconstruction and self-consistent contraction**.

## Verification and remaining obstruction

Portable verifier: `verification/verify_rl332_pairwise_anchor_contraction.py`.

Lower-bootstrap reconstruction: `verification/verify_rl332_self_consistent_ownership.py`.

Independent red team: `verification/red_team_rl332_pairwise_anchor_contraction.py`.

All are GREEN in the frozen closeout candidate.

The pairwise theorem is deliberately phase-uniform and avoids discrepancy accumulation. It is still only a quantitative contraction. A stronger finite-block theorem (`m>2`) or genuine physical all-length descent may increase the gain materially, but R1 remains open until the parent branch itself is closed.

`PARENT_DIFFICULTY_DELTA = EASIER`.
