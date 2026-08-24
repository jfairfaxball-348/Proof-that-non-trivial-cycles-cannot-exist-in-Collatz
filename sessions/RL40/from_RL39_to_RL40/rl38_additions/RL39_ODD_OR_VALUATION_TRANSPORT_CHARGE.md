# RL39 — odd-or-valuation transport charging inside every maximal excursion

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** in the inherited near-resonant `g=2` balanced-return branch. The bundled verifier is an **EXACT FINITE / SYMBOLIC sanity certificate** over all canonical positive excursions through transport area 15.

This note does **not** close RL. It supplies the missing local mechanism needed to convert RL36's high unsynchronized **full-parity columns** into a controlled collection of genuine odd correction phases even when many high columns lie inside one long halving chain.

## 1. Setup on one excursion

Let `E=[s,t]` be a maximal excursion of length

`h=t-s`,

common odd weight `p`, and local transport area

`r=sum_(s<=j<t) |d_j|`.

Choose the **leading trajectory**:

- for a positive excursion `d_j>0`, use the `v` trajectory;
- for a negative excursion `d_j<0`, use the `u` trajectory.

Write its local odd positions as

`0=i_1<i_2<...<i_p<h`.

The first position is odd because the excursion opens by the leading word taking bit `1` while the lagging word takes bit `0`.

Define interval lengths

`l_k=i_(k+1)-i_k` for `k<p`,

`l_p=h-i_p`.

Then

> **`sum_k l_k=h`.**                                      (R39.1)

For `k<p`, `l_k` is exactly the outgoing odd-map valuation of the leading odd state at `i_k`; for the final selected odd state it is at most its full outgoing valuation. Hence if `nu_k` is the genuine outgoing valuation,

> **`1<=l_k<=nu_k`.**                                     (R39.2)

So the excursion columns are partitioned among distinct owned odd states with multiplicities that are paid by genuine `2`-adic valuation.

## 2. Column depth forces the preceding odd state high

Let `y_k` be the leading odd state at local position `i_k`, and put

`alpha=log_3(2)`,

`H_k=log_3( ((3y_k+1) z)/R )`.                            (R39.3)

Consider a column

`j=i_k+q`, `0<=q<l_k`.

For `q>=1`, there is no intervening odd state on the leading trajectory, so exactly

`y_j=(3y_k+1)/2^q`.                                       (R39.4)

Every interior excursion column has nonzero prefix imbalance. RL36 gives

`y_j >= 3^(|d_j|) R/z`.                                   (R39.5)

Combining (R39.4)--(R39.5), for `q>=1`,

> **`|d_j| + q alpha <= H_k`.**                            (R39.6)

For `q=0` and `k>1`, RL36 gives directly `y_k>=3^(|d_j|)R/z`, hence in fact `H_k>|d_j|+1`; the weaker R39.6 again holds. At the first excursion column, `d_s=0`, so R39.6 is trivial there as well.

Thus every unsynchronized column is charged to its preceding owned odd state, and the charge strengthens with distance down its halving chain.

## 3. Exact odd-or-valuation area inequality

Sum R39.6 over the `l_k` columns assigned to `y_k`:

`sum_(q=0)^(l_k-1) |d_(i_k+q)|`
` <= l_k H_k - alpha l_k(l_k-1)/2`.

Summing over the excursion gives

> **`r <= sum_(k=1)^p [ l_k H_k - alpha l_k(l_k-1)/2 ].`** (R39.7)

This is the desired odd-or-valuation conversion.

Interpretation:

- transport depth forces `H_k`, hence the genuine odd state `y_k`, upward;
- transport length hidden behind one odd state forces `l_k` upward;
- but concentrating many columns at one odd state incurs the negative quadratic term
  `alpha l_k(l_k-1)/2`, so a long valuation chain can support the area only if its originating odd state is exponentially higher.

The unbounded-multiplicity objection from RL30 is therefore handled explicitly rather than ignored.

