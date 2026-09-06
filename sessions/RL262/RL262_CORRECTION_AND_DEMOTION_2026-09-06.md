# RL262 correction / demotion ledger

Date: 2026-09-06

## Promoted incoming mathematics

No RL261 or earlier promoted theorem is corrected or demoted.

## RL262 scratch correction during closeout

During the live RL262 session, an unpromoted global-lead summary stated the simplified ordered-defect congruence as

`Dcal == 3^rho*(9*N+61)/4 (mod 2^m)`.

That statement is two dyadic powers too strong. Dividing the RL65 equality by 12 cannot preserve modulus `2^m`.

Closeout re-derived the exact identity. With `m=a-k-1` and odd `k`, one has `N==19 (mod24)` and

`Dcal = 3^rho*(9*N+61)/4 - 2^(m-2) * (4+(N-2)*2^(k+1))/3`.

Therefore the correct uniform congruence is only

`Dcal == 3^rho*(9*N+61)/4 (mod 2^(m-2))`.

The stronger scratch version was never authoritative or committed, so no theorem is demoted.

## Effect on the fourth-selector certificate

None. The RL262 exact finite verifier uses the full exact RL65 defect value for each `(k,prefix,N)` class and never substitutes the overstrong scratch congruence. All 2,232 classes still die exactly with maximum death depth 988.

## Unpromoted route lead

Long-lived ordered extensions observed during RL262 suggest eventual low-density / alternating canonical corridors. This is retained only as a successor research lead. RL262 promotes no uniform alternation theorem, density theorem, Gate closure, or global cycle exclusion.
