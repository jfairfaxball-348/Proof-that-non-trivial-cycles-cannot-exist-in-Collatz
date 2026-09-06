# RL263 — correction to the RL262 modulus classification

Date: 2026-09-06
Classification: **CORRECTION OF PRIOR CLOSEOUT INTERPRETATION**

RL262 correctly promoted the exact identity

`Dcal = C - 2^(m-2) T`

with

`C=3^rho*(9N+61)/4`,
`T=(4+(N-2)*2^(k+1))/3`.

RL262's correction ledger then described the congruence modulo `2^m` as two powers too strong and retained only modulo `2^(m-2)`.

In the actual promoted scope, however, `k` is odd and `N==19 (mod24)`. Factor

`T = 4 * G`

where

`G=(1+(N-2)*2^(k-1))/3`.

The quotient `G` is an integer: modulo 3, `N-2==2` and odd `k` gives `2^(k-1)==1`, so the numerator is `0 mod3`.

Therefore the exact identity sharpens to

`boxed: Dcal = C - 2^m G`

and hence

`boxed: Dcal == C (mod 2^m)`.

So the earlier scratch modulus `2^m` was not false in the inherited odd-`k` full-phase scope; the RL262 closeout explanation overlooked the forced factor four in `T`.

This correction does **not** alter the RL262 fourth-selector elimination certificate. That certificate always used the exact value of `Dcal`, and its 2,232 classes still die exactly.

The correction also does not rescue the RL263 global-density route: RL263's physical-gap theorem proves the full prefix congruence is automatic on genuine physical full-phase pairs.
