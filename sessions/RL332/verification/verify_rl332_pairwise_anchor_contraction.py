#!/usr/bin/env python3
"""RL332 verifier: zero-slack phase splicing, pairwise anchor gain, all-rho contraction."""
import contextlib
import io
import runpy
from collections import defaultdict
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    base = runpy.run_path(str(Path(__file__).with_name("verify_rl332_self_consistent_ownership.py")))

A=base["A"]; ELL=base["ELL"]; LAM=base["LAM"]; l2lo=base["l2lo"]
states=base["states"]; edges=base["edges"]; pot=base["pot"]; b2=base["b2"]
full=base["full"]; rho59=base["rho59"]
BOOT=32_550_361_322; CAP=BOOT-1
assert base["H"] == BOOT and base["CAP"] == CAP

zero=[]; adj=defaultdict(list)
for s,t,z,k in edges:
    sigma=pot[t]-pot[s]-(2*z-43*k)
    assert sigma >= 0
    if sigma == 0:
        zero.append((s,t,z,k)); adj[s].append(t)

counter=0; stack=[]; on=set(); indices={}; lowlink={}; comps=[]
def visit(v):
    global counter
    indices[v]=lowlink[v]=counter; counter+=1; stack.append(v); on.add(v)
    for w in adj[v]:
        if w not in indices:
            visit(w); lowlink[v]=min(lowlink[v],lowlink[w])
        elif w in on:
            lowlink[v]=min(lowlink[v],indices[w])
    if lowlink[v] == indices[v]:
        c=[]
        while True:
            w=stack.pop(); on.remove(w); c.append(w)
            if w==v: break
        comps.append(c)
for v in range(len(states)):
    if v not in indices: visit(v)
co={v:i for i,c in enumerate(comps) for v in c}
cyclic={i for i,c in enumerate(comps) if len(c)>1 or any(s==t and co[s]==i for s,t,_,_ in zero)}
assert len(comps)==288 and len(cyclic)==16

low={i for i,state in enumerate(states) if state[0]=="N" and state[1]<=21}
assert all(pot[v] == 0 for v in low)
inside=defaultdict(list)
for s,t,z,k in zero:
    if co[s]==co[t] and co[s] in cyclic:
        assert k==1 and ((s in low) != (t in low))
        inside[s].append((t,z,k))
for s,outs in inside.items():
    if s in low:
        for mid,z1,k1 in outs:
            for target,z2,k2 in inside[mid]:
                assert target in low
                assert z1+k1+z2+k2 == 45

cross=[e for e in zero if co[e[0]] != co[e[1]]]
assert all(not (co[t] in cyclic and co[s] not in cyclic) for s,t,_,_ in cross)
recurrent_cross=[e for e in cross if co[e[0]] in cyclic and co[e[1]] in cyclic]
assert len(recurrent_cross) == 195
for s,t,z,k in recurrent_cross:
    assert s in low and t not in low and pot[s] == 0
    nxt=[e for e in zero if e[0]==t and co[e[1]]==co[t]]
    assert nxt
    for _,u,z2,k2 in nxt:
        assert u in low and pot[u] == 0
        assert z+k+z2+k2 == 45

dag=defaultdict(list); indeg=[0]*len(comps); arcs=set()
for s,t,z,k in cross:
    c,d=co[s],co[t]
    dag[c].append((d,k))
    if (c,d) not in arcs:
        arcs.add((c,d)); indeg[d]+=1
q=[c for c,x in enumerate(indeg) if x==0]; topo=[]
while q:
    c=q.pop(); topo.append(c)
    for d in {x for x,_ in dag[c]}:
        indeg[d]-=1
        if indeg[d]==0: q.append(d)
assert len(topo)==len(comps)
neg=-10**9
trans=[0 if c not in cyclic else neg for c in range(len(comps))]
tail=[neg]*len(comps)
for c in topo:
    for d,k in dag[c]:
        if c not in cyclic and d not in cyclic and trans[c] > neg:
            trans[d]=max(trans[d],trans[c]+k)
        if c in cyclic and d not in cyclic:
            tail[d]=max(tail[d],k)
        elif c not in cyclic and d not in cyclic and tail[c] > neg:
            tail[d]=max(tail[d],tail[c]+k)
assert max(trans)==3
assert max(tail)==4

for s,t,z,k in edges:
    sigma=pot[t]-pot[s]-(2*z-43*k)
    assert 2*(z+k)-(pot[t]-pot[s]) == 45*k-sigma

