# RL198 Red-Team Report

Date: 2026-08-31. Verdict: PASS for the scoped claims.

1. Re-derived RL197 numerators from the certified normalized gaps:
   `C34=21*2^(33+e34)`, `C33=63*2^(32+e33)`.
2. Applied only the inherited physical zero-prefix valuation law
   `v_2(C_start)=sum d_j>=tau`; no normalized-gap or mod-3 selector was smuggled in.
3. Checked the binary bounds force `e34=e33=1` uniquely.
4. Intersected with all six RL197 local states; exactly `011,111` remain.
5. Checked RL197 zero-edge states `000,100` are disjoint from the global survivors.
6. Checked valuation equality at `tau=34` and `tau=33`; positivity of every `d_j`
   forces every suffix cost to one.
7. Checked the `tau=35` valuations 35/36 give leading cost one/two after the common
   34-unit suffix.
8. Recomputed the preterminal rank interval and verified it lies wholly in mechanical bit 2.
9. Recomputed `ell=20`, preterminal common height 20,
   `C_pre=14*3^34`, `C_pre mod 8=6`, and `3*C_pre/2=7*3^35`.
10. Checked the monotone-height consequence on the unit-cost zero suffix, so the stronger
    whole-prefix zero-edge exclusion is valid.
11. Explicitly did not infer the final endpoint orientation/sign from `C_pre mod 8`.
12. Confirmed RL197's local interface theorem is narrowed by additional inherited prehistory,
    not contradicted or demoted.
13. Confirmed no H21 budget release, H21-family exclusion, branch/Gate/global closure is claimed.

No correction/demotion event is required.
