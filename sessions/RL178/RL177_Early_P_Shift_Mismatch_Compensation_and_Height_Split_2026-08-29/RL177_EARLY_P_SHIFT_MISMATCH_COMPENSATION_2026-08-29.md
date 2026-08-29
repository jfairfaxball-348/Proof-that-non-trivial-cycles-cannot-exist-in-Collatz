# RL177 — early p-shift mismatch compensation and height split

Date: 2026-08-29

## Outcome and classification

RL177 works the RL176 forced first p-shift mismatch in the preferred physical
branch `h_p=0`.  It does **not** close that branch.  It does convert the first
mismatch into an exact signed flow quantum, an unavoidable negative-flow
compensation floor, and a sharp split according to the common defect height at
the mismatch.

Retain
\[
G_i=S_{p+i}-S_p-S_i,
\qquad
F_2=\sum_i q_i(2^{G_i}-1)=3(\lambda-1)g_p,
\]
with
\[
1\le J\le36,
\qquad
v:=v_2(g_p)=S_J+\min(a_J,a_{p+J})\le37.
\]
Put
\[
d:=G_{J+1}=a_{p+J}-a_J\ne0,
\qquad H:=h_J=h_{p+J}.
\]

The new promoted results are:

1. **RL177.1 — consecutive lifted-defect pairing and first order crossing**
   (analytic): for `0<=i<=J`, `E_{p+i}=E_i+1`, so the paired physical states
   are consecutive in the lifted-defect/value order.  At `i=J+1`, the sign
   of `d` exactly determines whether the shifted state crosses below the
   unshifted state.
2. **RL177.2 — exact first-flow quantum and global compensation floor**
   (analytic):
   \[
   T_{J+1}:=q_{J+1}(2^d-1)
   =\operatorname{sgn}(d)\frac{(2^{|d|}-1)2^v}{3^{J+1}}.
   \]
   Hence `|T_{J+1}| >= (2/3)^37 > 3/10^7`.  If `N` denotes the total
   magnitude of all negative corrected-flow terms, then `N>3/10^7`.
3. **RL177.3 — zero-common-height finite interface** (analytic + exact finite
   certificate): if `H=0`, then `c_J=b_{J+1}-b_J=2`, `{a_J,a_{p+J}}={1,2}`,
   `|d|=1`, and `v=b_J+1`.  Under `v<=37` this leaves exactly 14 possible
   mismatch indices, hence 28 signed local types.  The first-flow magnitude
   is `rho_{J+1}/2>1/3`, so in every zero-height type the total negative flow
   satisfies `N>1/3`.
4. **RL177.4 — positive-common-height support and loss theorem** (analytic):
   if `H>=1`, then the global height profile has at least three distinct
   positive phases and
   \[
   R-Q>
   \frac32-2^{-H}-2^{-|d|-1}\ge\frac34.
   \]
   Consequently
   \[
   F_2<\rho_t-(q_p^{-1}-1)
   \left(\frac32-2^{-H}-2^{-|d|-1}\right)
   \]
   and uniformly in this branch
   \[
   F_2<\frac12-\frac{11\Delta}{16}.
   \]
5. **RL177.5 — exact local-automaton barrier** (exact finite certificate):
   the certified local rules alone still admit both mismatch signs and every
   valuation `v=2,...,37`.  Therefore no stronger `v_2(g_p)` modulus can be
   promoted from this local automaton alone.  The first-defect magnitude is
   nevertheless bounded by `|d|<=21`.  In the high branches, `v=36` forces
   `H>=1`; for `v=37`, the only `H=0` types are `J=23`, `d=+/-1`.

