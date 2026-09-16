# RL334 parent-bridge zero-run and q=22 provenance

The promoted theorem package is reproduced by the portable scripts in `verification/`.

Load-bearing facts:

- exact constants: `a=217976794617`, `ell=137528045312`, least-state floor `2^71`, state upper bound `2^76+2^36`, fixed high-carry threshold `20390252058`;
- zero-run certificate: 37 mechanical gaps, 38 factors, 1,825,797 ownership-compatible candidates, maximum deterministic escape 213 odd steps;
- lower bootstrap: `32546313238`, carry cap `32546313237`, total-44 rows 13,559, large rows 7,189;
- refined graph: N=37, L=141, T=31, P=176, total states=385, edges=15,835;
- density-potential range 0..31;
- q=22 charge-potential range 0..44;
- theorem `22(K-2H)-S<=44`;
- rho=60 optimum/gain `58,816,735`;
- exact finite consumer through rho=2894; uniform bridge from 2895; ordinary-consumer certified below bootstrap at rho=22,000,000.

The fixed-point omitted-mass certificate `verification/RL334_OMIT_RHO22000000_Q256.txt` stores the integer lower numerator at denominator `2^256` used by the consumer verifier.

Historical finite-run diagnostics are frozen under `scratch/` only. They are not load-bearing for the promoted theorem.
