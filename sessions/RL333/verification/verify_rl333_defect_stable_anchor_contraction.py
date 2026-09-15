#!/usr/bin/env python3
"""RL333 verifier: low-slack anchor geometry, 7/4 defect charging, phase consumer, all-rho contraction."""
import contextlib, io, runpy
from collections import Counter, defaultdict
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    base=runpy.run_path(str(Path(__file__).with_name('verify_rl333_self_consistent_ownership.py')))
A=base['A']; ELL=base['ELL']; edges=base['edges']; states=base['states']; pot=base['pot']; b2=base['b2']
l2lo=base['l2lo']; LAM=base['LAM']; full=base['full']; rho59=base['rho59']
BOOT=32_548_554_425; CAP=BOOT-1
assert base['H']==BOOT and base['CAP']==CAP

sig_edges=[]
for s,t,z,k in edges:
    sigma=pot[t]-pot[s]-(2*z-43*k)
    assert sigma>=0
    sig_edges.append((s,t,z,k,sigma))
low={i for i,state in enumerate(states) if state[0]=='N' and state[1]<=21}
assert len(low)==21 and all(pot[v]==0 for v in low)
good=[e for e in sig_edges if e[4]<=2]
assert len(good)==614

adj=defaultdict(list)
for s,t,z,k,sg in good: adj[s].append(t)
stack=[]; on=set(); ind={}; lowlink={}; comps=[]; counter=0
def visit(v):
    global counter
    ind[v]=lowlink[v]=counter; counter+=1; stack.append(v); on.add(v)
    for w in adj[v]:
        if w not in ind:
            visit(w); lowlink[v]=min(lowlink[v],lowlink[w])
        elif w in on: lowlink[v]=min(lowlink[v],ind[w])
    if lowlink[v]==ind[v]:
        c=[]
        while True:
            w=stack.pop(); on.remove(w); c.append(w)
            if w==v: break
        comps.append(c)
for v in range(len(states)):
    if v not in ind: visit(v)
cyclic=[c for c in comps if len(c)>1 or any(s==t and s in c for s,t,_,_,_ in good)]
assert len(comps)==269 and len(cyclic)==1 and len(cyclic[0])==55
assert all(v in cyclic[0] for v in low)
non=[v for v in range(len(states)) if v not in low]
indeg={v:0 for v in non}; nadj=defaultdict(list)
for s,t,z,k,sg in good:
    if s in low or t in low: continue
    nadj[s].append(t); indeg[t]+=1
q=[v for v in non if indeg[v]==0]; topo=[]
while q:
    v=q.pop(); topo.append(v)
    for t in nadj[v]:
        indeg[t]-=1
        if indeg[t]==0: q.append(t)
assert len(topo)==len(non)==302

gout=defaultdict(list)
for e in good: gout[e[0]].append(e)
shapes=Counter()
for a in low:
    pending=[]
    for s,t,z,k,sg in gout[a]:
        if t in low: shapes[(sg,k,z+k)]+=1
        else: pending.append((t,sg,k,z+k))
    while pending:
        v,sg0,k0,r0=pending.pop()
        for s,t,z,k,sg in gout[v]:
            vals=(sg0+sg,k0+k,r0+z+k)
            if t in low: shapes[vals]+=1
            else: pending.append((t,*vals))
assert shapes==Counter({(0,2,45):240,(2,2,44):238,(1,1,22):21})

psi=[0]*len(states)
for iteration in range(len(states)+1):
    changed=False
    for s,t,z,k,sg in good:
        w=k-2*(1 if t in low else 0)
        if psi[s]+w>psi[t]: psi[t]=psi[s]+w; changed=True
    if not changed: break
else: raise AssertionError('positive good-path cycle')
assert iteration+1==2 and min(psi)==0 and max(psi)==4
assert all(psi[s]+k-2*(1 if t in low else 0)<=psi[t] for s,t,z,k,sg in good)

equality=[]
for s,t,z,k,sg in sig_edges:
    if sg>=3:
        assert 4*k+16<=7*sg
        if 4*k+16==7*sg: equality.append((s,t,z,k,sg))
assert len(equality)==9 and all(sg==4 and k==3 for s,t,z,k,sg in equality)

step=(45*A)%ELL
assert step==44_464_540_613
CFIX=Fraction(25_120_009_946_627,10**14)
def exp2_lower_num(pnum,terms=14):
    y=Fraction(pnum,ELL)*l2lo
    return sum(y**j/factorial(j) for j in range(terms+1))
def block_excess(m):
    vals=[]
    for j in range(m):
        x=(-j*step)%ELL
        vals.append(sum(exp2_lower_num((x+k*step)%ELL) for k in range(m))-m)
    return min(vals)
