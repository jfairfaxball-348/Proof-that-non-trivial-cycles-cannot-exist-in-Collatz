#!/usr/bin/env python3
"""Independent RL333 red team: recompute low-slack geometry and contraction by separate routines."""
import contextlib, io, runpy
from collections import Counter, defaultdict, deque
from decimal import Decimal, localcontext, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    B=runpy.run_path(str(Path(__file__).with_name('verify_rl333_self_consistent_ownership.py')))
A=B['A']; L=B['ELL']; states=B['states']; edges=B['edges']; phi=B['pot']; b2=B['b2']
l2=B['l2lo']; lam=B['LAM']; full=B['full']; rho59=B['rho59']
BOOT=32_548_554_425; CAP=BOOT-1
assert (B['H'],B['CAP'],len(B['rows']),len(B['large']),len(states),len(edges),b2)==(BOOT,CAP,13558,7189,323,26514,129)

E=[]
for e in edges:
    s,t,z,k=e; sg=phi[t]-phi[s]-2*z+43*k
    if sg<0: raise AssertionError('negative slack')
    E.append((s,t,z,k,sg))
anchors={i for i,x in enumerate(states) if x[0]=='N' and x[1] in range(1,22)}
G=[e for e in E if e[-1]<=2]
assert len(G)==614

ga=defaultdict(list); gr=defaultdict(list)
for s,t,*_ in G: ga[s].append(t); gr[t].append(s)
seen=set(); order=[]
def dfs(v):
    seen.add(v)
    for w in ga[v]:
        if w not in seen: dfs(w)
    order.append(v)
for v in range(len(states)):
    if v not in seen: dfs(v)
seen=set(); comps=[]
def rdfs(v,c):
    seen.add(v); c.append(v)
    for w in gr[v]:
        if w not in seen: rdfs(w,c)
for v in reversed(order):
    if v not in seen:
        c=[]; rdfs(v,c); comps.append(c)
cyc=[]
for c in comps:
    C=set(c)
    if len(c)>1 or any(s==t and s in C for s,t,*_ in G): cyc.append(C)
assert len(comps)==269 and len(cyc)==1 and len(cyc[0])==55 and anchors<=cyc[0]

non=set(range(len(states)))-anchors
ind={v:0 for v in non}; out=defaultdict(list)
for e in G:
    s,t,z,k,sg=e
    if s in non and t in non:
        out[s].append(e); ind[t]+=1
q=deque(v for v in non if ind[v]==0); topo=[]
while q:
    v=q.popleft(); topo.append(v)
    for _,t,_,_,_ in out[v]:
        ind[t]-=1
        if ind[t]==0:q.append(t)
assert len(topo)==len(non)==302
suffix={v:Counter() for v in non}
for v in reversed(topo):
    for s,t,z,k,sg in [e for e in G if e[0]==v]:
        if t in anchors: suffix[v][(sg,k,z+k)]+=1
        else:
            for (sg2,k2,r2),n in suffix[t].items(): suffix[v][(sg+sg2,k+k2,z+k+r2)]+=n
sh=Counter()
for a in anchors:
    for s,t,z,k,sg in [e for e in G if e[0]==a]:
        if t in anchors: sh[(sg,k,z+k)]+=1
        else:
            for (sg2,k2,r2),n in suffix[t].items(): sh[(sg+sg2,k+k2,z+k+r2)]+=n
assert sh==Counter({(0,2,45):240,(1,1,22):21,(2,2,44):238})

P=[0]*len(states)
for _ in range(len(states)):
    upd=0
    for s,t,z,k,sg in reversed(G):
        cand=P[s]+k-(2 if t in anchors else 0)
        if cand>P[t]: P[t]=cand; upd+=1
    if not upd: break
else: raise AssertionError('positive cycle in good graph')
assert max(P)-min(P)==4
for s,t,z,k,sg in G: assert P[s]+k-(2 if t in anchors else 0)<=P[t]

bad=[e for e in E if e[-1]>=3]
assert bad and all(4*k+16<=7*sg for s,t,z,k,sg in bad)
tight=[e for e in bad if 4*e[3]+16==7*e[4]]
assert len(tight)==9 and Counter((e[4],e[3]) for e in tight)=={(4,3):9}

