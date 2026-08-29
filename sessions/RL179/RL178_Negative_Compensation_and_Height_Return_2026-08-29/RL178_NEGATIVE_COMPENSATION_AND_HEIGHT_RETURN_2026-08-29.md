# RL178 — negative compensation and height return

Date: 2026-08-29

## Outcome and classification

RL178 works the RL177 negative-compensation/height-return target in the preferred physical branch `h_p=0`.  It does **not** close that branch.  It does prove an exact second-transition valuation law, a residue-ordered deficit decomposition of the corrected flow, and a genuine exclusion inside the highest zero-height valuation case.

Retain

\[
G_i=S_{p+i}-S_p-S_i,
\qquad
F_2=\sum_i q_i(2^{G_i}-1)=3(\lambda-1)g_p,
\]

with the RL177 first mismatch

\[
1\le J\le36,\qquad
v=v_2(g_p)=S_J+\min(a_J,a_{p+J})\le37,
\]

and put `k=J+1`, `d=G_k!=0`, and `w=g_p/2^v` (odd).

The promoted results are:

1. **RL178.1 — exact signed pair relation and second-transition valuation law** (analytic).  At the first mismatch,
   \[
   d>0:\quad 2^d y_{p+k}-y_k=3^k w,
   \]
   \[
   d<0:\quad y_{p+k}-2^{|d|}y_k=3^k w.
   \]
   More generally, while `i<t`, the current signed relation and the next two accelerated exponents determine an exact 2-adic transition test.  This is a new arithmetic constraint beyond the RL177 height-only local automaton.
2. **RL178.2 — residue-ordered exact deficit decomposition** (analytic).  Reindex phases by the lifted-defect residue `r=A i (mod L)`.  The associated mechanical weights are strictly decreasing with `r`, and
   \[
   F_2=\rho_t-D,
   \qquad
   D=\sum_{r=1}^{L-1}(\omega_{r-1}-\omega_r)(1-2^{-H_r})>0.
   \]
   Thus every positive lifted-defect height contributes a positive, residue-localized loss from the mechanical envelope.  In a zero-height first mismatch this gives an explicit local deficit on the height-one vertex.
3. **RL178.3 — exclusion of the zero-height `v=37,J=23,d=+1` type** (analytic + exact arithmetic certificate).  RL176 forces `g_p=2^37`.  The first mismatch gives
   \[
   2y_{p+24}-y_{24}=3^{24},
   \]
   while the heights are `(1,0)` and the next mechanical digit is `c_24=1`.  Therefore `a_24 in {1,2}` and `a_{p+24}=1`.  But
   \[
   v_2(3^{25}+1)=2,
   \]
   whereas `a_24=1` would force valuation `1` and `a_24=2` would force cancellation valuation at least `3`.  Both are impossible.  Hence this signed physical type is excluded.
4. **RL178.4 — forced initial continuation of the surviving `v=37,d=-1` type** (analytic).  Here
   \[
   y_{p+24}-2y_{24}=3^{24},
   \]
   heights are `(0,1)`, and `v_2(3^{25}-1)=1`.  The next pair is forced to
   \[
   a_{24}=a_{p+24}=1,
   \]
   so `G_25=-1`.
5. **RL178.5 — exact earliest-return window for the surviving high type** (exact finite certificate with analytic transition rule).  Propagating only the mechanical height caps plus RL178.1's exact relation/valuation law gives necessary-state counts
   \[
   1,1,2,2,5,10,16
   \]
   at phases `24,25,...,30`.  Every physical continuation is contained in this propagation.  It proves
   \[
   G_i<0\quad(24\le i\le28).
   \]
   The earliest arithmetically admissible nonnegative defect is phase `29`, and at that phase `G_29=0` is still impossible: only strict positive crossings can occur in the necessary interface.  Their height pairs are
   \[
   (h_{29},h_{p+29})\in\{(1,0),(2,0),(2,1)\},
   \]
   with exact positive-flow quanta
   \[
   \frac{2^{43}}{3^{29}},\qquad
   \frac{2^{44}}{3^{29}},\qquad
   \frac{2^{43}}{3^{28}}.
   \]
   Surviving necessary states are **not** promoted as physical existence.

