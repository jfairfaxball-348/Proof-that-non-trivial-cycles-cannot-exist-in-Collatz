# RL43 — elimination of rho=49 and the excess-versus-gap lemma

Date: 2026-08-22

## Status

**ANALYTIC REDUCTIONS + EXACT FINITE CERTIFICATE** in the inherited near-resonant order-2 / `g=2` balanced-return branch.

Fresh consequence:

> **`rho >= 50`.**

RL and the full `g=2` branch remain open.

Companion verifier: `verify_rl43_rho49_elimination.py`.

## 1. New cutoff-free local lemma

Consider a canonical positive maximal excursion with

- length `h`,
- common odd weight `p`,
- transport area `r`,
- excess `e=r-p`,
- local numerator difference `D=Q(alpha)-Q(beta)>0`.

Because every one of the `h-1` internal excursion columns has nonzero prefix imbalance,

`r>=h-1`.

Hence

`h-p<=e+1`.                                                 (R43.1)

Let the odd positions of `alpha` be `i_0<...<i_(p-1)`. Since `alpha` has only `h-p` zeroes,

`i_j <= j+(h-p) <= j+e+1`.

Therefore

`Q(alpha)/3^p`

`=sum_(j=0)^(p-1) 2^(i_j)/3^(j+1)`

`<2^(e+1) sum_(j>=0) (2/3)^j/3`

`=2^(e+1)`.

Since `0<D<Q(alpha)`, we obtain

> **`D/3^p < 2^(e+1)`.**                                   (R43.2)

If the excursion physically crosses from positive incoming gap `g` to a negative outgoing gap, then

`D-3^p g = 2^h g_out >0`,

so

> **`g < 2^(e+1)`.**                                      (R43.3)

Equivalently, for odd integer `g`,

`e >= floor(log_2 g)`.                                     (R43.4)

If a synchronized run with `c` common odd columns immediately precedes the excursion, then `3^c|g`, hence `g>=3^c`, giving

> **`e >= floor(c log_2 3)`.**                             (R43.5)

For a noncrossing inward excursion with relative kick

`t_E=D/(3^p g)`,

(R43.2) gives the stronger RL38 replacement

> **`t_E < 2^(e+1)/g <= 2^(e+1)/3^c`.**                   (R43.6)

The key improvement is that synchronized mass is now priced in **excess `e=r-p`**, exactly the same defect variable that appears in the RL42 effective-mass loss.

## 2. Infinite-to-small reduction for low excess

For `e<=6`, (R43.3) implies any crossing incoming odd gap lies in

`1,3,5,...,127`.

This permits an exact 2-adic prefix filter. For a fixed candidate `g`, define

`S=Q(alpha)/3^p-Q(beta)/3^p`.

After `n` columns, future contributions are multiples of `2^n` in the 2-adic integers. A crossing requires

`S == g (mod 2^h)`,

so any prefix failing

`S == g (mod 2^n)`

can be discarded permanently.

The verifier uses this filter rather than enumerating the roughly 200 million raw `e=6` words in the relevant range.

It checks only 7,670 targeted prefix nodes to classify all crossing types with `e<=6` through the required `p` range.

It also verifies:

> **No physical crossing with `e<=3` exists through `p<=49`.** (R43.7)

This extends the inherited bounded certificate exactly far enough for the `rho=49` contradiction.

## 3. Top-level rho=49 reduction

At `rho=49`, the inherited transport theorem gives `G=4`.

The exact effective-mass lower bound is

`M_eff >= 12(z+1)/z^2`,

with `1<z` and `z^2<16/15`.

Since this function decreases with `z`,

`M_eff > (45/4)(1+sqrt(16/15)) > 91/4`.                   (R43.8)

For each positive moved rank of displacement `delta`,

`1-2^(-delta) <= (delta+1)/4`.

Therefore, if `P_+` is positive moved-rank mass,

`M_eff <= (rho+P_+)/4`.

If `P_+<=42`, this is at most `91/4`, contradicting (R43.8). Hence

> **`P_+>=43`.**                                           (R43.9)

A mandatory crossing has `e>=4` by (R43.7), so total excess `E>=4`. Since

`rho=P+E=49`,

we have `P<=45`. Combining `P>=P_+>=43`, only three layers remain:

`(P,E)=(45,4),(44,5),(43,6)`.                              (R43.10)

The same effective-mass inequality sharpens the sign pattern:

