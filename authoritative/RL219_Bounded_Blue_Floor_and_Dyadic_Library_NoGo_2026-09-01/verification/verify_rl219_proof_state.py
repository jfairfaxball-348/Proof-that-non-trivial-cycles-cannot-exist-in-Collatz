#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ps=json.loads((ROOT/'RL219_PROOF_STATE.json').read_text())
cert=json.loads((ROOT/'certificates/verify_rl219_bounded_blue_floor_output.json').read_text())
assert ps['completed_rl']==219 and ps['incoming_rl']==220
assert ps['necessary_rank_count']==13_415_865_871
assert ps['e16_h21_prefix_count']==45_045
assert ps['e16_phase51_candidates']==139_581_280
assert ps['phase51_live_cylinders']==3_132_617
assert ps['phase51_max_2adic_precision_bits']==25
assert ps['phase51_survivor_digest_sha256']=='abf94388354f55d34ae35370e3bcbcd2086da2f6053035840c0a9f68665e8d05'
assert ps['new_candidate_deletions']==0 and ps['new_prefix_deletions']==0 and ps['new_rank_exclusions']==0
assert ps['gate_a_global']=='open' and ps['gate_b_global']=='open' and ps['global_nontrivial_cycle_exclusion']=='open'
assert ps['physical_shortcut_floor']==cert['certified_physical_shortcut_floor']
assert ps['phase16_minimum_odd_state_superset']==cert['minimum_phase16_odd_state_over_superset']
assert ps['root_lower_bound_integer']==cert['root_lower_bound_integer']
assert ps['root_upper_bound_integer']==cert['root_upper_bound_integer']
assert ps['stable_external_collatz_verification_upper']==cert['stable_external_verified_interval_upper']==1<<71
assert ps['root_upper_bound_integer'] < 2*ps['root_lower_bound_integer']
# Unique successor target and explicit hard locks.
targets=list(ROOT.glob('*TARGET*.md'))
assert len(targets)==1 and targets[0].name=='RL220_UNBOUNDED_CERTIFIED_BLUE_FAMILY_ALIGNMENT_TARGET.md'
ledger=(ROOT/'RL219_CORRECTION_DEMOTION_LEDGER.md').read_text()
assert 'None.' in ledger
assert 'externally inherited computation' in ledger
assert 'finite seed set and finite library' in ledger
report=(ROOT/'RL219_RED_TEAM_REPORT_2026-09-01.md').read_text()
assert 'Zero candidate/rank deletions' in report or 'Zero candidate/rank' in report
assert 'No correction or demotion is required.' in report
print('PASS RL219 proof-state, scope locks, and unique RL220 target')
print('completed=219 incoming=220 candidates=139581280 frontier=13415865871')
print('candidate_deletions=0 rank_deletions=0 gates=open/open')
