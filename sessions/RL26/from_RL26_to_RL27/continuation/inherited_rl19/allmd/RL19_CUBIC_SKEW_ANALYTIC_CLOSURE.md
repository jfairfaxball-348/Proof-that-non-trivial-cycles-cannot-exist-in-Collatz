# RL19 — analytic closure of the one-orbit cubic skew leaf

## Status and scope

**Claim status in this note: ANALYTIC**, conditional only on the already-audited RL10 radius-3 flow reduction and RL17 full-`D` sparse promotion.

This note closes the final exact-radius-3 arithmetic leaf

`A=3a`, `L=3ell`, `gcd(a,ell)=1`, `gcd(3a,m)=1`,

with

`a p - m ell = 1`,

`D=2^(3a)-3^(3ell)>1`, and

`rho=2^m 3^(-p) (mod D)`.

Under RL17, a same-direction one-orbit radius-3 `D`-divisible rotation gives positive cyclic jump gaps

`u+v+w=3a`

and

`1+3 rho^u+9 rho^(u+v)=0 (mod D)`.

We prove that every geometrically realizable skew triple is impossible. Equal gaps force a nonprimitive word directly from the flow geometry. Thus this branch is closed for primitive words.

No LMN theorem and no finite cutoff are used in this closure.

---

## 1. The inverse-step identity

Let `r` be the least positive inverse of `m` modulo `3a`:

`m r = 1 (mod 3a)`, `1<=r<3a`.

There is a unique `k in {1,2,3}` with

`k m = p (mod 3)`.

Because `ell<a` (from `3^ell<2^a`), the integer `ka-ell` lies in `(0,3a)`. Moreover

`m(ka-ell)=1+a(km-p)=1 (mod 3a)`.

Hence

`r=ka-ell`.                                                   (R19.1)

Write `km-p=3h`. Then

`mr=1+3ah`,

and

`3ell h-pr = -k`,

using `ap-mell=1`. Therefore modulo `D`, where `2^(3a)=3^(3ell)`,

`rho^r = 2^(mr) 3^(-pr) = 2 / 3^k`.                         (R19.2)

Thus

- `k=1`: `r=a-ell`, `3 rho^r=2`;
- `k=2`: `r=2a-ell`, `9 rho^r=2`;
- `k=3`: `r=3a-ell`, `27 rho^r=2`.

All divisions are by units modulo `D` and its cubic cofactor.

---

## 2. Exact binary interlacing lemma

Use RL10 rotation coordinates `i_t=tm (mod 3a)`. In the positive discrepancy orientation, let

`g_t=G_{i_t}`.

The same-direction radius-3 branch has exactly three values `g_t=-1`; let their set be `T`.

Put `x_t=d_{i_t}`. Since `i_{t+r}=i_t+1`, the prefix-difference identity gives

`x_(t+1)-x_t = g_(t+r)-g_t
             = 1_T(t)-1_T(t+r)`.                            (R19.3)

Thus the `+1` events occur at `T` and the `-1` events at `T-r`. A cyclic binary sequence exists iff, after cancelling coincident opposite events, the nonzero `+/-` events alternate. This is exactly weak interlacing of `T` and `T-r`.

Let the positive cyclic gaps of `T` be `u,v,w`, with sum `A=3a`. Direct inspection of the three arcs gives the following exact criterion:

`r<=min(u,v,w)`, or

`A-r<=min(u,v,w)`, or

`max(u,v,w)<=min(r,A-r)`.                                   (R19.4)

Here is an explicit proof, including boundary coincidences. Binary realizability is unchanged by replacing `r` with `A-r`: the increment sequence for `A-r` is a cyclic shift of the negative of the increment sequence for `r`, so complementing the binary sequence restores a solution. Thus assume `r<=A/2`.

Write the jump points as `P_0,P_1,P_2` in cyclic order, with gaps `g_i=P_(i+1)-P_i` (indices modulo 3). The translated negative points are `N_j=P_j-r`. Weak alternation is equivalent to saying that each arc from `P_i` to `P_(i+1)` contains exactly one `N_j`, with an endpoint coincidence interpreted as cancellation. Because translation preserves cyclic order, the index of that negative point must have the form `j=i+c (mod 3)` for one fixed `c`.

