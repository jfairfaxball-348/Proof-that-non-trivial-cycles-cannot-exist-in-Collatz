# RL211 reduced H21 interface

Date: 2026-08-31. This is the compact successor interface.

## Inherited constants and frontier

`A=217976794617`, `L=137528045312`, `B=80448749305`,
`p=65470613321`, `u=103768467013`, `z=L-p=72057431991`,
`Ap-uL=1`, `pB=1 modL`, `K0=2^37`.

Necessary terminal ranks remain **13,415,865,871**:
- above-p source: `7,091,831,284`;
- below-p source: `6,324,034,587`.

Global necessary eta classes remain `0,8,9,17 mod18`;
`011 <=> eta=0 mod9`, `111 <=> eta=8 mod9`.
Below-p constants remain the corrected `37/60/97`.

## RL210 large-offset selector

For every above-p necessary offset `e>=56`, compare
`S_t=b_t-h_t`, `S'_t=b_t-h_(p+t)`.
The first mismatch m satisfies `24<=m<=37`,
`min(S_m,S'_m)=37`, and heights agree before m.
At m=24 the orientation `S_24=37<S'_24=38` is impossible;
the surviving m=24 orientation is
`h_(p+24)=1`, `h_24=0`.
No rank deletion is implied.

Six short offsets remain `e=4,16,28,33,40,45`.
For e=4 and16, RL210 gives p-separated height equality through the source and
`K_0=...=K_(e+1)=2^37`.

## RL211 new e=4 selector

A physical H21 realization at e=4 must satisfy exactly:
- root heights `h_0...h_4 = 00001`;
- root acceleration exponents `a_0...a_3 = 1211`;
- `eta = 207 (mod243)`;
- H21 state `011`, hence eta classes `8,17 mod18` are excluded at this offset;
- terminal parity/sign remains open.

No physical realization is asserted.

## RL211 barrier

Do not treat `K_i/rho_i` as an integer. RL195 requires only dyadicity after the
global odd denominator is removed. Flat `K_i=2^37` makes
`K_i/rho_i=3^i*2^(37-b_i)` automatically dyadic, including at the RL210 first
mismatch phase. A successor must add information beyond this denominator criterion.

## Scope locks

No physical H21 incidence, H21 charge, rank deletion, sole-branch contradiction,
Gate closure or global nontrivial-cycle exclusion is proved.
Preserve the p-shift carry at z, all RL206 correction locks, and the distinction
between necessary ranks and physical populations.
