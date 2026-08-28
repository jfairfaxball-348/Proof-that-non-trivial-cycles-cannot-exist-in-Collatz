# RL161 — Homogeneous ownership-to-global bridge barrier

## Scope

RL161 tests the weighted-difference/perimeter and population/packing priority
bridges from the authoritative RL161 target.  It proves a barrier for the
broad subclass whose global quantity is homogeneous under generalized
odd-increment scaling.  It does not rule out a non-homogeneous ordinary
Collatz (`+1`) bridge, and it does not exclude non-trivial cycles.

## Generalized-cycle interface

For a primitive binary word `w` of length `A`, weight `L`, and
`D=2^A-3^L>0`, let `Q_i` be its cyclic affine numerators, set
`g=gcd(D,Q_0)`, `s=D/g`, and `n_i=Q_i/g`.  The inherited RL79 theorem gives a
positive primitive cycle of

\[
T_s(n)=n/2\quad(n\text{ even}),\qquad T_s(n)=(3n+s)/2\quad(n\text{ odd}).
\]

Full ordinary ownership is exactly `s=1`.  For every positive odd `c`,

\[
T_{cs}(cn_i)=cT_s(n_i),\qquad \frac{cn_i}{cs}=\frac{n_i}{s}=\frac{Q_i}{D}.
\]

These are generalized-increment controls, not constructions of ordinary
Collatz cycles when `s>1`.

## Theorem RL161-A — homogeneous global quantities are increment-blind

Let `F(w;n_0,...,n_{A-1};s)` be homogeneous of degree `d` under simultaneous
odd scaling:

\[
F(w;cn_0,\ldots,cn_{A-1};cs)=c^dF(w;n_0,\ldots,n_{A-1};s).
\]

Then:

1. If `d=0`, it has the same value on every odd scaling of the generalized
   cycle.  Thus expressions solely in normalized phases `n_i/s=Q_i/D`,
   normalized differences, ratios, signs, and the word do not distinguish
   `s=1` from `s>1`.
2. If `d>0`, its raw positive burden scales by `c^d`; the homogeneous identity
   itself gives no scale-independent upper bound.
3. Homogeneous equalities and sign constraints are invariant under scaling,
   so they cannot alone force `s=1`.

**Proof.** Substitute `(cn,cs)` into the even and odd branches to obtain the
covariance.  Apply homogeneity.  Degree zero is invariant, positive degree is
unbounded over odd `c`, and multiplication by a positive factor preserves
zero and sign.  RL79 supplies a positive generalized cycle for each primitive
above-resonance word, so these normalized facts have no `s=1` discriminator.
∎

## Consequences

For fixed word-dependent weights, normalized weighted perimeters such as

\[
\sum_{i<j}a_{ij}|n_i-n_j|/s
\]

and homogeneous normalized products are degree zero.  Raw perimeters are
positive degree: they price scale but cannot contradict without an independent
ordinary-`s=1` absolute cap.  Population counts and normalized packing data
are word data; raw spacing/box bounds likewise require an absolute capacity
constraint beyond distinctness or homogeneous spacing.

Therefore the direct homogeneous weighted/perimeter and normalized
population/packing bridges are closed as ownership discriminators.  A live
bridge must consume a non-homogeneous `s=1` fact: exact content/lattice,
ordinary basin membership, or a uniform physical maximum/period cap.

## Scope checks

- Ordinary cycles cannot be scaled while remaining ordinary; this is not
  claimed.
- RL87's first-Farey physical-difference theorem survives because its
  physical maximum is an absolute ordinary-Collatz input, not homogeneous.
- No fixed-radius, unordered-valuation, or same-root elimination claim is
  revived.
