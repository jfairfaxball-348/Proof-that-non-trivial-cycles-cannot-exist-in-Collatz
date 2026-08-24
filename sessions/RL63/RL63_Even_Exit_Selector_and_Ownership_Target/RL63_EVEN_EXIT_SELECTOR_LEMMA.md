# RL63 exact even-exit selector and unrestricted synchronized obstruction

Date: 2026-08-24

## Status

The statements labelled **Lemma/Theorem** below are exact analytic consequences of the frozen RL45 quotient. They are not finite-search conjectures. The supplied verifier checks the algebra on broad exact samples and verifies finite instances, but the proofs below are the basis for theorem status.

These results do **not** close Gate A. Their purpose is to identify exactly what an ownership-sensitive proof must exclude, and to prove that no theorem using only unrestricted height-one synchronized dynamics can be sufficient.

## 1. Frozen RL45 quotient

Use

\[
J=T+3^d-2^d,
\qquad
K=H+\frac{d(d+1)}2-1.
\]

The state transitions are:

- odd `J`:
  - `00`: `J'=(J+3^d-2^d)/2`, `d'=d`;
  - `11`: `J'=(3J+2^d-1)/2`, `d'=d`;
- even `J`:
  - `01`: `J'=(3J+3^(d+1)-2^d-1)/2`, `d'=d+1`;
  - `10`: `J'=J/2`, `d'=d-1` for `d>1`;
- always `H'=H+d-1`.

The Gate-A valuation candidate is `J>0 => v2(J)<=K`; at `d=1`, `K=H`.

## 2. Lemma: exact T transitions

Substitution into `T=J-3^d+2^d` gives

- `00`: `T'=T/2`;
- `11`: `T'=(3T+3^d-1)/2`;
- `01`: `T'=(3T-1)/2`;
- `10`: `T'=(T+3^(d-1))/2`.

No approximation is used.

## 3. Lemma: exact K increments and 10-margin invariance

The four edge types change `K` by

- `00` or `11`: `K'-K=d-1`;
- `01`: `K'-K=2d`;
- `10`: `K'-K=-1`.

For a legal `10` edge with nonzero even `J`, `J'=J/2`, hence

\[
v_2(J')=v_2(J)-1.
\]

Therefore

\[
\boxed{v_2(J')-K'=v_2(J)-K}
\]

on every legal `10` edge.

**Interpretation.** A `10` return neither creates nor repairs valuation excess. Any dangerous margin present after a `10` was already present immediately before it. This is an exact localization fact, but by itself it does not prove that every possible birth occurs at height one; `01` and higher-height odd edges still require the inherited full-phase/reachability analysis.

## 4. Theorem: synchronized height-one affine selector

At `d=1`, `K=H` and odd `J` has exactly the two synchronized transitions

\[
00:\quad J\mapsto\frac{J+1}{2},
\qquad
11:\quad J\mapsto\frac{3J+1}{2}.
\]

Encode a synchronized word `w=(x_0,...,x_{n-1})` with `x_r=0` for `00` and `x_r=1` for `11`. Let

\[
s=\sum_{r=0}^{n-1}x_r
\]

and

\[
C(w)=\sum_{r=0}^{n-1}2^r 3^{\sum_{q=r+1}^{n-1}x_q}.
\]

Then every legal realization from entry `J_0` satisfies the exact composition law

\[
\boxed{2^nJ_n=3^sJ_0+C(w).}
\]

### Proof

Induct on `n`. For one edge the formula is exactly `2J_1=3^{x_0}J_0+1`. Appending a final edge `x_n` gives

\[
2^{n+1}J_{n+1}=3^{x_n}(2^nJ_n)+2^n,
\]

which multiplies every previous constant term by `3^{x_n}` and adds the new `2^n` term, precisely producing `C(w)`.

### Dangerous-exit congruence

If all intermediate pre-exit states are odd and the final state is a positive even exit with

\[
v_2(J_n)>H,
\]

then necessarily

\[
\boxed{3^sJ_0+C(w)\equiv0\pmod{2^{n+H+1}}.}
\]

Because `3^s` is invertible modulo every power of two, for fixed `(w,H)` this selects a single residue class

\[
J_0\equiv-3^{-s}C(w)\pmod{2^{n+H+1}}.
\]

Legality of a **first-even** exit also imposes the prefix conditions that for every `1<=r<n`, the corresponding prefix numerator is congruent to `2^r mod 2^(r+1)`, so that `J_r` is odd.

**Proof interface.** Gate A can therefore be attacked by showing that the actual full-phase/zero-position/ownership admissible macro-entry set never meets these dangerous 2-adic cylinders.

## 5. Theorem: unrestricted all-11 blocks contain an infinite dangerous family

This is the key negative result of RL63.

Take a maximal height-one block consisting only of `11` edges. Write

\[
Q_0=J_0+1=2^nq,
\]

with `q` odd and `n=v_2(J_0+1)`. Since `11` sends `Q=J+1` to `3Q/2`, after `r` steps

\[
Q_r=2^{n-r}3^rq,
\qquad
J_r=2^{n-r}3^rq-1.
\]

Thus `J_r` is odd for `r<n`, while the first even exit is

\[
\boxed{J_n=3^nq-1.}
\]

For any prescribed `H>=0` and `n>=1`, choose odd `q` satisfying

\[
q\equiv3^{-n}\pmod{2^{H+1}}.
\]

Such a `q` always exists because `3^n` is odd. Then

\[
3^nq-1\equiv0\pmod{2^{H+1}},
\]

so

\[
\boxed{v_2(J_n)>H.}
\]

The whole synchronized block is legal in the unrestricted height-one quotient: every pre-exit `J_r` is odd.

### Consequence

There is **no possible proof of Gate A based solely on unrestricted local height-one synchronized dynamics**. The dangerous local blocks exist in an infinite exact family. A successful theorem must exclude their entry data using information lost by the local quotient: actual reachability from the global start, full-phase prefix equations, zero-position data, ownership, or an equivalent arithmetic invariant.

This also explains why neutral `11` pumping is intrinsically invisible to the synchronized scalar telescope: inherited `Psi=g(J+1)/2` is unchanged by `11`.

## 6. Exact reachable sharpness witness

The RL45 quotient path

`00 01 10 00 00 01 11 10 11 11`

from `(d,H,J)=(1,0,-13)` reaches

\[
(d,H,J)=(1,3,8).
\]

There `K=H=3` and `v2(J)=3`, so the desired inequality is sharp: equality occurs in the actual reachable quotient.

This is an exact finite witness, not a counterexample.

## 7. What RL63 does and does not establish

Established analytically:

1. the exact T-edge formulas;
2. exact K increments;
3. exact `10` invariance of `v2(J)-K`;
4. the synchronized affine composition/2-adic selector;
5. an infinite unrestricted all-`11` family producing `v2(J_exit)>H`;
6. therefore ownership/reachability information is logically indispensable.

Not established:

1. exclusion of the dangerous residue classes for genuinely full-phase reachable entries;
2. a complete classification of mixed `00/11` first-even words under ownership;
3. uniform Gate A;
4. Gate B, RL closure, or Collatz.

The next proof target should be a **macro-entry cylinder exclusion theorem**: translate the inherited full-phase ownership conditions into a restriction on `(H,J_0,w)` strong enough to rule out the dangerous congruence above.
