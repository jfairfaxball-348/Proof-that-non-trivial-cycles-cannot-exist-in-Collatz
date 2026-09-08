# RL282 post-promotion correction — exact H<=22 checkpoint certificate

Date: 2026-09-08
Correction type: proof-state coverage repair
Original promoted commit: `4971b39282a4ba6f949d9fbb05624eb00cffc70b`

## Reason for correction

The RL282 closeout deliberately left the multi-million-state height-capped exploration unpromoted because its closeout fast suite did not reproduce that computation. That was too conservative for the already-completed `H<=22` portion.

The exact `H<=22` positive-checkpoint automaton has now been independently reconstructed from the normalized `(d,J,H)` recurrence, packaged as a portable deterministic verifier, rerun cleanly, and red-teamed. It is therefore promoted here as an **exact finite certificate**.

This correction does not amend the published RL282 commit and does not retract or alter any RL282 analytic theorem. It adds a post-promotion supplement and corrects the prepared RL283 handover.

The exploratory `H=23..26` work remains **unpromoted evidence**.

## Corrected subordinate classifications

Add:

- `HEIGHT_22_POSITIVE_CHECKPOINT_AUTOMATON_CERTIFIED`
- `K5_TO_K23_GATE_A_CASES_CLOSED_CERTIFIED`

These are exact finite certificate classifications, not uniform analytic theorems.

## Exact automaton

Height cap:

`R=22`.

### Phase A — before first positive d=1 state

Start from the canonical normalized initial state

`(d,J,H)=(1,-13,0)`.

Perform exhaustive BFS over both legal selector bits `x in {0,1}` using the exact normalized transition. Discard only transitions with `H>22`.

When a branch first reaches a positive `d=1` state, record that `(J,H)` as a positive-phase entry and stop the nonpositive BFS along that branch.

No `J` cutoff is used.

Exact results:

- nonpositive states visited: `3,254,996`;
- legal in-cap edges examined: `3,813,525`;
- distinct first-positive `(H,J)` entries: `169`.

### Phase B — positive d=1 checkpoint automaton

Positive even `d=1` states are checkpoints.

From an even checkpoint, the only legal boundary launch is `x=0`, which enters `d=2` at zero added height. Enumerate every exact first return to `d=1` whose added height stays within the remaining cap.

After launch and before first return, `d>=2`, so every interior step adds at least one unit of height. Therefore the height cap makes each first-return tree finite without any arbitrary word-length bound.

For a positive odd `d=1` return, exactly one boundary branch stays odd and exactly one exits to a positive even checkpoint. Follow the unique stay-odd branch and collect every even exit until the odd state repeats exactly. This quotients the complete zero-height boundary continuation.

No boundary-orbit length cutoff and no `J` cutoff are used. Every odd origin encountered by the certified run closes by exact repetition.

Exact results:

- positive even checkpoint states `(J,H)`: `146,341`;
- distinct odd boundary origins macro-closed: `13,583`;
- maximum exact stay-odd trace before repetition: `263`.

## Power-of-two terminal results

The complete checkpoint set for `H<=22` has power-of-two minima

- `k=1  -> H_min=3`;
- `k=3  -> H_min=3`;
- `k=5  -> H_min=9`;
- `k=7  -> H_min=15`;
- `k=9  -> H_min=15`;
- `k=11 -> H_min=18`;
- `k=13 -> H_min=18`;
- `k=15 -> H_min=22`.

No checkpoint with

`J in {2^17,2^19,2^21,2^23}`

occurs anywhere under `H<=22`.

Therefore every odd terminal exponent

`k in {5,7,9,11,13,15,17,19,21,23}`

is Gate-A safe:

- for `k<=15`, the exact minimum satisfies `H_min>=k`;
- for `k=17,19,21,23`, any Gate-A violator would have `H<k<=23`, hence `H<=22`, but no such terminal occurs in the complete cap.

Combining this finite certificate with RL281's analytic theorem that terminal `k` is odd and its analytic closure of `k=3`, the corrected live Gate-A residual is

`k>=25`, `k` odd, `H_can<k`.

## Scope limits

This certificate does **not** prove:

- a uniform theorem `H_can>=k`;
- `nu_2(J)<=H` for all reachable positive checkpoints;
- `J<=2^H`;
- anything from the exploratory `H=23..26` scratch search;
- Gate B;
- a fifth-selector result;
- Radius 6+;
- global non-trivial-cycle exclusion.

RL282's terminal-backward/local-tail barrier remains fully in force: final-tail 3-adic arithmetic and the existing positive mass/`F` budgets cannot alone close the remaining cases.

## Verification

Portable verifier:

`verification/verify_rl282_height22_checkpoint.py`

Recorded deterministic stdout:

`verification/RL282_HEIGHT22_CHECKPOINT_OUTPUT.txt`

The verifier was run twice from the frozen candidate bytes and produced byte-identical stdout with exit status `0`.

The certificate has no arbitrary state-value or word-length cutoff. Its only mathematical truncation is the explicitly promoted height cap `H<=22`.

## Handover correction

The prepared RL283 target must inherit

`k>=25`, `k` odd, `H_can<k`

rather than the superseded `k>=5` residual.

RL283's research mission is otherwise unchanged: attack upstream global positive-checkpoint reachability versus accumulated height, preferably via `nu_2(J)<=H` or the minimal strengthened invariant needed to obtain the same terminal consequence.
