# RL36 — order-2 synchronized-excursion charging and two-mode factor recovery

Date: 2026-08-21

## Status

Sections 1--8 are **ANALYTIC** in the `g=2` balanced-return branch, under the inherited near-resonant least-state hypotheses.  The bundled verifier is an **EXACT FINITE / SYMBOLIC SANITY CERTIFICATE** only.

This note does **not** close RL or the full order-2 branch.  It supplies a new global-to-sparse interface: the relative prefix-count path splits into synchronized runs and one-sided excursions.  Every excursion forces high odd-state/valuation charge, while the gap factor localizes the first and last disagreement.  The only remaining way to avoid a large excursion charge is to place a large fraction of the odd mass on common synchronized odd steps between excursions; that is now the precise anchor population to attack with an RL35-style successor/slack theorem.

## 1. Setup

Retain the inherited half-balanced notation

`A=2a`, `L=2ell`, `X=2^a`, `Y=3^ell`, `z=X/Y>1`,

with least state `R`, balanced half-cycle state

`x=R+G`, `G>0`,

and equal-density half words `u,v` of length `a` and weight `ell`:

`T^a(R)=x`, `T^a(x)=R`.

The exact block equations are

`U=Q(u)=Xx-YR`,

`V=Q(v)=XR-Yx`,

so

`U+V=(X-Y)(R+x)`,                                      (R36.1)

`U-V=(X+Y)G`.                                          (R36.2)

In the inherited near-minimum branch both `R,x` are odd and `4|G`.

For aligned trajectories put

`u_j=T^j(R)`, `v_j=T^j(x)`,

`p_u(j)=# {i<j:u_i is odd}`, `p_v(j)=# {i<j:v_i is odd}`,

`d_j=p_v(j)-p_u(j)`,

`q_u(j)=2^j/3^{p_u(j)}`, `q_v(j)=2^j/3^{p_v(j)}`.

Thus `d_0=d_a=0` and

`q_v(j)=q_u(j) 3^{-d_j}`.                              (R36.3)

## 2. Exact scaled-state windows

Along an affine parity segment, the scaled quantity `q_j state_j` is unchanged on an even step and increases by `q_j/3` on an odd step.  Therefore it is nondecreasing.

For the first half trajectory,

`R <= q_u(j)u_j <= z x`.                                (R36.4)

For the second,

`x <= q_v(j)v_j <= z R`.                                (R36.5)

The upper endpoint in (R36.5) is larger than `x` because `V>0` gives `zR-x=V/Y>0`.

Since every cycle phase is at least `R`, (R36.4)--(R36.5) imply the following pointwise imbalance-height theorem:

> **If `d_j>0`, then `v_j >= 3^{d_j} R/z`.**              (R36.6)
>
> **If `d_j<0`, then `u_j >= 3^{|d_j|} R/z`.**            (R36.7)

Proof for `d_j>0`: from `u_j>=R` and (R36.4),

`q_u(j)<=zx/R`.

Then using (R36.5),

`v_j >= x/q_v(j)=3^{d_j}x/q_u(j)>=3^{d_j}R/z`.

The other sign is symmetric.

Thus every unsynchronized column carries a phase whose height grows exponentially with the prefix-count imbalance.

## 3. Maximal excursions and high odd-state ownership

A **maximal excursion** is an interval `[s,t]` with

`d_s=d_t=0`,

and `d_j` has one fixed nonzero sign for every `s<j<t`.

Let

`h=t-s`

be its length and `p` the common number of odd bits in each of the two length-`h` segment words.  If the excursion is positive (`d_j>0` inside), the `v` segment is the **leading** segment; if it is negative, the `u` segment is leading.

The leading segment begins with an odd bit.  For a positive excursion, for example, the departure from `d_s=0` has `(u_s mod2,v_s mod2)=(0,1)`, so `v_s` is odd and `d_{s+1}=1`.

By (R36.6),

`v_{s+1} >= 3R/z`.

Since `v_s` is odd and `T(v_s)=v_{s+1}`,

> **`v_s >= 2R/z - 1/3`.**                               (R36.8)

Every later odd state of the leading segment occurs at an interior column with nonzero imbalance, so by (R36.6) or (R36.7) it is at least

> **`3R/z`.**                                             (R36.9)

Hence an excursion of common weight `p` owns `p` distinct odd cycle states:

- its first leading odd state is at least `2R/z-1/3`;
- its remaining `p-1` leading odd states are at least `3R/z`.

This is an integrality-sensitive statement: it uses the actual odd transition at the excursion boundary and the least-state scaled windows.

## 4. Excursion length is paid by outgoing valuation

Let the leading segment's odd positions be

`s=i_1<i_2<...<i_p<t`.

For a genuine integer cycle, the outgoing odd-map valuation `nu(i_k)` is the number of full-parity steps from that odd phase to the next odd phase.  Therefore

`nu(i_k)=i_{k+1}-i_k` for `k<p`,

and

`nu(i_p)>=t-i_p`.

