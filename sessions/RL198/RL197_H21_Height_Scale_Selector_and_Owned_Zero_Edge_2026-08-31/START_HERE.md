# START HERE — authoritative RL197 handover

Current handover: **RL197 — H21 Height-Scale Selector and Owned p-Shift Zero-Edge Interface**.  
Incoming job: **RL198**.

RL197 reduces the desired second owned p-shift zero-edge bridge to one H21 bit:
the common height at the `{33,34,35}` co-owner's `tau=34` start.

Every surviving H21 co-owner has predecessor/start mechanics `1|212`.
Its three shallow common heights have exactly six possibilities:
`000,010,011,100,110,111`.

Exactly `000` and `100` supply the canonical H21-owned p-shift-compatible zero edge at the
middle source. Equivalently the bridge is present iff the `tau=34` common height is zero.

The inherited H21 normalized gaps and predecessor mod-3 condition are exactly height-scale blind
and cannot decide that bit. No H21 budget release or branch/global closure is claimed.

Read the RL197 report, certified-facts ledger, correction/demotion ledger, red-team report and
`proofs/RL197_H21_HEIGHT_SCALE_SELECTOR.md`.
Run `sh verification/run_fast_rl197_verifiers.sh`.

Next target: `RL198_H21_GLOBAL_HEIGHT_SCALE_SELECTOR_TARGET.md`.
