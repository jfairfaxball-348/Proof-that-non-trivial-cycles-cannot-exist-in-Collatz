# RL267 certified facts

Date: 2026-09-06

Classification: **RADIUS5_KAPPA1_311_221_CLOSED**.

Promoted:
- exact determinant window identity `W_i(m)=q-g_{i-1}` under `qA-mL=1`;
- exact three-component support cut `U=floor((2A+2)/3)`;
- normalized five-edge bound `0<|E|<=5*3^(7+h)*2^(U-h)`, `h=min(m,A-m,U)`, preserving full `D|E`;
- non-bracketing exclusion for `A>=609`;
- exact reuse of the audited RL238 LMN dependency, giving bracketing cutoff `A<=261279`;
- exact 35-row Stern-Brocot upper-neighbour certificate, with only six coarse size survivors `(A,L;m,q)=(5,3;3,2),(8,5;3,2),(27,17;19,12),(46,29;19,12),(65,41;19,12),(149,94;84,53)`;
- exact complete size cover: 2,683 determinant pairs, of which 2,673 have `A>=8`; maximum pair `A=335`;
- `[3,1,1]` certificate: 26,792,286 gap configurations, 2,591,355 structural candidates, maximum structural `A=323`, zero full-`D` hits;
- `[2,2,1]` certificate over both cyclic orders: 53,584,572 gap configurations, 5,061,132 structural candidates, maximum structural `A=323`, zero full-`D` hits;
- independent complete-certificate reconstructions agree for both leaves;
- independent brute-force `A<=18` red team: `[3,1,1]` 5,144 raw `|kappa|=1` instances and `[2,2,1]` 10,292, with zero full-`D` hits;
- permanent negative-domain sentinel remains `D=-139,Q=18904` and is outside scope.

Together with RL266, determinant-one leaves `[3,2]`, `[3,1,1]`, `[2,2,1]` are closed.

Still open: `[2,1,1,1]`, `[1,1,1,1,1]`; then only after determinant one is complete may `|kappa|=3` or `5` be activated.

Radius 5, Gate A, Gate B, and global exclusion remain open.
