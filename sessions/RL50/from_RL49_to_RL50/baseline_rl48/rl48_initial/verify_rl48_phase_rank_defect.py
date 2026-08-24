#!/usr/bin/env python3
from math import gcd

# Two independent regressions of the algebraic Q(v)-to-defect identity:
# (i) inherited RL45 t=0 proper-factor countermodel;
# (ii) audited RL47 (65,41) minimum-excess terminal witness at t=2.

def Q(word):
    rem=sum(word); out=0
    for i,b in enumerate(word):
        if b:
            out += (1<<i)*3**(rem-1)
            rem-=1
    return out

def Qrank(word):
    pos=[i for i,b in enumerate(word) if b]
    r=len(pos)
    return sum((1<<p)*3**(r-j) for j,p in enumerate(pos,1))

def check(A,L,t,x,y):
    q=A-L; k=t+3; r=L-3; m=A-k-1
    assert len(x)==len(y)==m
    assert sum(x)==sum(y)==r
    apos=[i for i,b in enumerate(x) if b]
    bpos=[i for i,b in enumerate(y) if b]
    assert all(b<=a for a,b in zip(apos,bpos))
    H=sum(a-b for a,b in zip(apos,bpos))

    Qx=Qrank(x); Qy=Qrank(y); D=Qx-Qy
    terminal=14*3**r + (1<<(A-1)) - (1<<(A-k-1))
    assert 3*Qx-Qy==terminal

    # Standard reconstructed full phase word.
    v=[1,1,1]+y+[0]*(t+1)
    assert len(v)==A and sum(v)==L
    Qv=Q(v)
    assert Qv==19*3**r+8*Qy
    assert Qv==75*3**r+(1<<(A+1))-(1<<(A-k+1))-12*D

    M=(1<<A)-3**L
    phase_num=Qv+4*3**L
    defect_form=183*3**r+(1<<(A+1))-(1<<(A-k+1))-12*D
    assert phase_num==defect_form
    reduced=(237*3**r-(1<<(A-k+1))-12*D)%M
    assert reduced==phase_num%M
    return H,D,phase_num%M,gcd(phase_num,M)

# RL45 t=0 proper-factor countermodel.
path='00 01 10 00 PUMP 00 01 11 10 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 00 11 11'.split()
pairs=[(0,1)]
for token in path:
    if token=='PUMP': pairs += [(1,1)]*15
    else: pairs.append((int(token[0]),int(token[1])))
pairs.append((1,0))
internal=pairs[1:-1]
x0=[x for x,y in internal]; y0=[y for x,y in internal]
r0=check(65,41,0,x0,y0)

# RL47 audited t=2 minimum-excess terminal witness.
edges='''11 11 01 11 11 10 01 01 11 11 00 11 11 01 10 01 11 10 01 10 11 10 01 11 10 01 01 10 11 00 11 11 00 10 01 11 11 01 11 10 01 11 10 11 01 00 10 10 01 10 11 00 10 01 11 11 01 10 10'''.split()
x2=[int(e[0]) for e in edges]; y2=[int(e[1]) for e in edges]
r2=check(65,41,2,x2,y2)

assert r0[2]!=0 and r2[2]!=0  # neither regression is a full phase solution
print('RL48 phase-to-rank-defect algebra verifier: PASS')
print('t=0 countermodel: H,D,phase_residue,gcd =',r0)
print('t=2 audited witness: H,D,phase_residue,gcd =',r2)
print('conditional bridge congruence algebra: PASS')
