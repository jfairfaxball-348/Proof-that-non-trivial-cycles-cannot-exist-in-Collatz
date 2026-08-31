# RL194 — Rank Order, Weighted Speed, Height Occupation, and Owned Prefix

Date: 2026-08-31
Incoming handover: RL193; completed incoming job: RL194; successor: RL195.
BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.

## 0. Outcome and scope

RL194 proves physical sign/weight constraints that survive the RL193 total-
identity barriers.  It does **not** exclude or realize either extremal atom,
close the sole high branch, or close any global gate.

The necessary extremal core is tightened by a global rank-order theorem and
an exact chronological prefix-speed certificate.  The combined remaining
rank set has cardinality **27,057,465,824**, not a claimed number of physical
terminals.  Canonical lower/upper terminal phases must be at least
**190574 / 1826072**.  Independently, every hypothetical physical high-branch
word has at least **43,742,681,439 actual height-zero phases**.  That is a
different statistic; it is not an H21, clean-start, pair or terminal count.

Positive moving-window identities and an owned-numerator sign table provide
the next structural inputs.  All H21 charging and inherited spacing/flow
scope remain unchanged.

## 1. Portable operating definitions

The branch remains `(v,H,J,d)=(37,0,23,-1)`.  Constants:

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`R=2L-A=57079296007`, `p=65470613321`, `u0=103768467013`,
`Ap-u0 L=1`, `z=L-p=72057431991`, `Q=37B mod L=88514772733`.

Canonical phases are `0<=i<L`; rank is `r_i=iB mod L`, with inverse
`I(r)=pr mod L`.  The mechanical bit is

`c_i=floor(A(i+1)/L)-floor(Ai/L)`,

equal to 1 for rank below R and 2 otherwise.  A length-n word beginning at
rank r has exponent sum `floor((r+nA)/L)`.

The physical nonnegative integral heights h_i are L-periodic, h_0=0, and
`h_(i+1)<=h_i+1`.  With ordinary target `j=(i+p) mod L`, define
`G_i=h_i-h_j`; at the unique carry source z use `G_z=1+h_z`.

`rho_i=2^floor(Ai/L)/3^i`, `v_i=2^(-h_i)`, `q_i=rho_i v_i`,
`epsilon_i=v_i(2^G_i-1)`, `f_i=rho_i epsilon_i`.

Thus ordinary errors are `v_j-v_i` and the carry error is `2-v_z`.
The corrected gap K and normalized gap Delta satisfy

`K_0=K0=2^37`, `Delta_i=K_i/rho_i`,
`f_i=3(K_(i+1)-K_i)`,
`2^c_i Delta_(i+1)=3Delta_i+epsilon_i`.

Put `delta=A ln2-L ln3`, `lambda=2^A/3^L=exp(delta)`.  In the lift,
K, rho and q scale by lambda after L phases; h, G, epsilon and Delta are
periodic.  For canonical i,

`1/2<rho_i<=1`, `Klow=128081997553<K_i<Kup=146795909391`,

with rho_i=1 only at i=0, and `0<delta<2^-40`.

A physical extremal `{35,36,37}` terminal has a tau=37 zero-defect prefix,
ordinary terminal maximum height21, terminal Delta=`3^37/2^21`, and prefix-
start Delta T=`2^38` below terminal rank Q or `2^37` above Q.  Its incoming
rank core was `E=[72797034370,103818202602]` minus24 isolated RL193 deletions.
The anchored early signature is `G_0=...=G_23=0`,
`G_24,...,G_28<0`, `G_29!=0`.  The inherited early-window verifier is bundled.

For an ordinary owned pair of positive odd orbit states X=y_i, Z=y_(i+p),
put g=h_i-h_(i+p).  Its exact numerator is

`C=2^g Z-X` for g>0, `C=Z-2^(-g)X` for g<0, `C=Z-X` for g=0,

