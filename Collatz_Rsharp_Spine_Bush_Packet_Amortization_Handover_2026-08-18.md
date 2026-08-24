---
title: "Collatz R# Excursion-to-Proliferation — Spine / Bush / Packet Amortization Handover"
date: "2026-08-18"
status: "ACTIVE_RESEARCH_HANDOVER"
project: "3n+1"
intended_reader: "AI / mathematical research agent"
map_convention: "Shortened Collatz map T(n)=n/2 if even, (3n+1)/2 if odd; accelerated odd map F_r(u)=(3u+1)/2^r."
authoritative_previous_handover: "Collatz_Rsharp_Odometer_Packet_Potential_Handover_2026-08-17.md"
supersedes_for_operations: "Collatz_Rsharp_Odometer_Packet_Potential_Handover_2026-08-17.md"
primary_goal: "Prove an excursion-level spine–bush–packet amortization lemma strong enough to give a uniform positive trapped inverse-mass constant for arbitrary-length pure r=1 corridors, then reconnect to mixed RO excursions."
next_named_target: "Spine–Bush–Packet Amortization Lemma"
claim_labels:
  PROVED_DERIVED: "Algebraically derived in-session. Re-write as ordinary proof before publication."
  MACHINE_CHECKED_LOCAL_LEMMA: "Finite/exact local statement checked by frozen verifier. Independently reimplement and hand-reduce where practical before publication."
  INDEPENDENT_COMPUTATIONAL_REPRODUCTION: "Independent implementation reproduced a result, but this remains computer-assisted evidence until externally audited."
  COMPUTER_ASSISTED_CANDIDATE: "Finite exact/computational certificate exists but is not yet publication-grade."
  COMPUTATIONAL: "Experimental numerical evidence only."
  CONJECTURE: "Open target."
  FALSIFIED: "Tested candidate failed. Do not resurrect without a materially new hypothesis."
---

# 0. Executive handover

This memo is the authoritative operational start point for the next session.

Do **not** restart from generic Collatz background, from the q=24 certificate search, or from the original packet-potential problem. Those stages have already been pushed substantially further.

