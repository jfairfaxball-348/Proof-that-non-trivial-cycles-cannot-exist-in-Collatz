#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=json.loads((ROOT/'RL230_PROOF_STATE.json').read_text())

assert p['format']=='rl230-proof-state-v1'
assert p['completed_rl']==230
assert p['success_class']=='C'
assert p['incoming_rl']==231
assert p['incoming_rl_started'] is False
assert p['necessary_rank_count']==13_415_865_870
assert p['e4_terminal_rank']==31_435_476_727
assert p['e4_terminal_rank_excluded'] is False
assert p['e4_combined_survivors_through_transition_43']==3_856_660_232
assert p['new_distinct_physical_nonzero_defect_floor']==813_958_704
assert p['k_corridor_full_width']==18_713_911_838
assert p['arbitrary_boundary_one_pass_flow_threshold_strictly_greater_than']==56_141_735_514
assert p['minimum_nearly_unit_same_sign_defects_for_that_route']==56_141_735_515
assert p['shallow_population_required_by_optimistic_one_pass_model']==96_834_890_414
assert p['branch_contradiction_proved'] is False
assert p['gate_a_global']=='open'
assert p['gate_b_global']=='open'
assert p['global_nontrivial_cycle_exclusion']=='open'
assert p['knowledge_catalogue']=='stale/deferred'

print('RL230 PROOF STATE AND SCOPE LOCKS: PASS')
print('frontier 13415865870; e4 live with 3856660232 combined survivors')
print('distinct physical nonzero-defect floor 813958704')
print('no branch contradiction; Gate A/B and global exclusion remain open')
