`/mnt/data/rl292_scratch/verify_first_positive_reduction.py` — PASS, including 679 exact balanced pullback-center identities through canonical depth 14.

No authoritative repository state changed. Gate A remains open with exact residual `k>=25`, odd, `H_can<k`.

Next intended attack: use the exact first-positive crossing formulas together with RL288's `0<M<3^d` / first-positive area theorem to bound `Bcal` on the root family. Do not resume finite endpoint-template potentials unless they directly contribute to this root theorem.

## Fifth checkpoint — finite Bellman front door after neutral-gauge and renewal quotient

Status: ANALYTIC REDUCTION + EXACT RENEWAL QUOTIENT + ROUTE BARRIER / NOT PROMOTED.

### A. Three zero-cost departure roots are an exact Bellman cut

RL288 proved that the fixed seed boundary itinerary has neutral cycle `(101)` and that after quotienting arbitrary repetitions every nontrivial canonical path departs through exactly three off-boundary states. Direct normalized-recurrence replay gives the complete zero-height boundary graph from `(1,-13)`:

- `(1,-13) --0--> (1,-6) --0--> (2,-6)`;
- `(1,-13) --1--> (1,-19) --1--> (1,-28) --0--> (2,-39)`;
- `(1,-13) --1--> (1,-19) --0--> (1,-9) --0--> (1,-4) --0--> (2,-3)`;
- `(1,-13) --101--> (1,-13)`.

Every listed boundary edge has height cost zero. There are no other zero-height off-boundary exits from this boundary component.

Therefore, for RL290's physical Bellman threat `Bcal`, any finite successful future from the seed eventually erases some number of neutral `(101)` loops and enters one of

`R6=(2,-6)`, `R39=(2,-39)`, `R3=(2,-3)`

at zero cost. Hence at witness level

`Bcal(1,-13) = max(Bcal(R6), Bcal(R39), Bcal(R3))`

(with the equality understood as equality of suprema over finite checkpoint-ending futures; neutral infinite paths contribute no checkpoint witness).

This strictly strengthens the previous first-positive reduction: the fixed-seed historical side can be compressed to three fixed physical departure roots before positivity.

### B. Two departure roots collapse exactly

At `R3=(2,-3)`:

- `x=1` is a cost-one physical self-loop `R3 -> R3`;
- `x=0` is a cost-one exit `R3 -> (2,1)`.

Every finite checkpoint-ending future must eventually take `x=0`, so

`Bcal(2,-3)=Bcal(2,1)-1`.

At the positive state `(2,1)`, both legal bits merge physically at equal cost:

`(2,1) --0/1, cost 1--> (2,3)`.

Thus

`Bcal(2,1)=Bcal(2,3)-1`,

and hence

`boxed: Bcal(2,-3)=Bcal(2,3)-2`.

At `R6=(2,-6)`:

- `x=0` gives `(3,2)` at cost one;
- `x=1` gives boundary state `(1,-3)` at cost one.

The complete zero-cost boundary quotient from `(1,-3)` has only two off-boundary exits:

- `(1,-3) --10--> (2,-3)`;
- `(1,-3) --000--> (2,3)`;

with the only recurrent boundary state `-1` contributing a removable zero-cost self-loop. Since `Bcal(2,-3)=Bcal(2,3)-2`, the `(2,-3)` exit is Bellman-dominated. Therefore

`boxed: Bcal(2,-6)=max(Bcal(3,2)-1, Bcal(2,3)-1)`.

Finally `(3,2)` has

- `x=0 -> (4,39)` at cost two;
- `x=1 -> (2,1)` at cost two,

so

`Bcal(3,2)=max(Bcal(4,39)-2, Bcal(2,3)-3)`.

Consequently the entire `R6/R3` side of the seed target is equivalent to only

`Bcal(2,3)<=1`,
`Bcal(4,39)<=3`.

### C. The hard departure root has an exact positive-cost renewal

For `R39=(2,-39)`, the word `101` returns exactly to the seed with total height cost three:

`(2,-39) --1--> (2,-57) --0--> (2,-26) --1--> (1,-13)`.

