# RL95 correction and demotion ledger

Date: 2026-08-25

## 1. Ultra safe-depth floor update

RL94 froze the ultra tier

`d<=15,000,038`, `r<=335,000` => successor `<=15,000,053`

using the then-global bit-length minimum

`15,000,040 at r=2,900`.

RL95 extended the exact ultra scan gap-free through

`r=605,000`

and found a new global minimum

`15,000,037 at r=575,974`.

By the inherited minimal-reset interface `D=B-2`, the correct safe depth for the full RL95 ultra radius is therefore

`D_u=15,000,035`.

This does **not** invalidate the frozen RL94 theorem on its original radius domain. It updates the full-radius tier after new exact data.

Any provisional RL95 checkpoint that still used `D_u=15,000,038` beyond the discovery point was not promoted as a final theorem. The final RL95 geometry, support audit, top-stratum theorem, and interval exclusion all use the corrected `D_u=15,000,035`.

## 2. Conservative common successor charge

The RL93 correction remains authoritative:

whenever the ultra tier is load-bearing, use

`L_common=15,000,053`

unless a rigorous stronger mixed-charge theorem is proved.

The RL95 ultra floor event changes safe depth, not the modulus-derived ultra successor ceiling, so `L_common=15,000,053` remains load-bearing.

## 3. Support-line inheritance

No support edge was inherited blindly.

After the corrected ultra depth and final radii were fixed, RL95 re-enumerated the exact feasible supporting edges. The final feasible pairs are

`A-C`, `C-D`, `D-E`.

`A-C` is exact-terminal-direction optimal throughout the promoted interval and at the first failure.

## 4. Incomplete post-605k scans

Attempts to extend the ultra frontier beyond `r=605,000` hit execution-time limits before producing complete scan outputs.

Those incomplete attempts are excluded from the proof state and are not represented in the raw certificate directory.

No claim is made beyond the final certified ultra radius `R_u=605,000`.
