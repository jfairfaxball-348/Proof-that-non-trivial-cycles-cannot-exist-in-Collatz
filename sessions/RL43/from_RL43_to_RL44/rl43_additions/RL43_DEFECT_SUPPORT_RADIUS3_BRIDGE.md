# RL43 — defect-support compression and the radius-3 resultant gateway

Date: 2026-08-22

## Status

Sections 1–5 are **ANALYTIC** in the inherited near-resonant order-2 / `g=2` balanced-return branch. The companion verifier exhausts all equal-weight half-word pairs through length 9 as a finite sanity certificate; it is not the proof.

This note does **not** close RL or the surviving `g=2` branch. It gives a new exact bridge from arbitrary transport radius to sparse exponential algebra, controlled by excursion **excess plus excursion count**, rather than raw transport area or moved-rank mass.

The new complexity is

`K_def := E + N`,

where `E=sum_E e_E` is total excursion excess and `N` is the number of maximal excursions.

The main theorem is:

> **The proper-factor numerator `U-V=(X+Y)G` has a signed `2`–`3` monomial representation with at most `4 K_def` terms before collection.**

Thus a single excursion can move an arbitrarily large number of odd ranks while remaining fixed-support whenever its excess is bounded. This is precisely the concentration regime not controlled by the earlier packing inequalities.

## 1. Setup

Retain

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`,

with equal-weight half words `u,v` of length `a` and weight `ell`, and

`U=Q(u)`, `V=Q(v)`,

`(X+Y)G=U-V`.

Let

`d_j=p_v(j)-p_u(j)`

be the aligned prefix-count difference. Decompose its nonzero support into maximal excursions `E`.

For one excursion let

- `h_E` = excursion length;
- `p_E` = common odd weight of its two local words;
- `rho_E=sum |d_j|` over the internal excursion columns;
- `e_E=rho_E-p_E >=0` = transport excess.

Put

`E_tot=sum_E e_E`, `N=# excursions`,

and

`K_def=E_tot+N`.

## 2. Excess bounds the number of zero columns

Let an excursion have length `h`, common weight `p`, and therefore

`z=h-p`

zero bits in each local word.

Every internal excursion column has nonzero prefix imbalance, hence absolute imbalance at least one. There are `h-1` internal columns between departure and return, so

`rho_E >= h-1`.

Therefore

`e_E=rho_E-p >= h-1-p = z-1`,

or

> **`z <= e_E+1`.**                                      (R43D.1)

This is cutoff-free and purely combinatorial.

## 3. Every 1-run is a two-monomial object

For a binary word `w` of weight `p`, write its ordered odd positions as usual. Consider one maximal consecutive run of `k` ones beginning at bit position `t` and beginning at odd rank `m` (one-based).

Its contribution to `Q(w)` is

`sum_(s=0)^(k-1) 3^(p-m-s) 2^(t+s)`

`= 2^t 3^(p-m-k+1) (3^k-2^k)`

`= 2^t 3^(p-m+1) - 2^(t+k) 3^(p-m-k+1)`.                 (R43D.2)

Hence every maximal 1-run contributes exactly two signed pure `2^i 3^j` monomials.

In a canonical excursion, one local word starts with `0` and the other ends with `0`. Since each word has `z` zeros, each has at most `z` maximal 1-runs. Thus their local numerator difference `D_E` has a representation with at most

`2z+2z = 4z <= 4(e_E+1)`                                  (R43D.3)

signed monomials before collection.

This bound is independent of `p_E`, `h_E`, and `rho_E`.

## 4. Global defect-support theorem

Suppose excursion `E` begins at global bit position `s_E`, after `c_E` common odd ranks, and has local common weight `p_E`. Put

`q_E=ell-c_E-p_E`,

the number of global odd ranks after that excursion.

The ordered-rank formula for `Q` gives the exact excursion decomposition

`U-V = sum_E sigma_E 2^(s_E) 3^(q_E) D_E`,                (R43D.4)

where `sigma_E=+1` or `-1` according to excursion orientation.

Insert the run compression (R43D.3). Before collecting equal monomials, the total support is at most

`sum_E 4(e_E+1)`

`=4(E_tot+N)`.

Therefore:

> ## **RL43 defect-support theorem**
>
> **`(X+Y)G=U-V` admits an exact signed representation**
>
> `U-V = sum_(nu=1)^S eps_nu 2^(r_nu) 3^(s_nu)`,
>
> **with `eps_nu in {+1,-1}` and**
>
> **`S <= 4(E_tot+N)`.**                                  (R43D.5)

After collection the support can only decrease.

This strictly strengthens the earlier moved-rank support bound in the dangerous regime of a few very long excursions. RL42 gave support at most `2P`, where `P` is moved-rank mass; R43D.5 instead depends on the defect complexity `E_tot+N`.

### Example: why this is genuinely different

The retained RL21 `X+Y`-factor countermodel has one excursion with

`p=39`, `rho_E=170`, `e_E=131`, `N=1`.

So it is not low-defect: `K_def=132`. The companion verifier finds compressed support 66. This is consistent with the theorem and explains why that countermodel does not undermine the low-defect bridge.

## 5. Exact gateway to radius-3-style resultant algebra

Let `F=X+Y=2^a+3^ell`.

From (R43D.5), form the integer polynomial

