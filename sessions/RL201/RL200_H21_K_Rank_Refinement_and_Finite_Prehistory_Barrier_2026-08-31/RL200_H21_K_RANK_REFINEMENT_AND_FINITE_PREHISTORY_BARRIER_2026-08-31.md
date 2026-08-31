# RL200 — H21 K-rank refinement and finite oriented-prehistory barrier

Date: 2026-08-31  
Incoming authority: RL199 at `d042bbd11529b7660c729a069a97d623c4a292de`.  
All physical conclusions remain conditional on the sole high branch `(37,0,23,-1)`.

## 0. Outcome and classification

RL200 attacks RL199's requested global selector for the oriented H21 lift `eta`.

It does **not** remove one of the four classes `eta=0,8,9,17 mod 18`.  Instead it obtains two
useful exact results:

1. a genuinely global K-potential consumer sharply reduces the H21 terminal-rank core, deleting
   `2,213,738,806` previously surviving necessary ranks; and
2. the most obvious finite oriented-prehistory continuation is proved insufficient unless it
   couples the two endpoints to a global datum.

This is a qualified structural advance rather than the requested class selection.

## 1. Frozen interface

Use the inherited constants

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,  
`R=2L-A=57079296007`, `p=65470613321`, with `pB=1 mod L`.

For canonical phase `i`, the mechanical rank is `r=iB mod L` and
`rho_i=2^floor(Ai/L)/3^i`.

Retain the full-period K corridor

`128081997553 < K_i < 146795909391`

and the inherited logarithmic defect

`delta=A ln2-L ln3`, `0<delta<2^-40`.

The binding H21 `{33,34,35}` family has terminal invariant

`T=7*3^35=350220815692997949`, `H=21`

and incoming necessary terminal core

`D=[23369453298,41775866136]`

with 14 inherited isolated deletions.

RL199 parameterizes the oriented `tau=34` pair by

`Y_0^-=2^34 eta-1`, `Y_0^+=2^34(eta+21)-1`

and proves

`011 <=> eta=0 mod 9`, `111 <=> eta=8 mod 9`,

with terminal sign positive iff `eta` is even.  The four necessary classes are
`0,8,9,17 mod 18`.

## 2. Exact terminal K as a function of mechanical rank

The inherited H21 terminal normalization gives the positive normalized p-gap

`Delta_H21 = T/2^21 = 7*3^35/2^21`.

RL199's orientation changes which endpoint reaches height 21, but not this common normalized gap.

Let `r` be a canonical terminal mechanical rank and let

`i = pr mod L`, `0<=i<L`.

Since `A=B+L`, the same rank is `Ai mod L`, so there is a unique integer `n` with

`Ai=nL+r`.

Therefore

`rho(r)=2^n/3^i`

and the exact terminal K value forced by that rank is

`K_H21(r)=rho(r) Delta_H21`.

This is a global absolute-rank constraint.  It is not the eta-blind common-gap normalization by
itself: the nontrivial information is the rank-dependent mechanical weight `rho(r)` together with
the global K corridor.

## 3. Strict reverse-rank ordering

For canonical ranks `r<s`, write inverse phases `i_r,i_s`.  From
`Ai=nL+r`,

`ln rho(r)-ln rho(s)
 = ((i_r-i_s)delta + (s-r)ln2)/L`.

Because `|i_r-i_s|<L` and `s-r>=1`,

`ln rho(r)-ln rho(s)
 > (ln2-L delta)/L`.

The inherited `delta<2^-40` gives `L delta<ln2`; the exact verifier checks this with rigorous
rational logarithm enclosures.  Hence

**`rho(r)` and therefore `K_H21(r)` are strictly decreasing in rank.**

This turns the K-corridor test into one exact interval crossing rather than a scan.

## 4. Exact K-corridor crossing and refined H21 core

Let

`Klo=128081997553`, `Khi=146795909391`.

Exact rational logarithm bounds give

- `K_H21(25583192105) > Khi`;
- `K_H21(25583192106) < Khi`;
- `K_H21(41775866136) > Klo`.

Strict rank monotonicity then proves that the incoming H21 core survives the K corridor exactly on

**`D_K=[25583192106,41775866136]`.**

The interval contains `16,192,674,031` integer ranks.

The inherited 14 H21 isolated deletions were

`23369453298, 23783761791, 26058127773, 26058127774, 28746802249,
28746802250, 31435476726, 34124151202, 36398517184, 36398517185,
36812825678, 39087191660, 39087191661, 41775866136`.

