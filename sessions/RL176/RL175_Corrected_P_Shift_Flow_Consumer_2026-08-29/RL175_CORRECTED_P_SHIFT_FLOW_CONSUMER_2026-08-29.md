# RL175 — corrected p-shift flow consumer and half-barrier

Date: 2026-08-29

## Outcome and classification

RL175 consumes the corrected RL174 accelerated physical p-shift functional in the coprime `g=1` first-survivor least-root branch.

New promoted results:

1. **RL175.1 — exact endpoint/arc-mass decomposition** (analytic, ordinary `+1`): if `Q=sum_(j<L) q_j` and `Q0=sum_(j<p) q_j`, then `F2=(q_p^(-1)-1)Q + ((lambda-1)/q_p)Q0`.
2. **RL175.2 — height-zero second-minimum/arc consequence** (analytic): if `h_p=0`, then `E_p=1`, so `y_p` is the unique second-smallest physical state.
3. **RL175.3 — sparse-support closure exclusion** (analytic + exact size certificate): in the physical `h_p=0` branch, the height profile cannot be identically zero and cannot have exactly one positive phase. Hence it has at least two positive phases.
4. **RL175.4 — mechanical-mass loss theorem** (analytic): those two positive phases force `R-Q>5/8`, where `R=sum rho_j` is the full mechanical mass.
5. **RL175.5 — internal half-barrier** (analytic + exact constants): `F2 < 1/2 - Delta/16`, and the verifier certifies the explicit weaker display `F2 < 1/2 - 1/17,856,000,000,000`.
6. **RL175.6 — positive-height conditional flow floor** (analytic + inherited external minimum): if `H=h_p>=1` and `m>=2^71`, then `F2 > 6,365,000,000 (2^H-1)`.

No non-trivial cycle is excluded. Gate A, Gate B, global non-trivial-cycle exclusion, and Collatz remain open.

## 1. Scope and notation

Retain the first coprime survivor `A=217,976,794,617`, `L=137,528,045,312`, with a hypothetical ordinary accelerated cycle rooted at its least odd state `m=y_0`: `3y_j+1=2^(a_j)y_(j+1)`, `a_j>=1`.

Put `S_j=sum_(i<j)a_i`, `q_j=2^(S_j)/3^j`, `lambda=2^A/3^L`, `Delta=A log 2-L log 3`.

Let `p=A^(-1) mod L=65,470,613,321`, `u=(Ap-1)/L=103,768,467,013`, `t=L-p=72,057,431,991`.

The defect profile is `h_j=floor(Aj/L)-S_j>=0`. Write `b_j=floor(Aj/L)`, `rho_j=2^(b_j)/3^j`, so `q_j=rho_j 2^(-h_j)`.

RL174 supplies the corrected physical functional `F2=sum_i q_i(2^(G_i)-1)=3(lambda-1)(y_p-y_0)`. The RL173 `3^(-G)` functional remains demoted to an auxiliary quantity.

## 2. RL175.1 — exact endpoint/arc-mass decomposition

Let `Q=sum_(j=0)^(L-1) q_j`, `Q0=sum_(j=0)^(p-1) q_j`. The chronological affine increment `z_(j+1)-z_j=q_j/3`, with `z_j=q_jy_j`, gives `q_p y_p = m + Q0/3`. Also the full closure identity gives `Q=3(lambda-1)m`.

Therefore `y_p-y_0 = m(q_p^(-1)-1)+Q0/(3q_p)` and hence

### Theorem RL175.1

`F2=(q_p^(-1)-1)Q + ((lambda-1)/q_p)Q0`. (2.1)

This is a decomposition of the corrected physical `F2` into the endpoint multiplier and the actual chronological `0 -> p` arc mass.

## 3. The `h_p=0` branch

Assume `h_p=0`. Since `Ap-uL=1`, `E_p=Ap-LS_p=1`. RL168's lifted-defect/state-order theorem therefore makes `y_p` the unique second-smallest physical state.

Also `q_p=rho_p=2^u/3^p`. Put `s=-log(q_p)=p log 3-u log 2`. The inherited below-neighbour strip is `5Delta < s < 6Delta`. (3.1)

### 3.1 Mechanical envelope

For the all-zero mechanical profile, the p-shift carry occurs only at `t=L-p`. Thus the corresponding mechanical p-shift flow is exactly `F_mech=rho_t`. Equivalently, `rho_t=lambda/(2q_p)=exp(Delta+s)/2`. (3.2)

Since every `h_j>=0`, `Q<=R:=sum rho_j`, `Q0<=R0:=sum_(j<p)rho_j`. Writing `a=q_p^(-1)-1>0`, `b=(lambda-1)/q_p>0`, equation (2.1) gives `F2=aQ+bQ0 <= aR+bR0 = rho_t`. (3.3)

The all-zero profile would be the envelope, but it is not physically admissible.

## 4. RL175.3 — zero- and one-support closure exclusion

### 4.1 Zero support

If `h_j=0` for every phase, RL157's corrected dense ownership polynomial is `P(T)=1+T+...+T^(L-1)`. At the distinguished root `rho`, `2rho^L=1`, so `2(rho-1)P(rho)=-1 (mod D)`, `D=2^A-3^L`. Hence `P(rho)` is a unit modulo the odd integer `D` and cannot vanish. The all-zero profile is impossible.

### 4.2 Exactly one positive phase

