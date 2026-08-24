# RL-4 Canonical Register Delta — 2026-08-19

This delta supplements the RL-3 register.

| ID | Claim | Status |
|---|---|---|
| RL-L23 | Same-endpoint inverse branches satisfy an exact relative product identity. Equal-depth physical collision is impossible after the distinct entry split. At a first order reversal, the cumulative exponent-sum order must reverse too. | **PROVED ANALYTIC THEOREM** |
| RL-L24 | Least-red prefix slack `sigma_n=n beta_R-S_n` dominates physical height: `log2(r_n/R#)<=sigma_n`. In the tail-larger entry orientation, `sigma_(k-1)>2m` and `N1>(k-1)(2-beta_R)+2m`. | **PROVED ANALYTIC THEOREM** |
| RL-L25 | A first tail-larger down-crossing at depth `H=qL+r` requires total preperiod slack `s >= q(beta_R L-A)+(beta_R r-E_r^-)`. Since `beta_R L-A>0`, fixed phase/cycle/slack permits only finitely many pre-crossing turns. | **PROVED ANALYTIC THEOREM** |
| RL-L26 | In `k=0`, equality `xi(c_j)=R#+1` occurs exactly on the initial neutral spine. Every other cycle phase has `xi(c_j)>=R#+3`. | **PROVED ANALYTIC THEOREM** |
| RL-L27 | If `R#+1=2^s q` and `s<L`, the first post-neutral exponent is `t+1`, `t=v2(3^s q-1)`, its next xi valuation is `r=v3(2^t-1)`, and cycle minimality plus strict xi force `2^(t+s-r)<3^(s-r)`. For `s=2,3,4` with `s<L`, the exit exponent is exactly 2. The boundary case `s=L` reduces instead to `(2^(s+t)-3^s)q=2^t-1`. | **PROVED ANALYTIC THEOREM** |
| RL-L28 | Every maximal exponent-1 plateau has exact compressed state `y+1=2^s 3^mu q`, `n=s+mu`, `W=xi(y)=2^n q`; `n,q,W` stay invariant through the 1-run, and the exit is determined by `t=v2(3^n q-1)`. | **PROVED ANALYTIC THEOREM** |
| RL-L29 | For a regular plateau exit `t<n`, low threshold `2^(n+t-r)<3^(n-r)` forces xi level to rise; any regular xi descent requires the opposite high threshold. Thus a k=0 cycle with `s<L` must contain a later high/deep exit after its low root exit. | **PROVED ANALYTIC THEOREM** |
| RL-L30 | Plateau xi-level telescoping gives `A-L log2 3 = sum eps_j` exactly. This is a structural rewrite of the scalar cycle-product slope, not an independent strengthening; new power must come from discrete valuation/exit constraints. | **PROVED ANALYTIC THEOREM / STRUCTURAL REINTERPRETATION** |
| RL-G8 | The first neutral-spine exit filter alone leaves positive 2-adic Haar measure `mu_exit≈0.5402990693`; it cannot close `k=0` by itself. | **FAILED / REFUTED ROUTE** |
| RL-X6 | New verifier audits crossing catch-up, height/slack coupling, phase decomposition, neutral-spine identities, cycle-exit restrictions, general plateau compression/xi-descent thresholds, and the exit-filter measure series. | **EXACT FINITE CERTIFICATE** |

## Reformulated obligations

- **RL-O2 / k>0:** the first-crossing automaton can drop a free ratio interval and use cumulative exponent difference plus phase/slack. The remaining difficulty is controlling repeated crossings or proving only finitely many are possible.
- **RL-O3 / k=0:** use RL-L28/L29 to classify plateau exits. The root exit is low; periodic return forces at least one later high/deep xi-descent. Quantify the required density/cost of those exits around the cycle.
- **RL-O7:** still critical. The new phase/slack bound is a genuine finite-turn result only after a candidate cycle and slack are fixed; global RL closure still needs an unbounded-family exclusion.
