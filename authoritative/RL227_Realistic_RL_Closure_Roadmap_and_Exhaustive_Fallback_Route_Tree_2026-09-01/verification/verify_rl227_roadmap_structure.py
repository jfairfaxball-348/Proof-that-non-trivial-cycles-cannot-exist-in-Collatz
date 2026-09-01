#!/usr/bin/env python3
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'certificates/rl227_roadmap_matrix.json').read_text())
text=(root/'RL227_REALISTIC_RL_CLOSURE_ROADMAP_AND_EXHAUSTIVE_FALLBACK_ROUTE_TREE_2026-09-01.md').read_text()
assert m['format']=='rl227-roadmap-v1'
assert m['finish_line']['global_rl']=='Gate A + Gate B, or stronger exhaustive bypass'
ids={n['id'] for n in m['primary_nodes']}
assert {'P1','P2','P3','P4','P5','P8'} <= ids
for n in m['primary_nodes']:
    assert n['continue'] and n['pivot'] and n['retire']
assert m['fallbacks'][-1]=='SYNTHESISE NEW SOLUTIONS'
assert m['terminal_fallback']['name']=='SYNTHESISE NEW SOLUTIONS'
assert m['queue']['RL228'].startswith('uniform candidate-coupled height exhaustion')
required=[
 'Deleting `e=4` would delete **one more terminal rank**',
 '13,415,865,870',
 'e=4,28,33,40,45',
 'Physical H21 incidence / exhaustive charge',
 'Gate B cannot be postponed conceptually',
 'SYNTHESISE NEW SOLUTIONS',
 'Do **not** make “transition 44” the target'
]
for item in required:
    assert item in text, item
assert text.count('**CONTINUE**') >= 5
assert text.count('**PIVOT**') >= 5
assert text.count('**RETIRE**') >= 5
print('RL227 ROADMAP STRUCTURE AND FALLBACK COMPLETENESS: PASS')
print('finish line distinguishes rank/family/branch/Gate/global closure')
print('all primary nodes carry continue/pivot/retire rules; terminal fallback structured')
print('RL228 queue starts with uniformization, not a raw transition increment')