Consequently the RL177 zero-height interface is physically narrowed from 28 signed local types to at most 27, and the two zero-height `v=37` signs are reduced to the single `d=-1` sign.  Gate A, Gate B, the full `h_p=0` branch, global non-trivial-cycle exclusion, and Collatz remain open.

## 1. Frozen inherited state

Use

`A=217976794617`, `L=137528045312`,
`p=65470613321`, `u=103768467013`, `Ap-uL=1`,
`t=L-p=72057431991`.

Let

`b_i=floor(Ai/L)`, `h_i=b_i-S_i>=0`,
`q_i=2^(S_i)/3^i`, `rho_i=2^(b_i)/3^i`.

RL176/RL177 supply:

- `4|g_p`, `0<g_p<2^38`;
- the first mismatch `1<=J<=36`;
- `v2(g_p)=S_J+min(a_J,a_{p+J})<=37`;
- `G_i=0` through `i=J` and `d=G_(J+1)!=0`;
- in the zero-common-height branch, `|d|=1`, `v=b_J+1`, and 28 signed local types;
- the only zero-height `v=37` types are `J=23,d=+/-1`;
- `F2>0`, the exact corrected p-shift identity, and the mandatory positive carry at `t`;
- the local height-only automaton leaves both signs and every valuation `2..37` feasible and therefore cannot itself remove the high cases.

The external `m>=2^71` minimum is not used anywhere in RL178.

## 2. Exact signed pair relation

Before the first mismatch, the two trajectories use the same `J` accelerated maps, so

\[
y_{p+J}-y_J=\frac{3^J g_p}{2^{S_J}}.
\]

Write `a=a_J`, `b=a_(p+J)`, `r=min(a,b)`, `v=S_J+r`, and `w=g_p/2^v`, which is odd.  Then

\[
y_{p+J}-y_J=3^J 2^r w.
\]

If `d=b-a>0`, then `r=a`.  Applying the mismatched maps once gives

\[
2^{a+d}y_{p+k}-2^a y_k=3^{J+1}2^a w,
\]

hence

\[
\boxed{2^d y_{p+k}-y_k=3^k w}. \tag{2.1}
\]

If `d=-e<0`, then `r=b` and similarly

\[
\boxed{y_{p+k}-2^e y_k=3^k w}. \tag{2.2}
\]

These are exact integer relations, not merely flow magnitudes.

## 3. Second-transition valuation law

For a carry-free phase `i<t`, write `X=y_i`, `Z=y_(p+i)`, `a=a_i`, `b=a_(p+i)`, and `g=G_i`.  The next defect is

\[
g'=g+b-a. \tag{3.1}
\]

### 3.1 Current positive defect

If `g>0`, define the odd integer

\[
C=2^g Z-X.
\]

Then

\[
M_+=3C+2^g-1
    =2^g(3Z+1)-(3X+1). \tag{3.2}
\]

The two terms on the right have valuations `g+b` and `a`.  Therefore:

- if `a<g+b` (`g'>0`), then `v2(M_+)=a`;
- if `a>g+b` (`g'<0`), then `v2(M_+)=g+b`;
- if `a=g+b` (`g'=0`), then `v2(M_+)>a`.

The normalized relation after the step is obtained by dividing `M_+` by the smaller valuation in a strict-sign transition, or by the common valuation in a zero return.

### 3.2 Current negative defect

If `g=-e<0`, define the odd integer

\[
C=Z-2^e X.
\]

Then

\[
M_-=3C+1-2^e
    =(3Z+1)-2^e(3X+1). \tag{3.3}
\]

The term valuations are `b` and `e+a`.  Hence:

- if `b<e+a` (`g'<0`), then `v2(M_-)=b`;
- if `b>e+a` (`g'>0`), then `v2(M_-)=e+a`;
- if `b=e+a` (`g'=0`), then `v2(M_-)>b`.

### 3.3 Zero defect

If `g=0`, then `C=Z-X` is a positive even integer and

\[
3C=(3Z+1)-(3X+1).
\]

Unequal next exponents give valuation equal to their minimum; equal exponents require one further factor of two because the next state difference is again even.

