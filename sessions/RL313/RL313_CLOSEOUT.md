# RL313 closeout — terminal-row ownership consumers, sparse-support extension, and mandatory strategic audit

Date: 2026-09-13
Status: CLOSED AND FROZEN
Session type: MATHEMATICAL EXECUTION FROM RL312 DIVISOR/FULL-ACTIVITY FRONTIER
Incoming/base authoritative HEAD: `d65157eaf04a870c3e6ad4da21f33af8684c43c8`
Incoming authoritative tree: `f0665a4e073cd667da203187067cda0a1e0cb666`
Successor: RL314

## 0. Executive conclusion

RL313 does not prove Gate A, Gate B, global positive non-trivial-cycle
exclusion, or the Collatz conjecture.

It does make several theorem-sized advances in the RL312 inactive/terminal
branch:

1. the gcd/divisor descent has depth at most one and then becomes idempotent;
2. terminal equal-weight rows impose an integer row-boundary packing theorem;
3. the inherited `R>=2^71` floor forces every terminal survivor to have
   `ell0>=116`, `d>=184`, and reduced `ell>=17`;
4. exactly two active shift-orbits are impossible under full-D ownership,
   extending RL312's single-active-orbit theorem;
5. every terminal macro-cycle has row-numerator diameter at least
   `2^d+3^ell0`.

The session then found two exact barriers:

- numerator-span information alone cannot force arbitrary inactive partitions
  to fragment;
- bounded centered discrepancy / short balanced-return geometry alone cannot
  consume the fully-active branch, because an explicit all-scale family of
  positive rational cyclic countermodels realizes full activity at the RL312
  mass lower bound.

Those were two consecutive non-improving checkpoints.  Under the binding RL313
target, this triggers a route freeze and a full strategic step-back/audit for
RL314.  The next session must not automatically continue the current terminal
row attack or return to the older P/Q route.

## 1. Incoming RL312 frontier preserved

RL313 inherited, in the `lambda<3` one-sided sector, the RL311/RL312 structure

`A=ga`, `L=g ell`, `s=ma`, `1<=m<=h+1`.

With `c=gcd(g,m)`, RL312 gave the exhaustive balanced-shift alternative:

- all `ac` shift-orbits active, canonical zero-sum mass at least `2ac`; or
- after rotation, equal-count rows `(ac,c ell)` and a genuine full-D-owned
  balanced segment at that divisor scale.

Binding caveats remained:

- canonical flow mass is not automatically optimal cyclic transport radius;
- descended endpoints do not automatically inherit the original RL311 `<3`
  endpoint ratio;
- global full-D ownership never implies local-segment denominator ownership;
- RL20 whole-block coboundary divisibility is not an independent obstruction.

RL313 preserves every one of these corrections.

## 2. Exact one-step terminality of divisor descent

Let `c=gcd(g,m)` and `d=ac`.  In the inactive branch, terminal rows have counts
`(d,c ell)`.

For the descended shift `d`, the row-boundary shift-orbit is itself inactive.
The new multiplier is `m*=c`, and

`gcd(g,m*)=c=m*`.

Thus the map `m -> gcd(g,m)` is idempotent.  If `c<m`, the RL312 mechanism gives
one strict reduction and no second strict reduction.

For shifts `q d`, the inactive row-boundary partition only coarsens according
to

`gcd(A,q d)=d gcd(g/c,q)`.

This exact theorem prevents false claims of an indefinitely iterated gcd
descent.

Classification at checkpoint: `PARENT_DIFFICULTY_DELTA = EASIER`.

## 3. Terminal row-boundary packing theorem

Write terminal row counts as `(d,ell0)`, number of rows `n>1`, and

`X=2^d`, `Y=3^ell0`, `D0=X-Y`.

For row numerator `q_k` and genuine integer boundary state `x_k`,

`X x_(k+1)=Y x_k+q_k`.

Iterating around the rows shows every `x_k` is a positive geometric weighted
average of the row numerators divided by `D0`:

`q_min/D0 <= x_k <= q_max/D0`.

