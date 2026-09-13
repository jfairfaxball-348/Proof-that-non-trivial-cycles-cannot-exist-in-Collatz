# RL312 closeout — owned balanced-flow exclusions and divisor-aligned descent

Date: 2026-09-13
Status: CLOSED AND FROZEN
Session type: MATHEMATICAL EXECUTION FROM RL311 GLOBAL COMPRESSION ROUTE
Incoming base HEAD: `1859f9367d2f9dab2d704876413d042b4e3c4e1b`
Final pre-closeout HEAD: `a71741b635477a932e27be47a98fdfe9f2cc2168`
Successor: RL313

## 0. Executive conclusion

RL312 does not prove global non-trivial-cycle exclusion. Gate A and Gate B remain open.

It does, however, produce three genuine ownership/combinatorial consumers of the RL311 short balanced return and materially contracts that branch:

1. exact owned balanced Radius 2 is impossible;
2. a full-D owned balanced flow cannot be supported on a single shift-orbit;
3. every balanced shift satisfies an all-scale shift-orbit dichotomy: either every gcd shift-orbit is active, or the word admits an exact divisor-aligned equal-weight block decomposition, giving a shorter owned balanced segment whenever the divisor drops.

The third result is the final RL312 frontier and is the unique recommended starting point for RL313.

The complementary RL311 branch `g<=h+1` remains open. RL312 tested the old strict-excursion/state-packing route against this survivor and did not obtain an independent contradiction. No false packing closure is promoted.

Because RL312 produced a new all-scale consumer and a strict divisor descent, the previously requested strategic-audit fallback condition is not triggered by this closeout: something material did change.

## 1. Incoming object

RL312 inherited from RL311, in the active one-sided sector `lambda<3`, the exhaustive dichotomy

`g<=h+1`

or a proper equal-level pair of genuine full-D cycle rotations at reduced-block separation

`1<=m<=h+1`,

with exact segment counts

`(ma,m ell)`

and endpoint ratio

`1/lambda < (4x_k+1)/(4x_j+1) < lambda < 3`.

The balanced segment gives a genuine cyclic self-rotation with zero determinant in the canonical normalization.

## 2. Normalization repair and exact owned Radius-2 exclusion

RL312 first corrected an overstatement in scratch: the canonical balanced flow has zero total sum, but the optimally normalized cyclic transport flow may differ by an integer constant. Therefore arbitrary optimal transport determinant is not automatically zero.

For every local shell of radius `<A`, however, the nonzero constant normalization is too expensive and the canonical zero-sum normalization is forced.

In exact Radius 2, the canonical flow has one `+1` and one `-1`. Shift-coboundary structure places the two defects on the same shift-orbit. Their separation is `ta`, and the intervening odd count is `t ell-1`. Full-D weighted rotation arithmetic then forces

`D | (2^(ta)-3^(t ell))`,

with

`D=2^(ga)-3^(g ell)`, `1<=t<g`.

The nonzero left side has absolute value strictly smaller than `D`, contradiction.

Therefore an owned balanced return cannot have exact Radius 2.

Promoted files:

- `sessions/RL312/RL312_BALANCED_RETURN_RADIUS2_EXCLUSION_AND_NORMALIZATION_REPAIR.md`;
- `sessions/RL312/verify_rl312_balanced_radius2.py`.

Promoted commits:

- `15857a95066d4d6774a307f0f13cb95123f1152d`;
- `5804202aa1a4515747baee463e5369a0da9f6a8b`.

Classification: `PARENT_DIFFICULTY_DELTA = EASIER`.

## 3. Full-D single-shift-orbit exclusion

RL312 next proved an all-scale sparse-support theorem.

If the canonical balanced flow were supported on only one shift-orbit, the cyclic word could be rotated and cut into equal-weight rows such that every row is identical except for one adjacent pair, of type `10` or `01`.

Grouping the full numerator by rows yields

`Q=Q0 H + C S`,

where `H` is a proper geometric cofactor of the full denominator, `0<S<H`, and `gcd(C,H)=1`.

Full-D ownership implies `D|Q`, hence in particular `H|Q`, forcing `H|S`, impossible.

Thus a full-D owned balanced flow must activate at least two distinct shift-orbits.

This strictly subsumes the structural support pattern behind Radius 2 and is not a fixed-radius grammar.

Promoted files:

- `sessions/RL312/RL312_SINGLE_SHIFT_ORBIT_EXCLUSION.md`;
- `sessions/RL312/verify_rl312_single_shift_orbit.py`.

Promoted commits:

- `d2fab597cc6bb0de1f58b737ac8d6d5f65b6b33b`;
- `a71741b635477a932e27be47a98fdfe9f2cc2168`.

The finite regression check covered 1,046 primitive positive-D single-orbit instances through length 14.

Classification: `PARENT_DIFFICULTY_DELTA = EASIER`.

## 4. Final theorem: orbitwise zero sum and divisor-aligned descent

