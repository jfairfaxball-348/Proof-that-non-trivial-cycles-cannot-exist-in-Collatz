# Collatz R# RL-3 Seed — Root Xi Sparsity and Relative-Height Entry Amplification

**Date:** 2026-08-19  
**Branch:** RL / hypothetical least red integer eventually entering a nontrivial cycle  
**Session target:** begin the relative height/rotation/xi-probe phase from the RL-2 handover  
**Verdict:** RL remains open. Two next-phase structural results are obtained: (i) the full k=0 root xi-ceiling sieve is proved too sparse to close the branch, even after the inherited mod-144 root restrictions; (ii) the k>0 entry split has an exact factor-of-`4^m` height amplification and a relative-order crossing law.

## 1. Reproduction and scope

The inherited RL-2 verifier was rerun and passes. The new verifier

`tools/verify_rl3_rootxi_relative.py`

also passes. It audits the finite consequences of the results below. The analytic claims are proved here; the verifier is not a proof of absence of nontrivial Collatz cycles.

## 2. k=0 notation

In the `k=0` branch, `R#=C_min`, `R#=1 (mod 3)`, and every legal inverse exponent from `R#` is even. For even `d>=2`, put

`q_d(R#)=v3(2^(d-1)R#+1)`

and

`Q_d=floor((d-1) log(2) / log(3/2))`.

RL-L16 gives the necessary root ceiling

`q_d(R#) <= Q_d`.

A violation means `q_d>=Q_d+1`.

## 3. RL-L18 — every root xi violation is one explicit 3-adic cylinder

For each even `d`, the violation set is exactly

`R# = -2^(1-d) (mod 3^(Q_d+1))`.

So each probe excludes one and only one residue cylinder at its own 3-adic depth.

Reducing that bad cylinder modulo 9 gives the exact three-cycle

- `d=2 (mod 6)` -> bad root class `R#=4 (mod 9)`;
- `d=4 (mod 6)` -> bad root class `R#=1 (mod 9)`;
- `d=0 (mod 6)` -> bad root class `R#=7 (mod 9)`.

The inherited six `k=0` classes modulo 144 have `R# mod 9` only in `{1,7}`. Therefore:

- in the `R#=1 (mod 9)` branch, only probes `d=4 (mod 6)` can ever violate a ceiling;
- in the `R#=7 (mod 9)` branch, only probes `d=0 (mod 6)` can ever violate a ceiling;
- all probes `d=2 (mod 6)` are automatically harmless after the inherited mod-9 restriction.

**Status: PROVED ANALYTIC THEOREM.**

### Proof

`q_d>=Q_d+1` is equivalent to

`3^(Q_d+1) | 2^(d-1)R#+1`,

and `2` is a unit modulo every power of 3, giving the unique stated residue. Modulo 9, the inverse powers of 2 have period 6, which gives the three listed classes.

## 4. RL-G7 — the infinite k=0 xi-ceiling sieve has positive-measure survivors

Let the Haar measure inside either fixed mod-9 root cylinder be normalized to 1.

Set

`alpha=log(2)/log(3/2)`.

Since

`3^5=243 < 256=2^8`,

we have `alpha>5/3`.

### Branch `R#=1 (mod 9)`

Only `d=6j+4` can violate. Then

`Q_d >= floor((5/3)(6j+3)) = 10j+5`.

A bad cylinder modulo `3^(Q_d+1)` occupies relative measure `3^(1-Q_d)` inside a fixed mod-9 cylinder. Hence the total relative bad mass is at most

`sum_{j>=0} 3^(-10j-4) = 729/59048 < 0.012346`.

Thus the all-probe survivor set has relative 3-adic measure at least

`58319/59048 > 0.987654`.

### Branch `R#=7 (mod 9)`

Only `d=6j+6` can violate. Then

`Q_d >= floor((5/3)(6j+5)) = 10j+8`,

so the total relative bad mass is at most

`sum_{j>=0} 3^(-10j-7) = 27/59048 < 0.000458`.

Thus the survivor set has relative measure at least

`59021/59048 > 0.999542`.

