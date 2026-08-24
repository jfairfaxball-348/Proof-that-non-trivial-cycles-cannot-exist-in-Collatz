#!/usr/bin/env python3
from collections import deque
from fractions import Fraction
from itertools import product

# Exact cutoff-free state certificate for incoming gap 9.

def enumerate_states(maxe):
    start=(1,0,-14)  # d,e,T after canonical initial 0/1 column
    q=deque([start]); seen={start}; hits=[]
    while q:
        d,e,T=q.popleft()
        if d==1 and (T&1):
            gout=(T+1)//2
            if gout>0:
                hits.append((e,gout,T))
        for x,y in ((0,0),(1,1),(0,1),(1,0)):
            nd=d+y-x
            if nd<=0:
                continue
            ne=e+d-x
            if ne>maxe:
                continue
            num=(3**y)*T + x*3**(d+y-1)-y
            if num&1:
                continue
            st=(nd,ne,num//2)
            if st not in seen:
                seen.add(st);q.append(st)
    return seen,sorted(set(hits))

counts=[]
for E in range(9):
    seen,hits=enumerate_states(E)
    counts.append(len(seen))
    if E<=7:
        assert hits==[]
seen8,hits8=enumerate_states(8)
assert hits8==[(8,4,7)]
assert counts==[3,9,18,31,49,72,100,134,180]

# Check the transition formula directly against normalized prefix arithmetic
# on all canonical positive prefixes through a small depth.
def mod2(fr,n):
    m=1<<n
    return fr.numerator*pow(fr.denominator,-1,m)%m

def rec(S,n,d,e,pa,pb,T,depth):
    # T definition and compatibility for g=9
    assert T == 3**pb*(S-9)/(1<<n)
    assert T.denominator==1
    T=int(T)
    if depth==0:
        return 1
    count=1
    for x,y in ((0,0),(1,1),(0,1),(1,0)):
        nd=d+y-x
        if nd<=0: continue
        ne=e+d-x
        Sn=S
        if x: Sn += Fraction(1<<n,3**(pa+1))
        if y: Sn -= Fraction(1<<n,3**(pb+1))
        if mod2(Sn,n+1)!=9%(1<<(n+1)):
            continue
        num=(3**y)*T+x*3**(d+y-1)-y
        assert num%2==0
        Tn=num//2
        direct=3**(pb+y)*(Sn-9)/(1<<(n+1))
        assert direct.denominator==1 and int(direct)==Tn
        count += rec(Sn,n+1,nd,ne,pa+x,pb+y,Tn,depth-1)
    return count

S=Fraction(-1,3)
checked=rec(S,1,1,0,0,1,-14,8)

# Zero-cost 11 iteration formula at d=1.
for T in range(-100,101,2):
    cur=T
    for k in range(1,8):
        if (3*cur+2)%2: break
        cur=(3*cur+2)//2
        rhs=Fraction(3**k*(T+2),2**k)-2
        assert rhs.denominator==1 and int(rhs)==cur

print('RL43 gap-9 cutoff-free automaton verifier: PASS')
print('state counts E=0..8 =',counts)
print('first crossing = e=8, outgoing gap=4, terminal T=7')
print('direct transition-prefix checks =',checked)
