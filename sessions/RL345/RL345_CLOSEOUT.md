# RL345 closeout

Date: 2026-09-17
Status: CLOSED/FROZEN
Successor: RL346

RL345 produced two theorem-sized Phase-4 contractions without closing R1:

- source uniqueness improves from 24 gaps to 23 by combining RL344's `<2^37` window with odd parity, giving modulus `2*3^23`;
- endpoint uniqueness improves from 75 gaps to 72. Every low-modulus 72-gap exception was exhaustively eliminated: 67,070 words, 135,356 band endpoints, all descending below `2^71`, independently reproduced with maximum depth 446 and digest `2259e37604ca3de00ed18049f2423ff72fc66d63822fe4b597942c8fc2dbe18d`.

The live frontier is the exact decorated 23/72 singleton interface. Phase 4 remains open because predecessor/successor CRT, exact ownership, row-contact/wrap and deterministic descent have not yet been intersected for every singleton. Phase 5 remains scratch-only. Phase 6 remains conditional. R1 remains OPEN.