`f(T)=sum eps_nu 3^(s_nu) T^(r_nu)`,                       (R43D.6)

with degree at most `a-1`, so

`f(2)=U-V=FG`.                                             (R43D.7)

Hence modulo `F`, the residue `T=2` is a common root of

`B(T)=T^a+3^ell`

and `f(T)`.

Therefore

> **`F | Res(B,f)`.**                                      (R43D.8)

In the reduced `g=2` branch, `gcd(a,ell)=1`. The one-segment 3-adic Newton polygon of `T^a+3^ell` has coprime horizontal/vertical increments, so the standard Eisenstein–Dumas/Newton-polygon criterion makes `B` irreducible over `Q`. Since `f` is nonzero and `deg f<a`, the resultant in (R43D.8) is nonzero.

Thus every low-defect surviving balanced return produces a **nonzero sparse resultant divisible by the proper cyclotomic factor `X+Y`**.

This is the first exact point in the RL36–RL43 line at which the arbitrary-radius branch enters the same kind of sparse resultant setting used in the repaired radius-3 proof.

### Important limitation

The inherited radius-3 theorem cannot simply be invoked verbatim.

For the half rotation,

`Q(vu)-Q(uv)=(X-Y)(U-V)=DG`.                               (R43D.9)

Multiplying the sparse polynomial `f(T)` by `T^a-3^ell` gives a sparse polynomial whose value at `2` is a multiple of the full denominator `D`. But this polynomial shares the exact complex factor `T^a-3^ell` with

`T^(2a)-3^(2ell)`.

So the naive full-`D` resultant is identically zero. This is the precise algebraic reason the already-closed radius-3 theorem does not automatically close the half-rotation branch.

The live bridge is therefore sharper:

> **Use the sparse proper-factor resultant (R43D.8), or construct a second synchronized sparse relation whose combination removes the forced `T^a-3^ell` factor and restores a nondegenerate full-`D` resultant.**

That is a concrete algebraic target, not a generic request for “some bridge to radius 3”.

## 6. One-excursion specialization

The new theorem is especially strong when `N=1`.

In the inherited `G=4` branch, first disagreement occurs after `v2(G)=2` common bits. The near-minimum odd states are `3 mod 4`, so those two common bits are odd. The terminal common suffix has odd weight at most `v3(G)=0`.

Hence a one-excursion return has

`p=ell-2`                                                   (R43D.10)

and the global proper-factor relation becomes

`4 D_E=4(X+Y)`,

so

> **`D_E=X+Y`.**                                           (R43D.11)

The physical gap after the two common odd steps is

`4 -> 6 -> 9`,

so the unique excursion starts with incoming gap `9` and must cross to the negative side.

The new local kick bound from RL43 gives

`D_E/3^p < 2^(e_E+1)`.

But using (R43D.10)–(R43D.11),

`D_E/3^p = (2^a+3^ell)/3^(ell-2)`

`=9(z+1) >18`,

where `z=2^a/3^ell>1`.

Thus every genuine one-excursion return satisfies the analytic floor

> **`e_E >=4`.**                                          (R43D.12)

More importantly, for fixed `e_E` equation (R43D.11) is a fixed-support sparse representation of the entire proper factor `X+Y`, with support at most `4(e_E+1)` independently of `ell`. This is an attractive first branch on which to transplant the radius-3 resultant/LMN strategy.

A targeted exact 2-adic scan performed in this session found no incoming-gap-9 crossing with `e<=7` through `p<=240`; the first observed family occurs at `e=8`. This is **exploratory finite evidence only**, not an infinite theorem, and is not used in any claimed proof above.

## 7. Strategic consequence

The order-2 branch now has three genuinely different complexity controls:

1. **Moved-rank spread `P`:** large `P` owns many distinct high odd states (RL36/RL42 packing side).
2. **Excess `E`:** large excess directly reduces arithmetic efficiency in the RL42 effective-mass inequality.
3. **Defect support `K_def=E+N`:** small excess carried by only a few excursions gives a sparse proper-factor resultant irrespective of how large `P` or `rho` are.

The third item attacks exactly the “one or a few sacrificial long excursions” concentration pattern that survived the earlier global packing optimization.

The next high-value theorem is now explicit:

> **Fixed-defect sparse uniqueness target.** For fixed `K`, rule out the nonzero resultant congruence (R43D.8) under the near-resonant slope and endpoint ownership conditions; start with `N=1`, then `N=2`.

A successful fixed-`K` theorem would be a genuine radius-3-to-arbitrary-radius bridge: radius 3 would no longer be used as a literal distance bound, but as the base case/methodology for a sparse-resultant obstruction whose support is controlled by the new defect complexity.

## 8. Verification

Companion verifier:

`verify_rl43_defect_support_radius3_bridge.py`

Fresh output:

```text
RL43 defect-support / radius-3 bridge verifier: PASS
equal-weight word pairs exhausted through n = 9
pairs checked = 66196
analytic support inequality sanity: support <= 4(E+N)
max observed support/(E+N) = 4.0
RL21 gap-factor countermodel excursion: p=39, rho=170, e=131, N=1
countermodel compressed support = 66 pre-collection bound = 66
```

The finite run checks the combinatorial identities only. The proof of (R43D.1)–(R43D.8) is analytic as written above.