Classify a finite future by the first deviation from this renewal word:

- first bit `0` enters `(2,-17)` at cost `1`;
- prefix `11` enters `(2,-84)` at cost `2`;
- prefix `100` enters `(3,-28)` at cost `3`;
- prefix `101` returns to the seed at cost `3`.

A checkpoint-ending witness may repeat this renewal, but deleting a completed `R39 -> seed` renewal decreases paid height by three without altering the remaining physical future. Thus a maximal-score/counterexample witness never needs a completed renewal before its first deviation.

Combining Sections A--C gives an exact finite Bellman front door:

`boxed: Gate-A Bellman target Bcal(1,-13)<=0 is equivalent to the five fixed-state inequalities`

1. `Bcal(2,3) <= 1`;
2. `Bcal(4,39) <= 3`;
3. `Bcal(2,-17) <= 1`;
4. `Bcal(2,-84) <= 2`;
5. `Bcal(3,-28) <= 3`.

Necessity: each state is reached by an explicit fixed-seed prefix with exactly the displayed historical height (or is obtained by the exact branch-merger replacement above), so seed Bellman domination forces each threshold.

Sufficiency: any positive-score seed witness first quotients neutral `(101)` loops, then either enters the `R6/R3` branches handled by the first two inequalities or enters `R39`; completed `R39 -> seed` renewals are score-worsening and erase, so the first nonrenewal deviation lands in one of the last three states within exactly its displayed threshold.

This is a finite physical-state cutset theorem, not a finite-horizon certificate.

### D. Exact finite H<=22 falsification support on the front door

Using the repaired RL282 normalized recurrence and exact positive-boundary quotient, restricting total historical height to `<=22` gives the following finite-horizon Bellman maxima relative to the front-door state:

- `(2,3)`, threshold 1: `Bcap=1`, witnessed by checkpoint `8` at added height `2` (tight);
- `(4,39)`, threshold 3: `Bcap=-8`, witness `32` at added height `13`;
- `(2,-17)`, threshold 1: `Bcap=-1`, witness `8` at added height `4`;
- `(2,-84)`, threshold 2: `Bcap=-2`, witness `8` at added height `5`;
- `(3,-28)`, threshold 3: `Bcap=-2`, witness `8` at added height `5`.

FINITE EVIDENCE ONLY. The only tight front-door obligation in the exact H<=22 window is `Bcal(2,3)<=1`.

At the three departure roots themselves the same finite cap gives

- `Bcap(2,-6)=0` (checkpoint `8`, added height `3`);
- `Bcap(2,-39)=-2` (checkpoint `8`, added height `5`);
- `Bcap(2,-3)=-1` (checkpoint `8`, added height `4`).

### E. Ordinary real-magnitude Bellman shortcut fails

A tempting consequence of first-positive `M<3^d` was to seek a real-size Bellman potential such as `log_2(J+2)`. It is false even on the exact height-one kernel.

The globally reachable cost-one edge `2 -> 8` already violates

`J'+2 <= 2^h(J+2)`:

`10 > 8`.

More dramatically, the exact height-one kernel permits long zero-height positive-boundary retention after the paid excursion. Local legal examples such as `82 -> 13850` at macro cost one show that real size can grow by arbitrarily misleading factors while endpoint 2-adic hazard remains small. This is precisely why the Bellman target must be valuation-selective rather than an ordinary magnitude Lyapunov function.

Do not pursue crude `log(J+c)` supersolutions as the principal route.

### F. Strategic consequence

The principal RL292 target is now smaller than both the original all-checkpoint theorem and the previous first-positive-root theorem. Fixed-seed ancestry/gauge complexity has been compiled into a five-state physical Bellman cutset.

Next attack should start with the unique finite-certificate tight obligation

`Bcal(2,3)<=1`,

while red-teaming whether the other four front-door inequalities can be proved with a coarser reserve because they carry substantial observed margin. The Bellman front door should be treated as the new preferred formulation; the first-positive theorem remains a correct but weaker reduction.

Local regression:

`/mnt/data/rl292_scratch/verify_three_root_reduction.py` — PASS.

Finite support scripts:

