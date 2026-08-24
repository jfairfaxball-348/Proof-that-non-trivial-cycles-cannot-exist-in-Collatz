# RL48 — Phase condition rewritten as a rank-displacement defect congruence

Date: 2026-08-22

## Status

**Algebraic derivation conditional on the standard one-excursion word reconstruction; historical-definition audit still required.**

The RL47->RL48 bundle contains the RL45 phase-polynomial formula and the RL47 rank identity, but not the full RL43/RL44 source bundle defining the general full word `v` for arbitrary terminal suffix `t`.  The derivation below uses the natural reconstruction consistent with the inherited t=0 phase verifier and the RL46/RL47 terminal bookkeeping:

`v = 111 · y · 0^(t+1)`,

where `y` is the internal second-coordinate word of length `m=a-(t+3)-1` and weight `r=ell-3`.

This reconstruction is exact on the inherited `(65,41)` t=0 countermodel and dimensionally/weight-wise exact on the audited `(65,41)` t=2 RL47 terminal witness.  It must still be checked line-by-line against the missing RL43/RL44 definition before this note is promoted to an unconditional inherited theorem.

## 1. Internal rank polynomials

Let the internal words `x,y` have one positions

`a_1<...<a_r`, `b_1<...<b_r`,

with

`delta_j=a_j-b_j>=0`,

`H=sum delta_j`.

Define

`Qx = sum_j 2^a_j 3^(r-j)`,

`Qy = sum_j 2^b_j 3^(r-j)`.

The displacement defect is

`D = Qx-Qy`

`  = sum_j 3^(r-j) (2^a_j-2^b_j)`

`  = sum_{delta_j>0} 3^(r-j) 2^b_j (2^delta_j-1)`.

Hence

- `D>=0`;
- the number of active rank terms is at most `H`;
- under a hypothetical strict terminal violation, `H<=t+2`, so `D` has at most `t+2` active ranks.

This is a genuine support-compression statement; it does **not** say the defect is radius 3.

## 2. RL47 terminal identity in Q-form

RL47 proved

`2^m T_m = -14*3^r + 3Qx-Qy`.

At terminal

`T_m=2^k-1`, `k=t+3`, `m=a-k-1`.

Therefore

`3Qx-Qy = 14*3^r + 2^(a-1) - 2^(a-k-1)`.

Since `Qx=Qy+D`,

`2Qy+3D = 14*3^r + 2^(a-1) - 2^(a-k-1)`.

## 3. Full phase word in terms of Qy

Under the standard reconstruction

`v=111 · y · 0^(t+1)`,

the first three fixed ones contribute

`3^(ell-1) + 2*3^(ell-2) + 4*3^(ell-3)`

`=19*3^r`,

and every internal `y` one is shifted by three positions and three ranks, contributing `8Qy`.

Thus

`Q(v)=19*3^r+8Qy`.

Using the terminal identity,

`Q(v)`

`=19*3^r + 4(14*3^r + 2^(a-1)-2^(a-k-1)-3D)`

`=75*3^r + 2^(a+1) - 2^(a-k+1) - 12D`.

## 4. Combine with the canonical same-root phase scalar

The separate RL48 same-root theorem proves

`P(rho)=0  <=>  M | Q(v)+4*3^ell`,

where `M=2^a-3^ell` and `r=ell-3`.

Since `4*3^ell=108*3^r`, the full phase condition becomes

`M | 183*3^r + 2^(a+1) - 2^(a-k+1) - 12D`.

Modulo `M`, use `2^a = 3^ell = 27*3^r`, hence `2^(a+1)=54*3^r`.  Therefore the selected-root phase condition is equivalent to

`boxed:  12D + 2^(a-k+1) = 237*3^r  (mod M)`.

Since `k=t+3`, this is

`boxed:  12D + 2^(a-t-2) = 237*3^(ell-3)  (mod 2^a-3^ell)`.

This is the current sharpest candidate bridge equation.

## 5. The explicit remaining arithmetic lemma

A proof-level Gate-B target can now be stated without global resultants:

> **Rank-defect bridge lemma (open).**  Under the genuine retained one-excursion hypotheses, with `H=sum delta_j<=t+2`, no defect
>
> `D=sum_{delta_j>0} 3^(r-j)2^b_j(2^delta_j-1)`
>
> satisfying all prefix/order constraints can obey
>
> `12D + 2^(a-t-2) = 237*3^(ell-3) (mod 2^a-3^ell)`,
>
> except possibly configurations already covered by the audited radius-3 theorem.

This is substantially narrower than the previous request for an unspecified three-polynomial subresultant.  The common root has been eliminated, the phase polynomial has been eliminated, and the remaining arithmetic object is directly parameterized by rank displacement.

## 6. What remains before a radius-3 closure claim

1. Audit `v=111 y 0^(t+1)` against the exact RL43/RL44 full-denominator definitions.
2. Reconstruct the exact radius-3 theorem and identify whether the defect congruence above matches its sparse-uniqueness hypotheses.
3. If not, prove an additional compression from total displacement `H<=t+2` to the theorem's actual radius/support notion.
4. Check prime-power/multiplicity hypotheses if the radius-3 theorem is stated locally rather than modulo the full `M`.

No RL closure is claimed in this note.
