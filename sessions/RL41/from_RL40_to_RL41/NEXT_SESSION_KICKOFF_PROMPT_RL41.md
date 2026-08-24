# RL41 next-session kickoff

Continue the Collatz R-sharp / RL bridge research from the attached RL40 checkpoint as a skeptical research mathematician.

## First actions

1. Read `RL40_PROOF_STATUS_AND_NEXT_ATTACK.md` first.
2. Read the two main RL40 notes:
   - `rl40_additions/RL40_LOW_TRANSPORT_CROSSING_REACHABILITY.md`
   - `rl40_additions/RL40_RL39_SINGLE_STATE_EXTREMIZER_AND_CONCENTRATION_BARRIER.md`
3. Rerun:
   - `rl40_additions/verify_rl40_crossing_aware_area16.py`
   - `rl40_additions/verify_rl40_low_transport_reachability.py`
   - `rl40_additions/verify_rl40_single_state_extremizer.py`
4. Treat any verifier failure as a stop-and-repair event.

## Frozen new facts

In the surviving near-resonant order-2 / `g=2` branch:

- the low-transport floor is now `rho>=18`;
- for low area where the sign-reversal envelope forces `G=4`, the exact common prefix is `11` and the first excursion begins with physical gap `9`;
- synchronized-boundary gap reachability is compressed by
  `Delta=sign*2^s*m -> sign*m*3^c`, `0<=c<=s`, before the next divergence;
- the terminal synchronized suffix has zero odd weight when `G=4`, so the last excursion output must be `-4*2^s`;
- `prod_E J_E=z>1` eliminated all endpoint-compatible area-17 patterns;
- the exact RL39 fixed-multiplicity correction function is
  `C_l(q)=-R log(1-(z/R)2^(-(l-1)/2)3^(-q/l))`, and is decreasing + convex;
- therefore raw RL39 total charge can concentrate in one sacrificial state, so no uniform negative linear term in total `rho` follows from RL39 alone.

## Primary target — compressed area-18+ reachability DP

Do not repeat the timed-out raw permutation search.

Build a DP whose state tracks only information actually used by the proof, for example:

- transport spent;
- signed physical gap at the next excursion start;
- whether the first physical crossing has occurred;
- accumulated / remaining strong sign-reversal budget;
- accumulated exact distortion product (or a rigorous interval / rational numerator-denominator representation);
- enough endpoint information to enforce the terminal `-G` gap and, when `G=4`, zero terminal odd suffix weight.

Precompute canonical excursion summaries by area:

`(r,D,h,p,strong,crossing residues / gap transitions)`

and merge summaries that are numerically equivalent for the DP.  Prune dominated summaries aggressively.

Start at total area 18.  The exact exploratory data are:

- exact area-18 canonical excursions: `1,036,426`;
- crossing-capable: `568`;
- `E(18)=28793/2160`;
- `C(18)=118061/10935`;
- 23 crossing-aware budget-viable partitions, including `(9,9)`.

Try to close area 18 exactly, then determine how far the compressed DP scales before a genuine surviving abstract pattern appears.

## Secondary target — defeat RL39 concentration

In parallel, look for a theorem that prevents the convex extremizer from placing essentially all excess transport charge on one owned odd state.  Promising forms are:

1. a per-state effective-charge cap from local excursion/gap geometry;
2. a lower bound on the number of owned states that must carry nontrivial charge;
3. a direct relation between very large `H` / `l` and excursion distortion `J_E`, so concentration forces compensating excursions and hence charge spread;
4. a sparse S-unit uniqueness theorem for the complementary sublinear-transport regime.

Do not claim that `rho>=18` changes the asymptotic global packing coefficient by itself; a constant transport floor is sublinear in `L`.

## Success criteria

Best case: extend the exact low-transport exclusion substantially or prove a scalable charge-spread/direct-distortion theorem that closes the `g=2` branch.

If full closure is not reached, freeze the strongest exact DP theorem, record the first surviving abstract pattern if one exists, and state precisely which extra constraint would kill it.

Maintain evidence discipline: RL remains open unless a complete audited dependency path is actually closed.