Therefore the entire infinite family of RL-L16 root xi ceilings cannot cover either inherited mod-9 root branch. By CRT, fixing the corresponding mod-16 component of any of the six inherited mod-144 classes does not change this 3-adic conclusion.

This is an infinite extension statement, but it is an **obstruction to the route**, not an RL exclusion: root xi ceilings alone leave a large inverse-limit survivor set.

**Status: FAILED / REFUTED ROUTE for “all root xi ceilings + inherited root residues close k=0”.**

## 5. RL-L19 — explicit integer families cover all six inherited k=0 root classes and satisfy every root xi ceiling

The preceding positive-measure result is 3-adic. There is also an explicit ordinary-integer compatibility theorem.

Let `M>=4` be a multiple of 4. Then `3^M=0 (mod 9)` and `3^M=1 (mod 16)`.

Consider the six families

### `R=A*3^M-2`

- `A=25` -> `R=7 (mod 144)`;
- `A=13` -> `R=43 (mod 144)`;
- `A=1` -> `R=79 (mod 144)`.

### `R=A*3^M+1`

- `A=22` -> `R=55 (mod 144)`;
- `A=10` -> `R=91 (mod 144)`;
- `A=14` -> `R=127 (mod 144)`.

Every member is odd, is `1 (mod 3)`, is `3 (mod 4)`, lies in one of the six inherited `k=0` classes, and satisfies

`q_d(R) <= Q_d`

for **every even `d>=2`**.

Since `M` is unbounded, every one of the six inherited mod-144 classes contains arbitrarily large ordinary integers satisfying all root xi ceilings. In particular these families eventually exceed any fixed computational lower bound such as `2^71`.

**Status: PROVED ANALYTIC THEOREM.**

### Proof for `R=A*3^M-2`

Here `A` is a positive 3-adic unit and `A<=25`. For even `d`,

`2^(d-1)R+1 = A*2^(d-1)*3^M - (2^d-1)`.

By LTE,

`t:=v3(2^d-1)=1+v3(d/2)`.

If `t<M`, then `q_d=t`; if `t>M`, then `q_d=M`. In both cases `q_d<=d-1<=Q_d`, since `alpha>1`.

If `t=M`, then `d>=2*3^(M-1)`. For `M>=4`, this implies `d>3M+7`. Also

`2^(d-1)R+1 < 25*2^(d-1)*3^M < 2^(d-1)*3^(M+3)`.

Using `2^3<3^2` and `d>3M+7`, the last quantity is `<3^d`. Hence `q_d<d`, so again `q_d<=d-1<=Q_d`.

### Proof for `R=A*3^M+1`

Here `A` is again a positive 3-adic unit and `A<=22`. For even `d`,

`2^(d-1)R+1 = A*2^(d-1)*3^M + (2^(d-1)+1)`.

Since `d-1` is odd, LTE gives

`t:=v3(2^(d-1)+1)=1+v3(d-1)`.

If `t<M` or `t>M`, the same unequal-valuation argument gives `q_d=min(t,M)<=d-1<=Q_d`.

If `t=M`, then `d>=3^(M-1)+1`, which for `M>=4` again gives `d>3M+7`. Moreover

`2^(d-1)R+1 < 2^(d-1)(A*3^M+2) < 2^(d-1)*3^(M+3) < 3^d`.

Thus `q_d<=d-1<=Q_d`.

## 6. Consequence for the k=0 roadmap

The Rank-2 root-side xi program is now classified more sharply:

- using **all** root probes is stronger than any finite probe list;
- nevertheless, even the infinite family is compatible with every inherited mod-144 root class;
- the exact neutral-run theorem does not itself remove these families—it records a 2-adic length once the root is chosen;
- therefore a k=0 exclusion must use a genuinely cycle-coupled condition: minimum rotation, common denominator/integrality across rotations, or a cycle-wide xi profile tied to the exponent word.

Root arithmetic alone is not enough.

## 7. RL-L20 — exact entry predecessor amplification for k>0

Now assume `k>0`. Let

`d=b_(k-1)`, `e=a_(L-1)`

