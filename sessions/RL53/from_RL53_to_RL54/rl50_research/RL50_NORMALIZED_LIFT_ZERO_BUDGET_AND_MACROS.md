# RL50 — normalized lifts, all-height synchronized macros, and a phase zero-budget theorem

Date: 2026-08-22

## Status

**ANALYTIC IDENTITIES + NEW ANALYTIC CONSEQUENCE + EXACT REGRESSION VERIFIER.**

This note does not close Gate A. It strengthens the coupled full-phase object in three ways:

1. reconstructs the exact monotone lifts of both halves;
2. extends the RL49 height-one telescope to synchronized macroblocks at every fixed height;
3. proves a new phase-specific zero-count theorem, using only the accepted `2^71` external floor.

## 1. Internal coordinates

Before internal column `i`, let

- `p_x,p_y` be the numbers of internal `x`/`y` ones already used;
- `d = 1+p_y-p_x >= 1`;
- `g = 2^i/3^{p_x}`;
- `h = 2^i/3^{p_y} = g/3^{d-1}`;
- `T = 3^d A_i-B_i` for the two physical shortcut-Collatz states after the fixed leading prefixes `110` and `111`.

Put

`R := g T / 3^d`.

For the two global normalized monotone lifts define

`U_i = 2^(i+3) A_i / 3^(p_x+2)`,

`V_i = 2^(i+3) B_i / 3^(p_y+3)`.

Then exactly

`U_i - V_i = (8/9) R_i`.

At the internal entrance of a full-phase object starting at `N` and `N+4`,

`U_0 = N+5/9`,

`V_0 = N+127/27`,

`R_0 = -14/3`.

## 2. Exact per-column increments

For an internal edge `(x,y)` at height `d`,

`U_{i+1}-U_i = (8/27) x g`,

`V_{i+1}-V_i = (8/27) y g / 3^d`,

and

`R_{i+1}-R_i = (g/3)(x-y/3^d)`.

These identities are exact and are checked column-by-column on the audited RL47 `(65,41),t=2` structural witness.

The second formula shows that the previously used quantity

`S = sum_{y_i=1} h_i/3`

is exactly the internal `v`-lift mass:

`V_m-V_0 = 8S/27`.

Under full phase this equals

`N(zeta-1)-127/27`.

## 3. All-height synchronized telescope

On a synchronized edge (`00` or `11`) the height is fixed.

For `00`, `R` is unchanged and `V` is unchanged.

For `11` at fixed height `d`,

`Delta R = (g/3)(1-3^{-d})`,

`Delta V = (8/27)g/3^d`.

Therefore on **every maximal synchronized macroblock at fixed height `d`**,

`boxed: Delta V = [8/(9(3^d-1))] Delta R`.

For `d=1` the coefficient is `4/9`; multiplying by the relation between `R` and `gT` gives exactly the RL49 height-one synchronized-mass telescope.

This removes synchronized pumping from the explicit column grammar at every height. A future area proof can work with macro endpoints plus skew edges.

## 4. A sharper post-zero prefix cap

RL49's exact prefix cap gives at every actual internal prefix

`8 g_i <= 9 zeta^2`.

If column `i` has `x_i=0`, then

`g_{i+1}=2g_i`.

Applying the same prefix cap at the *next* prefix gives

`16 g_i <= 9 zeta^2`,

so every internal x-zero contributes to `Zx` with weight

`g_i <= (9/16) zeta^2`.

The terminal internal prefix must be included when the last internal column is an x-zero; this is part of the exact prefix-cap hypothesis and is explicitly regression-checked.

## 5. Safe phase squeeze gives a convenient rational cap

Using only the accepted computational floor `N >= 2^71`, RL49's phase squeeze gives

`zeta-1 < 398/(45*2^71)`.

Exact rational arithmetic shows

`(1+398/(45*2^71))^2 < 136/135`.

Hence on every genuine full-phase x-zero,

`g_i < (9/16)(136/135) = 17/30`.

No Ansari extension is used here.

## 6. New zero-budget theorem

RL49 proved the exact compressed identity

`3Zx-Zy = 12 + (27/2) zeta(1+2^{-k})`.

Since `Zy>=0` and `zeta>1`,

`3Zx > 12+27/2 = 51/2`,

hence

`Zx > 17/2`.

Suppose there were at most 15 internal x-zero columns. Each contributes strictly less than `17/30`, so

`Zx < 15*(17/30)=17/2`,

a contradiction.

Therefore:

> **RL50 phase zero-budget theorem.** Every retained genuine full-phase one-excursion object satisfying the exact prefix cap and lying above the accepted `2^71` verified prefix has at least 16 internal x-zero columns.

In the inherited one-excursion geometry, the terminal zero counter is

`z = 1 + (# internal x-zero columns)`

and `z+t=q=a-ell`. Consequently

`boxed: z >= 17}`

and

`boxed: t <= q-17}`.

The audited RL47 structural witness has 21 internal x-zero columns (`z=22`), so it is consistent with the theorem; it is not full phase and is used only as a convention/regression check.

## 7. Relation to the Gate-A target

The desired contradiction is

`H <= t+2` impossible,

equivalently at terminal height one

`v_2(T+1)=t+3 <= H`.

The zero-budget theorem alone does not imply this. Its value is structural:

- it is a uniform consequence at arbitrary enormous denominator;
- it removes the final 16 suffix positions from the live `t` range;
- together with the all-height synchronized telescope, it gives a macro grammar in which long synchronized stretches are represented only by endpoint data.

The hard unresolved part remains the height-one 2-adic exit mechanism of the inherited `(d,H,J)` quotient.

## Verification

Run:

`python rl50_research/verify_rl50_lift_zero_budget.py`.
