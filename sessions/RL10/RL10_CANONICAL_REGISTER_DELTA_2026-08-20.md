# RL-10 Canonical Register Delta — 2026-08-20

| ID | Statement | Status |
|---|---|---|
| RL-L62 | Exact cyclic transposition distance 3 can be cut linearly so its prefix-flow has exactly three nonzero unit edges. The support-run lengths are exactly `[3]`, `[2,1]`, or `[1,1,1]`. Connected length-3 local `Q` coefficients are `7,13,9,19` up to sign and a `2,3` unit. | **PROVED ANALYTIC THEOREM** |
| RL-L63 | No `D`-divisible self-rotation can have connected radius-3 flow. Coefficients `7,13,19` are each eliminated analytically and `9` is a unit modulo `D`. | **PROVED ANALYTIC THEOREM** |
| RL-L64 | If `gcd(A,L)=1` and `rL+sA=1`, then `theta=2^r3^s (mod D)` satisfies `theta^L=2`, `theta^A=3`; hence `2^u3^{-v}=theta^(uL-vA)`. | **PROVED ANALYTIC THEOREM** |
| RL-L65 | With `H_i=A P_i-iL`, `4Q(d) == 3^L sum_i theta^(-H_i) (mod D)` in the coprime branch. | **PROVED ANALYTIC THEOREM** |
| RL-L66 | For `d'=tau^m d`, prefix-flow `G_i` obeys `H_(i+m)=H_i+e+A G_i`, `e=H_m`; exact radius 3 gives exactly three `+/-A` jumps and `e in {+/-1,+/-3}`. | **PROVED ANALYTIC THEOREM** |
| RL-L67 | Coprime one-orbit radius-3 branches reduce to explicit sparse three-jump congruences: mixed `e=1` gives one of `rho^a+3rho^b-3rho^c`, `rho^a-rho^b+rho^c`, `-rho^a+rho^b+3rho^c`; same-direction `e=3` gives `sigma^a+3sigma^b+9sigma^c`. | **PROVED ANALYTIC REDUCTION** |
| RL-F10 | Exact constructive scan through `A<=40` finds only `(A,L,D)=(6,3,37)` with words `101010/010101` among radius-3 `D|DeltaQ` survivors; these are `(10)^3`, nonprimitive. | **FINITE EVIDENCE** |