- `(45,4)`: `P_+>=44`, so negative moved mass is at most 1;
- `(44,5)`: all 44 moved ranks are positive;
- `(43,6)`: all 43 moved ranks are positive.

## 4. Exact low-excess crossing families

The targeted 2-adic classifier finds the following exact families through the needed range.

### Excess 4

For every `p=5,...,45`, exactly one crossing type:

`h=p+3`, `g=1`, `g_out=4`,

`D=3^p+4*2^(p+3)`.

Its effective mass is exactly

`p/2+7/8`.                                                  (R43.11)

### Excess 5

The crossing types are the two parametric families

`D=3^p+2^(p+4)`, `g=1`, `g_out=1`,

and for `p>=6`,

`D=3^p+4*2^(p+4)`, `g=1`, `g_out=4`.

Every `e=5` crossing has effective mass at most

`p/2+9/8`.                                                  (R43.12)

### Excess 6

The exact catalog consists of the three parametric families

`3^p+2^(p+5)`,

`3^p+4*2^(p+5)`,

`5*3^p+4*2^(p+5)`,

in their verifier-recorded parameter ranges, plus one exceptional `p=6` type with incoming gap 3.

These classifications are certificate statements in the bounded `p` range used below; only (R43.2)–(R43.6) are asserted cutoff-free.

## 5. Safe boundary dynamic programmes

The verifier combines:

- exact `e<=2` local excursion catalogs;
- direct `e=0` transition formulas;
- the exact `e=4,5,6` crossing catalogs;
- the inherited first physical gap `9` for `G=4`;
- the terminal condition that the raw gap must be `-4*2^t`;
- a safe synchronized-run over-approximation allowing every `c=0,...,v2(raw)`.

The resulting state counts and near-resonant endpoint survivors are:

### `(P,E)=(45,4)`

- states: `588,221`;
- endpoints: `823`;
- near-resonant survivors:
  - `(a,ell,negative mass)=(130,82,1)`;
  - `(149,94,1)`.

### `(P,E)=(44,5)`

- states: `488,536`;
- endpoints: `652`;
- near-resonant survivor: `(130,82)`.

### `(P,E)=(43,6)`

- states: `1,151,440`;
- endpoints: `660`;
- near-resonant survivor: `(130,82)`.

## 6. Effective-mass elimination of the residue

For `(45,4)`, every near survivor has one negative moved rank, hence `P_+=44`. The unique `e=4` crossing contributes `p/2+7/8`, while positive `e=0` excursions contribute `p/2`. Thus

`M_eff=44/2+7/8=183/8=22.875`.

The exact integer comparison in the verifier gives

`12Y(X+Y)/X^2 >183/8`

at both `(130,82)` and `(149,94)`, contradiction.

For `(44,5)`, all ranks are positive. Whether the excess is carried by one `e=5` crossing or an `e=4` crossing plus one unit of noncrossing excess,

`M_eff <=44/2+9/8=185/8=23.125`.

At `(130,82)`, the exact lower bound is larger, contradiction.

For `(43,6)`,

`M_eff <=43/2+6/4=23`,

while the exact lower bound at `(130,82)` is larger, contradiction.

Therefore

> ## **`rho !=49`.**

Together with the inherited audited frontier `rho>=49`, this gives

> # **`rho>=50`.**                                         (R43.13)

## 7. Strategic meaning

The numerical advance from 49 to 50 is useful, but the larger gain is (R43.2)–(R43.6):

> **A large physical/synchronized gap has an unavoidable logarithmic cost in transport excess.**

This places synchronization charge and arithmetic transport efficiency on the same defect variable. The companion RL43 defect-support note develops the second consequence: low excess also forces low algebraic support, creating a sparse-resultant gateway to the radius-3 machinery.

## 8. Fresh verifier output

```text
RL43 rho=49 elimination verifier: PASS
targeted 2-adic prefix nodes = 7670
no physical e<=3 crossing through p<=49
crossing types p<=45: e4 = 41 e5 = 84 e6 = 123
(45,4) states/endpoints/near = 588221 823 [(130, 82, 1), (149, 94, 1)]
(44,5) states/endpoints/near = 488536 652 [(130, 82)]
(43,6) states/endpoints/near = 1151440 660 [(130, 82)]
effective-mass endpoint tests eliminate every near survivor
certified consequence: rho != 49; together with inherited rho>=49, rho>=50
```
