# RL262 — corrected universal ordered-phase reduction

Date: 2026-09-06
Classification: **ANALYTIC THEOREM / GLOBAL REDUCTION**
Scope: every full-phase-extendable datum in the inherited odd-terminal branch to which the promoted RL65 quotient theorem applies.

## Exact reduction

Use the RL65 notation

- `rho=ell-3`;
- `m=a-k-1`;
- `M=2^a-3^ell`;
- ordered rank defect `Dcal>=0`;
- positive phase quotient `N`, with `N == 3 (mod 8)`.

RL65 gives

`(N-2)M = 237*3^rho - 12*Dcal - 2^(a-k+1)`.

Since `ell=rho+3` and `a=m+k+1`, exact rearrangement gives

`12*Dcal = 3^(rho+1)*(9*N+61) - 2^(m+2) - (N-2)*2^a`.

For odd `k`, divisibility of the right-hand side by 3 forces

`N == 1 (mod 3)`.

Together with `N == 3 (mod 8)`, therefore

`boxed: N == 19 (mod 24)`.

Define

`C = 3^rho*(9*N+61)/4`,

`T = (4 + (N-2)*2^(k+1))/3`.

Both are integers under the preceding congruences. Then the exact identity is

`boxed: Dcal = C - 2^(m-2)*T`.

Consequently

`boxed: Dcal == C (mod 2^(m-2))`.

This is a selector-independent dyadic ordered-prefix condition: through depth `m-2`, the required rank defect is determined by `(rho,N)` alone. The last two dyadic bits are carried by the explicit integer `T`, which retains the terminal exponent `k`.

## Importance

The selector eliminations RL261 and RL262 both succeed by repeatedly enforcing ordered canonical-prefix congruences against the exact full-phase defect. The identity above isolates the part of that mechanism which is genuinely global rather than selector-specific.

It identifies a precise successor problem: control the canonical ordered extension satisfying this universal dyadic target strongly enough to show that it cannot attain the required common weight `rho` at internal length `m` throughout the surviving resonance regime.

No such uniform contradiction is proved in RL262.
