# RL195 — Physical Zero-Edge Incidence and Exact Window Ownership

Date: 2026-08-31
Incoming handover: RL194; completed incoming job: RL195; successor: RL196.
BASE_HEAD: `df980ce3df6fa3e8906a934692221917af25644a`.

## 0. Outcome and scope

RL195 proves that a hypothetical physical word on the sole high branch has
at least **9,719,139,553 chronological edges whose two endpoints have height
zero**. Denote this actual edge count by J00; the new proof notes locally
call it J, unrelated to the branch parameter J=23.

The weighted rank moment and the mechanical digit structure are both needed.
Occupation alone is insufficient: explicitly scoped height-only words can
have more than the inherited zero-height floor but only the mandatory edge,
or a whole p-window without zeros. Neither word satisfies the complete
incoming physical assumptions.

RL195 also identifies an exact arithmetic boundary. A complete admissible
height word has a unique positive rational cyclic orbit; one dyadic
normalized p-gap forces that orbit to be positive odd-integral. Thus an
exact K0=2^37 moment already enforces integrality for a complete word,
whereas necessary intervals and local graph survivors do not.

Every accepted depth3 owned parity path has infinite positive odd witnesses
in the uncoupled local relaxation, even with compatible initial odd-modulus
conditions. All34,039 final paths are covered, not merely one path per root.
This is a precise local-method barrier, not a physical p-edge realization.

RL194's necessary-rank cardinality **27,057,465,824**, canonical terminal
floors **190574 / 1826072**, actual zero-height vertex floor
**43,742,681,439**, and all inherited H21/spacing/flow bounds are unchanged.
No extremal atom is excluded or realized, and no branch or global gate is
closed. Sections2--6 restate the unchanged incoming mathematical state;
sections7--10 give the new RL195 results and their boundaries.

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
`h_i=floor(Ai/L)-S_i`, where `S_i=sum_(j<i)a_j` and a_j are actual positive
acceleration exponents. Thus universally, including switches/carry/seam,
`h_(i+1)=h_i+c_i-a_i`, so `h_(i+1)<=h_i+c_i-1<=h_i+1`.
The special carry belongs to the p-gap, not to this one-step height law.
With ordinary target `j=(i+p) mod L`, define
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

## 2. Inherited global rank order and exact corridor cut

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

## 3. Inherited chronological weighted-speed filter and final rank-set rule

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

## 4. Inherited rank signs, positive windows, and physical height occupation

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

## 5. Inherited owned first-transition sign restriction

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

RL194's spacing wording clarification remains recorded. No inherited
mathematical correction/demotion is introduced by RL195. The unpromoted
owned-helper interface repair is recorded separately below and in the
correction ledger. All branch and global closure obligations remain open.

## 7. New physical moment-to-chronological-edge incidence

Let x_r indicate h_(I(r))=0 and
`Z0=sum_(1<=r<L)d_r*x_r`. The incoming moment gives
`Z0>=M=2F-3rho_z+1`, with F=3(lambda-1)K0.

The c=1 sources r in[0,R) have disjoint successors r+B in[B,L); height
zero propagates across them. In particular h0=h1=0 and the edge0->1 is
mandatory. The c=2 doublets have first rank r in[2R,L), second rank r-R
in[R,B); the other c=2 sources are singletons[B,2R).

For every first c=2 doublet, the two d-weights have the same eta/theta coefficient because
neither canonical coefficient-boundary predecessor R nor R+1 is in[2R,L).
Thus d_(r-R)=4d_r/3. The binary doublet inequality and low-rank propagation
give the exact physical charging bound

`Z0<=C+sum_(1<=r<R)d_r*J_(I(r))+sum_(2R<=r<L)d_r*J_(I(r))`,

where J_i indicates h_i=h_(i+1)=0 and
`C=sum_(R<=r<2R)d_r=3(1+theta)/16`.
The charged source sets are disjoint and exclude phase0. Every charged
weight is <theta, and exact constants prove M>C. Therefore

`J00-1>(M-C)/theta=(2F-11/16)/theta-27/16`,

whose right side lies strictly between9719139551 and9719139552. Hence
**J00>=9719139553**. The independent higher-order rational replay agrees.
This is an actual chronological incidence theorem, not the invalid
unweighted inference2N0-L and not an H21/p-shifted pair count.

