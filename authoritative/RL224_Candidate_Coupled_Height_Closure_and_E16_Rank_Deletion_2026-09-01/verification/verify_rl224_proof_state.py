#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
s=json.loads((ROOT/'RL224_PROOF_STATE.json').read_text())
assert s['format']=='rl224-proof-state-v1'
assert s['completed_rl']==224 and s['incoming_rl']==225 and s['incoming_rl_started'] is False
assert s['research_base_head']=='7eacfbe28d424f747e4f1dbd81f3821b69a038eb'
assert s['incoming_authoritative_tree']=='db779d8d868f6a1f9656b3270b661fdfb0dbf74c'
assert s['inherited_necessary_rank_count']==13_415_865_871
assert s['necessary_rank_count']==13_415_865_870
assert s['above_p_source_necessary_count']==7_091_831_283
assert s['below_p_source_necessary_count']==6_324_034_587
assert s['inherited_e16_phase51_candidates']==139_581_280
assert s['e16_final_candidates']==0 and s['e16_final_prefixes']==0
assert s['e16_terminal_rank']==34_124_151_203 and s['e16_terminal_rank_excluded'] is True
assert s['new_rank_exclusions']==1 and s['new_candidate_deletions']==139_581_280 and s['new_prefix_deletions']==45_045
assert s['gate_a_global']==s['gate_b_global']=='open'
assert s['branch_contradiction_proved'] is False and s['global_nontrivial_cycle_exclusion']=='open'
assert s['physical_h21_incidence_proved'] is False and s['h21_charge_proved'] is False
assert s['knowledge_catalogue']=='stale/deferred'
targets=list(ROOT.glob('*TARGET*.md'))
assert [p.name for p in targets]==['RL225_REMAINING_SMALL_OFFSET_CANDIDATE_COUPLED_HEIGHT_TRANSFER_TARGET.md']
assert 'NOT STARTED' in targets[0].read_text()
print('RL224 PROOF STATE AND SCOPE LOCKS: PASS')
print('rank frontier 13415865871 -> 13415865870; e16 rank 34124151203 excluded')
print('gates=open/open global=open physical-incidence=false')
