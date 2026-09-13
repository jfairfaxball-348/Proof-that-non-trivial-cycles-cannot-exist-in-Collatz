# RL313 — partition-span and fully-active red teams

Date: 2026-09-13
Status: CLOSED RL313 BARRIER RECORD
Classification: EXACT NEGATIVE CONTROLS / ROUTE FREEZE

## 1. Exact inactive-cut partition span

Suppose inactive cuts partition every terminal row into subblocks with fixed
counts

`(h_1,r_1),...,(h_s,r_s)`.

For binary words `U,V`,

`Q(UV)=3^(|V|_1) Q(U)+2^(|U|) Q(V)`.

Therefore the exact maximum row-numerator diameter allowed by this partition is

`Delta_P =
 sum_i 2^(H_<i) 3^(R_>i)
       (2^(h_i-r_i)-1)(3^r_i-2^r_i)`,

where `H_<i` is the total length before block `i` and `R_>i` the total weight
after it.

The minimum-boundary theorem requires

`Delta_P >= 2^d+3^ell0`.

This is a valid scalable consumer once an independent theorem forces enough
fragmentation.

## 2. Why span alone does not force fragmentation

The converse fails badly.

If the first bit is fixed to 0 across all rows, the remaining suffix is a
single flexible block of length `d-1`, weight `ell0`, and

`Delta_0 =
 (2^(d-ell0)-2)(3^ell0-2^ell0)`.

If the first bit is fixed to 1,

`Delta_1 =
 2(2^(d-ell0)-1)(3^(ell0-1)-2^(ell0-1))`.

In the terminal sector

`3^ell0 < 2^d < sqrt(3) 3^ell0`.

Already for `ell0>=5`, both `Delta_0` and `Delta_1` exceed
`2^d+3^ell0`.  RL313 has independently forced `ell0>=116`, so the failure is
enormous in the actual surviving regime.

Thus the route

"optimize numerator span over all proper inactive partitions and infer almost
full activity"

is frozen.  A large flexible block retains too much coefficient freedom.
A future use of the span theorem needs an independent fragmentation-density or
block-size theorem.

## 3. Fully-active ownership-blind countermodel family

The final attempted splice was

RL311 bounded centered discrepancy + short equal-level return
+
RL312 orbitwise zero sums / fully active canonical flow.

This is not enough without integer/full-D ownership.

Take any coprime reduced pair `(a,ell)` with

`z=2^a/3^ell>1`

and choose `g>=4` so that

`z^g<3`.

Choose a length-`a`, weight-`ell` mechanical block `B` whose prefix discrepancy
lies in `[0,1)`.  Start with `B^g`.  Change one 0 in an early copy to 1 and,
more than `a` positions later (and also more than `a` around the complementary
arc), change one 1 in a later copy to 0.  Choose the two defect positions
non-antipodally when needed.

Then:

- total counts remain `A=ga`, `L=g ell`;
- `1<lambda=z^g<3`;
- the centered discrepancy remains in `[0,2)`;
- an untouched early block gives an exact `m=1` equal-level balanced return;
- the word is primitive;
- for shift `s=a`, every residue class modulo `a` receives exactly one window
  with count `ell+1` and one with count `ell-1`;
- hence every one of the `a` shift-orbits is active and
  `sum |G|=2a`, exactly attaining the RL312 fully-active lower bound;
- since `D=2^A-3^L>0`, the word has a positive rational cyclic orbit;
- the standard `U` monotonicity on the untouched equal-level pair gives the
  same qualitative near-endpoint ratio interval `(1/lambda,lambda)`.

The construction can be made for arbitrarily large scales by taking reduced
rational slopes approaching `log_2 3` from above.

### Concrete portable regression instance

`(a,ell,g)=(27,17,10)`.

The RL313 verifier certifies:

- `lambda=(2^27/3^17)^10` lies in `(1,3)`;
- the modified word is primitive;
- `0<=T_i<=53/27<2`;
- first block levels are `0,0,1,1,0`;
- all 27 shift-orbits are active;
- `sum|G|=54=2a`.

## 4. Strategic consequence

The fully-active branch cannot be closed using only recurrence geometry,
bounded discrepancy, short equal-level return, endpoint proximity, orbitwise
zero sums, or canonical-flow mass.

A genuinely new integer/full-D ownership-sensitive input is necessary.

This was the second consecutive non-improving RL313 checkpoint after the
partition-span barrier, so the binding RL313 audit trigger fired.  The route is
frozen intact for future re-entry rather than extended into support-3/4/... or
another local grammar.
