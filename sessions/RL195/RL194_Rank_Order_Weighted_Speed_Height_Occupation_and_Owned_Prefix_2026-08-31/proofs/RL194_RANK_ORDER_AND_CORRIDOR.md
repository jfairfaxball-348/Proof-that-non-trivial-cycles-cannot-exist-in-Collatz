# RL194 — canonical rank order and exact K-corridor cuts

RL194 closeout proof, independently reviewed.
BASE_HEAD: `4ded9b73d84cd3f9101c9eaef81d783e14390914`.
Incoming authority: RL193; active job RL194; date 2026-08-31.

## Scope and dependencies

All physical assertions are conditional on the sole high branch
`(v,H,J,d)=(37,0,23,-1)` and a hypothetical physical extremal triple.
Necessary rank survival is not physical realization.  No H21 charging budget,
spacing bound, branch, Gate A, Gate B, or global conclusion is changed.

The parent established the complete RL194 start gate.  This subtask checked
the local HEAD, read the binding AGENTS/protocol/classification documents,
and read current authoritative proof, correction, report, target and red-team
records.  Under verification economy it accepts their inherited constants
and bounds; no expensive historical replay was needed.

Constants and conventions from RL193:

`A=217976794617`, `L=137528045312`, `B=A-L=80448749305`,
`p=65470613321`, `Bp=1 mod L`, `Q=37B mod L=88514772733`,
`z=L-p=72057431991`.

Canonical phases satisfy `0<=i<L`, with rank `r_i=iB mod L` and

`rho_i=2^floor(Ai/L)/3^i=exp((i*delta-r_i*ln2)/L)`,

where `0<delta=A ln2-L ln3<2^-40`.  The physical coordinate satisfies
`K_0=K0=2^37`, `f_i=3(K_(i+1)-K_i)`, and, for every canonical i,

`Klow=128081997553 < K_i < Kup=146795909391`.

For the canonical start a of a physical 37-zero prefix, RL193 gives
`K_a=rho_a*T`, with T=2^38 if its terminal rank r<Q and T=2^37 if r>=Q.
The start rank is `(r-Q) mod L`; thus `a=((r-Q)p) mod L`.
The old necessary core is `E=[72797034370,103818202602]` minus the
24 isolated RL193 deletions.  In particular Q-1 and Q are excluded.
The canonical terminal is at least phase 71, so any such physical start and
terminal lie in the same canonical interval; no quasi-periodic lift is being
silently identified with a canonical value.

## 1. Exact global reverse rank order

For canonical phases i,j with `r_j-r_i=d>=1`,

`L log(rho_i/rho_j)=d ln2+(i-j)delta`.

Since `ln2>2/3`, `(L-1)2^-40<1/6`, and `i-j>=-(L-1)`,

`d ln2+(i-j)delta > 2d/3-1/6 >= d/2`.

Consequently

`rho_i/rho_j > exp(d/(2L)) > 1`.

The order is therefore exactly the reverse of canonical rank order, with a
strict quantitative gap.  The tiny chronological phase correction cannot
reverse even one rank step.  This is an analytic statement over all L phases,
not a numerical sampling claim.  It does not assert monotonicity in time.

## 2. One K formula across both atoms

Define a necessary-state value F(r) at every terminal rank r in the old E by

`F(r)=K0 exp(((Q-r)ln2+a(r)delta)/L)`,

`a(r)=((r-Q)p) mod L`.

If r<Q then the start rank is r-Q+L, and the factor T=2^38 loses one factor
of two when that extra L is inserted into rho.  If r>=Q then T=2^37 and
the start rank is r-Q.  Both cases give exactly this formula.  At a physical
triple, F(r)=K_a=K_terminal by the zero-prefix identity.

For r<s, the same estimate as above gives

`F(r)/F(s)>exp((s-r)/(2L))`.

Thus there is strict global reverse rank order across the atom seam as well
as inside each atom.  This formula defines a useful comparison value at ranks
not known to be realized; evaluating it does not realize those ranks.

## 3. Exact K-corridor endpoints

Using rigorous rational logarithm enclosures, four endpoint tests establish
the complete interval on which the displayed F passes the inherited corridor:

| r | a(r) | tested quantity | strict rational enclosure |
| ---: | ---: | --- | --- |
| 75446746412 | 76452012903 | `L log(F/Kup)` | `(1/10,3/25)` |
| 75446746413 | 4394580912 | `L log(F/Kup)` | `(-13/20,-16/25)` |
| 102504571503 | 134680116098 | `L log(F/Klow)` | `(3/40,2/25)` |
| 102504571504 | 62622684107 | `L log(F/Klow)` | `(-69/100,-17/25)` |

