# RL253 closeout report — beta=6 eliminated

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**

RL253 eliminates the entire Branch-C `beta(P)=6` regime.

The load-bearing theorem is the exact 38-window identity
`Z_38 = 14 + sum P`.
For beta=6, distinct sampled q-orbit sites have P-sum at most total positive P-mass 8, so every 38-window has at most 22 zeros. The canonical terminal `0^28` plus prefix `110` forces a 38-window with at least 29 zeros. Contradiction.

Therefore the RL252 first-frontier contraction `(783,494,289,317,200), 31<=k<=53` is subsumed: no beta=6 Branch-C object survives at that or any later arithmetic scale under the inherited corridor.

Proof-state:
- beta=6 Branch C: eliminated;
- Gate A: open;
- Gate B: open;
- Radius 4: not invoked;
- Radius 5: inactive;
- global Collatz-cycle exclusion: not claimed.

Successor RL254 should audit/generalise the 38-window identity beyond beta=6. The live-session estimate `beta(P)>=118` is retained only as a candidate lead until general-beta P-mass bookkeeping and multi-window q-orbit disjointness are independently proved.

Knowledge catalogues: stale/deferred.
