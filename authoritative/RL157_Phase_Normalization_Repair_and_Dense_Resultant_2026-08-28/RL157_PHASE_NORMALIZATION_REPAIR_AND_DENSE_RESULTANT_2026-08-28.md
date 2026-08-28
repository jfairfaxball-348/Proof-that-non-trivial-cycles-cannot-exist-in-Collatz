# RL157 — phase-normalization repair and dense resultant

**Correction/demotion plus analytic reformulation.** RL157 repairs a normalization error in RL155/RL156. It does not exclude the physical singleton owner.

With `Ap-uL=1` and `rho=2^u3^(-p)` modulo `D=2^A-3^L`, the exact relation is `rho^L=1/2 (mod D)`. Therefore RL155/RL156's reduction modulo `3T^L-2` and coefficient `2^h_j3^(H-h_j)` are invalid for that phase variable and are demoted here. The phase/numerator equivalence remains valid.

Put `r_j=Aj mod L`, `H=max_j h_j`, and `R_h(T)=sum_(j<L) T^(r_j+Lh_j)`. Ownership is equivalent to `R_h(rho)=0 (mod D)`. Correct reduction using `2T^L-1=0`, followed by multiplication by the unit `2^H`, is `P_h(T)=sum_(j<L) 2^(H-h_j)T^r_j`, with `P_h(rho)=0 (mod D)`.

As `gcd(A,L)=1`, every degree below `L` receives exactly one positive coefficient. For a nonzero nonnegative excursion some coefficient is one, where `h_j=H`, so `P_h` is primitive.

Finally `2T^L-1` is irreducible over `Q`, since its reciprocal is, up to sign, the Eisenstein polynomial `T^L-2`. Thus the nonzero polynomial `P_h` of degree below `L` is coprime to it and `D | Res(2T^L-1,P_h) != 0`.

This is an exact necessary full-modulus resultant target, not a size or factor exclusion. No sparse cancellation, individual-level ownership, `F_1`, small-prime sieve, or legacy `g=2` resultant route is used.
