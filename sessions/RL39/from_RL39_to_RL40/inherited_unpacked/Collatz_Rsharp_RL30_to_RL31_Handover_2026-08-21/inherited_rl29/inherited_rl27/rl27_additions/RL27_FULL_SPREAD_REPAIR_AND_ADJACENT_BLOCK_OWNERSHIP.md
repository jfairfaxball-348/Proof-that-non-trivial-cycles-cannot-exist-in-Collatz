# RL27 — full-spread repair and adjacent-block ownership in the exceptional cubic geometry

Date: 2026-08-21

## Status

Sections 1--5 are **ANALYTIC** under the inherited RL21--RL26 hypotheses stated below. The accompanying verifier is an **exact symbolic / finite sanity certificate** for the algebra, congruence tables, and threshold arithmetic; it is not a substitute for the analytic proofs.

This note does **not** close RL. It does two useful things:

1. repairs a specification gap in RL25/RL26: the notes define `Delta` using all three pairwise numerator differences, but their lattice verifier minimized only the two coordinates relative to `W`;
2. couples the surviving `R==91 mod288`, `G=12`, `H=4` geometry to block prefixes, block-end valuations, and a forced three-trajectory order braid.

The old RL25 lower bound remains valid, so this is a strengthening rather than a collapse of the previous proof frontier.

---

## 1. Full-spread repair

Retain the order-3 balanced notation

`B=2^b`, `Y=3^e`,

with block-start states

`R`, `x=R+G`, `y=R+H`,

and block numerators

`U=(B-Y)R+BG`,

`V=(B-Y)R+BH-YG`,

`W=(B-Y)R-YH`.

If the three blocks share `r` initial parity bits, write

`G=2^r N`, `H=2^r K`.

Then

`(U-W)/2^r = BN+YK`,

`(V-W)/2^r = BK+YK-YN`,

and, crucially,

> `(U-V)/2^r = B(N-K)+YN`.                                  (R27.1)

RL25 defined

`Delta=max(|U-V|,|V-W|,|W-U|)`,

but its verifier optimized only the first two `W`-referenced coordinates. In the `G>H` sector this can miss the true maximum.

### Full-spread lower bound in the `G>H` sector

Assume `N>K>0`. RL23 nonzero-mod-3 ownership gives

`3|N`, or `3|K`, or `3|(N-K)`.

Hence `(N,K)=(2,1)` is forbidden.

If `N>=4`, then

`BN+YK >= 4B+Y > 2B+3Y`

because `B>Y`.

If `N=3`, then `K=1` or `2`:

- at `(3,1)`, (R27.1) is exactly `2B+3Y`;
- at `(3,2)`, `BN+YK=3B+2Y>2B+3Y` because `B>Y`.

Therefore

> **If `G>H`, then `Delta >= 2^r(2B+3Y)`.**                 (R27.2)

The `H>G` orientation already had the same lower scale in RL25. Consequently the true orientation-independent full-spread statement is

> **`Delta >= 2^r(2B+3Y)`.**                                (R27.3)

At the universal `r=2` level,

> **`Delta >= 4(2B+3Y)`.**                                  (R27.4)

This is strictly stronger than the old `4(3B+Y)` hard-sector lower bound because the near-resonant branch has `B<2Y`.

### What happens to the old extremizer

The old coordinate extremizer `(N,K)=(3,1)` is still admissible, but its full spread is

`U-W=4(3B+Y)`,

`V-W=4(B-2Y)`,

`U-V=4(2B+3Y)`.

Since `B<2Y`, the last quantity is the largest. Thus `(3,1)` remains the weakest full-spread geometry, but the value is

> **`4(2B+3Y)`, not `4(3B+Y)`.**                             (R27.5)

The RL26 residue sieve remains strategically useful: `R==27 mod32` is still the unique weakest root residue, and it still attains its minimum at `(N,K)=(3,1)`. The corrected root-specific minima before the common factor `4` are

- `R==7 mod32`: `10B+6Y`;
- `R==15 mod32`: `4B+3Y`;
- `R==27 mod32`: **`2B+3Y`**;
- `R==31 mod32`: `7B+4Y`.

