---
title: "Collatz R# Excursion-to-Proliferation — Odometer / Packet Potential Handover"
date: "2026-08-17"
status: "ACTIVE_RESEARCH_HANDOVER"
project: "3n+1"
intended_reader: "AI / mathematical research agent"
map_convention: "Shortened Collatz map T(n)=n/2 if even, (3n+1)/2 if odd; accelerated odd map F_r(u)=(3u+1)/2^r."
authoritative_previous_handover: "Collatz_Rsharp_Finite_Certificate_State_Compression_Handover_2026-08-17.md"
primary_goal: "Turn the finite q=24 leak-or-proliferate certificate into a reusable arbitrary-length r=1 corridor mechanism, then reconnect it to mixed RO excursions."
claim_labels:
  PROVED_DERIVED: "Algebraically derived in-session. Re-check and write as ordinary proof before publication."
  INDEPENDENT_COMPUTATIONAL_REPRODUCTION: "A result was reproduced by a separate in-session implementation; still needs frozen source/certificate and external audit."
  COMPUTER_ASSISTED_CANDIDATE: "Finite exact/computational evidence produced in-session; not yet publication-grade."
  MACHINE_CHECKED_LOCAL_LEMMA: "Finite transition/kernel statement checked exhaustively in-session; should be independently reimplemented and preferably hand-reduced."
  COMPUTATIONAL: "Experimental evidence only."
  CONJECTURE: "Open target."
  FALSIFIED: "Tested candidate statement that failed; do not resurrect without a materially new hypothesis."
  EXTERNAL_REVERIFY: "Depends on an external literature/verification fact. Re-open the authoritative current source before publication use."
---

# 0. Purpose of this handover

This memo supersedes `Collatz_Rsharp_Finite_Certificate_State_Compression_Handover_2026-08-17.md` as the operational starting point for the next research session.

Do **not** restart from generic Collatz background.

The previous handover ended with the first finite all-residue certificate for a 24-step pure `r=1` corridor:

\[
\text{lower leak}\quad\lor\quad |\mathrm{Cl}_{[n,Y]}|\ge \frac{14}{25}\frac Yn.
\]

The main unresolved problem was to replace the exploding ternary-cylinder search by a reusable finite state / block potential.

This continuation made several structural advances:

1. the q=24 headline certificate was independently reconstructed in-session;
2. the literal inverse frontier was compressed to a bounded set of logarithmic **scale channels**;
3. the remaining ternary carry structure was shown to be an exact **3-adic sibling odometer**, not arbitrary residue noise;
4. inverse-frontier chains were grouped into arithmetic **packets**;
5. all sufficiently high packets were shown, by exact two-digit transition analysis, to be **self-financing**;
6. the entire starvation obstruction was reduced to a finite **eight-type fragile kernel**;
7. a genuine two-digit **telescoping packet potential** was found;
8. several attractive stronger constants and rank claims were falsified, clarifying what the eventual proof must and must not use.

The next target is no longer generic state compression. It is:

> **derive a positive-drift inequality from the odometer/packet structure, most plausibly by controlling ternary phase discrepancy in the eight-type fragile kernel.**

If that succeeds, the pure long-`r=1` corridor may become an arbitrary-length theorem rather than a family of finite certificates.

---

