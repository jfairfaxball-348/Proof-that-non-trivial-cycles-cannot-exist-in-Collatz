`/mnt/data/rl292_scratch/departure_root_cap.py`,
`/mnt/data/rl292_scratch/frontdoor_cap.py`.

No authoritative repository state changed. Gate A remains open with exact residual `k>=25`, odd, `H_can<k`.

## G. Exact minimum-height H<=24 certificate closes residual k=25 (NOT YET PROMOTED)

### G1. Motivation and dominance lemma

The authoritative RL282 certificate closes every odd terminal exponent through k=23 and leaves

`k>=25`, `k` odd, `H_can<k`.

For k=25 specifically, a Gate-A violator must have integer height `H_can<=24`. Therefore an exact minimum-height closure through H<=24 is sufficient to close the whole k=25 case.

Instead of retaining every `(d,J,H)` history, use the physical-state shortest-path dominance lemma:

- future canonical transitions depend only on `(d,J)`;
- every edge has nonnegative height increment `d-1`;
- if the same physical state `(d,J)` is reached at heights `H1<=H2`, every future available from the H2 history is also available from the H1 history with weakly smaller total height.

Hence, for any minimum-height endpoint question under a height cap, only the least height attained at each physical state is relevant. Pruning all larger-height duplicates is exact, not heuristic.

The positive phase uses the same RL282 exact quotient:

- positive even d=1 states are checkpoints;
- launch is forced;
- enumerate every first return to d=1 within remaining height;
- positive odd returns follow the unique stay-odd zero-height boundary branch until repetition and collect every complementary even exit.

### G2. Reproducible verifier

Local standalone verifier:

`/mnt/data/rl292_scratch/verify_rl292_height24_minima.py`

Frozen output:

`/mnt/data/rl292_scratch/RL292_HEIGHT24_MINIMA_OUTPUT.txt`

Standalone rerun: PASS.

Observed exact counts:

- height cap: 24;
- upstream minimum physical states retained: 7,396,469;
- first positive d=1 physical states at minimum height: 19;
- positive even checkpoint physical values at minimum height: 320,762;
- of these with minimum height <=22: 75,232;
- positive odd boundary origins used by the quotient: 58,132;
- maximum stay-odd trace among encountered origins: 356.

### G3. Regression against authoritative RL282 H<=22

The minimum-height verifier exactly reproduces the promoted RL282 power minima through H<=22:

`k1:H3, k3:H3, k5:H9, k7:H15, k9:H15, k11:H18, k13:H18, k15:H22`.

There are no additional power-of-two checkpoints at minimum height <=22. This is an independent regression of the new pruning architecture against the authoritative certificate before using the extension.

### G4. New exact H<=24 power minima

Through H<=24 the complete minimum-height power list is exactly

`k1:H3, k3:H3, k5:H9, k7:H15, k9:H15, k11:H18, k13:H18, k15:H22, k21:H24`.

In particular:

- `2^17`, `2^19`, `2^23`, and `2^25` are absent at height <=24;
- `2^21` first appears at exact minimum height 24;
- `2^25` is absent from the entire exact minimum-height closure through 24.

Therefore a terminal/checkpoint `J=2^25` cannot satisfy `H_can<25`.

Classification candidate:

`EXACT_MINIMUM_HEIGHT_H24_K25_GATE_A_CLOSURE_PROVED`.

Once promoted, the exact Gate-A residual contracts from

`k>=25`, k odd, `H_can<k`

to

`k>=27`, k odd, `H_can<k`.

Until closeout/promotion, repository authority remains unchanged at the inherited k>=25 residual.

### G5. Bellman work retained but not displaced

The fixed-seed Bellman route remains the scalable principal route for the infinite residual. The H24 closure is a fast-track finite contraction, not a replacement for the global theorem.

Useful exploratory observations retained from the V(8) attack:

- checkpoint 8 launches at zero height to `(d,J)=(2,15)`;
- there is an exact positive-cost renewal `(2,15) --00101, cost 6--> (2,15)`, so completed copies can be erased from a maximal Bellman witness;
- the tight `(2,3)` root admits the local affine normalization described in the prior working notes;
- exhaustive relaxed local-ballot suffix tests through length 13 found no valuation/area violation, but this is finite evidence only;
- the tempting reduction of a first valuation failure to the exact child `2^(DeltaH+4)` is VALID ONLY when that failure coincides with the first magnitude escape. RL288's harmless earlier magnitude-escape barrier remains active, so this conditional subcase must not be globalized.

Next scalable target after recording the finite k=25 closure: return to the tight Bellman/front-door problem, preferably the checkpoint-8 renewal/equality rigidity or an exact danger-cylinder ancestry theorem. Do not extend raw height enumeration merely for its own sake; any further finite cap should have an explicit residual-closing payoff.

## H. First-positive analytic over-approximation closes k=27 locally

Status: **LOCAL SCRATCH / NOT PROMOTED**.

This section supersedes the need to finish the large negative renewal tree for the finite k=27 contraction. It does **not** supersede the Bellman route for the infinite residual.

### H1. Analytic first-positive envelope

Use the promoted RL288 first-positive theorem. At the first canonical state with `J>0`, set

`M = J + 2^d - 2`,
`A = H + d - 1`.

Then

`0 < M < 3^d`,
`nu_2(M) <= A`,

with equality only at `(d,J,H)=(3,2,1)`.

Also use the promoted mod-3 reachability invariant

`J mod 3 in {0, (-1)^d}`

and the depth-area lower bound used in RL288

`A >= d(d-1)/2`.

For total height `H<=26`, this forces `d<=8` because `d=9` would require

`A>=36 > 26+9-1=34`.

For each `1<=d<=8`, every genuine first-positive state is therefore contained in the finite set

`1 <= J <= 3^d - 2^d + 1`,
`J mod 3 in {0,(-1)^d}`,

with minimum admissible height bounded below by

`H >= (d-1)(d-2)/2`

and

`H >= nu_2(M)-d+1`.

Except for the unique equality state `(3,2,1)`, integrality sharpens the latter to

`H >= nu_2(M)-d+2`.

Assigning every such physical state its *smallest* analytically permitted height creates a deliberate over-approximation of the true first-positive fixed-seed set: it may include fake states and may give genuine states more remaining height than they actually possess, but it cannot omit a genuine first-positive state relevant to `H<=26`.

There are exactly 6,224 physical relaxed first-positive seed states in this envelope.

### H2. Positive-future closure and shortest-path dominance

Promoted RL279 positive invariance gives: after `J>0` is first reached, every legal future remains `J>0`.

Close all legal positive futures from the 6,224 relaxed first-positive seeds through total height 26 using the exact normalized recurrence.

At each physical state `(d,J)`, retain only the least height reached. This is exact shortest-path dominance because transition legality and physical successors depend only on `(d,J)`, while every edge has nonnegative cost `d-1`. A larger-height duplicate can never improve a future minimum-height target.

The complete relaxed positive closure contains exactly

`11,380,217`

minimum-height physical states.

The complete power-of-two minima appearing in this deliberately enlarged closure through H<=26 are

`k1:H2, k3:H2, k5:H8, k7:H14, k9:H14, k11:H17, k13:H17, k15:H21, k17:H24, k19:H25, k21:H23`.

In particular there is **no** checkpoint

`J = 2^27`

at total height `H<=26`. There are also no relaxed `k=23` or `k=25` power checkpoints through H<=26.

### H3. k=27 closure logic

Any genuine terminal/checkpoint with `k=27` and a Gate-A violation would have

`H_can < 27`, hence integer `H_can <=26`.