be the immediate preperiod and cycle predecessor exponents into the common entry `c0`. RL-L14 gives

`d!=e` and `d=e (mod 2)`.

Write `|d-e|=2m` with `m>=1`. Let

`x=r_(k-1)=(2^d c0-1)/3`,

`y=c_(L-1)=(2^e c0-1)/3`.

If `d>e`, then exactly

`x = 4^m y + (4^m-1)/3`.

If `e>d`, then exactly

`y = 4^m x + (4^m-1)/3`.

Thus the two physical predecessor branches are not merely distinct: the larger is more than `4^m` times the smaller. In the minimum possible exponent gap `|d-e|=2`, the larger predecessor is exactly `4*smaller+1`.

**Status: PROVED ANALYTIC THEOREM.**

## 8. RL-L21 — relative-order recurrence and crossing certificate

Unwrap the cycle backwards periodically. Let

- `x_h=r_(k-h)` be the tail branch;
- `y_h=c_(-h mod L)` be the cycle branch;
- `d_h=b_(k-h-1)` and `e_h=a_(-h-1 mod L)` be the next reverse exponents;
- `Delta_h=x_h-y_h`.

Then exactly

`3 Delta_(h+1) = 2^(d_h) Delta_h + (2^(d_h)-2^(e_h)) y_h`.

Equivalently,

`x_(h+1) < y_(h+1)  <=>  2^(d_h)x_h < 2^(e_h)y_h`.

Two monotonicity rules follow immediately:

- if `Delta_h>=0` and `d_h>=e_h`, then `Delta_(h+1)>=0`;
- if `Delta_h<=0` and `d_h<=e_h`, then `Delta_(h+1)<=0`.

Since `Delta_0=0` and

`Delta_k=R#-y_k<0`

because every cycle state is `>R#` in the strict-preperiod branch, every valid `k>0` tail must contain at least one reverse phase with

`d_h<e_h`.

If the entry orientation has `d>e`, then `Delta_1>0`, so there must be a later first crossing phase at which `d_h<e_h` and

`x_h/y_h < 2^(e_h-d_h)`.

This is the first exact rotation-relative order law in the RL branch.

**Status: PROVED ANALYTIC THEOREM.**

## 9. RL-L22 — contraction debt when the tail is the larger entry branch

Continue with `k>0`, and suppose the entry exponent satisfies

`d-e=2m>0`.

By RL-L20 and `y=c_(L-1)>=C_min>R#`,

`(x+1)/(R#+1) > 4^m`.

For the normalized tail height

`u=(state+1)/(R#+1)`,

RL-L15 gives:

- a reverse exponent `1` maps `u -> (2/3)u` exactly;
- every reverse exponent `>=2` strictly increases `u` while the tail remains above `R#`.

Let `N_1` be the number of reverse exponent-1 moves after the entry predecessor and before reaching `R#`. Since the final normalized height is exactly 1,

`1 >= u_1 (2/3)^(N_1) > 4^m (2/3)^(N_1)`.

Therefore

`N_1 > m * log(4)/log(3/2)`.

Equivalently,

`N_1 >= floor(m*log(4)/log(3/2)) + 1`.

In particular the minimum entry gap `d-e=2` forces at least four later exponent-1 contractions.

This converts the entry orientation into a quantitative tail budget that can be fused with prefix slack and cycle phase.

**Status: PROVED ANALYTIC THEOREM.**

## 10. Current endpoint

RL is **not solved**. The next phase is narrower than at handover:

1. **k=0:** do not spend further effort on root-only xi ceilings. They admit large 3-adic survivor sets and explicit arbitrarily large integer witnesses in all six root classes. The next indispensable variable is cycle coupling.
2. **k>0:** promote the state from raw sign to `(cycle phase, relative order/ratio interval, entry orientation, contraction debt, prefix slack)`. RL-L20/L21/L22 provide exact transitions and a nontrivial initial condition.
3. **Cycle-wide xi:** apply probes to actual cycle states/rotations, where periodic product and minimum constraints can couple the 3-adic valuations to the exponent word. That coupling is not present in the refuted root-only sieve.