Thus the exceptional residue geometry remains `R==91 mod96`, and under the inherited weak-close package `R==91 mod288`; only the claimed sharp lower scale changes.

---

## 2. Immediate global-range consequence

RL25 proved the analytic upper bound

`Delta < Y[(4/5)e-3+3(2/3)^e]`.                              (R27.6)

Since `B>Y`, (R27.4) gives `Delta>20Y`. Hence a necessary condition is

`(4/5)e-3+3(2/3)^e >20`.

Exact arithmetic shows this first becomes possible at `e=29`. Therefore

> **every order-3 balanced survivor in the repaired full-spread regime has `e>=29`.**  (R27.7)

This is only a modest numerical strengthening and is not the main gain below.

---

## 3. Prefix-aware numerator floor in the exact `G=12,H=4` geometry

Now impose the inherited exceptional package

`R==91 mod288`, `G=12`, `H=4`.

Then modulo `32`,

`R==27`, `x=R+12==7`, `y=R+4==31`.

The RL26 five-bit sieve therefore fixes the three macroblock prefixes as

- block `U` from `R` to `x`: `11011`;
- block `V` from `x` to `y`: `11101`;
- block `W` from `y` to `R`: `11111`.

The middle block is especially useful. A length-`b`, weight-`e` word beginning `11101` has forced first-one positions

`0,1,2,4`.

For fixed total weight, `Q` is minimized by putting every remaining one as early as possible, at

`5,6,...,e`.

Because `B>Y` implies `b>e`, this configuration fits. A direct geometric-sum calculation gives

> **`V >= (35/27)Y - 2^(e+1)`.**                             (R27.8)

But the exact block equation at `G=12,H=4` is

`V=(B-Y)R+4B-12Y`.

Put `z=B/Y`. Dividing (R27.8) by `Y` yields

`R(z-1) >= 359/27 -4z -2(2/3)^e`.                            (R27.9)

RL25 has `z<46/45`, so

`R(z-1) > 1243/135 -2(2/3)^e`.                              (R27.10)

On the other hand RL25/RL24 give

`R(z-1)<23e/90`.                                             (R27.11)

Thus the exact exceptional geometry requires

`1243/135 -2(2/3)^e <23e/90`.                               (R27.12)

Exact rational checking shows (R27.12) fails for every `4<=e<=36` and first becomes possible at `e=37`. Therefore

> **`R==91 mod288`, `G=12`, `H=4` forces `e>=37`.**          (R27.13)

This is a genuinely coupled numerator/trajectory statement: it uses the exact balanced gap geometry to identify `V`, and the least-state residue geometry to raise the fixed-weight floor of the specific adjacent macroblock.

It still does not address the external-floor regime, where `e` is enormous.

---

## 4. Incoming valuation classes at the three balanced cuts

The exact root class also fixes useful block-end valuation data.

Let an odd phase `q` map under the odd shortcut to an odd endpoint `s` with valuation

`nu=v_2(3q+1)`:

`3q+1=2^nu s`.                                               (R27.14)

Every phase state is nonzero modulo `3`. Therefore

- integrality requires `2^nu s ==1 mod3`;
- `q` nonzero modulo `3` further requires `2^nu s !=1 mod9`.

Since `R==91 mod288`,

`R==1 mod9`, `x=R+12==4 mod9`, `y=R+4==5 mod9`.

Using the order-6 powers of `2 mod9` gives the exact incoming valuation classes

> **into `x`: `nu_x ==0 or 2 mod6`;**                        (R27.15)
>
> **into `y`: `nu_y ==3 or 5 mod6`.**                        (R27.16)

In particular

`nu_x>=2`, `nu_y>=3`.

For the inherited exceptional final return,

`z_close=(4R-1)/3`, `3z_close+1=4R`,

so

> **`nu_R=2` exactly.**                                      (R27.17)

Equivalently, the trailing full-parity zero runs at the three macroblock ends have distinct congruence types:

- before `x`: odd length `1 or 5 mod6`;
- before `y`: even length `2 or 4 mod6`;
- before `R`: exactly one zero.

This is the requested kind of adjacent-block valuation ownership. It does not by itself create a positive-density valuation gain, but it is additional structure absent from the independent local packing cores.

