# RL176 Integer p-Gap and Multi-Support Consumer

## Status

RL176 does **not** close the preferred `h_p=0` branch.  It does, however,
turn the RL175 half-barrier into an independent arithmetic and local
2-adic restriction on the physical p-gap
\[
g_p=y_p-m>0.
\]
The corrected RL174/RL175 p-shift convention is retained throughout:
\[
G_i=S_{p+i}-S_p-S_i,\qquad
F_2=\sum_i q_i(2^{G_i}-1)=3(\lambda-1)g_p.
\]

The new core facts are:

1. the two distinguished states have outgoing exponents
   \[
   a_0=a_p=1;
   \]
2. hence
   \[
   m\equiv y_p\equiv 3\pmod 4,\qquad 4\mid g_p;
   \]
3. the RL175 half-barrier and the inherited certified lower bound
   \(\Delta>1/1{,}116{,}000{,}000{,}000\) give
   \[
   0<g_p<186{,}000{,}000{,}000,
   \]
   and therefore
   \[
   4\le g_p\le185{,}999{,}999{,}996,\qquad
   g_p=4k,\quad 1\le k\le46{,}499{,}999{,}999;
   \]
4. if \(J\) is the first index for which
   \(a_{p+J}\ne a_J\), then
   \[
   v_2(g_p)=S_J+\min(a_J,a_{p+J});
   \]
5. consequently
   \[
   1\le J\le36,\qquad v_2(g_p)\le37.
   \]

Thus the p-shift cannot remain exponent-synchronous for 37 accelerated
steps.  The first disagreement is forced into a short, carry-free local
window, giving the next session a finite 2-adic interface to attack.

## Frozen inherited data

Use the RL175 constants
\[
A=217{,}976{,}794{,}617,\quad
L=137{,}528{,}045{,}312,\quad
p=65{,}470{,}613{,}321,\quad
u=103{,}768{,}467{,}013,
\]
with
\[
Ap-uL=1.
\]
Let
\[
\Delta=A\log 2-L\log 3>0,\qquad \lambda=e^\Delta.
\]
RL175 proved in the physical preferred branch \(h_p=0\):
\[
F_2=3(\lambda-1)g_p
\]
and
\[
F_2<\frac12-\frac{\Delta}{16}.
\]
It also inherited and certified
\[
\Delta>\frac1{1{,}116{,}000{,}000{,}000}.
\]

The odd states satisfy
\[
3y_j+1=2^{a_j}y_{j+1},\qquad a_j\ge1,
\]
with \(m=y_0\) the least odd state and, in the preferred branch,
\(y_p\) the unique second-smallest odd state.

## 1. The two minimum endpoints have exponent one

### Lemma RL176.1
\[
a_0=a_p=1.
\]

### Proof

Because the cycle is nontrivial, \(m>1\).  If \(a_0\ge2\), then
\[
y_1=\frac{3m+1}{2^{a_0}}
\le \frac{3m+1}{4}<m,
\]
contradicting the minimality of \(m\).  Hence \(a_0=1\).

Likewise, if \(a_p\ge2\), then
\[
y_{p+1}\le\frac{3y_p+1}{4}<y_p.
\]
Since \(y_p\) is the unique second-smallest state, the only state below it
is \(m\).  Thus \(y_{p+1}=m\).  But \(p+1<L\), so this would return to the
least state strictly before the period closes, contradicting the period
\(L\).  Hence \(a_p=1\).  ∎

For odd \(x\), the exact condition \(v_2(3x+1)=1\) is equivalent to
\(x\equiv3\pmod4\).  Therefore:

### Corollary RL176.2
\[
m\equiv y_p\equiv3\pmod4,\qquad 4\mid g_p.
\]

This is an independent integer restriction.  It uses only the physical
least/second-least state ordering and the accelerated recurrence; it does
not reuse the RL175 sparse-resultant ownership obstruction.

## 2. A rigorous global interval for the integer p-gap

Since \(e^\Delta-1>\Delta\),
\[
3(\lambda-1)g_p=F_2<\frac12.
\]
Hence
\[
g_p<\frac{1}{6\Delta}.
\]
Using the inherited certified inequality
\[
\Delta>\frac1{1{,}116{,}000{,}000{,}000}
\]
gives the exact safe bound
\[
g_p<186{,}000{,}000{,}000.
\]

Combining this strict upper bound with \(4\mid g_p\) yields:

### Corollary RL176.3
\[
4\le g_p\le185{,}999{,}999{,}996,
\]
or equivalently
\[
g_p=4k,\qquad
1\le k\le46{,}499{,}999{,}999.
\]

The exact RL175 identity therefore lies on the lattice
\[
F_2=12(\lambda-1)k.
\]
This lattice is real progress but is not itself a contradiction: its
smallest positive point remains far below the RL175 half-barrier.


## 3. The first p-shift mismatch occurs within 36 positions

Suppose, for contradiction, that
\[
a_{p+j}=a_j\qquad(0\le j\le36).
\]
The same 37 affine accelerated maps are then applied to \(m\) and
\(y_p=m+g_p\).  Hence
\[
y_{p+37}-y_{37}
=\frac{3^{37}g_p}{2^{S_{37}}}.
\]
Both endpoint states are odd, so their difference is even.  Therefore
\[
2^{S_{37}+1}\mid g_p.
\]
Since every accelerated exponent is at least one,
\[
S_{37}\ge37,
\]
and thus \(2^{38}\mid g_p\).  But Corollary RL176.3 gives
\[
0<g_p<186{,}000{,}000{,}000
<2^{38}=274{,}877{,}906{,}944,
\]
a contradiction.