c=Fraction(25_120_009_946_627,10**14); step=(45*A)%L
def e2(p):
    y=Fraction(p,L)*l2
    return sum(y**j/factorial(j) for j in range(19))
mins={}
for m in range(1,9):
    vals=[]
    for j in range(m):
        x=(-j*step)%L
        vals.append(sum(e2((x+r*step)%L) for r in range(m))-m)
    mins[m]=min(vals)
    assert mins[m]>=c*max(0,m-1)
assert mins[8]>=8*c

@lru_cache(None)
def W(K):
    s1=K*(K+1)//2; s2=K*(K+1)*(2*K+1)//6; s3=s1*s1
    s4=K*(K+1)*(2*K+1)*(3*K*K+3*K-1)//30
    return Fraction(K)+l2*s1/L+l2**2*s2/(2*L**2)+l2**3*s3/(6*L**3)+l2**4*s4/(24*L**4)
def ks(rho):
    K=(2*(L-rho+1)-b2+44)//45; s=b2-(2*(L-rho+1)-45*K)
    return K,s
def st(K0,h,s0):
    K=K0+h; S=45*h+s0
    return Fraction(K)+c*Fraction(4*K-15*S-24,8)
def gain(K0,s0):
    w=W(K0); s=st(K0,1,s0)-st(K0,0,s0)
    x=(st(K0,0,s0)-w)/(1-s); q=max(0,x.numerator//x.denominator)
    cand=[]
    for h in range(max(0,q-1),q+3): cand.append((max(Fraction(h),st(K0,h,s0)-w),h))
    return min(cand)
def omit(n): return sum((Fraction(1<<((A*r)//L),3**r) for r in range(1,n+1)),Fraction())/lam
def base(rho):
    K,_=ks(rho); return 1+(full-omit(rho-1))/3-W(K)/(12*lam)
K0,s0=ks(60); g60,h60=gain(K0,s0)
assert (h60,g60)==(31_922_482,Fraction(31_922_482))
assert base(60)-g60/(12*lam)<BOOT
fm=None
for rho in range(61,846):
    K,s0=ks(rho); g,h=gain(K,s0); fm=g if fm is None else min(fm,g)
    assert base(rho)-g/(12*lam)<BOOT
assert fm>=31_922_481
HAND=11_242_132; Km,_=ks(HAND-1); gu,hu=gain(Km,44)
assert (hu,gu)==(31_920_245,Fraction(31_920_245))
assert base(846)-gu/(12*lam)<BOOT

def dfrac(x,rounding):
    with localcontext() as C:
        C.prec=90; C.rounding=rounding
        return Decimal(x.numerator)/Decimal(x.denominator)
def ordinary(rho):
    with localcontext() as C:
        C.prec=90; C.rounding=ROUND_FLOOR
        t=Decimal(1); sm=Decimal(0); pq=0; three=Decimal(3)
        for r in range(1,rho):
            qq=(A*r)//L; t=t*Decimal(1<<(qq-pq))/three; sm+=t; pq=qq
        dl=Decimal(lam.numerator)/Decimal(lam.denominator)
        om=sm/dl; k,_=ks(rho); ww=W(k)
        wd=(Decimal(ww.numerator)/Decimal(ww.denominator))/(Decimal(12)*dl)
    fu=dfrac(full,ROUND_CEILING)
    with localcontext() as C:
        C.prec=90; C.rounding=ROUND_CEILING
        return Decimal(1)+(fu-om)/Decimal(3)-wd
up=ordinary(HAND)
assert up<Decimal(BOOT) and rho59<BOOT
print('RL333_RED_TEAM_GREEN')
print('good_edges',len(G),'sccs',len(comps),'first_returns',dict(sorted(sh.items())))
print('potential_range',min(P),max(P),'tight_high_defect',len(tight))
print('phase8',float(mins[8]),'rho60_gain',h60,'finite_min',fm,'uniform',hu)
print('handoff',HAND,'ordinary_upper',up,'cap',CAP)
