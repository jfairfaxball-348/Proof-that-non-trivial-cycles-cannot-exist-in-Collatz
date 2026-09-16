#!/usr/bin/env python3
"""Frozen independent RL340 red team."""
A=217_976_794_617;ELL=137_528_045_312;D=A-ELL;LOW=1<<71;UP=(1<<76)+(1<<36);L=51
def factors():
    cuts={0,ELL};cuts.update(((-D*j)%ELL) for j in range(L+1));reps=set()
    for c in cuts:
        if c<ELL:reps.add(c);reps.add(c+1) if c+1<ELL else None
    out=set()
    for r in reps:
        prev=(r+ELL-1)//ELL;w=[]
        for j in range(1,L+1):
            cur=(r+D*j+ELL-1)//ELL;w.append(1+cur-prev);prev=cur
        out.add(tuple(w))
    return out
def profs(p=6):
    out=[]
    def rec(a):
        if len(a)==p-1:
            q=tuple(a+[1])
            if all(q[i]<=q[i+1]+1 for i in range(p-1)):out.append(q)
            return
        for v in range(1,p-len(a)+1):rec(a+[v])
    rec([]);return out
def residue(g):
    suf=[0]*len(g);s=0
    for k in range(len(g)-1,-1,-1):suf[k]=s;s+=g[k]
    C=sum(3**k*(1<<suf[k]) for k in range(len(g)));m=3**len(g)
    return C*pow(1<<sum(g),-1,m)%m,m
def replay(x,g):
    for v in g:
        n=(1<<v)*x-1
        if n%3:return False
        x=n//3
        if not x&1:return False
    return True
rows=[];tc=0
for b in factors():
    for q in profs():
        e=(0,)+q+(0,);g=list(b)
        for off in range(7):
            i=22+off;g[i]+=e[off+1]-e[off]
            if g[i]<1:break
        else:
            tc+=1;r,m=residue(g);x=r+max(0,(LOW-r+m-1)//m)*m
            while x<UP:
                if x&1 and replay(x,g):rows.append(x)
                x+=m
def esc(x):
    d=0
    while x>=LOW:
        y=3*x+1;x=y//(y&-y);d+=1
    return d
assert len(factors())==52 and tc==684 and len(rows)==10 and len(set(rows))==10 and max(esc(x) for x in set(rows))==29
print('RL340_RED_TEAM_GREEN')
