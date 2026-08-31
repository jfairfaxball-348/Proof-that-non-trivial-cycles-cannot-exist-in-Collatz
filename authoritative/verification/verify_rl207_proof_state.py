#!/usr/bin/env python3
"""RL207 carry-forward/packaging guard; unfinished notes are not proof inputs."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
state = json.loads((root / 'RL207_PROOF_STATE.json').read_text())
assert state['format'] == 'rl207-proof-state-v1'
assert (state['completed_rl'], state['incoming_rl']) == (207, 208)
assert state['primary_target_status'] == 'unfinished at user-requested closeout'
assert state['new_analytic_result_groups'] == []
assert state['new_exact_certificates'] == []
assert state['new_corrections_or_demotions'] == []
assert state['inherited_analytic_result_groups'] == ['RL206-T1', 'RL206-T2', 'RL206-T3']
assert state['inherited_corrections'] == ['RL206-C1', 'RL206-C2']
assert state['new_rank_exclusions'] == 0
assert state['necessary_rank_count'] == 16188727234
assert state['eta_classes_mod18'] == [0, 8, 9, 17]
assert state['corrected_below_p'] == {
    'source_offset': 37, 'root_prefix_depth': 60, 'root_normalization_depth': 97}
for key in ('gate_a_global', 'gate_b_global', 'global_nontrivial_cycle_exclusion'):
    assert state[key] == 'open'
for key in ('quotient_solution_residues_excluded_by_no_go', 'unrestricted_quotient_no_go_proved',
            'exhaustive_gate_b_reduction_proved', 'physical_h21_incidence_proved',
            'h21_charge_proved', 'branch_contradiction_proved', 'independent_eta_selection_proved',
            'full_rank_count_recertified', 'checkpoint_notes_are_proof_dependencies',
            'rl208_started'):
    assert state[key] is False
assert state['stop_after_rl'] == 207
assert state['catalogue_status'] == 'stale/deferred'
assert state['above_p_unverified_source_range_inclusive'] == [65470613322, 137528045311]
assert state['new_root_cone_rank_scans'] == 0

targets = list(root.rglob('*TARGET*.md'))
assert len(targets) == 1 and targets[0].name == 'RL208_H21_INDEPENDENT_INFORMATION_TARGET.md'
required = {
    'START_HERE.md': ['RL208 incoming authoritative state', 'RL208 has not been started', '37 / 60 / 97'],
    'RL207_CERTIFIED_FACTS_AND_PROOF_LEDGER.md': [
        'No new RL207 theorem', 'RL206-T1', 'RL206-T2', 'RL206-T3', '16,188,727,234', 'NOT PROMOTED'],
    'RL207_CORRECTION_DEMOTION_LEDGER.md': ['No new RL207 correction', 'RL206-C1', 'RL206-C2', '37 / 60 / 97'],
    'RL207_RED_TEAM_REPORT_2026-08-31.md': [
        'PASS', 'Source/terminal', 'Carry', 'Eta', 'Real-mass', 'Denominator', 'Coverage', 'Globality',
        'RL20', 'RL79', 'Coboundary', 'Proper factor', 'Generalized increment', 'Scale'],
    'RL207_UNFINISHED_WORK.md': ['NOT PROMOTED', '65470613322', '137528045311', 'no new rank scan'],
    'RL206_INHERITED_H21_INTERFACE.md': ['i=a+34 modL', '40886621976', 'p-a>=37', '>=60', '>=97'],
    'RL208_H21_INDEPENDENT_INFORMATION_TARGET.md': ['Required red teams', '56-bit', '37', '60', '97'],
}
for name, needles in required.items():
    data = ' '.join((root / name).read_text().split())
    for needle in needles:
        assert needle in data, (name, needle)
for name in ('A_GT_P_CLOSEOUT_CHECKPOINT.md', 'ROOT_CONE_CLOSEOUT_CHECKPOINT.md'):
    assert 'NOT PROMOTED' in (root / 'unfinished' / name).read_text()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def safe(name):
    path = PurePosixPath(name)
    assert name and not path.is_absolute() and '..' not in path.parts
    return path

# Reconstruct the exact accepted RL206 payload, including its original manifest,
# target and proof-state guard. Its old operational instructions are provenance
# only in the RL207 bundle; they do not start another job.
mapping = json.loads((root / 'provenance/RL206_SOURCE_MAP.json').read_text())
assert mapping['source_commit'] == '9e971c260bcaee497b5e634c639a2cbc01a225ec'
assert mapping['source_authority_tree'] == 'c73f39dc12df9ceb467dab2127a9b97c28173030'
assert mapping['source_bundle_sha256'] == '9ae3077b93753fb25c77d899d14bd57e09f02eded96af68c95e6ba8c613b5469'
assert len(mapping['files']) == 39
assert len({item['source_path'] for item in mapping['files']}) == 39
assert len({item['path'] for item in mapping['files']}) == 39
with tempfile.TemporaryDirectory(prefix='rl207-inherited-rl206-') as tmp:
    old = Path(tmp)
    for item in mapping['files']:
        source = root / safe(item['path'])
        data = source.read_bytes()
        assert digest(data) == item['sha256'], item['path']
        assert len(data) == item['bytes'], item['path']
        dest = old / safe(item['source_path'])
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    assert digest((old / 'SHA256SUMS.txt').read_bytes()) == '22791316715eb5503586120ae5366c17f67a5ebbb0200d9ab4d11633926d47aa'
    run = subprocess.run([sys.executable, str(old / 'verification/verify_rl206_proof_state.py')],
                         cwd=old, text=True, capture_output=True, check=True)
    assert run.stdout == 'PASS RL206 proof-state, finite domains, corrections, provenance and manifest\n'

records = {}
for line in (root / 'SHA256SUMS.txt').read_text().splitlines():
    value, name = line.split('  ', 1)
    assert re.fullmatch('[0-9a-f]{64}', value)
    safe(name)
    assert name not in records
    assert digest((root / name).read_bytes()) == value, name
    records[name] = value
actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
          and '__pycache__' not in p.parts and p.name != 'SHA256SUMS.txt'
          and not (p.parent == root and (p.name.endswith('.zip') or p.name.endswith('.zip.sha256')))}
assert set(records) == actual, ('manifest coverage', set(records) ^ actual)
print('PASS RL207 unchanged proof frontier, inherited RL206 guard, unfinished-work scope and manifest')
