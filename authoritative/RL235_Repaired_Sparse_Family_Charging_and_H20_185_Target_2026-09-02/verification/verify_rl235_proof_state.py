#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
s=json.loads((root/'RL235_PROOF_STATE.json').read_text())
assert s['completed_rl']==235
assert s['classification']=='Success B'
assert s['incoming_rl']==236 and s['incoming_status']=='NOT STARTED'
assert s['ordinary_abs_corrected_flow_gt']==712
assert s['signed_corrected_flow_each_gt']==356
assert s['directional_K_variation_each_gt']==118
assert s['full_prefix_atomic_cells']==7531
assert s['generic_budget_overages']==13
assert s['h21_spacing_ge']==1001 and s['h21_occurrence_cap']==137390654
assert s['next_h20_incidence_cap_le']==746997478
assert s['next_h20_spacing_sufficient']==185
assert s['frontier']==13415865870
assert s['e4_rank']==31435476727
assert s['e4_survivors_through_transition_43']==3856660232
assert s['sole_high_branch']==[37,0,23,-1]
assert s['gate_A']==s['gate_B']==s['global_nontrivial_cycle_exclusion']=='open'
assert s['old_H17_1615_target']=='demoted'
assert s['old_H17_spacing_85103989']=='demoted'
assert s['knowledge_catalogues']=='stale/deferred'
summary=json.loads((root/'RL235_EXACT_CERTIFICATE_SUMMARY.json').read_text())
assert summary['cell_count']==7531
assert summary['RL234_H20_blocker']['spacing_184_sufficient'] is False
assert summary['RL234_H20_blocker']['spacing_185_sufficient'] is True
print('PASS: RL235 proof-state and successor guard')
print('completed_rl=235 incoming_rl=236 classification=Success B')
print('frontier=13415865870 e4_rank=31435476727 survivors=3856660232')
print('Gates=open old_H17_targets=demoted knowledge_catalogues=stale/deferred')
