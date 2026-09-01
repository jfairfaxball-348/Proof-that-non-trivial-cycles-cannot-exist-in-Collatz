#!/usr/bin/env python3
import hashlib, json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'RL208_PROOF_STATE.json').read_text())
out=json.loads((ROOT/'certificates/verify_rl208_layered_root_cone_output.json').read_text())
trans=json.loads((ROOT/'transport/INHERITED_GIT_OBJECTS.json').read_text())
assert state['completed_rl']==208 and state['incoming_rl']==209
assert state['new_rank_exclusions']==2_765_120_323
assert state['necessary_rank_count']==13_423_606_911
assert state['above_p_source_necessary_count']==7_099_572_324
assert state['below_p_source_necessary_count']==6_324_034_587
assert out['status']=='PASS'
assert out['new_rank_exclusions']==state['new_rank_exclusions']
assert out['remaining_necessary_rank_count']==state['necessary_rank_count']
assert out['above_p_source_necessary_after']==state['above_p_source_necessary_count']
assert out['below_p_source_necessary_after']==state['below_p_source_necessary_count']
assert out['coordinate_swapped_rectangle_recount']=='PASS'
assert out['discrete_preexisting_deletion_hits_in_new_layers']==0
assert out['common_radius_saturation_at_N']==2**35
assert out['common_radius_saturation_band']==[25_583_192_106,41_775_866_136]
assert state['eta_classes_mod18']==[0,8,9,17]
assert state['gate_a_global']==state['gate_b_global']==state['global_nontrivial_cycle_exclusion']=='open'
assert state['new_corrections_or_demotions']==[]
assert trans['base_head']==state['base_head']
assert trans['incoming_authoritative_tree']==state['incoming_authoritative_tree']
# Unique successor target in overlay.
targets=list(ROOT.glob('*TARGET*.md'))
assert [p.name for p in targets]==['RL209_H21_ABOVE_P_INDEPENDENT_CONSUMER_TARGET.md']
text=(ROOT/'RL208_CERTIFIED_FACTS_AND_PROOF_LEDGER.md').read_text()
for needle in ['2,765,120,323','13,423,606,911','7,099,572,324','6,324,034,587','Gate A globally open','Gate B globally open']:
    assert needle in text
corr=(ROOT/'RL208_CORRECTION_DEMOTION_LEDGER.md').read_text()
assert 'No new RL208 correction or demotion' in corr and '37' in corr and '60' in corr and '97' in corr
start=(ROOT/'START_HERE.md').read_text()
assert 'RL209 incoming authoritative state' in start and '13,423,606,911' in start
print('PASS RL208 proof-state, successor uniqueness, transport identities and scope locks')
