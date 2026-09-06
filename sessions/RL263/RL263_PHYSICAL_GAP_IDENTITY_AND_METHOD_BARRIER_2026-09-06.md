# RL263 — physical two-trajectory identity and ordered-prefix method barrier

Date: 2026-09-06
Classification: **ANALYTIC IDENTITY / METHOD BARRIER**

## Scope

Work in the inherited odd-terminal full-phase branch of RL64--RL65. Let

- `N>0`, with `N == 19 (mod 24)`;
- `rho=ell-3`;
- `m=a-k-1`;
- full words `u=110 x 1 0^t`, `v=111 y 0^(t+1)`;
- `k=t+3`;
- internal words `x,y` of common length `m` and common weight `rho`.

Let `F(n)=n/2` for even `n` and `F(n)=(3n+1)/2` for odd `n`.

## 1. The canonical path is a coordinate on the two physical trajectories

After the fixed prefixes `110` and `111`, define

`A_0=(9N+5)/8`,
`B_0=(27N+127)/8`,

and then

`A_(p+1)=F(A_p)`,
`B_(p+1)=F(B_p)`.

Let

`x_p=A_p mod 2`,
`y_p=B_p mod 2`,

and let `X_p,Y_p` be the numbers of ones among the first `p` bits of `x,y`. Put

`d_p=1+Y_p-X_p`.

Then the exact canonical RL state is

`boxed: T_p = 3^(d_p) A_p - B_p`.

At `p=0`, this gives `T_0=-14`. Substituting the two half-Collatz updates gives exactly

`T_(p+1)=(3^(y_p)T_p + x_p*3^(d_p+y_p-1) - y_p)/2`

(with the `x_p` term absent when `x_p=0`), which is the frozen canonical recurrence.

With `J_p=T_p+3^(d_p)-2^(d_p)`,

`boxed: J_p = 3^(d_p)(A_p+1) - (B_p+2^(d_p))`.

Modulo two this gives

`J_p odd <=> x_p=y_p`,

recovering the exact `step_x` parity rule.

## 2. Exact physical-gap factorization of the ordered defect

Define the ordered prefix defect

`S_p = sum_(i<p,x_i=1) 2^i 3^(rho-X_(i+1))
       - sum_(i<p,y_i=1) 2^i 3^(rho-Y_(i+1))`

and

`C=3^rho*(9N+61)/4`.

Then for every legal prefix,

`boxed: C-S_p = 2^p * 3^(rho-Y_p) * (B_p - 3^(d_p-1) A_p)`.

At `p=0`, the identity is immediate from

`B_0-A_0=(9N+61)/4`.

The induction step is obtained by substituting

`2A_(p+1)=3^(x_p)A_p+x_p`,
`2B_(p+1)=3^(y_p)B_p+y_p`

and the update `d_(p+1)=d_p+y_p-x_p`; the one-step correction is exactly the new `x_p` or `y_p` term in `S_(p+1)`.

Consequently, on every genuine physical full-phase pair,

`boxed: S_p == C (mod 2^p)`

is automatic. It is an exact physical-gap telescope, not an independent global density restriction.

## 3. Endpoint and carry

At `p=m`, common internal weight gives `d_m=1` and `S_m=Dcal`. The fixed terminal tails imply

`B_m = N*2^(k-2)`

and

`A_m = ((N+4)*2^(k-2)-1)/3`.

Therefore

`3A_m-B_m=2^k-1`

and

`B_m-A_m = (1+(N-2)*2^(k-1))/3`.

Hence the endpoint specialization of the prefix identity is

`boxed: Dcal = C - 2^m * (1+(N-2)*2^(k-1))/3`.

This is exactly equivalent to RL262's carry formula, but exposes an extra factor four in the carry coefficient in the odd-`k` scope.

## 4. Method-barrier conclusion

The selector-specific eliminations RL261--RL262 remain valid: they used exact finite geometry plus the full exact defect value, not merely a claimed global density theorem.

However, the selector-independent ordered dyadic congruence itself cannot force an eventual low-one-density corridor on genuine full-phase objects. Once `x,y` are the actual parity itineraries of the physical `N,N+4` pair, every prefix congruence is already an identity.

Therefore RL263 decisively falsifies the intended standalone global ordered-prefix weight-deficit route. Any successor must inject genuinely independent information: canonical low-area/height ownership, determinant/physical geometry, an eligible Radius-4 encounter with all hypotheses manufactured, or another non-tautological global constraint.

Gate A remains open. Gate B remains open. Radius 4 is not invoked here. Radius 5 remains inactive.
