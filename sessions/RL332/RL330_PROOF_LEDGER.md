# RL330 proof ledger — exact total-44 ownership and coefficient-43/2 contraction

Date: 2026-09-15
Status: FROZEN CANDIDATE FOR RL330 CLOSEOUT
Incoming authoritative HEAD: `ed74f86795c59228e89548ec19296e4914b45210`

## Scope retained

Work remains in the ordered genuine `g=2`, `Z0>0`, `K<0` late-row parent branch at `(a,ell)=(217976794617,137528045312)`, `d=80448749305`, and `lambda=2^a/3^ell<1+2^-40`, with incoming carry cap `1<=n<=32562630353`.

The external `2^71` least-state floor remains conditional. RL324's local-propagation barrier remains binding. Gate A, Gate B, R1, and global positive non-trivial-cycle exclusion remain open.

## RL330.1 — exact total-44 singleton ownership

Assume for contradiction `n>=32551214632`. Exhaust every singleton excursion `0,1,0` whose adjacent zero total is exactly 44, all 43 ordered zero pairs, all 45 rational-mechanical factors of length 44, and every odd endpoint lift in `2^71 <= P < 2^76+2^36`. Retain only reconstructions satisfying the displayed carry threshold through the exact upper enclosure for `a log 2-ell log 3`.

Exactly 13,556 physical realizations survive, covering all 43 ordered pairs.

Classification: **exact gap-free finite ownership certificate at the self-consistent RL330 threshold**.

## RL330.2 — exact shared-state linkage and owned singleton DAG

Consecutive singleton bridges are linked only when the first state on their shared zero plateau is exactly equal. Deterministic ordinary dynamics then fixes that plateau.

Inside the total-44 layer, exactly 14 physical links survive. Their pair projection is `(1,43)->(43,1)` (12 physical links) and `(2,42)->(42,2)` (2 physical links). There is no self-link and no reverse link. In particular neither conservative RL329 obstruction `N(22)->N(22)` nor `N(21)<->N(23)` has a genuine high-carry realization.

At the same threshold, the retained total-45--51 singleton layer has 7,188 realizations in 231 pair types and 14 physical large-to-large links / 13 pair links. Exact cross-linking gives 7 large-to-total-44 physical links and 6 total-44-to-large physical links.

The combined 274-state pair projection of every owned singleton type with adjacent zero total at least 44 has 21 exact-support edges. Its source and target sets are disjoint, so it is acyclic and every directed path has at most one edge.

Classification: **exact physical shared-state ownership certificate and proved finite-state acyclicity theorem over the retained singleton layer**.

## RL330.3 — exact owned-successor reconstruction

For each owned total-44 realization, take its exact right-plateau state and reconstruct every candidate following singleton with adjacent zero total at most 43 from that same state. Only 166 conservative pair transitions survive. The same threshold-sensitive reconstruction for the retained large layer leaves 282 large-to-short pair transitions with adjacent zero total at most 43.

Thus no transition leaving an owned singleton state is admitted through an unowned pair-type reset. Pair projection is used only after physical equality has certified each supported transition, so it can add paths but cannot remove any genuine trajectory.

Classification: **exact physical successor-ownership theorem**.

## RL330.4 — threshold-sensitive two-positive layer

The complete two-positive reconstruction at the same bootstrap threshold has multiplicities `45:2030, 46:707, 47:270, 48:93, 49:34, 50:11, 51:2`, and no survivor above adjacent zero total 51.

Classification: **exact gap-free finite certificate**.

## RL330.5 — conservative density automaton

Build states `N(z)`, `1<=z<=49`, after an unowned short singleton or any positive run of length at least two; `L(a,b)` for each of the 231 owned singleton pair types of total 45--51; and `T(a,b)` for each of the 43 total-44 pair types.

From `N`, retain all short singleton transitions of total at most 43, every owned total-44 or large singleton entry, the exact two-positive layer, and every positive run of length at least three. From `L` or `T`, retain singleton transitions only when certified by exact physical successor reconstruction/linkage, plus the exact two-positive layer and every run of length at least three. This is a conservative superset of every genuine trajectory in scope.

The graph has 323 states and 26,514 edges. An integer potential with range 0--53 is checked on every edge and proves

`2Z <= 43K + 129`.

The coefficient `43/2` is sharp for this conservative graph because the remaining unowned short layer contains the total-43 cycle `N(21)<->N(22)`. This is a graph obstruction, not a claimed physical trajectory.

Classification: **proved finite-state support-uniform density theorem backed by exact physical ownership**.

## RL330.6 — residue-weighted telescope and self-consistent carry contraction

At `rho=60`, with `T=ell-rho`, the density theorem gives `K>=6112357564`. The inherited RL327 residue-weighted telescope, with the same exact rational logarithmic and quartic enclosures, gives `n < 32551214631.602516...`.

This contradicts the bootstrap assumption `n>=32551214632`, hence

`n<=32551214631`.

The inherited `rho<=59` inequality remains far below this threshold. For `rho>=60`, increasing `rho` decreases the rounded density floor by at most one; the largest possible restored one-rank loss is strictly smaller than the newly omitted ideal term. Therefore the bound covers every live `rho`.

The authoritative carry cap improves by exactly `11415722`.

Classification: **proved self-consistent all-rho carry contraction from exact ownership plus the inherited exact residue-weighted telescope**.

## Verification

Portable verifier: `verification/verify_rl330_total44_ownership_density.py`.

Independent reconstruction/red team: `verification/red_team_rl330_total44_ownership_density.py`.

Both independently reconstruct the threshold-sensitive singleton and two-positive layers, exact physical links, owned-successor supports, graph size, every potential inequality, all-rho arithmetic, and the final cap.

## Binding obstruction and final scope

The coefficient-22 total-44 reset is closed. The new conservative sharp obstruction is the unowned total-43 short-singleton reset, represented by `N(21)<->N(22)`. This does not authorize a blind threshold catalogue. A successor should seek all-length physical identity, phase/residue coupling, owned-state drift, or a stronger nonlinear consumer.

R1 Parent Bridge: OPEN. Gate A: OPEN. Gate B: OPEN. `g=1`: separate. Global positive non-trivial-cycle exclusion: OPEN.

`PARENT_DIFFICULTY_DELTA = EASIER`.