Summing gives

> **the `p` high odd states owned by an excursion have total outgoing valuation at least `h`.**  (R36.10)

Maximal excursions are disjoint aligned intervals, and their leading odd states are distinct full-cycle phases.  Therefore, if the excursions have lengths `h_i` and weights `p_i`, and

`H=sum h_i`, `P=sum p_i`,

then there is a set of `P` distinct odd cycle states satisfying the height bounds above and whose outgoing valuations sum to at least

> **`V_charged >= H`.**                                   (R36.11)

This is the order-2 analogue of the RL35 philosophy: unsynchronized structure pays both a product-height charge and a valuation charge.

## 5. Synchronized rotations preserve both proper factors

At any synchronization time `s` with `d_s=0`, rotate the two half words simultaneously:

`u^(s)=u[s:] v[:s]`,

`v^(s)=v[s:] u[:s]`.

Equal prefix odd counts ensure both rotated words still have length `a` and weight `ell`.  Let their numerators be `U_s,V_s`.

They map the synchronized state pair into each other, so exactly

> **`U_s+V_s=(X-Y)(u_s+v_s)`,**                           (R36.12)
>
> **`U_s-V_s=(X+Y)(v_s-u_s)`.**                           (R36.13)

Thus both coprime proper factors remain visible at every equal-count synchronization; this is stronger than merely knowing full-`D` rotation divisibility.

### Absolute factor recovered from the first common odd step

Because `R,x` are both odd, `u_0=v_0=1` and `s=1` is synchronized.  Put `A_s=U_s+V_s`.  Since

`u_1+v_1=[3(R+x)+2]/2`,

(R36.12) gives the exact bounded-coefficient identity

> **`2A_1-3A_0=2(X-Y)`.**                                 (R36.14)

So the absolute factor `X-Y` is already exactly recoverable from two adjacent synchronized rotations.

### Relative factor recovered up to the odd part of the physical gap

Let

`r=v2(G)`.

The inherited integer-gap synchronization theorem gives a common prefix of exactly `r` bits.  If that prefix contains `p` odd bits, then at the first divergence

`v_r-u_r=3^p G/2^r`.

Put `B_s=U_s-V_s`.  From (R36.13),

`B_0=(X+Y)G`,

`B_r=(X+Y) 3^p G/2^r`.

Hence

> **`gcd(B_0,B_r)=(X+Y) G_odd`,**                          (R36.15)
>
> where `G_odd=G/2^{v2(G)}`.

Thus the only obstruction to exact two-rotation recovery of the relative factor is the odd part of the physical balanced gap.

## 6. First/last disagreement localization from the gap factor

The fixed-weight first-disagreement lemma gives

`v2(U-V)=` first differing bit position of `u,v`.

Since `X+Y` is odd, (R36.2) implies

> **the first disagreement occurs exactly at `v2(G)`.**   (R36.16)

There is a useful terminal analogue at the level needed here.  Suppose the words share a common terminal suffix of weight `q`.  Because their total weights are equal, removing that common suffix leaves equal-weight prefixes, and the concatenation identity gives

`U-V=3^q (U'-V')`.

Since `3` does not divide `X+Y`,

> **every common terminal suffix has odd weight `q<=v3(G)`.**  (R36.17)

So a small physical quotient `G` prevents the two words from hiding most of their discrepancy in arbitrarily long common prefix/suffix ownership.

## 7. Packing-or-synchronized-anchor decomposition

Let the maximal excursions have weights `p_i`, and let

`P=sum p_i`.

Let `C` be the number of common odd bits lying in synchronized regions strictly between the first and last excursion.  The common prefix before the first excursion contains at most `v2(G)` odd bits, and the final common suffix contains at most `v3(G)` odd bits.  Therefore

> **`P+C >= ell-v2(G)-v3(G)`.**                            (R36.18)

This is the new bridge decomposition.

- The `P` excursion odd steps are paid by `P` high odd states and valuation charge `H` via (R36.8)--(R36.11).
- The only way to keep `P` small is to make `C` large: a large population of **common synchronized odd anchors** between excursions.

That is a much narrower residual problem than the original simultaneous-factor branch.  It identifies the correct RL35-style next target: prove that repeated common synchronized odd anchors cannot occur at near-extremal packing cost without a compensating excursion/high-valuation charge.

### One-excursion corollary

If there is exactly one excursion, then `C=0`, so its common weight `p` obeys

> **`p >= ell-v2(G)-v3(G)`.**                              (R36.19)

Consequently all but at most `v2(G)+v3(G)` of the half-block's odd mass lies on the charged leading trajectory.  The branch then owns at least that many high odd states, with all but one at height at least `3R/z`.

The inherited RL21 gap-factor countermodel has `G=4`, `ell=41`, one excursion of weight `39`, and saturates (R36.19):

`39=41-v2(4)-v3(4)=41-2-0`.

That rational model therefore sits exactly on the new localization boundary; what it lacks is genuine integer parity ownership / full simultaneous-factor integrality.


