# RL140 — one-deviant-block contact obstruction

## Outcome and scope

Fix the inherited first reduced above-side pair `(A,L)` and a full-count
multiple `(gA,gL)` with `g>1`.  In the all-nonnegative **height-one** branch,
write the defect path as `h_j in {0,1}`.  RL140 proves the following
ordinary-owned exclusion.

> If the zero-contact pattern is identical in every reduced block except one,
> then it cannot be the exponent profile of an actual full-count cycle when
> `g>=3`.  The same exclusion holds for `g=2` when the exceptional block
> changes at most three contact residues.

Here a contact is an index with `h_j=0`, and a reduced block has length `L`.
The theorem is an analytic affine-numerator/factorization obstruction.  It
does not cover arbitrary nonperiodic contact patterns, height greater than
one, negative defects, or any entire multiplicity.  No count frontier, Gate
A/B status, RL exclusion, or Collatz status changes.

## 1. Inherited mechanical setup

Put `N=gL`,

`b_j=floor(Aj/L)`,
`c_j=b_(j+1)-b_j`,
`X=2^A`, `Y=3^L`, and

`F_g=sum_(t=0)^(g-1) X^t Y^(g-1-t)`.

The inherited first-survivor floor lock gives, for `0<r<L`,

`2^(floor(Ar/L)) < 3^r`.

Also `X>Y`; in particular `A>L`.  Define the one-block weights

`W_r=3^(L-1-r)2^(floor(Ar/L))`, `0<=r<L`,

and their total `Q_0=sum_r W_r`.  Then

`W_r < 3^(L-1) < X/3`,

including `r=0` by `Y<X`.  Consequently

`Q_0 < LX/3 < X^2`.                                      (1.1)

The last elementary inequality uses `L<3X`, immediate from `A>L>=1`.

The 2-adic valuations

`v_2(W_r)=floor(Ar/L)`

are strictly increasing in `r`, since `A/L>1`.  Therefore distinct subsets
of `{0,...,L-1}` have distinct `W`-weights: take the least residue in their
symmetric difference and reduce the signed difference modulo its next power
of two.

## 2. Height-one contact numerator

For `h_j in {0,1}`, let

`a_j=c_j+h_j-h_(j+1)`

and let `Q_h` be the standard accelerated affine numerator.  With

`B_j=3^(N-1-j)2^(b_j)`, direct substitution gives

`2Q_h=Q_c+R_0`,                                           (2.1)

where `Q_c=sum_j B_j` and

`R_0=sum_(h_j=0) B_j`.

Repeated mechanical factorization gives

`Q_c=Q_0F_g`, `2^(gA)-3^(gL)=(X-Y)F_g`.                  (2.2)

Thus actual full ownership, namely

`2^(gA)-3^(gL) | Q_h`,

forces

`F_g | R_0`.                                              (2.3)

This is only a necessary condition.  No converse or generic contact-count
claim is used.

For block `t`, set

`C_t={r: h_(tL+r)=0}` and `C(S)=sum_(r in S)W_r`.

Since

`B_(tL+r)=X^tY^(g-1-t)W_r`,

(2.3) becomes

`F_g | sum_(t=0)^(g-1) X^tY^(g-1-t) C(C_t)`.             (2.4)

## 3. One exceptional block

Assume `C_t=C` for every `t` except `s`, where `C_s=C'`.
Subtracting the periodic baseline `C(C)F_g` from (2.4) yields

`F_g | X^sY^(g-1-s) [C(C')-C(C)]`.

Both `X` and `Y` are coprime to `F_g`: modulo a prime factor of either,
the opposite endpoint term of `F_g` is nonzero.  Hence

`F_g | delta`, where `delta=C(C')-C(C)`.                 (3.1)

If the exceptional pattern is genuine, `C'!=C`; the increasing 2-adic
valuations above give `delta!=0`.

### Theorem RL140.1 — all `g>=3`

For `g>=3`,

`F_g > X^(g-1) >= X^2 > |delta|`,

where the last inequality is (1.1).  This contradicts (3.1).  Therefore no
actual full-count cycle has a height-one contact profile that is periodic by
reduced blocks except for one different block.

### Theorem RL140.2 — sparse exceptional block at `g=2`

For `g=2`, suppose `|C triangle C'|<=3`.  The signed sum `delta` has at most
three terms, each of absolute value `<X/3`; hence

`0<|delta|<X<X+Y=F_2`,

again contradicting (3.1).  Thus the same one-deviant-block profile is
excluded at multiplicity two under this explicit three-contact interface
bound.

## 4. Verification and red teams

`verification/verify_rl140_one_deviant_block.py` uses exact integers to
check:

- the height-one numerator identity (2.1) over all small admissible defect
  paths in representative mechanical pairs;
- the block factor reduction from (2.4) to (3.1) over every small contact
  subset pair;
- the two stated small-instance consequences for `g=2,3`.

The calculation is a finite algebraic cross-check, not the proof.

The ordinary `+1` numerator and full denominator are retained throughout, so
this does not pass the RL79 generalized-increment scaling red team merely by
normalizing states.  It also does not claim that all contact patterns are
physical, that a periodic pattern itself is a cycle, or that a nonperiodic
pattern is impossible.  The previously identified CRT/run-fibre gap remains:
contact positions alone do not create the actual repeated ordinary runs that
RL122/RL123 require.

## 5. Next target

Attack genuinely multi-block deviations from periodic height-one contact
patterns.  A valid extension must control the signed block polynomial in
(2.4) using full ordinary ownership or a newly proved physical-state/run
constraint; bare contact counts, raw periodicity, and a second restatement of
`D|Q` are insufficient.
