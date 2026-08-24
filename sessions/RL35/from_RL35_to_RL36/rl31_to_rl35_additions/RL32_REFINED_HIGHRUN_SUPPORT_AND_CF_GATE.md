# RL32 — Refined high-run supporting line and improved global CF gate

**Status:** analytic theorem plus exact symbolic/interval certificate.  This is a global quantitative improvement, not an RL closure.

## 1. Result

Let the RL22–RL24 low/high block decomposition be in force, with least odd state `R >= 161`,

\[
H=\frac{4R-1}{3},\qquad f(x)=\frac{9x+5}{8}.
\]

For a block let `n` be its number of odd states, `V` its stripped 2-adic valuation total, and `P` its odd correction product.  Define

\[
T(R)=\frac{256R}{256R-319},\qquad
U(R)=\frac{2187R+3767}{2187R}.
\]

Then every admissible RL22/RL23 block satisfies

\[
\boxed{P\le T^{7V-11n}U^{8n-5V}.}
\]

The equality anchors of the comparison line are the two dynamically attainable type-II direct-return blocks

\[
(k,h,n,V)=(2,1,5,8),\qquad (3,1,7,11),
\]

whose exact products are respectively `T` and `U`.

After multiplication over the entire odd cycle and use of `A/L = log 3/log 2 + log(lambda)/(L log 2)`, this gives

\[
\lambda\le T^{7A-11L}U^{8L-5A}.
\]

Writing `beta=log 3/log 2`, solve the resulting self-referential inequality to obtain

\[
\frac{\log\lambda}{L}
\le
\frac{(7\beta-11)\log T+(8-5\beta)\log U}
{1-(7\log T-5\log U)/\log 2}.
\]

Hence

\[
\boxed{
\lim_{R\to\infty}R\,\frac{\log\lambda}{L}
\le 0.2475585796969224835888150467\ldots
}
\]

with exact asymptotic constant

\[
(7\beta-11)\frac{319}{256}+(8-5\beta)\frac{3767}{2187}.
\]

Under the inherited external lower bound `R >= 2^71`, rigorous rational log intervals and the continued-fraction exclusion give

\[
\boxed{\frac{L}{\gcd(A,L)}\ge 57,494,140,717.}
\]

This improves the RL24 global floor `57,397,300,723` and also slightly exceeds the RL31 exceptional-branch floor `57,490,527,167`.  It remains below the next relevant convergent denominator `65,470,613,321`, so no qualitative CF gate is crossed.

---

## 2. Repair of the old type-I direct-return relaxation

For a type-I low chain of length `k`, the terminal high is

\[
z=2f^k(x).
\]

If this terminal high is followed directly by a low (`h=1`), its outgoing valuation is **exactly 3**.

Indeed, for `R>=161`:

- valuations `1` and `2` leave the next odd state at or above `H`;
- valuation at least `4` sends the next odd state below the least odd state `R`.

Thus only valuation `3` can make a direct high-to-low return.

The next-low condition `>=R` therefore imposes the exact start floors

\[
x\ge \frac{32R-19}{27}\quad(k=1),
\qquad
x\ge \frac{256R-287}{243}\quad(k=2),
\qquad
x\ge R\quad(k=3).
\]

Consequently the sharp type-I `h=1` core products become

\[
P_{I,1}=\frac{32R}{32R-19},\qquad
P_{I,2}=\frac{256R}{256R-287},\qquad
P_{I,3}=\frac{2187R+3511}{2187R}.
\]

In particular the old RL24 type-I `k=1,m=0` comparison equality at `x=R` is not dynamically attainable as a direct-return block.  The old RL24 inequality remains a valid relaxation; this observation is used only to sharpen the support analysis.

---

## 3. Exact high-run valuation inequality

For a high run of length `h`, terminal high `h_0`, next low `ell`, and valuation sum `V_H`, the exact telescoping correction identity is

\[
\prod F = \frac{2^{V_H}\ell}{3^h h_0}>1.
\]

Therefore

\[
\boxed{2^{V_H}>3^h\frac{h_0}{\ell}.}
\]

This is strictly stronger than the coarse density surrogate used in RL24.

For type II, `h_0>=H` and `ell<H`, hence

\[
2^{V_H}>3^h.
\]

For type I, the terminal-height floors give

\[
\frac{h_0}{\ell}>
\begin{cases}
27/16,&k=1,\\
243/128,&k=2,\\
2187/1024,&k=3.
\end{cases}
\]

Since `2^19 < 3^12`, these inequalities produce a period-12 valuation certificate: if `h=12q+r`, `1<=r<=12`, the certified valuation floor is the corresponding residue floor plus `19q`.

The exact residue floors used by the verifier are:

### Type II

`h=1..12`:

\[
2,4,5,7,8,10,12,13,15,16,18,20.
\]