and `Delta=C/2^max(h_i,h_(i+p))`.  C is odd when g!=0 and even when g=0.
At an extremal terminal C=`3^37`.  Ordinary acceleration obeys
`3X+1=2^alpha X'`, `3Z+1=2^beta Z'`; the proof note uses these local exponent
names independently of the global window coefficient alpha below.

## 2. Global rank order and the exact corridor cut

For canonical ranks r_j-r_i=d>=1,

`L log(rho_i/rho_j)=d ln2+(i-j)delta>d/2`.

This uses `ln2>2/3` and `(L-1)2^-40<1/6`; it covers every rank pair
analytically.  It proves reverse rank order, not monotonicity in time.

For terminal rank r, let `a(r)=((r-Q)p) mod L`.  Both atoms have the same
necessary start-K comparison value

`K_required(r)=K0 exp(((Q-r)ln2+a(r)delta)/L)`.

At a physical terminal it equals K_a and K_terminal.  This function strictly
decreases through both atoms and their seam.  Four exact rational logarithm
endpoint checks therefore prove the complete corridor-test core

`75446746413<=r<=102504571503`.

Its intersection with the old isolated-deletion rule leaves22 deletions and
27,057,825,069 necessary ranks.  The full list, exact endpoint margins and
gap-free monotonicity argument are in `proofs/RL194_RANK_ORDER_AND_CORRIDOR.md`.

The closest undeleted ranks Q-2 and Q+1 also strengthen the actual canonical
prefix signs to

`3(K_a-K0)>417/100` on the lower atom,

`3(K_a-K0)<-19/10` on the upper atom.

These remain true after the further finite filter below.

## 3. Chronological weighted-speed filter and final rank-set rule

For a<z, the canonical prefix contains no carry and `|f_i|<rho_i`.
The anchored early signature sharpens its positive and negative envelopes:

`0<F_a<sum_(29<=i<a)rho_i` on the lower atom,

`0<-F_a<sum_(24<=i<a)rho_i` on the upper atom,

where `F_a=3(K_a-K0)`; smaller empty-sum cases are handled separately.
These are actual chronological bounds, not an inference from total variation.

An exact certificate covers every start `1<=a<=1826035`.  It uses valid
coarse integer rejection tests, 96-bit outward-rounded rho recurrences, and
exact rational logarithm/exponential comparisons at every remaining candidate.
All interval comparisons resolve.  Independent128-bit replay with a different
coarse filter reproduces the same boundaries and counts.

The first lower/upper compatible starts are190537 /1826035.  Adding37 gives
canonical terminal floors190574 /1826072.  Boundary compatibility is not
physical realization.  The old canonical terminal floor already rules out
wrapped starts; the known early window separately excludes a=0.

Exactly ten corridor/isolated-filter ranks survive this speed test in the
entire scanned range.  They and their start phases are listed in
`proofs/RL194_CHRONOLOGICAL_WEIGHTED_SPEED.md`.  The scan removes359245
additional ranks (173499 lower,185746 upper), leaving **27057465824** in the
combined necessary set.

The final membership rule is precise:

1. require r in `[75446746413,102504571503]`;
2. remove the22 inherited isolated ranks listed in the rank-order proof;
3. compute `a=((r-Q)p) mod L`; for `1<=a<=1826035`, retain only the ten
   listed speed-envelope survivors; outside this range the new finite filter
   makes no decision.

This defines an exact necessary-rank set, not a physical population or a
separation theorem.  The inherited carry buffers remain11/5 and4/7.

## 4. Rank signs, positive windows, and physical height occupation

Define the global coefficients

`alpha=3^p/2^u0>1`, `eta=alpha-1`, `theta=lambda alpha-1>eta`,
`beta=eta/(lambda-1)>0`.

The carry-completed identity `f_i=alpha q_(i+p)-q_i` is an inherited RL181
restatement.  In this identity q_(i+p) is lifted, not silently reduced to a
canonical value.  Also `rho_z=lambda alpha/2`.

Let `w_r=rho_(I(r))`, `V_r=v_(I(r))`, `d_r=w_(r-1)-w_r>0`.  Every
carry-free rank-initial flow sum satisfies the exact identity

