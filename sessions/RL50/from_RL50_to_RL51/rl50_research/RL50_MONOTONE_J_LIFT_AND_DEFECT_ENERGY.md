# RL50 monotone J-lift and exact defect-energy decomposition

Date: 2026-08-22

## 1. Setup

Use the inherited one-excursion quotient state

`J = T + 3^d - 2^d`

and the RL50 prefix weight

`g = 2^i / 3^(p_x)`.

Define the new normalized lift

`W := g J / 3^d`.

This is complementary to the previously used `R=gT/3^d`: `W` is adapted to the Markov `J` coordinate and, crucially, is monotone on all four edge types.

## 2. Exact one-column increments

For a column `xy`, direct substitution in the four inherited `J` maps gives

- `00`: `Delta W = g(3^d-2^d)/3^d`;
- `11`: `Delta W = g(2^d-1)/3^(d+1)`;
- `01`: `Delta W = g(3^(d+1)-2^d-1)/3^(d+1)`;
- `10`: `Delta W = 0`.

For every `d>=1` these are nonnegative; the first three are strictly positive. Therefore `W` is an exact monotone potential and `10` is its only zero-increment edge.

The boundary values are especially simple. At the retained start,

`(d,J,g)=(1,-13,1)`, so `W_start=-13/3`.

At the terminal state `d=1`, `J=2^k`, and

`g_end = 27 zeta / 2^(k+1)`, so `W_end=9 zeta/2`.

Hence every retained path has the denominator-free total budget

`Delta W_total = 13/3 + 9 zeta/2`.

Under the safe phase squeeze this is only infinitesimally above `53/6`.

## 3. Local defect energy

Let the column's contribution to the normalized `v` odd-mass `S` be

`Delta S = y g / 3^d`,

and let its contribution to the `x`-zero mass `Zx` be

`Delta Zx = (1-x)g`.

Define

`epsilon := 3 Delta W - Delta S - Delta Zx`.

Exact simplification gives

- `00`: `epsilon = g(2 - 2^d/3^(d-1))`;
- `11`: `epsilon = g(2^d-2)/3^d`;
- `01`: `epsilon = g(2 - (2^d+2)/3^d)`;
- `10`: `epsilon = 0`.

Thus `epsilon>=0` for every legal height. More sharply,

`epsilon=0`

exactly on

- `10` at any height; and
- synchronized `00` or `11` at height one.

A height-one `01` exit already costs `2g/3`, and every `00`, `11`, or `01` column above height one has strictly positive cost.

## 4. Exact global identity

Summing the definition gives

`sum epsilon = 3 Delta W_total - S - Zx`.

Use the inherited exact zero-position identities

`Zx = S - 1 + g_end + E`

and

`2S + 3E = 14 + (27/2) zeta(1-2^(-k))`,

together with

`g_end = (27/2) zeta 2^(-k)`.

All boundary terms cancel, leaving the exact structural identity

`boxed: sum epsilon = 2E`.

This is not a relaxation and does not use the full-phase numerical bound. It is an exact positive decomposition of the rank defect `E` into local excursion/synchronization costs.

Consequences:

1. `E>=0` has a dynamical sum-of-nonnegative-terms certificate.
2. `E=0` would force every column to lie in the zero-cost grammar: height-one `00/11` plus `10` descents. Since leaving height one requires a positive-cost `01`, an actual excursion forces `E>0`.
3. On the sole safe continued-fraction survivor, RL50 already proved `E<5/3`; therefore

   `sum epsilon < 10/3`.

4. If the live Barina floor `2075*2^60` is admitted separately, `E<3/2`, hence

   `sum epsilon < 3`.

5. Locally `Delta S + Delta Zx <= 3 Delta W`, so globally

   `S+Zx <= 13 + (27/2)zeta`.

The last inequality is weaker than the exact identity once `E` is retained, but it makes the finite `W` budget transparent.

## 5. Relation to the height-one Collatz conjugacy

At height one, the zero-energy synchronized grammar is precisely the `00/11` grammar that RL50 identified with the shortcut Collatz dynamics under `n=(J-1)/2`. This is useful conceptually:

- the potentially arbitrarily long Collatz-like pumping is exactly the zero-energy part;
- every genuine departure from that height-one synchronized grammar is measured by `epsilon`;
- the phase defect `E` is exactly half of the total weighted departure energy.

So the live Gate-A problem can be reformulated as follows:

> show that a terminal path with `H<=t+2`, the exact prefix cap, and full phase cannot both (i) follow the zero-energy height-one Collatz grammar for arbitrarily long stretches and (ii) accomplish all required excursion/terminal changes with total defect energy below the phase-forced bound.

This is a materially sharper interface than treating `H`, `E`, and the height-one pump independently.

## 6. Status

**Analytic theorem:** exact monotone `W` lift; exact nonnegative local energy formulas; exact identity `sum epsilon=2E`.

**Exact finite certificate:** audited RL47 witness regression and symbolic height checks in `verify_rl50_monotone_J_lift_defect_energy.py`.

**Not proved:** Gate A `H>=t+3`. Small defect energy alone does not bound the number of zero-energy height-one synchronized steps, because those steps are Collatz-conjugate and can rescale `g`. The prefix cap must be used at macro exits to finish the argument.

## 7. Localization on the sole safe continued-fraction survivor

The positive-energy decomposition also localizes where the phase mass must live.

Let `S_free` denote the part of `S` carried by height-one `11` columns, and let `Z00_free` be the `g`-mass of height-one `00` columns.

For every `y=1` edge other than height-one `11`, the local formulas give

`epsilon >= 2 Delta S`.

Since `sum epsilon=2E`,

`S_nonfree <= E`, hence `S_free >= S-E`.

For every `x=0` edge other than height-one `00`,

`epsilon >= (2/3)g`.

Thus the nonfree x-zero mass is at most `3E`.  Using

`Zx=S-1+g_end+E`,

we get

`Z00_free >= Zx-3E = S-1+g_end-2E > S-1-2E`.

On the sole safe sub-Legendre survivor, the separately certified clean bounds

`S>45/4`, `E<5/3`

therefore force

`S_free > 115/12`,

`Z00_free > 83/12`.

### Initial negative-cycle budget

Before the first positive-energy edge, the path is forced to remain at height one on the zero-energy `00/11` grammar. Starting from `J=-13`, this is the exact negative shortcut cycle

`-13 -> -19 -> -9 -> -13`.

One full macro starting with weight `g` contributes

`S_11 = 7g/9`, `Z_00=2g/3`,

and scales `g` by `8/9`.

After any number of complete macros, and allowing the alternative same-bit even exit at any of the three phases before the forced `01`, the total pre-first-energy masses satisfy strictly

`S_11 < 7`, `Z_00 < 6`.

Hence the safe survivor must carry, **after its first positive-energy `01`**, at least

`S_11 > 31/12`,

`Z_00 > 11/12`.

The safe prefix caps give, at height one,

- each `11` contributes `Delta S<17/45`;
- each `00` has `g<17/30`.

Consequently the survivor must contain at least

- 7 height-one `11` columns, and
- 2 height-one `00` columns

strictly after its first genuine excursion departure.

So the explicit survivor cannot escape the initial negative cycle and then remain above height one until the terminal descent. It must return to height one and execute at least nine zero-energy synchronized columns later in the path.

**Status:** analytic consequence of the certified `S>45/4`, `E<5/3` survivor bounds plus exact local-energy formulas; regression/certificate in `verify_rl50_defect_energy_localization.py`.
