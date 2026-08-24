# RL56 — aggregate mass potential and terminal-compatible legal-prefix theorem

Date: 2026-08-23

## Status

**New analytic theorem + exact finite certificate.** This does not eliminate the safe-CF survivor, prove Gate A, construct Gate B, close RL, or prove Collatz.

The main gain is a new monotone potential that pays x-zero mass column-by-column and a rigorous terminal-compatible improvement of the first-26 mass bound.

## 1. A corrected monotone lift

Retain the inherited state

`g=2^i/3^(p_x)`, `d>=1`, `T`, `J=T+3^d-2^d`.

Define

`Xi = g * [ (T-1)/3^(d-1) + 1/2^(d-1) ]`.

Equivalently,

`Xi = 3(gT/3^d) + g(2^(1-d)-3^(1-d))`.

Thus `Xi` is a height-gauged version of the inherited `R=gT/3^d` lift; the gauge vanishes at height one.

Direct substitution in the four exact forward maps gives, with `g` the pre-edge scalar,

- `00`: `Delta Xi = g(2^(1-d)-3^(1-d)) >=0`, equality only at `d=1`;
- `01`: `Delta Xi = 0`;
- `11`: `Delta Xi = g(1-2^(1-d)/3) >0`;
- `10`: `Delta Xi = g(1+2^(1-d)/3-3^(1-d)) >0` for `d>=2`.

Hence `Xi` is monotone on every legal column.

At the retained start `(d,T,g)=(1,-14,1)`,

`Xi_start=-14`.

At terminal `(d,J)=(1,2^K)` with `T=2^K-1` and `g_end=27*zeta/2^(K+1)`,

`Xi_end = (27*zeta/2)(1-2^(-K))`.

Using the inherited safe bound `zeta<136/135` and `K>=3`,

`Xi_end < 68/5 = 13.6`.

Therefore every prefix of a genuine safe-CF survivor satisfies the **legal terminal-compatibility cut bound**

`Xi < 68/5`.

This is a true live-prefix theorem; unlike the demoted `-1318<J_cut<1379` interval, it does not assume the illegal relaxed-greedy prefix.

## 2. A zero-mass-majorizing potential

Define

`Psi = g + Xi/2`.

Equivalently,

`Psi = g * [1 + (T-1)/(2*3^(d-1)) + 1/2^d]`.

Its exact increments are

- `00`: `Delta Psi = g[1+2^(-d)-1/(2*3^(d-1))] >= g`;
- `01`: `Delta Psi = g`;
- `11`: `Delta Psi = g[1/6-1/(3*2^d)] >=0`;
- `10`: `Delta Psi = g[1/6+1/(3*2^d)-1/(2*3^(d-1))] >0`.

Therefore `Psi` is monotone and every x-zero of weight `w=g` is paid one-for-one:

`Delta Psi >= w` on `x=0`,

`Delta Psi >=0` on `x=1`.

Consequently, for **any** segment of a legal path,

`Zx(segment) <= Psi(end)-Psi(start)`.

At height one, `Psi=g(J+1)/2`; thus

`Psi_start=-6`,

`Psi_end=(27*zeta/4)(1+2^(-K))`.

The same inherited bounds give the uniform ceiling

`Psi_end <= 153/20 = 7.65`,

where equality is only the rational relaxation `zeta=136/135, K=3`; a genuine survivor is strict.

This is the requested aggregate/telescoping mechanism. It controls the sum of zero weights directly rather than forcing each weight microscopic.

## 3. The old legal-26 maximizer is not terminal-compatible

The independently audited RL55 legal maximum

`Zx_26 = 34057930625026471931596 / 2954312706550833698643`

occurs at x-zero positions

`[2,5,7,10,14,15,18,21,25,26,29,32,34,37,40,44,45,48,51,53,56,59,62,64,67,70]`.

Replaying the exact forced-y dynamics gives after column 70

