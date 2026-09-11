# RL295 closeout

Date: 2026-09-11

## Authority snapshot

Incoming `main` / `BASE_HEAD`:

`e59bccbc0091b9a118fb63bc8677895ae02ab03b`

Incoming authority:

`authoritative/RL295_CANONICAL_CASCADE_WALL_DEBT_AND_P_OWNER_GATE_A_TARGET.md`

Incoming authority blob:

`52200054aca6c9e4df1f6c2d866831ca0c6d2e06`

Incoming `authoritative/START_HERE.md` blob:

`96415f8407e5a148faf778b8a7e811a98ed42922`

## Frozen classification

`ZERO_DEPTH_WALL_NORMALIZATION_4_39_CUT_AND_Q17_OWNER_TAIL_PROVED`

## Proof state

Gate A remains open with exact residual

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted results

- exact zero-depth wall normalization `W_u o (b,B)=(b,B+3^b u)` and `(a,A)oW_u=(a,A+u)`;
- exact post-edge area accounting with no fictitious negative wall cost;
- exact double-E wall refactorization to `A' o P`;
- all-depth proof that every nonexceptional `(4,39)=P o Z o Z` sector is P-owned within the RL292 allowance;
- unique `(4,39)` residual `00 -> (5,191)` at source cost 6;
- exact inequality `Bcal(4,39)<=max(Bcal(P)+2,Bcal(5,191)-6)`;
- complete replayable P -> Q17 certificate: 303 columns, cost 183;
- exact `(6,807)` spine to Q17: 16 columns, cost 169;
- all-depth Q-tail P-owner bound `m_P(Q_d)<=d^2-3d-55` for d>=17;
- exact source cost `d^2-3d-69`, constant owner lag 14, and 17 units spare inside the inherited +31 credit;
- exact finite list of sixteen pre-Q17 `(6,807)` side sectors.

## Verification

Portable verifier:

`sessions/RL295/verification/verify_rl295_wall_owner.py`

Frozen output:

`sessions/RL295/verification/RL295_FAST_VERIFIER_OUTPUT.txt`

Target-specific red team:

`RL295_RED_TEAM_PASS_FOR_PROMOTED_SCOPE`.

The verifier passed before transition. The authority snapshot was re-read before closeout, and `main` remained at the RL294 base commit.

## Not promoted / remains open

- complete Bellman/P-owner closure of `(5,191)`;
- finite owner-search reductions from `(5,201)`, `(6,733)`, `(6,949)`, `(6,807)` unless rebuilt with frozen witnesses;
- closure of the sixteen pre-Q17 `(6,807)` side sectors;
- complete `(4,39)` Bellman inequality `Bcal(4,39)<=Bcal(P)+2`;
- the other non-P RL292 front-door states `(2,-17)`, `(2,-84)`, `(3,-28)`;
- collapse of the five-state front door to P;
- `Bcal(P)<=1`;
- any `k>=31` contraction;
- Gate A;
- Gate B, fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

High-value unpromoted reductions and superseded tail attacks are frozen in `RL295_SCRATCH_FREEZE.md`.

## Successor

Prepared successor:

`RL296_FINITE_WALL_SECTOR_CLOSURE_AND_Q17_OWNER_GATE_A_TARGET.md`

Primary mission: convert the remaining finite `(5,191)` wall sectors into replayable owner/Bellman certificates, use the promoted Q17 tail splice wherever `(6,807)` is recovered, close `(4,39)` if possible, then propagate the same exact wall calculus to the other non-P RL292 front-door states.

Only after the non-P front door closes should the tight target `Bcal(P)<=1` become primary.

## Catalogue

Generated `knowledge/` catalogues remain unchanged and `stale/deferred`.
