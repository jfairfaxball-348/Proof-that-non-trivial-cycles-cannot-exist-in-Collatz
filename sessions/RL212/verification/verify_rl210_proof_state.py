#!/usr/bin/env python3
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'RL210_PROOF_STATE.json').read_text())
out=json.loads((ROOT/'certificates/verify_rl210_global_prefix_overlap_output.json').read_text())
trans=json.loads((ROOT/'transport/INHERITED_GIT_OBJECTS.json').read_text())
assert state['completed_rl']==210 and state['incoming_rl']==211
assert state['base_head']=='3412fc6b8fefa2a5eba4626dc3dd73a6322739b5'
assert state['incoming_authoritative_tree']=='c918e8f1fdf4b0e30daf24c3af84ffd75c8d575a'
assert state['new_rank_exclusions']==0
assert state['inherited_necessary_rank_count']==13_415_865_871
assert state['necessary_rank_count']==13_415_865_871
assert state['above_p_source_necessary_count']==7_091_831_284
assert state['below_p_source_necessary_count']==6_324_034_587
assert state['above_p_e_lt_56_count']==6
assert state['above_p_e_ge_56_count']==7_091_831_278
assert state['small_offset_sources']==[4,16,28,33,40,45]
assert state['locked_small_offsets']==[4,16]
assert state['global_prefix_selector_proved']
assert (state['first_mismatch_index_min'],state['first_mismatch_index_max'])==(24,37)
assert state['first_mismatch_smaller_exponent']==37
assert state['m24_root_smaller_orientation_excluded']
assert out['status']=='PASS'
assert out['new_rank_exclusions']==0
assert out['current_total_count']==state['necessary_rank_count']
assert out['current_above_p_count']==state['above_p_source_necessary_count']
assert out['current_below_p_count']==state['below_p_source_necessary_count']
assert out['small_offset_count']==state['above_p_e_lt_56_count']
assert out['above_p_e_ge_56_count']==state['above_p_e_ge_56_count']
assert [x['e'] for x in out['small_offset_current_necessary_sources']]==state['small_offset_sources']
assert out['locked_offsets']==state['locked_small_offsets']
assert state['eta_classes_mod18']==[0,8,9,17]
assert state['corrected_below_p']=={'source_offset':37,'root_prefix_depth':60,'root_normalization_depth':97}
assert state['new_corrections_or_demotions']==[]
assert not state['independent_eta_selection_proved']
assert not state['physical_h21_incidence_proved'] and not state['h21_charge_proved']
assert not state['branch_contradiction_proved']
assert state['gate_a_global']==state['gate_b_global']==state['global_nontrivial_cycle_exclusion']=='open'
assert trans['base_head']==state['base_head']
assert trans['incoming_authoritative_tree']==state['incoming_authoritative_tree']
assert trans['freeze_session_path']=='sessions/RL209'
targets=sorted(p.name for p in ROOT.glob('*TARGET*.md'))
assert targets==['RL211_H21_GLOBAL_PREFIX_CASES_AND_ABSOLUTE_CLOSURE_TARGET.md']
start=(ROOT/'START_HERE.md').read_text()
assert 'RL211 incoming authoritative state' in start and '13,415,865,871' in start
ledger=(ROOT/'RL210_CERTIFIED_FACTS_AND_PROOF_LEDGER.md').read_text()
for needle in ['7,091,831,278','24<=m<=37','13,415,865,871','Gate A globally open','Gate B globally open']:
    assert needle in ledger
corr=(ROOT/'RL210_CORRECTION_DEMOTION_LEDGER.md').read_text()
assert 'No new RL210 correction or demotion' in corr and '37' in corr and '60' in corr and '97' in corr
print('PASS RL210 proof-state, successor uniqueness, transport identities and scope locks')