No cycle construction or exclusion is claimed.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`,

and

`b_j=floor(Aj/L)`, `h_j=b_j-S_j>=0`,
`q_j=2^(S_j)/3^j`, `rho_j=2^(b_j)/3^j`.

RL175/RL176 supply, in the preferred `h_p=0` branch,

- `E_p=1` and `y_p` is the unique second-smallest physical state;
- the corrected physical p-shift functional above;
- `F2<1/2-Delta/16`;
- `4 | g_p` and `4<=g_p<=185999999996`;
- the first mismatch `1<=J<=36` and exact valuation identity;
- the mechanical p-carry index `t=L-p=72057431991`;
- `rho_t=lambda/(2q_p)=exp(Delta+s)/2`, where
  `s=-log(q_p)` and `5Delta<s<6Delta`;
- `x=Delta+s<7Delta`, `x^2<Delta/16`, and the exponential estimate used in
  RL175.

RL168 supplies the internal lifted-defect state-order theorem:
`E_j<E_k` iff `y_j<y_k`, where `E_j=Aj-LS_j`.

The inherited external minimum `m>=2^71` remains external only.  RL177 does
not use it in any new core theorem.

## 2. Carry-free p-shift and lifted-defect pairing

For `0<=i<t`, the mechanical p-shift has no carry, so
\[
b_{p+i}=b_p+b_i.
\]
Since `h_p=0`, `S_p=b_p=u`, and therefore
\[
G_i=S_{p+i}-S_p-S_i=h_i-h_{p+i}.                 \tag{2.1}
\]
Also
\[
E_{p+i}
=A(p+i)-LS_{p+i}
=E_p+E_i-LG_i
=1+E_i-LG_i.                                    \tag{2.2}
\]
For `0<=i<=J`, RL176 gives `G_i=0`, hence
\[
E_{p+i}=E_i+1.                                   \tag{2.3}
\]
The `E` values are distinct integers, so there is no lifted defect strictly
between these two.  By RL168.1 the paired states `y_i,y_{p+i}` are therefore
consecutive in physical value order, with `y_i<y_{p+i}`.

At the first mismatch,
\[
E_{p+J+1}=E_{J+1}+1-Ld.                          \tag{2.4}
\]
Thus:

- if `d>0`, `E_{p+J+1}<E_{J+1}` and therefore
  `y_{p+J+1}<y_{J+1}`: the order crosses at the first defect;
- if `d<0`, `E_{p+J+1}>E_{J+1}` and therefore
  `y_{p+J+1}>y_{J+1}`: the order remains in the same direction.

This determines the physical order change from the sign of the corrected
defect; it does not determine that sign.

## 3. Exact first-flow quantum

Write
\[
a=a_J,\qquad b=a_{p+J},\qquad r=\min(a,b),
\qquad v=S_J+r.
\]
The first nonzero term of the corrected flow is at `i=J+1`.

If `d=b-a>0`, then `r=a`, so `S_{J+1}=v` and
\[
T_{J+1}
=q_{J+1}(2^d-1)
=\frac{(2^d-1)2^v}{3^{J+1}}.                    \tag{3.1}
\]
If `d=-e<0`, then `a=b+e`, `S_{J+1}=v+e`, and
\[
T_{J+1}
=q_{J+1}(2^{-e}-1)
=-\frac{(2^e-1)2^v}{3^{J+1}}.                   \tag{3.2}
\]
Therefore
\[
\boxed{
T_{J+1}=\operatorname{sgn}(d)
\frac{(2^{|d|}-1)2^v}{3^{J+1}}
}.                                               \tag{3.3}
\]
Since `v>=S_J+1>=J+1`, `|d|>=1`, and `J+1<=37`,
\[
|T_{J+1}|\ge\left(\frac23\right)^{37}
=\frac{137438953472}{450283905890997363}
>\frac3{10^7}.                                  \tag{3.4}
\]

### Negative-flow compensation

Let
\[
P=\sum_{G_i>0}q_i(2^{G_i}-1),\qquad
N=\sum_{G_i<0}q_i(1-2^{G_i}),
\]
so `F2=P-N`.

At the mechanical carry `t`, (2.1) gains the unique carry and
`G_t=1+h_t>0`.  Its positive contribution is
\[
T_t=\rho_t(2-2^{-h_t})\ge\rho_t>\frac12.        \tag{3.5}
\]
If `d<0`, the first term itself gives `N>=|T_{J+1}|`.  If `d>0`, then `P`
contains both `T_{J+1}` and `T_t`, while
`F2<1/2-Delta/16`; hence
\[
N=P-F_2>T_{J+1}+\frac{\Delta}{16}>T_{J+1}.       \tag{3.6}
\]
Thus in every first-mismatch type
\[
\boxed{N>3/10^7}.                                \tag{3.7}
\]
This is a global compensation requirement forced by a local defect plus the
mandatory mechanical carry.

## 4. Zero common height: 28 exact signed types

Assume `H=h_J=h_{p+J}=0`.  Let
\[
c_J=b_{J+1}-b_J\in\{1,2\}.
\]
The next heights are
\[
h_{J+1}=c_J-a,\qquad h_{p+J+1}=c_J-b.
\]
Both are nonnegative and `a,b>=1`.  If `c_J=1`, this forces `a=b=1`, contrary
to first mismatch.  Therefore `c_J=2` and necessarily
\[
\{a,b\}=\{1,2\},\qquad |d|=1.                  \tag{4.1}
\]
Because `S_J=b_J`,
\[
v=b_J+1.                                        \tag{4.2}
\]
The exact local certificate checks `v<=37` and leaves precisely
\[
J\in\{1,3,5,6,8,10,11,13,15,17,18,20,22,23\}.  \tag{4.3}
\]
Each index has the two signs `d=+1,-1`, so there are exactly 28 signed
zero-height local types.

At `k=J+1`, the mismatch creates exactly one height-one phase and one
height-zero phase.  Since `c_J=2`, this positive phase begins at a mechanical
component start.  The standard mechanical residue calculation gives
`rho_k>2/3`.  Equation (3.3) reduces to
\[
|T_{J+1}|=\frac{\rho_{J+1}}2>\frac13.            \tag{4.4}
\]
The exact minimum over the 14 indices is
\[
\frac{134217728}{387420489}>\frac13.             \tag{4.5}
\]
Consequently:

- for `d<0`, the first term alone gives `N>1/3`;
- for `d>0`, (3.6) gives `N>|T_{J+1}|+Delta/16>1/3`.

Hence every zero-common-height first mismatch obeys
\[
\boxed{N>1/3}.                                   \tag{4.6}
\]

## 5. Positive common height: three-support loss

Assume `H>=1`.  At the mismatch phase itself,
\[
h_J=h_{p+J}=H,
\]
so two distinct global phases are positive.  At `J+1`, equation (2.1) gives
\[
h_{J+1}-h_{p+J+1}=d.
\]
The two next heights are nonnegative, so at least one is at least `|d|>=1`.
This is a third distinct positive phase because `J<=36` and `p+37<L`.

For every nonzero phase `i<L`, `rho_i>1/2`: indeed
`A/L>log_2(3)` and `b_i>Ai/L-1` imply
`b_i-i log_2(3)>-1`.
Therefore the two height-`H` phases contribute more than
`1-2^{-H}` to `R-Q`, and the third phase contributes more than
`(1/2)(1-2^{-|d|})`.  Thus
\[
\boxed{
R-Q>
\frac32-2^{-H}-2^{-|d|-1}
\ge\frac34.
}                                                \tag{5.1}
\]

RL175 gives
\[
F_2=aQ+bQ_0,\qquad
\rho_t=aR+bR_0,
\]
where `a=q_p^{-1}-1>0` and `b=(lambda-1)/q_p>0`.  Hence
\[
\rho_t-F_2
=a(R-Q)+b(R_0-Q_0)
>a\left(\frac32-2^{-H}-2^{-|d|-1}\right),       \tag{5.2}
\]
which is the advertised local-height envelope.

Using only the uniform minimum `R-Q>3/4`, write `x=Delta+s` and use the
same certified inequalities as RL175:
`rho_t=e^x/2`, `e^x-1<x+2x^2`, `e^s-1>s`,
`s>5Delta`, and `x^2<Delta/16`.  Then
\[
F_2
<\frac{e^x}{2}-\frac34(e^s-1)
<\frac12+\frac{\Delta}{2}-\frac{s}{4}+x^2
<\boxed{\frac12-\frac{11\Delta}{16}}.           \tag{5.3}
\]
This is strictly stronger than the inherited RL175 half-barrier in the
`H>=1` first-mismatch branch.

## 6. Exact finite local automaton and its barrier

The target permits an exact local enumeration using only:

- `a_j>=1`;
- mechanical increments `c_j=b_{j+1}-b_j`;
- nonnegative heights;
- common shifted/unshifted prefix before `J`;
- first mismatch at `J`;
- the RL176 valuation cap `v<=37`.

The verifier propagates the common height by
\[
h_{j+1}=h_j+c_j-a_j\ge0,
\]
then enumerates the two unequal legal exponents at `J`.  After identifying
types by `(J,H,a_J,a_{p+J},d,v)`, it finds exactly 15,872 legal signed local
types.

Two conclusions are promoted with careful scope:

1. every `v=2,...,37` appears, and for every such `v` both signs of `d`
   appear;
2. `|d|<=21` in every legal type.

The first is a **method barrier**, not a physical existence claim: the local
rules by themselves cannot eliminate a valuation or a sign.  Any further
closure must use the global compensation/order information, not merely a
larger version of the same local automaton.

The high-valuation branches sharpen as follows:

- `v=36` has no `H=0` local type, so it is entirely in the three-support
  `H>=1` branch of Section 5;
- `v=37` has `H=0` only at `J=23`, with `d=+1` or `d=-1`; there
  \[
  |T_{24}|=\frac{2^{37}}{3^{24}}
  =\frac{137438953472}{282429536481}
  \approx0.4866309493.
  \]
  All other `v=37` local types have `H>=1`.

The exact automaton does not assert that any listed type extends to a full
physical cycle.

## 7. What is and is not proved

### Proved analytic mathematics

- carry-free relation `G_i=h_i-h_{p+i}` for the RL177 prefix;
- consecutive lifted-defect/value pairing through the common prefix;
- exact sign/order-crossing law at the first mismatch;
- exact first-flow quantum (3.3);
- total negative-flow floor `N>3/10^7`;
- zero-height structural reduction and `N>1/3`;
- positive-height three-support theorem, loss floor (5.1), and stronger
  half-barrier (5.3).

### Exact finite certification

- 15,872 identified local mismatch tuples under the stated certified rules;
- all valuations `2..37` and both signs survive those local rules;
- `|d|<=21`;
- exactly 28 signed zero-height types at the 14 listed indices;
- the exact first-flow lower bounds and high-valuation subcases.

### External-assisted only

No new RL177 theorem uses `m>=2^71`.  The inherited external lower gap band
may still be invoked only with its existing qualification.

### Not proved

- no contradiction in either first-mismatch sign branch;
- no exclusion of `h_p=0`;
- no exclusion of the secondary `h_p>=1` branch from RL175;
- no global non-trivial-cycle exclusion and no proof of Collatz.

## 8. Handover

RL178 should attack the **negative compensation/height-return mechanism**
created here.  The highest-value finite interface is the zero-height branch:
28 signed types with `|T|>1/3`, and especially the `v=37`, `J=23` pair with
`|T|=2^37/3^24`.

The next useful object is the earliest later phase where the height ordering
opposes the first mismatch (or where the p-shift height difference returns to
zero).  The aim is to turn the required negative-flow budget into a second
quantized transition or an impossible order/weight configuration.  Do not
repeat the certified local automaton as though it could remove valuations by
itself.
