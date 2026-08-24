#!/usr/bin/env python3
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
BASE_PATH = Path(__file__).resolve().with_name('verify_rl48_four_swap_factorization.py')
spec=spec_from_file_location('base', BASE_PATH)
base=module_from_spec(spec); spec.loader.exec_module(base)
Q=base.Q; build_words=base.build_words


def parity_residue(w):
    a=len(w); L=sum(w); X=1<<a; Y=3**L
    return (-Q(w)*pow(Y,-1,X))%X

def step(n,b):
    assert n&1 == b,(n,b)
    return (3*n+1)//2 if b else n//2

def simulate(n,w):
    vals=[n]
    for b in w:
        n=step(n,b); vals.append(n)
    return n,vals

def check(A,L,t,edges,label):
    u,v,x,y=build_words(edges,t)
    X=1<<A;Y=3**L;U,V=Q(u),Q(v)
    assert U-V==4*(X+Y)
    Nu=parity_residue(u); Nv=parity_residue(v)
    assert Nu%8==3 and Nv%8==7
    assert Nv==Nu+4, (Nu,Nv,X)
    Au,vals_u=simulate(Nu,u)
    Bv,vals_v=simulate(Nv,v)
    assert Au-Bv==4
    # After common leading 11 and mandatory local pair 0/1, the internal
    # trajectories are at step 3 and the exact gap coordinate is T=3^d A-B=-14.
    Acur=vals_u[3]; Bcur=vals_v[3]; d=1; T=3*Acur-Bcur
    assert T==-14
    H=0
    for e in edges:
        xi,yi=int(e[0]),int(e[1])
        assert (Acur&1)==xi and (Bcur&1)==yi
        H += d-1
        Acur=step(Acur,xi); Bcur=step(Bcur,yi)
        d=d+yi-xi
        T=3**d*Acur-Bcur
    k=t+3
    assert d==1 and T==(1<<k)-1
    # terminal 10 then t synchronized 00 columns
    assert Acur&1==1 and Bcur&1==0
    Acur=step(Acur,1); Bcur=step(Bcur,0)
    assert Acur-Bcur==(1<<(t+2))
    for _ in range(t):
        assert not(Acur&1) and not(Bcur&1)
        Acur//=2;Bcur//=2
    assert Acur-Bcur==4
    assert Acur==Au and Bcur==Bv
    print(label,'2-adic starts',Nu,Nv,'outputs',Au,Bv,'H',H,'T semantics PASS')

# witness
EDGES='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
check(65,41,2,EDGES,'RL47 witness')
# countermodel internal block
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split(); loops=15
pairs=[(0,1)]
for token in path:
    if token=='PUMP': pairs += [(1,1)]*loops
    else:pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
internal=[str(a)+str(b) for a,b in pairs[1:-1]]
check(65,41,0,internal,'RL45 countermodel')
print('RL48 two-trajectory semantic verifier: PASS')
