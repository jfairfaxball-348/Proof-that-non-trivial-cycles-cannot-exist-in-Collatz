#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'RL217_PROOF_STATE.json').read_text())
cert=json.loads((ROOT/'certificates/verify_rl217_prefix_wide_height_automaton_output.json').read_text())
transport=json.loads((ROOT/'transport/INHERITED_GIT_OBJECTS.json').read_text())
assert state['format']=='rl217-proof-state-v1'
assert state['completed_rl']==217 and state['incoming_rl']==218
assert state['base_head']=='7122546103d4631e79bdd3ffac7289e6aaab2eac'
assert state['incoming_authoritative_tree']=='aa82e4ce1466ee1649f4117411e6b3b1b37ab806'
assert state['necessary_rank_count']==13_415_865_871
assert state['targeted_e16_candidates_after_rl216']==331_927_916
assert state['targeted_e16_candidates_after_rl217']==139_581_280
assert state['arithmetic_candidates_removed_vs_rl216']==192_346_636
assert state['e16_h21_prefix_count']==45_045 and state['prefixes_deleted_rl217']==0
assert state['state011_candidate_count']==90_749_885
assert state['state111_candidate_count']==48_831_395
assert state['surviving_mod18_candidate_counts']=={'0':35_622_831,'8':19_167_422,'9':55_127_054,'17':29_663_973}
assert state['e16_reachable_eta_mod2187']==469
assert state['new_rank_exclusions']==0 and state['e16_terminal_rank']==34_124_151_203
assert state['physical_h21_incidence_proved'] is False
assert state['h21_charge_proved'] is False and state['branch_contradiction_proved'] is False
assert state['gate_a_global']=='open' and state['gate_b_global']=='open'
assert state['global_nontrivial_cycle_exclusion']=='open'
assert state['quotient_residue_determined'] is False
assert cert['rl217_candidates_surviving_through_phase51']==state['targeted_e16_candidates_after_rl217']
assert cert['rl217_candidates_removed_through_phase51']==state['arithmetic_candidates_removed_vs_rl216']
assert cert['universal_live_cylinders']==state['universal_live_cylinders']
assert cert['frontier']==state['necessary_rank_count']
assert transport['base_head']==state['base_head']
assert transport['incoming_authoritative_tree']==state['incoming_authoritative_tree']
assert transport['freeze_session_path']=='sessions/RL216'
assert transport['successor_completed_rl']==217 and transport['successor_incoming_rl']==218
targets=list(ROOT.glob('RL218_*_TARGET.md'))
assert len(targets)==1 and targets[0].name=='RL218_CERTIFIED_BLUE_LATTICE_RECOGNITION_EXPLORATION_TARGET.md'
target=targets[0].read_text()
for phrase in ['RL80/RL81','arbitrary backward closure','density','proximity','3*2^58 k','exact recognition system','Do **not** naively enumerate']:
    assert phrase in target, phrase
start=(ROOT/'START_HERE.md').read_text()
assert 'RL218 incoming authoritative state' in start
assert '139,581,280' in start and '3,132,617' in start
print('PASS RL217 proof-state, successor blue-route locks, transport pins and scope controls')
