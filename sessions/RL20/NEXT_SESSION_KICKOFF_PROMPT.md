# Next-session kickoff prompt

Continue the RL/3n+1 research from the attached RL20 Global Bridge Handover as a skeptical research mathematician.

First run all eight RL20 verifiers listed in `START_HERE.md`. Treat any failure as a stop-and-repair event. Read `RL20_PROOF_STATUS_AND_NEXT_ATTACK.md` and `RL20_NEAR_RESONANT_GCD_BLOCK_GEOMETRY.md` before extending the argument. Do not redo the closed radius-3 branch unless a verifier fails.

RL is still open. Radius 3 is closed for the inherited proof chain. The local-grammar-only bridge to radius 3 is formally false: the exact 184-bit model has minimum all-rotation distance 4 but is not an RL object because `D` does not divide `Q`. Therefore any new bridge must use genuinely global information such as `D|Q`, exact state ownership, or an arbitrary-rotation weighted-difference identity.

Primary track — balanced gcd-block return:

In the near-resonant branch `lambda<16/15`, write `A=ga`, `L=g ell` and `E_j=K_j-j ell` at canonical block cuts. RL20 proves `E_j>=0`. If some proper `E_j=0`, then the corresponding genuine cycle state satisfies

`R# < x_j < (16/15)R#`

and is necessarily odd.

Attack the precise question:

> Does a second odd, exact-balanced, `D`-divisible rotation in `(R#,16R#/15)` force either a cyclic adjacent-transposition radius-3 pair or a direct weighted-difference contradiction?

Start from the inherited arbitrary-rotation difference identity. Substitute `K_j=j ell` before estimating. Seek a nonzero multiple of `D` trapped in absolute value below `D`, or a transport/radius bound. Do not assume the desired bridge is true: try to falsify the sharp candidate theorem as well as prove it.

Secondary track — strict block excursion:

If no proper balanced cut exists, then every proper canonical block state lies above `45R#/16`, while the normalized coboundary lift remains monotone inside the narrow strip `(R#,lambda R#]`. Try to convert this repeated physical height separation into a quantitative packing or weighted-population contradiction.

Keep these results frozen unless a verifier fails:

- local bridge countermodel and all-rotation minimum 4;
- direct final-return-address/CF no-go;
- raw block-polynomial coboundary tautology;
- repaired final-return compatibility, with `t_close=1` only in `R#==91 mod144`;
- hard weak-close global numerator lower bound;
- continued-fraction denominator floor `L/g>=49,547,666,544` conditional on inherited `R#>=2^71` and without LMN.

Do not begin a generic radius-4/5 classification ladder. Radius 3 should be used only as a finished contradiction engine if a new global theorem actually forces entry into it.

At session end, update the proof-state ledger, label analytic results vs exact finite certificates vs inherited external inputs, rerun all release verifiers, and produce the next zipped handover.