Strict reverse rank order supplies the gap-free coverage between and outside
these four endpoints.  Therefore a physical extremal terminal must satisfy

`75446746413 <= r <= 102504571503`.

Every comparison value F(r) in this interval passes this *one corridor test*;
this is not a sufficiency claim for any physical condition.

The smaller interval discards 3,963,343,142 old E ranks.  Two were already
among the RL193 isolated deletions, namely the old endpoints 72797034370 and
103818202602.  The other 22 RL193 isolated deletions remain:

`75485708845, 75485708846, 78174383322, 80448749304, 80448749305,`
`80863057798, 83137423780, 83137423781, 83551732274, 85826098256,`
`85826098257, 88514772732, 88514772733, 91203447209, 93477813191,`
`93477813192, 93892121685, 96166487667, 96166487668, 98855162143,`
`98855162144, 101543836620`.

The remaining necessary-rank cardinality is 27,057,825,069, an additional
3,963,343,140 exclusions beyond RL193.  This is not a population count or an
ownership bound.  The four inherited carry buffers remain 11/5 and 4/7;
the smaller interval alone does not improve them.

## 4. Intermediate corridor-only canonical terminal floors

These corridor-only floors are superseded by the stronger chronological
floors in `RL194_CHRONOLOGICAL_WEIGHTED_SPEED.md`.  They are retained as
independently checked consequences of this one necessary test.

RL193 already excludes every canonical extremal terminal before phase 71.
At phases 71,72,73 the ranks are respectively

`73211342863, 16132046856, 96580796161`.

The first two miss the new core; the third is an undeleted upper-atom rank.
Hence the new overall and upper-atom canonical terminal floors are 73.
The complete check of phases 71..77 finds no lower-atom rank in the new core;
phase 78 has undeleted lower-atom rank 86240406750.  Thus the lower-atom floor
is 78.  The boundary survivors at phases 73/78 are not realized terminals.

## 5. Quantified canonical prefix displacement

Because Q-1 and Q are already deleted, any physical lower-atom terminal has
`r<=Q-2`; any physical upper-atom terminal has `r>=Q+1`.

At the closest lower necessary rank,

`a(Q-2)=6586818670`,
`x=(2 ln2+6586818670 delta)/L>0`,
`F(Q-2)=K0 exp(x)`.

Using global rank order, `exp(x)>1+x`, and exact rational log bounds yields

`sum_(0<=i<a) f_i =3(K_a-K0) >=3(F(Q-2)-K0)
 >3 K0 x >417/100`.

At the closest upper necessary rank,

`a(Q+1)=p`, `y=(ln2-p delta)/L>0`, `F(Q+1)=K0 exp(-y)`.

Since `1-exp(-y)>y/(1+y)`, the upper-atom prefix satisfies

`sum_(0<=i<a) f_i =3(K_a-K0) <=3(F(Q+1)-K0)
 <-3 K0*y/(1+y) <-19/10`.

These are signed chronological prefix-displacement inequalities anchored at
canonical phase zero.  They do not come from unsigned variation and do not
assert a chronological order between unrelated physical terminals.

## 6. Classification, verification and residual limitation

- Sections 1,2 and the endpoint-to-interval deduction are **proved analytic
  mathematics**, conditional on the stated physical assumptions when used for
  terminal exclusion.
- The four endpoint enclosures, inherited-deletion intersection, cardinality,
  finite phase ranges and displacement constants are **exact finite
  certificates**, with gap-free coverage provided in `verify_rank_order.py`.
- No inherited mathematical claim is repaired or demoted.  No branch or global
  result is proved.  No H21 binding budget, physical count or spacing bound is
  inferred from necessary-rank cardinality.
- The old sign-ordering obstacle is only partly reduced: weights are ordered
  in *rank*, not chronologically.  A separate physical theorem is still needed
  to couple epsilon signs/locations to actual chronological K displacement.
  These results do not establish a general impossibility of such a theorem.

Verifier command:

`python3 verification/verify_rl194_rank_order.py` from the package root.

All numerical checks use integers and Fractions.  Logarithms use the positive
atanh series through exactly 80 terms with its exact geometric tail bound.
There is no scan over the roughly 31 billion incoming ranks and no uncovered
range claimed complete; the global analytic monotonicity does that work.

The RL194 root proof ledger gives the final combined classification and
rank-set refinement, including the separate chronological-speed filter.
