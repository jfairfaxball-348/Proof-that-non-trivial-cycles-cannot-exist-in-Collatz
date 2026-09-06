#!/usr/bin/env python3
from collections import Counter
from math import gcd

def Q(bits):
    L=sum(bits); q=0; r=0
    for i,b in enumerate(bits):
        if b:
            r += 1
            q += (1<<i) * (3**(L-r))
    return q

def rotate(bits,m):
    return bits[m:]+bits[:m]

def optimal_flow(bits,m):
    y=rotate(bits,m)
    pref=[]
    s=0
    for a,b in zip(bits,y):
        s += a-b
        pref.append(s)
    med=sorted(pref)[(len(pref)-1)//2]
    return [z-med for z in pref]

def components(g):
    zeros=[i for i,v in enumerate(g) if v==0]
    if not zeros:
        z=g
    else:
        k=zeros[0]
        z=g[k:]+g[:k]
    rr=[];cur=[]
    for v in z:
        if v==0:
            if cur:
                rr.append(cur);cur=[]
        else:
            cur.append(v)
    if cur: rr.append(cur)
    return rr

raw32=0
k1=0
kp=0
km=0
full=0
proper=0
byA=Counter()
for A in range(1,19):
    for mask in range(1<<A):
        bits=[(mask>>i)&1 for i in range(A)]
        L=sum(bits)
        D=(1<<A)-3**L
        if D<=1:
            continue
        q0=Q(bits)
        for m in range(1,A):
            g=optimal_flow(bits,m)
            if sum(abs(v) for v in g)!=5:
                continue
            rr=components(g)
            if max(abs(v) for v in g)>1:
                continue
            if sorted((len(r) for r in rr),reverse=True)!=[3,2]:
                continue
            raw32 += 1
            k=sum(g)
            if abs(k)!=1:
                continue
            k1 += 1
            byA[A] += 1
            if k==1: kp += 1
            else: km += 1
            assert k in (-1,1)
            assert (m*L+k) % A == 0
            q=(m*L+k)//A
            assert q*A-m*L == k
            if q0%D==0:
                full += 1
            elif gcd(q0,D)>1:
                proper += 1

assert raw32==10382
assert k1==4774
assert kp==2387 and km==2387
assert full==0
assert byA==Counter({17:1496,18:720,13:624,16:576,15:420,11:286,14:224,12:192,9:90,8:64,7:42,10:40})

print("PASS RL266 independent A<=18 [3,2] red team")
print("raw_[3,2]_A_le_18=10382")
print("abs_kappa1_[3,2]_A_le_18=4774")
print("kappa_plus=2387 kappa_minus=2387")
print("full_D_hits_abs_kappa1=0")
print("proper_factor_instances_abs_kappa1="+str(proper))
print("REDTEAM_RL266_PASS")
