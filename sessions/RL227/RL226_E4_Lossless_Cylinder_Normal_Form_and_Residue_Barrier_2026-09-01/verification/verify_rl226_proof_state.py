#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'RL226_PROOF_STATE.json'
s=json.loads(p.read_text())
assert s['completed_rl']==226 and s['incoming_rl']==227 and s['incoming_rl_started'] is False
assert s['necessary_rank_count']==13415865870
assert s['above_p_source_necessary_count']==7091831283 and s['below_p_source_necessary_count']==6324034587
assert s['e4_terminal_rank']==31435476727 and s['e4_terminal_rank_excluded'] is False
assert s['e4_raw_candidates']==3863379575
assert s['e4_height_deletions_through_transition_43']==6717501
assert s['e4_height_survivors_through_transition_43']==3856662074
assert s['e4_terminal_hensel_deletions']==1842
assert s['e4_terminal_height_overlap_through_transition_43']==0
assert s['e4_combined_survivors']==3856660232
assert s['lossless_compressed_state']==['phase','residue','precision','intercept']
assert s['naive_phase_precision_merge_lossless'] is False
assert s['residue_intercept_required_for_exact_window'] is True
assert s['gate_a_global']=='open' and s['gate_b_global']=='open' and s['global_nontrivial_cycle_exclusion']=='open'
print('RL226 PROOF STATE AND SCOPE LOCKS: PASS')
print('rank frontier unchanged 13415865870; e4 rank 31435476727 remains live')
print('e4 combined survivors through transition43 3856660232')