## 4. Direct correction-factor consequence

From the definition of `H_k`,

`3y_k = R 3^(H_k)/z - 1`,

so

> **`R/(3y_k) = z/(3^(H_k)-z/R)`.**                        (R39.8)

Using `log(1+t)<=t`, each owned odd correction satisfies

> **`R log(1+1/(3y_k)) <= z/(3^(H_k)-z/R)`.**              (R39.9)

Thus R39.7 is immediately a constrained optimization bound on the actual odd-step correction product, not merely on phase heights.

There are also useful valuation-only floors on `H_k`.

### First owned odd state

RL36 proved

`y_1 >= 2R/z - 1/3`.

Therefore

> **`H_1 >= log_3(6)`.**                                  (R39.10)

If `l_1>=2`, the last charged column is interior with `|d|>=1`, so R39.6 also gives

`H_1 >= 1+(l_1-1)alpha`.

### Later owned odd states

For every `k>1`, the odd state itself lies at nonzero imbalance, so

`y_k>=3R/z`,

which gives

> **`H_k>2`.**                                            (R39.11)

If `l_k>=2`, again the last charged column gives

> **`H_k >= 1+(l_k-1)alpha`.**                            (R39.12)

Consequently long outgoing valuations automatically suppress the correction factor of their originating owned odd state geometrically.

For example, for `k>1`, combining R39.8, R39.11, and R39.12 yields

`R log F(y_k)`
` <= min( z/(9-z/R), z/(3*2^(l_k-1)-z/R) )`.              (R39.13)

The first state has the analogous bound with `6` replacing the `9` floor from R39.10.

## 5. Global excursion sum

Apply R39.7 to every maximal excursion. Their leading odd states are distinct cycle phases, and their assigned column intervals are disjoint. If `O_exc` denotes the resulting owned odd-state set, with assigned lengths `l_y`, then

> **`rho <= sum_(y in O_exc) [ l_y H_y - alpha l_y(l_y-1)/2 ]`,** (R39.14)

where

`H_y=log_3(((3y+1)z)/R)`,

and

`sum_(y in O_exc) l_y = H_exc`,                            (R39.15)

with `H_exc` the total number of full-parity columns lying in excursions.

Also `l_y<=nu(y)`, so

> **`H_exc <= sum_(y in O_exc) nu(y) <= A`.**              (R39.16)

By Cauchy,

`sum l_y(l_y-1)/2`
` >= (H_exc^2/|O_exc|-H_exc)/2`                            (R39.17)

when `O_exc` is nonempty. This gives a coarse global form

`rho`
` <= sum l_y H_y`
`    - (alpha/2)(H_exc^2/|O_exc|-H_exc)`.                  (R39.18)

R39.14 is stronger and should be used for optimization; R39.18 makes the anti-concentration mechanism explicit.

## 6. Strategic meaning

RL36's aggregate inequality

`sum_(d_j!=0) log_3(max(u_j,v_j)/R) >= rho-H log_3(z)`

was not yet a product theorem because many high full-parity columns could trace back to one odd state with a large outgoing valuation.

R39 resolves exactly that bookkeeping gap:

- every excursion column is assigned to a genuine owned odd state;
- the assignment multiplicity is bounded by that state's actual outgoing valuation;
- concentration into one valuation chain forces an additional quadratic height cost;
- the resulting height variable `H_y` controls the genuine correction factor directly through R39.8--R39.9.

Together with RL38, the `g=2` branch now has both missing interfaces:

1. synchronized runs are removed from the scaled-gap motion exactly;
2. unsynchronized full-parity area is converted to odd-state/valuation product currency exactly.

The next quantitative task is a global optimization combining R39.14 with the exact valuation identity `sum nu=A` and the near-resonant relation `A/L=log_2 3 + log(lambda)/(L log2)`. The target is a linear supporting inequality in `(rho,H_exc,log lambda)` strong enough to overlap the RL38 effective-excursion alternative.