For any binary cyclic word of length `A`, total weight `L`, and balanced shift `s` with

`p=sL/A in Z`,

define

`G_i=p-W_i(s)`.

Let

`d=gcd(A,s)`, `n=A/d`, `t=s/d`.

RL312 proves that `G` sums to zero separately on every one of the `d` shift-orbits.

Hence every active shift-orbit contributes at least `2` to the canonical zero-sum L1 mass. If all are active,

`sum_i |G_i| >= 2d`.

If one shift-orbit is inactive, then after rotating to that orbit and cutting into consecutive length-`d` blocks, all `A/d` block weights are equal to

`Ld/A`.

Specialize to the RL311 shift

`s=ma`, `A=ga`, `L=g ell`,

and let

`c=gcd(g,m)`.

Then

`d=ac`.

Therefore either

- all `ac` shift-orbits are active, giving canonical mass at least `2ac`; or
- after rotation, the full cycle decomposes into equal-count `(ca,c ell)` blocks, and in particular there is a genuine full-D-owned balanced segment of counts `(ca,c ell)`.

If `c<m`, this is a strict descent from the RL311 balanced gap `m` to gap `c`.

Important scope points:

- this is canonical zero-sum flow mass, not automatically optimal cyclic transport radius;
- descended endpoints retain global full-D ownership because they are genuine cycle rotations;
- no local denominator ownership is inferred;
- the original RL311 endpoint ratio `<3` is not automatically inherited by the descended pair.

Promoted files:

- `sessions/RL312/RL312_SHIFT_ORBIT_DICHOTOMY_AND_DIVISOR_DESCENT.md`;
- `sessions/RL312/verify_rl312_shift_orbit_dichotomy.py`.

The regression verifier exhausts 10,876 balanced binary word/shift instances through `A<=13`.

Classification: `PARENT_DIFFICULTY_DELTA = EASIER`.

## 5. Controlled-multiplicity branch audit

RL312 also tested the complementary RL311 survivor

`g<=h+1`

against the historical strict-excursion, state-packing, and continued-fraction interfaces.

No independent closure was obtained.

One exact local observation remains potentially useful but is not itself a contradiction: if a canonical block is all zero then its level drops by exactly `ell`; therefore under `0<=E_j<=h`, the subbranch `h<ell` forbids all-zero canonical blocks. This restores the positivity premise behind some historically demoted strip calculations only on that restricted subbranch. RL312 did not derive a global contradiction from it, so no stronger strip theorem is promoted.

The complementary regime `h>=ell` likewise remains open.

## 6. Red-team conclusions and frozen non-routes

The following remain binding:

1. Global `D|Q` does not imply proper-prefix or local-denominator ownership.
2. RL20 whole-block coboundary identities are closure identities and cannot be repackaged as independent obstructions.
3. The canonical zero-sum flow and the optimally normalized transport flow must not be conflated.
4. Radius 6+ remains frozen absent a proved encounter theorem.
5. The descended balanced pair does not automatically inherit the original physical endpoint-ratio bound.
6. The controlled branch `g<=h+1` is not finite merely because `g` is bounded by `h+1`.
7. No pure packing contradiction for the controlled branch has been proved.

## 7. Exact successor frontier

RL313 should begin from the divisor-aligned shift-orbit dichotomy, not by reopening Radius 6+, H21, Gate-A Y ancestry, fixed-depth P/Q commutation, or raw RL20 coboundary algebra.

The primary question is now:

> Can the divisor descent be iterated or combined with full-D row factorization so that every balanced return either reaches a terminal divisor-aligned owned segment that is impossible, or forces a fully active canonical defect whose global weighted moment / ownership is impossible?

The most valuable subcases are:

- `gcd(g,m)=1`: either all `a` shift-orbits are active or an owned exact `(a,ell)` segment exists;
- `c=gcd(g,m)<m`: exploit strict descent and determine what endpoint/ownership information survives iteration;
- `c=m` (equivalently `m|g`): no length descent occurs, so test whether the exact equal-weight `ma` partition plus full-D ownership has a direct factorization obstruction;
- fully active case: use orbitwise zero sums and full-D/weighted information, while respecting the optimal-normalization caveat.

The controlled-multiplicity branch `g<=h+1` remains live in parallel but should not displace this new parent-near theorem unless the divisor route stalls.

## 8. Final proof status

RL312: CLOSED AND FROZEN.

Gate A: OPEN.
Gate B: OPEN.
Global positive non-trivial-cycle exclusion: OPEN.
No Collatz conjecture claim is made.
Lean formalisation remains a separate project.
Knowledge catalogues remain stale/deferred.

`PARENT_DIFFICULTY_DELTA = EASIER`

Reason: RL312 supplied multiple independent ownership-sensitive consumers and, finally, an exhaustive all-scale divisor descent / full-activity dichotomy for every balanced shift. The parent balanced-return problem is strictly more structured than at RL312 entry.

It makes sense to continue here.
