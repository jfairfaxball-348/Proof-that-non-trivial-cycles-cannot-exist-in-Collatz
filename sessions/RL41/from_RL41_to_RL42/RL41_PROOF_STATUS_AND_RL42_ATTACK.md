# RL41 proof status and RL42 attack

Date: 2026-08-22

## Executive status

RL is **not proved**. The active near-resonant order-2 / `g=2` balanced-return branch is **not closed**.

RL41 continued the RL40 low-transport attack substantially. The current **research checkpoint** is

> **`rho >= 28`.**

Areas 18 through 27 were eliminated during the RL41 session by progressively stronger compressed physical-gap/distortion searches plus absolute numerator congruences.

There is, however, an important reproducibility distinction. The RL40 theorem `rho>=18` is fully retained with its original verifier bundle. The RL41 area-24/25 source fragments and exact area<=25 enumeration statistics are retained. The large area-26/27 transient search code/tables were not all persisted before session handover. Consequently, `rho>=28` should be regarded as the **current completed-session mathematical checkpoint**, but RL42 should reconstruct/rerun the area-26 and area-27 finite certificates before promoting it to a fully artifact-audited frozen theorem.

This is an evidence-preservation issue, not a discovered mathematical counterexample or verifier failure.

## Inherited frozen facts from RL40

The attached inherited RL40 handover contains the fully reproducible theorem

`rho >= 18`

in the surviving near-resonant order-2 / `g=2` branch, together with:

- exact crossing-aware area-16 and area-17 elimination;
- exact telescoping distortion identity `prod_E J_E = z > 1`;
- RL39 fixed-multiplicity correction function
  `C_l(q)=-R log(1-(z/R)2^(-(l-1)/2)3^(-q/l))`;
- proof that this correction is decreasing and convex in the assigned transport charge;
- the resulting **concentration barrier**: RL39 alone cannot produce a negative product term linear in raw total `rho`, because excess transport can concentrate in one sacrificial very-high state.

Read `inherited/Collatz_Rsharp_RL40_to_RL41_Handover_2026-08-21.zip` before extending anything.

## RL41 low-transport progression

### Areas 18--22

A compressed DP was built around the actual invariants used by the proof:

- total transport area spent;
- signed physical gap at excursion boundaries;
- crossing parity / crossing count;
- exact or maximized strong sign-reversal budget;
- exact distortion product compressed to powers `2^A/3^B`;
- terminal gap compatibility.

The search eliminated areas 18, 19, 20, 21 and 22.

Important milestones:

- area 18: 1,624 analytic-pruned DP nodes, 30 endpoint-compatible abstract paths, zero in the required window `1 < prod J_E < sqrt(16/15)`;
- area 19: 5,523 DP nodes, zero allowed near-resonant path;
- area 20: 24,609 DP nodes, zero allowed near-resonant path;
- area 21: three-crossing budget possibility `(7,7,7)` is physically impossible because the unique area-7 crossing requires incoming gap 1 while the first excursion starts at gap 9; the one-crossing DP has no allowed distortion path;
- area 22: `G=8` must be split off from `G=4`; the `G=8` possible initial gaps were safely over-approximated by `3,9,27`, and no terminal-compatible area-22 crossing exists. `G=4` also has no allowed near-resonant product.

This moved the floor to `rho>=23`.

### Area 23: first abstract arithmetic survivor

At total area 23 the compressed DP first produced genuine abstract near-resonant survivors. They all reduced to

`(a,l)=(46,29)`,

with

`prod J_E = 2^46 / 3^29`.

This is the same first reduced near-resonant pair previously seen in RL37.

The physical-gap/distortion compression alone therefore stops being sufficient at area 23.

Restoring the **absolute numerator factor** via the Collatz parity numerator

`Q(u) mod (2^46-3^29)`

eliminated both preterminal survivor classes. In one class 42,127 absolute-prefix states were tested at the relevant boundary with zero required residue; in the second, 206 budget-viable absolute residues were attained and again none equalled the required final residue.

The remaining `G=4` three-crossing cases and `G=8` budget cases were also eliminated.

Thus area 23 was closed.

### Area 24

A faster exact excursion enumerator was introduced using constant-time append recurrences

`Q(w0)=Q(w)`,

