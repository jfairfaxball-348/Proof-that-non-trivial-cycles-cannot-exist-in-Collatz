# RL237 — coupled H20 recurrence, repaired-charge saturation, and H21 returnability

## 1. Incoming blocker and exact spacing 210

RL237 begins at the RL236 exact H20 blocker

- `T=216803362095665397`,
- `H=20`,
- owners `{32,33,34}`,
- full-prefix core `[62456644959,96166487667]`.

The inherited carry-completed chronological-return transport excludes every self-return separation `35..209`. The exact scan has `1014` carry-word atoms across `85` separations with nonempty translated-core overlap and no survivor.

Therefore the exact invariant has spacing `>=210` and occurrence cap

`floor(137528045312/210)=654895453`.

This cap is used only for this invariant.

## 2. Coupled three-band repair and the six-owner H20 target

Keep the RL236 early and late levels at their exact local-budget definitions and allow the middle band to move. With `U=2^-25`, define

- `a = B(T=216803362095665397,H=20,r_hi=96166487667)/3`;
- `c = B(T=4052555153018976267,H=24,r_hi=111884226030)`;
- initially raise `b` until the exact H20 six-owner cell `T=150094635296999121`, `H=20`, owners `{31,32,33,34,35,36}`, core `[0,18406412838]` binds.

Numerically this corner has

- `a≈6.607706073334 U`,
- `b≈1.367050541510 U`,
- `c≈1.137969958291 U`.

The exact six-owner recurrence scan can be extended through separation `5596`: `278049` atoms, `1486` nonempty-overlap separations, no survivor. Hence spacing `>=5597` and exact invariant-specific cap `24571742`.

## 3. Final coupled lift and exhaustive 7,531-cell sweep

After paying that exact cap, the only locally profitable cap-free motion is to continue increasing the middle band. A full reconstruction of all `7531` retained atomic cells is mandatory; the old 13-cell generic-envelope shortlist is not sufficient once `b` changes.

The first genuinely new uncapped binding cell is

- `T=550346996088996777`,
- `H=21`,
- owners `{34,35}`,
- core `[109195551555,122224615441]`.

Set `b` exactly at this cell's local-budget boundary, i.e. `a+b=B(new H21 cell)`. Numerically

`b≈2.033753297438 U`.

At the final schedule the only over-budget cells are exactly:

1. H20 `T=150094635296999121`, owners `{31,...,36}`, paid at cap `24571742`;
2. H20 `T=250157725494998535`, owners `{32,33,34,35}`, paid at the RL236 cap `45358853`;
3. H21 `T=350220815692997949`, owners `{33,34,35}`, paid at inherited cap `137390654`;
4. H21 `T=450283905890997363`, owners `{34,35,36,37}`, paid at inherited cap `137390654`.

Exactly three cells bind without incidence assumptions: the H20 `{32,33,34}` cell, the new H21 `{34,35}` cell, and the H24 late-band cell. Every other retained cell lies within its local certified budget.

The resulting exact rational lower bound satisfies

- ordinary absolute corrected flow `>742.4232`;
- each signed corrected-flow mass `>371.2116`;
- each directional K variation `>123.7372`.

The variation statements are total-variation statements, not prefix-excursion claims.

## 4. Exact saturation obstruction

At the final H21 boundary, before charging occurrences of that new H21 invariant, the exact derivative for further middle-band increase is `6183`. Crossing the cell would cost one unit of charge per occurrence, so strict further improvement requires occurrence count `N<=6182`.

A direct spacing theorem would therefore require

`spacing >= 22242932`.

Spacing `22242931` yields cap `6183` and is neutral, not strictly improving; spacing `22242932` yields cap `6182` and is sufficient.

The local `a,b,c` cone has no alternative cap-free improving direction at this corner: early increase is already net-negative after its exact penalties; late increase violates the binding H24 budget; lowering early or late charge loses more objective than it frees. Thus the new H21 cell is a genuine local saturation obstruction of this repaired three-band programme.

## 5. Final H21 returnability certificate

For the new exact H21 `{34,35}` invariant, the same chronological-return machinery excludes all self-return separations `36..3031`. The exact scan has `41039` atoms across `569` nonempty-overlap separations and no survivor.

Therefore this exact invariant has spacing `>=3032`, cap `45358853`.

This does **not** reopen the charging direction: `45358853 >> 6182`. It is promoted as a returnability marker showing that the recurrence mechanism remains coherent on the new blocker.

## 6. Strategic freeze

The repaired sparse-family/chronological-recurrence programme has made genuine progress from RL231 through RL237 and is preserved as a returnable branch. It is not declared dead.

Nevertheless, its present local continuation asks for a very large additional incidence improvement on the new H21 invariant. At the user's direction, the programme is frozen here. RL238 must not continue this branch by default.

RL238 pivots to Gate B and radius 4: accept the already-proved radius-3 theorem and its unresolved global bridge as inherited state, construct/prove the exact radius-4 analogue, and determine whether the larger local theorem permits a structurally easier global bridge.