## 8. Transport area is exact sparse support

The same excursion path has a second invariant that links the global combinatorics directly to sparse exponential algebra.  Define the **transport area**

`rho=sum_{j=0}^{a-1} |d_j|`.                              (R36.20)

For two binary words of equal weight this is exactly the minimum number of adjacent transpositions `10 <-> 01` needed to transform `u` into `v`.  Equivalently, if the ordered odd positions are

`i_1<...<i_ell` in `u`, `j_1<...<j_ell` in `v`,

then

> **`rho=sum_{m=1}^ell |i_m-j_m|`.**                      (R36.21)

This standard one-dimensional transport identity has an especially useful exact affine consequence here.  If an equal-weight word `w` contains `10` at positions `i,i+1`, and `w'` is obtained by replacing that pair by `01`, let `k` be the number of odd bits strictly to the right of `i+1`.  Directly from the definition of `Q`, all unchanged contributions cancel and

> **`Q(w')-Q(w)=2^i 3^k`.**                               (R36.22)

The reverse swap has the negative of this increment.

Choose any minimum adjacent-swap path from `u` to `v`.  It has exactly `rho` swaps.  Telescoping (R36.22) gives an exact representation

> **`U-V=sum_{m=1}^rho epsilon_m 2^{i_m}3^{k_m}`,**        (R36.23)
>
> with `epsilon_m in {+1,-1}`.

After collecting repeated monomials, the support has cardinality at most `rho`; no approximation or modular reduction is involved.  Combining with the proper gap factor (R36.2) gives

> **`(X+Y)G=sum_{m=1}^rho epsilon_m 2^{i_m}3^{k_m}`.**     (R36.24)

Thus the order-2 branch has an exact **packing-or-sparse** bridge:

- small `rho` forces the full relative-factor equation into a genuinely low-support `2`--`3` exponential relation;
- large `rho` is global transport area.  By (R36.6)--(R36.7), every unsynchronized column `j` contributes a state at least `3^{|d_j|}R/z`, so over the `H` unsynchronized columns

`sum_{d_j != 0} log_3(max(u_j,v_j)/R) >= rho-H log_3(z)`. (R36.25)

Equation (R36.25) is only an aggregate height inequality; it is **not yet** a product contradiction because the selected phases and the global product budget must still be matched without double counting.  But it places the two residual regimes on the right sides of the existing machinery: low transport goes to sparse uniqueness, high transport goes to global packing/height charging.

For a maximal excursion `E=[s,t]`, its local area

`rho_E=sum_{s<j<t}|d_j|`

is likewise the minimum adjacent-swap distance between its two local equal-weight segment words.  Hence the exact excursion contribution in the decomposition used by the verifier is itself a signed sum of `rho_E` monomials.  Multiple excursions therefore do not destroy sparsity; their local sparse relations simply concatenate, with total pre-collection length `rho=sum_E rho_E`.

### Relation to the already closed radius-3 theorem

This does **not** mean radius-3 closure automatically settles every case with small `rho`.  A minimum adjacent-swap path is not the same object as the specific cyclic rotations covered by the inherited exact-radius-3 theorem, and a half-block transport distance can be larger than the cyclic Hamming/radius parameter.  What (R36.23)--(R36.24) supplies is the missing exact interface: any future low-support uniqueness theorem can now be invoked on a quantity canonically generated by the global order-2 branch, rather than on an ad hoc local pattern.

## 9. What is proved and what remains

### New analytic resources

1. Pointwise exponential height from prefix-count imbalance, (R36.6)--(R36.7).
2. Every maximal excursion owns `p` high odd states and valuation at least its length, (R36.8)--(R36.11).
3. Both proper factors persist under synchronized rotations, (R36.12)--(R36.13).
4. Exact two-rotation recovery of `X-Y`, (R36.14).
5. Recovery of `X+Y` up to `G_odd`, (R36.15).
6. First/last disagreement localization by `v2(G),v3(G)`, (R36.16)--(R36.17).
7. The packing-or-synchronized-anchor dichotomy, (R36.18), and the strong one-excursion corollary (R36.19).
8. Exact transport-area-to-sparse-support conversion, (R36.20)--(R36.24), plus the aggregate height inequality (R36.25).

### Still open

This does **not** yet exclude multiple-excursion solutions.  The residual obstruction is explicit: many common synchronized odd anchors can sit between excursions.  A local claim that a deep resynchronization requires a proportionally long immediately preceding excursion remains false and is not used here.

The highest-value next theorem is therefore a two-regime closure that combines synchronized-anchor charging with the transport bridge:

> **Synchronized-anchor charging target.**  In the `g=2` simultaneous-factor branch, bound the total number/product contribution of common synchronized odd anchors by the neighboring excursion charge, using the exact synchronized gap, the affine low-state maps, and the absolute-factor recovery (R36.14).

A fixed charge per bounded number of synchronized anchors would turn (R36.18) into a linear global arithmetic/product charge and would be a genuine branch-closing bridge candidate.