Because RL176.1 already gives \(a_p=a_0=1\), the first mismatch cannot be
at index zero.  Hence:

### Theorem RL176.4
There is a first shifted exponent mismatch
\[
1\le J\le36.
\]

This entire window lies far before the first mechanical p-carry
\[
t=L-p=72{,}057{,}431{,}991.
\]

## 4. Exact valuation at the first mismatch

For the \(J\) from Theorem RL176.4, the two exponent strings agree
through indices \(0,\ldots,J-1\).  Applying those same \(J\) affine maps
to \(m\) and \(y_p=m+g_p\) gives
\[
y_{p+J}-y_J=\frac{3^Jg_p}{2^{S_J}}.
\]
Set
\[
X=y_J,\qquad Z=y_{p+J},\qquad
a=a_J,\qquad b=a_{p+J}.
\]
At the first mismatch \(a\ne b\).  Now
\[
v_2(3X+1)=a,\qquad v_2(3Z+1)=b.
\]
For two integers of unequal 2-adic valuation, the valuation of their
difference equals the smaller valuation.  Therefore
\[
v_2\bigl((3Z+1)-(3X+1)\bigr)=\min(a,b).
\]
Since the left side is \(3(Z-X)\), and \(3\) is odd,
\[
v_2(Z-X)=\min(a,b).
\]
Using
\[
Z-X=\frac{3^Jg_p}{2^{S_J}}
\]
gives:

### Theorem RL176.5
At the first p-shift exponent mismatch,
\[
\boxed{v_2(g_p)=S_J+\min(a_J,a_{p+J}).}
\]

The global bound \(g_p<2^{38}\) yields
\[
v_2(g_p)\le37.
\]
Thus the first mismatch not only occurs early; it records the exact
2-adic depth of the physical gap.

A useful extremal quantization follows immediately:
if \(v_2(g_p)\in\{36,37\}\), the global upper bound forces
\[
g_p=2^{36}\quad\text{or}\quad g_p=2^{37},
\]
respectively.

## 5. External-assisted lower gap band

This subsection is **not** part of the internal core proof.  It uses the
inherited external computational minimum \(m\ge2^{71}\), exactly as
qualified in RL175.

Write
\[
s=p\log3-u\log2>0.
\]
The endpoint identity gives
\[
q_p=e^{-s},\qquad q_py_p=m+\frac{Q_{p-1}}3>m,
\]
so
\[
g_p=y_p-m>(e^s-1)m>sm.
\]
RL175 certified
\[
s>5\Delta
\]
and
\[
3\cdot2^{71}\Delta>6{,}365{,}000{,}000.
\]
Thus, conditional on \(m\ge2^{71}\),
\[
g_p>5\cdot2^{71}\Delta
>\frac{31{,}825{,}000{,}000}{3}.
\]
Together with \(4\mid g_p\):

### Corollary RL176.6 (external-assisted)
\[
10{,}608{,}333{,}336
\le g_p\le185{,}999{,}999{,}996.
\]

No internal claim depends on this computational minimum.

## 6. Relation to the corrected p-shift

For the first mismatch \(J\),
\[
G_i=S_{p+i}-S_p-S_i=0
\qquad (0\le i\le J),
\]
while
\[
G_{J+1}=a_{p+J}-a_J\ne0.
\]
Because \(J\le36\ll t=L-p\), this first nonzero corrected p-shift defect
occurs in the carry-free window.

RL176 therefore reduces the next local problem to two explicit sign
branches:

- \(G_{J+1}>0\): the shifted exponent is larger at the first mismatch;
- \(G_{J+1}<0\): the shifted exponent is smaller at the first mismatch.

The RL175 identity
\[
F_2=\sum_i q_i(2^{G_i}-1)=3(\lambda-1)g_p
\]
requires the full signed defect flow to end as a small positive number.
The first nonzero term is now known to occur within 37 prefix states.
That is the main multi-support localization achieved here.

## 7. What RL176 does and does not prove

### Proved analytic mathematics

- \(a_0=a_p=1\).
- \(4\mid g_p\).
- \(0<g_p<186{,}000{,}000{,}000\).
- \(4\le g_p\le185{,}999{,}999{,}996\).
- There is a first shifted exponent mismatch with \(1\le J\le36\).
- At that mismatch,
  \[
  v_2(g_p)=S_J+\min(a_J,a_{p+J})\le37.
  \]
- The first nonzero corrected p-shift defect occurs in the carry-free
  prefix window.

### Exact finite/arithmetic certification

`RL176_CERTIFICATES/verify_integer_p_gap_consumer.py` checks the inherited
integer constants and every new numerical/lattice consequence used above.

### External-assisted only

- Conditional on the inherited computational minimum \(m\ge2^{71}\),
  \(g_p\ge10{,}608{,}333{,}336\).

### Not proved

- No contradiction in the preferred \(h_p=0\) branch.
- No uniform positive lower bound for the full signed \(F_2\) sum strong
  enough to beat the half-barrier.
- No exclusion of the secondary \(h_p\ge1\) branch.
- No global non-trivial-cycle exclusion.

## 8. Handover

RL177 should attack the early first-mismatch interface directly.  It
should keep
\[
1\le J\le36,\qquad
v_2(g_p)=S_J+\min(a_J,a_{p+J})
\]
as frozen RL176 input and split on the sign of
\[
G_{J+1}=a_{p+J}-a_J.
\]
The goal is to convert this forced early defect into a quantitative
contribution/compensation law for \(F_2\), or into a stronger modulus for
\(g_p\), without recycling the RL175 ownership resultant.
