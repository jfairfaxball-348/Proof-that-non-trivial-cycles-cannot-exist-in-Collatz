#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=json.loads((root/'RL229_PROOF_STATE.json').read_text())
assert p['completed_rl']==229 and p['incoming_rl']==230 and p['incoming_rl_started'] is False
assert p['necessary_rank_count']==13_415_865_870
assert p['e16_terminal_rank']==34_124_151_203 and p['e16_terminal_rank_excluded'] is True
assert p['e4_terminal_rank']==31_435_476_727 and p['e4_terminal_rank_excluded'] is False
assert p['e4_combined_survivors_through_transition_43']==3_856_660_232
assert p['dangerous_h21_rank_core']==[23_369_453_298,41_775_866_136]
assert p['rank_blind_charge_barrier_proved'] is True
assert p['current_h21_charge_rank_sensitive'] is False
assert p['physical_h21_incidence_proved'] is False
assert p['h21_exhaustive_charge_bridge_proved'] is False
assert p['family_wide_dangerous_h21_exclusion_proved'] is False
assert p['new_rank_exclusions']==0
assert p['success_class']=='C_decisive_barrier'
assert p['primary_next_route']=='owned_macro_defect_block_and_strict_excursion_high_branch_consumer'
assert p['branch_contradiction_proved'] is False
assert p['gate_a_global']=='open' and p['gate_b_global']=='open'
assert p['global_nontrivial_cycle_exclusion']=='open'
print('RL229 PROOF STATE AND SCOPE LOCKS: PASS')
print('frontier 13415865870; no new rank exclusion')
print('physical H21 incidence/charge remains unproved')
print('success C rank-blind charge barrier; RL230 owned-macro strict-excursion')
