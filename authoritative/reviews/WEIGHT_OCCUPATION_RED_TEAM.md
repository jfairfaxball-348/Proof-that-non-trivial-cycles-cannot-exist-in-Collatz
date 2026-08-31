# RL194 bounded red team — weight order and zero-height occupation

Date: 2026-08-31. Status: **PASS**; scratch **NOT PROMOTED**.

Incoming authority remains RL193 at
`4ded9b73d84cd3f9101c9eaef81d783e14390914`.

Audited only the supplied report and verifier, plus their stated current
authority assumptions. No new research, extended scan, historical audit,
authority/Git modification, or infrastructure change was performed.

Audited SHA256 identities:

- `WEIGHT_ORDER_AND_ZERO_HEIGHT_OCCUPATION.md`:
  `3d29e89b668dd3657b8f055cf1f74522313dd790c92b3662b316704a3cd88ae3`;
- `verify_weight_order.py`:
  `29a1abc9e3f7febec898b943e328c6a06e54aae30977d47e97fcb487a7f3af31`.

Both files are in `.rl-work/RL194/agent_weight_identity/`.

## Passed mathematical checks

1. **Unified shift and carry.** From `Ap-u0L=1`, the floor increment over p
   lifted phases is u0 except at rank L-1, where it is u0+1. Thus
   `f_i=alpha*q_(i+p)-q_i` agrees with the ordinary formula and with the
   carry error `rho_z*(2-v_z)`. The lifted target q is used whenever the
   p-window crosses L. The exact identity `rho_z=lambda*alpha/2` and
   `alpha>1` are correct. The shift identity is explicitly an inherited
   restatement, not promoted as newly discovered here.
2. **Rank weights and summation by parts.** `I(r)=pr mod L` is the inverse
   mechanical-rank map. The predecessor weight ratio is alpha for target
   phase i>=p, and lambda*alpha for 0<i<p. Both exceed 1, so every d_r is
   positive. Expanding Equation (3) gives exactly the ordinary rank-prefix
   sum, with carry excluded because m<L. Its equality characterization is
   exact. The report does not substitute rank order for chronological
   order.
3. **Positive moving-window inversion.** For
   `H_i=alpha*C_i+beta*Y_i`, with `beta=(alpha-1)/(lambda-1)`, direct
   differencing gives `H_(i+1)-H_i=f_i=3(K_(i+1)-K_i)`. Therefore
   `H_i-3K_i` is constant. Both H and K scale by lambda after L phases,
   forcing that constant to zero since lambda!=1. This proves Equation
   (4), with positive coefficients and genuinely lifted windows. No
   unproved additive normalization is inserted. The canonical Y-window
   formula and displacement Equation (5) follow exactly.
4. **Atom-specific window signs.** The supplied inequalities are direct
   rearrangements of Equation (5) and the incoming canonical prefix signs.
   For the upper atom, a>0 and P_a>0, so the stated strict loss of p-window
   q mass is justified. The lower inequality is correctly not described
   as necessarily a positive q-mass gain. The early signature remains
   anchored at canonical phase zero.
5. **Moment and q-mass enclosure.** At phase zero, the moving-window identity
   is `3K0=beta*Q+alpha*P`, with 0<P<Q. The resulting strict inequalities
   `3K0/(beta+alpha)<Q<3K0/beta` are correct. The verifier's lower bound uses
   upper bounds on beta and alpha; its upper bound uses a lower bound on
   beta. Thus the certified enclosure
   `67236063233<Q<80336439250` has the correct interval directions. Q in
   this section denotes weighted q mass, not the incoming rank-split
   constant or a vertex count.
6. **Full-period carry-completed rank moment.** Adding the carry term to the
   ordinary rank sum gives exactly
   `F=2rho_z-1+sum_(r=1)^(L-1)d_r V_r`. In canonical coordinates,
   d_r equals eta*rho_i for p<=i<L and theta*rho_i for 0<i<p. The constant
   `2rho_z-1=theta` accounts for canonical phase zero and the carry; it is
   not omitted or counted twice.
7. **Actual height-zero occupation.** For nonzero integral heights, V_r<=1/2.
   Consequently the rank moment yields
   `Z0>=2F-3rho_z+1`. Every nonzero-rank d_r is strictly below theta,
   because eta<theta and its canonical rho is strictly below 1. Positivity
   of the certified lower bound ensures N0-1>0, so summing these strict
   per-rank bounds is valid and gives
   `N0-1>(2F-1/2)/theta-3/2`.
8. **Strict integer rounding.** The verifier proves the last real threshold
   is strictly above 43742681437. Since N0-1 is an integer strictly above
   that threshold, it is at least 43742681438; hence
   **N0>=43742681439**. The extra one for phase zero is correctly retained.
   The lower ratio enclosure is valid because its numerator is positive,
   established before division by the upper theta bound.

## Exact verification and numerical scope

Executed:

`python3 .rl-work/RL194/agent_weight_identity/verify_weight_order.py`

Result: **PASS**, exit 0.

The 80-term logarithm enclosure has the correct first omitted power and
positive geometric tail bound. The two-term exponential lower bound and
geometric upper bound are valid for the certified positive arguments below
1. All actual-constant tests use exact Fractions; no floating-point
comparison or enormous explicit power is load-bearing.

The 256 small height assignments and all 1024 rank-prefix boundaries were
replayed successfully. These are correctly labelled algebraic regression
tests, not physical states for the actual branch. In particular the toy K
is defined by the window formula, so its numerical tests do not substitute
for the analytic inversion proof or the inherited physical K0.

## Scope sign-off

N0 is an actual physical height-zero vertex count, conditional on the
recorded physical branch identities and K0. It is not a count of candidate
ranks, H21 terminals, clean shallow starts, zero-defect runs, co-owned
triples, or pairs. No H21 charging-budget release is inferred. The supplied
bound still gives a negative `2N0-L` adjacency lower expression at its
certified floor, as the verifier records.

No inherited claim was invalidated, and no correction/demotion is required.
No outstanding mathematical, numerical, indexing, or scope defect was found
in the audited files. Any stronger downstream consumer remains a separate
obligation.
