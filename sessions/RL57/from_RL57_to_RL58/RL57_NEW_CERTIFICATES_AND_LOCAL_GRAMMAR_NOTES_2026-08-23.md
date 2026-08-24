# RL57 new certificates and local grammar notes

Date: 2026-08-23

This file records only the new RL57 material that is not already part of the inherited RL56 handover.

## 1. Promoted computation: coupled-K `33/4`

Source:

`verification/new_rl57/independent_viable_33_4.cpp`

Fresh output:

`INDEPENDENT_CPP TARGET 33/4 hit False nodes 3676571 states 542063 ... pr [0,0,73533,1006639,675890] ...`

This independently reproduces the RL56 decision result and decision statistics. Treat `Zx_26<=33/4` as promoted, conditional only on the already inherited interfaces it uses.

## 2. Discovery computation: defect-aware `77/10`

Source:

`verification/new_rl57/defect_viable_search_pareto.cpp`

Fresh output:

`DEFECT_NOMEMO target=77/10 hit=0 nodes=6392873 ... prDef=2986 ... prMemo=1447103 memoKeys=1258066 paretoMax=1`

The label `DEFECT_NOMEMO` is a stale print label in the discovery program; the source actually uses Pareto memoization. Do not infer anything from that label.

The new necessary defect condition is

`D_raw - pending*(17/45) < 5/3`,

where `pending=d-1`.

The program rejects at equality or above, which is survivor-favouring because the sequential cap is strict.

Candidate conclusion:

`Zx_26<=77/10`.

Status: **exact run, independent-audit pending**.

## 3. Discovery computation: aligned `17/3`

Source:

`verification/new_rl57/aligned_prefix_search.cpp`

Fresh output:

`ALIGNED target=17/3 hit=0 nodes=11764045 ... memo=1144627 paretoMax=21 prDef=4610 prTot=147410 prTar=3125273 prMemo=2435536`

The aligned objective increments on a height-one `00` x-zero edge. Future aligned mass is upper-bounded by future total x-zero mass for pruning.

Candidate conclusion:

`M0_26<=17/3`.

Status: **exact run, independent-audit pending**.

## 4. Analytic consequence if `17/3` survives

From

`E=sum w[1-(2/3)^r] <5/3`,

every `r>=1` term costs at least `w/3`, so displaced mass is `<5`. With `Zx>143/12`,

`M0>83/12`.

Then

`M0_late >83/12-17/3=5/4`.

Two zero weights sum to `<2*(17/30)=17/15<5/4`, so at least three late aligned zeros are forced.

For a single height-one `00` run, if the first weight is `g` and the run length is `m`, the total is `g(2^m-1)`. Since the last weight is `<17/30`, the whole run is `<17/15`. Therefore `M0_late>5/4` requires at least two separated aligned runs.

## 5. Exact target-8 diagnostic

The path emitted by the current target-8 witness program is

`11011101011101111001001101101101101101101101101001101011110101010110110`.

Important indexing note: the search variable `i` is the **total step index**, not the count of x-zeros. Hence an x-zero at time `i` has weight `2^i/3^p`; this is why a naïve replay using the zero count as the exponent is wrong.

Exact replay gives:

- 71 total steps;
- 45 x-ones;
- 26 x-zeros;
- 25 y-zeros;
- final `(d,J)=(2,21)`;
- first 25 matched defect `1.6485409947...`;
- pending x-zero weight `0.3996163365...`;
- minimum possible final defect after one-step matching `1.7817464402...>5/3`.

Thus this old target-8 viability witness cannot survive the inherited defect bound.

## 6. Local grammar notes

### Aligned zeros

`r=0` corresponds to height-one `00`.

With height-one `Q=J+1`, forward `00` acts by

`Q-2 -> (Q-2)/2`.

Thus, except at the fixed `Q=2`, maximal run length is `v2(Q-2)`.

### Displacement one

Candidate maximal macro:

`01 (00)^(n-1) 10`.

Candidate entry arithmetic:

`v2(3Q-7)=n`.

Candidate potential ratio:

`Delta Psi=(7/6)M`.

These two candidate formulas were derived in-session but were not given a second independent derivation before handover. Audit them before theorem use.

### Terminal 3-adic control

At `Q_end=2^K+1` with odd `K`, LTE gives

`v3(Q_end)=1+v3(K)`.

This controls the terminal backward `11` run exactly. It does not by itself prohibit a final height-one `00`, so the promising target is the arithmetic compatibility of **multiple separated** aligned runs.