`Q(w1)=3Q(w)+2^{|w|}`,

and suffix peak recurrence

`M(wb)=max(1,(3^b/2)M(w))`.

Exact area-24 envelopes:

`E(24)=147604/6561`,

`C(24)=183671/9720`.

The compressed distortion DP found ten `G=4` abstract terminal configurations; **all ten** again reduced to `(46,29)`. An absolute-`Q` residue DP eliminated every one. The remaining `G=8` partitions had no allowed distortion path.

Thus area 24 was closed and the floor became `rho>=25`.

The retained file `rl41_additions/qmod_area24_alltargets.py` contains this stage of the absolute residue machinery. It depends on generated raw excursion tables; see the reproducibility ledger.

### Area 25

Exact retained enumeration statistics:

`E(25)=185963/8192`,

`C(25)=2230444/98415`,

and total canonical area-25 excursions

`362,802,072`,

with `17,840` integer-crossing excursions.

The `G=4` compressed distortion search produced 22 abstract near-resonant targets, all at `(46,29)`. The exact absolute numerator-residue DP eliminated all 22. The separate `G=8` search had no near-resonant terminal path. The total strong envelope satisfies

`F(25)=596977/26244 < 93/4`,

which excludes `G>=12` at this area.

Hence area 25 was closed and the floor became `rho>=26`.

The retained files `global_dp25_g4.py`, `stream_25_fast.cpp`, and `stream25_fast_stats.txt` document this frontier. The session also produced an exact absolute-residue elimination, but that final area-25 script was not retained as a separate persistent file.

### Area 26

A useful analytic simplification avoids a monolithic full area-26 search for most branches.

For a single-excursion half-return, the exact relation forces

`D * 2^{v2(G)} 3^{c1} / G = 2^a + 3^l`,

so in particular

`D >= 2^a + 3^l`.

For a canonical area-`rho` excursion, `h<=rho+1` and `D<3^h`. Therefore through `rho<=28`, at the first possible resonance `(46,29)`,

`D < 3^29 < 2^46+3^29`,

so **every single-excursion configuration through area 28 is analytically impossible**.

In multi-excursion area 26, the only genuinely new noncrossing size beyond the retained small tables would be area 19, appearing only in partition `19+7`; the unique area-7 crossing is `1 -> -1` and cannot be first from the allowed initial gaps nor last into terminal `-G 2^s`. Thus the earlier local tables suffice for multi-excursion structure.

The area-26 compressed search found:

- `G=8`: zero abstract near-resonant paths;
- `G=4`: 40 compressed candidates;
- 38 at `(46,29)`;
- 2 at the **new resonance** `(65,41)`.

Restoring the absolute numerator congruence eliminated all 40.

Exact area-26 session enumeration data:

- canonical excursions: `837,759,792`;
- integer-crossing excursions: `29,099`;
- `E(26)=112397/4374`;
- `C(26)=3631696/177147`.

This closed area 26 and moved the floor to `rho>=27`.

**Audit note:** the massive area-26 chunked enumerator/output was transient and is not retained in this bundle. RL42 should reconstruct and rerun this certificate before treating area 26 as independently reproducible.

### Area 27

Area 27 required the exact area-26 crossing table plus one special possible area-19 noncrossing branch. The latter (`G=8`, pattern `1+7+19`) was scanned over all `2,393,208` area-19 excursions and gave zero near-resonant solutions.

The complete compressed area-27 search then found:

- `G=8`: zero abstract near-resonant paths;
- `G=12`: zero abstract near-resonant paths;
- `G=4`: 66 abstract near-resonant paths;
- all 66 are at one of exactly two resonances: `(46,29)` or `(65,41)`;
- no third near-resonant exponent pair appears.

Absolute numerator congruences eliminated all 66.

Small modular witnesses were found:

`2^46-3^29 = 39409 * 44110909`,

and the factor

`44110909`

already eliminates all area-26/27 `(46,29)` candidates encountered in the session.

Also

`2^65-3^41 = 19 * 29 * 17021 * 44835377399`.

The single factor `17021` killed both area-26 `(65,41)` candidates, while at area 27 one residue survived modulo `17021`; the still-small combined modulus

`323399 = 19 * 17021`

