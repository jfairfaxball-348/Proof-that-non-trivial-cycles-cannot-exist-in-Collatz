# RL178 certified facts and proof ledger

## New proved analytic mathematics

- **RL178.1:** if `k=J+1` and `w=g_p/2^v` is odd, the first mismatch obeys the exact signed pair relation
  - `d>0`: `2^d y_(p+k)-y_k=3^k w`;
  - `d<0`: `y_(p+k)-2^|d| y_k=3^k w`.
  For every carry-free continuation, the next sign/return is constrained by the exact 2-adic comparison law of Section 3 of the main report.
- **RL178.2:** in residue order `r=A i (mod L)`, the mechanical weights are strictly decreasing and
  `F2=rho_t-sum_(r=1)^(L-1)(omega_(r-1)-omega_r)(1-2^(-H_r))`.
- **RL178.3:** the physical zero-height high type `(v,H,J,d)=(37,0,23,+1)` is impossible.
- **RL178.4:** in the surviving `(37,0,23,-1)` type, `a_24=a_(p+24)=1` and `G_25=-1` are forced.

## Exact finite / arithmetic certificate

- `B(23)=36`, `c_23=2`, `c_24=1`.
- `v=37` plus `0<g_p<2^38` gives `g_p=2^37`.
- `v2(3^25+1)=2` excludes the positive high sign.
- `v2(3^25-1)=1` forces the first continuation of the negative high sign.
- Necessary-state counts for the surviving negative high interface are exactly `1,1,2,2,5,10,16` at phases `24..30`.
- Every necessary state has `G_i<0` for `24<=i<=28`.
- Phase 29 is the first phase where a strict positive crossing is admitted; `G_29=0` is absent.
- The only phase-29 positive height pairs are `(1,0),(2,0),(2,1)`, with flow quanta `2^44/3^29`, `2^43/3^28`, `2^43/3^29`.

## Scope / method classification

- The transition automaton is a necessary arithmetic-and-height filter.  Surviving states are not promoted as physical existence.
- The RL177 height-only local automaton remains a certified method barrier; RL178 does not enlarge it and instead adds actual pair-state 2-adic relations.
- The residue-deficit identity is a flow representation, not a revival of the RL175 sparse ownership resultant.

## Inherited correction / scope state

- Corrected `G_i=S_(p+i)-S_p-S_i` remains authoritative.
- Physical `F2=sum q_i(2^G_i-1)=3(lambda-1)g_p` remains authoritative.
- RL173's `3^(-G)` functional remains auxiliary only.
- The inherited external `m>=2^71` minimum is not used in any RL178 core theorem.

## Global status

The zero-height interface is narrowed from 28 signed local types to at most 27 physical candidates, and the zero-height `v=37` pair is reduced to the single `d=-1` sign.  The preferred `h_p=0` branch, the `H>=1` branch, Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.