- If `c=1`, then `N_(i+1)=P_(i+1)-r` lies in the `i`-th arc exactly when `r<=g_i`. Hence this order occurs iff all three gaps are at least `r`.
- If `c=2`, then `N_(i+2)` lies in the `i`-th arc exactly when `g_(i+1)<=r<=g_i+g_(i+1)`. For all three `i`, the lower inequalities say that all gaps are at most `r`; the upper inequalities are then automatic because `r<=A/2` and `g_j<=r<=A-r`.
- If `c=0`, one would need `A-r<=g_i` for all three gaps, forcing `3(A-r)<=A`, impossible when `r<=A/2`.

Thus for `r<=A/2` the only possibilities are `r<=min(u,v,w)` or `max(u,v,w)<=r`. Restoring `r` versus `A-r` gives exactly (R19.4). The weak inequalities already include coincident translated/jump events.

Substitute `r=ka-ell`.

### `k=1`

Only the first alternative in (R19.4) is possible, hence

`min(u,v,w) >= a-ell`.                                      (R19.5)

### `k=2`

Only the third alternative is possible, hence

`max(u,v,w) <= min(2a-ell,a+ell)
             = a+min(ell,a-ell) < 2a`.                      (R19.6)

### `k=3`

Only the second alternative is possible, hence

`min(u,v,w) >= ell`.                                        (R19.7)

This is the exact rotation-gap geometry used below.

---

## 3. Eisenstein setup

Put

`X=2^a`, `Y=3^ell`, `C=X^2+XY+Y^2`,

and let `zeta` satisfy `zeta^2+zeta+1=0`. In `Z[zeta]` put

`pi=X-Y zeta`,

so `N(pi)=C`. Since `gcd(Y,C)=1`, the map

`Z[zeta] -> Z/CZ`, `zeta |-> X Y^(-1)`

is surjective and kills `pi`. Both its kernel and the principal ideal `(pi)` have index `C`, so the kernel is exactly `(pi)`. Thus the modular cubic phase calculation modulo `C` is equivalently divisibility by `pi` in `Z[zeta]`, and modulo `(pi)` one has `X/Y=zeta`.

Cyclic relabeling of the gaps preserves sparse vanishing: if

`P(u,v,w)=1+3rho^u+9rho^(u+v)=0`,

then, because `27rho^(3a)=1`, multiplying by `3rho^w` gives

`P(w,u,v)=0`.

Thus any cyclic choice of the starting jump is legitimate. The RL18 centered reduction writes

`d=u-a`, `t=a-w`

and turns the sparse zero modulo `C` into

`1 + zeta^m rho^d + zeta^(2m) rho^t = 0 (mod pi)`.          (R19.8)

We first isolate a boundary that the initial centered-size argument must not silently absorb.

---

## 4. One-gap-`a` boundary: a short-order obstruction

Modulo `C`, the Bezout relation gives the exact identity

`2 = zeta^p rho^(-ell)`.                                      (R19.9)

Suppose `rho^h=1 (mod C)` for some `0<|h|<a`. Replacing `h` by `|h|`,

`2^h = zeta^(ph) (mod C)`.

If `3|ph`, then `C | (2^h-1)`, impossible because

`0<2^h-1<X<C`.

If `3` does not divide `ph`, then `2^h` is a primitive cubic phase modulo `C`, so

`C | (2^(2h)+2^h+1)`.

But for `h<=a-1`,

`0<2^(2h)+2^h+1 < X^2 < C`,

again impossible. Therefore

`rho^h != 1 (mod C)` for `0<|h|<a`.                          (R19.10)

Now suppose a skew gap triple has one gap exactly `a`. Cyclically relabel so `w=a`. Then the centered equation (R19.8) has `t=0`, hence

`0 = 1+zeta^m rho^d+zeta^(2m)
    = zeta^m(rho^d-1)`,

where `d=u-a` is nonzero and `|d|<a`. This contradicts (R19.10).

Thus every skew triple with a gap equal to `a` is impossible.

---

## 5. Interior skew lemma: `max(u,v,w)<2a` and no gap equals `a`

A skew positive triple summing to `3a`, with no gap equal to `a`, has at least one gap above `a` and at least one below `a`. Around the cyclic gap list there is therefore a transition from a gap below `a` to one above `a`; cyclically relabel so the latter is `u` and the former is its predecessor `w`. Then

`a<u<2a`, `w<a`.

Then

`d=u-a`, `t=a-w`

satisfy

`0<d,t<a`.                                                   (R19.11)