eliminated every area-27 `(65,41)` candidate.

Therefore the completed session checkpoint is

> **`rho >= 28`.**

**Audit note:** as at area 26, the final large area-27 search/residue sources were not all retained. Reconstruct/rerun before calling this an artifact-audited theorem.

## New arithmetic landscape

The low-area machinery has exposed two genuine convergent-type bottlenecks:

1. `(46,29)`;
2. `(65,41)`.

Up through area 27, every abstract near-resonant survivor belongs to one of these two pairs. No third pair appeared.

This suggests the finite search is no longer encountering random combinatorial noise: it is resolving the Diophantine near-resonances inherent in the distortion identity.

## Strategic conclusion: do not make `rho>=29` the main goal

A fixed increase in the low-transport floor does **not** repair the asymptotic global packing coefficient. RL39's exact convex concentration extremizer remains the key obstruction.

The primary RL42 target should therefore be a scalable **distortion-versus-concentration bridge**.

A useful theorem would have one of the following forms:

1. **charge spread**

   `large rho => many owned odd states carry nontrivial RL39 charge`;

2. **per-state charge cap**

   actual excursion/gap geometry bounds the effective charge that one state can absorb;

3. **direct distortion coupling**

   a state with large `H` or large valuation multiplicity `l` necessarily contributes an excursion distortion `J_E` sufficiently far from 1 that the exact identity

   `prod_E J_E = z`, with `1<z<sqrt(16/15)`,

   forces compensating excursions, which in turn force charge spread;

4. **two-regime bridge**

   use the RL36 sparse relation

   `(X+Y)G = sum_{m=1}^rho epsilon_m 2^{i_m}3^{k_m}`

   to exclude `rho=o(L)`, and use an RL38/RL39 spread/distortion theorem for the complementary linear-transport regime.

The fourth route is especially attractive because it avoids asking one inequality to solve both sparse and dense transport.

## Recommended RL42 workflow

### Phase A — audit/reconstruct the finite certificate

1. Verify the inherited RL40 archive and rerun its verifiers.
2. Compile/run `stream_25_fast.cpp` and compare the printed exact counts/envelopes against `stream25_fast_stats.txt`.
3. Reconstruct the missing raw-table generator needed by `qmod_area24_alltargets.py`; `stream_25_repro.cpp` shows the intended `Q` columns, but writing all rows naively is slow and should be partitioned or streamed more carefully.
4. Reconstruct the area-25 absolute-residue verifier and confirm zero survivors for all 22 `(46,29)` targets.
5. Reconstruct the area-26 crossing enumeration in independent chunks. Confirm total `837,759,792`, crossing count `29,099`, `E(26)`, `C(26)`.
6. Reconstruct the area-26/27 compressed DP and full/small-modulus residue checks. Only after these pass should `rho>=28` be marked fully frozen.

Treat any discrepancy as a stop-and-repair event.

### Phase B — main bridge attack

Work on the RL38/RL39 overlap, not just another constant-area sweep.

Start from the exact RL39 one-state formula. Write the concentration extremizer explicitly for one sacrificial state and express that state's charge in the excursion variables that determine `J_E`. Seek an inequality connecting

- large `q = lH-alpha*l(l-1)/2`,
- local scaled gap / valuation multiplicity,
- and `|log J_E|`.

Then combine over excursions with

`sum_E log J_E = log z`,

where `0 < log z < (1/2)log(16/15)`.

The desired contradiction mechanism is:

`too much charge on one state -> too much local distortion -> compensating excursions -> additional charged owned states -> RL39 product saving`.

### Phase C — use finite search only as falsification support

Area 28 can be searched secondarily. Use it to test candidate bridge inequalities and to identify the next resonance, but do not let the project become an indefinite sequence `rho>=29`, `rho>=30`, ... unless a scalable pattern is extracted.

## Evidence discipline

- RL remains open.
- The full order-2 / `g=2` branch remains open.
- `rho>=18` is fully inherited and verifier-backed.
- `rho>=28` is the completed RL41 research checkpoint, but areas 26/27 need artifact reconstruction/rerun in RL42 because some transient source/data files were not retained.
- The external `R>=2^71` bound remains external where used.
- Older LMN dependencies elsewhere in the project remain external exactly as previously recorded.