The boundary states are distinct integers by primitivity.  Hence

`n <= floor(q_max/D0)-ceil(q_min/D0)+1`

and

`q_max-q_min >= (n-1)D0`.

The universal row numerator extrema are

`Q_min=3^ell0-2^ell0`,
`Q_max=2^(d-ell0)(3^ell0-2^ell0)`.

This is an independent integer-ownership consumer, not raw RL20 telescoping.

Classification: `EASIER`.

## 4. State-floor contraction

Using the inherited authoritative floor `R>=2^71`, every terminal boundary
must satisfy

`2^71(2^d-3^ell0)
 <= 2^(d-ell0)(3^ell0-2^ell0)`.

Since `n>=2` and `lambda<3`,

`3^ell0 < 2^d < sqrt(3)3^ell0`.

The portable verifier exhausts the exact finite range `ell0<=115` and finds 91
admissible row-count pairs, all below the state floor.

Therefore every terminal survivor satisfies

`boxed: ell0>=116, d>=184`.

The largest boundary upper bound below the cutoff is at `(111,176)` and equals

`751281177470410612498`.

The first row-count pair passing the necessary floor test is `(116,184)`, with
upper bound

`2804721460384257848662`.

At reduced level, every survivor satisfies

`boxed: ell>=17`.

The first reduced denominator capable of passing the floor test is
`(ell,a,c)=(17,27,7)`, giving `(ell0,d)=(119,189)`.

This is a bounded arithmetic certificate, not a proposal for a growing finite
row-weight search.

Classification: `EASIER`.

## 5. Exactly two active shift-orbits excluded

RL313 extends RL312's single-active-orbit exclusion.

With an inactive row partition, the canonical flow in row `k`, column `j` is

`G_(k,j)=P_k(j)-P_(k+t)(j)`,

where `P_k(j)` is the row prefix count and `k->k+t` is transitive.

If exactly two columns are active, row variation has only two possible forms:

- adjacent active cuts: a single variable three-bit fixed-weight window;
- separated active cuts: two independent adjacent `10/01` swaps.

After removing a common `2^u3^v` monomial from the row numerator variation, the
normalized coefficient alphabet has diameter strictly less than `X=2^d`.

Full-D ownership forces divisibility by the geometric cofactor

`H=(X^n-Y^n)/(X-Y)`.

This gives a polynomial relation with all coefficients of absolute value
`<X`.  Reduction successively modulo `X` forces every coefficient to vanish,
contradicting genuine row variation.

Therefore an inactive full-D balanced shift cannot have exactly two active
shift-orbits.  Together with RL312, every surviving inactive terminal shift has
at least three active shift-orbits.

Classification: `EASIER`.

## 6. Stronger support-independent numerator span

Choose the least row-boundary state `x_0`.  Its predecessor and successor
boundaries are distinct integers, so each is at least `x_0+1`.

The incoming/outgoing row recurrences immediately give

`q_max-q_min >= 2^d+3^ell0`.

Hence every terminal survivor obeys

`(2^(d-ell0)-1)(3^ell0-2^ell0)
 >= 2^d+3^ell0`.

For a fixed inactive-cut partition into count blocks `(h_i,r_i)`, exact
concatenation gives the maximum possible numerator span

`Delta_P =
 sum_i 2^(H_<i)3^(R_>i)
       (2^(h_i-r_i)-1)(3^r_i-2^r_i)`.

Any survivor must have `Delta_P>=2^d+3^ell0`.

Classification: `EASIER`.

## 7. First route barrier: span does not create fragmentation

A single fixed leading bit already leaves a flexible suffix whose exact
numerator span exceeds `2^d+3^ell0` throughout the large terminal regime.
Therefore existence of inactive cuts does not, by itself, make the span
consumer coercive.

The route "optimize over every proper inactive partition and infer almost full
activity" is frozen.  Reviving the span theorem requires an independent
fragmentation-density or block-size result.

Classification: `PARENT_DIFFICULTY_DELTA = LATERAL`.

## 8. Second route barrier: ownership-blind fully-active geometry survives

