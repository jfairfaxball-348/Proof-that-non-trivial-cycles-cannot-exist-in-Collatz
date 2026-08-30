# RL182 certified facts and proof ledger

## New proved analytic mathematics

- **RL182.1 — chronological numerator transport.** With `k_i=S_(i+1)-S_i`, `G_i=S_(i+p)-S_p-S_i`, and `U_i=2^G_i y_(i+p)-y_i` in the periodic dyadic extension,
  `2^k_i U_(i+1)=3U_i+2^G_i-1`.
  On an ordinary noncarry edge, the physical RL181 numerator is `C_i=2^max(0,-G_i)U_i`.
- **RL182.2 — ternary suffix ownership.** For every n, `C_i (mod 3^n)` is determined by the preceding n chronological `(k,G)` transitions and the current dyadic scaling. For shallow ordinary edges the certified size is below the stated power of three, so the residue uniquely determines the physical integer numerator.
- **RL182.2a — ternary divisibility reset.** `3|C_i` if and only if `G_(i-1)` is even. An odd predecessor defect forces `v_3(C_i)=0`.
- **RL182.2b — zero-defect suffix exclusions.** An ordinary `h<=1` shallow edge cannot be preceded by 25 consecutive zero defects; an ordinary `h<=4` edge cannot be preceded by 27 consecutive zero defects.
- **RL182.3 — universal p-window affine law.** For `P_i=sum_(r=0)^(p-1)q_(i+r)` and normalized p-gap `delta_i`,
  `delta_i=(exp(s)-1)x_i+exp(s)P_i/(3rho_i)`.
- **RL182.4 — affine-tail selected-width theorem.** If every p-gap has tail greater than T, any E selected p-shift ranks have total normalized width greater than
  `m(exp(sE)-1)+T(exp(sE)-1)/(exp(s)-1)`.

## Analytic results with exact rational / integer certificates

Inside the surviving `(37,0,23,-1)` high branch only:

- refined state band:
  `26,385,000,000,000,000,000,000 < m < 28,084,000,000,000,000,000,000`;
- `Q>71,134,646,723`;
- every cyclic t-element q-complement has mass `<60,422,815,771`;
- every periodic p-window has `P_i>10,711,830,952`;
- the affine tail on every normalized p-gap is `>3,570,610,317`;
- shallow numerator ownership depths:
  - `h<=1`: numerator `<3^25`;
  - `h<=2`: numerator `<3^26`;
  - `h<=3`: numerator `<3^26`;
  - `h<=4`: numerator `<3^27`;
- strengthened shallow width occupancy:
  - `h<=1`: `>25m/512`;
  - `h<=2`: `>33m/256`;
  - `h<=3`: `>167m/1024`;
  - `h<=4`: `>23m/128`;
- some fixed shallow defect `G=a-b` occurs on at least
  - `3,358,391,526` ordinary `h<=1` edges;
  - `5,136,718,940` ordinary `h<=2` edges;
  - `4,583,057,040` ordinary `h<=3` edges;
  - `3,888,913,815` ordinary `h<=4` edges.

## Exact verifier output

`verification/verify_rl182_numerator_ownership.py`: PASS.

## New method barrier

- Exact ternary suffix ownership does not by itself cap the number of physically admissible shallow suffixes. The next consumer must bound the physical suffix vocabulary or correlate it with shallow successor incidence/width; arbitrary ternary residue capacity is not closure-grade.

## Inherited correction / scope state

- Corrected `G_i=S_(p+i)-S_p-S_i` remains authoritative.
- The physical corrected-flow functional remains the `2^G` functional; RL173's `3^-G` quantity remains auxiliary only.
- Necessary automata remain one-way filters, not physical existence certificates.
- RL175's sparse ownership resultant is not revived as a generic independent gap obstruction.
- RL168-RL171 rank/chain/inverse-rank barriers remain in force.
- All refined m, Q, shallow population, numerator, and occupancy statements remain internal to the surviving high branch.

## Global status

The sole zero-height `v=37` negative-sign high type survives. The preferred `h_p=0` branch, the positive-height branch, Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.
