#!/usr/bin/env python3
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from random import Random

BASE = Path('/mnt/data/RL49_work_2026-08-22/rl48_continued/verify_rl48_four_swap_factorization.py')
spec=spec_from_file_location('base',BASE); base=module_from_spec(spec); spec.loader.exec_module(base)
build_words=base.build_words


def cyclic_transport_distance(a,b):
    assert len(a)==len(b) and sum(a)==sum(b)
    G=[]; s=0
    for x,y in zip(a,b):
        s += y-x
        G.append(s)
    assert s==0
    vals=sorted(G)
    med=vals[len(vals)//2]
    return sum(abs(g-med) for g in G)


def half_formula(u,v):
    assert len(u)==len(v) and sum(u)==sum(v)
    h=[]; s=0
    for x,y in zip(u,v):
        s += y-x
        h.append(s)
    assert s==0
    d=u+v; dp=v+u
    return cyclic_transport_distance(d,dp), 2*sum(abs(x) for x in h)

# General algebraic regression on random equal-weight half words.
rng=Random(4901)
checks=0
for a in range(2,13):
    for _ in range(300):
        wt=rng.randrange(1,a)
        pos1=rng.sample(range(a),wt); pos2=rng.sample(range(a),wt)
        u=[int(i in pos1) for i in range(a)]
        v=[int(i in pos2) for i in range(a)]
        got,want=half_formula(u,v)
        assert got==want,(u,v,got,want)
        assert got%2==0
        checks+=1


def one_excursion_check(A,L,t,edges,label,expected_H,expected_dist):
    u,v,x,y=build_words(edges,t)
    assert len(u)==A and len(v)==A and sum(u)==sum(v)==L
    # local height convention from RL47/RL48
    d=1; H=0
    for e in edges:
        xi,yi=int(e[0]),int(e[1])
        assert d>=1
        H += d-1
        d += yi-xi
        assert d>=1
    assert d==1
    got,twice=half_formula(u,v)
    assert got==twice
    formula=2*(A-t-3+H)
    assert got==formula
    assert H==expected_H and got==expected_dist
    print(label,'H=',H,'cyclic_half_rotation_distance=',got,'PASS')

EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
one_excursion_check(65,41,2,EDGES,'RL47 witness',104,328)

internal=base.internal
one_excursion_check(65,41,0,internal,'RL45 countermodel',3,130)

print('random equal-half metric checks:',checks)
print('RL49 half-rotation radius audit verifier: PASS')