RL313 tested the strongest natural splice

RL311 bounded centered discrepancy + short equal-level return
+
RL312 orbitwise zero sums/full activity.

An explicit all-scale positive rational cyclic family survives all of this.
Starting from a near-resonant mechanical block `B`, repeat it `g` times and
insert one early `+1` defect and one later `-1` defect, separated by more than
one block in both cyclic directions.

The resulting primitive word can have:

- `1<lambda<3`;
- centered discrepancy in `[0,2)`;
- an exact `m=1` equal-level return;
- the qualitative selected endpoint ratio interval;
- every shift-orbit active for the block shift;
- `sum|G|=2a`, exactly saturating RL312's fully-active lower bound;
- a positive rational cyclic orbit.

Concrete verifier instance:

`(a,ell,g)=(27,17,10)`,
`max T=53/27`,
all 27 shift-orbits active,
`sum|G|=54`.

What the family lacks is integer/full-D ownership.  Thus any future consumer of
the fully-active branch must exploit that distinction genuinely; recurrence
geometry and discrepancy alone cannot do it.

Classification: `PARENT_DIFFICULTY_DELTA = LATERAL`.

This is the second consecutive non-improving checkpoint.  The mandatory RL313
audit trigger therefore fires.

## 9. Corrections / non-promotions

The following conversational scratch is not promoted as an independent result:

- any suggestion that terminal boundary states are universally `<2^d`;
- the earlier ad-hoc small-row macrocycle checks at weights 3 and 4 (the
  state-floor theorem supersedes the need to rely on them);
- the conversational regression count "10,246" for the two-active theorem.
  The committed portable verifier uses a reproducible structural-class
  regression instead; no theorem depends on that earlier count;
- any claim that the numerator-span inequality alone forces almost full
  activity;
- any claim that RL311 centered discrepancy plus RL312 full activity yields a
  contradiction without new full-D/integrality input.

No promoted RL311/RL312 correction is reversed.

## 10. Frozen exact frontier for future re-entry

Inactive/terminal branch, if revisited:

- descent is already terminal after at most one strict gcd reduction;
- rows satisfy `ell0>=116`, `d>=184`, reduced `ell>=17`;
- at least three shift-orbits are active;
- row-boundary integer packing and the `X+Y` numerator-span theorem are
  available;
- arbitrary inactive partitions remain possible unless a new fragmentation
  theorem is proved.

Fully-active branch, if revisited:

- orbitwise zero sum and mass `>=2d` remain valid;
- ownership-blind discrepancy/endpoint geometry is insufficient;
- the missing consumer must be genuinely integer/full-D sensitive.

The complementary RL311 branch `g<=h+1` remains open.

Gate A remains open.
Gate B remains open.
Global positive non-trivial-cycle exclusion remains open.
No Collatz conjecture claim is made.
Lean formalisation remains a separate project.

## 11. Successor instruction

RL314 must be a full strategic audit / step-back session.

Do not automatically continue the RL313 terminal-row/full-activity attack.
Do not automatically resume fixed-96 P/Q commutation or any other frozen route.

Preserve RL313 intact as a candidate resource.  Review the entire authoritative
research history by eras, build a theorem/obligation/route map, identify overlap
and possible shortcuts, and rank genuinely parent-near next attacks.  The audit
must explicitly revisit what the early, middle, and late RL generations taught,
including whether recent advances unlock old consumers in a new way.

The detailed successor target is
`authoritative/RL314_FULL_STRATEGIC_AUDIT_TARGET.md`.

## 12. Verification / transport

Promoted RL313 mathematics is analytic except for the explicit bounded
state-floor/reduced-denominator certificate and regression checks.

`sessions/RL313/verify_rl313_closeout.py` is the portable verifier.

The session directory plus `SHA256SUMS.txt` is the documented lossless transport
for this connector transition.  `RL313_SUCCESSOR_SHA256SUMS.txt` records the
two successor authoritative files.

Knowledge catalogues are `stale/deferred`, as permitted for a connector worker.

RL313: CLOSED AND FROZEN.