block=[Fraction(0)]+[block_excess(m) for m in range(1,9)]
for m in range(1,8): assert block[m]>=CFIX*max(0,m-1)
assert block[8]>=8*CFIX

@lru_cache(None)
def weighted(K):
    s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return Fraction(K)+l2lo*s1/ELL+l2lo**2*s2/(2*ELL**2)+l2lo**3*s3/(6*ELL**3)+l2lo**4*s4/(24*ELL**4)
def kbase_s0(rho):
    K=(2*(ELL-rho+1)-b2+44)//45
    s0=b2-(2*(ELL-rho+1)-45*K)
    assert 0<=s0<=44
    return K,s0
def structural(Kbase,h,s0):
    K=Kbase+h; S=45*h+s0
    return Fraction(K)+CFIX*Fraction(4*K-15*S-24,8)
def min_gain(Kbase,s0):
    W=weighted(Kbase)
    slope=structural(Kbase,1,s0)-structural(Kbase,0,s0)
    cross=(structural(Kbase,0,s0)-W)/(1-slope)
    q=max(0,cross.numerator//cross.denominator)
    vals=[(h,max(Fraction(h),structural(Kbase,h,s0)-W)) for h in {0,q,q+1} if h>=0]
    return min(vals,key=lambda row:row[1])
def omit_exact(last):
    return sum((Fraction(1<<((A*r)//ELL),3**r) for r in range(1,last+1)),Fraction())/LAM
def baseline_exact(rho):
    K,_=kbase_s0(rho)
    return 1+(full-omit_exact(rho-1))/3-weighted(K)/(12*LAM)

K0,s060=kbase_s0(60); h60,g60=min_gain(K0,s060)
assert K0==6_112_357_564 and s060==3
assert h60==31_922_482 and g60==31_922_482
rhs60=baseline_exact(60)-g60/(12*LAM)
assert rhs60<BOOT and rhs60.numerator//rhs60.denominator==CAP
finite_min=None
for rho in range(61,846):
    K,s0=kbase_s0(rho); h,g=min_gain(K,s0)
    finite_min=g if finite_min is None else min(finite_min,g)
    assert baseline_exact(rho)-g/(12*LAM)<BOOT
assert finite_min>=31_922_481

HANDOFF=11_242_132
KMIN,_=kbase_s0(HANDOFF-1)
struct_inc=structural(K0+1,0,0)-structural(K0,0,0)
w_inc_max=weighted(K0+1)-weighted(K0)
assert struct_inc>w_inc_max
hu,uniform=min_gain(KMIN,44)
assert hu==31_920_245 and uniform==31_920_245
assert baseline_exact(846)-uniform/(12*LAM)<BOOT

def decfrac(fr,prec,rounding):
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=rounding
        return Decimal(fr.numerator)/Decimal(fr.denominator)
def ordinary_upper(rho,prec=80):
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=ROUND_FLOOR
        term=Decimal(1); total=Decimal(0); prevq=0; d3=Decimal(3)
        for r in range(1,rho):
            qr=(A*r)//ELL; gap=qr-prevq
            term=term*Decimal(1<<gap)/d3; total+=term; prevq=qr
        lam=Decimal(LAM.numerator)/Decimal(LAM.denominator)
        omitted_lo=total/lam
        K,_=kbase_s0(rho); w=weighted(K)
        weighted_lo=Decimal(w.numerator)/Decimal(w.denominator)
        wdiv_lo=weighted_lo/(Decimal(12)*lam)
    full_up=decfrac(full,prec,ROUND_CEILING)
    with localcontext() as ctx:
        ctx.prec=prec; ctx.rounding=ROUND_CEILING
        return Decimal(1)+(full_up-omitted_lo)/Decimal(3)-wdiv_lo
assert ordinary_upper(HANDOFF-1)>Decimal(BOOT)
handoff_upper=ordinary_upper(HANDOFF)
assert handoff_upper<Decimal(BOOT)
assert rho59<BOOT

print('RL333_DEFECT_STABLE_ANCHOR_CONTRACTION_GREEN')
print('good_edges',len(good),'good_sccs',len(comps),'cyclic',len(cyclic),'cyclic_size',len(cyclic[0]))
print('first_return_shapes',dict(sorted(shapes.items())))
print('good_path_potential_range',min(psi),max(psi))
print('high_defect_equality_edges',len(equality))
print('phase_c',float(CFIX),'block8_excess',float(block[8]))
print('rho60_gain',h60,'rhs',float(rhs60),'cap',CAP)
print('finite_61_845_min_gain',finite_min)
print('uniform_846_bridge_gain',uniform)
print('handoff_rho',HANDOFF,'ordinary_upper',handoff_upper)
print('bootstrap',BOOT,'rows',len(base['rows']),'large',len(base['large']),'graph',len(states),len(edges))