For either `n=d` or `n=t`, define

`h=floor(nm/a)`,

`J=nm-ah`,

`I=np-ell h`.

Because `gcd(a,m)=1` and `0<n<a`,

`1<=J<=a-1`.

The determinant relation gives

`aI-ell J=n`.                                                (R19.12)

Thus `I>=1`; also `I<=ell`, since `I>=ell+1` would imply

`n=aI-ell J >= a(ell+1)-ell(a-1)=a+ell>a`.

In the quotient by `(pi)`,

`rho^n = zeta^h 2^J/3^I
       = zeta^(h+1) 3^(ell-I)/2^(a-J)`.                     (R19.13)

Furthermore (R19.12) gives

`(ell-I)/(a-J) < ell/a < log(2)/log(3)`,

hence

`0 < 3^(ell-I)/2^(a-J) < 1`.                                (R19.14)

Use (R19.13) for `d,t` in (R19.8), and multiply by a common power `2^S`, where

`S=max(a-J_d,a-J_t)<=a-1`.

We obtain an Eisenstein integer

`Z=M0 zeta^e0 + M1 zeta^e1 + M2 zeta^e2`,                  (R19.15)

with positive integer coefficients satisfying

`M0=2^S <= X/2`,

`0<M1<M0`, `0<M2<M0`,                                      (R19.16)

and `pi|Z`.

### Eisenstein size lemma

If the three phases in (R19.15) are not all equal, combine equal directions if necessary. There are either three distinct cube-root directions, or two directions with positive coefficients `A,B`. In the three-direction case

`N(Z)=1/2[(M0-M1)^2+(M1-M2)^2+(M2-M0)^2] < M0^2 < X^2`.

In the two-direction case

`N(Z)=A^2-AB+B^2 <= max(A,B)^2 < X^2`.

The first inequality is strict unless `A=B`; equality is harmless. Each combined coefficient is strictly below `2M0<=X`, so `max(A,B)<X`.

If all phases are equal, `Z=zeta^e N` with

`0<N=M0+M1+M2<3X/2<X^2`.

If `pi|N` for a rational integer `N`, write

`N=(X-Yzeta)(s+tzeta)`.

The `zeta` coefficient gives `(X+Y)t=Ys`. Since `gcd(Y,X+Y)=1`, this forces

`s=(X+Y)c`, `t=Yc`,

and therefore `N=Cc`. Thus `C|N`, impossible because `0<N<C`.

In the non-collinear cases, `pi|Z` implies `C=N(pi)` divides the positive integer `N(Z)`, while

`0<N(Z)<X^2<C`,

again impossible. The integer `Z` itself cannot vanish: cancellation of three distinct cube-root directions with positive coefficients requires all three coefficients equal, contrary to (R19.16); two directions cannot cancel with positive coefficients.

Therefore no skew sparse zero with `max(u,v,w)<2a` is geometrically realizable.                    (R19.17)

---

## 6. Extreme gaps: only `k=1` and `k=3`

The `k=2` geometry (R19.6) already has `max(u,v,w)<2a`, so it is closed by Sections 4--5.

Assume now `max(u,v,w)>=2a`. Cyclically relabel so the large gap is `w`; cyclic relabeling preserves sparse vanishing because `27 rho^(3a)=1`.

### 6.1 `k=1`

Put

`r=a-ell`.

By (R19.5), write

`u=r+x`, `v=r+y`, `x,y>=0`.

Since `w>=2a`,

`n=x+y <= a-2r = 2ell-a = ell-r`.                           (R19.18)

From `3rho^r=2`, the sparse zero becomes

`1+2rho^x+4rho^n=0 (mod C)`.                                (R19.19)

Thus `rho` is a common root modulo `C` of

`f(z)=3z^r-2`,

`g(z)=1+2z^x+4z^n`.

The standard resultant Bezout identity writes `Res(f,g)` as an integer-polynomial combination of `f` and `g`. Evaluating at the common residue `rho (mod C)` therefore gives

`C | R=Res(f,g)`.                                            (R19.20)

If `n>0`, `R` is nonzero: at any characteristic-zero root `alpha` of `f`, normalized 2-adic valuations of the three terms of `g(alpha)` are

`0`, `1+x/r`, `2+n/r`,

so the constant term has the unique minimum valuation.

Also every complex root of `f` has absolute value `(2/3)^(1/r)<1`. Therefore

`0<|R| < 3^n 7^r`.

