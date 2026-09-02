#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

A=217_976_794_617
L=137_528_045_312
B=A-L
R=L-B
H=17
CA=11*3**32
CB=5*3**33
A_CORE=(11_443_822_977,28_746_802_249)
B_CORE=(72_981_981_437,100_039_806_527)

assert L//1616+1 == 85_103_989

def v2(n):
    n=abs(n); assert n
    return (n & -n).bit_length()-1

def cbit(r): return 1 if r<R else 2

def shifted_intervals(core,j):
    lo,hi=core; s=(j*B)%L; a,b=lo+s,hi+s
    if b<L: return [(a,b)]
    if a>=L: return [(a-L,b-L)]
    return [(0,b-L),(a,L-1)]

def common_bit(core,j):
    bits=set()
    for lo,hi in shifted_intervals(core,j):
        bits.add(cbit(lo)); bits.add(cbit(hi))
        if lo<R<=hi: bits.update((1,2))
    assert len(bits)==1
    return next(iter(bits))

A_WORD=tuple(common_bit(A_CORE,j) for j in range(3))
B_WORD=tuple(common_bit(B_CORE,j) for j in range(3))
assert A_WORD==(1,2,1)
assert B_WORD==(2,1,2)

def normalized_delta(h,hp,C): return Fraction(C,1<<max(h,hp))

def successors(state,c):
    h,hp,C=state; g=h-hp; out=[]
    for alpha in range(1,h+c+1):
        h2=h+c-alpha
        for beta in range(1,hp+c+1):
            hp2=hp+c-beta
            if g>0:
                N=3*C+(1<<g)-1; eZ=g+beta; eX=alpha
            elif g<0:
                N=3*C+1-(1<<(-g)); eZ=beta; eX=-g+alpha
            else:
                N=3*C; eZ=beta; eX=alpha
            vv=v2(N)
            if eZ!=eX:
                d=min(eZ,eX)
                if vv!=d: continue
            else:
                d=eZ
                if vv<=d: continue
            assert N%(1<<d)==0
            C2=N>>d
            lhs=(1<<c)*normalized_delta(h2,hp2,C2)
            rhs=3*normalized_delta(h,hp,C)+Fraction(1,1<<hp)-Fraction(1,1<<h)
            assert lhs==rhs
            # exact intercept E = 2^d C2 - 3C
            E=(1<<d)*C2-3*C
            assert d == c + max(h,hp)-max(h2,hp2)
            out.append(((h2,hp2,C2),d,E))
    return out

def initial_states(C):
    return [(17,j,C) for j in range(17)] + [(j,17,C) for j in range(17)]

def enumerate_paths(C,word):
    paths=[]
    for init in initial_states(C):
        cur=[(init,[],[init[2]])]
        for c in word:
            nxt=[]
            for state,labels,Cs in cur:
                for st2,d,E in successors(state,c):
                    nxt.append((st2,labels+[(d,E)],Cs+[st2[2]]))
            cur=nxt
        for state,labels,Cs in cur:
            paths.append((init,state,labels,Cs))
    return paths

def check_path(path):
    init,final,labels,Cs=path
    n=len(labels); C0=Cs[0]
    Ds=[0]
    for d,E in labels: Ds.append(Ds[-1]+d)
    # Q telescope and dyadic rebasing for every k
    Q=[]
    for k,Ck in enumerate(Cs):
        Q.append((1<<Ds[k])*Ck - 3**k*C0)
    for k in range(n+1):
        T=(1<<(Ds[n]-Ds[k]))*Cs[n]-3**(n-k)*Cs[k]
        assert Q[n] == 3**(n-k)*Q[k] + (1<<Ds[k])*T
        if k>0:
            assert (Q[n]-3**(n-k)*Q[k])%(1<<Ds[k])==0
            assert (Q[n]-3**(n-k)*Q[k])//(1<<Ds[k])==T
    # unit-modulus fixed-label affine evolution
    for q in (5,7,11,13):
        for k in range(n+1):
            x=Cs[k]%q
            Acoef=1; Bcoef=0
            for j in range(k,n):
                d,E=labels[j]
                inv2d=pow(pow(2,d,q),-1,q)
                Acoef=(3*inv2d*Acoef)%q
                Bcoef=(inv2d*(3*Bcoef+E))%q
            assert Acoef%q!=0
            assert Cs[n]%q == (Acoef*x+Bcoef)%q
    # 3-adic recurrence and explicit source-term loss after b steps
    for b in (1,2,3):
        mod=3**b
        x=C0%mod
        for d,E in labels:
            x=(pow(pow(2,d,mod),-1,mod)*(3*x+E))%mod
        assert x==Cs[n]%mod
        if n>=b:
            # recompute from only the final b labels with arbitrary source 0/1;
            # 3^b kills any source difference after b transitions.
            vals=[]
            for seed in (0,1,2):
                y=seed%mod
                for d,E in labels[-b:]:
                    y=(pow(pow(2,d,mod),-1,mod)*(3*y+E))%mod
                vals.append(y)
            assert len(set(vals))==1
            assert vals[0]==Cs[n]%mod

A_paths=enumerate_paths(CA,A_WORD)
B_paths=enumerate_paths(CB,B_WORD)
assert len(A_paths)==14_244, len(A_paths)
assert len(B_paths)==16_976, len(B_paths)
for p in A_paths: check_path(p)
for p in B_paths: check_path(p)

print('PASS: RL233 finite-modulus decomposition regression')
print('A_paths=14244')
print('B_paths=16976')
print('total_paths=31220')
print('standalone_3adic_required_b_ge=85103989')
print('classification=EXACT_REGRESSION_SUPPORT_FOR_ANALYTIC_THEOREM')