Full proofs: `proofs/RL195_MOMENT_TO_ZERO_ADJACENCY.md` and
`proofs/RL195_ZERO_GEOMETRY_AND_RELAXATION_BARRIERS.md`.

## 8. Exact global window normalization and the odd denominator

For any complete nonnegative periodic height word with h0=0 and all
`a_i=c_i+h_i-h_(i+1)>=1`, define q by the operating definitions. It has
the unique positive rational cyclic affine orbit

`y_i=Y_i/[3(lambda-1)q_i]`.

Put `D=2^A-3^L` and `d=3^p-2^u0`. With cumulative exponents s_(i,k),
write `R_i=sum_(k=0)^(L-1)3^(L-1-k)2^s_(i,k)` and use the analogous
p-arc numerator P_i. Then

`y_i=R_i/D`, `2^a_i R_(i+1)=3R_i+D`,
`Delta_i=(d*y_i+P_i)/2^(u0+h_i)`.

All R_i are positive odd integers. The y_i share the reduced odd denominator
`D/gcd(D,R0)`. Bezout Ap-u0L=1 proves gcd(D,d)=1 symbolically,
so the odd part of each reduced Delta denominator is exactly the same.
Consequently one dyadic normalized gap is equivalent to the complete
reconstructed orbit being positive odd-integral. At phase0, Delta0=K0;
the exact equation alpha*C0+beta*Y0=3*2^37 thus forces odd integrality.

This does not construct a complete admissible word satisfying that equation.
The inherited q*y telescope and corrected owned-gap formula are explicitly
restatements from RL175/RL181. A numerical moment inequality or local prefix
is not an exact normalization and does not inherit this equivalence.
See `proofs/RL195_PHYSICAL_WINDOW_RECONSTRUCTION_AND_DENOMINATOR.md`.

## 9. Complete local odd-witness certificate and its precise barrier

For each accepted path of the owned parity graph, exact finite acceleration
words impose a single compatible dyadic seed class on the initial owned
line. Endpoint oddness implies exact valuations at every preceding step.
Every class has arbitrarily large positive members, and any compatible
initial odd-modulus class can be adjoined by the coprime-modulus argument.

The certificate covers all42 initial unequal maximum21 pairs, C=3^37,
the entire common mechanical word212 and every path through depth3.
Full path counts are540 /4517 /34039; all44 four-source sign patterns have
local positive odd witnesses. The earlier merged-state/edge counts remain
540/540,4202/4517,25417/30977 and are distinct statistics.

Every path is replayed at two members of its seed family with t=1 modulo3^5.
An independent replay also checks every final path with t=0 modulo3.
Neither choice supplies actual p-step coupling, period closure, a shared
global height word, the extremal prehistory, K/window bounds or H21 ownership.
Thus local positivity, exact finite forward consistency, lower size bounds
and compatible initial odd-modulus constraints alone cannot exclude a path.

During review a general helper assertion incorrectly rejected initial
multiples of3. It was repaired and336 helper cases passed; the original
full replay, counts and witness digest are unchanged. No inherited proof
state was demoted. See `proofs/RL195_OWNED_LOCAL_REALIZABILITY.md`.

## 10. Height-only countermodels and the RL196 obligation

Two actual-constant constructions are explicitly height-only relaxations:

- Zero ranks `{0} union[R+1,2R-1]`, all other heights1, give N0=R and
  J00=1 exactly. Their Z0=C-d_R<C fails the physical lower bound M>C.
- Height1 exactly on chronological[2,p+2), height0 elsewhere, gives N0=z
  but no height-zero vertex in that whole p-window. It omits the exact
  K0 moment and fails the inherited h_p=0 anchor.

Both satisfy the actual positive-exponent height law and h0=0. They are
not odd-orbit or high-branch realizations. They show precisely why global
occupation alone, even with the local height law, does not supply the
desired physical window incidence. Complete rank cells and exact boundary
checks establish the stated relaxed witnesses without a giant phase scan.

RL196 must couple actual zero-edge placement to p-shifted/global ownership,
or control existence of a complete height word satisfying the exact fixed
gap. The target is `RL196_ZERO_EDGE_PLACEMENT_AND_GLOBAL_P_SHIFT_COMPATIBILITY_TARGET.md`.
Do not replace global compatibility by the local CRT theorem, do not infer
H21 ownership from J00, and do not extend a finite cutoff automatically.
