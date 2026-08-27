#!/usr/bin/env python3
import re, pathlib
p=pathlib.Path(__file__).resolve().parent.parent/'audit'/'RL128_L12_CANONICAL_OWNERSHIP_CERTIFICATE.txt'
rows=[]; total=None
pat=re.compile(r'^Z=(\d+) U=(\d+) capacity_profiles=(\d+) periodic=(\d+) canonical_primitive_profiles=(\d+) orbit_weight=(\d+) canonical_roots_tested=(\d+) divisibility_hits=(\d+)$')
tpat=re.compile(r'^TOTAL capacity_profiles=(\d+) periodic=(\d+) canonical_primitive_profiles=(\d+) orbit_weight=(\d+) canonical_roots_tested=(\d+) divisibility_hits=(\d+)$')
for line in p.read_text().splitlines():
    m=pat.match(line)
    if m: rows.append(tuple(map(int,m.groups()))); continue
    m=tpat.match(line)
    if m: total=tuple(map(int,m.groups()))
assert [r[0] for r in rows]==list(range(8,41))
assert total is not None
s=[sum(r[i] for r in rows) for i in range(2,8)]
assert tuple(s)==total
for z,u,P,per,can,w,tests,hits in rows:
    D=2**(12+z)-3**12; B=(2**z-1)*(3**12-2**12)
    assert u==B//D
    assert w==P-per
    assert tests==can
    assert hits==0
assert total==(1559151385,8839,160979484,1559142546,160979484,0)
assert all(r[2]==0 for r in rows if r[0]>=37)
print('RL128 certificate structural audit: PASS')
print('rows: 33 (Z=8..40), gap-free')
print('capacity_profiles=1559151385 periodic=8839 canonical_tests=160979484 hits=0')