Exactly the first two are already below the new lower endpoint, leaving 12 inherited deletions
inside `D_K`.  Thus the refined necessary-rank count is

`16,192,674,031 - 12 = 16,192,674,019`.

The previous post-deletion count was `18,406,412,825`, so RL200 newly removes

**`2,213,738,806` previously surviving necessary ranks.**

These are certificate-state ranks, not physical terminal counts.

## 5. Rank-resolved prehistory geometry

Chronological phase advance adds `B` to mechanical rank.  Over `D_K`:

- the `tau=34` start rank `(r-34B) mod L` lies in
  `[40886621976,57079296006]`, ending exactly at `R-1`;
- one source before the `tau=35` start, `(r-36B) mod L`, lies in
  `[17517168678,33709842708]`, entirely below `R`;
- the next earlier source, `(r-37B) mod L`, lies in
  `[74596464685,90789138715]`, entirely above `R`.

Hence the first two genuinely new backward prehistory mechanical bits are fixed:

`c_(t-36)=1`, `c_(t-37)=2`.

This is stronger phase information than RL199 had, but by itself it still does not determine
`eta mod 18`.

## 6. Exact finite reverse-prehistory insufficiency theorem

Suppose a current physical odd state is a positive unit `y` modulo 3, has height `h>=0`, and the
preceding mechanical bit is prescribed as `c in {1,2}`.

A reverse accelerated predecessor with exponent `a>=1` is

`x=(2^a y-1)/3`.

It is an odd integer exactly when

`2^a y = 1 mod 3`.

To remain a unit modulo 3 we additionally require

`2^a y != 1 mod 9`.

Powers of two modulo 9 have period six.  For either unit residue class of `y mod 3`, the
integrality condition selects three exponent classes modulo 6; exactly one of those makes the
numerator divisible by 9.  Thus **exactly two exponent classes modulo 6 are safe**.

Each safe class has arbitrarily large positive representatives.  Choosing `a` sufficiently large
also makes the predecessor height

`h_prev=h+a-c`

nonnegative, or above any prescribed finite lower bound.

Therefore the construction can be iterated through any finite prescribed mechanical-bit word.
It applies separately to both endpoints of every RL199 H21 oriented class.  Representative
terminal-compatible choices are

- class `0`: `eta=18`, terminal `nu=1`;
- class `8`: `eta=8`, terminal `nu=2`;
- class `9`: `eta=9`, terminal `nu=4`;
- class `17`: `eta=17`, terminal `nu=3`.

The exact verifier extends each representative through a finite rank-compatible reverse word.

So a finite consumer that only asks each endpoint independently to satisfy reverse odd
integrality, unit-mod-3 status, nonnegative height and the actual local mechanical bits is
**provably class-blind**.

This theorem does not cover coupled global information.  In particular it does not permit the
two endpoints to choose reverse exponents independently if a complete defect word, common
numerator, fixed global height word, exact p-chain position, or fixed-K moment couples them.

## 7. Why the terminal K consumer also does not select eta

The new rank cut is useful but terminal `K_H21(r)` contains no eta.  At a fixed terminal rank,
all four RL199 classes share the same terminal normalized p-gap and the same mechanical weight.

RL199's first eta-sensitive K datum remains the **next** signed increment

`K_next-K_terminal = ±rho(2^nu-1)/(3*2^21)`.

RL200 has not inherited or proved a subunit rank-resolved successor interval sharp enough to
consume that sign.

Thus the two tested consumers divide cleanly:

- global terminal K: strong rank localization, no eta bit;
- finite uncoupled reverse prehistory: exact local extendability, no eta bit.

## 8. Classification and next datum

New proved analytic mathematics:

1. exact rank-resolved H21 terminal K law and strict reverse-rank ordering;
2. refined H21 K-compatible core `[25583192106,41775866136]`;
3. exact reduction to `16,192,674,019` necessary ranks after inherited deletions;
4. fixed first two extra prehistory mechanical bits `1,2`;
5. exact finite uncoupled reverse-prehistory insufficiency theorem.

Exact finite certificate:
`verification/verify_rl200_h21_k_rank_and_prehistory.py`.

The next attack must couple the absolute lower endpoint

`Y_0^-=2^34 eta-1`

to a **global absolute-position datum**.  Preferred targets are a complete p-shift-chain/fixed-K0
moment reconstruction at the refined rank, a coupled reverse defect/numerator word, or an exact
rank-resolved successor-K constraint capable of resolving RL199's signed subunit increment.

No H21 class is excluded, no charge is released, and all branch/Gate/global obligations remain
open.
