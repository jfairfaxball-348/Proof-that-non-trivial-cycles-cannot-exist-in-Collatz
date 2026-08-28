# RL155 — dense singleton phase remainder

RL155 gives an analytic full-modulus reformulation and a method boundary; it
does not exclude a cycle.

Put `D=2^A-3^L`.  Choose `p,m` with `Ap-mL=1` and set
`rho=2^m3^(-p)` modulo `D`.  For the physical singleton defect path,
ordinary affine ownership is exactly

`sum_(j<L) rho^(Aj-LS_j)=0 (mod D)`.

Since `S_j=floor(Aj/L)-h_j`, its exponent is

`Aj-LS_j=(Aj mod L)+Lh_j`.

Also `rho^L=1/2`.  On reducing the phase polynomial modulo `3T^L-2` and
multiplying by `3^H`, its coefficient at the residue
`r=Aj mod L` is `2^(h_j)3^(H-h_j)`.  The residues permute every class because
`gcd(A,L)=1`; hence the remainder has exactly `L` strictly positive
coefficients and no inter-phase collisions.

This retains the whole modulus and all defect levels coupled, but removes a
possible sparse-resultant/cancellation route.  A successor needs new
arithmetic of the dense positive remainder.  No factor `F_1`, individual
level congruence, small-prime sieve, or legacy one-excursion resultant is
licensed.

No correction/demotion, exclusion, Gate result, or Collatz claim is made.

