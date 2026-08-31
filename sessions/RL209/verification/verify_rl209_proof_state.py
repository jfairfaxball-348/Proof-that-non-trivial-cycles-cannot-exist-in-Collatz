#!/usr/bin/env python3
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'RL209_PROOF_STATE.json').read_text())
out=json.loads((ROOT/'certificates/verify_rl209_pointwise_root_cone_output.json').read_text())
trans=json.loads((ROOT/'transport/INHERITED_GIT_OBJECTS.json').read_text())
assert state['completed_rl']==209 and state['incoming_rl']==210
assert state['base_head']=='a080622ce3d020c249b71c8b12552361601810de'
assert state['incoming_authoritative_tree']=='159e625b25c7cd9aadf6f53f03e0a63643906c32'
assert state['new_rank_exclusions']==7_741_040
assert state['inherited_necessary_rank_count']==13_423_606_911
assert state['necessary_rank_count']==13_415_865_871
assert state['above_p_source_necessary_count']==7_091_831_284
assert state['below_p_source_necessary_count']==6_324_034_587
assert state['old_backward_root_pointwise_remaining']==986
assert state['signed_successor_pairs_checked']==41_412
assert out['status']=='PASS'
assert out['new_above_p_rank_exclusions']==state['new_rank_exclusions']
assert out['incoming_total_count']==state['inherited_necessary_rank_count']
assert out['remaining_total_count']==state['necessary_rank_count']
assert out['remaining_above_p_count']==state['above_p_source_necessary_count']
assert out['below_p_count_unchanged']==state['below_p_source_necessary_count']
assert out['old_backward_root_pointwise_remaining']==state['old_backward_root_pointwise_remaining']
assert out['signed_successor_pairs_checked_on_root_remaining']==state['signed_successor_pairs_checked']
assert out['preexisting_discrete_deletion_hits']==0
assert out['eta_classes_removed']==0 and not out['sign_or_valuation_selected']
assert state['eta_classes_mod18']==[0,8,9,17]
assert state['corrected_below_p']=={'source_offset':37,'root_prefix_depth':60,'root_normalization_depth':97}
assert state['new_corrections_or_demotions']==[]
assert not state['independent_eta_selection_proved']
assert not state['physical_h21_incidence_proved'] and not state['h21_charge_proved']
assert not state['branch_contradiction_proved']
assert state['gate_a_global']==state['gate_b_global']==state['global_nontrivial_cycle_exclusion']=='open'
assert trans['base_head']==state['base_head']
assert trans['incoming_authoritative_tree']==state['incoming_authoritative_tree']
assert trans['freeze_session_path']=='sessions/RL208'
targets=sorted(p.name for p in ROOT.glob('*TARGET*.md'))
assert targets==['RL210_H21_ABOVE_P_PREFIX_CANCELLATION_AND_GLOBAL_SELECTOR_TARGET.md']
start=(ROOT/'START_HERE.md').read_text()
assert 'RL210 incoming authoritative state' in start and '13,415,865,871' in start
ledger=(ROOT/'RL209_CERTIFIED_FACTS_AND_PROOF_LEDGER.md').read_text()
for needle in ['7,741,040','13,415,865,871','7,091,831,284','6,324,034,587','Gate A globally open','Gate B globally open']:
    assert needle in ledger
corr=(ROOT/'RL209_CORRECTION_DEMOTION_LEDGER.md').read_text()
assert 'No new RL209 correction or demotion' in corr and '37' in corr and '60' in corr and '97' in corr
print('PASS RL209 proof-state, successor uniqueness, transport identities and scope locks')
