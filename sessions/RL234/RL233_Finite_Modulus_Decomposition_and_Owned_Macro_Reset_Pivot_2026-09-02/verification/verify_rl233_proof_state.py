#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=json.loads((R/'RL233_PROOF_STATE.json').read_text())
assert p['completed_rl']==233
assert p['incoming_rl']==234
assert p['success_class']=='C'
assert p['frontier']==13415865870
assert p['e4_rank_live']==31435476727
assert p['e4_combined_survivors']==3856660232
assert p['h17']['spacing_ge']>=1001
assert p['h17']['required_incidence_cap']==1615
assert p['h17']['incidence_cap_proved'] is False
assert p['open']=={'sole_high_branch':True,'gate_a':True,'gate_b':True,'global_exclusion':True}
assert p['successor_target']=='RL234_OWNED_MACRO_RESET_COST_AND_LEGAL_TAIL_CONSUMER_TARGET.md'
assert (R/p['successor_target']).exists()
print('PASS: RL233 proof state')
print('completed_rl=233 incoming_rl=234 success_class=C')
print('frontier=13415865870 e4_rank=31435476727 survivors=3856660232')
print('H17_incidence_cap_1615_proved=no Gates=open')
