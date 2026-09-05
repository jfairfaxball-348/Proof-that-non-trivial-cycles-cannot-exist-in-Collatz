# RL250 — beta=6 exact support lift and terminal-window covering checkpoint

Date: 2026-09-05
Classification: **R4_BRIDGE_REDUCED**.

## Promoted exact support results

For Branch C with `beta(P)=6`, let `c` be the number of positive components, `r2` the number of maximal `P=2` runs and `n2` the number of `P=2` roots. Then

`M_q=sum_i |P_(i+1)-P_i|=12+2c+2r2`,

so each mismatch orientation occurs exactly `6+c+r2` times. With `n1+2n2=8` and `n1>=c+r2`, exactly 19 `(c,r2,n2)` topology parameter classes are feasible.

Put `delta_i=P_(i+1)-P_i`. On each q-orbit, `delta_i=u_i-u_(i+q)` has a binary solution iff the nonzero signs of `delta` strictly alternate cyclically. In beta=6 every q-orbit is nonconstant, so the binary `u` is unique for `(P,q)`. In the two-orbit case, `sum_even P=sum_odd P=1`.

For the reconstructed word, `W_(i+1)(q)-W_i(q)=-delta_i`, hence `P_i+W_i(q)` is constant. Writing it as `r` gives exactly

`P_i=r-W_i(q)`, `ar-qell=2`.

Thus the q-orbit integrability condition lifts exact support data back to the determinant q-window relation.

## Independent resonance recovery and terminal tail

Writing `z=a-ell`, RL249's ratio gives

`41z/24 <= ell < z/(log_2(3)-1)`.

There is no integer ell for `z=46,47`; hence independently `z>=48`.

The inherited canonical word is `u=110 x 1 0^t`. RL248 gives internal-zero count `m=z-k+2`, `k>=31`. Since all word zeros total `z=1+m+t`,

`boxed: t=k-3>=28`.

## Terminal-window cover/packing lemma

From `P_i=r-W_i(q)` and `P_i in {-1,0,1,2}`, every q-window contains between

`D_q=q-r-1` and `U_q=q-r+2`

zeros. Every complementary `(a-q)`-window contains between

`D_c=z-q+r-2` and `U_c=z-q+r+1`

zeros.

For a cyclic interval of length `e`, define a forced-zero lower bound

- `tau(0)=0`;
- `tau(e)=e` for `1<=e<=28`;
- `tau(e)=28` for `e=29,30`;
- `tau(e)=29` for `e>=31`.

The last case uses the terminal 28 zeros plus the fixed zero at position 2 of prefix `110`.

If every cyclic length-L window contains between D and U zeros, put `n=ceil(a/L)`, `e=nL-a`. A family of n length-L windows covers the cycle once except for one overlap interval of length e, which can be rotated onto the forced-zero interval. Therefore

`boxed: z+tau(e)<=nU`.

Similarly put `m=floor(a/L)`, `g=a-mL`. There are m disjoint length-L windows leaving one gap of length g; rotate the gap onto the forced-zero interval. Therefore

`boxed: mD+tau(g)<=z`.

These inequalities apply with `L=q` or `L=a-q`. This is a new generic cyclic interval identity, not the RL249-demoted q-ordered covering formula.

## Exact elimination below z=289

Use exact integer tests

`41a<=65ell`, `2^a>3^ell`, `15*4^a<16*9^ell`, `a=ell+z`, and `ar-qell=2`.

For `46<=z<289` there are exactly 18 resonance triples. Two admit no determinant branch; the remaining 16 produce exactly 20 determinant branches. Every one violates at least one terminal-window cover/packing inequality. The exact portable verifier checks all 20 certificates.

Therefore

`boxed: z=a-ell>=289`.

At `z=289`, exact resonance leaves only `(a,ell)=(783,494)` and the determinant only `(q,r)=(317,200)`. Every q-window has 116..119 zeros. The terminal tail gives `t<=119`; since `783=2*317+149`, two disjoint q-windows plus a 149-gap placed over the tail and prefix zero give `289>=2*116+(t+1)`, so `t<=56`. Thus

`boxed: (a,ell,z,q,r)=(783,494,289,317,200), 31<=k<=59`

is the first arithmetic frontier not eliminated by this lemma.

## Verification / proof-state boundary

Fresh canonical-bundle verification: PASS. Exact verifier checks 19 topology classes, 1,324 small integrability instances, 18 resonance triples, 20 determinant branches, and 20 terminal-window contradictions.

Beta=6 Branch C remains live. Gate A/B remain open. Radius 4 is not invoked. Radius 5 is inactive.
