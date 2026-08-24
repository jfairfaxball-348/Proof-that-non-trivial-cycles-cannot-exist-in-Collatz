# RL40 next-session kickoff

Continue the Collatz R-sharp / RL bridge research from the attached `Collatz_Rsharp_RL39_to_RL40_Handover_2026-08-21.zip` as a skeptical research mathematician.

## First actions

1. Read `RL39_PROOF_STATUS_AND_NEXT_ATTACK.md` first.
2. Read RL38 and RL39 in full:
   - `rl38_additions/RL38_SCALED_GAP_TELESCOPING_AND_CROSSING_CHARGE.md`
   - `rl38_additions/RL39_ODD_OR_VALUATION_TRANSPORT_CHARGE.md`
3. Rerun these verifiers before extending the argument:
   - `rl36_additions/verify_rl36_g2_excursion_charging.py`
   - `rl37_additions/verify_rl37_g2_sign_reversal_bridge.py`
   - `rl38_additions/verify_rl38_scaled_gap_telescoping.py`
   - `rl38_additions/verify_rl39_odd_or_valuation_charge.py`
4. Treat any verifier failure as a stop-and-repair event.

## Primary target

Do **not** reopen already-closed radius-3 branches and do not spend the session shaving RL35 constants.

Attack the remaining order-2 / `g=2` bridge by combining:

- RL37: `rho >= 16`;
- RL38: synchronized runs cancel exactly from scaled-gap multiplicative dynamics, `lambda=prod_E J_E^2`, and the mandatory sign-changing excursion satisfies `r_cross >= max(7,c_pre+2)` with ineffective-excursion bound `t_E<3^(r-1-c)`;
- RL39: `rho <= sum_y [l_y H_y - log_3(2) l_y(l_y-1)/2]`, with `l_y<=nu(y)`, `sum nu=A`, and correction bound `R log(1+1/(3y)) <= z/(3^H_y-z/R)`;
- exact near-resonant identity
  `A/L = log_2(3) + log(lambda)/(L log 2)`.

The goal is a **uniform overlap inequality** that forces the surviving `g=2` branch below the next continued-fraction gate (approximately `0.1909116`) or otherwise makes the mandatory sign reversal impossible.

## Work plan

### Track A — solve the RL39 constrained extremal problem

For fixed assigned valuation multiplicity `l`, determine the sharp maximal correction factor compatible with a transport charge `q = lH - alpha*l(l-1)/2`, `alpha=log_3 2`.

Then aggregate over states using `sum l<=A` and the exact `A/L` relation. Identify whether the extremizer concentrates or spreads valuation. Use exact/rational computation to discover the extremal pattern if useful, but formulate the final result analytically.

### Track B — exploit effective transport from RL38

Partition excursions by `r-c` or by inward kick `t_E`. Show that excursions with small `r-c` contribute too little to reverse the scaled gap. Therefore a fixed amount of total transport must lie in effective excursions. Feed that effective transport into Track A's product saving.

### Track C — direct excursion distortion, if needed

Because `lambda=prod J_E^2`, try to bound `log J_E` directly by the RL39 area/valuation variables. A direct inequality may avoid separately summing odd correction factors.

## Required skepticism

Red-team every use of:

- sign/orientation conventions for positive vs negative excursions;
- boundary columns at excursion starts/ends;
- whether `l_p` is equal to or only bounded by the final outgoing valuation;
- physical gap vs scaled gap;
- any claim that a synchronized run has a specific parity pattern;
- strict versus weak inequalities when converting to the CF gate.

Do not use the failed naive gcd route: excursion numerator differences can share a factor `3`.

## Success criteria for this session

Best case: close the order-2 / `g=2` branch analytically and state exactly what remains before global RL closure.

If full closure is not reached, freeze the strongest rigorously proved overlap inequality, quantify the remaining numerical gap, give an exact extremizer/countermodel if one exists, add a verifier, and prepare the next handover without overstating the result.
