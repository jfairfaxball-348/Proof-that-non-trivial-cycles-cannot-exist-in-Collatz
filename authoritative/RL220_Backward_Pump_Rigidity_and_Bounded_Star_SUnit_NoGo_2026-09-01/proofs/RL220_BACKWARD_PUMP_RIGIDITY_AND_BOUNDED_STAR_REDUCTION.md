# RL220 theorem — backward pump rigidity and bounded-star S-unit reduction

Date: 2026-09-01

## Scope and inherited algebra

Use the shortcut Collatz map

`T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.

RL218 proved that a fixed legal raw backward word `w` of length `n` with `h`
odd-inverse letters acts on an integer boundary value `x` as

`F_w(x)=(2^n x-C_w)/3^h`,

with `C_w>=0`, and `C_w>0` when `h>0`.

RL220 studies parameterized families built by repeating fixed backward blocks.
The result below is a theorem about exact integrality. Full backward legality is
stronger, so every legality consequence follows a fortiori.

## RL220-T1 — fixed-block infinite-integrality rigidity

Let a nonempty fixed backward block have affine map

`F(x)=(A x-C)/B`,

where `A=2^n`, `B=3^h`, `C=C_w`, and `h>0`.
Then `gcd(A,B)=1` and `A!=B`.

If an integer `x` has

`F^m(x) in Z`

for every integer `m>=0`, then necessarily

`(A-B)x=C`

and hence

`F(x)=x`.

### Proof

Define the integer defect

`Delta(x)=(A-B)x-C`.

A direct calculation gives

`Delta(F(x)) = (A/B) Delta(x)`.

Therefore

`B^m Delta(F^m(x)) = A^m Delta(x)`.

If every `F^m(x)` is integral, then every `Delta(F^m(x))` is integral, so

`B^m | A^m Delta(x)`.

Because `gcd(A,B)=1`, this forces

`B^m | Delta(x)`

for every `m`. The only integer divisible by every power of `B>1` is zero.
Thus `Delta(x)=0`, so `(A-B)x=C` and `F(x)=x`. QED.

### Positive/certified-blue consequence

If `A<B`, then `C>0` makes the fixed point `C/(A-B)` negative, so no positive
integer boundary can support an indefinitely repeatable block containing an
odd inverse.

If `A>B`, indefinite positive legality is possible only at the single fixed
point `x=C/(A-B)` when that value is an integer and the block is legal there.
If that fixed point is independently certified to converge to `1`, then its
forward orbit is periodic and convergent, so it lies on the trivial shortcut
cycle; for an odd certified seed this leaves only `x=1`.

No claim is made here that arbitrary fixed points are absent: excluding a
hypothetical nontrivial periodic fixed point would be a global cycle claim and
is not used.

## RL220-T2 — one-star family collapse

Let `G`, `F`, and `H` be fixed legal backward blocks and let `s` be a fixed
integer seed. Consider the family, in application order,

`x_m = H(F^m(G(s)))`, `m>=0`.

Assume all intermediate values are legal positive integers for every `m`.

- If `F` contains an odd inverse (`h(F)>0`), RL220-T1 forces the entry
  `G(s)` to be the fixed point of `F`. Therefore `F^m(G(s))=G(s)` and the
  parameter `m` contributes no endpoint variation.
- If `F` contains no odd inverse, then `F=D^n` and
  `F^m(G(s))=2^(nm)G(s)`. The family is a fixed-word image of a dyadic seed
  ray, exactly the architecture already covered by RL219-T2.

Thus a single starred fixed block cannot produce the genuinely varying
non-dyadic certified-blue family requested by RL220.

## RL220-T3 — bounded-star rectangular classification

Consider a fixed finite expression of backward blocks

`H_r F_r^(m_r) H_(r-1) ... F_1^(m_1) H_0(s)`

with fixed integer seed `s`, fixed blocks `H_i,F_i`, and independent parameters

`(m_1,...,m_r) in N^r`.

Assume the complete backward computation is legal in positive integers for
**every** parameter tuple.

Fix all parameters except `m_i` and look at the integer boundary entering
`F_i`. That boundary is independent of `m_i`. If `F_i` contains an odd
inverse, RL220-T1 applies and forces the boundary to the unique fixed point of
`F_i`; hence the star `F_i^(m_i)` is algebraically idle. This holds for every
non-dyadic star.

After deleting all idle non-dyadic stars, every genuinely varying star is a
pure `D` block. All odd-inverse letters therefore occur only in the fixed
blocks `H_i`; their total number `h` is fixed. The remaining parameters only
change the dyadic gap exponents between those fixed odd inverses.

This is an exact classification of the stated **rectangular bounded-star**
class. It does not cover correlated/nonrectangular parameter domains, a number
of odd inverses growing with the parameter, or genuinely aperiodic word
generators.

## RL220-T4 — exact S-unit/exponential pullback for the surviving class

Write the reduced fixed-odd-count word in RL218 odd-only form with gap
exponents `e_1,...,e_h`. Let

`Q_0=0`,
`Q_j=2^(e_j) Q_(j-1)+3^(j-1)`,

and `E=sum_j e_j`. Then

`Q_h = sum_(i=1)^h 3^(i-1) 2^(e_(i+1)+...+e_h)`,

and an endpoint `y` from fixed odd seed `s` obeys

`3^h y = s 2^E - Q_h`.

For a bounded-star family after RL220-T3, each gap is affine in the remaining
pure-dyadic star parameters:

`e_j=b_j + sum_l a_(j,l) m_l`

with fixed nonnegative integer coefficients. Hence the endpoint is a finite
signed exponential/S-unit expression in powers of `2`:

`3^h y =
 s 2^(B + sum_l A_l m_l)
 - sum_(i=1)^h 3^(i-1)
   2^(B_i + sum_l A_(i,l) m_l)`.

Substituting the exact RL root lattice

`y=y_*+3*2^58 k`

gives

`3^(h+1) 2^58 k + 3^h y_* =
 s 2^(B + sum_l A_l m_l)
 - sum_(i=1)^h 3^(i-1)
   2^(B_i + sum_l A_(i,l) m_l)`.

Thus every parameter tuple proposes at most one exact `k`, subject to
integrality, finite-window, terminal-Hensel, phase-51, and blue-certification
checks. Branch legality or the parameterization alone does **not** certify a
non-singleton RL `k` class.

Classification: proved analytic reduction theorem / method barrier.

## What remains open

The theorem intentionally leaves open the structures that RL221 should attack:

1. certified-blue families whose number of odd inverses grows unboundedly;
2. correlated or nonrectangular parameter domains where a non-dyadic repeat
   is not independently pumpable;
3. genuinely aperiodic/substitution/recursive word families;
4. an independent theorem proving that the resulting exponential/S-unit image
   contains or excludes an exact non-singleton subset of the current RL lattice.

No candidate, prefix, terminal rank, Gate, or global cycle conclusion follows
from RL220-T1--T4 alone.
