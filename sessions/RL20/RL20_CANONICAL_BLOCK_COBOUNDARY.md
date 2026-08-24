# RL20 — canonical gcd-block polynomial is an exact state coboundary

Date: 2026-08-20

## Status

**ANALYTIC.**  This is an exact algebraic identity for the rational fixed orbit of any full-parity word with `D=2^A-3^L>0` and `g=gcd(A,L)>1`.

It does **not** prove RL.  Its main value is strategic: it explains why the raw higher-block/proper-factor polynomial cannot by itself be the missing contradiction.

## 1. Canonical block setup

Write

`A=ga`, `L=g ell`, `g=gcd(A,L)>1`,

and put

`X=2^a`, `Y=3^ell`, `D=X^g-Y^g`.

Partition the full parity word into `g` consecutive blocks `B_j` of length `a`.

Let

- `r_j` be the number of ones in `B_j`;
- `K_j=r_0+...+r_(j-1)` with `K_0=0`;
- `E_j=K_j-j ell`, so `E_0=E_g=0`;
- `Q_j=Q(B_j)` be the affine numerator of block `B_j`.

Let `x_j` be the phase state at the start of block `j`.  For an actual cycle these are positive integers.  More generally, for any word they may be taken along its exact rational fixed orbit `R=Q(d)/D`.

The block affine relation is

`X x_(j+1) = 3^(r_j) x_j + Q_j`.                         (R20B.1)

## 2. Imbalance-normalized states

Define

`y_j = 3^(-E_j) x_j`.                                     (R20B.2)

Because

`r_j = ell + E_(j+1)-E_j`,

multiplying (R20B.1) by `3^(-E_(j+1))` gives

`3^(-E_(j+1)) Q_j = X y_(j+1) - Y y_j`.                  (R20B.3)

Thus the weighted block coefficient in RL-L55 is not an independent combinatorial quantity.  It is an exact first difference of normalized states.

Set

`c_j = 3^(-E_(j+1)) Q_j`.                                  (R20B.4)

Then

`c_j = X y_(j+1)-Y y_j`.                                   (R20B.5)

## 3. The full block polynomial telescopes

Let

`z=X/Y=2^a/3^ell`.

Consider the canonical block polynomial

`F(z)=sum_(j=0)^(g-1) c_j z^j`.                             (R20B.6)

Using `X=zY` and (R20B.5),

`F(z)`

`=Y sum_j z^j (z y_(j+1)-y_j)`

`=Y(z^g y_g-y_0)`

`=Y(z^g-1)R`,                                               (R20B.7)

because `E_g=0` and the fixed orbit has `x_g=x_0=R`.

Since `z^g=2^A/3^L=lambda`,

`F(z)=Y(lambda-1)R`.                                        (R20B.8)

Multiplying by `Y^(g-1)` recovers exactly

`Q(d)=R(X^g-Y^g)=RD`.                                       (R20B.9)

So the entire canonical block hierarchy is a repackaging of cycle closure.

## 4. Why RL-L55 alone cannot obstruct an actual cycle

Modulo the proper factor

`D0=X-Y`,

one has `z=1`.  Summing (R20B.5) cyclically gives

`sum_j c_j = (X-Y) sum_j y_j`.                              (R20B.10)

After clearing the harmless powers of `3`, this is precisely the weighted block cancellation seen in RL-L55.

Thus, for an actual fixed orbit, the `D0` cancellation is forced by an exact coboundary identity.  It is not an additional independent restriction capable of producing a contradiction by itself.

Likewise, working modulo the cofactor

`(X^g-Y^g)/(X-Y)`

makes `1+z+...+z^(g-1)=0`, but the full polynomial still telescopes because it comes from (R20B.5).

## 5. Strategic consequence

This formally narrows the higher-block route.

**Retire:** attempts to contradict RL using only the existence of the raw RL-L55 weighted block congruence or the corresponding whole-block cyclotomic polynomial.

**Still viable:** arguments that add information not contained in the coboundary identity, for example

1. least-state inequalities that force one-sided bounds on the normalized states `y_j`;
2. root/final-return ownership or residue restrictions on specific blocks;
3. a difference between two rotations, where the state coboundaries do not cancel identically term-by-term;
4. a proper sparse subfactor/resultant obtained after independently controlling the coefficient pattern.

This matches the RL19 lesson for the raw orbit sum: the right global target is a constrained **difference** or a proper factor with extra state structure, not positivity or divisibility of the whole tautological closure polynomial.

Verifier: `verify_rl20_block_coboundary.py` checks the identities exactly with rational arithmetic on 2,645 words.
