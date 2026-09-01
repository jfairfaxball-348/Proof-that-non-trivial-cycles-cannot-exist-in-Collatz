# RL214 research report — discrete ownership quotient at e=16

Date: 2026-09-01.

RL214 attacked the exact route requested by RL213: a full-word ownership quotient observable outside the saturated endpoint-moment and G56 families.

The first task was a representation issue. RL206's quotient state and the H21 odd root live in different-looking coordinate systems. Expanding the accelerated exponents into the complete binary word and aligning the binary phase at the H21 root proves that they are the same state:
`y_0=Q(d)/(2^A-3^L)`.

That bridge alone is not a new obstruction. It makes the RL206 limitation explicit: ordinary ownership only says `Q modD=0`; a residue of the quotient requires `Q modD^2`.

RL214 then extracted a genuinely new full-word inequality. The complete p-arc from the root has a positive affine numerator, while the inherited root gap is exactly `K_0=2^37`. This gives
`0<y_0<K_0/(alpha-1)`, and the inherited logarithmic defect bounds make the portable exact version
`29y_0<48LK_0`.

This materially changes the e=16 arithmetic problem. RL212 had left an infinite progression of exact eta/root lifts over each H21-compatible prefix. RL214 proves that positivity and the p-arc cap leave only `k=0..36,180` or `0..36,181` in those progressions: exactly **1,629,819,720** bounded root candidates.

The ordinary terminal Hensel restriction can now be applied to that finite family without a CRT-independence handwave. Exact modular counting removes 789 individual candidates, but no prefix; **1,629,818,931** remain. Both states, all four mod18 classes, and all 469 RL212 low ternary classes survive.

So RL214 is a structural advance but not a rank deletion. It turns the ownership quotient from an unbounded formal variable into a finite exact e=16 candidate family and identifies the next missing global datum: a residue of `y_0`, equivalently `Q modD^2`, or an independently anchored congruence/valuation of the full p-arc numerator.

The frontier remains **13,415,865,871** necessary terminals. No physical H21 incidence/charge, branch contradiction, Gate closure or global nontrivial-cycle exclusion is proved.
