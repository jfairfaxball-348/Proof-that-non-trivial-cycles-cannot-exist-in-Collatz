#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
state=json.loads((ROOT/'RL213_PROOF_STATE.json').read_text())
out=json.loads((ROOT/'certificates/verify_rl213_global_consumer_barriers_output.json').read_text())
trans=json.loads((ROOT/'transport/INHERITED_GIT_OBJECTS.json').read_text())

assert state['completed_rl']==213 and state['incoming_rl']==214
assert state['base_head']=='3120105163bbcad7f14186db4499514dfd216cab'
assert state['incoming_authoritative_tree']=='0eabe22e53e170eaaa8b6ff8ef2149f17356f739'
assert state['necessary_rank_count']==13_415_865_871
assert state['new_rank_exclusions']==0
assert state['endpoint_moment_e16_collapses_to_root_telescope'] is True
assert state['g56_first_divergence_start_cases']==304
assert state['g56_feasible_start_cases']==303
assert state['g56_only_infeasible_case']=='m24-root-smaller-k38-inherited-RL210'
assert state['e16_h21_reachable_mod2187']==469 and state['e16_h21_universe_mod2187']==486
assert state['e16_forbidden_eta_mod2187']==[0,53,431,891,917,972,1160,1295,1458,1493,1565,1620,1701,1862,2060,2088,2106]
assert state['physical_h21_incidence_proved'] is False
assert state['h21_charge_proved'] is False
assert state['state_selected'] is False and state['terminal_parity_selected'] is False
assert state['gate_a_global']=='open' and state['gate_b_global']=='open'
assert state['global_nontrivial_cycle_exclusion']=='open'

assert out['status']=='PASS'
assert out['endpoint_moment_e16_collapses_to_root_telescope'] is True
assert out['g56_first_divergence_start_cases']==304
assert out['g56_feasible_start_cases']==303
assert out['new_rank_exclusions']==0 and out['frontier']==13_415_865_871
assert out['witness_digest_sha256']=='dd7dc63df94e0360f556fa255fea04e75463f8502f57588e051b49b081be2c5a'

assert trans['base_head']==state['base_head']
assert trans['incoming_authoritative_tree']==state['incoming_authoritative_tree']
assert trans['freeze_session_path']=='sessions/RL212'
assert trans['successor_completed_rl']==213 and trans['successor_incoming_rl']==214

targets=sorted(p.name for p in ROOT.glob('*TARGET*.md'))
assert targets==['RL214_H21_E16_DISCRETE_OWNERSHIP_QUOTIENT_TARGET.md']

print('PASS RL213 proof-state, successor uniqueness, transport pins and scope locks')
