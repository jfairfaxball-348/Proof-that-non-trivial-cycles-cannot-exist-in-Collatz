#!/usr/bin/env python3
"""RL340 fast verifier: exact q=0 (23,23,p=6) escape + consumer barrier."""
from fractions import Fraction
from functools import lru_cache
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LOW=1<<71; UP=(1<<76)+(1<<36); PAIR=(23,23); P=6
@lru_cache(None)
def factors(length):
    cuts=sorted({0,ELL,*(((-D*j)%ELL) for j in range(length+1))}); out=set()
    for a,b in zip(cuts,cuts[1:]):
        for r in {a,min(a+1,b-1)}:
            prev=(r+ELL-1)//ELL; gaps=[]
            for j in range(1,length+1):
                cur=(r+D*j+ELL-1)//ELL; gaps.append(1+cur-prev); prev=cur
            out.add(tuple(gaps))
    assert len(out)==length+1; return tuple(out)
@lru_cache(None)
def profiles(p):
    out=[]
    def rec(pref):
        i=len(pref)
        if i==p-1:
            q=tuple(pref+[1])
            if all(q[j]<=q[j+1]+1 for j in range(p-1)): out.append(q)
            return
        for v in range(1,p-i+1): rec(pref+[v])
    rec([]); return tuple(out)
def residue(gaps):
    c=0
    for j,g in enumerate(gaps): c=(1<<g)*c+3**j
    m=3**len(gaps); return c*pow(1<<sum(gaps),-1,m)%m,m
def reconstruct(x,gaps):
    st=[x]
    for g in gaps:
        y=(1<<g)*x-1
        if y%3:return None
        x=y//3
        if not(x&1):return None
        st.append(x)
    return tuple(st)
def candidates(gaps):
    r,m=residue(gaps); x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x&1:
            st=reconstruct(x,gaps)
            if st is not None: yield x,st
        x+=m
def templates(pair,p):
    left,right=pair; L=left+right+p-1
    for base in factors(L):
        for q in profiles(p):
            ext=(0,)+q+(0,); g=list(base); ok=True
            for off in range(p+1):
                pos=left-1+off; g[pos]+=ext[off+1]-ext[off]
                if g[pos]<1:ok=False;break
            if ok:yield tuple(g),q
def escape(x):
    for step in range(1001):
        if x<LOW:return step
        y=3*x+1; x=y//(y&-y)
    raise AssertionError
rows=[]; tc=0
for gaps,q in templates(PAIR,P):
    tc+=1
    for source,states in candidates(gaps): rows.append((source,states[29],q))
assert tc==684 and len(rows)==10
sources={r[0] for r in rows}; assert len(sources)==10
escapes=[escape(x) for x in sources]; assert max(escapes)==29
CURRENT_CAP=32_537_248_343; HIGH_CARRY=20_390_252_058; K60=6_251_274_783; LAM=1+Fraction(1,1<<40)
gap=CURRENT_CAP-HIGH_CARRY; required_gain=12*LAM*gap
assert gap==12_146_996_285 and required_gain>145_000_000_000 and required_gain>23*K60
assert 2*Fraction(46,91)==Fraction(92,91)
print('RL340_FAST_GREEN'); print('templates',tc,'rows',len(rows),'sources',len(sources),'max_escape',max(escapes)); print('carry_gap',gap,'candidate_status','UNPROMOTED')
