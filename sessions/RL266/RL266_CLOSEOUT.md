# RL266 closeout

Date: 2026-09-06  
Classification: **RADIUS5_KAPPA1_32_CLOSED**

RL266 closes exactly one Radius-5 determinant-one topology family: `[3,2]`.

Promoted:
- exact zero-flow-cut five-edge numerator identity for the flat determinant-one setting used here;
- `[3,2]` component compression and complementary two-term reduction;
- universal safe numerator bound `24*3^floor(A/2)`;
- analytic closure of the non-bracketing branch for `A>=57`;
- exact use of the already-audited RL238 LMN two-logarithm dependency to reduce the bracketing branch to `A<=51389`;
- exact 33-edge Stern-Brocot bracket certificate and coarse elimination to four small rows;
- gap-free structural finite certificate of 7,040 canonical positive-domain candidates for `A<=56`, with zero full-D hits;
- independent A<=18 brute-force red-team pass.

Corrections:
- the scratch single-particle component formula was discarded and replaced by the exact edge identity before promotion;
- no inherited theorem is demoted.

Not promoted:
- closure of `[3,1,1]`, `[2,2,1]`, `[2,1,1,1]`, or `[1,1,1,1,1]`;
- closure of the entire `|kappa|=1` sector;
- any `|kappa|=3` or `5` result;
- the Radius-5 local theorem;
- Gate A/B/global exclusion;
- a general Radius-n theorem.

RL267 is prepared but not started. It must remain in determinant one and attack `[3,1,1]` next. It must not advance to `|kappa|=3` merely because `[3,2]` is closed.