step=(45*A)%ELL
alpha=Fraction(step,ELL)
assert step==44_464_540_613 and 2*step < ELL
y=alpha*l2lo
CLOW=sum(y**j/factorial(j) for j in range(1,9))
CFIX=Fraction(25_120_009_946_627,10**14)
assert CLOW > CFIX

@lru_cache(None)
def weighted(K):
    s1=K*(K+1)//2
    s2=K*(K+1)*(2*K+1)//6
    s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return (Fraction(K)+l2lo*s1/ELL+l2lo**2*s2/(2*ELL**2)+l2lo**3*s3/(6*ELL**3)+l2lo**4*s4/(24*ELL**4))

def kbase_s0(rho):
    K=(2*(ELL-rho+1)-b2+44)//45
    s0=b2-(2*(ELL-rho+1)-45*K)
    assert 0 <= s0 <= 44
    return K,s0

def structural(Kbase,h,s0):
    K=Kbase+h; S=45*h+s0
    return Fraction(K)+CFIX*Fraction(K-10*S-7,4)

def min_gain(Kbase,s0):
    W=weighted(Kbase)
    slope=structural(Kbase,1,s0)-structural(Kbase,0,s0)
    crosspoint=(structural(Kbase,0,s0)-W)/(1-slope)
    q=max(0,crosspoint.numerator//crosspoint.denominator)
    vals=[(h,max(Fraction(h),structural(Kbase,h,s0)-W)) for h in {0,q,q+1} if h>=0]
    return min(vals,key=lambda row:row[1])

K0,s060=kbase_s0(60)
h60,g60=min_gain(K0,s060)
assert K0==6_112_357_564 and s060==3
assert h60==10_239_722 and g60==10_239_722

def omit_exact(last):
    return sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,last+1)),Fraction())/LAM
def baseline_exact(rho):
    K,_=kbase_s0(rho)
    return 1+(full-omit_exact(rho-1))/3-weighted(K)/(12*LAM)

rhs60=baseline_exact(60)-g60/(12*LAM)
assert rhs60 < BOOT and rhs60.numerator//rhs60.denominator == CAP

finite_min=None
for rho in range(61,200):
    K,s0=kbase_s0(rho); h,g=min_gain(K,s0)
    finite_min = g if finite_min is None else min(finite_min,g)
    assert baseline_exact(rho)-g/(12*LAM) < BOOT
assert finite_min >= 10_239_721

HANDOFF=3_607_000
KMIN,_=kbase_s0(HANDOFF-1)
assert KMIN==6_112_197_256
struct_inc=1+CFIX/4
w_inc_max=weighted(K0+1)-weighted(K0)
assert struct_inc > w_inc_max
hu,uniform=min_gain(KMIN,44)
assert hu==10_239_542 and uniform==10_239_542
assert baseline_exact(200)-uniform/(12*LAM) < BOOT

def decfrac(fr,prec,rounding):
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=rounding
        return Decimal(fr.numerator)/Decimal(fr.denominator)

def ordinary_upper(rho,prec=80):
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=ROUND_FLOOR
        term=Decimal(1); total=Decimal(0); prevq=0
        for r in range(1,rho):
            qr=(A*r)//ELL; gap=qr-prevq
            term=term*Decimal(1<<gap)/Decimal(3)
            total+=term; prevq=qr
        lam=Decimal(LAM.numerator)/Decimal(LAM.denominator)
        omitted_lo=total/lam
        K,_=kbase_s0(rho)
        w=weighted(K)
        weighted_lo=Decimal(w.numerator)/Decimal(w.denominator)
        wdiv_lo=weighted_lo/(Decimal(12)*lam)
    full_up=decfrac(full,prec,ROUND_CEILING)
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=ROUND_CEILING
        return Decimal(1)+(full_up-omitted_lo)/Decimal(3)-wdiv_lo

handoff_upper=ordinary_upper(HANDOFF)
assert handoff_upper < Decimal(BOOT)
assert rho59 < BOOT

print("RL332_PAIRWISE_ANCHOR_VERIFIER_GREEN")
print("zero_sccs",len(comps),"cyclic_sccs",len(cyclic),"recurrent_cross",len(recurrent_cross))
print("transient_tail_positive",max(trans),max(tail))
print("pair_gain_lower",str(decfrac(CFIX,30,ROUND_FLOOR)))
print("rho60_gain",h60,"rhs",float(rhs60),"cap",CAP)
print("finite_61_199_min_gain",finite_min)
print("uniform_200_bridge_gain",uniform)
print("handoff_rho",HANDOFF,"ordinary_upper",handoff_upper)
print("bootstrap",BOOT,"ownership_graph",len(states),len(edges))
