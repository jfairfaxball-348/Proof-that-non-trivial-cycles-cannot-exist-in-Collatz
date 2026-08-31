#!/usr/bin/env python3
"""RL206 packaging/scope guards; analytic validity is in the proofs and review."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
state = json.loads((root/'RL206_PROOF_STATE.json').read_text())
assert state['format'] == 'rl206-proof-state-v1'
assert (state['completed_rl'],state['incoming_rl']) == (206,207)
assert state['new_rank_exclusions'] == 0
assert state['necessary_rank_count'] == 16188727234
assert state['eta_classes_mod18'] == [0,8,9,17]
assert state['corrections'] == ['RL206-C1','RL206-C2']
assert state['corrected_below_p'] == {'source_offset':37,'root_prefix_depth':60,'root_normalization_depth':97}
for key in ('gate_a_global','gate_b_global','global_nontrivial_cycle_exclusion'):
    assert state[key] == 'open'
for key in ('quotient_solution_residues_excluded_by_no_go','unrestricted_quotient_no_go_proved',
            'exhaustive_gate_b_reduction_proved','physical_h21_incidence_proved','h21_charge_proved'):
    assert state[key] is False
assert state['catalogue_status'] == 'stale/deferred'

targets=list(root.rglob('*TARGET*.md'))
assert len(targets)==1 and targets[0].name=='RL207_H21_INDEPENDENT_INFORMATION_TARGET.md'
required={
    'RL206_CERTIFIED_FACTS_AND_PROOF_LEDGER.md':['RL206-T1','RL206-T2','RL206-T3','RL206-C1','RL206-C2','16,188,727,234'],
    'RL206_CORRECTION_DEMOTION_LEDGER.md':['first','RL206-C1','RL206-C2','39','37','63','60','100','97'],
    'RL206_INHERITED_H21_INTERFACE.md':['i=a+34 modL','40886621976','p-a>=37','>=60','>=97'],
    'RL206_RED_TEAM_REPORT_2026-08-31.md':['PASS','RL20','RL79','Coboundary','Proper factor','Generalized increment','Scale','Globality'],
    'proofs/QUOTIENT_MODULE_THEOREM.md':['c^T B=D e_0^T','diag(1,...,1,D)','mod D^2','not an all-quotient-residual no-go'],
    'proofs/FINITE_ARC_SCALE_THEOREM.md':['every sufficiently large integer','a constant rational function','both the divisibility modulus','additional global hypotheses'],
    'corrections/RL20_INCREMENT_NORMALIZATION_REPAIR.md':['3^(-E_(j+1))','5/9'],
    'corrections/RL203_SOURCE_TERMINAL_INDEX_REPAIR.md':['33709842710','p-a>=37','60>56'],
    'START_HERE.md':['RL207 incoming authoritative state','37 / 60 / 97'],
}
for name,needles in required.items():
    data=' '.join((root/name).read_text().split())
    for needle in needles:
        assert needle in data,(name,needle)

def certificate(name):
    obj=json.loads((root/'certificates'/name).read_text())
    assert obj['status']=='PASS'
    return obj

module=certificate('verify_rl206_quotient_module_output.json')
assert module['matrix_words_A_2_to_9']==778
assert module['annihilator_coefficient_vectors']==159975
assert module['annihilator_word_modulus_pairs_A_2_to_4_M_1_to_9']==135
assert module['kernel_forcings_A_2_to_5_entries_minus1_to_1']==6984
assert module['quotient_residue_exceptions_D_gt_1']==776
arc=certificate('verify_rl206_finite_arc_and_increment_output.json')
assert arc['finite_arc_domain']['all_binary_word_lengths']==[1,10]
assert arc['finite_arc_domain']['sampled_integer_parameters']==[0,1,2,17]
assert arc['finite_arc_checks']['words']==2046
assert arc['finite_arc_checks']['sampled_arcs']==8184
assert arc['finite_arc_checks']['sampled_phase_checks']==81920
assert arc['corrected_block_checks']['words']==940
assert arc['corrected_block_checks']['corrected_increment_checks']==2880
assert arc['RL20_fake']['full_D_quotient_integral'] is False
assert arc['RL20_fake']['near_resonant_16_over_15_scope_satisfied'] is False
assert arc['RL20_fake']['rotation_distance_scan_performed'] is False
h21=certificate('verify_rl206_h21_coordinate_repair_output.json')
assert h21['finite_offset_range']==[34,39]
assert h21['first_necessary_below_p_offset']==37
assert h21['root_prefix_depth_lower_bound']==60
assert h21['root_normalization_depth_lower_bound']==97
assert h21['qualitative_mod2_56_boundary_preserved'] is True
assert h21['physical_realization_claimed'] is False
assert h21['full_rank_count_recertified'] is False

for item in json.loads((root/'provenance/SOURCE_IDENTITIES.json').read_text()):
    assert hashlib.sha256((root/item['path']).read_bytes()).hexdigest()==item['sha256']

records={}
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    digest,name=line.split('  ',1)
    assert re.fullmatch('[0-9a-f]{64}',digest)
    path=PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts
    assert name not in records
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
    records[name]=digest
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
        and '__pycache__' not in p.parts and p.name!='SHA256SUMS.txt'
        and not (p.parent==root and (p.name.endswith('.zip') or p.name.endswith('.zip.sha256')))}
assert set(records)==actual,('manifest coverage',set(records)^actual)
print('PASS RL206 proof-state, finite domains, corrections, provenance and manifest')