`(d,J,p_x)=(1,24,45)`,

`g=2^71/3^45`.

At height one, `Xi=g(J-1)=23g`, and exact arithmetic gives

`Xi > 68/5`.

Therefore the RL55 mass-maximizing legal 26-zero prefix cannot occur inside any genuine terminal survivor. This is a new correction to the optimization interface: the old `11.528207745...` maximum is legal as a prefix but terminal-incompatible.

## 4. Exact terminal-compatible first-26 certificate

The companion verifier adds only two analytic necessary conditions to the audited legal-prefix automaton:

- `Xi<68/5`;
- `Psi<153/20`.

It otherwise relaxes in the survivor's favor:

- the strict x-zero cap is replaced by `g<=17/30`;
- the terminal ceilings use the larger rational safe bounds;
- future mass is bounded by the same safe sequential-cap/geometric relaxations, plus the new aggregate bound `future Zx <= 153/20-Psi`.

Accumulated mass is represented exactly as `N/3^p`, so the search uses integer arithmetic for the objective and exact integer cross-multiplication for all cuts.

The exhaustive result is

`Zx_26^(terminal-compatible) <= 107/10 = 10.7`.

Therefore every genuine safe-CF survivor must satisfy the stronger late-mass lower bound

`Zx_late > 143/12 - 107/10 = 73/60`

`= 1.216666666666...`.

This replaces the previous contradiction threshold `Delta=0.3884589215...` **for any argument that uses the new terminal-compatible prefix theorem**. A future upper bound only needs to beat `73/60`, not the smaller old `Delta`.

## 5. Why this does not yet close the survivor

The scalar potential has a genuine neutral obstruction inherited from the height-one negative Collatz cycle.

One complete negative macro `11,00,11`, starting with scalar `g`,

- has one x-zero;
- contributes `(2/3)g` x-zero mass;
- scales `g` by `8/9`.

After `r` complete macros,

`Zpre = 6(1-(8/9)^r)`

and, at the return state `J=-13`,

`Psi = -6(8/9)^r`.

For `r=26`, the remaining scalar potential room to terminal is still far larger than `73/60`. Thus a theorem using only monotonicity of `Psi` cannot finish the aggregate late-mass bound. The terminal power/divisibility condition must be used to rule out or compress this neutral pumping.

This is a useful method barrier: the new potential removes the earlier pointwise-weight problem, but it does not remove the Collatz-conjugate height-one obstruction by itself.

## 6. P-coordinate relation and next attack

With the audited backward normalization `P=2^r J`, the new theorem suggests carrying not `P` alone but the pair

`(P, Xi)` or `(P, Psi)`.

`P` supplies the fixed terminal arithmetic endpoint `P_end=2^(q-24)`, while `Xi/Psi` supplies a monotone real/rational budget and exact aggregate mass control. The next high-leverage task is therefore:

1. derive the backward updates of `Xi` or `Psi` alongside the four exact `P` moves;
2. quotient the height-one `00/11` neutral macros using `P` residues/divisibility;
3. prove that a terminal-compatible state after 26 x-zeros cannot retain `73/60` of future `Psi`-paid zero mass;
4. only if that reduces to a bounded K-window, use exact computation there.

The old fixed `2^-1000` pointwise target should remain retired.

## 7. Classification

- `Xi` monotonicity and terminal ceiling: **analytic theorem**.
- `Psi` zero-mass majorization: **analytic theorem**.
- exclusion of the old legal-26 maximizer: **exact analytic/rational consequence**.
- `Zx_26<=107/10` under terminal compatibility: **exact exhaustive finite certificate**.
- `Zx_late>73/60` for any surviving path: **exact consequence of the certificate plus inherited `Zx>143/12`**.
- uniform upper bound `Zx_late<73/60`: **open**.
- safe-CF survivor elimination: **open**.
- Gate A, Gate B, RL, Collatz: **open**.