Suppose exactly one phase `k` is positive. Because `h_(j+1)-h_j=(b_(j+1)-b_j)-a_j <=1` and all neighbouring heights are zero, necessarily `h_k=1`.

Let `r=Ak mod L`. A positive component can start only when the preceding mechanical digit is `2`; therefore `0<=r<M:=A-L`. (4.1)

The corrected dense polynomial is `P(T)=2(1+T+...+T^(L-1))-T^r`. Using `2T^L-1=0`, the equation `P(T)=0` implies `K_r(T):=1-T^r+T^(r+1)=0`. (4.2)

The distinguished root also satisfies the independent companion binomial `B2(T)=3T^M-2=0 (mod D)`. Therefore physical ownership would force `D | Res(B2,K_r)`. (4.3)

The decisive extra input is a strict absolute size bound on this sparse resultant. Normalize `B2` to `T^M-2/3`. Multiplication by `K_r` in the basis `1,T,...,T^(M-1)` has every row of Euclidean norm strictly below `2` after reducing `T^M=2/3`; Hadamard therefore gives `|Res(T^M-2/3,K_r)| < 2^M`.

Restoring the leading coefficient of `B2` gives, since `r+1<=M`, `0 < |Res(B2,K_r)| < 3^(r+1)2^M <= 6^M`. (4.4) The exact logarithm certificate proves `6^M < D`. Thus (4.3) is impossible.

Consequently every physical `h_p=0` profile has at least two positive phases.

## 5. RL175.4 — at least `5/8` mechanical mass is lost

A start `k` of a positive height component has `h_(k-1)=0`, `h_k=1`, and forces the preceding mechanical digit to be `2`. Hence its mechanical residue satisfies `r_k<M`, which gives `rho_k>2/3`. (5.1)

Take the first two positive phases. If they begin different components, both are component starts, so their mechanical weights sum to more than `4/3`.

If they are the first two phases `k,k+1` of one component, then when the mechanical digit at `k` is `1`, `rho_(k+1)=(2/3)rho_k` and the digit condition gives `rho_k>3/4`, hence their sum is greater than `5/4`; when that digit is `2`, `rho_(k+1)=(4/3)rho_k` and `rho_k>2/3`, hence the sum is greater than `14/9`.

Thus two positive phases have total mechanical weight exceeding `5/4`. Since each positive height loses at least half its mechanical weight,

### Theorem RL175.4

`R-Q=sum_j rho_j(1-2^(-h_j)) > 5/8`. (5.2)

## 6. RL175.5 — strict internal half-barrier

From (3.3) and (5.2), `F2 < rho_t-(5/8)(q_p^(-1)-1)`. (6.1)

Use `s=-log q_p`, `x=Delta+s`. Then `5Delta<s<6Delta`, `rho_t=e^x/2`, and `q_p^(-1)-1=e^s-1`.

For `x<1/2`, `e^x-1 < x+2x^2`, while `e^s-1>s`. Therefore `F2 < 1/2 + x/2 + x^2 - 5s/8 = 1/2 + Delta/2 - s/8 + x^2 < 1/2 - Delta/8 + x^2`.

The inherited `5theta<1` implies `Delta<1/784`; together with `x<7Delta` this gives `x^2<Delta/16`. Hence

### Theorem RL175.5

`F2 < 1/2 - Delta/16`. (6.2)

The exact verifier also records the explicit weaker numerical form `F2 < 1/2 - 1/17,856,000,000,000`. (6.3)

This is internal to the `g=1` physical first-survivor branch and does not use the external `m>=2^71` input.

## 7. RL175.6 — conditional `h_p>=1` flow floor

Let `H=h_p>=1`. Then `q_p=rho_p 2^(-H)<2^(-H)`, because the below-neighbour mechanical endpoint has `rho_p<1`. The physical prefix squeeze gives `q_p y_p>m`, so `y_p>2^H m` and therefore `y_p-y_0>(2^H-1)m`.

Hence `F2>3m(lambda-1)(2^H-1)`. Conditional on the inherited external least-state floor `m>=2^71`, and using `lambda-1>Delta`, the exact interval verifier certifies

### Theorem RL175.6

`F2 > 6,365,000,000 (2^H-1)`. (7.1)

This result is explicitly conditional on the inherited external computation.

## 8. Red teams and method barriers

- **RL173 coordinate repair:** PASS. Only the corrected `2^G` physical functional is used.
- **Ordinary increment:** PASS.
- **Physical/quotient:** PASS.
- **Same-root elimination:** PASS WITH SCOPE. RL159 showed same-root Sylvester/SNF stacking alone is tautological; Section 4 adds the independent strict size estimate `|R|<D`.
- **Fixed-radius / unordered valuation:** PASS.
- **External provenance:** PASS. Only RL175.6 uses `m>=2^71`.
- **No false closure:** PASS. No global cycle exclusion is claimed.

## 9. Strategic barrier and next target

The direct `h_p=0` mechanical-envelope route has crossed `1/2`, but further material improvement requires information not supplied by merely counting more height support. The live physical quantity is the integer gap `g_p=y_p-y_0 >=2` with `F2=3(lambda-1)g_p`.

RL176 should seek an independent congruence, divisibility, parity, or multi-support relation on `g_p` that couples the `p` endpoint to the corrected dense ownership/chronological structure without collapsing to a same-root tautology. In parallel, retain the large conditional `h_p>=1` flow floor as a separate externally qualified branch.

Global status remains open.
