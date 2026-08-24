# RL58 audit findings and obstruction notes

Date: 2026-08-23

## 1. Independently audited certificates

RL58 reimplemented both RL57 discovery searches in exact rational C++ using a gap-between-x-zeros recursion rather than the RL57 bit-by-bit/Pareto discovery traversal.

The aligned audit returned

`RL58_GAP_AUDIT target=17/3 hit=0`

with 13,984,558 recursion calls and 18,645,943 gap states. Promote

`M0_26 <= 17/3`.

Using the inherited analytic `M0>83/12`, obtain

`M0_late > 5/4`.

The total-prefix audit returned

`RL58_GAP_TOTAL_AUDIT target=77/10 hit=0`

with 7,624,090 recursion calls and 10,144,875 gap states. Promote

`Zx_26 <= 77/10`,

hence

`Zx_late > 253/60`.

Because each x-zero weight is `<17/30`, the late suffix contains at least eight x-zeros. The strict aligned lower bound forces at least three late aligned zeros and at least two separated aligned runs.

## 2. Repaired/audited local grammar

The complete displacement-one return macro survives reconstruction:

`01 (00)^(n-1) 10`,

with

`n=v2(3Q-7)`

and

`Delta Psi=(7/6)M`.

For displacement zero, one wording repair is essential. For even height-one `Q != 2`,

`v2(Q-2)`

is the **maximum possible uninterrupted all-00 continuation length**, not necessarily the length of the run actually chosen by the word; a legal synchronized `11` may end the actual `00` run earlier.

For odd terminal `K`, the terminal valuation remains

`v3(2^K+1)=1+v3(K)`.

## 3. Sharpened Psi cut

The inherited phase squeeze is

`zeta-1 < (398/45)/2^71 = 199/53126622932283508654080`.

At terminal height one,

`Psi_end=(27*zeta/4)(1+2^-K)`.

With odd `K>=25`,

`Psi_end < 6.750000201165676...`.

Using `Zx_late>253/60` and `Zx(segment)<=Psi(end)-Psi(start)`, obtain

`Psi_cut < 2.533333534499010...`.

This replaces the older loose convenience ceiling used during discovery.

## 4. Exact synchronized positive-cycle obstruction

The direct target `M0_late<=5/4` cannot follow from defect, the sequential cap, and the Psi ceiling alone.

At height one in `J` coordinates there is the exact synchronized pump

`J=3 --11--> 5 --00--> 3`.

One full pump has zero defect, changes `g` by

`g_out=(4/3)g_in`,

adds one aligned zero of weight `(2/3)g_in`, and changes the event counters by

`Delta i=2`, `Delta p=1`, one x-zero.

After `m` consecutive pumps,

`g_m=g_0(4/3)^m`,

`A_m=2g_0((4/3)^m-1)`.

An exact four-pump witness starts at `J=3`, `g=7/20`. Its aligned-zero weights are

`7/30, 14/45, 56/135, 224/405`,

with total

`245/162 = 1.512345679... > 5/4`.

All zero weights remain `<17/30`; final `g=448/405<17/15`; and Psi rises from `7/10` to `896/405=2.212345679...`, below the sharpened RL58 cut ceiling.

Therefore the missing ingredient must use terminal endpoint/exponent arithmetic that local defect and potential accounting do not see.

This witness is only a **local obstruction to the proposed proof method**. RL58 did not prove that four pumps embed in a genuine terminal suffix.

## 5. Other route ruled out at the present relaxation

A discovery search found a survivor-necessary-condition prefix with

`Psi approximately -2.08689`.

Thus current prefix constraints do not force a useful positive lower bound for `Psi_cut`. The sharpened upper ceiling alone does not close the suffix.

## 6. Unpromoted sharper prefix evidence

The RL57 discovery framework rejects aligned targets `5.57`, `5.60`, and `5.65`, with a necessary-condition witness near `5.566678`. RL58 attempted an independent audit of `557/100`, but the independent run did not complete within the session execution limit.

Do **not** promote `M0_26<=557/100`. The audited theorem remains `17/3`.

## 7. RL59 focus

The bottleneck is now the **terminal embeddability of synchronized Collatz-conjugate pumping**.

Before tightening prefix constants again, determine whether enough repeated pumping to supply `M0_late>5/4` can coexist with

`Q_end=2^K+1`, odd `K>=25`,

including `v3(Q_end)=1+v3(K)`, exact event counts, scalar scaling, and the legal grammar entering and leaving the pump block.
