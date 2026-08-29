# RL179 V37 Negative Return and Zero-Height Transition Target

## Main objective

Attack the sole surviving zero-height high-valuation type

`(v,H,J,d)=(37,0,23,-1)`

using the exact RL178 second-transition relation and its forced early negative window.

Frozen facts:

- `g_p=2^37`;
- `y_(p+24)-2y_24=3^24`;
- `(h_24,h_(p+24))=(0,1)`;
- `a_24=a_(p+24)=1` and `G_25=-1`;
- every physical continuation satisfies `G_i<0` for `24<=i<=28`;
- the first arithmetically admissible positive reversal is phase `29`;
- phase-29 zero return is impossible in the exact necessary interface;
- the only phase-29 positive height pairs admitted by that interface are `(1,0),(2,0),(2,1)` with flow quanta
  `2^44/3^29`, `2^43/3^28`, `2^43/3^29`;
- exact global value `F2=3(lambda-1)2^37`;
- corrected physical p-shift and residue-deficit identities from RL178.

## Primary attack A: signed early budget

Compute the exact pathwise negative-flow range accumulated through phase 28 for every RL178 necessary state, then compare the first admissible positive return at phase 29 with the exact high-gap `F2`.  Use interval or rational arithmetic only; do not infer realizability from the necessary automaton.

Seek a contradiction, or a strict requirement on additional later positive support that can be paired with the residue-ordered deficit identity.

## Primary attack B: exact return relation after phase 29

For each of the three positive phase-29 interfaces, continue the normalized integer pair relation across the first subsequent zero return or next sign reversal.  Promote only exact valuation/congruence restrictions that every physical continuation must satisfy.

## Primary attack C: remaining zero-height odd-part classes

If the high branch survives, apply RL178.1 to the other zero-height types with

`w=g_p/2^v` odd.

Work by congruence classes of `w` and exact `v2(3^k w +/- 1)` conditions.  Do not enumerate billions of odd gaps individually, and do not enlarge the RL177 height-only automaton.

## Avoid

- no resurrection of the old RL173 `3^(-G)` functional;
- no use of the RL175 sparse resultant as an independent gap obstruction;
- no silent use of `m>=2^71`;
- no physical-existence claim from a surviving necessary transition state;
- no move to the secondary `h_p>=1` branch until this high/zero-height return mechanism is worked as far as productive.

## Success condition

Preferred: exclude `(37,0,23,-1)`, eliminating zero-height `v=37` entirely.

Strong partial success: prove a new exact return/congruence theorem that removes one or more phase-29 return types or materially sieves the remaining zero-height odd-part classes.
