#!/usr/bin/env python3
"""Independent RL332 red team: Kosaraju geometry and pairwise-consumer reconstruction."""
import contextlib, io, runpy
from collections import defaultdict
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(Path(__file__).with_name("verify_rl332_self_consistent_ownership.py")))
A=b["A"]; L=b["ELL"]; l2=b["l2lo"]; lam=b["LAM"]; full=b["full"]
states=b["states"]; edges=b["edges"]; phi=b["pot"]; boundary=b["b2"]
BOOT=32_550_361_322; CAP=BOOT-1
assert b["H"]==BOOT

fwd=defaultdict(list); rev=defaultdict(list); zero=[]
for s,t,z,k in edges:
    sig=phi[t]-phi[s]-(2*z-43*k); assert sig>=0
    if sig==0:
        zero.append((s,t,z,k)); fwd[s].append(t); rev[t].append(s)
seen=set(); order=[]
def d1(v):
    seen.add(v)
    for w in fwd[v]:
        if w not in seen:d1(w)
    order.append(v)
for v in range(len(states)):
    if v not in seen:d1(v)
seen.clear(); comps=[]
def d2(v,c):
    seen.add(v); c.append(v)
    for w in rev[v]:
        if w not in seen:d2(w,c)
for v in reversed(order):
    if v not in seen:
        c=[]; d2(v,c); comps.append(c)
co={v:i for i,c in enumerate(comps) for v in c}
cyc={i for i,c in enumerate(comps) if len(c)>1 or any(s==t and co[s]==i for s,t,_,_ in zero)}
assert len(comps)==288 and len(cyc)==16
low={v for v,s in enumerate(states) if s[0]=="N" and s[1]<=21}
assert all(phi[v]==0 for v in low)

cross=[e for e in zero if co[e[0]]!=co[e[1]]]
assert all(not(co[t] in cyc and co[s] not in cyc) for s,t,_,_ in cross)
rr=[e for e in cross if co[e[0]] in cyc and co[e[1]] in cyc]
assert len(rr)==195
internal=defaultdict(list)
for e in zero:
    s,t,z,k=e
    if co[s]==co[t] and co[s] in cyc: internal[s].append(e)
for s,t,z,k in rr:
    assert s in low and t not in low
    outs=internal[t]; assert outs
    assert all(u in low and z+k+z2+k2==45 for _,u,z2,k2 in outs)

dag=defaultdict(list); indeg=[0]*len(comps); arc=set()
for s,t,z,k in cross:
    c,d=co[s],co[t]; dag[c].append((d,k))
    if (c,d) not in arc: arc.add((c,d)); indeg[d]+=1
queue=[i for i,x in enumerate(indeg) if x==0]; topo=[]
while queue:
    c=queue.pop(); topo.append(c)
    for d in {x for x,_ in dag[c]}:
        indeg[d]-=1
        if indeg[d]==0: queue.append(d)
NEG=-10**9
tr=[0 if c not in cyc else NEG for c in range(len(comps))]
ta=[NEG]*len(comps)
for c in topo:
    for d,k in dag[c]:
        if c not in cyc and d not in cyc and tr[c]>NEG: tr[d]=max(tr[d],tr[c]+k)
        if c in cyc and d not in cyc: ta[d]=max(ta[d],k)
        elif c not in cyc and d not in cyc and ta[c]>NEG: ta[d]=max(ta[d],ta[c]+k)
assert max(tr)==3 and max(ta)==4

step=(45*A)%L; alpha=Fraction(step,L); assert 2*step<L
y=alpha*l2
c10=sum(y**j/factorial(j) for j in range(1,11))
c=Fraction(25_120_009_946_627,10**14)
assert c10>c

@lru_cache(None)
def W(K):
    s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return Fraction(K)+l2*s1/L+l2*l2*s2/(2*L*L)+l2**3*s3/(6*L**3)+l2**4*s4/(24*L**4)
def ks(r):
    K=(2*(L-r+1)-boundary+44)//45
    s=boundary-(2*(L-r+1)-45*K)
    return K,s
def S(K,h,s):
    actual=K+h; slack=45*h+s
    return Fraction(actual)+c*Fraction(actual-10*slack-7,4)
def mg(K,s):
    w=W(K); slope=S(K,1,s)-S(K,0,s)
    x=(S(K,0,s)-w)/(1-slope); q=max(0,x.numerator//x.denominator)
    return min((max(Fraction(h),S(K,h,s)-w),h) for h in {0,q,q+1} if h>=0)
K0,s0=ks(60); g,h=mg(K0,s0)
assert (h,g)==(10_239_722,Fraction(10_239_722))

def omit(n):
    return sum((Fraction(1<<((A*r)//L),3**r) for r in range(1,n+1)),Fraction())/lam
def base_rhs(r):
    K,_=ks(r); return 1+(full-omit(r-1))/3-W(K)/(12*lam)
assert base_rhs(60)-g/(12*lam)<BOOT
for r in range(61,200):
    K,s=ks(r); gg,hh=mg(K,s); assert base_rhs(r)-gg/(12*lam)<BOOT

HAND=3_607_000; Kmin,_=ks(HAND-1); ug,uh=mg(Kmin,44)
assert (uh,ug)==(10_239_542,Fraction(10_239_542))
assert base_rhs(200)-ug/(12*lam)<BOOT

prec=85
with localcontext() as ctx:
    ctx.prec=prec; ctx.rounding=ROUND_FLOOR
    term=Decimal(1); om=Decimal(0); prev=0
    for r in range(1,HAND):
        q=(A*r)//L; gap=q-prev
        term=term*Decimal(1<<gap)/Decimal(3); om+=term; prev=q
    ld=Decimal(lam.numerator)/Decimal(lam.denominator); om/=ld
    K,_=ks(HAND); w=W(K)
    wd=Decimal(w.numerator)/Decimal(w.denominator)/(Decimal(12)*ld)
with localcontext() as ctx:
    ctx.prec=prec; ctx.rounding=ROUND_CEILING
    fu=Decimal(full.numerator)/Decimal(full.denominator)
    upper=Decimal(1)+(fu-om)/Decimal(3)-wd
assert upper<Decimal(BOOT)

print("RL332_PAIRWISE_ANCHOR_RED_TEAM_GREEN")
print("sccs",len(comps),len(cyc),"recurrent_cross",len(rr),"tail",max(ta))
print("pair_constant_gt",float(c))
print("gains",h,uh)
print("handoff_upper",upper)
print("cap",CAP,"ownership",len(b["rows"]),len(b["large"]),len(states),len(edges))
