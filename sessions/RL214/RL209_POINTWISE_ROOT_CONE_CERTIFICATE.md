# RL209 pointwise root-cone and above-p information-boundary certificate

Date: 2026-08-31. All physical implications remain conditional on the sole high
branch `(37,0,23,-1)`. Necessary ranks are not physical H21 occurrences or
charges.

## 1. Canonical above-p endpoint decomposition

Retain the RL206/RL208 notation

`A=217976794617`, `L=137528045312`, `B=A-L`, `p=65470613321`,
`u=103768467013`, `Ap-uL=1`, `K_0=2^37`, `d=3^p-2^u`,
`P_a=sum_(0<=j<a) q_j`.

At a tau34 source phase `a`, terminal phase and terminal rank are

`i=a+34 mod L`,  `r=iB mod L`.

The inherited exact endpoint moment is

`E_a=3*2^(u+37)-3^p P_p+d P_a
    =d*2^(b_a-1)*3^(1-a)*(2^34 eta-1)`.

For the genuine canonical above-p side put `a=p+e`, `e>=1`, and
`R_(p,a)=sum_(p<=j<a)q_j`.  Then `P_a=P_p+R_(p,a)` and therefore

`E_a=3*2^(u+37)-2^u P_p+d R_(p,a)`.                 (1)

Also

`b_(p+e)=u+floor((Ae+1)/L)`

and, because the H21 source has height one,

`S_a=b_a-1=u+floor((Ae+1)/L)-1 >= u`.              (2)

Thus the `2^u P_p` term in (1) does **not** become a high-depth vanishing root
term after normalization by `2^S_a`.  Its normalized depth is `u-S_a<=0`.
The physical endpoint identity instead forces cancellation with the other terms.
This is the precise one-sided obstruction to reflecting the corrected below-p
37/60/97 theorem.  Rewriting (1) is not a new eta determination.

## 2. Lifted p-shift and the actual carry

For every lifted phase define

`epsilon(a)=b_(a+p)-b_a-u`.

The inherited exact law gives `epsilon(a)=1` only at mechanical rank `L-1`,
equivalently at the unique canonical phase `a=L-p`; otherwise it is zero.
If `a+p>=L`, canonical notation wraps, but the paired endpoint is still the
**lifted** phase `a+p`; q, rho and K carry their lambda-quasiperiodic lift.
Canonical period wrap is therefore not permission to reflect a below-p tau34
source theorem.  In particular, the canonical partner reached after a wrap is
not thereby proved to be a second tau34 source with the hypotheses of RL203.

## 3. Sharper absolute-root bracket

Let `delta=A ln2-L ln3` and `lambda=exp(delta)`.  The exact fixed-point logarithm
certificate in `verification/verify_rl209_pointwise_root_cone.py` proves

`ln(1+1/(9K_0)) < delta < ln(1+1/(8K_0))`.

Hence

`K_0+1/9 < K_L=lambda K_0 < K_0+1/8`.               (3)

For a terminal phase `i=L-d` with `1<=d<=2^35`, every chronological source on
the path from i to L is away from the unique p-shift carry because
`L-2^35 > L-p`.  The inherited noncarry speed law gives
`|K_(j+1)-K_j|<1/3`.  Summing the **actual** distance d and using (3) yields

`K_0+1/9-d/3 < K_i < K_0+1/8+d/3`.                  (4)

This is a pointwise theorem.  It is strictly sharper than using one common outer
radius for all phases in a coarse layer, and it does not cross the carry.

## 4. Exact disjoint rank consumption

For H21 terminals the inherited law

`K_i=K_H21(r)=rho_(I(r))*T/2^21`,  `T=7*3^35`,

is strictly decreasing in r.  Equation (4) therefore gives a contiguous safe
rank band at every distance bound.

First, in the inherited backward root window `[L-2^24,L)`, the RL208-reduced
predicate has exactly 1,969 surviving ranks in the inherited root safe band.
Testing (4) at each rank's exact distance deletes **983**, leaving 986.

Second, for each dyadic band from `2^24` through `2^35`, divide the RL208
backward layer into 4,096 equal sublayers.  In each sublayer `(N_prev,N]`, use N
only as an outer consequence of the pointwise theorem (4), intersect with the
already-required RL208 coarse safe band, and count only the newly excluded rank
rectangles.  Exact modular floor sums give, by octave:

- `2^24..2^25`: 13
- `2^25..2^26`: 63
- `2^26..2^27`: 241
- `2^27..2^28`: 970
- `2^28..2^29`: 3,893
- `2^29..2^30`: 15,517
- `2^30..2^31`: 62,044
- `2^31..2^32`: 248,182
- `2^32..2^33`: 740,166
- `2^33..2^34`: 1,925,308
- `2^34..2^35`: 4,743,660.

Those sublayers contribute 7,740,057.  Together with the exact 983 root-window
cuts, RL209 deletes exactly

**7,741,040 previously surviving above-p necessary ranks.**          (5)

The verifier proves there are zero hits on the inherited isolated/anchor
deletions, so (5) is disjoint from all previous cuts.  The below-p frontier is
unchanged.  The exact new counts are

- canonical `a>p`: **7,091,831,284**;
- canonical `a<p`: **6,324,034,587**;
- total necessary terminals: **13,415,865,871**.

No materialized multi-billion-element set is used or claimed.

## 5. Scoped signed-successor barrier

At a noncarry H21 terminal the inherited signed next increment is

`K_(i+1)-K_i=sigma*rho_i*(2^nu-1)/(3*2^21)`,

where `sigma in {+1,-1}` and `1<=nu<=21`.  Since
`K_i=rho_i*T/2^21`, this is equivalently

`K_(i+1)=K_i*(1+sigma*(2^nu-1)/(3T))`.               (6)

The verifier checks (6) against the independently anchored pointwise corridor at
phase `i+1` for every one of the 986 exact root-window survivors and every one of
the 42 sign/valuation pairs: **41,412 exact cases**.  All pass.

Therefore this particular signed-successor/root-anchor consumer selects neither
sign nor valuation on that precisely named survivor set.  This is a scoped
method barrier, not a theorem that signed successor-K information can never work
elsewhere or with an additional global datum.

## 6. Classification and locks

- Equations (1)-(2): proved analytic above-p decomposition/information boundary.
- Equations (3)-(4): proved analytic pointwise root-anchor theorem.
- Equation (5): exact finite disjoint rank-exclusion certificate.
- Section 5: exact finite scoped consumer barrier.

No eta class is removed; no state/sign/valuation selector is proved; no physical
H21 incidence or charge is proved; the sole high branch is not contradicted.
Gate A remains globally open, Gate B remains globally open, and global
nontrivial-cycle exclusion remains open.
