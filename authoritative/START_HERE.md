# Authoritative start — RL283

Date prepared: 2026-09-08
Authority repair: 2026-09-08 — exact RL282 `H<=22` checkpoint certificate restored.

Incoming completed generation: **RL282 — terminal-backward height-digit pricing and local-tail barrier, plus exact H<=22 Gate-A contraction**.

RL282 primary classification:

`TERMINAL_BACKWARD_HEIGHT_DIGIT_PRICING_AND_LOCAL_TAIL_BARRIER_PROVED`

Promoted analytic subordinate results:

- `ONE_ZERO_MOD3_OUTPUT_SHELL_PROVED`
- `ARBITRARY_POSITIVE_BOUNDARY_SUFFIX_AFFINE_COMPRESSION_PROVED`
- `TERMINAL_ONE_ZERO_HEIGHT_DIGIT_PRICING_PROVED`
- `BOUNDARY_INVERSE_RUN_RECURRENCE_PROVED`
- `PURE_ZERO_FINAL_TAIL_LOCAL_REALIZABILITY_FAMILY_PROVED`
- `POSITIVE_TAIL_MASS_AND_F_BARRIER_PROVED`
- `UPSTREAM_CHECKPOINT_REACHABILITY_IDENTIFIED_AS_GATE_A_OBSTRUCTION`

Promoted exact finite certificates:

- `HEIGHT_22_POSITIVE_CHECKPOINT_AUTOMATON_CERTIFIED`
- `K5_TO_K23_GATE_A_CASES_CLOSED_CERTIFIED`

Promoted exact state:

- every reachable positive one-zero output has `nu_3(J)=1`;
- any final positive boundary suffix compresses exactly to `(L,r,C_w)` with
  `2^(k+L)=3^r J_0+C_w`;
- the preceding one-zero height is bounded by the exact terminal valuation
  `h<=nu_3(2^(k+L+1)-2C_w+3^(r+1))-r`;
- the positive boundary inverse block is
  `R_t(A)=2(2^t A/3^t-1)`;
- deep inverse undershoot forces available one-zero height `1`;
- for every odd `k>=3` and every `h>=2`, infinitely many locally legal positive final blocks
  `J_in --0 1^h--> J_0 --0^q--> 2^k`
  exist;
- along that local family, positive zero mass tends to `Q_T` and `F_T-F_in` tends to `4Q_T`;
- therefore final-tail 3-adic thinning plus the inherited positive mass/`F` budgets cannot by themselves close Gate A;
- the exact `H<=22` checkpoint automaton contains `146,341` positive even checkpoints and closes every odd terminal exponent `k=5,7,...,23`;
- the exact power minima are
  `k5:H9, k7:H15, k9:H15, k11:H18, k13:H18, k15:H22`;
- no `2^17,2^19,2^21,2^23` terminal occurs anywhere under `H<=22`;
- the exploratory `H=23..26` computation remains unpromoted evidence.

Gate A remains open with exact target

`H_can>=k`

at terminal `d=1,J=2^k`.

Every hypothetical Gate-A violator is now in

`k>=25`, `k` odd, `H_can<k`.

Read

`RL283_UPSTREAM_2ADIC_CHECKPOINT_REACHABILITY_GATE_A_TARGET.md`

first.

RL283 is **prepared but NOT STARTED**.

Priority: prove an upstream global reachability/state-height theorem, preferably
`nu_2(J)<=H` for reachable positive even `d=1` checkpoints, or identify the minimal additional invariant needed to obtain an equivalent terminal consequence.

Do not restart final-tail 3-adic classification, positive zero-count/mass-only arguments, or raw height-cap enumeration as the principal route.

Gate B remains separate/open/frozen. The fifth selector was not scanned. Radius 6+ remains frozen. No global non-trivial-cycle exclusion is claimed.
