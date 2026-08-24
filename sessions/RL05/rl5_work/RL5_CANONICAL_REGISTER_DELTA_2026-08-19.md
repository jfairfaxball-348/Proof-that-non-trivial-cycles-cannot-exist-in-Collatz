# RL-5 Canonical Register Delta — 2026-08-19

This delta supplements the RL-4 register.

| ID | Claim | Status |
|---|---|---|
| RL-L31 | Every compressed exponent-1 plateau has a canonical red anchor `u=xi(y)-1=2^n q-1`, with `v3(u+1)=0`; the physical plateau is a suffix of the anchor's exact neutral run. The compressed cycle is a deterministic orbit of the induced map `F(u)=xi(z)-1`. | **PROVED ANALYTIC THEOREM** |
| RL-L32 | The next `mu'=v3(z+1)` is determined by `r=v3(2^t-1)` versus `n`; `mu'=0 iff t` is odd. If `r>=n`, then `2*3^(n-1)|t`, so saturation costs `t>=2*3^(n-1)`. | **PROVED ANALYTIC THEOREM** |
| RL-L33 | With `h=n-mu'`, `W'/W=(3/2)^h 2^-t(1+eta)`, `0<eta<1`. Thus `h<=0` forces descent; for `h>0`, low forces rise, supercritical forces descent, and only the single critical integer `t=ceil(h log2(3/2))` remains unit-dependent. | **PROVED ANALYTIC THEOREM** |
| RL-L34 | Exact exit `t` is one 2-adic `q` cylinder of mass `2^-t`; saturation mass at depth `n` is exactly `1/(2^(2*3^(n-1))-1)`. Any non-rise obeys `2t>=n`, so potential non-rise mass is at most `2^(1-ceil(n/2))`. Cancellation depth has exact local 3-adic geometric law. | **PROVED ANALYTIC THEOREM / EXACT LOCAL HAAR LAW** |
| RL-L35 | The RL-4 boundary `s=L` and any anchor fixed point `F(u)=u` reduce to a one-local-minimum Collatz cycle. Accepted external result RL-E3 (`m>=92`) excludes them, so consecutive plateau xi levels are never equal on a nontrivial RL cycle. | **PROVED REDUCTION + EXTERNAL EXCLUSION** |
| RL-L36 | The final anchor returning to `R#` satisfies `n=v3(2^tR#+1)`, `t` odd, and is exactly `xi(p_(t+1)(R#))-1`. Its `t` lies in a unique discrete-log class modulo `2*3^(n-1)`, with exact valuation selecting two of three lifts at the next level. | **PROVED ANALYTIC THEOREM** |
| RL-L37 | For k>0, if `((3R#+1)/(3R#))^h<2`, the sign of nonzero `D_h-E_h` equals the physical order sign. In particular this holds for every `h<=2R#`. | **PROVED ANALYTIC THEOREM** |
| RL-X7 | New verifier audits anchor normalization, valuation/reset laws, xi direction, local Haar costs, root-return discrete logs, and the k>0 rigidity horizon; inherited RL-4 verifier passes. | **EXACT FINITE CERTIFICATE** |
| RL-L38 | Every anchor transition is exactly `W'=ceil(3^h W / 2^(h+t))`, `h=n-mu'`; equivalently `dW'=ell W+c` with explicit positive integer coefficients. | **PROVED ANALYTIC THEOREM** |
| RL-L39 | For a cyclic compressed word, every rotation has denominator defect `6^M(2^A-3^L)` and unique rational candidate `W_r=C_r/[6^M(2^A-3^L)]`. Genuine cycles require simultaneous all-rotation integrality and exact local valuation realization. | **PROVED ANALYTIC THEOREM** |
| RL-L40 | The composed numerator is 2-adically triangular, so `v2(C_r)=M+n_r` is automatic. If no exit satisfies the exact boundary `v3(2^t-1)=n`, then `v3(C_r)=M` is automatic too; nontrivial 3-adic numerator cancellation is localized to those boundary exits. | **PROVED ANALYTIC THEOREM** |
| RL-X8 | Finite compressed-word sieve checks 75,894 words with `P<=3`, `n,t<=6`, cancellation depth `<=2`; only repetitions of the trivial `W=2` anchor survive. This is diagnostic only. | **EXACT FINITE CERTIFICATE (DECLARED DOMAIN)** |
| RL-L41 | For a generic admissible cyclic word (`v3(2^t-1) != n` at every exit), `D|C_r` at one rotation is necessary and sufficient for a positive periodic integer anchor orbit. `D`-divisibility propagates to all rotations, automatic numerator valuations supply `6^M`, and the affine identity forces the declared local exit valuations to be exact. | **PROVED ANALYTIC THEOREM** |
| RL-X9 | Exhaustive finite audit of 165,728 generic admissible words with `P<=3`, `n,t<=8`: only three `D`-divisible words occur, all repetitions of the trivial `W=2` anchor; no nontrivial realization in the declared domain. | **EXACT FINITE CERTIFICATE (DECLARED DOMAIN)** |

## Reformulated obligations

- **RL-O3 / k=0:** RL-L41 reduces every generic admissible word to one scalar condition `D|C_r`. The next obstruction must act directly on this divisibility using the low departure and high/discrete-log return gates. Exact saturation-boundary words remain a separate 3-adic cancellation subproblem.
- **RL-O5 / k=0 boundary:** the exceptional one-plateau branch is closed conditional on the accepted Hercher `m>=92` external theorem.
- **RL-O2 / k>0:** repeated order requires no ratio state through depth `2R#` away from `D_h-E_h=0`; extend this with a cumulative correction/reciprocal-height budget for arbitrary `k`.
- **RL-O7:** remains critical. RL-L40 shows generic numerator valuation tests are automatic; dependence now lives in exact denominator divisibility/local-cylinder realization, while exact saturation-boundary exits carry a separate 3-adic cancellation grammar.