This recursion is exact for every physical continuation.  The RL178 certificate uses it only as a **necessary** transition filter together with the mechanical height caps.  A surviving filtered state is not asserted to be realizable by a cycle.

## 4. Residue-ordered flow deficit

For each residue `r=0,...,L-1`, let `i_r` be the unique phase with

\[
A i_r\equiv r\pmod L,
\]

and set

\[
H_r=h_{i_r},\qquad \omega_r=\rho_{i_r}.
\]

Since

\[
E_i=Ai-LS_i=(Ai\bmod L)+Lh_i,
\]

we have `E_(i_r)=r+L H_r`.  For `r<L-1`, the p-shift advances residue `r` to `r+1`, so

\[
G_{i_r}=H_r-H_{r+1}. \tag{4.1}
\]

At `r=L-1`, the residue wraps to zero and the unique mechanical carry gives

\[
G_t=H_{L-1}+1,
\qquad i_{L-1}=t. \tag{4.2}
\]

Because `h_p=0`, `q_p=rho_p=e^{-s}` with inherited `s>0`, while `lambda=e^Delta` with `Delta>0`.  Moving from residue `r` to `r+1` multiplies `omega` by either `e^{-s}` or `e^{-(s+Delta)}` according to whether the chronological phase wraps.  Therefore

\[
1=\omega_0>\omega_1>\cdots>\omega_{L-1}=\rho_t. \tag{4.3}
\]

Put `x_r=2^{-H_r}` and `x_L=x_0=1`.  For `r<L-1`,

\[
q_{i_r}(2^{G_{i_r}}-1)
=\omega_r(x_{r+1}-x_r),
\]

while the final carry term is

\[
\rho_t+\omega_{L-1}(x_0-x_{L-1}).
\]

Summation by parts gives

\[
\boxed{
F_2=\rho_t-D,
\quad
D=\sum_{r=1}^{L-1}
(\omega_{r-1}-\omega_r)(1-2^{-H_r}).
} \tag{4.4}
\]

Every summand of `D` is nonnegative, and a positive-height vertex contributes strictly positively.  This is a residue-localized form of the inherited mechanical-envelope loss, not a revival of the RL175 sparse ownership resultant.

For a zero-height first mismatch at phase `k<=37`:

- if `d=+1`, the source height at residue `r=A k mod L` is `H_r=1`, and its predecessor phase is `t+k`; hence
  \[
  D\ge |T_k|(e^{s+\Delta}-1);
  \]
- if `d=-1`, the target residue has height one and phase `p+k`; hence
  \[
  D\ge |T_k|(1-e^{-s}).
  \]

These localize the compensation loss to the exact height-one interface, although the decisive `v=37,d=+1` exclusion below is purely integer and stronger.

## 5. The zero-height `v=37` pair

RL177 leaves only `J=23,d=+/-1` when `v=37,H=0`.  Since RL176 gives `0<g_p<2^38`, exact valuation `v2(g_p)=37` forces

\[
\boxed{g_p=2^{37}}. \tag{5.1}
\]

Also `b_23=36`, so at the common-prefix endpoint

\[
y_{p+23}-y_{23}
=\frac{3^{23}2^{37}}{2^{36}}
=2\cdot3^{23}. \tag{5.2}
\]

The mismatch digit is `c_23=2`, and the next mechanical digit is

\[
c_{24}=1. \tag{5.3}
\]

### 5.1 Positive sign `d=+1`: excluded

Here `(a_23,a_(p+23))=(1,2)`.  After the mismatch, the phase-24 states satisfy

\[
2y_{p+24}-y_{24}=3^{24}, \tag{5.4}
\]

and their heights are `(1,0)`.  From `c_24=1`, nonnegative next heights force

\[
a_{24}\in\{1,2\},\qquad a_{p+24}=1. \tag{5.5}
\]

Applying the valuation law to (5.4) gives

\[
2(3y_{p+24}+1)-(3y_{24}+1)=3^{25}+1. \tag{5.6}
\]

Since `25` is odd, `3^25=3 (mod 8)`, so

\[
v_2(3^{25}+1)=2. \tag{5.7}
\]

If `a_24=1`, the two terms on the left of (5.6) have unequal valuations `2` and `1`, so the difference must have valuation `1`, contradicting (5.7).  If `a_24=2`, both terms have valuation `2`, so cancellation forces valuation at least `3`, again contradicting (5.7).

