# RL196 Red-Team Report

Date: 2026-08-31. Status: PASS for the claims actually promoted.

Checks performed:

1. Re-derived `pB=1 (mod L)` and inverse rank `I(r)=pr mod L`.
2. Verified that rank `+1` crosses the c-partition only at `R-1` and `L-1`, whose chronological phases are exactly `t-1` and `t`.
3. Re-derived the G increment identity directly from the two height recurrences; checked the sign convention.
4. Checked that only edges `i=0..22` use both endpoints inside `G_0=...=G_23=0`; no edge-23 duplication is claimed.
5. Checked the anchor: nonnegativity with `h_0=0,c_0=1,a_0>=1` forces `h_1=0`; G0/G1 then force the p-shifted copy.
6. Independently counted the mod-5 placement relaxation. After adding rank 1 and removing rank 2 its zero count is unchanged, its B-edge count drops by exactly one, and its only rank adjacency is 0->1.
7. Confirmed both barrier counts exceed the frozen RL195 floors by wide margins.

No H21 multiplicity map is present, so no H21 budget release is allowed. No atom, branch or global closure claim is supported. PASS with that scope.
