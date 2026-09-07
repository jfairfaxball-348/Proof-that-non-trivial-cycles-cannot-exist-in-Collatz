#!/usr/bin/env python3
from collections import Counter
from math import gcd

def rot(bits,m):
    m %= len(bits)
    return bits[m:]+bits[:m]

def Q(bits):
    L=sum(bits); out=0; r=0
    for i,b in enumerate(bits):
        if b:
            r += 1
            out += (1<<i) * (3**(L-r))
    return out

def prefix_values(bits,m):
    y=rot(bits,m); c=0; vals=[]
    for a,b in zip(bits,y):
        c += a-b
        vals.append(c)
    return vals

def all_optimal_flows(bits,m):
    vals=prefix_values(bits,m)
    s=sorted(vals); A=len(vals)
    lo=s[(A-1)//2]; hi=s[A//2]
    best=sum(abs(v-lo) for v in vals)
    out=[]
    for t in range(lo,hi+1):
        g=[v-t for v in vals]
        if sum(abs(z) for z in g)==best:
            out.append(g)
    return out

def runs(g):
    if not any(g): return []
    if 0 in g:
        k=g.index(0); z=g[k:]+g[:k]
    else:
        z=g[:]
    out=[]; cur=[]
    for v in z:
        if v==0:
            if cur: out.append(cur); cur=[]
        else:
            cur.append(v)
    if cur: out.append(cur)
    return out

def topology(g):
    rr=runs(g)
    if max(abs(v) for v in g)<=1:
        ll=sorted((len(r) for r in rr),reverse=True)
        return "["+",".join(map(str,ll))+"]"
    masses=sorted((sum(abs(v) for v in r) for r in rr),reverse=True)
    if masses==[5]: return "height2-connected-5"
    if masses==[4,1]: return "height2-4+1"
    raise AssertionError((g,masses))

def normalize_plus(bits,m,g):
    A=len(bits)
    if sum(g)==-3:
        # Reverse source and target exactly; -g is an optimal flow for the reversed pair.
        bits=rot(bits,m)
        m=A-m
        g=[-z for z in g]
    assert sum(g)==3
    p=None
    for i in range(A):
        if [g[(i+j)%A] for j in range(3)]==[1,2,1]:
            p=i
            break
    assert p is not None
    bits=rot(bits,p)
    g=rot(g,p)
    assert g[:3]==[1,2,1]
    neg=[i for i,z in enumerate(g) if z==-1]
    assert len(neg)==1
    u=neg[0]
    assert 4<=u<=A-2
    return bits,m,g,u

flow_occ=0
plus=minus=0
distinct=set()
by_A=Counter()
formula_bad=0
full_diff=0
proper_diff=0
actual_full=0
multi=Counter()

for A in range(6,16):
    for mask in range(1<<A):
        bits=[(mask>>i)&1 for i in range(A)]
        L=sum(bits); D=(1<<A)-3**L
        if D<=1: continue
        q0=Q(bits)
        for m in range(1,A):
            flows=all_optimal_flows(bits,m)
            if not flows or sum(abs(z) for z in flows[0])!=5:
                continue
            matched=0
            for g in flows:
                if topology(g)!="height2-4+1" or abs(sum(g))!=3:
                    continue
                matched += 1
                flow_occ += 1
                by_A[A] += 1
                distinct.add((A,mask,m))
                if sum(g)==3: plus += 1
                else: minus += 1

                b,m0,g0,u=normalize_plus(bits,m,g)
                y=rot(b,m0)
                L0=sum(b); D0=(1<<A)-3**L0
                r=sum(b[:u+1])
                diff=Q(y)-Q(b)
                form=15*3**(L0-2)-(1<<u)*3**(L0-r-1)
                if diff!=form:
                    formula_bad += 1
                if diff%D0==0:
                    full_diff += 1
                elif gcd(abs(diff),D0)>1:
                    proper_diff += 1

                assert (m0*L0+3)%A==0
                q=(m0*L0+3)//A
                assert q*A-m0*L0==3

            if matched:
                multi[matched] += 1
                if q0%D==0:
                    actual_full += 1

assert flow_occ==708
assert plus==minus==354
assert len(distinct)==702
assert by_A==Counter({6:12,9:72,12:144,15:480})
assert multi==Counter({1:696,2:6})
assert formula_bad==0
assert full_diff==0
assert actual_full==0
assert proper_diff==30

# The canonical positive-orientation certificate has counts
# A=6:1,9:4,12:6,15:16; multiplying by A rotations gives 354.
assert 6*1 + 9*4 + 12*6 + 15*16 == plus

# Permanent negative-domain sentinel.
neg=list(map(int,"00011110111"))
A=len(neg); L=sum(neg); D=(1<<A)-3**L
assert (A,L,D,Q(neg),Q(neg)//D)==(11,7,-139,18904,-136)

print("RL272 height-two 4+1 A<=15 red team: PASS")
print("optimal_flow_occurrences=%d plus=%d minus=%d distinct_instances=%d" % (flow_occ,plus,minus,len(distinct)))
print("byA=%s multi_optimal_instances=%s" % (dict(sorted(by_A.items())),dict(sorted(multi.items()))))
print("binomial_identity_mismatches=%d" % formula_bad)
print("proper_factor_only_diff=%d full_D_diff_hits=%d actual_full_D_words=%d" % (proper_diff,full_diff,actual_full))
print("negative_sentinel=(11,7,-139,18904,-136)")
print("RL272_HEIGHT2_SMALL_REDTEAM_PASS")
