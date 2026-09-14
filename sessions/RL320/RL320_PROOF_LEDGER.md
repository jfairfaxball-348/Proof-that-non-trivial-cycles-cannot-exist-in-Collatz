# RL320 proof ledger — bounded carries and exact ownership barriers

Date: 2026-09-14
Status: FROZEN WITH RL320 CLOSEOUT

## A. Proved analytic mathematics

1. **Weighted late-row factors.** At least-root height `s>=1`,
   `U_s+3^sV_s=D0(y+3^sm)` and `U_s-3^sV_s=HK`.
2. **Late-row ternary residue.** `K==X^(-1)U_s (mod 3^s)`; for fixed residue
   the RL319 band contains at most `2^36` lifts, although the residue remains
   support-dependent.
3. **Positive-carry three-clock cap.** If `kappa>0`, then
   `min(v2(E),v2(rho))<=33`; if the clocks agree, both are at most 32.
4. **Bounded balanced surrogate.** Conditional on the inherited external
   least-state floor, there are integers `c,theta` with
   `K=3^sc+theta`, `|c|<=2^35`, and `0<|theta|<3^s`, such that positive
   `Z=D0m+Xc`, `W=D0m-Yc` obey
   `Z+W=D0(m+m+c)` and `Z-W=Hc`.
5. **Residual splice.** `U_s=3^sZ+Xtheta` and
   `V_s=W-(Y/3^s)theta`; all unbounded height dependence is localized in
   the signed support residue.

## B. Exact finite arithmetic certificate

At the exact first external survivor, the rational atanh-series enclosure
proves

`Delta>2^-41`.

Together with the inherited external `m>=2^71`, this makes the positive
interval used for the bounded-surrogate extraction wider than one. This is
an exact certificate in externally conditional scope.

## C. Barriers and red teams

1. The three-clock cap controls the earliest interface among three paths,
   not necessarily the physical/coprime-shadow crossing; `kappa=0` remains
   unbounded.
2. The positive balanced surrogate is not ordinary-owned. Determinism
   forbids a balanced row from `m`, whose actual next half has weight
   `ell+s`.
3. Nonnegative-defect and ordered-row geometry admits the explicit
   unbounded-height family `1^(2ell)0^(2a-2ell)`.
4. Unrestricted mixed-height full ownership reaches RL147's combined-layer
   barrier; height-one contact theorems cannot be invoked.
5. Bounded enumeration is regression evidence, not theorem or certificate.

## D. Preserved scope

- Internal-only frontier: `ell>=190537`.
- External-certificate-conditional frontier: `ell>=49,547,666,544`.
- The external `2^71` floor remains externally inherited.
- RL21, RL79, RL147, RL206, RL233, and RL263--RL264 remain binding.
- Gate A: OPEN.
- Gate B: OPEN.
- Global positive non-trivial-cycle exclusion: OPEN.
- `g=1`: separate and OPEN.

`PARENT_DIFFICULTY_DELTA = EASIER`
