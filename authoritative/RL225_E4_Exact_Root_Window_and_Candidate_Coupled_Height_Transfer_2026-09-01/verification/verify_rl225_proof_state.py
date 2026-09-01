#!/usr/bin/env python3
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent.parent
s=json.loads((HERE/'RL225_PROOF_STATE.json').read_text())
c=json.loads((HERE/'certificates'/'rl225_e4_transfer_summary.json').read_text())
assert s['completed_rl']==225 and s['incoming_rl']==226 and s['incoming_rl_started'] is False
assert s['necessary_rank_count']==13415865870
assert s['above_p_source_necessary_count']==7091831283
assert s['below_p_source_necessary_count']==6324034587
assert s['e4_terminal_rank']==c['e4_terminal_rank']==31435476727
assert s['e4_terminal_rank_excluded'] is False and c['rank_deleted'] is False
assert s['e4_raw_candidates']==c['raw_candidates']==3863379575
assert s['e4_terminal_hensel_deletions']==c['terminal_hensel_deletions']==1842
assert s['e4_height_deletions_through_transition_41']==c['height_deletions_through_transition_41']==1988460
assert s['e4_combined_survivors']==c['combined_survivors']==3861389273
assert s['new_rank_exclusions']==0
assert s['gate_a_global']=='open' and s['gate_b_global']=='open'
assert s['global_nontrivial_cycle_exclusion']=='open'
print('RL225 proof-state verifier: PASS')