The programme began from a hypothetical least counterexample \(R^\#\), record-scale excursions, and the question whether one hypothetical red integer must force enough inverse-tree proliferation that the red set cannot remain asymptotically negligible. The current tractable subproblem is a long pure accelerated `r=1` corridor. The earlier finite certificate showed such a corridor can force substantial trapped inverse mass at fixed length. The intervening work compressed the inverse frontier into packet states and isolated a finite fragile kernel.

This continuation achieved four durable advances:

1. **strict packet drift:** the earlier nondecreasing packet potential was upgraded to a uniform strict two-digit inequality;
2. **scale-coordinate simplification:** after Beatty normalization and a corrected-height coordinate, high-channel scale obeys an exact geometric downward kernel;
3. **critical 3-adic structure:** the only locally neutral singular propagation is the phase-2 branch near the sticky point \(y=-1\), with an explicit rational critical ray and a broader neutral-ray invariant;
4. **side-bush spectral gap:** every exact negative side bush emitted away from the sticky branch admits a nine-residue fractional-moment Lyapunov function with a rigorously machine-certified contraction factor \(<0.99\) after critical normalization.

The main obstruction is therefore no longer “find a packet potential” or “control arbitrary ternary discrepancy.” It is now much sharper:

> **Combine neutral critical-spine scale, uniformly contracting side-bush credit, strict packet-count drift, and permanently certified inverse nodes into a single excursion-level amortization inequality.**

A successful version need not preserve scale pointwise. In fact, pointwise scale preservation has been experimentally falsified as the right target. The desired theorem should say that whenever critical scale temporarily collapses, the collapse necessarily creates enough packet fragmentation / packet transitions that the strict packet potential banks a proportional amount of permanent inverse mass.

The next session should begin at Section 17.

---

# 1. Core setting and notation

Use the shortened Collatz map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

User notation:

- `C`: positive integers whose orbit reaches 1;
- `R`: hypothetical counterexamples;
- `RL`: non-trivial-cycle counterexamples;
- `RO`: unbounded/non-periodic non-convergent counterexamples;
- \(R^\#\): least positive integer in `R`, if `R` is nonempty;
- \(R(X)=\#(R\cap[1,X])\).

For the accelerated odd map,

\[
F_r(u)=\frac{3u+1}{2^r},
\qquad r=\nu_2(3u+1)\ge1.
\]

For a record-scale excursion use lower barrier \(n\) and upper ceiling \(Y\). The shortened inverse children of a node \(y\) are

\[
2y
\]

always, and

\[
\frac{2y-1}{3}
\]

when \(y\equiv2\pmod3\).

For a seed set \(S\subset[n,Y]\), write \(\mathrm{Cl}_{[n,Y]}(S)\) for its trapped inverse closure. Normalize trapped mass by

\[
\eta(S;n,Y)=\frac{|\mathrm{Cl}_{[n,Y]}(S)|}{Y/n}.
\]

For \(n=R^\#\), every legal inverse predecessor of a red node is red; a legal predecessor below \(R^\#\) contradicts minimality.

Keep logically separate:

1. infinitely many red integers;
2. positive upper density;
3. positive lower/natural density;
4. every integer above \(R^\#\) red.

The current programme is aimed at 2/3, not 4.

---

# 2. Inherited baseline that remains active

The previous handover `Collatz_Rsharp_Odometer_Packet_Potential_Handover_2026-08-17.md` remains the detailed source for all earlier derivations. Its SHA-256 is recorded in Section 20.

The following inherited statements remain active.

## 2.1 Least-counterexample barrier

**[PROVED_DERIVED]**

If \(R^\#\) exists,

\[
T^k(R^\#)\ge R^\#\qquad\forall k\ge0.
\]

Also \(R^\#\) is odd and \(R^\#\not\equiv2\pmod3\), hence

\[
R^\#\equiv0\text{ or }1\pmod3.
\]

## 2.2 Bounded discrepancy would force positive density

With

\[
m_k=\#\{\text{odd shortened steps before time }k\},\qquad
\alpha=\log_3 2,
\]

\[
D_k=m_k-\alpha k,
\qquad
C_k=3^{D_k},
\]

**[PROVED_DERIVED]** if an injective infinite `RO` orbit satisfies

\[
0<c\le C_k\le M<\infty,
\]

then

\[
\underline d(R)\ge\frac{3c}{\alpha M}>0.
\]

Thus a hypothetical density-zero `RO` must have unbounded discrepancy / large coefficient excursions.

## 2.3 Supercritical blocks contain many `r=1` steps

If a block has \(q\) accelerated odd transitions and

\[
\frac{3^q}{2^{r_1+\cdots+r_q}}\ge1,
\]

then if \(A\) of the \(r_j\)'s equal 1,

\[
A\ge 2q-\lfloor q\log_2 3\rfloor
=\left\lceil(2-\log_2 3)q\right\rceil.
\]

Thus at least about 41.5% of odd transitions are `r=1` in a supercritical block.

## 2.4 Pure `r=1` corridor arithmetic

For \(q\) consecutive accelerated `r=1` transitions, parameterize

\[
n+1=2^{q+1}k.
\]

Then

\[
\boxed{n=2^{q+1}k-1}
\]

and after the \(q\)-step corridor

\[
\boxed{Y=2\,3^qk-1.}
\]

The corridor shadows \(-1\) 3-adically:

\[
u_j+1=\left(\frac32\right)^j(u_0+1),
\qquad
u_j\equiv-1\pmod{3^j}.
\]

## 2.5 Fixed-length q=24 certificate

**[COMPUTER_ASSISTED_CANDIDATE]**

The inherited q=24 all-residue certificate at threshold

\[
c=\frac{14}{25}=0.56
\]

has:

- terminal ternary depth \(K=21\);
- 142,371 terminal compressed cylinders;
- 142,295 `MASS` terminals;
- 76 `LEAK` terminals;
- zero unresolved cylinders;
- exact depth-21 coverage \(3^{21}\);
- weakest final ratio about \(0.560053294775\).

Interpretation: a 24-step `r=1` corridor beginning at the global lower barrier either leaks below the barrier or forces at least \((14/25)(Y/n)\) distinct inverse nodes in \([n,Y]\).

This remains computer-assisted and is not the desired arbitrary-length theorem.

---

# 3. Packet language inherited from the previous handover

The literal inverse frontier was compressed into arithmetic packets.

A packet is denoted

\[
P_{x,b}=(x,x-2,\ldots,b),
\qquad b\in\{0,1,2\},\quad x\ge b,\quad x\equiv b\pmod2.
\]

Its combinatorial mass function is

\[
F(P_{x,b})=F(x,b)
=\left(\frac{x-b}{2}+1\right)
\left(b+\frac{x-b}{2}+1\right).
\]

The sibling boundary variable obeys the exact odometer

\[
y_{i+1}=4y_i+1.
\]

The two admissible Beatty-carry words across a two-digit block are not arbitrary; the legal two-carry words are

\[
01,\quad10,\quad11.
\]

The prior work identified exactly eight low-channel fragile packets:

\[
P_{0,0},P_{2,0},P_{4,0},P_{1,1},P_{3,1},P_{5,1},P_{2,2},P_{4,2}.
\]

The original packet potential \(\Phi\) on these is

\[
\begin{array}{c|cccccccc}
P&P_{0,0}&P_{2,0}&P_{4,0}&P_{1,1}&P_{3,1}&P_{5,1}&P_{2,2}&P_{4,2}\\ \hline
\Phi&0&0&3&0&1&8&0&2.
\end{array}
\]

For high packets \(x\ge6\), \(\Phi(P)=F(P)\).

The previous handover established a nondecreasing two-digit inequality but left zero drift as the central obstruction.

That obstruction has now been removed.

---

# 4. New theorem-bearing result: strict packet drift

## 4.1 Zero-drift graph

**[MACHINE_CHECKED_LOCAL_LEMMA + PROVED_DERIVED STRUCTURE]**

Enumerating equality cases of the original two-digit packet inequality shows that the zero-drift kernel is not recurrent.

Seven fragile zero-drift cases terminate immediately. The only nonterminal zero-drift transition is

\[
\boxed{P_{5,1}\longrightarrow P_{1,1}},
\]

and \(P_{1,1}\) has no further nonterminal zero-drift continuation.

This permits a finite rank correction.

## 4.2 Corrected integer potential

Define

\[
r(P)=
\begin{cases}
2,&P=P_{5,1},\\
1,&P\text{ is one of the other seven fragile packets},\\
0,&x\ge6.
\end{cases}
\]

Define

\[
\boxed{W(P)=4\Phi(P)-r(P)}
\]

and

\[
\boxed{V(P)=W(P)+1.}
\]

On the eight fragile packets,

\[
\begin{array}{c|rrrrrrrr}
P&P_{0,0}&P_{2,0}&P_{4,0}&P_{1,1}&P_{3,1}&P_{5,1}&P_{2,2}&P_{4,2}\\ \hline
W&-1&-1&11&-1&3&30&-1&7,\\
V&0&0&12&0&4&31&0&8.
\end{array}
\]

Let \(H_2\) be the node production over a legal two-digit packet transition, and let \(Q\) range over the resulting packets.

The frozen verifier proves the exact finite inequality

\[
\boxed{
4H_2+\sum_Q W(Q)\ge W(P)+1.
}
\]

Equivalently,

\[
\boxed{
4H_2+\sum_QV(Q)\ge V(P)+\#Q.
}
\]

This is the first **uniform strict drift** statement in the packet programme.

Interpretation: every two-digit packet transition either creates actual inverse nodes or produces successor-packet credit with an extra unit per successor packet. Packet number is therefore not a nuisance variable; it is a bankable resource.

## 4.3 Infinite high-channel reduction is algebraic

The strict inequality is not based only on checking a large finite \(x\)-range.

For one-step high-channel gain, increasing \(x\) by six gives exact margin increments according to starting ternary phase \(p\):

\[
\Delta_0(x)=\frac{x^2+3x-10}{2},
\]

\[
\Delta_1(x)=\frac{x^2+7x+12}{2},
\]

\[
\Delta_2(x)=\frac{x^2+5x+6}{2}.
\]

The required base packets have worst one-step margins:

\[
\begin{array}{c|ccccccccc}
P&(10,0)&(12,0)&(14,0)&(11,1)&(13,1)&(15,1)&(10,2)&(12,2)&(14,2)\\\hline
\min(g_1-F)&3&16&35&9&25&48&3&17&36.
\end{array}
\]

Thus sufficiently high packets are already self-financing after one refinement; only a finite low/high-exception set requires explicit checking.

The verifier also stress-checks every packet top \(x\le100\), but publication proof should use the algebraic six-channel induction rather than treating that stress range as the theorem.

---

# 5. Scale mass and why packet count alone is insufficient

The packet potential \(V\) grows only polynomially in channel height. The corridor target scale is exponential.

Define exponential frontier capacity

\[
\boxed{E=\sum_{\text{frontier chains}}2^J.}
\]

Empirically, \(E\) remains on the same order as \(Y/n\) even when already-certified core mass becomes very small. For example, in one exact q=60 diagnostic the initial certified core ratio was about \(2.16\times10^{-4}\), while \(E/(Y/n)\) was about 1.366.

Therefore a final arbitrary-length theorem must preserve or harvest **scale capacity**, not merely packet count.

Simple per-packet exponential potentials fail. The reason is not an implementation detail: the common ternary digit acting simultaneously on the whole frontier is essential.

---

# 6. Exact high-channel moment identities and corrected-height kernel

Define channel moments

\[
E=\sum 2^J,
\qquad
L=\sum J2^J,
\qquad
Q=\sum J^2 2^J.
\]

For a single chain of channel \(J\), summing over the three possible common ternary rotations gives exact identities.

For Beatty carry \(\delta=0\):

\[
E' = 2^{J+1}-1,
\]

\[
L'=(J-1)2^{J+1}+2,
\]

\[
Q'=2^{J+1}(J^2-2J+3)-6.
\]

For \(\delta=1\):

\[
E'=2(2^{J+1}-1),
\]

\[
L'=J2^{J+2}+2,
\]

\[
Q'=2^{J+2}(J^2+2)-6.
\]

These are frozen in `collatz_scale_mixing_verifier.py`.

## 6.1 Beatty-normalized corrected height

Let \(r_t\) be the number of Beatty `1` carries accumulated through time \(t\), and define

\[
\boxed{h=J-r_t.}
\]

After Beatty normalization, the carry disappears from the bulk averaged dynamics.

Across the three common ternary digits, scale from corrected height \(h\) is distributed to

\[
h,h-1,h-2,\ldots
\]

with exact weights

\[
\boxed{
\frac12,\frac14,\frac18,\ldots
}
\]

until the finite bottom cutoff.

Thus the hidden bulk process is a geometric downward walk with decrement

\[
D\sim\mathrm{Geom}(1/2),
\qquad
\mathbb E D=1,
\qquad
\operatorname{Var}(D)=2.
\]

This explains why first- and second-order martingale-looking combinations appear naturally. Do not mistake this averaged kernel for a pointwise theorem: a single common ternary digit can be much worse than the average.

## 6.2 Pointwise corrected-height monotonicity

For an individual packet, the highest surviving corrected child height is

\[
h,\qquad h-1,\qquad\text{or}\qquad h-3
\]

depending on top phase \(2,1,0\).

Hence corrected top height never rises. Avoiding descent requires repeatedly taking the phase-2 continuation.

This points directly to the sticky 3-adic structure at \(y=-1\).

---

# 7. Deterministic bad-hit mixing

Classify scale according to which of the three next common ternary digits is locally hostile for that packet boundary.

For a long high packet actually hit by its bad digit, the surviving high-channel scale is redistributed among the three next bad-digit classes, up to a vanishing packet-end correction, in the exact proportions

\[
\boxed{
\frac{2752}{4161},\qquad
\frac{1366}{4161},\qquad
\frac{43}{4161}
}
\]

in some permutation.

A canonical orientation has exponent shifts

\[
\{3,10\},\qquad\{4,15\},\qquad\{9,16\},
\]

which yield the geometric weights whose normalized ratio is

\[
2752:1366:43.
\]

The largest share is only about 0.66138.

So a concentrated vulnerability class cannot remain equally concentrated after being successfully attacked. This is a deterministic mixing mechanism, not a probabilistic heuristic.

A simple scalar three-bin discrepancy potential was nevertheless insufficient; see Section 14.

---

# 8. Finite 3-adic Perron hierarchy

To preserve the common-digit coupling exactly, retain the packet boundary residue \(y\bmod3^m\). Let \(f_m(r)>0\) be a scale credit on each residue. For each residue, the adversary chooses among the three lifts modulo \(3^{m+1}\). The high-channel transfer defines a nonlinear Bellman/Perron operator

\[
T_m f(r)=\min_{d\in\{0,1,2\}} T_{m,d}f(r).
\]

Let \(\lambda_m\) be the largest subeigenvalue for which

\[
T_m f\ge\lambda_m f.
\]

Frozen computations reproduce:

\[
\begin{array}{c|c|c}
m&\lambda_m&(m+1)(1-\lambda_m)\\\hline
1&0.5758898173&0.848220\\
2&0.7132796945&0.860161\\
3&0.7715006305&0.913997\\
4&0.8072697954&0.963651\\
5&0.8304581796&1.017251\\
6&0.8595081609&0.983443\\
7&0.8748778792&1.000977\\
8&0.8871945120&1.015249\\
9&0.8986703291&1.013297.
\end{array}
\]

**[COMPUTATIONAL]** The data strongly suggest

\[
1-\lambda_m\asymp\frac1m,
\]

and numerically are strikingly close to

\[
\lambda_m\approx\frac{m}{m+1}.
\]

The monotonicity

\[
\lambda_{m+1}\ge\lambda_m
\]

has a straightforward lifting argument and should be written formally if used.

Do **not** treat the \(1/m\) asymptotic as proved. The later neutral-structure work explains a plausible mechanism for it.

---

# 9. Sticky point, singular propagation, and critical neutral structure

Use the packet-boundary maps

\[
S(y)=4y+1,
\]

\[
B_1(y)=\frac{4y-1}{3}\quad(y\equiv1\pmod3),
\]

\[
B_2(y)=\frac{2y-1}{3}\quad(y\equiv2\pmod3).
\]

## 9.1 Linearizing coordinates

With

\[
u=3y+1,
\]

the sibling odometer becomes

\[
\boxed{u\mapsto4u.}
\]

With

\[
x=y+1,
\]

the dangerous phase-2 branch becomes

\[
\boxed{x\mapsto\frac{2x}{3}.}
\]

Thus \(v_3(y+1)\) is a genuine remaining shadow-depth around the sticky fixed point \(y=-1\).

## 9.2 Critical normalization and local propagation weights

A singular amplitude suggested by the finite Perron vectors grows like

\[
\left(\frac32\right)^{v_3(y+1)}.
\]

After normalizing by the loss of one ternary precision digit, the leading local propagation weights are

\[
\boxed{
B_2:1,\qquad B_1:\frac12,\qquad S:\frac14.
}
\]

Therefore the **only locally neutral edge type is the phase-2 branch**. Phase 1 contracts by \(1/2\), and pure sibling predecessor propagation contracts by \(1/4\).

This normalization corrects an earlier exploratory statement: at the raw recursive level the two maps meeting at \(-1/2\) have coefficients \(3/4\) and \(1/4\), which sum to 1, but after critical precision normalization the phase-1 contribution is \(1/2\). The effective normalized sum at that collision is \(3/4\), not 1.

Do not resurrect the incorrect normalized “neutral collision at \(-1/2\)” statement.

## 9.3 Explicit rational critical ray

Define

\[
z_0=-\frac12,
\qquad
z_{n+1}=\frac{3z_n+1}{2}.
\]

Then

\[
\boxed{
z_n=-1+\frac{3^n}{2^{n+1}}.
}
\]

The first terms are

\[
-\frac12,-\frac14,\frac18,\frac{11}{16},\frac{49}{32},\frac{179}{64},\ldots
\]

For \(n\ge1\),

\[
z_n\equiv2\pmod3
\]

and

\[
\boxed{B_2(z_n)=z_{n-1}.}
\]

So this ray is exactly neutral at leading singular order.

## 9.4 Important correction: not literally a unique global neutral ray

The visible \(z_n\) chain should not be overinterpreted as the only neutral ray in the full backward singularity graph.

**[PROVED_DERIVED, NOT YET FROZEN IN THE MAIN VERIFIER]** If

\[
P_2(t)=\frac{3t+1}{2}
\]

denotes a backward phase-2 singular predecessor, then

\[
\boxed{
\xi(t)=
\frac{2^{v_3(t+1)}(t+1)}{3^{v_3(t+1)}}
}
\]

is invariant under \(P_2\). Thus neutral rays are naturally classified by \(\xi\). The visible \(z_n\) ray has \(\xi=1/2\).

The correct mental model is therefore:

> one **neutral edge type** generating a family of neutral rays, with the \(z_n\) ray the diagnostically important one linked directly to the sticky \(-1\) geometry; all non-phase-2 local propagations are contracting.

The next session should freeze/verify this \(\xi\)-classification before relying on it in a publication proof.

## 9.5 Collision points

The exact local collision equations give only

\[
S(y)=B_1(y)\iff y=-\frac12,
\]

with both maps landing on \(-1\), and

\[
S(y)=B_2(y)\iff y=-\frac25,
\]

with both maps landing on \(-3/5\).

The second collision has large raw combined coefficient but no known short recurrence into the sticky \(-1\) structure. This is evidence that recurrence to the neutral component, not merely local coefficient size, is the relevant issue.

---

# 10. Exact side-bush separation

The latest work attacks excursions away from the sticky branch directly.

## 10.1 Negative-half-line invariance

**[PROVED_DERIVED]**

Every non-neutral exact side exit emitted from \(y=-1\) lands below \(-1\). Moreover

\[
y<-1
\]

implies

\[
S(y)=4y+1<-1,
\]

and whenever the branch is legal,

\[
B_1(y)=\frac{4y-1}{3}<-1,
\]

\[
B_2(y)=\frac{2y-1}{3}<-1.
\]

Hence the exact negative side bush can never return to \(-1\) or to the visible rational critical points \(z_n>-1\).

The exact first-return weight from that negative bush to the visible critical ray is therefore 0.

This does **not** by itself solve finite-cylinder shadowing: a boundary can be congruent to a critical point modulo \(3^m\) without being exactly equal to it. That finite-precision issue is what the spectral-gap certificate controls.

## 10.2 Immediate side-exit mass

For a phase-2 sticky state, non-neutral sibling exits occur in exact pairs. Their total precision-normalized mass is

\[
\boxed{\frac1{21}.}
\]

More strongly, the side-exit weight that retains at least \(s\) additional sticky digits is

\[
\boxed{
W_{\ge s}=\frac{3}{4^{3^{s+1}}-1}.
}
\]

Thus

\[
W_{\ge0}=\frac1{21},
\]

while

\[
W_{\ge1}=\frac{3}{4^9-1}=\frac1{87381}.
\]

Conditioned on leaving the critical branch, the fraction retaining even one sticky digit is

\[
\frac{1/87381}{1/21}
=\boxed{\frac1{4161}}.
\]

So over 99.97% of side-exit normalized mass loses all sticky depth immediately. Deeper shadow retention is super-exponentially suppressed.

---

# 11. Side-bush spectral-gap certificate

This is the strongest new machine-checked local lemma.

## 11.1 Negative-bush coordinate

For exact negative bush states \(y\le-2\), set

\[
\boxed{X=-(3y+1)\ge5.}
\]

Then under siblings,

\[
X(S^iy)=4^iX.
\]

The legal branch coordinates are

\[
X(B_2(S^iy))=\frac{2(4^iX+1)}3,
\]

\[
X(B_1(S^iy))=\frac{4(4^iX+1)}3.
\]

## 11.2 Precision-normalized side-bush operator

After factoring out one critical \(3/2\) unit of singular growth, the auxiliary side-bush operator is

\[
\mathcal Bf(y)
=
\sum_{i:\,S^iy\equiv2\,(3)}4^{-i}
 f(B_2(S^iy))
+
\sum_{i:\,S^iy\equiv1\,(3)}\frac12\,4^{-i}
 f(B_1(S^iy)).
\]

This is the exact operator certified in `collatz_side_bush_spectral_gap.py`.

## 11.3 Nine-residue fractional-moment Lyapunov function

Define

\[
\boxed{
G(y)=c_{y\bmod9}\,[-(3y+1)]^{1/4}
}
\]

for \(y\le-2\), with

\[
(c_0,\ldots,c_8)
=(156,453,670,226,654,264,100,287,716).
\]

Using exact rational upper majorants for the radical coefficients and a rigorous infinite sibling-tail bound, all 27 source lifts satisfy

\[
\boxed{
\mathcal BG(y)<0.99\,G(y).
}
\]

**[MACHINE_CHECKED_LOCAL_LEMMA]**

The worst certified ratio is

\[
\boxed{0.9888021178022558\ldots<0.99.}
\]

This is qualitatively different from the finite high-channel Perron problem: the ordinary side bush has an honest spectral gap after critical normalization.

## 11.4 Green-mass bound

The same rational majorants show the entire first side emission from one critical level has

\[
G\text{-mass}<34.
\]

Every negative bush state has

\[
G(y)>149.
\]

Therefore the total future precision-normalized ordinary bush mass generated by one critical emission is bounded by

\[
\frac{34}{149}(1+0.99+0.99^2+\cdots)
=
\boxed{
\frac{3400}{149}<22.82.
}
\]

This is the key side-bush conclusion:

> one critical level can emit only a uniformly bounded total transient cloud after normalization.

A critical episode lasting \(m\) neutral levels can therefore create at most \(O(m)\) such transient normalized bush mass.

This provides a concrete mechanism consistent with the empirical \(1/m\) finite-memory Perron defect.

---

# 12. Independent direct inverse-BFS oracle

A deliberately simple implementation now serves as an independent audit of the packet machinery.

For a pure `r=1` corridor

\[
n=2^{q+1}k-1,
\qquad
Y=2\,3^qk-1,
\]

start from \(Y\) and repeatedly apply the exact shortened inverse rules inside \([n,Y]\):

- \(y\mapsto2y\);
- if \(y\equiv2\pmod3\), \(y\mapsto(2y-1)/3\).

For the known hostile q=26 specimen

\[
q=26,
\qquad
k=278{,}850{,}931{,}755{,}356,
\]

the independent BFS reproduces exactly

\[
\boxed{20{,}275}
\]

trapped nodes, no lower leak, and

\[
\boxed{
\eta=0.535288764039315\ldots
}
\]

This agrees with the inherited packet/certificate calculations.

Use this BFS as a falsification oracle for proposed hostile families or claimed constants.

The obvious raw approximation

\[
k=3^m-1
\]

is **not** the hostile mechanism. Selected checks give ratios comfortably above 0.8 or leak. The critical 3-adic alignment occurs in an affine packet-boundary coordinate, not simply in raw \(k\).

---

# 13. What has been ruled out

These negative results are important. Do not waste a new session rediscovering them.

## 13.1 Uniform pointwise scale floor

**[FALSIFIED AS A PLAUSIBLE STRONG TARGET]**

A potential such as

\[
3C+\widehat E
\]

can undergo a q-dependent valley. Greedy exact affine trajectories gave minima behaving approximately like \(O(1/J_{\max})\), with representative normalized minima around

\[
0.1965,0.1805,0.1578,0.1404,0.1288
\]

for q around 40–56.

Therefore do not try to prove that scale capacity stays above a fixed positive fraction at every time.

## 13.2 First derivative-martingale correction

**[FALSIFIED]**

Height moments \(L=\sum J2^J\) and natural Beatty-normalized derivative corrections still exhibit the same shrinking q-dependent bottleneck. They are useful diagnostics but not sufficient final potentials.

## 13.3 Simple three-bin discrepancy correction

**[FALSIFIED]**

A scalar correction based only on the three bad-digit scale bins, such as

\[
A C+\widehat E-\kappa\widehat D,
\]

cannot be patched with a q-independent node coefficient. More 3-adic state is genuinely required.

## 13.4 Per-packet exponential potentials

**[FALSIFIED]**

Exponential potentials attached to individual packets fail even when they remember residues modulo

\[
3,9,27,81,243.
\]

Allowing more local residue memory improves the minimax deficit but does not make a simple bounded packet-local scale potential work.

## 13.5 Independent-packet Bellman amortization

**[FALSIFIED]**

Even when the legal deterministic Beatty carry word is respected, allowing each packet independently to choose its own worst ternary phase makes the guaranteed harvested fraction decay exponentially with channel height.

Thus the **shared common ternary digit is indispensable**. Any proof relaxation that lets packets choose hostile phases independently is too pessimistic.

## 13.6 Beatty carries alone

**[FALSIFIED AS SUFFICIENT]**

The legal Beatty sequence by itself does not rescue the local Bellman game. The common ternary coupling remains essential.

## 13.7 One-spike harmonic ansatz

**[FALSIFIED]**

A harmonic candidate of the form

\[
A\left(\frac32\right)^{v_3(y+1)}+\text{bounded regular correction}
\]

cannot satisfy an eigenvalue-1 finite-core splice. Singular credit propagates through a larger backward structure.

## 13.8 “Only one neutral rational spine”

**[CORRECTED]**

The visible \(z_n\) ray is highly important, but the full backward phase-2 graph contains a family of neutral rays classified by the invariant \(\xi\) in Section 9.4. What is unique locally is the **neutral phase-2 edge type**, not a single global ray.

## 13.9 Raw `k=3^m-1` sticky family

**[FALSIFIED]**

Long raw ternary `222...2` prefixes in \(k\) are not enough to realize the hostile mechanism.

## 13.10 Finite-ternary exhaustion shortcut

**[FALSIFIED]**

Although each individual ordinary \(k\) has a finite ternary expansion, \(k\) is unbounded independently of q. Arbitrarily long hostile 3-adic prefixes can therefore occur. “Eventually all digits are zero” does not give a uniform corridor theorem.

---

# 14. Interpretation of the current obstruction

The high-channel process should now be thought of as three coupled resources.

## 14.1 Critical scale

A narrow phase-2 neutral mechanism can preserve leading singular scale through long 3-adic shadowing episodes. This is the source of the finite-memory \(1/m\)-type bottleneck.

## 14.2 Transient side bushes

Every exact ordinary side bush emitted from the sticky mechanism is uniformly subcritical after normalization:

\[
\mathcal BG<0.99G.
\]

Per critical level, total future normalized bush mass is bounded by \(<22.82\).

Thus side bushes cannot themselves sustain critical growth indefinitely.

## 14.3 Packet fragmentation / strict drift

Whenever scale fragments into many packets, the strict packet potential earns one unit per successor packet every two digits:

\[
4H_2+\sum_QV(Q)\ge V(P)+\#Q.
\]

This is the mechanism by which a temporary loss of exponential scale may be converted into permanent certified inverse nodes.

The conjectural proof slogan is now:

> **Critical scale can survive only along a narrow neutral structure. Leaving it produces a transient bush. If scale is dispersed enough to create a deep pointwise valley, the dispersion creates many packet transitions, and strict packet drift must cash that fragmentation into actual inverse nodes.**

The missing theorem is to quantify this slogan with constants.

---

# 15. Desired next theorem: Spine–Bush–Packet Amortization Lemma

The next session should try to formulate and prove a theorem at the level of a **complete critical excursion**, not a single digit.

A useful abstract target is the following.

Let an entry ensemble have critical scale \(E_{\rm in}\) at high corrected height. Follow the exact common ternary dynamics until an excursion stopping time at which one of the following holds:

1. corrected height has dropped by a prescribed amount / entered the bounded low-channel kernel;
2. the ensemble has left the critical shadow class into ordinary side bushes;
3. enough two-digit packet transitions have occurred to accumulate strict packet drift.

Seek constants \(a,b,c,d>0\), independent of q and entry height, and a scale-normalized critical credit \(S_{\rm crit}\), such that an excursion potential of the rough form

\[
\boxed{
\mathscr A
=
aC
+bS_{\rm crit}
+cG_{\rm bush}
+d\sum_PV(P)
}
\]

has a **uniform excursion-level lower bound** or positive amortized drift.

An equivalent and perhaps easier formulation is a dichotomy:

\[
\boxed{
\text{over every complete critical excursion, either}
}
\]

\[
E_{\rm out}\ge \varepsilon E_{\rm in}
\]

or

\[
\Delta C\ge \varepsilon E_{\rm in},
\]

possibly with \(\Delta C\) replaced initially by

\[
4\Delta C+\Delta V
\]

and then telescoped until the packet credit is discharged.

The constant \(\varepsilon\) may be extremely small. A horrible explicit positive constant is acceptable. The immediate goal is **uniform positivity**, not optimization.

The side-bush spectral gap should be used to bound all noncritical excursions as a finite correction. The core missing quantitative bridge is:

> **scale loss / critical fragmentation \(\Rightarrow\) enough cumulative packet count or packet transitions \(\Rightarrow\) strict \(V\)-drift \(\Rightarrow\) actual certified nodes.**

---

# 16. Most promising quantitative bridge

The observed pointwise scale valley is approximately \(O(1/J)\), while the strict packet potential earns \(+1\) per successor packet every two digits.

Along hostile large-q trajectories, the valley occurs simultaneously with explosive packet-number growth. A representative q=56 diagnostic saw packet number increase from roughly 108,000 to over 2 million while average scale per packet collapsed from about \(5.8\times10^4\) to a few hundred.

This strongly suggests an inequality of the following type should be sought:

\[
\boxed{
E_{\rm in}-E_t
\lesssim
\sum_{s\le t}\omega_s N_s
+
\text{bounded side-bush correction},
}
\]

where \(N_s\) is packet count or a height-weighted packet count and \(\omega_s\) is chosen so that the strict two-digit drift can pay the right-hand side.

A more structural alternative is to prove that decreasing average scale per packet from \(\bar E\) to \(\bar E/J\) necessarily requires \(\Theta(J)\) packet refinements per unit surviving scale. Then the \(+\#Q\) term in the \(V\)-inequality pays exactly the critical \(1/J\) loss.

Do not assume this is true without proof. This is the central next research question.

---

# 17. Immediate next-session execution programme

The next session should proceed autonomously through the following gates.

## Task A — reproduce the frozen local lemmas first

Run, without modification:

1. `packet_positive_drift_verifier.py`;
2. `collatz_scale_mixing_verifier.py`;
3. `collatz_neutral_spine_verifier.py`;
4. `collatz_side_bush_spectral_gap.py`.

Expected headline outputs:

- strict packet drift passes;
- corrected-height geometric kernel passes;
- bad-hit split \(1366:43:2752\) in canonical ordering passes;
- Perron values m=1..9 pass;
- neutral-edge weights \(1,1/2,1/4\) pass;
- q=26 BFS reproduces 20,275 nodes and \(\eta=0.535288764039315\ldots\);
- side-bush worst ratio \(0.9888021178\ldots<0.99\);
- Green bound \(<3400/149\).

If any frozen verifier fails, stop the proof push and audit environment/code before continuing.

## Task B — freeze the neutral-ray quotient formally

Prove and add a verifier for the invariant

\[
\xi(t)=\frac{2^{v_3(t+1)}(t+1)}{3^{v_3(t+1)}}
\]

under

\[
P_2(t)=\frac{3t+1}{2}.
\]

Classify exactly what counts as the same neutral ray and how actual packet-boundary finite cylinders project to this quotient.

The purpose is to avoid accidentally proving statements only for the visible \(\xi=1/2\) ray.

## Task C — formalize a critical excursion decomposition

Define a stopping-time / combinatorial decomposition of exact packet evolution into:

- neutral phase-2 critical continuation;
- side-bush emissions;
- return to bounded low-channel packet kernel;
- packet fragmentation events.

This definition must preserve the **single common ternary digit**. Do not independently rotate descendants.

The decomposition should be compatible with finite 3-adic shadow cylinders, not only the exact rational point \(-1\).

## Task D — convert the G-certificate into a reusable bush-charge lemma

Use

\[
\mathcal BG<0.99G
\]

and the \(<22.82\) total Green bound to state a lemma of the form:

> total future scale/credit contributed by all ordinary side bushes emitted during an m-level critical episode is at most \(K_0m\), with an explicit \(K_0\).

Prefer a theorem that charges bush mass to critical levels rather than tracking each bush separately.

## Task E — derive a scale-to-fragmentation inequality

This is likely the decisive new mathematics.

Search for a deterministic inequality linking exponential capacity \(E\), packet count \(N\), corrected heights, and/or packet moment \(V\). Candidate forms include:

\[
E\le \sum_P a(h_P)V(P)+bN,
\]

or an excursion integral

\[
\int \frac{N_t}{E_t}\,dt \gtrsim \log\frac{E_{\rm in}}{E_{\rm out}},
\]

or a discrete entropy/fragmentation inequality measuring the reduction of average \(2^J\)-scale per packet.

The inequality must be strong exactly in the regime where pointwise \(E\) becomes small.

## Task F — splice strict packet drift

Apply

\[
4H_2+\sum_QV(Q)\ge V(P)+\#Q
\]

over successive two-digit blocks.

Aim to convert the cumulative packet-count lower bound from Task E into either:

- actual new node mass \(\sum H_2\); or
- residual \(V\)-credit that must later be discharged because corrected height cannot increase forever.

Establish careful distinctness: counted nodes must be genuinely new in the inverse closure or charged in a way that avoids double counting.

## Task G — prove an excursion dichotomy

Target:

\[
\boxed{
\text{critical excursion from scale }E_0
\implies
E_{\rm exit}+A\,C_{\rm new}\ge\varepsilon E_0
}
\]

for explicit constants \(A<\infty\), \(\varepsilon>0\) independent of height/q.

If direct \(C\) is too hard, allow temporary \(V\)-credit, but prove that it telescopes away over a complete bounded-to-bounded excursion.

## Task H — arbitrary-length pure `r=1` corridor theorem

Once Task G is available, reconnect entry scale to corridor scale \(Y/n\).

Desired result:

> There exists an explicit universal \(c_0>0\) such that every sufficiently long pure `r=1` corridor beginning at the global lower barrier either has a legal inverse leak below the barrier or forces at least
> \[
> c_0\frac Yn
> \]
> distinct trapped inverse nodes in \([n,Y]\).

Do not optimize \(c_0\). Even \(10^{-100}\) would be conceptually decisive if rigorous and uniform.

## Task I — only after Task H, reconnect to mixed excursions

Use the inherited fact that supercritical blocks contain a positive fraction of `r=1` steps. The hard later task is to decompose mixed r-words into enough pure/near-pure productive pieces while managing local leaks and overlaps.

Do not jump to this before the pure-corridor amortization theorem is genuinely closed.

---

# 18. Research gates

## Gate 1 — verifier reproduction

All frozen scripts pass from a clean environment.

## Gate 2 — neutral-ray quotient frozen

The \(\xi\) invariant and ray classification are formalized and machine-checked.

## Gate 3 — finite-cylinder critical-excursion decomposition

Exact common-digit coupling is preserved and side emissions are correctly identified.

## Gate 4 — side-bush charge theorem

The \(<0.99\) spectral gap is converted into an explicit excursion-level \(O(m)\) bush correction.

## Gate 5 — scale-to-fragmentation lemma

A deterministic inequality quantitatively forces packet proliferation when scale enters the critical valley.

## Gate 6 — packet drift splice

Cumulative fragmentation is converted into certified node mass using \(V\).

## Gate 7 — uniform critical-excursion dichotomy

An explicit \(\varepsilon>0\) independent of q/height is proved.

## Gate 8 — arbitrary pure `r=1` corridor theorem

Lower leak or \(c_0Y/n\) trapped mass for all sufficiently long corridors.

## Gate 9 — mixed excursion integration

Reconnect to hypothetical `RO` least-counterexample excursions and density.

---

# 19. Claim ledger at handover

## 19.1 Proved/derived algebraic structure

- least-counterexample barrier;
- pure `r=1` corridor formulas;
- sibling odometer \(S(y)=4y+1\);
- corrected-height variable \(h=J-r_t\);
- exact geometric averaged kernel \(1/2,1/4,1/8,\ldots\);
- pointwise corrected top height never increases;
- coordinate linearizations \(u=3y+1\), \(x=y+1\);
- critical-normalized local edge weights \(B_2=1,B_1=1/2,S=1/4\);
- explicit visible critical ray \(z_n=-1+3^n/2^{n+1}\);
- collision points \(-1/2\) and \(-2/5\);
- negative-half-line invariance for exact side bushes;
- immediate side mass \(1/21\);
- sticky-depth tail \(3/(4^{3^{s+1}}-1)\);
- neutral-ray invariant \(\xi\), derived but should be newly frozen.

## 19.2 Machine-checked local lemmas

- eight fragile packet kernel reproduced;
- uniform strict two-digit packet drift using \(V\);
- high-channel base margins and \(x\mapsto x+6\) algebraic increments;
- exact moment identities;
- exact bad-hit mixing split;
- side-bush nine-residue Lyapunov inequality \(\mathcal BG<0.99G\);
- side-bush Green bound \(<3400/149\).

## 19.3 Independent computational reproductions

- hostile q=26 direct BFS: 20,275 trapped nodes, \(\eta=0.535288764039315\ldots\);
- q=24 inherited certificate independently reconstructed in the previous session.

## 19.4 Computational evidence / conjectures

- finite 3-adic Perron multipliers satisfy \(1-\lambda_m\approx1/(m+1)\) through at least frozen m=1..9;
- critical pointwise scale valleys empirically behave on the order of \(1/J\);
- hostile scale collapse coincides with large packet fragmentation;
- the desired amortization should trade scale loss for cumulative strict packet drift.

## 19.5 Falsified / corrected

See Section 13. Most importantly:

- no uniform pointwise scale floor;
- no per-packet independent-phase solution;
- no one-spike harmonic solution;
- raw \(k=3^m-1\) is not the hostile family;
- finite ternary exhaustion is not uniform;
- visible \(z_n\) ray is not literally the only neutral ray;
- normalized \(-1/2\) collision is contracting, not neutral.

## 19.6 Open theorem targets

1. neutral-ray quotient formalization;
2. finite-cylinder critical excursion decomposition;
3. scale-to-fragmentation lemma;
4. spine–bush–packet amortization lemma;
5. uniform arbitrary-length pure `r=1` corridor theorem;
6. mixed excursion telescope;
7. positive-density contradiction for a hypothetical least `RO` counterexample.

---

# 20. Frozen artifact manifest and hashes

All paths below refer to the current handover bundle/runtime layout. A new session receiving the bundle should preserve filenames even if paths change.

## 20.1 Previous authoritative handover and data

`Collatz_Rsharp_Odometer_Packet_Potential_Handover_2026-08-17.md`

SHA-256:

`afe74573b234f665674422352dd11aa65bc76c8aea9d95b515126d1247af8c81`

Data files:

- `hold24.csv` — `3a2f8e2b34db742122ea4c0f05c40d39f405043fd95444c06a5cca2e164ff35c`
- `hold26.csv` — `f92a6fa5a1076f51190119aaec6d79a2267f6245db42669a707db6a329d2f2f7`
- `initstats.csv` — `092ce051c2f68fbcf0458d2e60fe27d83be5e43abf8e900cb7ffe86abf724a51`
- `trans24.csv` — `4af84a2f23d2bdef04108c24e0e8f6083ff0628ec822a84468dba5888536c1d0`
- `trans26.csv` — `5ef120f07c88f369d66dbb3c942f3eeb74fe273900c13da1f7623f33d1971d1d`

Original 2026-08-17 bundle:

`Collatz_Rsharp_Odometer_Packet_Potential_Handover_Bundle_2026-08-17.zip`

SHA-256:

`d4478b64f24c2dd05a8b1f468b205482e3b6fc59f3127c36d827335d1b11c5a8`

## 20.2 New theorem-bearing verifiers

`packet_positive_drift_verifier.py`

SHA-256:

`779ce1038a19300b0471fb064664b6441a3551c7567aa6cacf1b538096b4e9c0`

Purpose: reproduces fragile packet kernel; checks strict \(V\)-drift; verifies high-channel base margins and \(x\mapsto x+6\) increment identities.

`collatz_scale_mixing_verifier.py`

SHA-256:

`a96f8772343c9c16c84591e484178a4bd4658f3557b97626bfb870b69cf51e3e`

Purpose: exact moment identities; corrected-height geometric kernel; exact bad-hit mixing split; Perron m=1..9 reproduction.

`collatz_3adic_perron.py`

SHA-256:

`f599ee8ffaf9dc1ffa363604854e5681d44ec1b0e077d7eb798b34071687c3aa`

Purpose: exploratory nonlinear Perron iteration at configurable memory depth.

`collatz_badclass_trace.py`

SHA-256:

`3ea42fa21bf919039c3af4b2594ceac4a7ce57179bb49bb54216fa02b07eb156`

Purpose: traces vulnerable-scale class mixing on hostile affine trajectories.

`collatz_beatty_bellman.py`

SHA-256:

`6fa3aaabb108348b2b0c707a6c033b6580416fc8d1eda5045acb8ec62f554dc6`

Purpose: falsifies the independent-packet legal-Beatty Bellman shortcut.

`collatz_neutral_spine_verifier.py`

SHA-256:

`4732eccaf617c0b3764a773a0f7d457245b6852e331fbb005db0099f48fac445`

Purpose: coordinate identities; critical-normalized edge weights; collision points; explicit visible spine; independent q=26 BFS; raw `k=3^m-1` falsification checks.

`collatz_side_bush_spectral_gap.py`

SHA-256:

`4f74aaec099ef8fe4f7fe88503ac2a606081f0d83ede776f321da0a56567ad74`

Purpose: exact-rational nine-residue side-bush Lyapunov certificate \(<0.99\); negative-half-line invariance audit; side-emission identities; finite-cylinder shadow coupling audit; Green bound \(<3400/149\).

---

# 21. Audit notes for publication-quality work

Before any public theorem claim, do all of the following.

1. Reimplement the strict packet kernel independently from the mathematical rules rather than copying the verifier.
2. Turn the high-channel \(x\mapsto x+6\) induction into ordinary prose proof.
3. Re-derive the side-bush operator \(\mathcal B\) carefully from the packet/sibling rules and verify every normalization coefficient.
4. Independently check the nine residue weights and all rational radical majorants in the \(<0.99\) certificate.
5. Replace floating display of the worst ratio by an exact rational inequality against \(99/100\).
6. Formalize finite-cylinder shadow coupling for arbitrary legal labels, not only sample paths.
7. Freeze and independently verify the neutral-ray invariant \(\xi\).
8. Prove all node distinctness / no-double-counting statements used in the final amortization telescope.
9. Keep computational evidence such as \(1-\lambda_m\sim1/m\) labelled empirical unless a proof is obtained.
10. Do not imply that the Collatz conjecture has been solved until the mixed excursion and global least-counterexample argument are complete.

---

# 22. What not to redo

A fresh session should not spend material time on:

- generic introductions to Collatz;
- re-deriving the least-counterexample barrier;
- rebuilding q=24 cylinder search from scratch unless auditing;
- hunting for a stronger fixed q=24 constant;
- literal frontier-state equality compression;
- independent worst-phase packet potentials;
- simple residue-only exponential packet Lyapunov functions;
- first-moment or first derivative-martingale scale corrections;
- a scalar three-class Fourier/discrepancy potential;
- raw `k=3^m-1` hostile searches;
- arguing that finite ternary expansions force eventual recovery;
- treating the visible \(z_n\) ray as the only neutral ray;
- trying to prove a uniform pointwise lower bound for \(E_t/E_0\).

The next new mathematics should target **amortization across a complete critical excursion**.

---

# 23. Fresh-session kickoff instruction

Use the following instruction verbatim or nearly verbatim in a clean session:

> Continue the 3n+1 / Collatz `R#` excursion-to-proliferation research from `Collatz_Rsharp_Spine_Bush_Packet_Amortization_Handover_2026-08-18.md`.
>
> Treat that handover as the authoritative current state. Do not restart from generic Collatz background and do not silently promote computational evidence to theorem status.
>
> First reproduce the frozen theorem-bearing verifiers and confirm their hashes/results. Then proceed directly to the **Spine–Bush–Packet Amortization Lemma** programme in Section 17.
>
> The core established ingredients are:
>
> 1. strict packet drift
> \[
> 4H_2+\sum_QV(Q)\ge V(P)+\#Q;
> \]
> 2. exact corrected-height geometric scale kernel;
> 3. one locally neutral phase-2 3-adic propagation type, with explicit critical rays;
> 4. exact side-bush spectral gap
> \[
> \mathcal BG<0.99G;
> \]
> 5. total normalized bush Green mass \(<3400/149\) per critical emission.
>
> The main unresolved step is to prove that a critical scale collapse forces enough fragmentation / cumulative packet transitions that the strict packet drift converts it into permanent inverse-node mass. Preserve the exact common ternary digit coupling at all times.
>
> Aim first for any explicit uniform \(\varepsilon>0\), however small, in an excursion dichotomy of the form
> \[
> E_{\rm exit}+A\,C_{\rm new}\ge\varepsilon E_{\rm in},
> \]
> or a temporary variant including residual \(V\)-credit that telescopes away.
>
> Once such an excursion lemma is proved, derive an arbitrary-length pure `r=1` corridor theorem: lower leak or at least \(c_0Y/n\) distinct trapped inverse nodes for some universal \(c_0>0\). Only after that should the research return to mixed r-words and the global `RO` density argument.
>
> Act autonomously: derive, compute, falsify, and verify. If a candidate inequality fails, retain the counterexample and use it to sharpen the state/potential rather than reverting to previously falsified routes.

---

# 24. One-paragraph current state

The programme has reduced a difficult arbitrary-length inverse-Collatz proliferation problem to a much more structured critical-process question. Packet starvation no longer has recurrent zero drift: a corrected finite potential \(V\) earns strict two-digit packet-count drift. Exponential corridor scale is captured by \(E=\sum2^J\), whose Beatty-normalized corrected-height dynamics have an exact geometric downward kernel. Pointwise scale can nevertheless fall through an \(O(1/J)\)-type critical valley, so uniform instantaneous scale preservation is the wrong theorem. The remaining high-credit 3-adic structure is generated by the unique locally neutral phase-2 edge type near \(y=-1\), with explicit critical rays, while every exact ordinary side bush is uniformly transient: the frozen nine-residue Lyapunov function satisfies \(\mathcal BG<0.99G\) and bounds total normalized future bush mass per critical emission by \(<22.82\). The next decisive step is therefore to prove a **spine–bush–packet amortization lemma** showing that any temporary critical scale loss necessarily creates enough packet fragmentation / transitions for the strict \(V\)-drift to bank proportional permanent inverse-node mass. A uniform positive excursion constant would likely unlock the arbitrary-length pure `r=1` corridor theorem and reopen the route toward a density contradiction for a hypothetical least unbounded Collatz counterexample.
