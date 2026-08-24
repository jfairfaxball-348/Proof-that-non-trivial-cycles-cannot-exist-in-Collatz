# RL28 next-session kickoff prompt

Continue the RL/3n+1 research from the attached `Collatz_Rsharp_RL27_to_RL28_Handover_2026-08-21.zip` as a skeptical research mathematician.

## Mandatory audit before extension

1. Read `START_HERE.md`, `RL27_PROOF_STATUS_AND_NEXT_ATTACK.md`, `RL27_METHOD_EVIDENCE_AND_NOGO.md`, and `rl27_additions/RL27_FULL_SPREAD_REPAIR_AND_ADJACENT_BLOCK_OWNERSHIP.md`.
2. Run all 19 inherited verifiers in `inherited_rl26/continuation/verify_*.py` and the RL27 verifier `rl27_additions/verify_rl27_full_spread_adjacent_ownership.py`.
3. Treat any failure as stop-and-repair.
4. Preserve the distinction between analytic theorem, exact finite certificate, external computational input, and exploratory evidence.

Do not reopen the already-audited radius-3 branches unless a verifier/dependency check fails.

## Corrected frontier

Under the inherited near-resonant weak-close hypotheses the unique exceptional geometry is

`R == 91 mod 288`, `G=12`, `H=4`,

with balanced-block prefixes

`11011 / 11101 / 11111`.

RL27 repaired the cubic full spread. With

`Delta=max(|U-V|,|V-W|,|W-U|)`,

the exceptional geometry has

`Delta=4(2B+3Y)`,

because the omitted pair is

`U-V=4(2B+3Y)`.

Do not reuse the old claim that `4(3B+Y)` is sharp for the full `Delta`.

RL27 also proves:

- exceptional geometry forces `e>=37` via the prefix-aware `V` numerator floor;
- incoming valuation ownership:
  `nu_x mod6 in {0,2}`, `nu_y mod6 in {3,5}`, `nu_R=2`;
- the three trajectories undergo a complete order reversal across the balanced macroblocks, forcing at least two later opposite-parity crossings.

## Primary Track — first synchronized sign-reversal lemma

Let

`u_j=T^j(R)`, `v_j=T^j(R+12)`, `w_j=T^j(R+4)`.

At an equal-odd-count synchronization with common odd count `p`, exploit

`2^j(v_j-u_j)=3^p*12 + (Q_v-Q_u)`,

`2^j(w_j-u_j)=3^p*4  + (Q_w-Q_u)`.

The common macroblock endpoint has synchronized gap target

`(v_b-u_b,w_b-u_b)=(-8,-12)`.

Find and analyze the first synchronization where one gap changes sign.

Attack it from both sides:

### Forward cone

Use:

- forced prefixes `11011/11101/11111`;
- least-state inequalities;
- equal-weight / first-divergence identities from RL21;
- exact sparse difference `U-V=8B+12Y`;
- the repaired full-spread lower bound.

### Backward cone

Use:

- endpoint gaps `12,8,4`;
- `nu_x mod6 in {0,2}`;
- `nu_y mod6 in {3,5}`;
- `nu_R=2` exactly;
- predecessor alignment with `z_close=(4R-1)/3` and the RL23/RL24 high-threshold packing geometry.

### Desired theorem

Prefer, in order:

1. prove the forward/backward synchronized cones cannot meet;
2. show any meeting forces a proper-factor/resultant obstruction already covered by the sparse/radius-3 machinery;
3. prove reconvergence requires `Omega(e)` disagreement/high-valuation events, yielding a positive-density global penalty;
4. derive a substantially sub-`eY` numerator-range bound in the unique weak sector.

## Secondary Track — sparse/resultant interface

Investigate whether

`U-V=8B+12Y`

plus the endpoint valuation classes can be normalized into one of the already-closed sparse uniqueness/resultant configurations. Be extremely explicit about hypotheses: do not claim radius-3 closure applies merely because an expression has few terms. Identify the exact polynomial/support/gcd object and verify every interface assumption.

## Known no-go evidence

Do not spend the session simply:

- pushing the simultaneous mod-`2^k` least-state lift deeper; the tree grows strongly through tested depths;
- trying to prove a density contradiction from the raw 3-adic valuation-tail congruence alone; low-average admissible tails were found;
- adding another independent local packing constant without coupling it to the exceptional three-block geometry.

The exploratory scripts are under `rl27_experiments/` and should be used to red-team candidate invariants.

## Closing discipline

If a new lemma is found, create an exact verifier where appropriate, update the proof-status ledger, and state clearly whether it is analytic, finite-certified, external-input conditional, or only computational evidence. RL remains open unless the final global implication is fully justified.
