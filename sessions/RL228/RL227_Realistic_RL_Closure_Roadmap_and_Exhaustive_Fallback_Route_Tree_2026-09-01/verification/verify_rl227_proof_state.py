#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
s=json.loads((root/'RL227_PROOF_STATE.json').read_text())
assert s['completed_rl']==227 and s['incoming_rl']==228 and s['incoming_rl_started'] is False
assert s['necessary_rank_count']==13415865870
assert s['above_p_source_necessary_count']==7091831283
assert s['below_p_source_necessary_count']==6324034587
assert s['e16_terminal_rank_excluded'] is True
assert s['e4_terminal_rank']==31435476727 and s['e4_terminal_rank_excluded'] is False
assert s['e4_combined_survivors_through_transition_43']==3856660232
assert s['new_mathematical_theorems']==0 and s['new_exact_rank_certificates']==0 and s['new_rank_exclusions']==0
assert s['retained_rl_closure_condition']=='gate_a_and_gate_b_or_stronger_direct_bypass'
assert s['physical_h21_incidence_proved'] is False and s['h21_charge_proved'] is False
assert s['gate_a_global']=='open' and s['gate_b_global']=='open'
assert s['global_nontrivial_cycle_exclusion']=='open'
assert s['raw_transition_increment_sufficient_closeout'] is False
assert s['terminal_fallback']=='SYNTHESISE NEW SOLUTIONS'
print('RL227 PROOF STATE AND SCOPE LOCKS: PASS')
print('frontier 13415865870; e4 rank remains live with 3856660232 combined survivors')
print('no new theorem/rank exclusion; Gate A, Gate B, global exclusion remain open')
