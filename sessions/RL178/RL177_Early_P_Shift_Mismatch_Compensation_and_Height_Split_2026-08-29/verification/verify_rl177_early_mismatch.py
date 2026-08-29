#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

base=Path(__file__).resolve().parents[1]
report=(base/'RL177_EARLY_P_SHIFT_MISMATCH_COMPENSATION_2026-08-29.md').read_text(encoding='utf-8')
for token in [
    'T_{J+1}=\\operatorname{sgn}(d)',
    'N>1/3',
    '15,872 legal signed local',
    'F_2<\\frac12-\\frac{11\\Delta}{16}',
    'J=23',
]:
    assert token in report, token

run=subprocess.run(
    [sys.executable,str(base/'RL177_CERTIFICATES/verify_early_mismatch_consumer.py')],
    cwd=base,text=True,capture_output=True)
if run.returncode:
    print(run.stdout,end='')
    print(run.stderr,end='',file=sys.stderr)
    raise SystemExit('FAIL: RL177 exact finite certificate')
print(run.stdout,end='')
print('PASS: RL177 portable fresh-unpack verifier completed successfully.')