# 1. Core definitions and notation

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
- `R#` (written mathematically \(R^\#\)): least positive integer in `R`, if `R` is nonempty;
- \(R(X)=\#(R\cap[1,X])\).

For the accelerated odd map,

\[
F_r(u)=\frac{3u+1}{2^r},
\qquad
r=\nu_2(3u+1)\ge1.
\]

For a record-scale excursion use lower barrier \(n\) and upper ceiling \(Y\).

Inverse children under the shortened map are

\[
2y
\]

always, and

\[
\frac{2y-1}{3}
\]

when \(y\equiv2\pmod3\).

For a seed set \(S\subset[n,Y]\), let \(\mathrm{Cl}_{[n,Y]}(S)\) be its trapped inverse closure.

Normalize by

\[
\eta(S;n,Y)=\frac{|\mathrm{Cl}_{[n,Y]}(S)|}{Y/n}.
\]

For \(n=R^\#\), every inverse predecessor of a red node is red. A legal predecessor below \(R^\#\) contradicts minimality.

Keep separate:

1. infinitely many red integers;
2. positive upper density;
3. positive lower/natural density;
4. every integer above \(R^\#\) red.

This programme targets 2/3, not 4.

---

# 2. Inherited active results

These come from the previous handover and remain active unless explicitly amended below.

## 2.1 Minimality barrier

**[PROVED_DERIVED]**

If \(R^\#\) exists,

\[
T^k(R^\#)\ge R^\#\qquad\forall k\ge0.
\]

Also

\[
R^\#\text{ is odd},
\qquad
R^\#\not\equiv2\pmod3.
\]

Hence

\[
R^\#\equiv0\text{ or }1\pmod3.
\]

## 2.2 Bounded discrepancy would already imply positive density

With

\[
m_k=\#\{\text{odd shortened steps before time }k\},
\qquad
\alpha=\log_3 2,
\]

\[
D_k=m_k-\alpha k,
\qquad
C_k=3^{D_k},
\]

the inherited result is:

**[PROVED_DERIVED]**

If an injective infinite `RO` orbit satisfies

\[
0<c\le C_k\le M<\infty,
\]

then

\[
\underline d(R)\ge\frac{3c}{\alpha M}>0.
\]

Therefore a density-zero `RO` must exhibit unbounded discrepancy / large coefficient excursions.

## 2.3 Supercritical blocks force many r=1 transitions

If a block has \(q\) accelerated odd transitions and

\[
\frac{3^q}{2^{r_1+\cdots+r_q}}\ge1,
\]

then if \(A\) of the \(r_j\)'s equal 1,

\[
\boxed{
A\ge
2q-\lfloor q\log_2 3\rfloor
=
\left\lceil(2-\log_2 3)q\right\rceil.
}
\]

Thus at least about 41.5% of odd transitions are `r=1`.

## 2.4 Pure r=1 corridor arithmetic

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
\boxed{Y=2\,3^q k-1.}
\]

The corridor approaches \(-1\) 3-adically:

\[
u_j+1=\left(\frac32\right)^j(u_0+1),
\qquad
u_j\equiv-1\pmod{3^j}.
\]

## 2.5 q=24 finite certificate inherited from previous handover

Threshold

\[
c=\frac{14}{25}=0.56.
\]

Previous certificate statistics:

- terminal ternary depth: \(K=21\);
- terminal compressed cylinders: \(142{,}371\);
- `MASS` terminals: \(142{,}295\);
- `LEAK` terminals: \(76\);
- unresolved cylinders: 0;
- exact depth-21 coverage: \(3^{21}\);
- weakest final ratio: approximately \(0.560053294775\);
- same statistics for all four \(k\bmod4\) continuation classes.

The theorem represented by that certificate is:

> a 24-step `r=1` block beginning at the global lower barrier either leaks below the barrier or forces at least \((14/25)(Y/n)\) distinct inverse nodes in \([n,Y]\).

Publication status remains computer-assisted pending the audit gates in Section 15.

---

# 3. Independent q=24 reconstruction in this continuation

**[INDEPENDENT_COMPUTATIONAL_REPRODUCTION]**

A separate in-session implementation reconstructed the q=24 certificate using paired affine endpoint/lift logic rather than the original certificate searcher's symbolic control flow.

It reproduced the headline statistics exactly for one continuation class and then for all four \(k\bmod4\) classes:

\[
142{,}371\text{ terminals},
\]

\[
142{,}295\text{ MASS},
\qquad
76\text{ LEAK},
\]

\[
K_{\max}=21,
\qquad
0\text{ unresolved},
\]

with minimum certified ratio

\[
\boxed{0.560053294775141\ldots}.
\]

This materially strengthens confidence in the q=24 result, but the implementation/certificate should still be frozen and independently audited outside this conversation before publication use.

### Important implementation warning

A **different experimental symbolic evaluator** used later in the state/rank work suffered an intermediate 128-bit overflow. It generated spurious frontier anomalies until caught by forward-legality checking.

This overflow did **not** become an accepted mathematical counterexample. The contaminated observations were discarded.

After switching the relevant audits to arbitrary-precision integer arithmetic, the suspect frontier roots disappeared and forward checks were clean.

Do not use fixed-width arithmetic for symbolic numerators merely because the final divided node fits in the integer type.

---

# 4. Exact affine frontier structure and scale channels

An inverse path from the corridor ceiling \(Y\) has affine form

\[
\boxed{
x=\frac{2^\ell Y-A}{3^d}
}
\]

for path-dependent integers \(\ell,A,d\).

Here \(d\) counts odd inverse divisions.

After resolving \(K\) ternary digits beyond the compulsory q-digit \(-1\) tail, unresolved odd branches occur at

\[
\boxed{d=q+K.}
\]

Changing to another lift within the same ternary cylinder changes such an affine node by a predictable multiple of \(3^{q+K-d}\); this is why all odd-inverse legality below the current frontier is already fixed, while the next ternary digit acts precisely on the frontier.

## 4.1 Channel variable

Define

\[
\boxed{
J=\lfloor d\log_2 3\rfloor-\ell.
}
\]

**[PROVED_DERIVED / hand proof still required]**

For an unresolved frontier node, \(J\) is the exact number of further legal even inverse doublings available before exceeding the ceiling, under the corridor normalization used by the search.

At depth \(K\), where \(d=q+K\), the lower/upper-window geometry confines \(J\) to a bounded strip depending on \(q\), not on \(K\): approximately

\[
0\le J\le q\log_2(3/2).
\]

Thus the number of scale channels is only

\[
\boxed{
O(q),
}
\]

and for q=24 it is only about 14-15 channels.

This is the first true compression of the raw ternary tree: raw cylinder count may be exponential in \(K\), while geometric scale type is bounded independently of \(K\).

---

# 5. Local channel gain algebra

For one frontier chain of channel \(J\), define the Beatty carry

\[
\delta_d=
\lfloor(d+1)\log_2 3\rfloor-
\lfloor d\log_2 3\rfloor-1
\in\{0,1\}.
\]

For the next ternary split, one digit kills the chain and the other two produce explicit node gains.

If

\[
J=2h,
\]

the two nonzero gains are

\[
\boxed{
A=(h+1)(h+\delta+1),
\qquad
B=h(h+\delta+1).
}
\]

If

\[
J=2h+1,
\]

the two nonzero gains are

\[
\boxed{
A=(h+1)(h+\delta+2),
\qquad
B=(h+1)(h+\delta+1).
}
\]

Therefore each chain contributes the multiset

\[
\boxed{\{0,A,B\}}
\]

across the three possible next ternary digits.

This converts much of the inverse-tree problem into a weighted three-phase balancing problem.

---

# 6. Exact 3-adic sibling odometer

This is the strongest new structural lemma from this continuation.

Take successive legal odd inverse children generated along one even chain. Index them by \(i\):

\[
y_i.
\]

Successive siblings satisfy

\[
\boxed{y_{i+1}=4y_i+1.}
\]

Hence

\[
\boxed{
3y_i+1=4^i(3y_0+1).
}
\]

Now use

\[
v_3(4^{3^h}-1)=h+1,
\]

so 4 has exact order \(3^h\) modulo \(3^{h+1}\) inside the subgroup of units congruent to 1 modulo 3.

Because

\[
y\mapsto3y+1
\]

is a bijection from residues modulo \(3^h\) to that subgroup, one obtains:

**[PROVED_DERIVED]**

\[
\boxed{
 y_0,y_1,\ldots,y_{3^h-1}
 \text{ form a complete residue system modulo }3^h.
}
\]

Interpretation:

> a block of \(3^h\) siblings is perfectly balanced through \(h\) ternary digits of future legality information.

The previously observed period-three kill-phase cycle is only the \(h=1\) shadow of this stronger fact.

This means the deep 3-adic history inside a sibling family is an exact cyclic odometer, not arbitrary noise.

This lemma should be written as a clean standalone proposition early in the next session.

---

# 7. Packet normal form

Sibling chains generated from one frontier chain have channels descending by 2.

Write a packet as

\[
\boxed{
P_{x,b}=(x,x-2,x-4,\ldots,b),
}
\]

where

\[
b\in\{0,1,2\}
\]

and \(x\equiv b\pmod2\), \(x\ge b\).

If

\[
x=b+2r,
\]

then its already-counted node mass is

\[
\boxed{
F(P_{x,b})=(r+1)(b+r+1)
=
\frac{(x-b+2)(x+b+2)}4.
}
\]

The Beatty carry sequence used by packet evolution has no `00` pair because

\[
\log_2(3/2)>\frac12.
\]

Therefore over two consecutive ternary refinements the only admissible carry words are

\[
\boxed{01,\ 10,\ 11.}
\]

This is another finite reduction.

---

# 8. Two-digit packet self-financing theorem

Using exact two-digit residue evolution modulo 9, all three allowed carry words \(01,10,11\), and all starting phase rotations, the packet analysis yielded:

**[MACHINE_CHECKED_LOCAL_LEMMA]**

For every packet with top channel

\[
\boxed{x\ge6,}
\]

the number \(H_2(P)\) of genuinely new inverse nodes generated during the next two ternary refinements satisfies

\[
\boxed{
H_2(P_{x,b})\ge F(P_{x,b}).
}
\]

So every packet with top channel at least 6 is **self-financing within two ternary digits**.

Representative checks:

\[
P_{6,0}=(6,4,2,0),\qquad F=16,
\]

with worst exact two-step production 17;

\[
P_{6,2}=(6,4,2),\qquad F=15,
\]

with worst exact two-step production 17.

The earlier independent-phase relaxation could not prove these. Exact modulo-9 coupling is essential.

---

# 9. Eight-type fragile kernel

Because every packet with top channel \(x\ge6\) self-finances, the only packet types that can lose packet potential over two digits are:

| Packet | Present mass \(F\) | Guaranteed next-two-digit mass |
|---|---:|---:|
| \(P_{0,0}\) | 1 | 0 |
| \(P_{2,0}\) | 4 | 0 |
| \(P_{4,0}\) | 9 | 3 |
| \(P_{1,1}\) | 2 | 0 |
| \(P_{3,1}\) | 6 | 1 |
| \(P_{5,1}\) | 12 | 8 |
| \(P_{2,2}\) | 3 | 0 |
| \(P_{4,2}\) | 8 | 2 |

Thus the unbounded starvation problem has been reduced to a finite low-channel obstruction:

\[
\boxed{
\text{eight fragile packet types.}
}
\]

All higher packets can be treated as automatically safe in a two-digit amortized argument.

This is currently the most important compression result.

---

# 10. First genuine telescoping packet potential

Define a packet credit \(\Phi\) by

\[
\Phi(P)=
\begin{cases}
0,&P=P_{0,0},P_{2,0},P_{1,1},P_{2,2},\\
3,&P=P_{4,0},\\
1,&P=P_{3,1},\\
8,&P=P_{5,1},\\
2,&P=P_{4,2},\\
F(P),&\text{top channel }x\ge6.
\end{cases}
\]

Let \(H_2\) be genuinely new nodes created over the next two ternary refinements and let the surviving/generated final packets be \(Q\).

The finite exact packet transition check found:

**[MACHINE_CHECKED_LOCAL_LEMMA]**

\[
\boxed{
H_2+\sum_Q\Phi(Q)\ge\Phi(P)
}
\]

for every packet \(P\), every admissible two-carry word, every starting residue modulo 9, and every two-digit ternary continuation.

Summing over disjoint frontier packets gives a global monotone quantity:

\[
\boxed{
C_{t+2}+\sum_{P\in\mathcal P_{t+2}}\Phi(P)
\ge
C_t+\sum_{P\in\mathcal P_t}\Phi(P),
}
\]

where \(C_t\) is the number of already certified inverse nodes and \(\mathcal P_t\) is the packetized frontier.

This is the first compact, carry-independent **telescoping potential** found in the programme.

### Limitation

The inequality is presently nondecreasing, not uniformly positively drifting.

It therefore does **not yet** prove a linear bound

\[
C\ge cY/n.
\]

The missing piece is a positive-drift / discrepancy theorem showing that the fragile kernel cannot absorb indefinitely the surplus generated by safe packets.

---

# 11. Phase discrepancy and Fourier route

Inside hostile low-channel tails, the actual three residue populations remained surprisingly balanced for most of the descent.

One directly rebuilt q=26 hostile orbit displayed examples such as

\[
(115,119,127),
\]

then

\[
(93,92,97),
\]

then

\[
(85,103,84).
\]

Large imbalance appeared only close to extinction.

This is consistent with the sibling odometer.

Define the cubic Fourier discrepancy

\[
\boxed{
Z=N_0+\omega N_1+\omega^2N_2,
\qquad
\omega^3=1,\ \omega\ne1.
}
\]

Complete sibling triples cancel in \(Z\).

For three sibling chains with top channels

\[
x,\ x-2,\ x-4,
\]

the mean total gain is quadratic in \(x\), while the difference between largest and smallest ternary-digit gains was derived to be only

\[
\boxed{2x+2\delta-1.}
\]

Therefore, schematically,

\[
\text{bulk gain}=O(x^2),
\qquad
\text{phase discrepancy}=O(x).
\]

Summed across a long packet, bulk is expected to scale one degree faster than boundary discrepancy.

This is the leading candidate mechanism for upgrading monotone \(\Phi\) to positive drift.

### Next desired theorem

Seek a recurrence of the form

\[
\boxed{
|Z_{t+1}|
\le
\lambda |Z_t|+O(\text{fragile boundary}),
}
\]

with the discrepancy growth rate strictly smaller than the bulk gain growth rate.

Equivalent formulations using total variation among the three phases, packet boundary terms, or an explicit finite spectral matrix are all acceptable.

---

# 12. Hostile q=26 example independently rebuilt with big integers

A previously reported q=26 no-leak hostile cylinder was rebuilt directly using arbitrary-precision integers and full exact inverse closure, avoiding the fixed-width overflow issue.

Take

\[
q=26,
\qquad
k=278{,}850{,}931{,}755{,}356.
\]

Then

\[
n=2^{27}k-1,
\qquad
Y=2\,3^{26}k-1.
\]

The complete trapped inverse closure has

\[
\boxed{20{,}275}
\]

distinct nodes and no predecessor below \(n\).

Also

\[
\frac Yn\approx37876.75244106352,
\]

so

\[
\boxed{
\eta\approx0.535288764039315.
}
\]

Therefore:

**[COMPUTATIONAL / independently rebuilt in-session]**

\[
\boxed{
c=14/25=0.56\text{ does not extend universally to }q=26.}
\]

This hostile example eventually drives its entire frontier into the fragile low-channel kernel before extinction, directly supporting the packet picture.

A lower preliminary value around \(\eta\approx0.53046\) was reported during earlier exploratory search, but it was **not promoted in the final clean audit**. Recheck it independently before using it.

---

# 13. Further finite corridor evidence

The continuation reported the following additional finite results.

Treat them conservatively until a frozen verifier is produced.

## 13.1 q=26, c=1/2

**[COMPUTER_ASSISTED_CANDIDATE]**

A compressed exhaustive search was reported to close all cylinders by ternary depth 18, identically across the four \(k\bmod4\) continuation classes, with:

- evaluated states: 170,642;
- `MASS` terminals: 341,113;
- `LEAK` terminals: 172;
- unresolved: 0;
- maximum ternary depth: 18.

Thus the candidate finite statement is

\[
q=26
\quad\Longrightarrow\quad
\text{leak}\ \lor\ |\mathrm{Cl}|\ge\frac12\frac Yn.
\]

This must be independently rerun with arbitrary-precision-safe code before theorem-level use.

## 13.2 q=28, c=2/5

**[COMPUTER_ASSISTED_CANDIDATE]**

A compressed exhaustive search was reported to close all cylinders by ternary depth 15, again identically across all four \(k\bmod4\) classes, with:

- evaluated states: 129,194;
- `MASS` terminals: 258,148;
- `LEAK` terminals: 241;
- unresolved: 0;
- maximum depth: 15.

Candidate statement:

\[
q=28
\quad\Longrightarrow\quad
\text{leak}\ \lor\ |\mathrm{Cl}|\ge\frac25\frac Yn.
\]

## 13.3 q=30 disproves a universal c=1/2 continuation

**[COMPUTATIONAL]**

A no-leak terminal state was reported with

\[
|\mathrm{Cl}|=95{,}492,
\qquad
Y/n\approx191{,}751.0592,
\]

so

\[
\boxed{
\eta\approx0.4979998566<\frac12.
}
\]

Therefore the attractive hypothesis that \(c=1/2\) works uniformly for all pure `r=1` corridor lengths is false.

This example should also be independently rebuilt with arbitrary precision before publication use.

## 13.4 Hostile beam-search trend

**[COMPUTATIONAL ONLY]**

Adversarial searches reported approximate no-leak minima:

| q | hostile eta found |
|---:|---:|
| 24 | 0.58471 |
| 26 | 0.53046 preliminary / 0.53529 independently rebuilt explicit family |
| 28 | 0.51284 |
| 30 | 0.49800 |
| 32 | 0.48862 |
| 34 | 0.48439 |

For q>=28 these were search minima, not exhaustive optimal values.

The important qualitative observation is that hostile ratios were declining but appeared to flatten rather than obviously collapse toward zero.

Do not infer an asymptotic constant from this table.

---

# 14. Rank experiments: useful but secondary

Several deficit/capacity ranks were investigated.

Let

\[
D=\text{remaining node deficit to a chosen target},
\]

and let

\[
B_2=\min_{\text{unresolved two-digit continuations}}(\text{nodes gained over those two digits}).
\]

Define

\[
R_2=\left\lceil\frac D{B_2}\right\rceil.
\]

An early strict claim

\[
R_2(t+2)<R_2(t)
\]

was falsified by exact q=24 plateau states.

**[FALSIFIED]**

Do not use strict two-step descent as a theorem.

However, tested states showed no increase in \(R_2\), and plateau states appeared to discharge under a secondary quantity

\[
E=D-(R_2-1)B_2.
\]

One hostile plateau chain had

\[
E:1190\to349\to17
\]

while \(R_2=4\) remained constant.

This motivated the lexicographic candidate

\[
\boxed{(R_2,E).}
\]

**[CONJECTURE / computational support only]**

A sufficient two-digit inequality derived for lexicographic descent was

\[
\boxed{
H\ge R\max(0,B-B'),
}
\]

where \(H\) is two-digit gained mass and \(B,B'\) are the old/new two-step capacities.

This route remains available, but the odometer/packet/Fourier programme now has stronger structural justification and should be prioritized.

---

# 15. Important falsifications / routes not to redo

Preserve these negative results.

## 15.1 Strong constants

**[FALSIFIED]**

- universal \(c=1\) for arbitrary compatible record prefixes;
- universal q-independent \(c=14/25\);
- universal q-independent \(c=1/2\), based on the q=30 candidate hostile example.

The main conjecture only requires some absolute \(c>0\).

## 15.2 Literal frontier equality is the wrong state equivalence

At moderate depth, almost every unresolved cylinder had a different exact multiset of raw \((\ell,d)\) frontier types.

So merging only literally identical inverse frontiers does not solve the q=26 explosion.

The useful compression is by channel/packet dynamics and amortized potential, not exact raw frontier identity.

## 15.3 Independent hostile packet rotations are too pessimistic

Allowing each packet to choose its own adversarial ternary phase destroys the desired linear guarantee.

This is not the actual Collatz geometry.

The **same global ternary digit acts simultaneously on all packets**, and sibling phases are coupled by the odometer.

Do not throw away this global coupling.

## 15.4 Raw worst-gain monotonicity is false

The frontier's worst one/two-step capacity can decrease even while enough permanent nodes have already been banked.

Therefore a proof must be amortized.

## 15.5 Strict R2 descent is false

Plateaus exist.

If rank methods are revisited, use lexicographic correction or a packet potential.

## 15.6 Fixed-width symbolic arithmetic is unsafe

Intermediate affine numerators can exceed 128-bit width even when the final divided node is small.

Use arbitrary precision or formally established overflow bounds.

---

# 16. Current proof architecture

The programme is now best viewed as the following chain.

## Stage A — least-counterexample excursion structure

Large supercritical odd blocks force many `r=1` transitions.

Minimality forbids lower red predecessors and imposes shadow-code constraints.

## Stage B — pure long-r=1 corridor theorem

For a pure `r=1` corridor:

1. convert inverse paths to affine form;
2. compress unresolved branches to bounded logarithmic channels;
3. packetize sibling chains;
4. use the 3-adic sibling odometer to control ternary phases;
5. bank self-financing high packets;
6. reduce starvation to the eight-type fragile kernel;
7. upgrade the monotone packet potential \(\Phi\) to a **positive-drift** potential.

The desired result is an absolute \(c>0\) such that for arbitrarily long pure corridors,

\[
\boxed{
\text{global lower leak}\ \lor\ |\mathrm{Cl}_{[n,Y]}|\ge c\frac Yn.
}
\]

## Stage C — internal block composition

For an internal block beginning at \(a>R^\#\), a local leak \(z<a\) is not necessarily a contradiction.

But if the first downward odd predecessor exits below \(a\), then

\[
\boxed{
\frac{2a-1}{3}\le z<a.
}
\]

So local leakage transfers red mass downward by only a bounded scale factor rather than sending it arbitrarily far away.

This should be incorporated into the telescoping potential.

## Stage D — mixed r-words

Once the long pure `r=1` mechanism is established, reconnect it to the supercritical-block fact that at least about 41.5% of odd transitions are `r=1`.

The major mixed-word question is how to extract enough disjoint or overlapping `r=1` packet production from an arbitrary coefficient-supercritical excursion.

## Stage E — density conclusion

Use record excursions and the resulting linear red mass to rule out asymptotic negligibility of `R` in the `RO` case.

Record-gap control / lower-density conversion remains a separate downstream problem.

`RL` remains separate and should not be silently folded into the `RO` proof.

---

# 17. Immediate next-session execution programme

Proceed directly with these tasks.

## Task A — write the sibling odometer as a clean theorem

Prove in ordinary mathematics:

1. sibling recurrence
   \[
   y_{i+1}=4y_i+1;
   \]
2. identity
   \[
   3y_i+1=4^i(3y_0+1);
   \]
3. LTE/order statement
   \[
   v_3(4^{3^h}-1)=h+1;
   \]
4. exact order of 4 modulo \(3^{h+1}\);
5. complete residue theorem
   \[
   \{y_0,\ldots,y_{3^h-1}\}\equiv\mathbb Z/3^h\mathbb Z.
   \]

Check all legality/index assumptions explicitly.

**Gate:** this should become a hand-checkable lemma, not remain a computational observation.

## Task B — independently reimplement the packet transition kernel

Use arbitrary-precision arithmetic.

Inputs should be only:

- packet type \(P_{x,b}\);
- starting phase/residue modulo 9 (or the minimal sufficient odometer phase);
- one of carry words `01`, `10`, `11`;
- two global ternary digits.

Verify independently:

\[
H_2(P)\ge F(P)\quad\text{for }x\ge6,
\]

and reproduce the eight fragile packet table.

Then generate a small frozen certificate/verifier for this finite kernel.

## Task C — prove or machine-certify the packet potential

Independently verify

\[
H_2+\sum_Q\Phi(Q)\ge\Phi(P)
\]

for every allowed transition.

Then attempt to convert the finite check into a short human proof by:

1. proving a six-channel induction for all \(x\ge6\);
2. checking only the finitely many low packets explicitly.

## Task D — derive a positive-drift discrepancy inequality

This is the central task.

Represent ternary phase imbalance by

\[
Z=N_0+\omega N_1+\omega^2N_2.
\]

Use the sibling odometer to show complete groups cancel and only packet boundaries contribute to \(Z\).

Seek inequalities of one of the following forms:

\[
|Z'|\le \lambda|Z|+C\,B_{\rm fragile},
\]

or

\[
\min_j G_j\ge \frac13\sum_jG_j-C\,B_{\rm boundary},
\]

where bulk gain dominates the boundary term for large packets.

The target is a two-digit block inequality

\[
\boxed{
C_{t+2}+\Phi_{t+2}
\ge
C_t+\Phi_t+\varepsilon\,S_t
}
\]

for some meaningful scale quantity \(S_t\) and absolute \(\varepsilon>0\).

Even a conservative rational \(\varepsilon\) is valuable.

Do not optimize constants yet.

## Task E — solve the eight-type fragile kernel as a finite game

If Fourier control is difficult, formulate the fragile kernel as a finite Bellman/minimax system.

State should retain only genuinely necessary coupling information, likely:

- counts of the eight packet types;
- common ternary phase / residue class information;
- Beatty carry state;
- packet boundary discrepancy.

Seek:

- a rational linear/piecewise-linear potential;
- a finite spectral radius bound;
- or an explicit finite-state positive drift certificate.

## Task F — audit q=26/q=28 finite certificates using the packet engine

Re-run with arbitrary precision:

- q=26, target \(c=1/2\);
- q=28, target \(c=2/5\).

If they reproduce, freeze small certificate files and verifiers.

Use them as diagnostics for the general proof, not as the end goal.

## Task G — independently rebuild the q=30 c=1/2 counterexample

Confirm or falsify the reported

\[
\eta\approx0.4979998566.
\]

This is useful for understanding the true scale of any universal constant.

## Task H — incorporate local leaks as potential transfer

For an internal block, replace terminal `LEAK` by either:

- `GLOBAL_LEAK` if below \(R^\#\);
- `TRANSFER` if \(R^\#\le z<a\).

Give transferred red mass an explicit potential at its new lower scale.

The goal is to telescope successive corridor blocks.

---

# 18. Suggested research gates

## Gate 1 — odometer theorem formalized

Pass only when the sibling complete-residue result is written as a clean proof with all index/legal assumptions stated.

## Gate 2 — packet kernel independently reproduced

Pass only if a second arbitrary-precision implementation reproduces:

- the `x>=6` self-financing statement;
- the eight fragile packet types;
- their guaranteed two-digit gains.

## Gate 3 — packet potential certified

Pass only if a tiny verifier checks the finite low-kernel inequalities and a proof handles the high-channel induction.

## Gate 4A — positive drift obtained

Pass if a Fourier/Bellman/piecewise-linear potential proves a uniform positive drift term.

This would be the major breakthrough.

## Gate 4B — structural obstruction isolated

If positive drift fails, produce an explicit infinite family of packet/phase states where drift tends to zero and identify the diverging parameter.

Do not hide a genuine obstruction.

## Gate 5 — arbitrary pure r=1 corridor theorem

Pass if the positive-drift packet potential proves a leak-or-linear-proliferation theorem for arbitrary corridor length q with one fixed \(c>0\).

## Gate 6 — block telescope with local transfers

Pass if internal downward leakage can be composed without losing linear red mass.

## Gate 7 — mixed excursion integration

Only then reconnect to the 41.5% forced-`r=1` frequency and arbitrary supercritical `RO` excursions.

---

# 19. Current claim ledger

## Exact / derived

- least-counterexample lower barrier;
- \(R^\#\) odd;
- \(R^\#\not\equiv2\pmod3\);
- bounded discrepancy implies positive lower density;
- coefficient-supercritical blocks force at least about 41.5% `r=1` transitions;
- pure `r=1` corridor parameterization
  \[
  n=2^{q+1}k-1,
  \quad
  Y=2\,3^qk-1;
  \]
- \(-1\) 3-adic corridor congruence;
- affine inverse-path form;
- sibling recurrence
  \[
  y_{i+1}=4y_i+1;
  \]
- sibling odometer identity
  \[
  3y_i+1=4^i(3y_0+1);
  \]
- complete sibling residue system modulo \(3^h\) for blocks of length \(3^h\), subject to clean proof write-up;
- packet mass formula;
- no `00` Beatty carry pair;
- local leak scale bound
  \[
  (2a-1)/3\le z<a.
  \]

## Independently reproduced computational result

- q=24, \(c=14/25\) headline finite certificate statistics, including all four \(k\bmod4\) classes.

## Machine-checked local finite structure

- high packets \(x\ge6\) self-finance over two ternary digits;
- exactly eight fragile low packet types in the present two-digit model;
- explicit packet potential \(\Phi\) is nondecreasing after adding newly created node mass.

These need independent reimplementation and certificate freezing.

## Computational evidence / candidates

- q=26 explicit no-leak closure with 20,275 nodes and \(\eta\approx0.5352887640\), rebuilt using arbitrary precision;
- q=26, \(c=1/2\) full closure candidate;
- q=28, \(c=2/5\) full closure candidate;
- q=30 candidate counterexample to universal \(c=1/2\);
- hostile longer-q ratios appear to flatten above zero, but no asymptotic claim is justified;
- lexicographic rank \((R_2,E)\) has encouraging finite behaviour.

## Falsified

- universal \(c=1\);
- universal q-independent \(c=14/25\);
- likely universal q-independent \(c=1/2\) if q=30 rebuild confirms;
- literal frontier equality as useful state compression;
- independent adversarial packet rotations;
- raw worst-gain monotonicity;
- strict two-step \(R_2\) descent.

## Open conjectures / targets

- positive-drift packet/Fourier potential;
- arbitrary-length pure `r=1` leak-or-proliferate with one absolute \(c>0\);
- local-transfer telescope across internal blocks;
- mixed-`r` excursion theorem;
- positive upper/lower density consequence for `RO`;
- separate `RL` treatment.

---

# 20. Diagnostic artifacts currently available

The session directory contains these supporting files:

- `trans24.csv`
- `trans26.csv`
- `hold24.csv`
- `hold26.csv`
- `initstats.csv`

They arose during rank/transition diagnostics.

Treat them as **diagnostic**, not authoritative proof certificates. Some earlier exploratory transition data may predate the fixed-width overflow discovery, so any next session using them must establish which rows were generated before/after the arbitrary-precision correction.

Do not make theorem claims from these CSVs without regenerating them using the clean big-integer implementation.

The authoritative previous handover file is also present:

- `Collatz_Rsharp_Finite_Certificate_State_Compression_Handover_2026-08-17.md`

---

# 21. Publication/audit checklist

Before describing the new structure as publication-grade mathematics:

1. reverify the external computational Collatz bound and map convention;
2. write the sibling odometer theorem by hand;
3. formally establish the channel definition and window interpretation;
4. independently implement packet transitions with arbitrary precision;
5. freeze the exact eight-type kernel table;
6. produce a tiny verifier for the packet-potential inequalities;
7. prove the high-channel induction symbolically rather than enumerating arbitrarily large \(x\);
8. rebuild q=26/q=28 finite certificates with the clean packet engine;
9. independently rebuild the q=30 \(c=1/2\) counterexample;
10. formally prove distinctness/disjointness when packet credits are summed;
11. distinguish global-barrier leaks from internal-block transfers;
12. do not promote positive-drift claims until the discrepancy argument is actually proved.

---

# 22. What not to redo

Do not spend the next session rediscovering:

1. generic Collatz background;
2. why one red integer only implies infinitely many red integers, not density;
3. why exponent-1 growth alone is insufficient;
4. why \(c=1\) fails;
5. why the \(-1\)-only universal core is sublinear;
6. why raw q=26 ternary brute force explodes;
7. literal frontier-state equality hashing;
8. independent per-packet hostile phase rotations;
9. strict \(R_2\) descent;
10. attempts to preserve \(14/25\) or \(1/2\) as aesthetically preferred universal constants;
11. fixed-width symbolic numerators without formal overflow bounds.

The active problem is positive drift from packet/phase coupling.

---

# 23. Fresh-session kickoff instruction

The next AI agent should treat the following as the execution brief:

> Continue the Collatz \(R^\#\) excursion-to-proliferation programme from `Collatz_Rsharp_Odometer_Packet_Potential_Handover_2026-08-17.md`. Do not restart from generic Collatz background.
>
> The central new structure is the chain
>
> \[
> \text{affine frontier}
> \to
> \text{bounded scale channels}
> \to
> \text{sibling packets}
> \to
> \text{3-adic odometer}
> \to
> \text{eight-type fragile kernel}
> \to
> \text{two-digit telescoping packet potential}.
> \]
>
> First formalize and independently audit the sibling odometer and packet-kernel lemmas using arbitrary-precision arithmetic. Then attack the **positive-drift problem**.
>
> The preferred route is a ternary phase-discrepancy/Fourier argument. Use
>
> \[
> Z=N_0+\omega N_1+\omega^2N_2
> \]
>
> and the fact that sibling blocks of length \(3^h\) are complete modulo \(3^h\). Show that bulk packet gain grows faster than the boundary discrepancy that an adversarial common ternary digit can exploit.
>
> The desired theorem is a fixed-horizon inequality of the form
>
> \[
> C_{t+2}+\Phi_{t+2}
> \ge
> C_t+\Phi_t+\varepsilon S_t,
> \]
>
> for some absolute \(\varepsilon>0\) and an appropriate scale quantity \(S_t\).
>
> If a direct Fourier inequality fails, solve the eight-type fragile kernel as a finite Bellman/minimax or spectral problem while retaining the **global common ternary digit** and odometer coupling. Do not revert to independent adversarial packet rotations.
>
> Re-run q=26 at \(c=1/2\) and q=28 at \(c=2/5\) with clean arbitrary-precision packet code as audit/stress tests, but do not mistake finite-q certificates for the main goal.
>
> Actively search for counterexamples. If no positive drift exists, isolate the exact infinite family of packet/phase states that causes drift to vanish.
>
> If positive drift is proved, immediately use it to formulate an arbitrary-length pure `r=1` leak-or-proliferate theorem, then move to the internal-block transfer/telescoping problem. Only after that reconnect to mixed `r`-words and the inherited 41.5% forced-`r=1` frequency in supercritical excursions.
>
> Preserve the distinction between `RO` and `RL`, and do not theorem-inflate computational evidence.

---

# 24. One-paragraph current state

The programme has progressed from a one-off q=24 residue certificate to a much more structural view of long pure `r=1` excursions. The q=24, \(c=14/25\) finite certificate was independently reconstructed in-session. Unresolved inverse branches admit a bounded logarithmic channel coordinate, and sibling chains generated from one frontier root form arithmetic packets. Most importantly, successive odd siblings satisfy \(y_{i+1}=4y_i+1\), so \(3y_i+1=4^i(3y_0+1)\); because 4 has exact order \(3^h\) modulo \(3^{h+1}\), every block of \(3^h\) siblings forms a complete residue system modulo \(3^h\). Thus higher ternary carry information is an exact 3-adic odometer, not arbitrary history. Exact two-digit packet analysis then shows every packet with top channel at least 6 self-finances, reducing the starvation obstruction to eight fragile low-channel packet types. A finite packet credit \(\Phi\) has been found such that already-counted inverse nodes plus frontier packet credit is nondecreasing every two ternary digits. The missing step is a **positive drift** term. The leading route is to control ternary phase discrepancy, likely through a cubic Fourier coefficient, using the fact that packet bulk gain grows faster than odometer boundary imbalance. If successful, this would turn the q=24 finite certificate into an arbitrary-length pure-`r=1` leak-or-proliferate theorem, after which local leak transfer and mixed-excursion composition become the next bridges toward a density consequence for hypothetical `RO` counterexamples.
