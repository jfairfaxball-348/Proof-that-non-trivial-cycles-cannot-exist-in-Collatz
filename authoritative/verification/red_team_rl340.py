#!/usr/bin/env python3
"""Independent RL340 red team for the promoted (23,23,p=6) certificate."""
from functools import lru_cache
A=217_976_794_617; ELL=137_528_045_312; D=A-ELL
LOW=1<<71; UP=(1<<76)+(1<<36); LEFT=23; RIGHT=23; P=6; L=51
def factor_words(length):
    cuts={0,ELL}; cuts.update(((-D*j)%ELL) for j in range(length+1)); reps=set()
    for c in sorted(cuts):
        if c<ELL:
            reps.add(c)
            if c+1<ELL:reps.add(c+1)
    out=set()
    for r in reps:
        prev=(r+ELL-1)//ELL; word=[]
        for j in range(1,length+1):
            cur=(r+D*j+ELL-1)//ELL; word.append(1+cur-prev); prev=cur
        out.add(tuple(word))
    assert len(out)==length+1; return out
@lru_cache(None)
def q_profiles(p):
    ans=[]
    def walk(pref):
        if len(pref)==p-1:
            q=tuple(pref+[1])
            if all(q[i]<=q[i+1]+1 for i in range(p-1)):ans.append(q)
            return
        for v in range(1,p-len(pref)+1):walk(pref+[v])
    walk([]); return ans
def all_templates():
    for base in factor_words(L):
        for q in q_profiles(P):
            ext=(0,)+q+(0,); g=list(base)
            for off in range(P+1):
                idx=LEFT-1+off; g[idx]+=ext[off+1]-ext[off]
                if g[idx]<1:break
            else:yield tuple(g),q
def direct_residue(gaps):
    suffix=[0]*len(gaps); s=0
    for k in range(len(gaps)-1,-1,-1):suffix[k]=s;s+=gaps[k]
    C=sum((3**k)*(1<<suffix[k]) for k in range(len(gaps))); m=3**len(gaps)
    return (C*pow(1<<sum(gaps),-1,m))%m,m
def replay(x,gaps):
    st=[x]
    for g in gaps:
        num=(1<<g)*x-1
        if num%3:return None
        x=num//3
        if x%2==0:return None
        st.append(x)
    return st
rows=[];tc=0
for gaps,q in all_templates():
    tc+=1; r,m=direct_residue(gaps); x=r+max(0,(LOW-r+m-1)//m)*m
    while x<UP:
        if x%2:
            st=replay(x,gaps)
            if st is not None:rows.append((x,st[29],q))
        x+=m
def escape(x):
    d=0
    while x>=LOW and d<=1000:
        y=3*x+1;x=y//(y&-y);d+=1
    assert x<LOW;return d
sources={x for x,_,_ in rows}; depths=[escape(x) for x in sources]
assert len(factor_words(L))==52 and tc==684 and len(rows)==10 and len(sources)==10 and max(depths)==29
print('RL340_RED_TEAM_GREEN'); print('factors',52,'templates',tc,'rows',len(rows),'sources',len(sources),'max_escape',max(depths))
