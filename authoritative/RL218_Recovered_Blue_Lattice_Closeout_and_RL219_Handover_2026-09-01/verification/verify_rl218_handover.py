#!/usr/bin/env python3
import json
from pathlib import Path
from itertools import product

ROOT = Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit("FAIL: " + msg)

state = json.loads((ROOT / "RL218_PROOF_STATE.json").read_text())
expected = {
    "completed_rl": 218,
    "incoming_rl": 219,
    "necessary_rank_count": 13415865871,
    "e16_h21_prefix_count": 45045,
    "e16_phase51_candidates": 139581280,
    "phase51_live_cylinders": 3132617,
    "phase51_max_2adic_precision_bits": 25,
    "e16_terminal_rank": 34124151203,
    "new_prefix_deletions": 0,
    "new_rank_exclusions": 0,
    "gate_a_global": "open",
    "gate_b_global": "open",
    "global_nontrivial_cycle_exclusion": "open",
}
for k,v in expected.items():
    if state.get(k) != v:
        fail(f"{k}: {state.get(k)!r} != {v!r}")

# Independent finite sanity check of the promoted raw-word algebra:
# formula + terminal congruence iff stepwise legality, for small exhaustive words/seeds.
def apply_stepwise(seed, word):
    y = seed
    for ch in word:
        if ch == "D":
            y = 2*y
        else:
            if y % 3 != 2:
                return None
            y = (2*y - 1)//3
    return y

def formula(seed, word):
    C = 0
    h = 0
    for ch in word:
        if ch == "D":
            C = 2*C
        else:
            C = 2*C + 3**h
            h += 1
    num = (2**len(word))*seed - C
    legal_terminal = num % (3**h) == 0
    value = num // (3**h) if legal_terminal else None
    return legal_terminal, value

for n in range(0,8):
    for word_tuple in product("DO", repeat=n):
        word = "".join(word_tuple)
        for seed in range(1,80):
            step = apply_stepwise(seed, word)
            legal, value = formula(seed, word)
            if legal != (step is not None):
                fail(f"terminal-legality mismatch seed={seed} word={word}")
            if legal and value != step:
                fail(f"normal-form mismatch seed={seed} word={word}")

# Verify the inherited counts partition correctly.
if state["state011_survivors"] + state["state111_survivors"] != state["e16_phase51_candidates"]:
    fail("state counts do not partition e16 candidates")
if sum(state["mod18_survivors"].values()) != state["e16_phase51_candidates"]:
    fail("mod18 counts do not partition e16 candidates")

# Ensure the two recovered bounded results are explicitly non-deleting and the
# unfinished forward-floor work remains outside promotion.
if len(state.get("new_exact_bounded_results", [])) != 2:
    fail("expected two recovered bounded results")
if any(x.get("candidate_deletions") != 0 for x in state["new_exact_bounded_results"]):
    fail("bounded results unexpectedly claim deletions")
if not any("forward-floor" in x for x in state.get("not_promoted", [])):
    fail("forward-floor incomplete work not marked NOT PROMOTED")

print("RL218 corrected handover verifier: PASS")
print("analytic raw-word algebra finite sanity suite: PASS")
print("frontier/count consistency: PASS")
print("recovered bounded-result scope locks: PASS")
