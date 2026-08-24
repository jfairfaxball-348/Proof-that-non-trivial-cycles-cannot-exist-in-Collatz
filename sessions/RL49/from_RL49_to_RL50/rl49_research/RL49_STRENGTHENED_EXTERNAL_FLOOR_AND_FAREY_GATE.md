# RL49 — strengthened external floor and Farey extension of the phase gate

Date: 2026-08-22

## Status

**Conditional analytic consequence + exact arithmetic verifier.**

The Collatz prefix extension used here is external: Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3), 471–480 (2025), Proposition 3.2 and Remark 3.1. The paper combines the verified prefix through `2^71` with recursively sufficient sets to extend the certified prefix to

\[
R_{\rm ext}=4\cdot 3^{44}+2
=3,939,083,608,734,444,931,526
\approx 1.6682667993\,2^{71}.
\]

This note does **not** claim a proof of Collatz or of RL. It records the exact consequence of accepting that published external theorem together with the already-derived RL49 phase inequality.

## 1. Input from RL49

Under a hypothetical full phase, put

\[
\zeta=\frac{2^a}{3^\ell}>1.
\]

RL49 proved

\[
N(\zeta-1)<C,\qquad C=\frac{398}{45},
\]

where `N` is an odd state in the hypothetical nontrivial cycle. Therefore every certified Collatz prefix lower bound `R` gives

\[
0<\zeta-1<\frac{C}{R}.
\]

With Ansari's extended prefix this becomes

\[
\boxed{
0<\zeta-1<\frac{398}{45R_{\rm ext}}
=\frac{199}{88629381196525010959335}
\approx2.24530508183\times10^{-21}.
}
\]

Since

\[
\lambda:=a\log2-\ell\log3=\log\zeta<\zeta-1,
\]

every full-phase pair must satisfy the same upper bound for the positive linear form `lambda`.

## 2. Stronger Legendre gate

Writing `beta=log_2 3`,

\[
0<\frac a\ell-\beta
=\frac{\lambda}{\ell\log2}
<\frac{C}{R_{\rm ext}\,\ell\log2}.
\]

Whenever

\[
\ell<\frac{R_{\rm ext}\log2}{2C},
\]

this is strictly below `1/(2 ell^2)`, so Legendre's theorem forces `a/ell` to be a continued-fraction convergent of `beta`.

Using a rigorous rational atanh-series enclosure for `log 2` and `log 3`, the companion verifier obtains the integer gate

\[
\boxed{
Q_{\rm Leg}=154,354,788,168,703,375,435.
}
\]

Every above-`beta` convergent with denominator at most this gate is excluded by the strengthened phase inequality. In particular, the old RL49 survivor

\[
\frac{123139092617126647266}{77692117359936589403}
\]

is now excluded: its rigorously lower-bounded positive linear form already exceeds `C/R_ext`.

Thus there are **zero** full-phase candidates with `ell <= Q_Leg`.

## 3. Elementary Farey extension beyond the Legendre gate

The two consecutive convergents around `beta` are

\[
U=\frac{p_{41}}{q_{41}}
=\frac{123139092617126647266}{77692117359936589403}>\beta,
\]

and

\[
L=\frac{p_{42}}{q_{42}}
=\frac{202780263237295321099}{127940101513462006853}<\beta.
\]

They are Farey neighbours:

\[
|p_{41}q_{42}-p_{42}q_{41}|=1.
\]

Their mediant is exactly the next convergent,

\[
\frac{p_{43}}{q_{43}}
=\frac{p_{41}+p_{42}}{q_{41}+q_{42}}
=\frac{325919355854421968365}{205632218873398596256}>\beta.
\]

Now suppose a reduced rational `p/q` with

\[
Q_{\rm Leg}<q<q_{43}
\]

satisfied the full-phase bound.

Because `q>Q_Leg>q_41`, if `p/q >= U`, then

\[
p-q\beta
=q\left(\frac pq-\beta\right)
\ge q(U-\beta)
>q_{41}(U-\beta)
=p_{41}-q_{41}\beta.
\]

After multiplication by `log 2`, its positive linear form is therefore larger than the already-excluded `c_41` linear form. So this case cannot satisfy the phase bound.

The only remaining possibility is

\[
\beta<\frac pq<U.
\]

But then `p/q` lies strictly between the Farey neighbours `L` and `U`. Any reduced fraction strictly between Farey neighbours has denominator at least the sum of their denominators:

\[
q\ge q_{41}+q_{42}=q_{43},
\]

contrary to `q<q_43`.

Hence the Legendre exclusion extends without any further approximation theorem all the way to the next upper convergent:

\[
\boxed{
\ell\ge205,632,218,873,398,596,256.
}
\]

The first phase-spine point not excluded by this argument is therefore

\[
\boxed{
(a,\ell,q)=
(325919355854421968365,
205632218873398596256,
120287136981023372109).
}
\]

Its positive linear form is about `8.90e-23`, so the present phase bound genuinely does not eliminate it. The argument must not be advertised as a global phase closure.

## 4. Significance

This strengthens the phase branch in two ways.

1. The formerly unique sub-gate exceptional convergent is gone once the published recursive-sufficiency extension is admitted.
2. A simple Farey-neighbour argument pushes the rigorous denominator floor about one-third beyond the conservative Legendre gate, to the next live upper convergent.

This does **not** replace the internal one-excursion/area theorem. The most promising remaining task is to combine the huge phase denominator floor and the exact height-one telescoping invariant with the prefix-cap geometry, rather than to continue a naked continued-fraction search.

## 5. Reproducibility

Run:

```bash
python phase_squeeze/verify_rl49_ansari_floor_and_farey_extension.py
```

Expected final lines include:

- `RL49 strengthened phase/Farey verifier: PASS`
- `no surviving above-beta convergent at q <= Q_LEG`
- `new denominator floor ell >= 205632218873398596256`