Therefore:

### Theorem RL178.3

\[
\boxed{
(v,H,J,d)=(37,0,23,+1)\text{ is impossible.}
} \tag{5.8}
\]

This is a physical-type exclusion, not a global cycle exclusion.

### 5.2 Negative sign `d=-1`: forced next pair

Here `(a_23,a_(p+23))=(2,1)`, so

\[
y_{p+24}-2y_{24}=3^{24}, \tag{5.9}
\]

with heights `(0,1)`.  Thus `a_24=1` and `a_(p+24) in {1,2}`.  Now

\[
(3y_{p+24}+1)-2(3y_{24}+1)=3^{25}-1. \tag{5.10}
\]

Because `3^25=3 (mod 4)`,

\[
v_2(3^{25}-1)=1. \tag{5.11}
\]

The choice `a_(p+24)=2` would give equal valuation `2` on the two terms and therefore a difference divisible by `8`, contradicting (5.11).  Hence

\[
\boxed{a_{24}=a_{p+24}=1,\qquad G_{25}=-1.} \tag{5.12}
\]

## 6. Earliest admissible return for the surviving high type

The exact certificate propagates (3.2)-(3.3), the mechanical digits, and nonnegative heights from the state

\[
(h_{24},h_{p+24},C_{24})=(0,1,3^{24}).
\]

It deliberately does **not** impose an unproved physical-existence converse.  The resulting necessary-state counts are:

| phase | necessary states |
|---:|---:|
| 24 | 1 |
| 25 | 1 |
| 26 | 2 |
| 27 | 2 |
| 28 | 5 |
| 29 | 10 |
| 30 | 16 |

Every state through phase 28 has negative defect.  At phase 29 the first strict positive crossings enter, while zero defect is still absent.  The only positive height pairs in this exact necessary interface are

\[
(1,0),\quad(2,0),\quad(2,1). \tag{6.1}
\]

Since `b_29=45`, their first possible positive-flow terms are respectively

\[
\frac{2^{44}}{3^{29}},\qquad
\frac{2^{43}}{3^{28}},\qquad
\frac{2^{43}}{3^{29}}. \tag{6.2}
\]

Thus the high negative branch cannot immediately undo its `>1/3` first negative term; it is forced to remain negative for four further phases, and the first admissible sign reversal is itself quantized.

## 7. What is and is not proved

### Proved analytic mathematics

- Exact signed first-mismatch pair relations (2.1)-(2.2).
- Exact second-transition valuation law (Section 3).
- Exact residue-ordered deficit decomposition (4.4).
- Physical exclusion of `v=37,H=0,J=23,d=+1`.
- Forced `a_24=a_(p+24)=1` in the surviving `v=37,d=-1` type.

### Exact finite certificate

`RL178_CERTIFICATES/verify_second_transition_consumer.py` checks the high-case arithmetic, the exclusion, the forced next pair, the complete necessary transition propagation through phase 30, and the phase-29 positive quanta.

### Scope barrier

The transition propagation is one-way: every physical continuation must survive it, but a surviving necessary state is not certified to extend to a cycle.  No existence claim is made.

### Not proved

- The remaining `v=37,H=0,d=-1` type is not excluded.
- The other 26 zero-height signed types are not excluded.
- The `H>=1` first-mismatch branch, including `v=36`, is not excluded.
- The preferred `h_p=0` branch is not closed.
- Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.

## 8. Handover

RL179 should continue the exact return mechanism rather than restart the RL177 local automaton.  Its primary target is the surviving

\[
(v,H,J,d)=(37,0,23,-1)
\]

branch.  Use the forced negative window through phase 28 and the three phase-29 positive quanta to couple the early signed-flow budget to the exact value

\[
F_2=3(\lambda-1)2^{37}.
\]

If that branch survives, apply RL178.1's second-transition law across the remaining zero-height types by odd part `w=g_p/2^v`, using congruence classes rather than a larger height-only path count.  The next success criterion is exclusion of the remaining high type, a further exact sign/return restriction, or a congruence sieve that materially shrinks the 27-type physical interface.
