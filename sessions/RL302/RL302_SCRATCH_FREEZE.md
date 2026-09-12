# RL302 scratch freeze

Date: 2026-09-12

This file preserves the non-authoritative derivational state needed to reconstruct RL302. Promoted claims are only those restated in `RL302_REPORT.md` / `RL302_PROOF_AND_SCOPE.md`.

## Checkpoint 1 — exact Bellman contraction and finite evidence

The local Bellman equations were derived from the states P, A, R2, R3, boundary 2/3/5/8, and D0=(3,K=24). They gave

`m_2(E)=1+min(m_R3(E),m_8(E))`

and reduced the P/8 identity to O1 + O2. Exact finite regressions found:

- `m_2=m_8+1` on 17,602 common non-2 checkpoints under the local caps;
- `m_3=m_8` on 36,207 common non-2 checkpoints;
- `m_R3=m_8+3` on 4,263 common non-2 checkpoints;
- `m_A=m_2+1` on 8,628 common non-2 checkpoints;
- `m_P=m_8+2` on 36,207 common non-2 checkpoints.

These counts remain evidence only.

## Checkpoint 2 — tower zipper and paired transducer

The R3 tower departure was zipped exactly to RL295 wall families. Tight credits were identified as

`B_L(D)=(D^2+D-6)/2`, `B_R(D)=(D^2+3D-4)/2`.

A relative paired-coordinate recurrence was derived:

`delta'=delta+x-z`,

`r'=(3^x/2)[r+(1-z)3^delta-(1-x)]`,

with synchronized owner-source edge-area difference `delta`. A shared-endpoint zero spine from `(-m,-1)` was observed to earn exact saving `rm+r(r-1)/2` after r source-zero columns. This became the cascade theorem in checkpoint 3.

## Checkpoint 3 — cascade factor identification

After `m=-delta`, `U=-3^m r`, the relative recurrence was recognized as the ordinary canonical recurrence for the left cascade factor. This yielded

`L_D=R_2 o R_(D-2)`

and a structural proof of the RL297 scratch merger

`L_D101100=R_(D-2)000001`

with two-unit owner saving.

Notation correction: this checkpoint temporarily used `R1` for `(1,K=6)`. The correct auxiliary name is `U=(1,K=6)`; established tower notation remains `R_d=(d,3^d)`.

## Checkpoint 4 — tight-wall run-length normal form

The stronger identities

`L_D 0 1^k 01 = R_D 1^(k+1)00`

and

`endpoint(L_D 0 1^k00)=P o endpoint(R_D 1^(k+1)01)`

were derived, both with owner-side continuation saving `k+2`.

An exploratory all-one terminal-ray estimate after the first L-wall zero also gave a Bellman-safe bound for the no-second-zero sector; this estimate is retained as a useful lead but is not needed as a promoted load-bearing theorem in RL302 closeout.

The attempted unrestricted wall grammar was diagnosed as circular because first wall hits of the relative R2 factor encode checkpoint-2 futures.

## Checkpoint 5 — D0 zero spine and F/S normal forms

The D0 all-zero residual was found to be the exact two-state tower

`V_d=(d,3^d-3)`, `W_d=(d,3^d-2)`,

`V_d --0--> W_d --0--> V_(d+1)`.

The first-departure states are

`F_d=(d-1,(3^d-3)/2)`,

`A_d=(d,(3^(d+1)-9)/2)=F_d o Z`.

Checkpoint 2 reaches the adjacent `S_d=(d-1,(3^d-1)/2)` with quadratic historical advantage `(d^2-d-4)/2`.

Odd d produced a merger/leading-P run normal form; even d produced a mod-4 merger/trailing-P normal form. Explicit exact counterexamples showed that neither leading- nor trailing-P insertion is generically monotone for checkpoint distances.

## Checkpoint 6 — conditional O2 collapse and index shift

Because O1 gives `m_2=m_8+1`, O2 becomes direct D0-vs-8 domination. The wall and odd-F/S leading-P siblings were then identified as the same physical states under `D -> D+2`, using

`S_(D+2) --1--> R_D`.

The D0 history enters the shared bootstrap state more expensively than R3 by

`(D^2+7D+8)/2`.

Hence all odd-d>=5 leading-P O2 residuals become conditional sinks into O1; d=3 is directly checkpoint-8 owned at equal cost 4.

## Additional late-session leads not promoted

During the last continuation, a direct shared-endpoint coupling was noticed for the A3 branch: its left endpoint `T=10` equals checkpoint 8's right endpoint `N=10`, and repeated source zeros evolve the shared endpoint along `10->5->7->10`. This suggested a constant relative state `(-1,-2/3)` under a periodic zero coupling. The observation was not completed to theorem standard before closeout and is preserved only as an RL303 lead.

A further finite shortest-path observation suggested D0 is often exactly two area units more expensive than R3 to common checkpoints, with a few small exceptions in the tested range. This was not promoted and should be re-derived from scratch if used.

## Route discipline for RL303

Do not promote any late scratch lead without a fresh exact derivation. Start from the authoritative O1 tight-wall normal form. Use the A3 periodic shared-endpoint observation only if it materially helps close the remaining A_d family after O1.
