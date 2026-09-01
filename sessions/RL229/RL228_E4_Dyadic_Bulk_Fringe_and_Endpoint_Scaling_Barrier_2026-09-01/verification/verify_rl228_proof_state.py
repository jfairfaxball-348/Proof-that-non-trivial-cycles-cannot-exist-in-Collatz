#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=json.loads((root/'RL228_PROOF_STATE.json').read_text())
assert p['completed_rl']==228 and p['incoming_rl']==229 and p['incoming_rl_started'] is False
assert p['necessary_rank_count']==13415865870
assert p['e4_terminal_rank']==31435476727 and p['e4_terminal_rank_excluded'] is False
assert p['e4_combined_survivors_through_transition_43']==3856660232
assert p['e4_phase_44_state_count']==7743281
assert p['transition_44_failure_modulus']==1<<33
assert p['bulk_coefficient_transition_44']==0
assert p['transition_44_deletion_count_promoted'] is False
assert p['success_class']=='C_decisive_barrier'
assert p['all_possible_compressors_ruled_out'] is False
assert p['primary_next_route']=='physical_h21_incidence_and_exhaustive_charge'
assert p['physical_h21_incidence_proved'] is False and p['h21_charge_proved'] is False
assert p['gate_a_global']=='open' and p['gate_b_global']=='open'
assert p['global_nontrivial_cycle_exclusion']=='open'
print('RL228 PROOF STATE AND SCOPE LOCKS: PASS')
print('frontier 13415865870; e4 rank remains live')
print('combined e4 survivors certified through transition43 3856660232')
print('success C endpoint-scaling barrier; RL229 physical H21 incidence/charge')
