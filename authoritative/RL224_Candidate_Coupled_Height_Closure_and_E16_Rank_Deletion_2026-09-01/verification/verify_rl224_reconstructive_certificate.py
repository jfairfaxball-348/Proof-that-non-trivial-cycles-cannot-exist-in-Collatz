#!/usr/bin/env python3
"""Reconstruct and rerun the complete RL224 e=16 height-closure certificate."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[1]
SUMMARY=json.loads((ROOT/'certificates/rl224_reconstructive_summary.json').read_text())
assert SUMMARY['format']=='rl224-reconstructive-certificate-v1'
assert SUMMARY['base_head']=='7eacfbe28d424f747e4f1dbd81f3821b69a038eb'
assert SUMMARY['incoming_authoritative_tree']=='db779d8d868f6a1f9656b3270b661fdfb0dbf74c'
assert SUMMARY['records_sha256']=='26323e6ccde617b98890c22349e2b74b1fc17b91f0b5e8b5835b9cbf5fc50d14'
assert SUMMARY['rl216_targeted_candidates']==331_927_916
assert SUMMARY['inherited_phase51_candidates']==139_581_280
assert SUMMARY['phase200_survivors']==4242 and SUMMARY['phase200_prefixes_remaining']==4054
assert SUMMARY['phase200_prefixes_deleted']==40991 and SUMMARY['e16_final_candidates']==0
assert SUMMARY['last_failure_transition_index']==346 and SUMMARY['excluded_terminal_rank']==34124151203
assert SUMMARY['necessary_rank_count_after']==13415865870
if shutil.which('g++') is None:
    raise SystemExit('g++ with OpenMP support is required for the full reconstructive certificate verifier')
with tempfile.TemporaryDirectory() as td:
    td=Path(td); records=td/'records.tsv'; exe=td/'verify_rl224_full_e16_height_closure'
    subprocess.run([sys.executable,str(ROOT/'support/reconstruct_rl224_records.py'),str(records)],check=True)
    got=hashlib.sha256(records.read_bytes()).hexdigest(); assert got==SUMMARY['records_sha256'],got
    subprocess.run(['g++','-O3','-std=c++17','-fopenmp',str(ROOT/'support/verify_rl224_full_e16_height_closure.cpp'),'-o',str(exe)],check=True)
    p=subprocess.run([str(exe),str(records)],check=True,text=True,capture_output=True)
    print(p.stdout,end='')
print('RL224 RECONSTRUCTIVE CERTIFICATE WRAPPER: PASS')