Using (R19.18), `ell=a-r`, and `r>0`,

`3^n 7^r <= 3^(ell-r) 7^r
          = 3^a (7/9)^r
          < 4^a=X^2<C`.                                     (R19.21)

This contradicts (R19.20).

If `n=0`, (R19.19) is simply `7=0 (mod C)`, impossible since `C>X^2>=16` in this sector.

Thus the extreme `k=1` sector is impossible.

### 6.2 `k=3`

Here (R19.7) gives `min(u,v,w)>=ell`. Since `r=3a-ell` and `rho^r=2/27`, the relation `27rho^(3a)=1` yields

`rho^ell=1/2`.                                               (R19.22)

Write

`u=ell+x`, `v=ell+y`, `x,y>=0`,

and put `n=x+y`. Since `w>=2a`,

`n<=a-2ell`.                                                 (R19.23)

The sparse zero becomes

`4+6rho^x+9rho^n=0 (mod C)`.                                (R19.24)

By the same resultant Bezout identity, `C` divides

`R=Res(2z^ell-1, 4+6z^x+9z^n)`.                             (R19.25)

For `n>0`, this resultant is nonzero: at a root of `2z^ell-1`, the normalized 3-adic valuations of the three summands are `0,1,2`, so the constant term has unique minimum.

Let `s=2^(-1/ell)`. The roots are `alpha_j=s xi_j`, where `xi_j` runs through the `ell`-th roots of unity. By geometric-mean <= root-mean-square,

`prod_j |4+6alpha_j^x+9alpha_j^n| < 16^ell`.                (R19.26)

For completeness, the mean square is

`M = 16 + 36 s^(2x) + 81 s^(2n)
     + 48 s^x 1_(ell|x)
     + 72 s^n 1_(ell|n)
     + 108 s^(x+n) 1_(ell|(n-x))`.

This is just root-of-unity orthogonality. The collision cases are explicit:

- if `0,x,n` are distinct modulo `ell`, then `M<16+36+81=133`;
- if `x=n (mod ell)` and that class is nonzero, then `x>0` and `M<16+15^2=241`;
- if `x=0 (mod ell)` but `n` is in a different class, then either `x=0`, giving `M<10^2+9^2=181`, or `x>=ell`, giving `s^x<=1/2` and `M<7^2+9^2=130`;
- if `n=0 (mod ell)` but `x` is in a different class, then `n>=ell`, so `M<(4+9/2)^2+6^2<109`;
- if all three exponents are congruent modulo `ell`, then `n>0` gives `s^n<=1/2`; if `x=0`, `M<14.5^2<211`, while if `x>0` also `s^x<=1/2`, giving `M<11.5^2<133`.

Thus always `M<241<256` when `n>0`, proving (R19.26) by geometric-mean <= root-mean-square.

Consequently

`0<|R| < 2^n 16^ell
       <=2^(a+2ell)`.                                       (R19.27)

For `n>0`, (R19.23) implies `2ell<a`, so

`|R|<2^(2a)=X^2<C`,

contradicting (R19.25).

If `n=0`, (R19.24) is the constant `19=0 (mod C)`, again impossible.

Thus the extreme `k=3` sector is impossible.

---

## 7. Equal gaps imply nonprimitivity

The only remaining geometrically realizable sparse zero is therefore

`u=v=w=a`.

But then the jump indicator `g_t=-1_T(t)` is `a`-periodic. Equation (R19.3) shows that the bit increment sequence `x_(t+1)-x_t` is also `a`-periodic. Its sum over one `a`-block is zero because it is a difference of two translates of the same `a`-periodic indicator. Hence

`x_(t+a)=x_t` for every `t`.

Since `x_t=d_(tm)` and `gcd(m,3a)=1`, this gives a nontrivial rotational period of the original word. Therefore the word is not primitive.

So the one-orbit cubic branch has no primitive `D`-divisible radius-3 survivor.

---

## 8. Conclusion

Subject to the inherited, already-audited RL10/RL17 hypotheses,

**the final exact-radius-3 leaf `gcd(A,L)=3`, `gcd(A,m)=1` is CLOSED ANALYTICALLY.**

Evidence label for the new closure: **ANALYTIC**.

The old `a<=80` scan remains **COMPUTATIONAL EVIDENCE** only and is not used.

This does **not** imply RL. A separate arbitrary-radius/global bridge is still required.
