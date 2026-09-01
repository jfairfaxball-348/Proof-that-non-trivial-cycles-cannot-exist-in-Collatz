# RL206 targeted recovery audit: RL20 strip-increment normalization

Classification: **explicit mathematical correction RL206-C1**. This is a narrowly identified mathematical formula correction,
not a demotion of Gate A, Gate B, or the inherited radius-3 obstruction. No tracked source
has been changed. Ordinary research was paused on discovery. Root subsequently
independently reviewed the symbolic proof, verified the exact Fraction witness, recorded
this as **RL206-C1** in working STATE, and cleared the targeted stop-and-repair gate.

## First invalid expression and exact dependencies

`sessions/RL20/RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md:167` prints

`H_(j+1)-H_j = z^j Q(B_j)/Y` (R20G.12).

This omits `3^(-E_(j+1))` when `Q(B_j)` is the raw block affine numerator.
There is no ambiguity in the exact dependency:

- `sessions/RL20/RL20_CANONICAL_BLOCK_COBOUNDARY.md:28` defines raw `Q_j=Q(B_j)`;
- its lines 34, 40, 48 define/prove `X x_(j+1)=3^(r_j)x_j+Q_j`,
  `y_j=3^(-E_j)x_j`, and `3^(-E_(j+1))Q_j=Xy_(j+1)-Yy_j`;
- its lines 54 and 58 name the **normalized** numerator `c_j`;
- the geometry note itself repeats the correctly normalized block identity at line 159,
  then sets `H_j=z^j y_j` at line 163;
- `sessions/RL20/verify_rl20_block_coboundary.py:11` returns raw `Qword(w)` from
  `block_Q(w)`; lines 55–58 explicitly multiply by `3^(-E_(j+1))` before asserting
  the normalized block identity.

Thus the correct identity, directly by multiplication of the inherited exact block
identity by `z^j/Y`, is

`H_(j+1)-H_j = (z^j/Y) 3^(-E_(j+1)) Q(B_j) = z^j c_j/Y`.

Every factor preceding `Q(B_j)` is positive. Consequently increments are nonnegative
and are strictly positive exactly when the block has at least one `1`. Positive block
length alone does not imply a positive affine numerator.

## Targeted arithmetic witness, with honest scope

The six-bit word `110000` has `A=6,L=2,g=2,a=3,ell=1,X=8,Y=3,D=55`.
Its raw numerator is `Q=5` and its rational fixed state is `R=1/11`.
With blocks `110|000`, `E=(0,1,0)` and block states are
`x=(1/11,8/11,1/11)`. Thus

`H_1-H_0 = 64/99-1/11 = 5/9`,

whereas the printed raw expression gives `Q(110)/Y=5/3`.
The corrected expression gives `3^(-1)*5/3=5/9`.
The second block has positive length but zero numerator/increment.

This witness tests the exact all-word algebraic dependency; it is neither a positive
integer Collatz cycle nor a witness satisfying the near-resonance assumptions of the
geometry theorem. The correction is established symbolically from the inherited block
identity, not by presenting this finite example as a counterexample to an owned theorem.

## Affected frontier

Affected: the exact coefficient in the printed R20G.12, and any proposed quantitative
population/strip lower bound that substitutes its unnormalized raw right-hand side.
Such a substitution would overcount blocks with `E_(j+1)>0` and cannot be used.

Unaffected, by direct inspection of their derivations in the same geometry note:

- one-sided imbalance `E_j>=0` under `lambda<3` (lines 41–69);
- the block-cut height sandwich from prefix/suffix affine equations (lines 71–103);
- the balanced odd pair and separated positive-imbalance height bands under
  `lambda<16/15` (lines 105–149);
- nondecreasing lift and its exact endpoints `H_0=R#`, `H_g=lambda R#`;
- the total strip width `(lambda-1)R#`;
- the open classification of the balanced-return and strict-excursion contradiction;
- conditional rescue/CF lower bounds (not replayed and not needed for this correction).

The inherited `verify_rl20_near_gcd_block_geometry.py` has 56 lines. It checks the
imbalance implication, height-band/parity reasoning, rescue threshold, and CF-induced
length floor, but contains no R20G.12 check. Its historical pass therefore does not verify
the erroneous displayed coefficient. No expensive historical suite was rerun.

The exact mathematical correction must be carried explicitly into the next proof and
correction ledger in this generation. The old frozen session must remain immutable.
