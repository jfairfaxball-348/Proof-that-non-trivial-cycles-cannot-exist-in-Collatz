# RL293 closeout

Date: 2026-09-10

## Authority snapshot

Incoming `main` / `BASE_HEAD`:

`afce6e5659343daf37c78c967c452e60eb57b373`

Incoming authority:

`authoritative/RL293_FIXED_SEED_BALLOT_STATIC_BOUNDARY_DANGER_TREE_SEPARATION_GATE_A_TARGET.md`

Incoming authority blob:

`812733469bdeda0caebddfdbb20140045f51997b`

Incoming `authoritative/START_HERE.md` blob:

`010e166d18bd53407ddee6cf43b41ef3b05753ae`

## Frozen classification

`FIXED_SEED_MINPLUS_OWNER_DANGER_TREE_REDUCTION_AND_K29_CONTRACTION_PROVED`

## Proof state

Gate A remains open, but the exact terminal residual contracts from

`k>=29`, `k` odd, `H_can<k`

to

`k>=31`, `k` odd, `H_can<k`.

Gate B remains separate/open/frozen. Fifth selector unscanned. Radius 6+ frozen. No global non-trivial-cycle exclusion is claimed.

## Main promoted results

Proved analytic mathematics:

- exact odd-affine pullback isometry for every RL292 static danger-tree ball through any fixed legal segment;
- merger-invariant min-area/static-ball separation equivalence for the boundary-hazard subproblem;
- checkpoint-8 area-two renewal/equality-class rigidity;
- checkpoint-2 to checkpoint-8 strict min-plus domination through source-2 cost 29;
- normalized-K first-boundary corridor and high-signed-drift necessary condition for a first checkpoint failure;
- dangerous first-checkpoint principal parity-cylinder representative reduction;
- conditional Bellman-front-door reduction to first-d=1 minimum-owner domination.

Exact finite certificates:

- complete checkpoint-8 nonempty balanced closure through added area `A<=7`, proving `nu_2(J)<=A+1` on that range;
- compact RL288-envelope first-checkpoint splice through historical `H<=28` to `P=(2,3)`;
- exact positive P-source closure through added cost 27, excluding `J=2^29`;
- resulting `k=29 => H_can>=29` Gate-A contraction;
- exact first-positive first-d=1 P-owner certificate through historical `H<=60`.

Method barrier:

- support-count and excursion-count danger charging are false on an explicit genuine fixed-seed history.

## Mechanical repair

The H<=60 owner verifier originally compared the total tiny H<=8 fixed-seed `dist` map with the intended transient count `225`. The map also stores the two terminal checkpoint states `2` and `8`, so its correct total is `227`; the correct transient count remains `225`. The verifier now asserts both numbers and passes. Endpoint set/heights and every mathematical conclusion are unchanged. This is a bookkeeping repair, not a mathematical correction or demotion.

## Verification

Portable sources and frozen outputs are under `sessions/RL293/verification/`.

Closeout fast suite:

- `verify_rl293_pullback_barrier.py`: PASS;
- `verify_rl293_checkpoint8_lowarea.py`: PASS;
- `verify_rl293_checkpoint2_domination.py`: PASS;
- `verify_rl293_first_checkpoint_splice.py`: PASS;
- `verify_rl293_p_source_k29.cpp`: PASS, exact `23,652,724` positive states, `5,962,876` even checkpoints through added cost 27, and `2^29` absent;
- `verify_rl293_first_boundary_corridor.py`: PASS;
- `verify_rl293_first_d1_owner_h60.py`: PASS after the mechanical 225/227 repair;
- target-specific red team: PASS for promoted scope;
- all Python verifier sources compile cleanly.

The complete suite is rerun from a clean reconstructed session before promotion and the internal SHA256 manifest is verified there.

## Not promoted / remains open

- `Bcal(2,3)<=1`;
- all-depth first-d=1 owner theorem `m_P(B)<=H(B)-1`;
- full static danger-ball separation theorem;
- checkpoint-8 excess-one beyond the certified `A<=7` region;
- any `k>=31` contraction;
- universal checkpoint-8 gateway or universal checkpoint-8 minimum ownership;
- Gate B, fifth selector, Radius 6+, or global non-trivial-cycle exclusion.

Exploratory finite observations that are superseded or were not independently status-checked are preserved only in `RL293_SCRATCH_FREEZE.md`.

## Successor

Prepared successor:

`RL294_FIRST_D1_OWNER_AND_TIGHT_P_STATIC_DANGER_TREE_GATE_A_TARGET.md`

Primary mission: prove or sharply characterize the all-depth first-positive first-d=1 minimum-owner theorem rooted at `P=(2,3)`, then use it to collapse the five-state Bellman front door and attack the single tight inequality `Bcal(2,3)<=1` in the principal-representative/high-signed-drift sector of RL292's static danger tree.

## Catalogue

Generated `knowledge/` catalogues are unchanged and `stale/deferred`.