---

## 5. A forced three-trajectory braid and later re-crossing

The same prefixes give an exact dynamical interaction among the three balanced trajectories.

Let

`u_j=T^j(R)`,

`v_j=T^j(R+12)`,

`w_j=T^j(R+4)`.

The prefixes are

`u: 11011...`, `v:11101...`, `w:11111...`.

After the first five steps, direct affine calculation gives

`u_5=(81R+85)/32`,

`v_5=(81R+1045)/32`,

`w_5=(243R+1183)/32`.

Hence

> **`w_5 > v_5 > u_5`, with `v_5-u_5=30`.**                 (R27.18)

The `v,w` pair is more dramatic. Their first three bits agree (`111`), so their gap `8` becomes `27`. At the fourth bit they have opposite parity, and the order reverses:

> **`w_4-v_4=(27R+23)/8`.**                                 (R27.19)

Thus the exact small balanced gap forces an order-`R` separation immediately after the first divergence.

At the macroblock endpoint, however,

`u_b=x=R+12`,

`v_b=y=R+4`,

`w_b=R`,

so the final ordering is

> **`u_b>v_b>w_b`,**                                        (R27.20)

which is the complete reversal of (R27.18).

A same-parity step multiplies a pairwise difference by `1/2` or `3/2`, so it cannot change its sign. Therefore each inverted pair must undergo a later opposite-parity crossing. Since a single binary parity split can involve at most two of the three pairwise comparisons, the complete reversal from `w>v>u` to `u>v>w` requires

> **at least two distinct opposite-parity crossing steps after the forced five-bit prefix.**  (R27.21)

At each such crossing the RL21 first-divergence minimax lemma applies: among the pre/post pair one separation is at least `(2R+1)/3`, hence some involved phase is at least `(5R+1)/3`.

This is a genuinely nonlocal consequence: the later crossings are forced by the *endpoint permutation of the three full macroblocks*, not by a one-block residue table.

It is still only an `O(1)` number of forced high episodes. To affect the global packing coefficient one would need to promote this braid into a number of crossings growing with `e`, transport area, or valuation excess.

---

## 6. Proof-frontier correction

The following inherited statements remain safe:

- RL25/RL26 upper range bounds;
- the mod-32 least-state sieve;
- the localization of the weakest residue to `R==27 mod32` / `R==91 mod96`;
- the exceptional weak-close refinement `R==91 mod288`;
- the physical geometry `(G,H)=(12,4)` as the coordinate-minimal exceptional configuration.

The following wording should be retired/repaired:

- “`Delta=4(3B+Y)` at exact weak-vector equality”;
- “the old `4(3B+Y)` vector is sharp for the full pairwise range `Delta`.”

For the `Delta` defined in RL25, the correct exact full-spread value at `(G,H)=(12,4)` is

> **`Delta=4(2B+3Y)`.**                                     (R27.22)

The old verifiers passed because they checked `max(|U-W|,|V-W|)` rather than all three pairwise differences. This is a verifier/specification gap, not evidence that the stronger statement fails.

---

## 7. Next attack

The strongest new objects to exploit are now:

1. the exact sparse pair equation
   `U-V=4(2B+3Y)`;
2. the forced prefix triple `11011 / 11101 / 11111`;
3. the incoming valuation classes `(nu_x,nu_y,nu_R)` with `nu_y>=3` and `nu_R=2`;
4. the complete trajectory-order reversal, which forces at least two later opposite-parity crossings.

The most promising next theorem would make one of these scale with the macroblock size. Examples:

- prove that reconvergence from the forced order-`R` separation to gaps `12,8,4` requires `Omega(e)` parity-disagreement/valuation events;
- convert the exact sparse difference `U-V=4(2B+3Y)` plus the endpoint valuation classes into a proper-factor/resultant obstruction;
- show that the two later order crossings force repeated high-valuation blocks, giving a positive-density penalty in the RL24 supporting line.

Absent such a scaling statement, the new results narrow and strengthen the exceptional sector but do not close the order-3 bridge or RL.

Verifier: `verify_rl27_full_spread_adjacent_ownership.py`.