`sum_(r<m)w_r(V_(r+1)-V_r)`

`=-w_(m-1)(1-V_m)-sum_(1<=r<m)d_r(1-V_r)<=0`, `1<=m<L`.

Equality means all heights at ranks1..m are zero.  A chronological prefix
is generally not rank-initial; no time-order conclusion is substituted.

For lifted windows `C_i=sum_(i<=j<i+p)q_j`, `Y_i=sum_(i<=j<i+L)q_j`,
the new positive inversion is

`3K_i=alpha C_i+beta Y_i`.

For canonical a and `P_a=sum_(0<=i<a)q_i`, it gives

`3(K_a-K0)=alpha(C_a-C_0)+eta P_a`.

Thus the upper atom requires `C_a<C_0-(1-alpha^-1)P_a`; the lower requires
the reverse strict inequality, not necessarily C_a>C_0.

Writing `Q_mass=sum_(0<=i<L)q_i`, the moment at phase zero certifies

`67236063233<Q_mass<80336439250`.

The exact full-period rank moment is

`F=3(lambda-1)K0=2rho_z-1+sum_(1<=r<L)d_r V_r`.

With `N0=#{i mod L:h_i=0}`, integral positive heights give V<=1/2 off
height zero.  Because every d_r<theta, the moment yields

`N0-1>(2F-1/2)/theta-3/2>43742681437`,

hence **N0>=43742681439**.  All numerical comparisons have exact rational
log/exp certificates.  This is an actual physical vertex-occupation theorem,
conditional on the branch.  It is not a terminal/rank count and does not
supply H21 incidence.  The full proof and rounding are in
`proofs/RL194_WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md`; Q there locally
denotes Q_mass, not the terminal-rank split.

## 5. Owned first-transition sign restriction

All42 ordered unequal terminal-height pairs of maximum21 have owned C=3^37.
The first three mechanical transitions have common ordinary word212 on all
incoming E, a superset of the final core.  The exact owned transition gives
first-step sign persistence except at initial g=+3 or g=-1.

An immediate zero return occurs only through:

- `(h,hp)=(21,18)`, local exponents `(4,1)`, successor
  `(19,19,(3^38+7)/16)`;
- `(h,hp)=(20,21)`, local exponents `(1,2)`, successor
  `(21,21,(3^38-1)/4)`.

Both successor numerators have valuation1, so neither can remain zero at
the next transition: `not(G_(t+1)=0 and G_(t+2)=0)`.

The complete depth3 necessary-state certificate has540,4202,25417 states.
Every one of the42 initial pairs survives this particular parity filter.
This is a narrowly scoped filter barrier, not a physical realization or a
barrier to stronger congruence methods.  No depth>=4 propagation is certified.
See `proofs/RL194_OWNED_PREFIX_INTERFACE.md` for the full sign/exponent table.

## 6. Preserved inherited facts and successor obligation

RL191 retains distinct-extremal spacing>=1001, `N35<=7559400754`, ordinary
absolute corrected flow `>24171310097/50331648>480`, and each directional K
variation `>24171310097/301989888>80`.  Neither RL194's canonical floors nor
its rank-cardinality reductions improve that spacing or convert variation
into excursion.

The H21 `{33,34,35}` family remains binding, with core
`D_H21=[23369453298,41775866136]` minus the same14 RL193 ranks:

`23369453298,23783761791,26058127773,26058127774,28746802249,28746802250,`
`31435476726,34124151202,36398517184,36398517185,36812825678,39087191660,`
`39087191661,41775866136`.

Its canonical terminal floor67, budget and physical-incidence obligations
are unchanged.  The inherited RL193 total weighted-debt and total-valuation
barriers remain: neither total identity alone excludes the full-period atoms.

RL195 must couple the new positive-window/occupation structure to physical
locations, or use an owned sign-order constraint not already erased by total
summation.  No mathematical correction/demotion is recorded.  A candidate
scope phrase was clarified to preserve the inherited spacing explicitly.
All branch and global closure obligations remain open.