### Type I, k=1

\[
3,4,6,8,9,11,12,14,16,17,19,20.
\]

### Type I, k=2

\[
3,5,6,8,9,11,13,14,16,17,19,20.
\]

### Type I, k=3

\[
3,5,6,8,10,11,13,14,16,17,19,21.
\]

---

## 4. Sharper first high/high pair for type I

When a type-I run has `h>=2`, the first outgoing valuation from the terminal type-I high can only be `1` or `2`; valuation at least `3` already leaves the high interval.

For two consecutive high odd states `a,b`,

\[
F(a)F(b)=1+\frac{2^\nu+3}{9a}.
\]

The maximum is therefore attained at `nu=2` and the minimum permitted terminal high.  This yields the k-specific bounds

\[
P_{I,1}^{(HH)}\le\frac{81R+73}{81R+45},
\]

\[
P_{I,2}^{(HH)}\le\frac{729R+989}{729R+765},
\]

\[
P_{I,3}^{(HH)}\le\frac{6561R+11557}{6561R+9765}.
\]

The latter two improve the universal type-I first-pair relaxation inherited from RL24.

---

## 5. Finite support verification

The local support inequality

\[
P\le T^{7V-11n}U^{8n-5V}
\]

is checked exactly for all

- 2 orientations (type I / type II),
- 3 low-chain lengths `k=1,2,3`,
- 12 high-run residues `h=1,...,12`,

for **72 seed cases** in total.

For each seed the verifier substitutes the certified valuation floor and proves the resulting rational-function difference nonnegative for all `R>=161` by shifting `R=t+161` and checking nonnegative polynomial coefficients.

Long high runs are reduced to the 12 residues because increasing `h` by 12:

- increases `n` by 12,
- increases certified `V` by 19,
- contributes at most six generic high/high pairs.

The support RHS gains exactly `TU`, so the extension follows from the exact polynomial inequality

\[
\left(\frac{16R}{16R-7}\right)^6\le TU.
\]

Finally, the RHS is increasing in the actual valuation `V`, since

\[
\frac{T^7}{U^5}>1
\]

for `R>=161`.  Therefore replacing actual valuation by the certified floor is legitimate.

---

## 6. Globalization

Multiplying the block inequalities around the complete odd cycle gives

\[
\lambda\le T^{7A-11L}U^{8L-5A}.
\]

Set

\[
x=\frac{\log\lambda}{L},\qquad
\beta=\frac{\log3}{\log2}.
\]

The exact cycle identity gives

\[
\frac AL=\beta+\frac{x}{\log2}.
\]

Substitution yields

\[
x\le (7\beta-11)\log T+(8-5\beta)\log U
+\frac{x}{\log2}(7\log T-5\log U).
\]

Because `T^7/U^5>1` but `<2`, the denominator is positive, giving the stated exact global coefficient.

---

## 7. Rigorous continued-fraction gate

At `R0=2^71`, the verifier computes certified rational intervals for `log T`, `log U`, `log 2`, and `log 3` via the atanh series

\[
\log u=2\sum_{j\ge0}\frac{x^{2j+1}}{2j+1},
\qquad x=\frac{u-1}{u+1},
\]

with an explicit geometric tail bound.

This gives a rigorous interval for `C(R0)=R0*x`, and hence the Legendre threshold

\[
2q^2\frac{C(R0)}{R0}<\log 2.
\]

Exact continued-fraction reconstruction for `beta=log3/log2`, together with exact-sign interval tests of `p log2-q log3`, excludes every above convergent through the threshold.  The resulting maximum possible denominator below the Legendre cutoff is

\[
q_{\max}=57,494,140,716,
\]

so

\[
\boxed{q=\frac{L}{\gcd(A,L)}\ge57,494,140,717.}
\]

The first convergent denominator beyond the threshold is

\[
65,470,613,321,
\]

and it is on the wrong side for the desired next gate.

---

## 8. Proof-state significance

This theorem is a genuine **global** improvement over RL24 and is not restricted to the exceptional `(G,H)=(12,4)` branch studied in RL31.

It does **not** prove RL.  The coefficient remains far above the roughly `0.1909` scale needed for the next qualitative CF jump identified in the inherited audit.

The theorem does, however, identify a new non-artificial saturation pair: the direct type-II `(k,h)=(2,1)` and `(3,1)` blocks.  Their low-state maps are dynamically coupled, so treating their support-line maxima independently is the next visible source of slack.  That coupling is the principal target after RL32.

---

## 9. Certificate

Exact verifier:

`verify_rl32_refined_highrun_support.py`

Recorded run:

`RL32_REFINED_HIGHRUN_SUPPORT_VERIFIER_RUN.txt`

Expected headline:

`RL32 refined high-run supporting-line verifier: PASS`
